#!/usr/bin/env python3
"""
Build "Vatsal Sharma — Bird Photography Style & Brand Guide" PDF
from the markdown files in this folder.

Requires: reportlab (pip install reportlab)
Run:       python3 build_pdf.py
"""
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate,
                                PageBreak, PageTemplate, Paragraph, Preformatted, Spacer,
                                Table, TableStyle, ListFlowable, ListItem)

BASE = Path(__file__).resolve().parent
OUT = BASE / "Vatsal-Sharma-Bird-Photography-Style-and-Brand-Guide.pdf"
FONTS = "/usr/share/fonts/truetype/dejavu"

# ----------------------------------------------------------------- palette
SLATE = colors.HexColor("#16232A")
SAGE = colors.HexColor("#7C8B84")
SAND = colors.HexColor("#D9C7A7")
EMBER = colors.HexColor("#C97B3C")
BONE = colors.HexColor("#F2EBE0")
RULE = colors.HexColor("#DCE2DF")
CODEBG = colors.HexColor("#F1F4F3")
ZEBRA = colors.HexColor("#F5F7F6")
INK = colors.HexColor("#16232A")
MUTED = colors.HexColor("#6E7A74")

pdfmetrics.registerFont(TTFont("Body", f"{FONTS}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", f"{FONTS}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", "/home/user/.pdffonts/DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("Display", f"{FONTS}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Display-Bold", f"{FONTS}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", f"{FONTS}/DejaVuSansMono.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic",
                              boldItalic="Body-Bold")

# ----------------------------------------------------------------- styles
S = StyleSheet1()
S.add(ParagraphStyle("body", fontName="Body", fontSize=9.4, leading=13.6, textColor=INK,
                     alignment=TA_JUSTIFY, spaceAfter=5))
S.add(ParagraphStyle("h2", fontName="Display-Bold", fontSize=19, leading=23, textColor=SLATE,
                     spaceBefore=0, spaceAfter=8, alignment=TA_LEFT))
S.add(ParagraphStyle("h3", fontName="Display-Bold", fontSize=13.5, leading=17, textColor=SLATE,
                     spaceBefore=10, spaceAfter=5))
S.add(ParagraphStyle("h4", fontName="Body-Bold", fontSize=10.8, leading=14, textColor=SLATE,
                     spaceBefore=8, spaceAfter=3))
S.add(ParagraphStyle("h5", fontName="Body-Bold", fontSize=9.6, leading=13, textColor=EMBER,
                     spaceBefore=7, spaceAfter=3))
S.add(ParagraphStyle("h6", fontName="Body-Bold", fontSize=9.2, leading=12.5, textColor=SAGE,
                     spaceBefore=5, spaceAfter=2))
S.add(ParagraphStyle("bullet", parent=S["body"], leftIndent=12, bulletIndent=2, spaceAfter=2.5,
                     alignment=TA_LEFT))
S.add(ParagraphStyle("quote", parent=S["body"], leftIndent=12, rightIndent=6, fontName="Body-Italic",
                     textColor=colors.HexColor("#3C4A51"), spaceBefore=3, spaceAfter=6))
S.add(ParagraphStyle("cell", fontName="Body", fontSize=8.3, leading=11.2, textColor=INK))
S.add(ParagraphStyle("cellhead", fontName="Body-Bold", fontSize=8.3, leading=11.2, textColor=BONE))
S.add(ParagraphStyle("code", fontName="Mono", fontSize=7.8, leading=10.5, textColor=INK))
S.add(ParagraphStyle("toc1", fontName="Body-Bold", fontSize=10.5, leading=16, textColor=SLATE))
S.add(ParagraphStyle("toc2", fontName="Body", fontSize=9, leading=13.5, textColor=colors.HexColor("#3C4A51"),
                     leftIndent=12))


# ----------------------------------------------------------------- inline markup
def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    """markdown inline -> reportlab paragraph markup"""
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+?)`", r'<font face="Mono" size="8.2">\1</font>', t)
    t = re.sub(r"\[(.+?)\]\((https?://[^\s)]+)\)",
               r'<a href="\2" color="#C97B3C"><u>\1</u></a>', t)
    return t


# ----------------------------------------------------------------- block parser
def parse(md, level_shift=0):
    """Return a list of flowables for a markdown string."""
    lines = md.split("\n")
    story, i = [], 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # fenced code
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            txt = "\n".join(buf)
            tbl = Table([[Preformatted(txt, S["code"])]], colWidths=[176 * mm])
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CODEBG),
                ("LINEBEFORE", (0, 0), (0, -1), 2.2, SAGE),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(tbl)
            story.append(Spacer(1, 4))
            continue

        # table
        if line.strip().startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[\s:|-]+$", "".join(row)):
                    rows.append(row)
                i += 1
            if rows:
                header, body = rows[0], rows[1:]
                data = [[Paragraph(inline(c), S["cellhead"]) for c in header]]
                data += [[Paragraph(inline(c), S["cell"]) for c in r] for r in body]
                ncol = len(header)
                avail = 176 * mm
                tbl = Table(data, colWidths=[avail / ncol] * ncol, repeatRows=1)
                st = [
                    ("BACKGROUND", (0, 0), (-1, 0), SLATE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
                    ("LINEBELOW", (0, 0), (-1, 0), 0.8, EMBER),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
                for k in range(1, len(data)):
                    if k % 2 == 0:
                        st.append(("BACKGROUND", (0, k), (-1, k), ZEBRA))
                tbl.setStyle(TableStyle(st))
                story.append(tbl)
                story.append(Spacer(1, 4))
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = min(len(m.group(1)) + level_shift, 6)
            txt = inline(m.group(2).strip())
            style = S[f"h{lvl}"] if f"h{lvl}" in S else S["h6"]
            p = Paragraph(txt, style)
            if lvl <= 3:
                p = KeepTogether([p])
            story.append(p)
            i += 1
            continue

        # hr
        if re.match(r"^\s*---+\s*$", line):
            story.append(Spacer(1, 2))
            t = Table([[""]], colWidths=[176 * mm], rowHeights=[0.8])
            t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.6, RULE)]))
            story.append(t)
            story.append(Spacer(1, 6))
            i += 1
            continue

        # blockquote
        if line.strip().startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            txt = " ".join(x for x in buf if x.strip())
            t = Table([[Paragraph(inline(txt), S["quote"])]], colWidths=[176 * mm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), ZEBRA),
                ("LINEBEFORE", (0, 0), (0, -1), 2.2, SAND),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]))
            story.append(t)
            story.append(Spacer(1, 4))
            continue

        # bullets / numbered
        m = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)$", line)
        if m:
            items = []
            while i < n and re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)$", lines[i]):
                items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lines[i]))
                i += 1
            numbered = bool(re.match(r"^\s*\d+\.", line))
            flows = [ListItem(Paragraph(inline(t), S["bullet"]), leftIndent=16)
                     for t in items]
            story.append(ListFlowable(
                flows,
                bulletType="1" if numbered else "bullet",
                start="1" if numbered else "\u2022",
                bulletFontName="Body", bulletFontSize=8, leftIndent=14,
                bulletColor=EMBER if not numbered else SLATE))
            story.append(Spacer(1, 4))
            continue

        # paragraph
        if line.strip():
            buf = [line.strip()]
            i += 1
            while i < n and lines[i].strip() and not re.match(
                    r"^\s*(#{1,6}\s|\||\s*>\s|\s*(?:[-*]|\d+\.)\s|```|---)", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            story.append(Paragraph(inline(" ".join(buf)), S["body"]))
            continue

        i += 1
    return story


