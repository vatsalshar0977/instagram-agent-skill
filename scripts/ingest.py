#!/usr/bin/env python3
"""
Ingest photos from photos/inbox/ into photos/01-source/YYYY-MM-DD/.

Files by EXIF capture date (falls back to file mtime), avoids collisions,
writes thumbnails where possible, and logs everything.

    python3 scripts/ingest.py                 # dry run
    python3 scripts/ingest.py --run           # move files
    python3 scripts/ingest.py --run --copy    # copy instead of move
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "photos" / "inbox"
SOURCE = ROOT / "photos" / "01-source"
THUMBS = ROOT / "photos" / "thumbnails"
LOGS = ROOT / "photos" / "logs"

PHOTO = {".cr3", ".craw", ".cr2", ".raw", ".arw", ".nef", ".dng", ".raf", ".orf",
         ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".webp"}
VIDEO = {".mp4", ".mov", ".m4v"}

# formats ImageMagick can usually open for a preview
PREVIEWABLE = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".heic", ".dng"}


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def exif_date(path: Path) -> str | None:
    """Return YYYY-MM-DD from EXIF, or None."""
    if have("exiftool"):
        try:
            out = subprocess.run(
                ["exiftool", "-s3", "-DateTimeOriginal", "-SubSecDateTimeOriginal",
                 "-CreateDate", str(path)],
                capture_output=True, text=True, timeout=30).stdout.strip().splitlines()
            for line in out:
                line = line.strip()
                if len(line) >= 10 and line[:4].isdigit():
                    d = line[:10].replace(":", "-")
                    datetime.strptime(d, "%Y-%m-%d")
                    return d
        except Exception:
            pass
    if have("identify"):
        try:
            out = subprocess.run(
                ["identify", "-format", "%[EXIF:DateTimeOriginal]", str(path)],
                capture_output=True, text=True, timeout=30).stdout.strip()
            if len(out) >= 10 and out[:4].isdigit():
                d = out[:10].replace(":", "-")
                datetime.strptime(d, "%Y-%m-%d")
                return d
        except Exception:
            pass
    return None


def file_date(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")


def unique(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix, parent = dest.stem, dest.suffix, dest.parent
    n = 2
    while True:
        cand = parent / f"{stem}-{n}{suffix}"
        if not cand.exists():
            return cand
        n += 1


def thumbnail(src: Path, dest_dir: Path) -> bool:
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / f"{src.stem}.jpg"
    if out.exists():
        return False
    if have("convert"):
        try:
            subprocess.run(["convert", str(src), "-thumbnail", "400x400>", str(out)],
                           capture_output=True, timeout=120)
            if out.exists() and out.stat().st_size > 0:
                return True
        except Exception:
            pass
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true", help="actually move/copy files")
    ap.add_argument("--copy", action="store_true", help="copy instead of move")
    ap.add_argument("--inbox", default=str(INBOX))
    args = ap.parse_args()

    inbox = Path(args.inbox)
    if not inbox.exists():
        print(f"No inbox at {inbox}")
        return 1

    files = sorted(p for p in inbox.rglob("*")
                   if p.is_file() and p.suffix.lower() in PHOTO | VIDEO
                   and not p.name.startswith("."))
    if not files:
        print("Inbox is empty. Drop your card contents into photos/inbox/")
        return 0

    LOGS.mkdir(parents=True, exist_ok=True)
    log = LOGS / "ingest.log"
    moved = thumbs = skipped = 0
    verb = "Copying" if args.copy else "Moving"

    print(f"{'DRY RUN — ' if not args.run else ''}{verb} {len(files)} file(s)\n")
    for f in files:
        ext = f.suffix.lower()
        date = exif_date(f) or file_date(f)
        date += "  (EXIF)" if exif_date(f) else "  (file date)"
        target_dir = SOURCE / (date.split()[0])
        target = unique(target_dir / f.name)
        kind = "video" if ext in VIDEO else "photo"
        print(f"  {f.name:38s} -> 01-source/{target_dir.name}/   [{kind}]")

        if args.run:
            target_dir.mkdir(parents=True, exist_ok=True)
            try:
                if args.copy:
                    shutil.copy2(str(f), str(target))
                else:
                    shutil.move(str(f), str(target))
                moved += 1
                with log.open("a") as fh:
                    fh.write(f"{datetime.now().isoformat(timespec='seconds')}\t"
                             f"{f.name}\t{target.relative_to(ROOT)}\n")
            except Exception as e:
                print(f"    FAILED: {e}")
                skipped += 1
                continue

            src = target if args.copy else target
            if ext in PREVIEWABLE:
                thumbs += 1 if thumbnail(src, THUMBS / target_dir.name) else 0
            elif ext in PHOTO:
                print("    (RAW — no preview without extra tooling; filed anyway)")

    print()
    if args.run:
        print(f"Filed {moved} · thumbnails {thumbs} · failed {skipped}")
        if not args.copy:
            for d in sorted(inbox.rglob("*"), reverse=True):
                if d.is_dir() and not any(d.iterdir()):
                    d.rmdir()
    else:
        print("Dry run only. Re-run with --run to file them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
