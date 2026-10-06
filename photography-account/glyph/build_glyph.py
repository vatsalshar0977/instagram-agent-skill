#!/usr/bin/env python3
"""
Build the FLYWAY GLYPH assets.

    python3 build_glyph.py

Outputs transparent PNGs (watermark / chop / lockup), profile photos,
SVG masters, and a PDF asset sheet.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

SLATE = (22, 35, 42)        # #16232A
SAGE = (124, 139, 132)      # #7C8B84
SAND = (217, 199, 167)      # #D9C7A7
EMBER = (201, 123, 60)      # #C97B3C
BONE = (242, 235, 224)      # #F2EBE0

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ----------------------------------------------------------------- geometry
# Three climbing strokes. Each stroke is placed in a basis of
#   u = direction of flight (up and to the right)
#   p = perpendicular (the "spacing" axis, down-right in image coords)
# Offsetting along p keeps the strokes strictly parallel and separated,
# so the mark still reads as three birds when it is 32px tall.

PRESETS = {
    "wide":  {"angle": 22.0, "su": 0.62, "sp": 0.40},   # watermark / lockup
    "stack": {"angle": 24.0, "su": 0.28, "sp": 0.62},   # avatar / square
    "mark":  {"angle": 24.0, "su": 0.45, "sp": 0.50},   # watermark corner
}
TAPER = (0.78, 0.88, 1.00)   # far stroke lightest, near stroke heaviest
SS = 4                       # supersample factor for anti-aliasing


def _basis(angle):
    a = math.radians(angle)
    return (math.cos(a), -math.sin(a)), (math.sin(a), math.cos(a))


def glyph_box(L, preset="wide"):
    """Bounding box (w, h) of the glyph given stroke length L."""
    cfg = PRESETS[preset]
    u, p = _basis(cfg["angle"])
    pts = []
    for i in range(3):
        sx = i * cfg["su"] * L * u[0] + i * cfg["sp"] * L * p[0]
        sy = i * cfg["su"] * L * u[1] + i * cfg["sp"] * L * p[1]
        pts.append((sx, sy))
        pts.append((sx + L * u[0], sy + L * u[1]))
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    return (max(xs) - min(xs)), (max(ys) - min(ys))


def draw_glyph(draw, ox, oy, L, thick, color, preset="wide", winged=False):
    """(ox, oy) = TOP-left of the glyph bounding box, in image coords."""
    cfg = PRESETS[preset]
    u, p = _basis(cfg["angle"])
    for i in range(3):
        sx = ox + i * cfg["su"] * L * u[0] + i * cfg["sp"] * L * p[0]
        sy = oy + i * cfg["su"] * L * u[1] + i * cfg["sp"] * L * p[1]
        ex, ey = sx + L * u[0], sy + L * u[1]
        t = max(1.0, thick * TAPER[i])
        if not winged:
            draw.line([(sx, sy), (ex, ey)], fill=color, width=int(round(t)))
            r = t / 2.0
            for (qx, qy) in ((sx, sy), (ex, ey)):
                draw.ellipse([qx - r, qy - r, qx + r, qy + r], fill=color)
        else:
            mx, my = (sx + ex) / 2, (sy + ey) / 2
            lift = L * 0.14
            draw.line([(sx, sy), (mx, my - lift)], fill=color, width=int(round(t)))
            draw.line([(mx, my - lift), (ex, ey)], fill=color, width=int(round(t)))
            r = t / 2.0
            for (qx, qy) in ((sx, sy), (mx, my - lift), (ex, ey)):
                draw.ellipse([qx - r, qy - r, qx + r, qy + r], fill=color)


def make_glyph_png(path, height, color, thick_ratio=0.085, pad=0.06, winged=False,
                   bg=None, ring=None, preset="wide"):
    """Transparent PNG of the glyph, `height` px tall (the glyph itself)."""
    # solve L so that the bounding box height equals `height`
    L = 100.0
    for _ in range(60):
        gw, gh = glyph_box(L, preset)
        L *= height / gh
    gw, gh = glyph_box(L, preset)
    thick = height * thick_ratio
    m = int(math.ceil(max(gw, gh) * pad + thick))
    W, H = int(math.ceil(gw)) + 2 * m, int(math.ceil(gh)) + 2 * m

    big = (W * SS, H * SS)
    img = Image.new("RGBA", big, (0, 0, 0, 0) if bg is None else bg + (255,))
    d = ImageDraw.Draw(img)
    if ring:
        d.ellipse([0, 0, big[0] - 1, big[1] - 1], outline=ring + (255,),
                  width=int(round(max(gw, gh) * 0.012 * SS)))
    draw_glyph(d, (m + (W - 2 * m - gw) / 2) * SS, m * SS, L * SS, thick * SS,
               color + (255,), preset, winged)
    img = img.resize((W, H), Image.LANCZOS)
    img.save(path)
    return path, (W, H)


def make_profile(path, size, glyph_ratio=0.58, bg=SLATE, fg=BONE, ring=None):
    """Square profile photo: slate field, bone glyph, centred."""
    big = size * SS
    img = Image.new("RGBA", (big, big), bg + (255,))
    d = ImageDraw.Draw(img)
    if ring:
        d.ellipse([big * 0.02, big * 0.02, big * 0.98, big * 0.98],
                  outline=ring + (255,), width=int(round(big * 0.012)))
    gw_target = big * glyph_ratio          # width drives the square layout
    L = gw_target
    for _ in range(60):
        gw, gh = glyph_box(L, "stack")
        L *= gw_target / gw
    gw, gh = glyph_box(L, "stack")
    ox = (big - gw) / 2
    oy = (big - gh) / 2
    thick = gh * 0.17           # heavier stroke for avatar legibility
    draw_glyph(d, ox, oy, L, thick, fg + (255,), "stack")
    img.resize((size, size), Image.LANCZOS).save(path)
    return path


def make_chop(path, size=1000):
    """Print chop: glyph inside a thin ring, black on transparent."""
    big = size * SS
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([big * 0.03, big * 0.03, big * 0.97, big * 0.97],
              outline=(0, 0, 0, 255), width=int(round(big * 0.010)))
    gw_target = big * 0.44
    L = gw_target
    for _ in range(60):
        gw, gh = glyph_box(L, "stack")
        L *= gw_target / gw
    gw, gh = glyph_box(L, "stack")
    draw_glyph(d, (big - gw) / 2, (big - gh) / 2, L, gh * 0.10, (0, 0, 0, 255), "stack")
    img.resize((size, size), Image.LANCZOS).save(path)
    return path


def make_lockup(path, width=1600):
    """'VS' monogram + glyph lockup, bone on slate."""
    h = int(width * 0.34)
    big = (width * SS, h * SS)
    img = Image.new("RGBA", big, SLATE + (255,))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT_SERIF, int(h * 0.52 * SS))
    text = "VS"
    tb = d.textbbox((0, 0), text, font=f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    gh = h * 0.30
    L = gh
    for _ in range(60):
        gw, ghh = glyph_box(L, "wide")
        L *= gh / ghh
    gw, ghh = glyph_box(L, "wide")
    gap = h * 0.10
    total = tw + gap + gw
    x = (big[0] - (total + tw * 0.14)) / 2     # optical tracking correction
    d.text((x, (big[1] - th) / 2 - tb[1]), text, font=f, fill=BONE + (255,))
    draw_glyph(d, x + tw + gap, (big[1] - ghh) / 2, L, gh * 0.085, BONE + (255,), "wide")
    img.resize((width, h), Image.LANCZOS).save(path)
    return path


# ----------------------------------------------------------------- assets
files = {}

files["glyph-white-512"] = make_glyph_png(OUT / "flyway-glyph-white.png", 512, (255, 255, 255), preset="mark")
files["glyph-black-512"] = make_glyph_png(OUT / "flyway-glyph-black.png", 512, (0, 0, 0), preset="mark")
files["glyph-ember-512"] = make_glyph_png(OUT / "flyway-glyph-ember.png", 512, EMBER, preset="mark")
files["glyph-winged-512"] = make_glyph_png(OUT / "flyway-glyph-winged.png", 512, (255, 255, 255),
                                           winged=True)
make_glyph_png(OUT / "flyway-glyph-stack.png", 512, (255, 255, 255), preset="stack")
files["chop-1000"] = make_chop(OUT / "flyway-glyph-chop.png")
make_profile(OUT / "profile-glyph-640.png", 640)
make_profile(OUT / "profile-glyph-320.png", 320)
make_profile(OUT / "profile-glyph-640-ring.png", 640, ring=SAND)
make_lockup(OUT / "flyway-glyph-lockup.png")

# avatar legibility tests at true pixel size
for s in (32, 48, 110):
    make_profile(OUT / f"test-glyph-{s}px.png", s, bg=SLATE, fg=BONE)

# ----------------------------------------------------------------- SVG masters
def svg_glyph(color="#F2EBE0", thick_ratio=0.085, size_h=200, preset="wide"):
    L = size_h
    for _ in range(60):
        gw, gh = glyph_box(L, preset)
        L *= size_h / gh
    gw, gh = glyph_box(L, preset)
    thick = size_h * thick_ratio
    m = thick * 2 + gh * 0.06
    cfg = PRESETS[preset]
    u, q = _basis(cfg["angle"])
    parts = []
    for i in range(3):
        sx = m + i * cfg["su"] * L * u[0] + i * cfg["sp"] * L * q[0]
        sy = m + i * cfg["su"] * L * u[1] + i * cfg["sp"] * L * q[1]
        ex, ey = sx + L * u[0], sy + L * u[1]
        t = thick * TAPER[i]
        parts.append(
            f'  <line x1="{sx:.2f}" y1="{sy:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" '
            f'stroke="{color}" stroke-width="{t:.2f}" stroke-linecap="round"/>')
    body = "\n".join(parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{gw + 2 * m:.0f}" '
            f'height="{gh + 2 * m:.0f}" viewBox="0 0 {gw + 2 * m:.0f} {gh + 2 * m:.0f}">\n'
            f'{body}\n</svg>\n')


(OUT / "flyway-glyph.svg").write_text(svg_glyph("#F2EBE0", preset="mark"), encoding="utf-8")
(OUT / "flyway-glyph-black.svg").write_text(svg_glyph("#000000", preset="mark"), encoding="utf-8")
(OUT / "flyway-glyph-stack.svg").write_text(svg_glyph("#F2EBE0", preset="stack"), encoding="utf-8")

L = 160.0
for _ in range(60):
    gw, gh = glyph_box(L, "stack")
    L *= 160.0 / gh
gw, gh = glyph_box(L, "stack")
cfg = PRESETS["stack"]
u, q = _basis(cfg["angle"])
lines = []
for i in range(3):
    sx = i * cfg["su"] * L * u[0] + i * cfg["sp"] * L * q[0]
    sy = i * cfg["su"] * L * u[1] + i * cfg["sp"] * L * q[1]
    ex, ey = sx + L * u[0], sy + L * u[1]
    t = 160 * 0.10 * TAPER[i]
    lines.append(f'    <line x1="{sx:.2f}" y1="{sy:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" '
                 f'stroke="#000000" stroke-width="{t:.2f}" stroke-linecap="round"/>')
(OUT / "flyway-glyph-chop.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">\n'
    '  <circle cx="200" cy="200" r="186" fill="none" stroke="#000000" stroke-width="4"/>\n'
    f'  <g transform="translate({(400 - gw) / 2:.2f},{(400 - gh) / 2:.2f})">\n'
    + "\n".join(lines) + "\n  </g>\n</svg>\n", encoding="utf-8")

# ----------------------------------------------------------------- PDF sheet
pdfmetrics.registerFont(TTFont("Body", FONT_SANS))
pdfmetrics.registerFont(TTFont("Body-Bold", FONT_BOLD))
pdfmetrics.registerFont(TTFont("Display", FONT_SERIF))

pdf_path = OUT / "Flyway-Glyph-Asset-Sheet.pdf"
c = canvas.Canvas(str(pdf_path), pagesize=A4)
W, H = A4


def header(c, title):
    c.setFillColorRGB(*[v / 255 for v in SLATE])
    c.rect(0, H - 44, W, 44, stroke=0, fill=1)
    c.setFillColorRGB(*[v / 255 for v in BONE])
    c.setFont("Display", 17)
    c.drawString(20 * 72 / 25.4, H - 29, title)


def label(c, x, y, txt, size=8.5, color=SAGE, bold=False):
    c.setFillColorRGB(*[v / 255 for v in color])
    c.setFont("Body-Bold" if bold else "Body", size)
    c.drawString(x, y, txt)


mm = 72 / 25.4
header(c, "The Flyway Glyph — asset sheet")
y = H - 70

c.setFillColorRGB(*[v / 255 for v in SLATE])
c.setFont("Display", 13)
c.drawString(20 * mm, y, "What it is")
y -= 16
c.setFillColorRGB(*[v / 255 for v in (60, 74, 81)])
c.setFont("Body", 9)
for line in [
    "Three strokes climbing to the right: a flock rising, and the arc of the route they fly.",
    "Stroke weight tapers 1.00 / 0.88 / 0.78 from bottom-left to top-right, so the near bird reads",
    "closest and the flock recedes into distance. Angle of climb: 22 degrees.",
]:
    c.drawString(20 * mm, y, line)
    y -= 12

y -= 10
c.setFillColorRGB(*[v / 255 for v in SLATE])
c.setFont("Display", 13)
c.drawString(20 * mm, y, "Master — rendered at four sizes")
y -= 14
sizes = [(20 * mm, 26), (62 * mm, 14), (96 * mm, 8), (120 * mm, 3.2)]
for x, h in sizes:
    if True:
        from PIL import Image as _I
        w = _I.open(OUT / "flyway-glyph-black.png")
        ar = w.size[0] / w.size[1]
        c.drawImage(str(OUT / "flyway-glyph-black.png"), x, y - h, width=h * ar, height=h,
                    mask="auto")
    label(c, x, y - h - 9, f"{h:.0f}pt", 7)

y -= 62
c.setFillColorRGB(*[v / 255 for v in SLATE])
c.setFont("Display", 13)
c.drawString(20 * mm, y, "Profile photo — 640px and the 32px test")
y -= 16
c.drawImage(str(OUT / "profile-glyph-640.png"), 20 * mm, y - 40 * mm,
            width=40 * mm, height=40 * mm)
label(c, 20 * mm, y - 44 * mm, "640 x 640  ·  glyph 46% of frame  ·  bone on slate", 8)
c.drawImage(str(OUT / "profile-glyph-640-ring.png"), 68 * mm, y - 40 * mm,
            width=40 * mm, height=40 * mm)
label(c, 68 * mm, y - 44 * mm, "with sand ring", 8)
c.drawImage(str(OUT / "test-glyph-110px.png"), 116 * mm, y - 22 * mm,
            width=22 * mm, height=22 * mm)
label(c, 116 * mm, y - 26 * mm, "110px (grid)", 8)
c.drawImage(str(OUT / "test-glyph-48px.png"), 116 * mm, y - 34 * mm,
            width=9 * mm, height=9 * mm)
label(c, 116 * mm, y - 38 * mm, "48px", 8)
c.drawImage(str(OUT / "test-glyph-32px.png"), 140 * mm, y - 34 * mm,
            width=6 * mm, height=6 * mm)
label(c, 140 * mm, y - 38 * mm, "32px (comments)", 8)

y -= 52 * mm
c.setFillColorRGB(*[v / 255 for v in SLATE])
c.setFont("Display", 13)
c.drawString(20 * mm, y, "Variants")
y -= 16
c.drawImage(str(OUT / "flyway-glyph-winged.png"), 20 * mm, y - 16 * mm,
            width=16 * mm, height=16 * mm, mask="auto")
label(c, 20 * mm, y - 20 * mm, "Winged (large use only)", 8)
c.drawImage(str(OUT / "flyway-glyph-chop.png"), 56 * mm, y - 16 * mm,
            width=16 * mm, height=16 * mm, mask="auto")
label(c, 56 * mm, y - 20 * mm, "Chop (print / emboss)", 8)
c.drawImage(str(OUT / "flyway-glyph-lockup.png"), 92 * mm, y - 12 * mm,
            width=44 * mm, height=15 * mm)
label(c, 92 * mm, y - 20 * mm, "VS lockup", 8)

y -= 34 * mm
c.setFillColorRGB(*[v / 255 for v in SLATE])
c.setFont("Display", 13)
c.drawString(20 * mm, y, "Specs")
y -= 15
specs = [
    ("Angle of climb", "22 degrees"),
    ("Offset between strokes", "0.62 L across, 0.30 L up"),
    ("Thickness taper", "1.00 / 0.88 / 0.78 (recession)"),
    ("Stroke weight", "8.5% of glyph height (12% for avatar)"),
    ("Watermark size", "28-40px tall on a 2000px export"),
    ("Watermark opacity", "12-18% white on dark, 15-22% black on light"),
    ("Placement", "glyph top-left at 4% margin + handle bottom-right at 2.5%"),
    ("Never", "below 24px tall, or in Ember on Slate (too little contrast)"),
]
for k, v in specs:
    label(c, 20 * mm, y, k, 8.5, SLATE, bold=True)
    label(c, 62 * mm, y, v, 8.5)
    y -= 12

c.setFillColorRGB(*[v / 255 for v in SAGE])
c.setFont("Body", 7.5)
c.drawString(20 * mm, 14 * mm,
             "Vatsal Sharma · Flyway Glyph · Slate #16232A · Sage #7C8B84 · Sand #D9C7A7 · "
             "Ember #C97B3C · Bone #F2EBE0")
c.showPage()
c.save()

print("Built:")
for f in sorted(OUT.glob("*")):
    if f.is_file() and f.suffix in {".png", ".svg", ".pdf"}:
        print(f"  {f.name:42s} {f.stat().st_size:>7,} bytes")