# ----------------------------------------------------------------- source text
def read(name):
    return (BASE / name).read_text(encoding="utf-8")


def between(text, start, end=None):
    i = text.index(start)
    j = text.index(end) if end else len(text)
    return text[i:j].strip()


def shift_headings(text, by=1):
    out = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,5}) (.*)$", line)
        if m:
            line = "#" * min(len(m.group(1)) + by, 6) + " " + m.group(2)
        out.append(line)
    return "\n".join(out)


INTRO = """
## How to use this guide

This is the working document for building the visual identity of your bird photography account. Four parts:

1. **Reference study** — three of the best-known bird photographers, researched, with what each one actually does and what none of them do.
2. **Style directions** — nine options for your signature grade, each with real numbers. Pick one.
3. **The working style system** — the complete Lightroom workflow for the recommended default, variations, preset recipe, and the mistakes that give amateur edits away.
4. **Brand kit** — watermarks, profile photo, the mixed-crop system, palette and fonts, plus the handle shortlist.

Two notes on honesty. Your three attached reference images never reached this workspace, so Part 1 is built from published sources instead, with citations inline. And `@mathiphotography` could not be accessed — Instagram and Threads both return HTTP 403 to automated requests, so nothing about that account has been guessed.

## Decisions still open

| # | Decision | Default if you skip it |
|---|---|---|
| 1 | Style direction (Part 2) | **#1 Dust & Dawn**, with #8 Cyanotype as a Nov–Feb series and #7 Platinum one frame in nine |
| 2 | Handle (Part 5) | `@vatsal.photo` |
| 3 | Watermark | **Concept 2 — Flyway Glyph**, two-point, 10–12% on the feed |
| 4 | Profile photo | **#1 — bird eye macro** |
| 5 | Crop | **Mixed**, assigned by frame type (Part 4) |
| 6 | Cadence | 3 per week — Tue / Thu / Sun, 7–8pm IST, plus one Reel Friday |
"""

