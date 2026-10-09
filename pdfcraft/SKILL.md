---
name: pdfcraft
description: "Work on existing PDFs with PdfCraft (Acrobat-style): read and extract text, merge/combine, split, reorder, rotate or delete pages, highlight and comment, fill or create forms, redact, add watermarks, headers/footers and page numbers, edit metadata and bookmarks, compress/optimize, password-protect, sign, compare, export to Word/HTML/images."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Office, PDF, Documents, Forms, Redaction, Annotation, MCP]
    related_skills: [storytold, storytold-install, designcraft, wordcraft, vectorcraft, photocraft]
---

# PdfCraft

PdfCraft is a free, open-source, clean-room take on Adobe Acrobat (storytold Crafting Apps). An agent
drives it through an MCP server (`pdfcraft-cli mcp`, 131 tools) or one-shot CLI commands. Edits stay in
memory and are undoable until you save. Saving over the original appends an incremental update.

## When to Use

Use it when the job is **an existing PDF**, or a quick PDF assembled from pages, images or text:

- read, search or extract text, images and page renders; summarise or check a PDF
- combine, split, extract, reorder, rotate, delete, insert or duplicate pages; page labels, crop boxes
- review: highlights, notes, stamps, shapes, replies, comment summaries; compare two versions
- forms: list, fill, import/export data, add fields, auto-detect fields, flatten; Fill & Sign without fields
- redact text, patterns (email, phone, SSN, credit card, date) or areas; remove hidden info; passwords
- watermarks, headers/footers, Bates and page numbers, backgrounds; metadata, bookmarks, links
- shrink/optimize, PDF/A, accessibility checks, digital signatures, export to Word, HTML, RTF, PNG, text

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Designing a new multi-page layout (brochure, magazine, book) from scratch | `designcraft` |
| Writing or heavily rewriting a document's prose | `wordcraft` (then export PDF) |
| Vector artwork, logos, editing a single PDF page as artwork | `vectorcraft` |
| Retouching the photos inside a PDF | `photocraft` |
| Slides | `deckcraft` |
| Spreadsheets and tables of numbers | `gridcraft` |

## Setup

1. If tools named `mcp_pdfcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `pdfcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup pdfcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots and `pdfcraft-cli run --script` (see **CLI**).

The MCP server is always **headless** (an in-process engine; it never attaches to the desktop app).
`pdfcraft-cli mcp --root DIR` confines every path it reads or writes to `DIR`. To let the user watch, they
start `pdfcraft --control FILE` and you drive the real UI with `pdfcraft-cli ui --control FILE …` (see **CLI**).

## Mental Model

- **Documents have ids.** `doc_open {path}` (or `doc_create`, or `doc_combine {open:true}`) returns `doc: 1`,
  the next one 2, and so on. Almost every tool takes `doc`. `doc_list` shows what's open and `dirty`.
- **Pages are 1-based.** Page lists are arrays (`pages: [1,3]`), except `doc_combine.pages` and
  `doc_print.pages`, which are range strings (`"1-3, 6"`).
- **Geometry** is in points (1/72 in) with the origin at the **top-left of the displayed page, y down**,
  the same as `page_render` at 72 dpi and the rects `text_find` returns. Exceptions: `doc_compare` and
  `form_detect_fields` return rects with the origin **bottom-left**, and `text_edit`'s `dy` is **up**-positive.
- **Edits are in memory** and each is one undo step (`edit_undo` / `edit_redo`). Nothing reaches disk until
  `doc_save`. `doc_save {doc}` writes an incremental update to the same file; `doc_save {doc, path}` writes a
  full rewrite to a new file and the doc then points at that file.
- **Some tools write files directly** and leave the open doc unchanged: `doc_combine {out}`, `page_extract`,
  `doc_split`, `doc_reduce`, `doc_optimize`, `doc_export_*`, `comments_summarize`, `doc_compare_report`,
  `action_run`. `sign_document` always saves to `out` and the doc then shows the signed file.
- Every result echoes the document state (`dirty`, `pages`, `undo`), so you can check each step.

