# EDITING STYLE & BRAND — Vatsal Sharma, Bird Photography (Canon R8)

---

# STEP 1 — RESEARCH STATUS (read this first)

**What I verified:**
- `@mathiphotography`: Instagram and Threads both refuse automated access (HTTP 403). The only publicly indexed trace is a **Threads account with the display line "Photographers of Threads" posting bird content** — including a migration-themed post [1](https://www.threads.com/@mathiphotography/post/C7skDjhRRr-). That is the complete verifiable footprint. I have **no** follower count, grid, posting pattern or caption data, and I will not guess them.
- **Your three attached images did not reach this workspace** (no `/home/user/uploads/`, no image files on disk). I could not identify or analyze those photographers.

**What that means for Step 2:** I've written it at **genre level** — the dominant, observable patterns across bird photography on Instagram — clearly labelled as such. The moment you get me the images or the handles, I'll redo it per-account with specifics.

**What Steps 3 and 4 do not depend on:** anything. They're built for *you* — your camera, your light, your locations. Those are complete and ready to use.

---

# STEP 2 — ANALYSIS

## 2A. What the genre does (bird photography on Instagram, not these specific accounts)

Treat this as the baseline you're differentiating *from*.

**Colour grading**
- Warm golden-hour grade as the default; temperature pushed 5,800–6,800K
- High contrast, crushed blacks (Blacks −30 to −50), punchy midtone microcontrast
- Teal-and-orange split toning: cool shadows, warm highlights
- Vibrance and Saturation both pushed positive — vivid, candy-adjacent
- Green and yellow often left at or near default → neon grass, radioactive bokeh

**Mood and tone**
- Moody-dark or bright-and-punchy; very little in between
- Rarely any restraint — the feed is an arms race of saturation
- Almost no film-like highlight rolloff; highlights clipped or recovered hard

**Background treatment**
- Maximum blur, long-lens compression, busy bokeh often accepted
- Heavy vignette (−25 and beyond) used as a "look"
- Background colour rarely controlled — whatever was there, stays there

**Composition and framing**
- Tight portraits dominate; the bird fills 60–90% of frame
- Eye-level, rule of thirds, gaze into the frame
- 4:5, 1:1 and 3:2 mixed within one feed
- Environmental frames (bird small in habitat) are rare — maybe 1 in 15 posts

**Sharpness, texture, detail**
- Global Clarity +20 to +40, Texture +20 to +40 → crunchy halos on feather edges
- Oversharpened: Radius 1.2–1.5, Amount 70–100, Masking near 0
- Noise reduction over-applied at high ISO → plastic, smeared feathers

**Feed consistency**
- Strong per-photographer consistency in *subject*, weak consistency in *grade*
- Most feeds shift colour over time as presets get updated

**Watermark, logo, profile**
- Bottom-right corner, semi-transparent, script or geometric sans
- Corner placement = trivially cropped out
- Profile photo: usually a bird portrait crop or a logo

**Captions, hashtags, patterns**
- Species name + location + EXIF, then 15–30 hashtags
- Daily posting, or bursts after a trip
- Almost no ambient sound, almost no sound design in Reels

## 2B. What nobody is doing — the gaps you can own

These are my strategic reads. Ranked by how ownable they are for *you* specifically.

1. **Temperature separation.** Everyone separates subject from background with *blur*. Almost nobody separates with *colour temperature*. Making the bird the only warm object in a cool frame is a signature you can own outright.
2. **Restraint.** The genre is maxed on saturation, clarity and contrast. A quiet, film-like grade — lifted blacks, rolled highlights, net desaturation — reads as *art* next to a feed of candy-coloured birds. This is the single biggest visual gap.
3. **Environmental frames.** Tight portraits dominate. Bird-in-landscape at 1/3 frame height is what people actually hang on a wall, and almost nobody shoots it for Instagram. Print buyers want room-scale images.
4. **Backlit translucency.** Most shoot front-lit for maximum sharpness. Glowing feathers, rim light, halo — rare, difficult, and instantly recognisable.
5. **Seasonal identity.** One preset forever = static feed. A grade that breathes with the Gujarat season (cool slate Nov–Feb migration, warm ochre pre-monsoon) gives you a living feed and a story.
6. **Place as brand.** Flyway. The Rann. Indroda. Almost no Indian bird photographer brands *place* — they brand "bird photography," which is a commodity.
7. **High-key negative space.** Dark and moody is saturated as a look. Clean, bright, misty frames with the bird small are underused and stop the scroll precisely because they're quiet.

**I'll firm this up into a proper per-photographer comparison once I can see your references.**

---

# STEP 3 — YOUR SIGNATURE STYLE

## 3.1 The concept

# DUST & DAWN
### *The temperature-separation look*

**One line:** *Cool, desaturated habitat — the bird is the only warm thing in the frame.*

Named for Gujarat's two colours: the mineral dust of the dry months and the cold blue of a November dawn on the flyway. It's built on one idea that most bird photographers never touch:

> **Blur separates the bird from the background locally. Colour temperature separates it globally — across the whole frame, and at thumbnail size.**

The mechanism, in one sentence: **you cool and desaturate everything that isn't the bird, and warm and texturise everything that is.** That's a −12 temp / −18 saturation radial on the background, and a +10 temp / +18 texture brush on the subject. The eye reads "warm thing = important thing" before it reads anything else.

**The seven rules:**

1. **Background cool.** Teal/slate in the shadows, greens and cyans −30 to −45 saturation.
2. **Subject neutral-to-warm.** 300–500K warmer than the background. No exceptions.
3. **Net desaturation.** Vibrance +8, Saturation −6. The constraint is the style.
4. **Film curve.** Lifted blacks, rolled-off highlights, low global contrast. Prints like a dream, looks nothing like HDR.
5. **Grain always.** 18–28. It's a print, not a screenshot.
6. **Local, not global, texture.** Texture goes on the bird. Clarity goes *negative* on the background.
7. **One warm accent per frame.** Eye, beak, or legs. Exactly one carries the ember.

**Signature palette**

| Role | Name | Hex |
|---|---|---|
| Background dominant | Slate | `#16232A` |
| Background secondary | Sage Grey | `#7C8B84` |
| Habitat light | Sand | `#D9C7A7` |
| Subject accent | Ember | `#C97B3C` |
| Highlight / paper | Bone | `#F2EBE0` |

Rule: **maximum two hues per frame.** If a third appears, kill it in HSL. That single discipline does more for feed cohesion than any preset.

---

## 3.2 LIGHTROOM CLASSIC / CC WORKFLOW — exact values

Starting point: a Canon R8 RAW/CRAW file from golden hour, ISO 400–1600, exposed to the right.

### Panel 1 — Basic

| Control | Value | Why |
|---|---|---|
| Profile | **Adobe Neutral** (or camera-matching "Neutral") | Adobe Standard oversaturates reds and greens; Neutral is the honest base |
| Temperature | **5650K** as a starting point | Adjust to taste, then use locals for the separation |
| Tint | **+6** | Canon files almost always need +5 to +10 magenta to kill the green cast |
| Exposure | **−0.15** *(after exposing right in camera)* | Pull back from ETTR for clean shadows |
| Contrast | **−12** | Shape comes from the curve, not this slider |
| Highlights | **−55** | Protects white feather detail — this is where most edits die |
| Shadows | **+28** | Opens habitat shadow without going milky |
| Whites | **+12** | Keeps the specular sparkle in the eye |
| Blacks | **−18** | Deep but not crushed. **Never below −30** |
| Texture | **+12** | Feather micro-detail |
| Clarity | **−8** | Negative global = soft, filmic. Clarity gets added back locally on the bird |
| Dehaze | **+6** | Slight atmosphere removal. **Never above +15** — it turns skies into grey leather |
| Vibrance | **+8** | |
| Saturation | **−6** | The net-desaturation signature |

### Panel 2 — Tone Curve

**Parametric:** Highlights −10 · Lights −5 · Darks +8 · Shadows −6

**Point curve (RGB), four moves:**
- Lift the black point: `input 0 → output 14` (film base — nothing is truly black)
- Soften the shoulder: `input 255 → output 245`
- Gentle mid S-curve: `(64, 58)` · `(128, 132)` · `(192, 196)`

**Per-channel split (this is the DUST & DAWN* engine):**
- **Blue channel:** lift shadows — `input 32 → output 40`; drop highlights — `input 224 → output 218`
- **Red channel:** lift midtones — `input 128 → output 132`
- **Green channel:** tiny dip in shadows — `input 48 → output 44`

### Panel 3 — HSL

| Colour | Hue | Sat | Lum |
|---|---|---|---|
| Red | 0 | −6 | +8 |
| Orange | −4 | **−10** | **+12** |
| Yellow | −8 | **−30** | +6 |
| Green | +6 | **−45** | −12 |
| Aqua | 0 | **−35** | −6 |
| Blue | −6 | −20 | −14 |
| Purple | 0 | −25 | 0 |
| Magenta | 0 | −20 | 0 |

Green and Yellow are where the amateur look lives. −45 on green is not a typo.

### Panel 4 — Colour Grading

| Zone | Hue | Sat | Luminance |
|---|---|---|---|
| Shadows | **210** (cool slate/teal) | **10** | −4 |
| Midtones | **38** (warm sand) | 6 | 0 |
| Highlights | **48** (cream) | 5 | +2 |
| Global | 40 | 4 | 0 |

**Blending 50 · Balance −8** — the negative balance biases the grade toward the shadows, which is where your background lives.

### Panel 5 — Effects

| Control | Value |
|---|---|
| Grain Amount | **22** |
| Grain Size | **40** |
| Grain Roughness | **55** |
| Post-Crop Vignette | **−10** |
| Vignette Midpoint | **55** |
| Vignette Feather | **65** |

### Panel 6 — Detail / Sharpening

| Control | Value | Note |
|---|---|---|
| Sharpening Amount | **45** | |
| Radius | **1.0** | Above 1.4 = white halos on feather edges |
| Detail | **25** | |
| **Masking** | **55–70** | Hold Alt while dragging — only feather edges should be white |
| Noise Reduction Luminance | **12–20** | **Never above 25** — it smears feather structure |
| Noise Reduction Colour | 10 | |
| Noise Reduction Detail | 50 | |
| Lens Corrections | Remove CA on; Profile corrections on | Essential for backlit work |

### Panel 7 — Local adjustments (this *is* the look)

Four masks. Do these and the preset is irrelevant.

**Mask 1 — Background** (Select Subject → Invert, or a linear/radial gradient)
`Temp −12 · Saturation −18 · Clarity −20 · Dehaze −8 · Texture −20`
→ Cool, soft, slightly hazy habitat.

**Mask 2 — The bird** (Select Subject)
`Temp +10 · Exposure +0.15 · Texture +18 · Clarity +8 · Dehaze +6`
→ Warm, crisp subject. This is the 300–500K differential.

**Mask 3 — The eye**
`Exposure +0.25 · Clarity +25 · Sharpening +20`
Plus a 3–4px dodge brush on the catchlight at `Exposure +0.35`.

**Mask 4 — Separation halo** (small radial behind the bird's head)
`Temp +15 · Exposure +0.10`
→ A hint of warmth behind the head. Subtle; nobody should notice it's there.

**Result to check for:** background reads cool and low-saturation; the bird is the only warm, textured object. If you desaturate everything equally, you've made a flat photo, not a DUST & DAWN frame.

### Lightroom Mobile (free) — same look

The free mobile app now includes **Select Subject** masking, so the whole system works:
1. Light panel: apply every Basic value above (same numbers).
2. Curves: tap the curve icon → use the RGB point curve; add the blue-channel shadow lift via the channel selector.
3. Colour: HSL and Colour Grading panels accept the same values.
4. Effects: Grain 22 / Vignette −10.
5. Masking → **Select Subject**: apply Mask 2 values. Tap **Invert** → apply Mask 1 values. Brush → eye, Mask 3.
6. Detail: Sharpening 45, Masking 60, Noise Reduction 15.

### Snapseed alternative (no Lightroom)

| Step | Tool | Values |
|---|---|---|
| 1 | Tune Image | Brightness +8 · Contrast −12 · Saturation −12 · Ambiance +20 · Highlights −35 · Shadows +22 · Warmth −6 |
| 2 | Curves | Film preset, then custom: lift the black point slightly, soften the top |
| 3 | Selective → background | Saturation −25 · Temperature −10 · Structure −20 |
| 4 | Selective → bird | Structure +15 · Saturation +6 · Warmth +8 |
| 5 | Selective → eye | Brightness +25 · Structure +25 |
| 6 | Details | Sharpening +25 · Structure −5 |
| 7 | Grainy Film | Grain +20 · Style Strength 25 |
| 8 | Vignette | −12, inner brightness neutral |
| 9 | Dodge & Burn | +25 on the catchlight |

Snapseed's weakness: no global HSL. Compensate with Selective on the greenest area at Saturation −30.

---

## 3.3 VARIATIONS

Apply **on top of** the base. Deltas only.

**1 · Golden hour (your default)**
`Temp +150 (→ 5800) · Highlights −65 · Shadows +35 · Orange Sat −5 / Lum +15 · Grain 25 · Vignette −8`
Add a warm glow radial behind the subject: `Temp +12 · Exposure +0.15`.

**2 · Overcast / flat light**
`Temp +100 · Contrast −20 · Dehaze +12 · Shadows +40 · Blacks −10 · Saturation −10 · Texture +8 · Colour Grading Shadows Sat 10`
Overcast is your friend for soft, even feather detail — lean into the low contrast.

**3 · Backlit / rim-lit**
`Exposure −0.20 · Highlights −75 · Shadows +45 · Dehaze −6 (keep the glow — do not dehaze it away) · Texture +20 on rim feathers · Grain 28`
Add a radial **behind** the head: `Exposure +0.25 · Blacks −20` — burn the background down so the rim light reads.
Turn on **remove chromatic aberration** and manual defringe; backlit edges will fringe purple/green.

**4 · Dark forest / low light / pre-dawn**
`Exposure +0.30 · Shadows +55 · Blacks −8 · Noise Reduction Luminance 25 · Clarity −15 · Dehaze +8 · Colour Grading Shadows Sat 14 / Hue 210 · Grain 30 · Vignette −14`
At ISO 6400+, keep Noise Reduction Detail at 55 to protect feather texture.

**5 · Water birds (Thol, Nalsarovar — reflections)**
`Dehaze +10 · Contrast −8 · Blue Sat −25 / Lum −18 · Texture +10 local on water ripple`
Compose for the reflection: place the waterline at the lower third, or dead centre for a mirror frame. Crop 1:1 or 5:4. If the reflection is near-perfect, a vertical flip symmetry crop is a showpiece — use it once a season, not often.

**6 · Birds in flight**
`Exposure +0.10 · Shadows +20 · Highlights −40 · Clarity −12 · Texture +18 (wings) · Sharpening Masking 35 (lower than base, so wing edges catch) · Grain 18`
Crop tighter than feels right — a flying bird needs the frame filled. Shoot 1/3200 minimum.

---

## 3.4 MAKING THE BIRD POP — eight moves, in priority order

1. **Temperature differential: 300–500K.** The strongest separation tool you have. Background −12, subject +10.
2. **Luminance separation: ½ to 1 stop.** The bird should sit brighter than its background. Check with the colour picker — keep the subject between 55% and 75% luminance.
3. **Background desaturation −18 to −25.** A busy, colourful background fights the bird even when it's blurred.
4. **Local clarity inversion.** Background −20, subject +8. This is what makes the bird feel three-dimensional.
5. **Move your body.** Before you edit, fix it in camera: 30 cm left or right often turns a busy background into a clean one. Increase subject-to-background distance; shoot wide open.
6. **The eye.** Sharp eye + visible catchlight beats every other technical factor. Check at 100% before export. If the eye is soft, the frame is a record shot.
7. **Underexpose backlit subjects by ⅔ stop in camera**, then lift the bird locally in post. Far cleaner than recovering a blown sky.
8. **Clean your edges.** Scan all four edges for intruding branches and clone them out — a stray twig across a corner destroys an otherwise perfect frame.

---

## 3.5 A COHESIVE FEED

**Crop ratio:** **4:5 portrait for every feed post.** It takes ~25% more screen area than square. 9:16 for Reels covers. Pick one and never deviate — mixed ratios are the fastest way to look like a hobbyist.

**Palette discipline:** 60% slate/sage backgrounds · 30% sand/khaki · 10% ember accent. Two hues per frame, maximum.

**The rhythm — post in threes, repeating:**
1. Tight portrait (bird fills 70–90%)
2. Environmental frame (bird ~⅓ of frame height, habitat visible)
3. Detail or action (feather texture, takeoff, a beak, a wing)

**The checkerboard rule:** never let two adjacent grid posts share the same background temperature. Alternate cool-background and warm-background frames. This is what makes a grid read as *designed* at thumbnail size.

**Cadence:** 3 posts a week — **Tue / Thu / Sun, 7–8pm IST**, plus one Reel on Friday.

**Batch discipline:** apply the preset, then allow yourself **three moves per image** — Exposure, Temperature, and one local mask. Restraint is what makes nine frames look like one author.

**The thumbnail test:** before posting, view the grid at 25% zoom. If you can't tell what the bird is in under a second, crop tighter. Instagram is judged at thumbnail size, and edited at full size.

---

## 3.6 PRESET RECIPE (reusable)

| Preset name | Purpose |
|---|---|
| `D&D — 00 Base` | Everything in §3.2, no locals. Apply first, always. |
| `D&D — 01 Golden` | Base + variation 1 |
| `D&D — 02 Overcast` | Base + variation 2 |
| `D&D — 03 Backlit` | Base + variation 3 |
| `D&D — 04 Forest` | Base + variation 4 |
| `D&D — 05 Water` | Base + variation 5 |
| `D&D — 06 Flight` | Base + variation 6 |
| `D&D — BG Cool` | **Mask-only preset** — Mask 1 values, for applying the background cool-down to any image |
| `D&D — Subj Warm` | **Mask-only preset** — Mask 2 values |
| `D&D — Print` | Base with Grain 12, Sharpening 55 / Radius 0.8 / Masking 70, Vignette −6. Output-sharpened for 300dpi. |

**Build order for a new image:** `00 Base` → variation preset → `BG Cool` (inverted subject mask) → `Subj Warm` (subject mask) → eye brush → export.

Save the two mask-only presets as **local** presets and the whole workflow takes about 90 seconds a frame.

---

## 3.7 MISTAKES TO AVOID

| Mistake | Limit | What it looks like |
|---|---|---|
| Crushed blacks | Blacks **> −30** | Dead shadows, HDR look, no detail in dark plumage |
| Over-clarity | Clarity **< +25** global | White halos on feather edges, "crunchy" |
| Over-dehaze | Dehaze **< +15** | Skies become grey leather, all atmosphere gone |
| Candy colour | Saturation **< +10**, Vibrance **< +25** | Amateur, and it prints badly |
| Global texture | Texture only locally | Background noise and grain mush |
| Oversharpening | Radius **< 1.4**, Amount **< 70**, Masking **55+** | Outlined feathers, white edges |
| Over noise reduction | Luminance **< 25** | Plastic, smeared feathers — worse than the noise |
| Neon habitat | Green Sat **−45**, Yellow Sat **−30** | Radioactive grass |
| Heavy vignette | **> −25** is 2014 | Dated, obvious |
| Fake grain | Grain **< 35** | Reads as a filter, not as film |
| Editing on a phone screen | Calibrate; check on two displays | Everything you post looks black on other people's screens |
| Mixed presets per post | One base, forever | No authorship — the feed looks like three different people |

**The one-line test:** if someone can tell you edited it, you over-edited it.

---

# STEP 4 — BRANDING & COPYRIGHT

## 4.1 Profile photo

**The test that matters:** it must read at **110px** in the grid and survive at **32px** in a comment thread. Most profile photos are designed at 400px and fail at both.

**What works, ranked:**

1. **A bird eye, extreme macro, filling the circle** ← **my recommendation.** It's already circular, it's high contrast, and it's unmistakably a bird photographer at 32px with zero text. Fill 80% of the circle with the eye; put the pupil dead centre.
2. **Monogram** — "VS" or "V", thin stroke, letter-spaced, on slate. Clean, but says "designer," not "photographer."
3. **You in the field** — a silhouette with the R8, low horizon, lots of sky. Best for print authorship, weakest at small size.

**Spec:** Background `#16232A` · subject/text `#F2EBE0` · a 2px `#D9C7A7` ring at the outer edge · no text below 40px equivalent · **no stroke thinner than 2px** · no collages · no busy multi-bird images.

**Test it:** zoom to 32px and squint. If you can't tell what it is, it failed.

## 4.2 Watermark

**First, an honest trade-off.** Earlier in this project I told you not to watermark — because feature accounts (the hub reposts that are your main growth lever) skip watermarked images. That tension is real. My recommendation for where you are now:

- **Instagram feed:** the **Quiet Mark** at 10–12% opacity, or nothing at all. Growth first.
- **Website, print files, portfolio exports:** the **Plate Mark**. Protection where it counts.
- **Always, on every file:** IPTC metadata. That's the part that actually holds up.

### The rules

| Property | Value |
|---|---|
| Text | `@vatsalsharma.photo` (findable) or `VATSAL SHARMA` (timeless) |
| Height | **1.5–2% of the long edge** — on a 2000px export, ~30–40px cap height |
| Opacity — dark images | **12–18% white** (`#FFFFFF`) |
| Opacity — light images | **15–22% black** (`#1A1A1A`) |
| Blend | Normal, with a **1px soft shadow at 20%** for legibility on mixed backgrounds |
| Placement | Bottom-right, **2.5% margin** from both edges, in the flattest, blurriest area |
| Font | Geometric sans, uppercase, **tracking +150 to +200** — Inter, Avenir Next, Montserrat. **Never a script** (illegible small) and **never black weight** (distracting) |

### Anti-crop strategy

A corner watermark is gone in two seconds with the crop tool. Three defences, in order of effectiveness:

1. **Place it inside the subject zone**, not the extreme corner — over blurred background *near* the bird. Cropping it out means cutting the bird.
2. **Two-point mark.** A tiny glyph top-left + the handle bottom-right. Cropping one corner leaves the other. This is the most practical defence on social.
3. **Metadata.** IPTC Copyright Notice + Creator fields in every exported file, EXIF preserved. The visible mark is *deterrence*; the metadata is *evidence*. Register anything you sell.

## 4.3 THREE CONCEPTS TO CHOOSE FROM

### Concept 1 — THE QUIET MARK
*Bottom-right. `@VATSALSHARMA.PHOTO` in Inter uppercase, tracking 150, 14% white, with a 24px hairline rule floating above it.*

Gallery-minimal. Disappears into the frame until someone looks for it. Safest for feature-account reposts. Weakest anti-crop protection. **Use this on the Instagram feed.**

### Concept 2 — THE FLYWAY GLYPH
*Top-left: a 1.5px-stroke mark of three ascending strokes — a flock in migration, abstracted. Bottom-right: the handle in small caps at 12%.*

Two-point placement makes it genuinely crop-resistant, and the glyph becomes your maker's chop — it can stand alone on prints, embossed or blind-debossed, with no text at all. Strongest brand asset of the three. Ties directly to the Central Asian Flyway story. **My recommendation as your primary identity.**

### Concept 3 — THE PLATE MARK
*Centred at the bottom, in Cormorant Garamond italic at 12%: `Vatsal Sharma · Halcyon · Thol, 2026` — a museum wall label, with edition numbers on prints.*

Reads as an art object rather than social content, which is exactly right for selling prints. Weakest theft deterrence, so pair it with full metadata. **Use this on the website, print files and exhibition prints.**

## 4.4 BRAND IDENTITY

**Name styling:** `VATSAL SHARMA` — uppercase, tracking +150–200 (social and watermark) · *or* `Vatsal Sharma` in Cormorant Garamond (fine-art and print contexts)

**Palette**

| Role | Hex | Use |
|---|---|---|
| Slate | `#16232A` | Backgrounds, profile photo, dark type |
| Sage Grey | `#7C8B84` | Secondary, dividers |
| Sand | `#D9C7A7` | Accent rule, ring, paper tones |
| Ember | `#C97B3C` | The single warm note — subject accent only |
| Bone | `#F2EBE0` | Type on dark, highlight |

**Typefaces (two maximum)**
- **Display:** Cormorant Garamond — fine-art, print, the Plate Mark
- **UI / body / watermark:** Inter — uppercase, letter-spaced

**Hard rules:** two typefaces, never three · watermark never exceeds 3.5% of the frame · **never place type over the bird** · ember appears exactly once per frame · every export carries IPTC copyright metadata.

---

# THE ONE THING I NEED FROM YOU

**Your three reference images never arrived** — there's no uploads folder in this workspace and no image files on disk, so I could not identify those photographers and I refuse to invent analysis of work I haven't seen.

Re-attach them (a `.jpg` or `.png` usually makes it through where other formats don't), or just type the three handles into chat. I'll then rewrite **Step 2 properly** — per-photographer breakdowns, the comparison table, and a gap analysis based on what those specific accounts are actually doing instead of what the genre generally does.

Steps 3 and 4 above stand on their own and are ready to use now.

---

Source:
- `@mathiphotography` — the only publicly indexed trace is a Threads account with the display line "Photographers of Threads" posting bird content [1](https://www.threads.com/@mathiphotography/post/C7skDjhRRr-). Instagram and Threads both return HTTP 403 to direct access, so no follower count, grid or posting data was available.
