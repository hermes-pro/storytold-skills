---
name: designcraft
description: "Page layout and publishing with DesignCraft (InDesign-style): brochures, newsletters, magazines, flyers, booklets, reports, certificates and data-merged cards. Multi-page documents with parent pages, page numbers, text frames, columns, paragraph / character styles, images, tables, text wrap; export print PDF, PNG, IDML, EPUB, HTML."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Layout, Publishing, Typography, Brochure, Newsletter, Magazine, PDF, MCP]
    related_skills: [storytold, storytold-install, vectorcraft, photocraft, pdfcraft, wordcraft, deckcraft]
---

# DesignCraft

DesignCraft is a free, open-source clean-room take on Adobe InDesign (storytold Crafting Apps). An agent
drives it through an MCP server (`designcraft-cli mcp`) or CLI one-shots. It has a Knuth–Plass paragraph
composer, hyphenation, real styles and parent pages. Its exported PDFs embed subset fonts and keep text as text.

## When to Use

Use it for **typeset, multi-page or print-ready documents**:

- newsletters, brochures, tri-folds, flyers, posters with body text, magazines, booklets, reports, menus, programmes
- anything that needs parent pages (running heads, folios, page numbers), columns, styles or text flowing across pages
- data merge: certificates, badges, name cards and labels from a CSV or `.xlsx` file
- converting to or from IDML, and exporting EPUB or HTML from a layout

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A logo, icon or illustration (vector art to place into the layout) | `vectorcraft` |
| Retouching or compositing the photos you place | `photocraft` |
| Editing, merging, redacting or filling an *existing* PDF | `pdfcraft` |
| A plain word-processed document (letter, memo, manuscript) | `wordcraft` |
| Slides | `deckcraft` |

## Setup

1. If tools named `mcp_designcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `designcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup designcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI (`script`/`run`, see **CLI** below).

The MCP server is **headless** by default: an in-process engine with a CPU renderer. It starts with an empty
Letter document. The window-only tools (`screenshot`, `click`, `drag`, `menu_list`, `ui_inspect`, `ui_set`,
`dialog_*`) return an error in this mode. For the user to watch live, start `designcraft --control 7979` and
run the server as `designcraft-cli mcp --connect 7979` (tested).

## Mental Model

- **Units are points** (72 pt = 1 in). **y points down.** Coordinates are in **spread space**. On a
  single-page spread the page's top-left is (0, 0). On a facing spread the right page starts at x = page width
  (612 for Letter). `inspect_document` lists each spread's pages with their bounds.
- **Page indices** are 0-based in `render_page`, `export_png`, `layout.pages.*` and the CLI's `--page`.
  `file.exportPdf {pages}`, `layout.section` and `layout.pageSize` take 1-based numbers.
- **Every action is a command** (444 of them). Run one with `execute {command, params}` or a list with `batch`.
  Find commands with `list_commands {filter}`, or grep `references/commands.md`.
- **Frames hold content.** A text frame shows a **story**. A story can thread through several frames, and
  `inspect_document → stories` shows `frames` and `overset`. A graphic frame holds a placed image.
- **Parent pages** (masters) are spreads of their own, addressed as `spread: {"kind": "parent", "index": 0}`.
  Every new page uses `A-Parent` unless you change it with `layout.pages.applyParent {pages, parent: "A"|null}`.
- **Selection matters.** Commands without `ids` act on the selection. `frame.create` with text leaves a text
  caret in the new frame. Text commands (`type.char`, `style.*.apply`, `text.insert`) act on the caret or the selected text.

## Tools (Hermes names them `mcp_designcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `new_document` | `preset` (`Letter`, `A4`, `A5`, `Tabloid`…) or `width`/`height`, `pages`, `facingPages`, `margins` (number or `{top,bottom,inside,outside}`), `columns`, `gutter`, `bleed`, `title` (becomes the PDF Title). `sample: true` opens the demo magazine |
| `execute {command, params}` | Any command. Returns its result, e.g. `frame.create` → `{id, story}` |
| `batch {commands}` | Several commands in one call, stopping at the first error (`failedIndex`). `"$N.path"` reuses step N's result, e.g. `"$0.story"`, `"$7.0.start"` |
| `inspect_document` | Pages, spreads, items (ids, bounds, fill, story, columns), stories (frames, overset), styles, swatches, selection |
| `get_story` / `set_story_text` | Read a story's text (`overset: null` means it fits) / replace it (`\n` = new paragraph, keeps the first paragraph's format) |
| `place_image` | PNG/JPEG/WebP/GIF/TIFF into `frame`, the selected empty frame, or a new frame at `x, y, width` (height follows the aspect ratio) |
| `render_page {page, scale?, path?}` | Render a page to PNG so you can **look** at it (scale 1 = 72 ppi) |
| `export_png {page, path, scale?}` | Write one page as PNG/JPEG (default scale 2) |
| `save_document` / `open_document` | Native `.designcraft` files (`file.open` also reads `.idml`) |
| `list_commands {filter}` | Look up command ids and params |
| `select_tool`, `pointer`, `key`, `type_text` | Drive tools like a mouse and keyboard would (rarely needed) |