story = []
story.append(NextPageTemplate("main"))
story.append(PageBreak())
story += parse(INTRO, level_shift=0)

# Part 1
story.append(PageBreak())
story.append(Paragraph("Part 1 · Reference Study", S["h2"]))
story += parse(shift_headings(between(read("REFERENCE-STUDY.md"), "## PHOTOGRAPHER 1")), 0)

# Part 2
story.append(PageBreak())
story.append(Paragraph("Part 2 · Nine Style Directions", S["h2"]))
story += parse(between(read("STYLE-DIRECTIONS.md"), "You said the first four", "## 1 ·"))
story += parse(shift_headings(between(read("STYLE-DIRECTIONS.md"), "## 1 ·")), 0)

# Part 3
story.append(PageBreak())
story.append(Paragraph("Part 3 · The Working Style System", S["h2"]))
body = between(read("EDITING-STYLE-AND-BRAND.md"), "# STEP 3", "# STEP 4")
body = body.replace("# STEP 3 — YOUR SIGNATURE STYLE", "### The default: Dust & Dawn")
body = body.replace(
    "**Crop ratio:** **4:5 portrait for every feed post.**",
    "**Crop ratio:** 4:5 portrait is the default — it takes roughly 25% more screen area than a square. "
    "*You chose mixed crops, so follow the ratio-by-frame-type system in Part 4 instead of a single ratio.*")
story += parse(shift_headings(body, 1), 0)

# Part 4
story.append(PageBreak())
story.append(Paragraph("Part 4 · Brand Kit", S["h2"]))
story += parse(shift_headings(read("BRAND-KIT.md"), 1), 0)

# Part 5
story.append(PageBreak())
story.append(Paragraph("Part 5 · Handle Shortlist", S["h2"]))
story.append(Paragraph(
    "Full lists with reasoning are in <font face='Mono' size='8.2'>HANDLE-OPTIONS.md</font> through "
    "<font face='Mono' size='8.2'>HANDLE-OPTIONS-4.md</font>. Across all four batches, these seven are "
    "the ones worth checking first:", S["body"]))
