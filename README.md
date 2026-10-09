# storytold skills for Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) skills for the
[storytold Crafting Apps](https://github.com/storytold): twelve free, open-source creative tools written in Rust.
Each app ships a desktop app, a CLI and an MCP server.

The skills give an agent three things:

- **Install and wiring** (`storytold-install`): download the apps, put them on PATH, check that each MCP server
  answers, and register it with Hermes.
- **Picking the right tool** (`storytold`): a router that maps a creative task to the right app.
- **Knowing how to use it** (one skill per app): the app's mental model, MCP tools, recipes, formats, CLI
  one-shots, pitfalls and how to verify the result.

## Quick start

Install the `storytold` skill:

```bash
hermes skills install hermes-pro/storytold-skills/storytold --yes
```

Then tell Hermes:

> Install the storytold skills.

The `storytold` skill tells the agent how to install the other 13 skills. Then start a new session so they load,
and tell Hermes:

> Set up the storytold Crafting Apps.

The agent downloads the apps, puts them on PATH, checks that their MCP servers answer, and registers them with
Hermes. After one more new session (or `/reload-mcp`), the app tools are loaded and the agent picks the right
app for each creative task.

The agent will ask you before it installs `storytold-install` with `--force`. Hermes scans skills from community
sources and blocks any that match risky code patterns. The app skills and the router pass that scan.
`storytold-install` doesn't, because its job is to:

- persist a PATH entry (the Windows registry, or `~/.profile` / `~/.bashrc` / `~/.zshrc`)
- run the app CLIs and `hermes mcp add`
- read `STORYTOLD_*` / `GITHUB_TOKEN` environment variables

To review it first, read [`storytold_tools.py`](storytold-install/scripts/storytold_tools.py), or run
`hermes skills inspect hermes-pro/storytold-skills/storytold-install`.

## Skills

| Skill | App | For |
|---|---|---|
| [`storytold`](storytold/SKILL.md) | (router) | Choosing the app for a creative task |
| [`storytold-install`](storytold-install/SKILL.md) | (all) | Install, PATH, MCP check, Hermes registration |
| [`vectorcraft`](vectorcraft/SKILL.md) | VectorCraft (Illustrator-style) | Logos, icons, posters, illustration, SVG / PDF / EPS |
| [`photocraft`](photocraft/SKILL.md) | PhotoCraft (Photoshop-style) | Photo editing, retouching, compositing, PSD |
| [`lightcraft`](lightcraft/SKILL.md) | LightCraft (Lightroom-style) | RAW development, culling, presets, batch export |
| [`effectcraft`](effectcraft/SKILL.md) | EffectCraft (After Effects-style) | Motion graphics, animated titles, lower thirds |
| [`filmcraft`](filmcraft/SKILL.md) | FilmCraft (Premiere Pro-style) | Video editing, transitions, titles, captions, MP4 |
| [`designcraft`](designcraft/SKILL.md) | DesignCraft (InDesign-style) | Brochures, newsletters, multi-page layout, print PDF |
| [`pdfcraft`](pdfcraft/SKILL.md) | PdfCraft (Acrobat-style) | Merge/split, annotate, forms, redact, sign PDFs |
| [`wordcraft`](wordcraft/SKILL.md) | WordCraft (Word-style) | Letters, reports, .docx |
| [`gridcraft`](gridcraft/SKILL.md) | GridCraft (Excel-style) | Spreadsheets, formulas, charts, .xlsx / .csv |
| [`deckcraft`](deckcraft/SKILL.md) | DeckCraft (PowerPoint-style) | Slide decks, .pptx |
| [`soundcraft`](soundcraft/SKILL.md) | SoundCraft (Pro Tools-style) | Podcast editing, mixing, mastering, sound design |
| [`cadcraft`](cadcraft/SKILL.md) | CADCraft (AutoCAD-style) | Floor plans, technical drawings, DXF / DWG |

Each app skill has a `references/` folder with that app's full command, effect or function catalog, generated
from the live MCP server. The skills tell the agent to grep these files rather than read them whole.

## Install the skills

The [Quick start](#quick-start) lets the agent install them. To install all 14 yourself in one line:

```bash
for s in storytold-install storytold vectorcraft photocraft lightcraft effectcraft filmcraft designcraft pdfcraft wordcraft gridcraft deckcraft soundcraft cadcraft; do hermes skills install "hermes-pro/storytold-skills/$s" --yes --force; done
```

```powershell
'storytold-install','storytold','vectorcraft','photocraft','lightcraft','effectcraft','filmcraft','designcraft','pdfcraft','wordcraft','gridcraft','deckcraft','soundcraft','cadcraft' | % { hermes skills install "hermes-pro/storytold-skills/$_" --yes --force }
```

`--force` is only needed for `storytold-install` (see [Quick start](#quick-start)). Single skills install the
same way, e.g. `hermes skills install hermes-pro/storytold-skills/vectorcraft`.

You can also add the repo as a tap with `hermes skills tap add hermes-pro/storytold-skills`. Taps look under
`skills/` by default and these skills live at the repo root, so point that tap's `path` at the root in
`~/.hermes/skills/.hub/taps.json`.

To use a local checkout, copy the skill folders into your Hermes skills directory (`~/.hermes/skills/<category>/`,
or `%LOCALAPPDATA%\hermes\skills\` on Windows).

## Install the apps

Once the skills are installed, ask Hermes to set up the Crafting Apps, or run the helper yourself. It needs
Python 3.9+ and nothing else:

```bash
python storytold-install/scripts/storytold_tools.py setup            # all twelve apps
python storytold-install/scripts/storytold_tools.py setup vectorcraft photocraft
```

`setup` does four things:

1. **Install:** downloads each app's latest GitHub release for this OS and CPU, checks it against the release's
   `SHA256SUMS.txt`, and unpacks it.
2. **PATH:** links `<app>` and `<app>-cli` into one bin directory and adds it to the persistent PATH if it
   isn't there yet.
3. **Verify:** runs an MCP handshake (`initialize` + `tools/list`) against every server.
4. **Register:** adds each server to Hermes with `hermes mcp add` and enables all its tools.

Then start a new Hermes session or run `/reload-mcp`. The tools appear as `mcp_<app>_<tool>`.

| | Windows | Linux / FreeBSD | macOS |
|---|---|---|---|
| Apps | `%LOCALAPPDATA%\storytold\apps\` | `~/.local/share/storytold/apps/` | `~/Library/Application Support/storytold/apps/` (CLI only) |
| On PATH | `%LOCALAPPDATA%\storytold\bin` | `~/.local/bin` | `~/.local/bin` |

The helper also has the subcommands `status`, `install`, `path`, `verify` and `register` (with `--replace`).
See [`storytold-install/SKILL.md`](storytold-install/SKILL.md) for those, for the environment variables that
change the locations, and for the per-app MCP arguments. PhotoCraft gets file-access roots and LightCraft gets a
persistent library.

## How the skills were tested

Every recipe marked **(tested)** was run against the released apps through their MCP servers or CLIs. The
outputs were checked by rendering and looking at them, by reading values back, or by measuring them with
ffprobe or ffmpeg. The versions tested were:

vectorcraft 0.7.0 · photocraft 0.5.0 · lightcraft 0.4.0 · effectcraft 0.6.0 · filmcraft 0.4.0 · designcraft 0.4.0 ·
pdfcraft 0.4.0 · wordcraft 0.3.0 · gridcraft 0.3.0 · deckcraft 0.3.0 · soundcraft 0.3.0 · cadcraft 0.3.0

Bugs and quirks found along the way, with their exact error text, are in each skill's **Pitfalls** section.
Each skill also says what wasn't tested. When an app updates, regenerate its `references/` from the live
server and re-run its recipes.

## Repository layout

```
<skill>/
├── SKILL.md          # frontmatter (name, description, platforms, metadata.hermes) + instructions
├── references/       # generated catalogs (app skills)
└── scripts/          # helper scripts (storytold-install)
```

## License

MIT. See [LICENSE](LICENSE). The Crafting Apps themselves are licensed separately by their own repositories.