Resources: `designcraft://document` (same as `inspect_document`) and `designcraft://commands`.

## Text and Styles

- **Create a text frame:** `frame.create {rect: [x0,y0,x1,y1], content: "text", text: "…"}`. Pass `caret: false`
  when you don't want the caret left inside it. `content` defaults to `graphic`. Use `unassigned` for a plain coloured
  shape, then `object.fill {swatch}` and `object.stroke {swatch: "[None]"}`. Unassigned shapes get a 1 pt black stroke.
- **Columns** belong to the frame: `object.textFrameOptions {ids?, columns, gutter, inset?, verticalJustification?}`.
- **Threading across pages:** there is no "link frames" command. Flow long text with
  `file.place {path, autoflow: true}`. It adds pages, each with a threaded margin-sized frame, until the story fits.
  For extra frames on the same page, use `columns` instead.
- **Styles:** `style.paragraph.create {name, basedOn?, nextStyle?, para: {…}, chars: {…}}`,
  `style.character.create {name, chars}`, then `style.paragraph.apply {name}` / `style.character.apply {name}` on the
  caret or selected text. `style.paragraph.edit {name: "[Basic Paragraph]", …}` sets the document's default body text.
  - `chars` keys: `fontFamily`, `fontStyle` ("Bold", "Italic"), `size`, `leading: {kind:"points", value}` or
    `{kind:"auto"}`, `tracking`, `fill` (a swatch name), `capitalization`, `underline`, `baselineShift`.
  - `para` keys: `align` (`left|center|right|leftJustified|…`), `spaceBefore`, `spaceAfter`, `firstLineIndent`,
    `leftIndent`, `keepWithNext`, `dropCapLines`, `hyphenate`.
  - Unknown keys fail with `unknown attribute`, so you can't silently misspell one. `type.selectionAttrs` lists every key with its current value.
- **Selecting text:** `edit.selectAll` (while a caret is in a story) selects the whole story. Use `text.select {story, anchor, focus}` for a range.
  Offsets are **UTF-8 byte** offsets, as `find.find {find, grep?}` returns them: `[{story, start, end, text}]`.
- **Fonts:** Source Serif 4 (the default) and Source Sans 3 are bundled, and installed system fonts work too. Check with
  `font.list`: every face reports `missing` and `source`.
- **Special characters in text:** page number ``, next/previous page number ``/``, section
  marker ``, column break ``, frame break ``, page break ``, forced line break ` `.

## Colour, Images, Objects

- **Swatches:** `swatch.create {name, color: "#rrggbb" | {c,m,y,k} (0–100) | [r,g,b]}`. Use CMYK for print. `preflight.run`
  warns `RGB swatch in a print document`. Use `object.fill {swatch, tint?: 0..1}` on frames, and the `fill` char attr on text.
- **Images:** `place_image`, then `object.fit {mode: fillProportionally|fitProportionally|centerContent|fitFrameToContent}`.
  Placing into an ellipse frame crops the image to a circle (tested).
- **Text wrap:** `object.textWrap {mode: boundingBox|contour|jumpObject|jumpToNextColumn, offset}` on the image.
  Text frames under it reflow around it.
- **Arrange and align:** `object.align {edge, to: margins|page}`, `object.distribute`, `object.group`, `object.arrange`,
  `transform.move|rotate|scale`, `edit.stepAndRepeat`. Effects: `object.dropShadow`, `object.opacity`, `object.cornerOptions`.
- **Tables:** type tab-separated lines, `edit.selectAll`, `table.convertFromText {columnSeparator: "tab"}`; then
  `table.select {story, rows:[0,0], what:"row"}` + `table.setCell {fill, tint}`. `table.get {story}` reads it back.

## Procedure

1. **Plan** the page size, margins, grid (columns), 2–4 swatches, and a style sheet (Headline, Subhead, Body, Caption, Folio).
2. **Set up:** `new_document {…, facingPages: false}` for flyers and single sheets. Keep `facingPages: true` for
   bound booklets, but then remember that the right-hand pages are offset by the page width.
