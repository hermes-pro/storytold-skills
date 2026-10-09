---
name: storytold
description: "Pick the right storytold Crafting App for a creative task: vector art, photo editing, RAW development, motion graphics, video, layout, PDF, documents, spreadsheets, slides, audio, CAD. Routes to the app's own skill."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Photo, Video, Audio, Office, CAD, MCP, Router]
    related_skills: [storytold-install, vectorcraft, photocraft, lightcraft, effectcraft, filmcraft, designcraft, pdfcraft, wordcraft, gridcraft, deckcraft, soundcraft, cadcraft]
---

# storytold Crafting Apps: which one?

The storytold Crafting Apps are twelve free, open-source creative tools. Each has a desktop app, a CLI and an
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

Bigger jobs often combine apps: build a chart in GridCraft and place it in DeckCraft or DesignCraft, or
design a logo in VectorCraft and animate it in EffectCraft. Use each app's native save for its master, and
pass files between apps in open formats (SVG, PDF, PNG, WAV, MP4, CSV).

## Setup

If the app you need has no `mcp_<app>_*` tools and `<app>-cli --version` fails, load the `storytold-install`
skill and run `setup <app>`. It installs the app, puts it on PATH, checks the MCP server and registers it with
Hermes.