## Tools (Hermes names them `mcp_pdfcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_open {path, password?}` / `doc_create {from: blank\|images\|text}` | Get a doc id |
| `doc_info` | Metadata, page sizes and labels, bookmarks, annotations, fields, links, fonts, security |
| `page_render {page, dpi?}` | PNG of a page so you can **look** at it (96 dpi default, 72 = 1 px per point) |
| `text_extract {pages?}` / `text_find {query}` | Reading-order text; phrase search with rects |
| `text_lines` / `text_paragraphs` → `text_edit` | Rewrite existing text in place |
| `page_add_text` / `page_add_image` / `content_update` | Add new page content (helvetica, times, courier) |
| `page_rotate` `page_delete` `page_move` `page_insert_blank` `page_insert_file` `page_extract` | Organize pages |
| `doc_combine {paths, out?}` / `doc_split {every\|before\|bookmarks\|max_mb, out_dir}` | Merge and split files |
| `comment_add {page, type, …}` / `comment_list` / `comment_reply` | Review markup (19 types) |
| `form_fields` / `form_fill {values}` / `form_add_field` / `form_detect_fields` | Forms |
| `redact_mark` → `redact_apply` | Permanent redaction |
| `doc_header_footer` / `doc_watermark` / `doc_background` | Page marks (remove with `doc_remove_marks`) |
| `doc_set_info {key, value}` / `bookmark_add` / `page_number` | Metadata, outline, page labels |
| `doc_reduce` / `doc_optimize` / `doc_audit_space` | Smaller files |
| `doc_protect` / `doc_remove_hidden` / `doc_flatten` | Security and distribution |
| `doc_export_office` / `doc_export_images` / `doc_export_text` | Word, HTML, RTF, PNG/JPEG/TIFF, .txt |
| `doc_save {path?}` / `doc_close {discard_changes?}` / `edit_undo` | Save, close, undo |

All 131 tools with every parameter are in `references/tools.md`. Grep it (`grep -n "### \`form_" …`) rather
than reading it whole. Resources: `pdfcraft://doc/{doc}/info`, `/text`, `/page/{page}/text`,
`/page/{page}/image{?dpi}`. The server has no prompts.

## Comments

`comment_add` needs `page` and `type`; the geometry depends on the type:

- `highlight` / `underline` / `strikeout` / `squiggly` / `replace`: `find: "text on the page"` (`all: true`
  for every match) or `quads`. This is the easy way: no coordinates needed.
- `note` and `caret`: `at [x,y]`. `stamp`: `at` (centre) + `stamp: draft|approved|confidential|final|…`.
- `rectangle` / `oval` / `textbox`: `rect [x0,y0,x1,y1]`. `line` / `arrow`: `from`, `to`. `ink`: `strokes`.
  `polygon` / `cloud` / `polyline`: `points`. `callout`: `rect` + `to`. `attachment`: `path` + `at`.
