#!/usr/bin/env python3
"""
Apply every signature style from STYLE-DIRECTIONS.md to one photograph,
and build a labelled contact sheet so you can compare them side by side.

    python3 scripts/styles.py photo.jpg
    python3 scripts/styles.py photo.jpg --out photos/02-working/styles
    python3 scripts/styles.py photo.jpg --only "Dust & Dawn,Nocturne"

Needs: pillow, numpy  (contact sheet also needs reportlab)

Notes on fidelity
-----------------
This is an approximation of Lightroom, not Lightroom. Slider behaviour is
modelled, not identical. Two things it cannot do:
  1. It does not demosaic RAW. Feed it a JPEG/TIFF export, not a CR3.
  2. The subject mask is a heuristic - it finds the sharpest region of the
     frame, which on a bird portrait is almost always the bird. Check the
     debug mask output before trusting it on an unusual composition.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

# ------------------------------------------------------------------ colour utils
def srgb_to_linear(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * (c ** (1 / 2.4)) - 0.055)


def to_arr(img):
    return np.asarray(img, dtype=np.float32) / 255.0


def to_img(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8), "RGB")


def luma(a):
    return a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722


def blur_arr(a, radius):
    if radius <= 0:
        return a
    return to_arr(to_img(a).filter(ImageFilter.GaussianBlur(radius)))


# ------------------------------------------------------------------ style spec
@dataclass
class Style:
    key: str
    name: str
    tagline: str = ""

    # basic
    exposure: float = 0.0      # stops
    contrast: float = 0.0      # -1..1
    highlights: float = 0.0    # -1..1  (positive = recover)
    shadows: float = 0.0       # -1..1  (positive = lift)
    whites: float = 0.0        # -1..1
    blacks: float = 0.0        # -1..1  (negative = deepen)
    temp: float = 0.0          # -1..1  (positive = warmer)
    tint: float = 0.0          # -1..1  (positive = magenta)
    saturation: float = 0.0    # -1..1
    vibrance: float = 0.0      # -1..1
    clarity: float = 0.0       # -1..1  (mid-tone local contrast)
    dehaze: float = 0.0        # -1..1
    texture: float = 0.0       # -1..1  (fine detail)

    # tone
    curve_pts: list | None = None     # [(in, out), ...]
    bw: bool = False
    bw_mix: tuple = (0.30, 0.59, 0.11)

    # colour
    hsl: dict = field(default_factory=dict)   # name -> (sat_mult, lum_mult)
    split_shadow: tuple = (0.0, 0.0, 0.0)     # hue deg, sat, lum
    split_mid: tuple = (0.0, 0.0, 0.0)
    split_high: tuple = (0.0, 0.0, 0.0)
    split_balance: float = 0.0                # negative biases to shadows

    # subject separation
    subject: bool = False
    bg_temp: float = 0.0
    bg_sat: float = 0.0
    bg_clarity: float = 0.0
    subj_temp: float = 0.0
    subj_sat: float = 0.0
    subj_texture: float = 0.0
    subj_exposure: float = 0.0

    # effects
    vignette: float = 0.0     # negative darkens corners
    vig_mid: float = 0.55
    grain: float = 0.0        # 0..1
    grain_size: float = 1.0
    sharpen: float = 0.0


HUE_RANGES = {
    "red": (0, 60), "orange": (20, 50), "yellow": (45, 75),
    "green": (75, 165), "aqua": (165, 200), "blue": (200, 255),
    "purple": (255, 290), "magenta": (290, 345),
}


# ------------------------------------------------------------------ engine
def apply_style(img: Image.Image, st: Style, debug_mask: Path | None = None) -> Image.Image:
    a = to_arr(img)
    h, w = a.shape[:2]
    base_px = max(h, w)

    # --- exposure in linear light
    if st.exposure:
        lin = srgb_to_linear(a) * (2.0 ** st.exposure)
        a = linear_to_srgb(lin)

    # --- white balance
    if st.temp or st.tint:
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        t = st.temp * 0.18
        ti = st.tint * 0.12
        r = r * (1 + t) * (1 + ti * 0.5)
        g = g * (1 - ti)
        b = b * (1 - t) * (1 + ti * 0.5)
        a = np.stack([r, g, b], -1)

    # --- contrast
    if st.contrast:
        a = (a - 0.5) * (1.0 + st.contrast) + 0.5

    # --- highlights / shadows / whites / blacks
    L = luma(a)[..., None]
    if st.highlights:
        m = np.clip((L - 0.5) / 0.5, 0, 1) ** 1.5
        a = a - st.highlights * 0.55 * m
    if st.shadows:
        m = np.clip((0.5 - L) / 0.5, 0, 1) ** 1.5
        a = a + st.shadows * 0.55 * m
    if st.whites:
        m = np.clip((L - 0.7) / 0.3, 0, 1) ** 1.2
        a = a + st.whites * 0.35 * m
    if st.blacks:
        m = np.clip((0.3 - L) / 0.3, 0, 1) ** 1.2
        a = a + st.blacks * 0.35 * m
    a = np.clip(a, 0, 1)

    # --- tone curve
    if st.curve_pts:
        pts = np.array(st.curve_pts, dtype=np.float32)
        a = np.interp(a, pts[:, 0], pts[:, 1]).astype(np.float32)

    # --- local contrast: clarity (mid) + texture (fine) + dehaze
    if st.clarity:
        a = a + st.clarity * 0.9 * (a - blur_arr(a, base_px / 220.0))
    if st.dehaze:
        lowfreq = blur_arr(a, base_px / 40.0)
        a = a + st.dehaze * 0.55 * (a - lowfreq)
        a = a + st.dehaze * 0.04 * (a - luma(a)[..., None])
    if st.texture:
        a = a + st.texture * 0.8 * (a - blur_arr(a, max(1.0, base_px / 900.0)))
    a = np.clip(a, 0, 1)

    # --- subject / background separation
    if st.subject:
        mask = subject_mask(a, base_px)
        if debug_mask is not None:
            to_img(np.stack([mask, mask, mask], -1)).save(debug_mask)
        m = mask[..., None]
        # background: cooler, less saturated, softer
        bgc = (1.0 - m)
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        r = r * (1 - st.bg_temp * 0.16 * bgc[:, :, 0])
        b = b * (1 + st.bg_temp * 0.16 * bgc[:, :, 0])
        a = np.stack([r, g, b], -1)
        Lb = luma(a)[..., None]
        a = Lb + (a - Lb) * (1.0 + st.bg_sat * bgc)
        if st.bg_clarity:
            a = a + st.bg_clarity * 0.9 * (a - blur_arr(a, base_px / 220.0)) * bgc
        # subject: warmer, more texture, slight lift
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        r = r * (1 + st.subj_temp * 0.16 * m[:, :, 0])
        b = b * (1 - st.subj_temp * 0.16 * m[:, :, 0])
        a = np.stack([r, g, b], -1)
        Ls = luma(a)[..., None]
        a = Ls + (a - Ls) * (1.0 + st.subj_sat * m)
        if st.subj_texture:
            a = a + st.subj_texture * 0.8 * (a - blur_arr(a, max(1.0, base_px / 900.0))) * m
        a = a + st.subj_exposure * 0.12 * m
        a = np.clip(a, 0, 1)

    # --- black & white
    if st.bw:
        Lb = luma(a)
        wts = np.array(st.bw_mix, dtype=np.float32)
        wts = wts / wts.sum()
        g = a[..., 0] * wts[0] + a[..., 1] * wts[1] + a[..., 2] * wts[2]
        a = np.stack([g, g, g], -1)

    # --- HSL
    if st.hsl:
        hsv = np.asarray(to_img(a).convert("HSV"), dtype=np.float32) / 255.0
        H, S, V = hsv[..., 0] * 360.0, hsv[..., 1], hsv[..., 2]
        dS = np.zeros_like(S)
        dV = np.zeros_like(V)
        for name, (smult, lmult) in st.hsl.items():
            if name not in HUE_RANGES:
                continue
            centre, width = HUE_RANGES[name]
            diff = np.abs((H - centre + 180) % 360 - 180)
            m = np.clip(1.0 - (diff / (width / 2.0)) ** 2, 0, 1)
            dS += (smult - 1.0) * m
            dV += (lmult - 1.0) * m
        S = np.clip(S * (1.0 + dS), 0, 1)
        V = np.clip(V * (1.0 + dV), 0, 1)
        a = to_arr(Image.fromarray(
            np.stack([H / 360.0 * 255, S * 255, V * 255], -1).astype(np.uint8), "HSV").convert("RGB"))

    # --- saturation / vibrance
    if st.saturation or st.vibrance:
        Lb = luma(a)[..., None]
        sat = np.abs(a - Lb).max(axis=-1, keepdims=True) + 1e-6
        if st.vibrance:
            boost = st.vibrance * 0.8 * (1.0 - sat)
            a = Lb + (a - Lb) * (1.0 + boost)
        if st.saturation:
            a = Lb + (a - Lb) * (1.0 + st.saturation)
        a = np.clip(a, 0, 1)

    # --- split toning
    for (hue, sat, lumv), kind in ((st.split_shadow, "s"), (st.split_mid, "m"), (st.split_high, "h")):
        if not sat and not lumv:
            continue
        L2 = luma(a)
        if kind == "s":
            wgt = np.clip(1.0 - L2, 0, 1) ** 2
        elif kind == "h":
            wgt = np.clip(L2, 0, 1) ** 2
        else:
            wgt = 1.0 - np.clip(1.0 - L2, 0, 1) ** 2 - np.clip(L2, 0, 1) ** 2
        wgt *= (1.0 + (st.split_balance if kind == "s" else -st.split_balance))
        wgt = np.clip(wgt, 0, 1)[..., None] * abs(sat)
        tint = np.array(hue_to_rgb(hue), dtype=np.float32)
        a = a * (1 - wgt) + (a + (tint - 0.5) * 0.5) * wgt
        a = a + lumv * 0.08 * wgt
        a = np.clip(a, 0, 1)

    # --- vignette
    if st.vignette:
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
        r = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2) / 1.4142
        t = np.clip((r - st.vig_mid) / max(1e-6, (1 - st.vig_mid)), 0, 1)
        t = t * t * (3 - 2 * t)
        a = a * (1.0 + st.vignette * t)[..., None]
        a = np.clip(a, 0, 1)

    # --- grain
    if st.grain:
        rng = np.random.default_rng(7)
        n = rng.normal(0.0, 1.0, (h, w)).astype(np.float32)
        if st.grain_size > 1.0:
            n = np.asarray(Image.fromarray(((n * 40 + 128)).clip(0, 255).astype(np.uint8))
                           .filter(ImageFilter.GaussianBlur(st.grain_size)), np.float32) / 40.0 - 3.2
        Lg = luma(a)
        gate = 1.0 - np.abs(Lg - 0.5) * 1.2          # most grain in the midtones
        a = a + (n * st.grain * 0.12 * np.clip(gate, 0.15, 1.0))[..., None]
        a = np.clip(a, 0, 1)

    out = to_img(a)
    if st.sharpen:
        out = out.filter(ImageFilter.UnsharpMask(radius=max(1.0, base_px / 900.0),
                                                 percent=int(st.sharpen * 120), threshold=3))
    return out


def hue_to_rgb(hue_deg):
    """rough RGB direction for a hue, centred on 0.5 grey"""
    h = (hue_deg % 360) / 60.0
    x = 1 - abs(h % 2 - 1)
    if h < 1:   r, g, b = 1, x, 0
    elif h < 2: r, g, b = x, 1, 0
    elif h < 3: r, g, b = 0, 1, x
    elif h < 4: r, g, b = 0, x, 1
    elif h < 5: r, g, b = x, 0, 1
    else:       r, g, b = 1, 0, x
    s = (r + g + b) or 1
    return (r / s, g / s, b / s)


def subject_mask(a, base_px, percentile=88):
    """Find the sharpest region of the frame - usually the bird."""
    L = luma(a)
    gy, gx = np.gradient(L)
    sharp = np.sqrt(gx ** 2 + gy ** 2)
    k = max(4, int(base_px / 160))
    H, W = sharp.shape
    kh, kw = max(1, H // k), max(1, W // k)
    blocks = sharp[:kh * k, :kw * k].reshape(kh, k, kw, k).mean(axis=(1, 3))
    thr = np.percentile(blocks, percentile)
    hot = (blocks >= thr).astype(np.float32)
    # centre of mass of the sharp blocks, weighted
    ys, xs = np.nonzero(hot)
    if len(xs) == 0:
        xs = np.array([blocks.shape[1] // 2]); ys = np.array([blocks.shape[0] // 2])
    cy = (ys.mean() + 0.5) * k
    cx = (xs.mean() + 0.5) * k
    rad = base_px * 0.30
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / rad
    mask = np.clip(1.0 - d ** 2, 0, 1)
    mask = to_arr(to_img(np.stack([mask] * 3, -1)).filter(ImageFilter.GaussianBlur(base_px / 60.0)))[..., 0]
    return np.clip(mask / max(1e-6, mask.max()), 0, 1)


# ------------------------------------------------------------------ the nine styles
def styles():
    return [
        Style(
            key="dust-dawn", name="Dust & Dawn",
            tagline="Cool desaturated habitat, bird is the only warm thing",
            exposure=-0.15, contrast=-0.12, highlights=0.55, shadows=0.28,
            whites=0.12, blacks=-0.18, texture=0.12, clarity=-0.08, dehaze=0.06,
            saturation=-0.06, vibrance=0.08,
            hsl={"orange": (0.90, 1.12), "yellow": (0.70, 1.06), "green": (0.55, 0.88),
                 "aqua": (0.65, 0.94), "blue": (0.80, 0.86), "purple": (0.75, 1.0),
                 "magenta": (0.80, 1.0)},
            split_shadow=(210, 0.10, -0.04), split_mid=(38, 0.06, 0.0),
            split_high=(48, 0.05, 0.02), split_balance=-0.08,
            subject=True, bg_temp=0.12, bg_sat=-0.18, bg_clarity=-0.20,
            subj_temp=0.10, subj_sat=0.05, subj_texture=0.18, subj_exposure=0.10,
            vignette=-0.10, vig_mid=0.55, grain=0.22, grain_size=1.4, sharpen=0.35,
        ),
        Style(
            key="slate-ember", name="Slate & Ember",
            tagline="Almost monochrome, one surviving warm note",
            exposure=-0.05, contrast=0.06, highlights=0.45, shadows=0.22,
            blacks=-0.22, clarity=-0.05, dehaze=0.08, saturation=-0.30,
            hsl={"orange": (1.25, 1.10), "yellow": (1.10, 1.05), "green": (0.30, 0.92),
                 "aqua": (0.35, 0.95), "blue": (0.40, 0.90)},
            split_shadow=(210, 0.14, -0.03), split_high=(40, 0.06, 0.0),
            subject=True, bg_temp=0.10, bg_sat=-0.70, subj_temp=0.12, subj_sat=0.35,
            subj_texture=0.15, vignette=-0.12, grain=0.26, sharpen=0.35,
        ),
        Style(
            key="portra", name="Portra Restraint",
            tagline="Film: warm mids, cool shadows, lifted blacks, real grain",
            exposure=0.05, contrast=-0.18, highlights=0.45, shadows=0.30,
            whites=0.05, blacks=0.18, saturation=-0.04, vibrance=0.06,
            curve_pts=[(0.0, 0.055), (0.25, 0.28), (0.5, 0.52), (0.75, 0.76), (1.0, 0.97)],
            hsl={"green": (0.80, 0.95), "yellow": (0.85, 1.02), "blue": (0.90, 0.95)},
            split_shadow=(215, 0.12, 0.0), split_mid=(40, 0.08, 0.0),
            vignette=-0.06, grain=0.32, grain_size=1.8, sharpen=0.30,
        ),
        Style(
            key="highkey", name="High-Key Mist",
            tagline="Bright, airy, negative space, bird small",
            exposure=0.35, contrast=-0.25, highlights=0.30, shadows=0.35,
            whites=0.22, blacks=0.20, dehaze=-0.10, saturation=-0.10, vibrance=0.04,
            hsl={"blue": (0.85, 1.05), "green": (0.75, 1.02)},
            split_high=(200, 0.05, 0.02), split_shadow=(210, 0.04, 0.0),
            vignette=0.0, grain=0.15, sharpen=0.30,
        ),
        Style(
            key="nocturne", name="Nocturne",
            tagline="Chiaroscuro - the bird emerges from black",
            exposure=-0.30, contrast=0.10, highlights=0.70, shadows=0.20,
            blacks=-0.32, clarity=0.10, dehaze=0.05, saturation=-0.08,
            curve_pts=[(0.0, 0.0), (0.25, 0.18), (0.5, 0.46), (0.75, 0.78), (1.0, 1.0)],
            subject=True, bg_temp=0.06, bg_sat=-0.25, subj_temp=0.08,
            subj_texture=0.16, subj_exposure=0.25,
            vignette=-0.18, vig_mid=0.45, grain=0.30, sharpen=0.35,
        ),
        Style(
            key="halo", name="Halo",
            tagline="Backlit translucency - light through the feathers",
            exposure=-0.20, contrast=-0.05, highlights=0.75, shadows=0.45,
            dehaze=-0.06, texture=0.20, saturation=0.02, vibrance=0.08,
            hsl={"orange": (1.10, 1.10), "yellow": (1.05, 1.05)},
            split_high=(45, 0.08, 0.03), split_shadow=(215, 0.06, 0.0),
            subject=True, subj_temp=0.15, subj_texture=0.20, subj_exposure=0.18,
            vignette=-0.08, grain=0.28, sharpen=0.35,
        ),
        Style(
            key="platinum", name="Platinum",
            tagline="Warm-toned black and white, museum print",
            exposure=0.0, contrast=0.18, highlights=0.25, shadows=0.15,
            blacks=-0.20, clarity=0.08, texture=0.10,
            bw=True, bw_mix=(0.42, 0.53, 0.05),
            split_shadow=(35, 0.06, 0.0), split_high=(45, 0.08, 0.0),
            vignette=-0.08, grain=0.35, grain_size=1.5, sharpen=0.40,
        ),
        Style(
            key="cyanotype", name="Cyanotype",
            tagline="Blue-cyan wetland duotone - Thol and Nalsarovar",
            exposure=0.05, contrast=0.10, highlights=0.30, shadows=0.20,
            blacks=-0.15, dehaze=0.10, texture=0.12,
            bw=True, bw_mix=(0.25, 0.45, 0.30),
            split_shadow=(205, 0.18, -0.02), split_high=(195, 0.08, 0.02),
            vignette=-0.10, grain=0.24, sharpen=0.35,
        ),
        Style(
            key="graphic", name="Graphic",
            tagline="Strong shapes, negative space, subject small",
            exposure=0.0, contrast=0.14, highlights=0.20, shadows=0.10,
            blacks=-0.22, whites=0.10, clarity=0.10, dehaze=0.08, saturation=-0.15,
            curve_pts=[(0.0, 0.0), (0.25, 0.20), (0.5, 0.52), (0.75, 0.84), (1.0, 1.0)],
            hsl={"green": (0.70, 0.95), "blue": (0.85, 0.95)},
            vignette=-0.06, grain=0.12, sharpen=0.40,
        ),
    ]


# ------------------------------------------------------------------ contact sheet
def contact_sheet(original: Image.Image, results: list, out: Path):
    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfgen import canvas
    except ImportError:
        return None

    pdfmetrics.registerFont(TTFont("Body", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("Body-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    pw, ph = landscape(A4)
    c = canvas.Canvas(str(out), pagesize=(pw, ph))
    m = 12 * mm
    cols, rows = 3, 3
    tw = (pw - m * 2 - 8 * mm * (cols - 1)) / cols
    th = tw * 0.66
    top = ph - m - 10 * mm

    c.setFillColorRGB(0.086, 0.137, 0.165)
    c.rect(0, ph - 12 * mm, pw, 12 * mm, stroke=0, fill=1)
    c.setFillColorRGB(0.949, 0.921, 0.878)
    c.setFont("Body-Bold", 10)
    c.drawString(m, ph - 8 * mm, "STYLE COMPARISON")
    c.setFont("Body", 8)
    c.drawRightString(pw - m, ph - 8 * mm, "nine directions · same frame · no hand masking")

    for i, (st, im) in enumerate(results):
        r, col = divmod(i, cols)
        x = m + col * (tw + 8 * mm)
        y = top - (r + 1) * th - r * 11 * mm
        c.drawImage(str(im), x, y, width=tw, height=th)
        c.setFillColorRGB(0.086, 0.137, 0.165)
        c.setFont("Body-Bold", 8.5)
        c.drawString(x, y - 4.5 * mm, f"{i + 1}. {st.name}")
        c.setFont("Body", 7)
        c.setFillColorRGB(0.35, 0.42, 0.46)
        c.drawString(x, y - 8 * mm, st.tagline[:78])

    c.setFillColorRGB(0.5, 0.55, 0.52)
    c.setFont("Body", 7)
    c.drawString(m, 6 * mm, "Approximation of Lightroom sliders, not Lightroom. Subject mask is a sharpness heuristic — verify on unusual compositions.")
    c.showPage()
    c.save()
    return out


# ------------------------------------------------------------------ cli
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("--out", default=None)
    ap.add_argument("--only", default=None, help="comma separated style keys")
    ap.add_argument("--sheet", action="store_true", default=True)
    ap.add_argument("--jpeg-quality", type=int, default=92)
    args = ap.parse_args()

    src = Path(args.photo)
    if not src.exists():
        print(f"No such file: {src}")
        return 1
    out_dir = Path(args.out) if args.out else Path("photos/02-working/styles")
    out_dir.mkdir(parents=True, exist_ok=True)

    img = Image.open(src).convert("RGB")
    print(f"{src.name}  {img.size[0]}x{img.size[1]}")

    chosen = styles()
    if args.only:
        keys = {k.strip() for k in args.only.split(",")}
        chosen = [s for s in chosen if s.key in keys or s.name in keys]

    results = []
    for st in chosen:
        tmp = out_dir / f"_tmp_{st.key}.jpg"
        edited = apply_style(img, st, debug_mask=out_dir / f"_mask_{st.key}.png" if st.subject else None)
        p = out_dir / f"{src.stem}__{st.key}.jpg"
        edited.save(p, quality=args.jpeg_quality, subsampling=0)
        tmp_p = out_dir / f"_sheet_{st.key}.jpg"
        edited.copy().resize((900, int(900 * img.size[1] / img.size[0])), Image.LANCZOS).save(tmp_p, quality=88)
        results.append((st, tmp_p))
        print(f"  {st.name:18s} -> {p.name}")

    if args.sheet and results:
        sheet = out_dir / f"{src.stem}__STYLE-COMPARISON.pdf"
        if contact_sheet(img, results, sheet):
            print(f"\nContact sheet: {sheet}")
        for _, p in results:
            p.unlink(missing_ok=True)

    print(f"\n{len(results)} style(s) written to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