3. **Styles and swatches first**, including `[Basic Paragraph]`, so autoflow measures the final text size.
4. **Parent page:** add folios and running heads on `spread: {kind:"parent", index:0}`.
5. **Build each page back to front:** background shapes, images, then text frames. Place or flow the copy, then apply styles.
6. **Look.** `render_page` every page and actually check it: overset, empty trailing pages, collisions, rag, widows.
7. **Check:** `inspect_document` (no `overset: true`), `font.list` (nothing `missing`), `preflight.run`.
8. **Save** `save_document {path: "/abs/x.designcraft"}` and **export** `file.exportPdf {path}`. Read its `warnings`.

### Recipe: two-page newsletter (tested)

```text
new_document {preset:"Letter", pages:1, facingPages:false, margins:54, title:"The Plot"}
batch {commands:[
  {command:"swatch.create", params:{name:"Brand", color:"#1b4d89"}},
  {command:"style.paragraph.edit", params:{name:"[Basic Paragraph]", para:{spaceAfter:6, align:"leftJustified"},
      chars:{fontFamily:"Source Serif 4", size:10, leading:{kind:"points", value:14}}}},
  {command:"style.paragraph.create", params:{name:"Subhead", nextStyle:"[Basic Paragraph]",
      para:{spaceBefore:10, spaceAfter:4, align:"left", keepWithNext:2},
      chars:{fontFamily:"Source Sans 3", fontStyle:"Bold", size:13, fill:"Brand"}}},
  {command:"style.paragraph.create", params:{name:"Headline", chars:{fontFamily:"Source Sans 3", fontStyle:"Bold", size:40, fill:"Brand"}}},
  {command:"style.paragraph.create", params:{name:"Folio", para:{align:"center"}, chars:{size:8, leading:{kind:"points", value:10}}}},
  {command:"style.character.create", params:{name:"Emphasis", chars:{fontStyle:"Italic", fill:"Brand"}}},
  {command:"frame.create", params:{spread:{kind:"parent", index:0}, rect:[54,746,558,762], content:"text",
      text:"Page   ·  The Plot Newsletter"}},
  {command:"style.paragraph.apply", params:{name:"Folio"}},
  {command:"frame.create", params:{spread:{kind:"parent", index:0}, rect:[54,740,558,741], content:"unassigned"}},
  {command:"object.fill", params:{swatch:"Brand"}},  {command:"object.stroke", params:{swatch:"[None]"}},
  {command:"frame.create", params:{rect:[54,54,558,110], content:"text", text:"The Plot"}},
  {command:"style.paragraph.apply", params:{name:"Headline"}},
  {command:"frame.create", params:{rect:[54,474,558,730], content:"text", caret:false}},
  {command:"object.textFrameOptions", params:{columns:2, gutter:18}},
  {command:"file.place", params:{path:"/abs/article.txt", autoflow:true}},          → {pagesAdded, overset:false}
  {command:"find.find", params:{find:"^(Spring planting|Volunteer roster)$", grep:true}} ]}
place_image {path:"/abs/photo.jpg", x:54, y:120, width:504}
# per heading match: text.select {story, anchor:start, focus:start} + style.paragraph.apply {name:"Subhead"}
# autoflowed frames are 1 column: object.textFrameOptions {ids:[…], columns:2, gutter:18}
render_page {page:N} for every page → delete empty trailing pages: execute layout.pages.delete {pages:[2,3]}
execute file.exportPdf {path:"/abs/news.pdf"}   ·   save_document {path:"/abs/news.designcraft"}
```

### Recipe: data-merged certificates (tested)

```text
new_document {width:432, height:288, facingPages:false, margins:24}
batch {commands:[
  {command:"data.source.select", params:{path:"/abs/people.csv"}},              → {fields, records}
  {command:"frame.create", params:{rect:[24,100,408,200], content:"text", text:"Thank you, \n"}},
  {command:"edit.selectAll"}, {command:"type.char", params:{attrs:{size:24}}}, {command:"type.alignCenter"},
  {command:"data.placeholder.add", params:{field:"role", story:"$1.story", at:12}},   # insert back to front
  {command:"data.placeholder.add", params:{field:"name", story:"$1.story", at:11}},
  {command:"data.merge"} ]}                → {records, pages, oversetStories}; the merged doc becomes active
execute file.exportPdf {path:"/abs/certificates.pdf"}
```

Also tested: a landscape tri-fold flyer (792×612, a full-bleed side panel, placeholder text, an image cropped to a
circle with contour text wrap, and a table converted from tab-separated text).