- Style with `color`, `fill`, `opacity`, `width`, `author`, `contents` (the comment's text).

## Procedure

1. **Open and inspect:** `doc_open`, then `doc_info` (pages, fields, fonts, security) and `text_extract`.
2. **Locate** what to change with `text_find`, `form_fields`, `text_lines` or `comment_list` instead of
   guessing coordinates. Rects they return feed straight into `rect`, `at` and `quads`.
3. **Edit.** Each call returns the doc state; an `isError` result names the problem (see Pitfalls).
4. **Look.** `page_render {page, dpi: 72}` for each changed page, and re-run `text_extract` where text matters
   (redaction, header text, form values).
5. **Save** with `doc_save {doc, path: "/abs/new.pdf"}` to keep the original, or `doc_save {doc}` to update it.

### Recipe: review a report (tested)

```text
doc_open    {path:"/abs/report.pdf"}                                  → doc 1
text_find   {doc:1, query:"total due"}                                → page + rects
comment_add {doc:1, page:1, type:"highlight", find:"Revenue grew 12 percent", color:"yellow",
             contents:"Check this figure", author:"Reviewer"}
comment_add {doc:1, page:1, type:"note", at:[500,72], contents:"Looks good overall"}
comment_add {doc:1, page:2, type:"stamp", at:[450,300], stamp:"draft"}
comment_add {doc:1, page:1, type:"rectangle", rect:[68,216,376,449], color:"red", width:2}
comments_summarize {doc:1, out:"/abs/comments.pdf"}  ·  doc_export_data {doc:1, path:"/abs/c.xfdf", what:"comments"}
doc_save    {doc:1, path:"/abs/report-reviewed.pdf"}
```

### Recipe: fill a form (tested)

```text
form_fields {doc:1}                     → names, types, combo options, current values
form_fill   {doc:1, values:{"name":"Ada Lovelace", "country":"France", "subscribe":true}}
page_render {doc:1, page:3, dpi:72}     → values are drawn in the fields
doc_flatten {doc:1}                     → optional: bake fields and comments into the page
doc_save    {doc:1, path:"/abs/filled.pdf"}
```

Bulk data: `doc_import_data {path: "data.csv|.xfdf|.fdf|.xml"}`; `doc_export_data {path: "x.csv", what: "fields"}`.
No fields at all? `fill_sign_add {page, type: text|check|date|signature|initials, at, text}` (tested), or
`form_detect_fields` to create fields from underscore blanks (tested).

### Recipe: redact and distribute (tested)

```text
redact_mark {doc:1, pattern:"email"}  ·  redact_mark {doc:1, pattern:"phone"}
redact_mark {doc:1, find:"98,000", overlay:"REDACTED"}       (or rect + page, or whole_pages)
redact_apply {doc:1}                                         → applied: n
text_extract {doc:1}                                         → confirm the strings are gone
doc_header_footer {doc:1, header_right:"Quarterly Report", footer_center:"Page <<1 of n>>", font_size:9}
doc_watermark {doc:1, text:"CONFIDENTIAL", opacity:0.15, color:"#cc0000"}
doc_set_info {doc:1, key:"Author", value:"Jane Smith"}
doc_remove_hidden {doc:1, categories:["metadata","comments"]}   (omit categories = full sanitize)
doc_protect {doc:1, open_password:"open123", permissions_password:"owner456", printing:"high", copy:false}
doc_save {doc:1, path:"/abs/final.pdf"}                      → AES-256, needs the password to open
```

### Recipe: merge, reorder, split (tested)

```text
doc_combine {paths:["/abs/a.pdf","/abs/b.pdf"], out:"/abs/combined.pdf"}  (pages:["1, 3", null] picks pages)
doc_open {path:"/abs/combined.pdf"}                          → doc 2
page_move {doc:2, pages:[3], to:1}  ·  page_rotate {doc:2, pages:[2], degrees:90}   (clockwise)
page_delete {doc:2, pages:[5]}  ·  page_insert_blank {doc:2, at:1}
page_insert_file {doc:2, at:6, path:"/abs/b.pdf", pages:[1]}
page_number {doc:2, from:1, to:1, style:"lower-roman"}  ·  page_number {doc:2, from:2, to:6, start:1}
bookmark_add {doc:2, page:2, title:"Overview"}
page_extract {doc:2, pages:[2,3], out:"/abs/excerpt.pdf"}
doc_split {doc:2, every:2, out_dir:"/abs/parts"}             → <name>-part1.pdf, …
doc_save {doc:2, path:"/abs/reorganized.pdf"}
```

### More building blocks (all tested)

- **New PDF:** `doc_create {from:"blank", pages:3}` + `page_add_text {page, text, at:[72,72], width:468, size, bold,
  font, color}` (`at` is the text box's top-left) + `page_add_image {page, path, rect}`; or
  `doc_create {from:"images", paths:[…]}` for a scan-like PDF.
- **Edit existing text:** `text_paragraphs {page}` → `text_edit {page, paragraph:1, text:"…"}` (rewraps), or
  `text_lines` → `text_edit {page, line:2, text}`. Unsupported characters fall back to Helvetica.
- **Smaller file:** `doc_reduce {path}` (Acrobat defaults) or `doc_optimize {path, color:{downsample:true, ppi:72,
  above_ppi:100, compression:"jpeg", quality:50}}`; `doc_audit_space` shows what takes the bytes.
- **Compare versions:** open both, `doc_compare {doc: newer, other: older}`, `doc_compare_report {…, path}`.
- **Sign:** `sign_id_create {name, password (≥ 6 chars), path:"/abs/id.p12"}`, then
  `sign_document {doc, id:"/abs/id.p12", password, page, rect, reason, out:"/abs/signed.pdf"}`; `sign_list` validates.
- **Form scripting:** `js_run {doc, script:"this.getField('name').value='X'"}` (Acrobat JS; one undo step).
- **Batch many files:** `action_run {action:"Add Page Numbers", paths:[…], folder}` or custom `steps`
  (see `references/actions-and-commands.md`). The folder is created if missing.
- **Exports:** `doc_export_office {path:"x.docx"|"x.html"|"x.rtf"}`, `doc_export_images {folder, dpi, format}`,
  `doc_export_text {path}`, `doc_export_all_images {folder}`.

## Formats

- **Read:** PDF (including encrypted with `password`, damaged files are repaired), XFDF/FDF/XML/CSV/TXT form
  and comment data; images (PNG, JPEG, TIFF, GIF, BMP) via `doc_create`, `page_add_image`, `stamp_custom`.
- **Write:** PDF (incremental or full), PDF/A-2b/3b (`pdfa_convert`, then save), .docx .html .rtf, PNG/JPEG/TIFF
  pages, .txt, XFDF/FDF/XML/CSV/TXT data, accessibility report HTML, measurement CSV, .p12 digital IDs.
- OCR (`ocr_recognize`) needs models that release builds don't ship: check `ocr_status` first.

## CLI (no MCP needed)

```bash
pdfcraft-cli info file.pdf [--password PW]              # JSON summary: pages, title, fields, fonts, warnings
pdfcraft-cli text file.pdf [--page N]                   # reading-order text, pages split by form feeds
pdfcraft-cli render file.pdf --page N [--dpi 96] --out p.png        # also .jpg .tif
pdfcraft-cli edit in.pdf --out out.pdf [--rotate 1,3:90] [--delete 2,4] [--move 5:1] [--insert-blank 1] \
                  [--title T] [--author A] [--full]
pdfcraft-cli combine a.pdf b.pdf --out combined.pdf
pdfcraft-cli extract in.pdf --pages 1,3,5 --out out.pdf
pdfcraft-cli split in.pdf (--every N | --before 3,7) [--out-dir DIR]      # → <name>-p1.pdf …
pdfcraft-cli run --script steps.json [--root DIR]     # [{"tool":"doc_open","args":{…}}, …, {"tool":"page_render","args":{…},"out":"p.png"}]
pdfcraft-cli run doc_combine 'paths=["a.pdf","b.pdf"]' out=c.pdf   # key=value, values parse as JSON
pdfcraft-cli tools                                    # every tool with its JSON Schema
pdfcraft-cli ui --control FILE state|inspect query=…|click|type|key|command id=view.layout.two_up|open path=…|screenshot --out s.png
```

All tested. `run` and `mcp` share the same tool table, so the recipes above work as `--script` steps.

## Pitfalls

- **Absolute paths** for every file argument. Headless, the working directory is the server's, not yours.
- **`run <tool>` is a fresh session** each time: `pdfcraft-cli run text_find doc=1 …` fails with
  `no open document with id 1 (see doc_list)`. Use `run --script` for anything that needs `doc_open` first.
- **Check redactions.** `redact_apply` reported success while boxes on text set in a non-embedded **Times** font
  drifted left and left the last characters readable (`…example.co` covered, `m` and `7` visible). Helvetica text
  was exact. Always re-run `text_extract`/`text_find` after applying; widen with a `rect` mark if anything remains.
- **`page_number` only sets page labels** (what viewers show in the page box). For visible numbers use
  `doc_header_footer {footer_center:"Page <<1 of n>>"}`.
- **Bottom-left rects:** `doc_compare` and `form_detect_fields` return y measured from the bottom; convert
  (`y_top = page_height - y`) before reusing them with top-left tools.
- `form_fill` checks values: `"country" has no option "Germany" (options: Canada, France, Japan)`,
  `there is no field named "nope" (see form_fields)`.
- `doc_close` refuses with unsaved changes: `the document has unsaved changes: save it with doc_save, or pass
  discard_changes: true`.
- `sign_id_create` rejects short passwords: `the password must have at least 6 characters`.
- Encrypted files: `doc_open` without the password fails with `the document is protected by a password`, but
  the CLI (`render`, `info`, `text`) says only `the document could not be parsed`. Pass `--password`.
- `doc_protect` restrictions (`printing`, `copy`, `changes`) need `permissions_password`, and `doc_remove_hidden`
  with `metadata` also wipes Title/Author. Set metadata after sanitizing if it must stay.
- `doc_flatten` before `doc_remove_hidden {categories:["comments"]}` keeps the markup visible as page content.
- Out-of-range pages fail cleanly: `page 9 is out of range: the document has 3 pages`.

## Verification

- `page_render {page, dpi: 72}` every changed page and look at it before reporting done.
- `text_extract` confirms text changes, redactions, header/footer and watermark text, and filled values.
- `doc_info` / `form_fields` / `comment_list` / `sign_list` confirm structure; every `doc_save` reply has `bytes`
  and `path`, and `incremental` says how it was written.
- `pdfcraft-cli info out.pdf` and `pdfcraft-cli render out.pdf --page 1 --out p.png` independently re-open the file.

## References

- `references/tools.md`: all 131 MCP tools with every parameter, grouped by area. Grep it.
- `references/actions-and-commands.md`: Action Wizard actions and steps, and the 178 app command ids for `ui command`.
- Upstream: https://github.com/storytold/pdfcraft (README "Built for agents, too"; CLI options in
  `apps/pdfcraft-cli/src/main.rs`).
