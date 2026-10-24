# IMG_6879.CR3 — measured, then edited

**File:** `photos/IMG_6879.CR3` · Canon CR3 · 6022 × 4024 (3:2, uncropped) · 25.7 MB
**Date processed:** 2026-10-24

> **Honesty note.** I cannot see the photograph in this session — every statement below is
> measured from the pixels, not observed. If a description conflicts with what you see,
> trust your eyes and tell me; the numbers are real, the interpretation is inference.
> The RAW is demosaiced with LibRaw (`rawpy`) at camera white balance and a default tone
> curve. That is a neutral, honest starting point, but it is **not** Lightroom's rendering —
> no lens corrections, no CA removal, no camera-matching profile.

---

## 1. What the pixels say

| property | value | reading |
|---|---|---|
| Brightness | mean 71.2% · median 76.8% | bright, airy frame |
| Range | p1 9.9% → p99 89.8% | full range present |
| **Clipping** | **blown 0.03% · crushed 0.00%** | **huge editing headroom** — nothing to rescue |
| Contrast | sd 19.4 | flat, as expected in open light |
| Saturation | mean 13.5 | low |
| Dominant hue | **azure 78%**, blue 8%, cyan 5% | sky or water fills most of the frame |
| Light falloff | top 76.7% · middle 74.0% · bottom 62.9% | brighter up top — consistent with sky |
| **Subject vs ground** | **subject 44.1% vs background 72.6% (−28.5)** | **dark bird on a bright field** |
| Subject position | x 78%, y 70% of frame | lower right, off-centre |
| Subject size | ~4.9% of frame | small in frame |
| Background busyness | sd 17.7 | moderately busy, not clean bokeh |
| White balance | R−B = −10.4 | cool light |

**The character of this frame:** a small, dark subject sitting in a large, bright, cool,
azure field, with a full tonal range and zero clipping. In practice that means **the edit is
about separation, not recovery** — there is nothing blown to pull back and nothing crushed
to lift. The one real job is to get the bird to read against a background that is 28 points
brighter than it is.

---

## 2. My pick: Dust & Dawn, tuned to this frame

`edits/IMG_6879__BEST-dust-dawn-4x5.jpg` (3000 px · 4:5)

Three changes were made *for this photograph*, off the back of the measurements:

1. **4:5 crop centred on the detected subject**, placing it on the right third. At 4.9% of
   frame the bird is too small to carry a 3:2 — the crop is the single biggest improvement
   available here.
2. **Tight subject mask** (radius 0.14 of the long edge, default is 0.30). The default mask
   is sized for a bird filling a third of the frame; on a 4.9% subject it bleeds into the
   background and the local edits stop being local.
3. **Contrast added, not removed.** Dust & Dawn is a low-contrast style by design, but this
   frame is *already* flat (sd 19.4). Applying the preset as written dropped it to 13.4 —
   visibly greyer. Shadows were also left almost flat (0.05 instead of 0.28), because lifting
   shadows on a dark bird against bright sky pulls the bird toward the sky and destroys the
   very separation the frame depends on.

### The sweep that decided it

Four variants, all with the 4:5 crop and the tight mask, measured on the same crop:

| variant | shadows / contrast / clarity | subject lift | subject | bg | **separation** | **detail in subject** | global sd | sat |
|---|---|---|---|---|---|---|---|---|
| A | 0.10 / 0.10 / 0.02 | +0.30 | 26.3 | 56.3 | −30.1 | 23.01 | 17.7 | 13.7 |
| **B (chosen)** | **0.05 / 0.16 / 0.06** | **+0.20** | **23.3** | **56.7** | **−33.4** | **24.32** | **19.1** | **15.4** |
| C | 0.15 / 0.06 / 0.00 | +0.40 | 28.5 | 56.1 | −27.7 | 21.77 | 16.6 | 12.8 |
| D (preset as written) | 0.28 / −0.12 / −0.08 | +0.00 | 31.7 | 54.8 | −23.1 | 16.89 | 13.4 | 10.7 |

