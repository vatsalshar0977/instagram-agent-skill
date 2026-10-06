# THE FLYWAY GLYPH

## First, the honest bit

It's not an ancient symbol and it's not an existing logo — **I designed it for you** in this session, and I've now built it as real vector and raster files. That means it means whatever you decide it means. Below is the meaning I designed it *around*, plus five other readings you can adopt instead if one of them sits better.

---

## What the three lines signify

### The primary reading: a flock climbing

Three strokes, parallel, rising to the right. Not birds drawn as birds — birds drawn as *motion*: the trail a flock leaves as it lifts off and climbs away from you.

**Why three, specifically:**
- **One** stroke is a bird.
- **Two** is a pair — it reads as a relationship, a couple.
- **Three** is the smallest number that reads as *many*. It's the minimum for a flock, and the minimum for rhythm. Four starts to look like a pattern; five looks like wallpaper.

Three is also the only count where your eye can still see all of them individually at 32 pixels. Which matters, because that's the size it has to survive as a profile photo.

### What the geometry is doing

| Element | Value | What it carries |
|---|---|---|
| **Angle of climb** | 22–24° | The angle a bird actually leaves a perch — shallow, not vertical. It's the angle of departure, not of flight |
| **Three parallel strokes** | offset along a perpendicular axis | They never touch, at any size. Three birds, not a zigzag |
| **Thickness taper** | 0.78 → 0.88 → 1.00 | The far stroke is lightest, the near stroke heaviest. **Recession** — the flock is going away from you and slightly up |
| **Stagger** | each stroke offset along the flight path | Suggests sequence: one after another, not side by side |

So the mark contains a direction (up and right), a distance (the taper), and a time (the stagger). That's a lot of meaning for three lines.

---

## Five other readings — pick one, or none

You don't have to explain your mark to anyone. But if you ever do, here are five that fit:

1. **The flyway.** The route itself. Nalsarovar sits on the Central Asian Flyway — the mark is the path the migrants take over Gujarat, rising and heading out. This is the reading that ties to your strongest brand story.
2. **The three seasons of your year.** Arrival (November), peak (December–January), departure (February–March). Your shooting calendar as a mark.
3. **The arc of a morning.** Dark and setting up → first light → the bird arrives. The three beats of every shoot you do, and the exact structure of your Reel Format C ("The Wait").
4. **Three patches.** Indroda, Thol, Nalsarovar — the three places you'll actually build the body of work from. Very specific, very yours, and it changes meaning as you add locations.
5. **Three frames.** Portrait, environmental, detail — the repeating rhythm of your feed. Reads as intentional design rather than nature.

My recommendation: **the flyway** as the official meaning (it's the most ownable and the hardest for anyone else to claim), with the morning-arc as a private second reading.

---

## The three variants

| Variant | Aspect | Use | Why |
|---|---|---|---|
| **Mark** | 2.8 : 1 | Watermark corners, captions, headers | Wide enough to feel like a path, compact enough for a corner |
| **Stack** | 1.7 : 1 | Profile photo, print chop, app icon | Nearly square — fills a circle or square without awkward empty space |
| **Winged** | 4.8 : 1 | Large use only — print titles, website header | Each stroke becomes a shallow chevron, so they read as wings. **Never below 100px** — the chevrons close up |

---

## Geometry (if you ever need to redraw it)

```
angle of climb      22° (mark variant) / 24° (stack)
stroke length       L
offset along flight 0.45 L   (stagger = sequence)
offset perpendicular 0.50 L  (spacing = the flock spreads)
thickness taper     0.78 / 0.88 / 1.00  (far → near)
stroke weight       8.5% of glyph height  (17% for the avatar)
```

The strokes are placed on a **perpendicular axis**, not stacked vertically — that's the fix that keeps them from merging into a single blob at small sizes. Verified: 3 separate connected components at 512px, 110px, 48px and 32px.

---

## Files

| File | What it is |
|---|---|
| `flyway-glyph.svg` / `-black.svg` | Master vector, Mark variant — scale to anything |
| `flyway-glyph-stack.svg` | Master vector, Stack variant |
| `flyway-glyph-chop.svg` | Glyph inside a ring — your print chop |
| `flyway-glyph-white.png` | Transparent, 512px tall — watermarks on dark photos |
| `flyway-glyph-black.png` | Transparent, 512px tall — watermarks on light photos |
| `flyway-glyph-ember.png` | Transparent, Ember `#C97B3C` — accents only |
| `flyway-glyph-stack.png` | Transparent, square-ish variant |
| `flyway-glyph-winged.png` | Chevron variant, large use only |
| `flyway-glyph-chop.png` | 1000px black-on-transparent, ringed — blind emboss on prints |
| `flyway-glyph-lockup.png` | "VS" + glyph lockup, bone on slate |
| **`profile-glyph-640.png`** | **Ready to upload as your profile photo** |
| `profile-glyph-320.png` | Small version |
| `profile-glyph-640-ring.png` | With a Sand ring |
| `test-glyph-32px.png` / `-48px` / `-110px` | Legibility tests at true pixel size |
| **`Flyway-Glyph-Asset-Sheet.pdf`** | All variants, sizes and specs on one page |

Rebuild everything: `python3 build_glyph.py` (needs `pillow`, `reportlab`).

---

## How to use it

**Watermark (two-point, the crop-resistant method):**
- Glyph top-left at 4% margin, 12% opacity, 28–40px tall on a 2000px export
- Handle bottom-right at 2.5% margin, 12% opacity, Inter uppercase tracking 150
- Crop one corner, the other survives

**Profile photo:** upload `profile-glyph-640.png` as-is. It's already 640×640, Slate field, Bone glyph, and it holds three separate strokes down to 32px.

**Print chop:** `flyway-glyph-chop.png` — blind emboss (no ink, just pressure) on the lower-right of a print, or foil it in Sand. No text. That's the fine-art convention, and it's the thing that makes a print feel signed rather than stamped.

**Never:** Ember on Slate (not enough contrast) · the Winged variant under 100px · stretching the aspect ratio · rotating it.