## Formats

- **Read:** `.designcraft` (native JSON), `.idml`. `file.place` takes images, PDF pages (`pdfPage`), `.txt`, `.docx`, `.rtf`,
  `.md` (as plain text), and `.xlsx` (as a table).
- **Write:** `file.exportPdf {path, pages?: "1-3", bleed?, marks?, standard?: none|x4|a2b, tagged?, spreads?}` (vector,
  subset-embedded fonts), `export_png`, `file.exportIdml`, `file.exportEpub` / `file.exportFixedEpub`, `file.exportHtml`,
  `file.exportText`, `file.printBooklet` (imposed PDF), `file.package {dir}` (document + links + fonts).
  Without `path`, the exports return base64.

## CLI (no MCP needed)

```bash
designcraft-cli script steps.dcs --in in.designcraft --save out.designcraft --export out.pdf --export out.png
#   steps.dcs: one `command.id {json}` per line, `#` comments, "$N.path" refs. Prints {completed, results}
designcraft-cli run --cmd 'file.new={"preset":"A5","facingPages":false}' \
    --cmd 'frame.create={"rect":[36,36,384,200],"content":"text","text":"Hi"}' --export out.pdf
designcraft-cli run --in doc.designcraft --page 1 --scale 0.5 --export p2.png      # --page is 0-based
designcraft-cli run --sample --all-pages outdir/        # every page to PNG (with bleed)
designcraft-cli commands frame      ·      designcraft-cli describe file.exportPdf
```

`--export` picks the format from the extension. A PNG export is page 0 at 2× unless you pass `--page`/`--scale`.

## Pitfalls

- **`new_document` defaults to `facingPages: true`.** Then a 3-page document is spreads [1], [2,3], and page 3's frames
  need x + page width (612). Pass `facingPages: false` unless you want a bound spread layout.
- **`new_document` adds a document.** The headless session already has `Untitled-1` open. `document.list` and `file.activate {index}` switch between documents.
- **`file.place` for text uses the caret first.** If a text caret is active, the text goes there and `frame` is
  ignored. Create the target frame with `caret: false` (it stays selected), or `selection.set {ids}` first.
- **Autoflow overshoots.** In tests it added 3 pages where 1 was enough. Render the pages and `layout.pages.delete` the empty
  ones. Autoflowed frames are single-column margin rectangles, so set `columns` on them.
- **Markdown is not parsed.** `.md` places as plain text (`##`, `*` stay literal), and blank lines become empty
  paragraphs. Place plain text with one paragraph per line and style the headings yourself.
- **`type.char` with only a caret changes nothing visible.** It sets the format for the next typed text. Select the text
  first (`edit.selectAll` or `text.select`). `style.paragraph.apply` does work with only a caret (it styles the caret's paragraph).
- **`data.placeholder.add` doesn't move the caret.** Several fields inserted at the caret come out in reverse order.
  Give an explicit `at` (byte offset) and insert from the end of the story back to the start.
- **Small frames go overset.** A 14 pt-high frame with 12 pt auto leading shows nothing (`lines: 0, overset: true`).
  Give single lines explicit leading, or make the frame taller.
- **Byte offsets:** `text.select` and `find.find` count UTF-8 bytes, so `·`, `é` and `—` count as 2–3.
- **Paths:** use absolute paths everywhere. The server's working directory isn't yours.
- Error texts are actionable, e.g. `unknown command \`nope.command\``, `invalid parameters for \`frame.create\`: missing rect`,
  `no paragraph style \`Missing\``, `render_page: no page 5 (the document has 1 pages, indices are 0-based)`,
  `invalid parameters for \`data.placeholder.add\`: select a data source`.

## Verification

- `render_page` every page and look at it before you report the work as done.
- `inspect_document`: every story should show `overset: false`, with no stray empty frames or pages.
- `font.list`: no `missing: true`. `preflight.run`: `errors: 0` (it also flags low-ppi images and RGB in print).
- The `file.exportPdf` reply should have the right `pages`, `bytes > 0` and empty `warnings`. To see the PDF itself,
  `vectorcraft-cli convert out.pdf p.png --artboard 0`, or open it with `pdfcraft`.

## References

- `references/commands.md`: all 444 commands with params, grouped by area (file, layout, frame, object, style,
  type, text, table, data, find, toc, book, …). Grep it rather than reading it whole.
- Upstream docs: https://github.com/storytold/designcraft/tree/main/docs (`mcp.md`, `agents.md`, `control-protocol.md`).
