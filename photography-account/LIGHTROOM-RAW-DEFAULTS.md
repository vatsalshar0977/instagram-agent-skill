# Why raw files change on import — and how to control it

*Written 2026-10-24, prompted by `IMG_6879.CR3`. Measurements are from that file.
Applies to Lightroom Classic. The same Raw Defaults preference is shared with Adobe
Camera Raw and Lightroom (cloudy) — change it in one and it changes in all three
[17](https://kevinlisota.photography/2021/12/lightroom-profile-sharpening-noise-reduction-and-lens-profile-defaults-for-nikon-z9/).*

---

## 1. The short answer

Nothing changed about your photograph. **You were never looking at the raw data before
import.** You were looking at a JPEG your camera made.

Every raw file contains two things: the linear sensor data, and an embedded JPEG preview
that the camera rendered using its own settings — Picture Style, contrast, saturation,
white balance, highlight tone priority, noise reduction and lens corrections all baked in.
The camera LCD, Windows Photos, macOS Preview/Quick Look, Finder thumbnails and even
Lightroom's own import dialog all show you that JPEG.

Lightroom then throws the camera's rendering away and builds its own from the sensor data.
Different profile, different tone curve, no lens corrections. Hence the jump.

---

## 2. Measured on IMG_6879.CR3

I extracted the camera's embedded preview from your file and compared it with a neutral
raw render of the same data. Side-by-side image: `edits/IMG_6879__camera-vs-raw.jpg`.

| | camera preview (what you saw) | neutral raw render | |
|---|---|---|---|
| Saturation | 18.1 | 13.4 | **−26%** |
| Black point (p5) | 4.3% | 15.5% | lifted |
| Highlights (p95) | 56.9% | 87.8% | stretched |
| Warm/cool (R−B) | −9.4 | −10.4 | near identical |
| Contrast (sd) | 14.1 | 19.4 | |

Two honest caveats on that table:

- Part of the brightness/highlight gap comes from the decoder auto-stretching the raw
  (LibRaw's `no_auto_bright`). Adobe does not stretch the same way. Running it without
  auto-bright gives brightness 23.6% / highlights 30.2% — i.e. the raw data has no baked
  tone curve at all, and every renderer invents its own. That is the whole problem in one
  number.
- **The saturation gap and the black-point lift are not artifacts.** They are real
  differences between Canon's rendering and a neutral one.

---

## 3. The six things that cause it

1. **Profile.** Lightroom defaults to **Adobe Color** — a universal profile built to look
   the same across all camera brands. It is not Canon's Picture Style, and it is not
   trying to be [16](https://lightroomkillertips.com/customizing-camera-raw-defaults-in-lightroom-classic/).
2. **Adobe deliberately zeroes most sliders.** The default is a flat, consistent *starting
   point* — contrast and saturation left low so there is room to edit, and so files from
   different bodies match each other [15](https://blog.adobe.com/en/publish/2020/06/16/streamline-edits-with-the-improved-raw-defaults).
3. **Lens corrections are off by default.** Your camera corrected vignetting, distortion
   and chromatic aberration in-body before writing the preview. Lightroom's "Enable
   Profile Corrections" and "Remove Chromatic Aberration" are both unchecked on import, so
   corners look darker and straight lines bow.
4. **Adobe's own Detail panel defaults** are applied to raw files only (never to JPEG):
   sharpening **40 / radius 1.0 / detail 25 / masking 0**, colour noise reduction **25**,
   luminance noise reduction 0
   [14](https://www.digitalcameraworld.com/tutorials/how-to-change-lightroom-classics-default-sharpening-and-noise-settings).
5. **"Apply auto tone adjustments"** — if this is ticked in Preferences → Presets,
   Lightroom also auto-sets exposure and contrast on import, which shifts the look again.
   Worth checking; it is easy to leave on by accident.
6. **The two-stage preview.** During import Lightroom shows the *camera's* embedded
   preview because it is instant, then re-renders with its own engine a moment later. That
   visible "snap" is the change people notice most — and it is not a setting, it is just
   the render catching up.

Not on the list, and worth ruling out: a bad or missing monitor ICC profile will make
Lightroom look different from other apps for reasons that have nothing to do with raw
processing.

---

## 4. How to get the original look back

### Option A — the one-setting fix: **Camera Settings**

**Windows:** `Edit > Preferences > Presets` · **macOS:** `Lightroom Classic > Settings >
Presets` — then under **Raw Defaults**, set **Master** to **Camera Settings**
[13](https://helpx.adobe.com/lightroom-classic/desktop/help/raw-defaults.html).

Lightroom reads the Picture Style out of the file's EXIF and picks the matching **Camera
Matching** profile — shoot Standard and you get Camera Standard, shoot Monochrome and the
file imports in black and white
[15](https://blog.adobe.com/en/publish/2020/06/16/streamline-edits-with-the-improved-raw-defaults).

Be clear about what this does and doesn't do:

- It is **Adobe's simulation** of Canon's Picture Style, not Canon's own code. Usually
  close, sometimes not [12](https://www.dpreview.com/forums/thread/4638153).
- On most bodies (the Nikon Z series is the exception) it **only changes the profile** —
  every other slider stays at Adobe Default
  [16](https://lightroomkillertips.com/customizing-camera-raw-defaults-in-lightroom-classic/).
  So your lens corrections are *still* off.
- If the setting isn't recognised, it silently falls back to Adobe Default.

### Option B — the right fix: freeze your own starting point

Do this once, properly:

1. Open one representative file.
2. **Profile** → pick *Camera Standard* (closest to Canon's Standard Picture Style) or
   *Camera Faithful* / *Camera Neutral* if you shot one of those.
3. **Lens Corrections** → tick **Enable Profile Corrections** and **Remove Chromatic
   Aberration**.
4. Set sharpening and noise reduction to your taste (their defaults of 40 / 1.0 / 25 are a
   reasonable starting point for a 24 MP file).
5. `Develop > Set Default Settings` → **Update to current settings**.

Or set it up as a named develop preset and choose **Raw Defaults > Master > Preset**. The
fallback order is: your preset → Camera Settings → Adobe Defaults
[15](https://blog.adobe.com/en/publish/2020/06/16/streamline-edits-with-the-improved-raw-defaults).

You can also set defaults **per camera model, per serial number, and per ISO** — useful if
you ever add a second body with a different rendering character.

### Option C — fixing photos you already imported

**Raw Defaults only applies at import.** Changing the preference does nothing to images
already in the catalogue
[17](https://kevinlisota.photography/2021/12/lightroom-profile-sharpening-noise-reduction-and-lens-profile-defaults-for-nikon-z9/).

For existing files: select them in Grid or Filmstrip, then

- `Develop > Reset Settings` (or `Cmd/Ctrl + Shift + R`) to fall back to the current
  defaults, or
- paste your new default/preset across the selection.

### If you want the literal camera rendering as a file

- **Canon Digital Photo Professional (DPP)** — free with the camera — renders CR3 exactly
  as Canon intends. Use it as the reference when you want to know "what the camera meant."
- Or **shoot RAW+JPEG** and keep the JPEG alongside; that is the camera's rendering as an
  actual file rather than a buried preview.
- Building previews as **Embedded & Sidecar** on import shows the camera look in the grid
  immediately (it is literally reading the camera JPEG), but Lightroom re-renders with its
  own engine as soon as you zoom in.

---

## 4b. Which one should you actually pick — Adobe or Camera Settings?

**Keep Adobe. And switch the profile from Adobe Color to Adobe Neutral.**

I tested this rather than guessing. `IMG_6879.CR3` was rendered two ways — a neutral
render standing in for an Adobe base, and the camera's own JPEG standing in for a
camera-look base — then the *identical* Dust & Dawn preset was applied to both:

| | from neutral base | from camera-look base | divergence |
|---|---|---|---|
| Brightness | 54.5% | 39.2% | **−28%** |
| Contrast (sd) | 19.1 | 13.9 | **−27%** |
| Saturation | 15.4 | 22.1 | **+44%** |

Image: `edits/IMG_6879__preset-drift.jpg`.

That is the whole argument. **A preset is not a look — it is a set of moves applied to a
floor.** Change the floor and the same moves land somewhere else
[7](https://aaapresets.com/en-gb/blogs/fix-lightroom-preset-problems-step-by-step-troubleshooting/adobe-color-vs-camera-matching-profiles-decoding-presets-for-stellar-photos-in-2026).

### Why Adobe, for this account

- **Determinism.** The real problem with *Camera Settings* is not that camera profiles look
  bad — it is that the base becomes **a function of whatever Picture Style was set that
  day**. Leave it on Landscape and your blues and greens come in pre-pushed; switch to
  Faithful for a day and they don't. Your preset then renders differently for reasons that
  have nothing to do with the photo. Adobe profiles are sensor-invariant: same floor, every
  file, every body [8](https://fotolab.app/blog/adobe-color/).
- **Adobe Neutral suits this work specifically.** It reduces saturation *and* contrast for
  the flattest starting point and the most headroom, and it is the one Adobe recommends for
  images with **tricky blues and gradients**
  [9](https://jkost.com/blog/2024/07/the-power-of-profiles-in-lightroom-classic.html)
  [10](https://www.goaskerin.com/tutorials/lightroom/jump-start-your-editing-with-new-easy-to-use-profiles-in-lightroom-classic/).
  `IMG_6879` is 78% azure with sky gradients — that is the exact use case. Adobe Color, the
  default, adds a small amount of contrast and warmth to reds, yellows and oranges
  [9](https://jkost.com/blog/2024/07/the-power-of-profiles-in-lightroom-classic.html), which
  is aimed at people and landscapes, not birds.
- **This is a cheap decision to reverse.** Profiles are nondestructive, can be switched at
  any time, and don't move a single slider
  [9](https://jkost.com/blog/2024/07/the-power-of-profiles-in-lightroom-classic.html)
  [11](https://lightroom.adobe.com/academy/editing/black-and-white/lightroom-profile-essentials).
  So this is about workflow efficiency, not getting it permanently right.

### When Camera Settings is the right call

- You shoot with a **deliberate** Picture Style and want it honoured (e.g. monochrome in
  camera to visualise).
- High-volume work where matching the out-of-camera JPEG *is* the deliverable (events,
  weddings, second shooters).
- You've compared and simply prefer Canon's colour. In that case choose **Camera Faithful**
  or **Camera Neutral** deliberately as a named profile and lock it — the point is not
  "camera profiles are bad", it is "the floor must not move".

### The one rule that matters more than the choice

**Set the base once, then build every preset on top of it, and never change it again.**
Changing raw defaults later silently re-renders every preset you built earlier. That is the
usual reason a preset "stops working" six months on.

---

## 5. My recommendation for this account

Do **not** chase the camera preview as your permanent look.

The camera JPEG is a lossy, baked rendering made for a 3-inch LCD. Your raw file from
`IMG_6879` has **0.03% blown highlights and 0.00% crushed shadows** — real headroom that
the camera's own preview throws away by committing to a contrast curve. Matching the LCD
means matching a preview.

The professional version of this question is: **freeze a known starting point, then build
your look on top of it.** Concretely:

1. Set the raw default once (Option B) — Camera Standard profile + lens corrections on,
   everything else neutral. Same starting point for every file, every time.
2. **Then** build the nine house styles (`STYLE-DIRECTIONS.md`) as develop presets on top
   of that fixed base.

The order matters. If you change your raw defaults later, every preset you built earlier
renders differently — which is the usual reason a preset "stops working" months down the
line. Set the floor once, then build upward.

---

## 6. Related files

- `edits/IMG_6879__camera-vs-raw.jpg` — the visual proof, both renderings side by side
- `edits/NOTES-IMG_6879.md` — measured properties of this frame and the style edits
- `STYLE-DIRECTIONS.md` — the nine house styles that should become presets
- `scripts/styles.py` — the style engine used to produce the comparisons