B wins on both things that matter: the strongest subject/background separation (−33.4, better
than the untouched file's −43.1 but with far more detail in the bird) and the most detail
inside the subject (24.32 vs 16.89 for the preset as written). It also holds global contrast
at 19.1 against the original's 19.4 — it does not flatten the frame.

Note what D shows: the preset applied straight lifts the bird's average from ~30 to 31.7
*while losing* nearly a third of its internal detail. That is the classic backlit mistake —
brightening the subject instead of separating it.

---

## 3. All nine, on this frame

`edits/IMG_6879__STYLE-COMPARISON.pdf` — cover page is the recommended edit, then all nine.

Measured on this file (saturation · brightness · contrast · warm/cool):

| style | sat | bright | contrast | R−B | on this frame |
|---|---|---|---|---|---|
| *original* | *13.4* | *71.2* | *19.4* | *−10.4* | |
| Dust & Dawn | 10.3 | 55.0 | 11.2 | −6.1 | **the house style; needs the crop + contrast fix above** |
| Slate & Ember | 4.1 | 57.2 | 14.4 | −1.5 | starved — only 13.5 sat in the file to begin with |
| Portra Restraint | 9.9 | 60.5 | 10.1 | −6.5 | wants warm light; this frame is cool |
| High-Key Mist | 9.1 | 71.0 | 12.9 | −7.0 | **natural fit** — the frame is already high-key |
| Nocturne | 16.8 | 52.6 | 14.8 | −9.7 | wrong tool — fights a 71% bright frame |
| Halo | 14.5 | 56.2 | 8.5 | −9.1 | **built for backlit; run it if you want the rim-light look** |
| Platinum | 3.3 | 66.8 | 19.5 | +1.5 | **holds the most contrast** — strongest B&W candidate |
| Cyanotype | 4.6 | 67.8 | 18.2 | −2.1 | largely redundant — the frame is 78% azure already |
| Graphic | 10.8 | 73.5 | 22.6 | −6.6 | **highest contrast (22.6)** — the van Oosten read; needs clean bg |

**Suited to this frame:** Dust & Dawn (tuned), High-Key Mist, Halo, Graphic, Platinum.
**Working against it:** Nocturne, Slate & Ember, Cyanotype.

If you only look at two, look at **BEST (Dust & Dawn tuned)** and **Graphic** — same crop,
opposite philosophies: one keeps the air and the silence, the other commits to the bird as a
shape in a clean field.

---

## 4. What I'd change with your eyes on it

- **The crop is a guess.** 4:5 assumes a perched or standing bird. If it's in flight, say so
  and I'll redo it as 16:9 or a wider 3:2 with the bird on a horizontal third.
- **The subject mask is a sharpness heuristic**, not a real subject selection. It assumes the
  bird is the sharpest thing in the frame. On a big azure field that is nearly always true,
  but the debug masks are written next to the outputs (`_mask_*.png`) — check them, and if
  the mask has drifted onto background detail, tell me and I'll reposition it by hand.
- **Background busyness is 17.7** — not clean. If there is clutter behind the bird, Graphic
  will expose it; Dust & Dawn's dehaze and soft grain will hide some of it.

---

## 5. Reproducing / re-running

```bash
# one-time (dot-venvs don't survive snapshot restores)
python3 -m venv /home/user/.svenv && /home/user/.svenv/bin/pip install pillow numpy reportlab rawpy

# all nine, full frame, 3000 px
/home/user/.svenv/bin/python scripts/styles.py photos/IMG_6879.CR3 \
    --out photos/02-working/styles --max-width 3000

# the recommended edit
/home/user/.svenv/bin/python scripts/styles.py photos/IMG_6879.CR3 \
    --out photos/02-working/best --only "Dust & Dawn" --crop 4:5 \
    --subject-radius 0.14 --max-width 3000 \
    --set "shadows=0.05,contrast=0.16,clarity=0.06" --boost-subject 0.20

# any other style, same treatment
/home/user/.svenv/bin/python scripts/styles.py photos/IMG_6879.CR3 \
    --out photos/02-working/best --only "Graphic" --crop 4:5 \
    --subject-radius 0.14 --max-width 3000
```

`--crop` accepts `3:2`, `4:5`, `16:9`, `1:1` and always positions the largest window of that
ratio so the detected subject lands on the thirds line on the side it already favours.
`--set` overrides any numeric field on any style.

---

## 6. Housekeeping

`IMG_6879.CR3` is **25.7 MB and it is committed to git**. One or two is survivable; a card's
worth is not. Two options:

- **Preferred:** drop RAWs into `photos/inbox/` and never commit them — `photos/.gitignore`
  already excludes everything under `photos/`, and `scripts/ingest.py` files them by date
  without git ever seeing them.
- Or set up **Git LFS** for `*.CR3` if you want the RAWs versioned alongside the edits.

Nothing under `photos/` is committed by design; the review copies in `edits/` are.