story += parse(shift_headings(between(read("HANDLE-OPTIONS-4.md"),
                                      "## MY SHORTLIST ACROSS ALL FOUR BATCHES")), 0)


# ----------------------------------------------------------------- page furniture
def draw_cover(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(SLATE)
    canvas.rect(0, 0, w, h, stroke=0, fill=1)

    canvas.setFillColor(SAGE)
    canvas.setFont("Body", 8.5)
    canvas.drawString(22 * mm, h - 46 * mm, "B I R D   P H O T O G R A P H Y   ·   C A N O N   R 8   ·   G U J A R A T")

    canvas.setFillColor(BONE)
    canvas.setFont("Display-Bold", 32)
    canvas.drawString(21 * mm, h - 66 * mm, "Style & Brand")
    canvas.drawString(21 * mm, h - 78 * mm, "Guide")

    canvas.setFillColor(SAND)
    canvas.setFont("Body-Italic", 13)
    canvas.drawString(21 * mm, h - 90 * mm, "Dust & Dawn — and eight other ways to be recognisable")

    canvas.setFillColor(EMBER)
    canvas.rect(21 * mm, h - 99 * mm, 34 * mm, 2, stroke=0, fill=1)

    canvas.setFillColor(colors.HexColor("#A9B2AC"))
    canvas.setFont("Body", 9.5)
    canvas.drawString(21 * mm, h - 111 * mm, "Prepared for Vatsal Sharma")
    canvas.drawString(21 * mm, h - 117 * mm, "Editing signature · Lightroom workflow · brand identity · watermarks")

    canvas.setFillColor(SAGE)
    canvas.setFont("Body", 7)
    canvas.drawString(21 * mm, h - 132 * mm, "S I G N A T U R E   P A L E T T E")
    swatches = [SLATE, SAGE, SAND, EMBER, BONE]
    x = 21 * mm
    for c in swatches:
        canvas.setFillColor(c)
        canvas.rect(x, h - 146 * mm, 24 * mm, 9 * mm, stroke=0, fill=1)
        x += 27 * mm

    canvas.setStrokeColor(colors.HexColor("#2E3B42"))
    canvas.setLineWidth(0.6)
    canvas.line(21 * mm, 22 * mm, w - 21 * mm, 22 * mm)
    canvas.setFillColor(colors.HexColor("#6E7A74"))
    canvas.setFont("Body", 7.5)
    canvas.drawString(21 * mm, 16 * mm,
                      "Slate #16232A · Sage #7C8B84 · Sand #D9C7A7 · Ember #C97B3C · Bone #F2EBE0")
    canvas.restoreState()


def draw_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(16 * mm, h - 15 * mm, w - 16 * mm, h - 15 * mm)
    canvas.setFont("Body", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(16 * mm, h - 13 * mm, "VATSAL SHARMA · STYLE & BRAND GUIDE")
    canvas.drawRightString(w - 16 * mm, h - 13 * mm, "Bird Photography · Canon R8")
    canvas.setFont("Body", 8.5)
    canvas.setFillColor(SAGE)
    canvas.drawCentredString(w / 2, 11 * mm, str(canvas.getPageNumber() - 1))
    canvas.restoreState()


doc = BaseDocTemplate(str(OUT), pagesize=A4,
                      leftMargin=16 * mm, rightMargin=16 * mm,
                      topMargin=20 * mm, bottomMargin=18 * mm,
                      title="Vatsal Sharma — Bird Photography Style & Brand Guide",
                      author="Vatsal Sharma", subject="Editing style and brand identity")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
cover_frame = Frame(0, 0, A4[0], A4[1], id="cover")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
    PageTemplate(id="main", frames=[frame], onPage=draw_page),
])

print("Building PDF...")
doc.build(story)
print("Wrote", OUT.name, "-", OUT.stat().st_size, "bytes")
