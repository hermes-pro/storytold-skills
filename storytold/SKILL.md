---
name: storytold
description: "Pick the right storytold Crafting App for a creative task: vector art, photo editing, RAW development, motion graphics, video, layout, PDF, documents, spreadsheets, slides, audio, 2D CAD, 3D parametric CAD, UI design, procedural materials, 3D texture painting, or studying how a website, app or game works to build your own. Routes to the app's own skill."
version: 0.3.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Photo, Video, Audio, Office, CAD, 3D, UI, MCP, Router]
    related_skills: [storytold-install, vectorcraft, photocraft, lightcraft, effectcraft, filmcraft, designcraft, pdfcraft, wordcraft, gridcraft, deckcraft, soundcraft, cadcraft, figcraft, solidcraft, materialcraft, texturecraft, craft-anything]
---

# storytold Crafting Apps: which one?

The storytold Crafting Apps are seventeen free, open-source creative tools. Each has a desktop app, a CLI and an
MCP server (`<app>-cli mcp`, which Hermes exposes as `mcp_<app>_*` tools). Each also has its own skill. Use
this table to pick one, then **load that app's skill** before you start working.

## Pick by output

| You need to produce… | App | Skill |
|---|---|---|
| A logo, icon, illustration, poster, flyer, badge, infographic, SVG | VectorCraft | `vectorcraft` |
| An edited photo, retouch, composite, mockup, banner from photos, PSD | PhotoCraft | `photocraft` |
| Developed RAW photos, a consistent look across many photos, a catalog, batch exports | LightCraft | `lightcraft` |
| An animated title, lower third, motion graphic, animated GIF, logo animation | EffectCraft | `effectcraft` |
| An edited video: cuts, sequence, titles, transitions, an MP4 export | FilmCraft | `filmcraft` |
| A multi-page layout: brochure, magazine, newsletter, book, print-ready PDF | DesignCraft | `designcraft` |
| Changes to an existing PDF: merge/split, annotate, fill forms, redact, watermark, sign, compare | PdfCraft | `pdfcraft` |
| A text document: letter, report, essay, .docx | WordCraft | `wordcraft` |
| A spreadsheet: budget, table with formulas, chart, .xlsx/.csv | GridCraft | `gridcraft` |
| A slide deck or presentation, .pptx | DeckCraft | `deckcraft` |
| Audio: podcast edit, mix, mastering, sound design, WAV/MP3 | SoundCraft | `soundcraft` |
| A precise technical drawing: floor plan, part, DXF/DWG, dimensions | CADCraft | `cadcraft` |
| A UI design: app or web screen, wireframe, mockup, prototype, component library, design tokens, .fig | FigCraft | `figcraft` |
| A 3D part or assembly: parametric solid model, enclosure, bracket, STEP / STL for machining or 3D printing | SolidCraft | `solidcraft` |
| A procedural material: tiling PBR texture maps (base color, normal, roughness, height) built as a node graph | MaterialCraft | `materialcraft` |
| Painted textures on a 3D model: bake maps, paint PBR channels on a mesh, export a texture set | TextureCraft | `texturecraft` |
| An understanding of how a website, app or game works, and your own version of it, checked against the original | Craft Anything | `craft-anything` |

## Tie-breakers

- **Single page vs many pages:** one page of art is VectorCraft. Several pages with flowing text is DesignCraft.
- **Pixels vs paths:** photographs and painted textures are PhotoCraft. Shapes that must scale are VectorCraft.
- **One photo vs a shoot:** one image, layered, is PhotoCraft. Many photos with the same adjustments is LightCraft.
- **Motion:** an edit of footage over time is FilmCraft. Animating graphics and type is EffectCraft. Render the motion
  graphic in EffectCraft and cut it into the edit in FilmCraft.
- **PDF:** to *create* a designed PDF, use DesignCraft, VectorCraft, WordCraft or DeckCraft and export. To *change*
  an existing PDF, use PdfCraft.
- **Documents:** prose is WordCraft. Numbers and calculations are GridCraft. Something to present is DeckCraft.
- **Drawings to scale** with real units and dimensions are CADCraft, not VectorCraft.
- **Screens vs artwork:** app and web screens, components with variants, auto layout and clickable prototypes are
  FigCraft. A standalone logo, icon or illustration is VectorCraft. Draw the icon in VectorCraft and import the SVG
  into FigCraft.
- **2D vs 3D CAD:** a drawing with views and dimensions (DXF / DWG) is CADCraft. A solid part you can rotate,
  measure, 3D print or machine (STEP / STL) is SolidCraft.
- **Materials vs painting:** a tiling material made from nodes (stone, fabric, metal) is MaterialCraft. Painting
  wear, decals and colour onto one particular model is TextureCraft, which can load MaterialCraft's materials.
  A single flat image edit is PhotoCraft.
- **Learn and rebuild vs design from scratch:** to study how existing software works and build your own version of
  it, use Craft Anything. It builds your own original work, not a copy of someone else's assets or branding. To
  design a new UI from scratch, use FigCraft.

Bigger jobs often combine apps: build a chart in GridCraft and place it in DeckCraft or DesignCraft, or
design a logo in VectorCraft and animate it in EffectCraft. Use each app's native save for its master, and
pass files between apps in open formats (SVG, PDF, PNG, WAV, MP4, CSV).

## Setup

### Install the other skills

When the user asks to install the storytold skills (or an app skill above isn't available), install them from
GitHub. Install each one on its own, because `hermes skills install` takes one skill per call:

```bash
hermes skills install hermes-pro/storytold-skills/<skill> --yes
```

The skills are `storytold-install`, `vectorcraft`, `photocraft`, `lightcraft`, `effectcraft`, `filmcraft`,
`designcraft`, `pdfcraft`, `wordcraft`, `gridcraft`, `deckcraft`, `soundcraft`, `cadcraft`, `figcraft`, `solidcraft`,
`materialcraft`, `texturecraft` and `craft-anything`. Skip any that
`hermes skills list` already shows.

The 17 app skills pass Hermes' security scan. **`storytold-install` is blocked** ("community source + caution
verdict"), because its job is to persist a PATH entry, run the app CLIs and `hermes mcp add`, and read
`STORYTOLD_*` / `GITHUB_TOKEN` environment variables. Tell the user that, and point them to
`hermes skills inspect hermes-pro/storytold-skills/storytold-install`. Re-run it with `--force` **only after the
user agrees**. Then ask the user to start a new session so the new skills load.

### Install the apps

If the app you need has no `mcp_<app>_*` tools and `<app>-cli --version` fails, load the `storytold-install`
skill and run `setup <app>`, or `setup` on its own for all seventeen. It installs the app, puts it on PATH, checks
the MCP server and registers it with Hermes.
