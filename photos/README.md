# PHOTOS — your bird photography workspace

This is the registered image workspace. It follows the folder convention used by
the vendored `image-production` plugin (`plugins/image-production/`), so those
commands and skills work here without reconfiguration.

## Drop photos here first

```
photos/inbox/          <-- drag everything off the memory card into here
```

Then run the ingest script (below). Nothing else needs touching.

## The folders

| Folder | What lives there |
|---|---|
| `inbox/` | Everything off the card. Unsorted, temporary, expected to be empty |
| `01-source/` | Originals, filed by capture date. **Never edited in place** |
| `02-working/` | Culls in progress, layered files (PSD, XCF, TIFF), Lightroom exports |
| `03-selects/` | The keepers. A frame only gets here if you'd print it at 12×18 |
| `04-exports/instagram/` | Feed and Reel exports at exact pixel sizes |
| `04-exports/print/` | 300dpi TIFF/JPEG for printing |
| `04-exports/web/` | Site and portfolio versions |
| `references/` | Style references, palette, the style guide PDF |
| `thumbnails/` | Small previews for quick indexing |
| `logs/` | Ingest log and your outing / species log |

## Ingest

```bash
python3 scripts/ingest.py              # see what it would do
python3 scripts/ingest.py --run        # actually move files
python3 scripts/ingest.py --run --copy # copy instead of move (safer)
```

It files by capture date taken from EXIF (falls back to file date), names
collisions safely, and writes thumbnails where it can. Canon CR3/CRAW originals
can't be previewed without extra tooling — they'll be filed and skipped for
thumbnails. That's expected.

## Export sizes — the ones that matter

From the crop system in `photography-account/BRAND-KIT.md`:

| Use | Ratio | Pixels |
|---|---|---|
| Tight portrait | 4:5 | 2160 × 2700 |
| Environmental / animalscape | 3:2 | 2700 × 1800 |
| Flight / action | 16:9 | 2700 × 1519 |
| Detail / macro | 1:1 | 2160 × 2160 |
| Reels | 9:16 | 2160 × 3840 |
| Carousel cover | **always 4:5** | 2160 × 2700 |
| Print | any | 300 dpi |

## The pipeline this folder is built for

1. **Ingest** — card → `inbox/` → `01-source/YYYY-MM-DD/`
2. **Cull** — rating in `02-working/`; three passes: sharp → keeper → portfolio
3. **Edit** — apply the style (see `photography-account/STYLE-DIRECTIONS.md`)
4. **Select** — `03-selects/`. If you wouldn't print it at 12×18, it stops here
5. **Export** — exact sizes above, IPTC copyright filled in on every file
6. **Post** — 3 a week: Tue / Thu / Sun, 7–8pm IST, plus a Reel on Friday

## Two rules

- **Never commit photographs.** `photos/.gitignore` ignores everything here
  except this README. Originals live on a drive with a backup, not in git.
- **Never edit `01-source/`.** If a frame needs work, it gets copied forward
  into `02-working/`. The original stays untouched, forever.

## Getting photos in — if drag-and-drop or chat upload fails

Image attachments do not always reach the agent. The path that always works is
through git, because the agent can pull:

1. Open the repo on GitHub and switch to the branch `arena/01a0cde6-instagram-agent-skill`
2. Navigate into `photos/inbox/`
3. **Add file → Upload files**, drag your photo in, commit
4. Tell the agent: "pull the photo"

The agent runs `git pull`, then `python3 scripts/ingest.py --run` to file it by
date. This handles files far larger than chat attachments, and the photo is
backed up on GitHub the moment it lands.

## Applying the styles

```bash
python3 -m venv .svenv && .svenv/bin/pip install pillow numpy reportlab
.svenv/bin/python scripts/styles.py photos/01-source/2026-11-08/IMG_1234.jpg
```

Writes one JPEG per style into `photos/02-working/styles/` plus a
`__STYLE-COMPARISON.pdf` contact sheet. See `scripts/styles.py` for what it
approximates and what it cannot do.
