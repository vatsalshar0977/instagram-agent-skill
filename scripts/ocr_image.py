#!/usr/bin/env python3
"""Read text out of screenshots (Lightroom UI, Instagram posts, articles).

Installed because the sandbox has no OCR binary and tesseract cannot be
apt-installed. rapidocr-onnxruntime is pure pip and ships its own models.

    python3 -m venv /home/user/.svenv
    /home/user/.svenv/bin/pip install rapidocr-onnxruntime "opencv-python-headless<5"

Usage:
    ocr_image.py IMAGE [IMAGE ...]           text with positions
    ocr_image.py IMAGE --sort                reading order (top to bottom)
    ocr_image.py IMAGE --min-conf 0.8        drop weak detections
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="+")
    ap.add_argument("--sort", action="store_true",
                    help="print in reading order instead of detection order")
    ap.add_argument("--min-conf", type=float, default=0.0)
    args = ap.parse_args()

    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        print("missing: pip install rapidocr-onnxruntime 'opencv-python-headless<5'",
              file=sys.stderr)
        return 2

    engine = RapidOCR()
    for p in args.images:
        path = Path(p)
        if not path.exists():
            print(f"{p}: not found", file=sys.stderr)
            continue
        img = Image.open(path).convert("RGB")
        result, _ = engine(np.asarray(img))
        print(f"=== {path.name} ({img.size[0]}x{img.size[1]}) ===")
        if not result:
            print("  (no text detected)")
            continue
        rows = []
        for box, text, conf in result:
            ys = [b[1] for b in box]
            xs = [b[0] for b in box]
            rows.append((min(ys), min(xs), conf, text))
        if args.sort:
            rows.sort(key=lambda r: (round(r[0] / 12), r[1]))
        for y, x, conf, text in rows:
            if conf < args.min_conf:
                continue
            if args.sort:
                print(f"  {text}")
            else:
                print(f"  y{int(y):4d} x{int(x):4d}  {conf:.2f}  {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
