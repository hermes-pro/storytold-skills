---
name: storytold-install
description: "Install the storytold Crafting Apps (VectorCraft, PhotoCraft, FilmCraft, …) on PATH and wire their MCP servers into Hermes."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Illustration, Photo, Video, Audio, Office, CAD, MCP]
    related_skills: [storytold]
---

# storytold Crafting Apps

The [storytold](https://github.com/storytold) Crafting Apps are free, open-source, clean-room creative
tools written in Rust. Every release ships a desktop app `<app>` and an automation CLI `<app>-cli`.
`<app>-cli mcp` is a stdio MCP server that can drive every menu item, tool, panel and export.

| App | What it is |
|---|---|
| `vectorcraft` | Vector illustration (Illustrator-style) |
| `photocraft` | Raster image editing (Photoshop-style) |
| `lightcraft` | Photo development and catalog (Lightroom-style) |
| `effectcraft` | Motion graphics and compositing (After Effects-style) |
| `filmcraft` | Video editing (Premiere Pro-style) |
| `designcraft` | Page layout and publishing (InDesign-style) |
| `pdfcraft` | PDF viewing and editing (Acrobat-style) |
| `wordcraft` | Word processing (Word-style) |
| `gridcraft` | Spreadsheets (Excel-style) |
| `deckcraft` | Presentations (PowerPoint-style) |
| `soundcraft` | Audio editing and mixing (Pro Tools-style) |
| `cadcraft` | Computer-aided design and drafting (AutoCAD-style) |

## When to Use

- The user asks to install, update or set up any storytold / Crafting App (by name or "the craft apps").
- The user wants to create or edit vector art, photos, video, audio, documents, spreadsheets, slides,
  PDFs or CAD drawings, and a Crafting App is the tool for it.
- A `<app>-cli` command is "not found", or a storytold MCP server fails to start.

## Quick Reference

All of the setup goes through one stdlib-only helper (Python 3.9+, no packages):

```bash
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py status              # installed vs latest, PATH state
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py install [APP ...]   # download + checksum + link + PATH
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py path                # only add the bin dir to PATH
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py verify  [APP ...]   # MCP handshake per CLI
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py register [APP ...]  # hermes mcp add <app>
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py setup   [APP ...]   # install + verify + register
```

Leave `APP` out to act on all twelve apps. Every command prints one JSON object per line.

| Where | Windows | Linux / FreeBSD | macOS |
|---|---|---|---|
| Release asset | `<app>-<ver>-windows-<arch>-portable.zip` | `<app>-<ver>-<os>-<arch>.tar.gz` | `<app>-cli-<ver>-macos-universal.zip` (CLI only) |
| Unpacked to | `%LOCALAPPDATA%\storytold\apps\<app>\<ver>` | `~/.local/share/storytold/apps/…` | `~/Library/Application Support/storytold/apps/…` |
| On PATH as | `%LOCALAPPDATA%\storytold\bin` (hard links) | `~/.local/bin` (symlinks) | `~/.local/bin` (symlinks) |
| PATH persisted in | `HKCU\Environment\Path` | `~/.profile`, `~/.bashrc`, `~/.zshrc`, fish `conf.d` | same |

To change the locations, set `STORYTOLD_HOME` (install root) and `STORYTOLD_BIN` (bin dir). Set `GITHUB_TOKEN`
if the GitHub API rate limit (60 requests an hour without a token) gets in the way.

## Procedure

1. **Check first.** Run `status`. An app counts as present when its `<app>-cli` is on PATH, whether
   this skill installed it or an MSI, .deb or Flatpak did. Don't reinstall an app that's already there
   unless the user asks, or `latest` is newer than `installed`.
2. **Install.** Run `install` with the apps the user wants. Leave `APP` out to install all twelve, about 1 GB of
   downloads. For each app it finds the latest GitHub release, downloads the asset for this OS and CPU,
   checks it against the release's `SHA256SUMS.txt`, unpacks it and links `<app>` and `<app>-cli` into the bin
   dir. Then it adds the bin dir to the persistent PATH unless it's already there. Running it again does no
   harm: an up-to-date app is skipped, and a PATH entry that's already there isn't added twice.
3. **Verify the MCP servers.** Run `verify`. For each CLI it starts the MCP server with the same arguments
   Hermes will use (below), and sends `initialize`, `notifications/initialized` and `tools/list`. It reports the
   server name and version, the protocol, the number of tools and the `args`. The exit code is 0 only when every
   server answers with at least one tool.
4. **Register with Hermes** (if the user wants the tools in Hermes). Run `register`. It runs
   `hermes mcp add <app> --command <abs path to bin>/<app>-cli --args <mcp args>` and enables all tools. Hermes
   probes the server before saving, so this is a second end-to-end check. Then tell the user to start a
   new session or run `/reload-mcp`. `hermes mcp test <app>` re-checks a single server later. An entry
   registered before these args existed is left alone: update it with `register <app> --replace`.

   | App | MCP args | Why |
   |---|---|---|
   | most apps | `mcp` | headless in-process engine |
   | `photocraft` | `mcp --automation-read-root <HOME> --automation-write-root <HOME>` | without roots it can't open or save files. Paths are relative to HOME. Override HOME with `STORYTOLD_PHOTOCRAFT_ROOT` |
   | `lightcraft` | `mcp --library <install root>/lightcraft-library` | without a library the catalog lives in memory only. Override with `STORYTOLD_LIGHTCRAFT_LIBRARY` |
5. **Report.** List the installed versions, PATH changes, MCP results and anything that failed, with its
   `error`.

## Using the apps

- **App skills.** Each app has its own skill (`vectorcraft`, `photocraft`, …), and the `storytold` skill picks
  the right app for a task. Load the app's skill before you work in it.
- **MCP modes.** Bare `<app>-cli mcp` starts every app and runs an in-process engine (VectorCraft first
  tries a desktop app on `127.0.0.1:7979`). To watch a live desktop app instead, start it with
  `<app> --control <port>` and pass the app's own flag. The flags differ from app to app: `--connect`
  (vectorcraft, gridcraft, designcraft, deckcraft) or `--bridge` (photocraft, effectcraft). Check
  `<app>-cli --help` for the exact form before relying on it.
- **Without MCP.** Most CLIs have `run` (headless batch of commands plus exports), `convert IN OUT`,
  `info FILE`, `commands` (the command catalog as JSON) and `bench`. `<app>-cli --help` lists them for each app.
- Each repository's `docs/mcp.md` and `docs/control-protocol.md` document the tools, resources and prompts,
  e.g. https://github.com/storytold/vectorcraft/blob/main/docs/mcp.md.

## Pitfalls

- **PATH changes don't reach running processes.** New terminals see the updated PATH. Hermes and its
  terminal tool keep the PATH they started with, so call the CLI by its absolute path (as `status` and
  `verify` print it) until Hermes restarts. MCP registration always stores the absolute path.
- **Updating while a server runs (Windows).** Windows can't delete an exe that's running. `install` renames
  the busy link to `<name>.old-<timestamp>` and puts the new one in place. Restart the MCP server, or
  Hermes, to pick up the new version.
- **Microsoft Store Python (Windows)** redirects everything written under `%LOCALAPPDATA%` into its own
  package folder, where no other program sees it. The helper detects this and re-runs itself with the
  first regular `python.exe` on PATH, or refuses to run if there isn't one. Prefer Hermes' own Python.
- **macOS** releases have only the CLI as a zip. The desktop app is a `.dmg`, so point the user to
  `https://github.com/storytold/<app>/releases/latest` to install the GUI.
- **Name clash.** `register` won't overwrite an existing Hermes MCP entry with the same name. Pass
  `--replace` to update it.
- **Stdout is protocol-only.** The servers log to stderr. When `verify` fails it includes `stderr_tail`,
  so read that before retrying.

## Verification

```bash
python ${HERMES_SKILL_DIR}/scripts/storytold_tools.py verify --json   # every app: "ok": true
<app>-cli --version                                                  # from a NEW shell: PATH works
hermes mcp list                                                       # registered servers show as enabled
hermes mcp test vectorcraft                                           # Hermes-side handshake
```
