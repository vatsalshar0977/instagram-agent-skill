# Vendored plugins

These are **snapshots of other people's Claude Code plugins**, copied into this
repo because this session is Arena Agent Mode, where `/plugin` commands cannot run.

They are here as reference and as markdown you can follow by hand. They do not
auto-update — pull a fresh copy from the source repo if you want the latest.

| Plugin | Version | Source | Folder |
|---|---|---|---|
| `image-production@danielrosehill` | 2.3.2 | [repo](https://github.com/danielrosehill/Claude-Image-Production-Plugin) | `image-production/` |

## Installing for real (in Claude Code)

```bash
/plugin marketplace add https://github.com/danielrosehill/Claude-Code-Plugins
/plugin install image-production@danielrosehill
```

The marketplace repo (181 plugins) is
[danielrosehill/Claude-Code-Plugins](https://github.com/danielrosehill/Claude-Code-Plugins).
Worth browsing for the `media-library` and `video-editing` companions.

## Notes, defects and sandbox status

See `image-production/INSTALLED.md` — including two defects found in this
snapshot (a missing `workspace-setup` skill referenced by `setup-workspace`,
and a README/plugin.json version mismatch), and which dependencies actually
exist in this sandbox (`ImageMagick` yes, `exiftool` no).
