# Vendored copy — image-production@danielrosehill v2.3.2

**Source:** https://github.com/danielrosehill/Claude-Image-Production-Plugin
**Marketplace:** https://github.com/danielrosehill/Claude-Code-Plugins
**Version:** 2.3.2 · **Licence:** MIT · **Author:** Daniel Rosehill
**Vendored:** 2026-10-24 (a snapshot — it will not auto-update)

## Why it's here as a copy

This session is Arena Agent Mode, not Claude Code, so `/plugin install` cannot run.
The plugin's skills and commands are plain markdown, so they are still useful as
reference and can be followed manually. To use them as real slash commands:

```bash
/plugin marketplace add https://github.com/danielrosehill/Claude-Code-Plugins
/plugin install image-production@danielrosehill
```

## What's inside

`commands/` — 21 slash commands: apply-filters, batch-resize, bg-removal,
compress-images, convert-to-webp, crop-images, dedupe, group-by-camera,
group-by-time, images-here, install-gimp-plugin, organize-by-aspect-ratio,
organize-by-format, organize-by-orientation, organize-by-resolution,
scrub-small-images, separate-photos-and-video, setup-workspace, sort-media

`skills/` — 28 skills: read-metadata, set-metadata, batch-set-copyright,
scrub-metadata, fast-resize, fast-thumbnail, optimize-png, optimize-jpeg,
convert-to-avif, images-to-pdf, pdf-to-images, pdf-extract-embedded-images,
upscale-image, to-jxl, from-jxl, transcode-jpeg-to-jxl-lossless, svg-to-raster,
vectorize, auto-white-balance, auto-tone, auto-deskew, new-project, new-workflow,
open-workspace, install-deps, ai-graphics, nano-tech-diagrams

## Two defects found in this snapshot — worth knowing

1. `plugin.json` lists `./skills/workspace-setup/SKILL.md` and
   `./skills/web-ready/SKILL.md`, but **neither file exists in the repo**.
   That means `commands/setup-workspace.md` (which calls the `workspace-setup`
   skill) will fail. Workaround: create the workspace folders manually —
   which is what `photos/` in this repo already is.
2. The README documents version 2.0.0 while `plugin.json` says 2.3.2.

## Dependencies in THIS sandbox

| Tool | Status | Needed for |
|---|---|---|
| ImageMagick (`identify`, `convert`) | **available** | dimension probing, resize, crop, filters |
| `exiftool` | **missing** (apt unreachable) | metadata read/write, EXIF date grouping, scrub |
| `libvips` (`vips`, `vipsthumbnail`) | missing | fast-resize, fast-thumbnail |
| `heif-convert`, `avifenc`, `cjxl`, `oxipng`, `pngquant`, `jpegoptim` | missing | format conversion, optimisation |
| `uv` + plugin venv (`Pillow`, `imagehash`) | missing (Pillow is present only in a local venv) | perceptual dedupe |

**Bottom line:** the organisation and conversion commands that rely on ImageMagick
will work here. Anything needing `exiftool` (the metadata group) will not, until
`exiftool` can be installed.
