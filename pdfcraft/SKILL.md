---
name: pdfcraft
description: "Work on existing PDFs with PdfCraft (Acrobat-style): read and extract text, merge/combine, split, reorder, rotate or delete pages, highlight and comment, fill or create forms, redact and audit redactions, add watermarks, headers/footers and page numbers, edit metadata and bookmarks, compress/optimize, password-protect, sign, compare, export to Word/HTML/images."
version: 0.5.0
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
drives it through an MCP server (`pdfcraft-cli mcp`, 184 tools) or one-shot CLI commands.
Edits stay in memory and are undoable until you save. Saving over the original appends an incremental update.
This skill is tested against PdfCraft 0.18.1.

## When to Use

Use it when the job is **an existing PDF**, or a quick PDF assembled from pages, images or text:

- read, search or extract text, images and page renders; summarise or check a PDF
- combine, split, extract, reorder, rotate, delete, insert or duplicate pages; page labels, crop boxes
- review: highlights, notes, stamps, shapes, replies, comment summaries; compare two versions
- forms: list, fill, import/export data, add fields, auto-detect fields, flatten; Fill & Sign without fields
- redact text, word lists, patterns (email, phone, SSN, credit card, date) or areas; find faux redactions
- watermarks, headers/footers, Bates and page numbers, backgrounds; metadata, bookmarks, links
- shrink, OCR or convert whole folders; PDF/A, print and accessibility checks, signatures; export to Word, HTML, PNG

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

Server options: `pdfcraft-cli mcp [--root DIR] [--compact] [--automation-read-root DIR] [--automation-write-root
DIR]`. `storytold-install` registers `mcp --compact`, which (like bare `mcp`) reads and writes any absolute path.
Relative paths resolve against the server's working directory, so always pass absolute paths.

- `--automation-read-root` / `--automation-write-root` confine what tools read (open, combine, import, images,
  IDs) and write (save, export, split, reports): `automation path rejected: outside the write root <DIR>: <path>`.
  A root left out grants nothing: read root alone → `automation filesystem access is not granted: write authority
  is absent: <path>` (tested).
  A missing root dir stops the server: ``mcp: cannot open the automation read root `<DIR>`: No such file or directory``.
- `--root DIR` confines every path to `DIR` (relative paths resolve inside it): `<path> is outside the allowed
  directory <DIR>` (`\\?\<DIR>` on Windows). With both kinds, a path must pass `--root` and the matching automation root.
- `--compact` lists 15 core tools plus `tool_search` and `tool_call` (17 tools, about 3.5k tokens of schemas instead
  of about 48k for all 184; checked on 0.18.1). If that is all you see, run every other tool as
  `mcp_pdfcraft_tool_call {name:"comment_add", arguments:{…}}` (the recipes below were run this way). `tool_search {name}`
  returns its full schema; `tool_search {query: "bates"}` or `{category: "page"}` finds tools. An unknown name fails
  with `unknown tool "nope"; use tool_search to find the right name`.

OCR needs the `models` folder. The CLI-only downloads (`pdfcraft-cli-*-macos-universal.zip`, and judging by size
`pdfcraft-cli-*-linux-*.tar.gz`) don't have it; the server looks beside the exe, in `../Resources/models` (the macOS
app) and `../share/pdfcraft/models`. The Windows portable zip had it in 0.9.0. Without it `ocr_status` says
`available: false` (with the `search_dirs` it tried) and OCR fails with `the text recognition models are not installed (reinstall PdfCraft, or set PDFCRAFT_MODELS to
the folder that holds them)`. A hard link in the storytold `bin` dir also misses it. Set `PDFCRAFT_MODELS` to that folder.

The MCP server is always **headless** (an in-process engine; it never attaches to the desktop app). To let the
user watch, they start `pdfcraft --control FILE` and you drive the real UI with `pdfcraft-cli ui --control FILE …`.

## Mental Model

- **Documents have ids.** `doc_open {path}` (or `doc_create`, or `doc_combine {open:true}`) returns `doc: 1`,
  the next one 2, and so on. Almost every tool takes `doc`. `doc_inspect` (no args) or `doc_list` shows what's open.
- **Pages are 1-based.** Page lists are arrays (`pages: [1,3]`), except `doc_combine.pages`,
  `doc_create_multiple.pages` and `doc_print.pages`, which are range strings (`"1-3, 6"`).
- **Geometry** is in points (1/72 in) with the origin at the **top-left of the displayed page, y down**,
  the same as `page_render` at 72 dpi and the rects `text_find` returns. Exceptions: `doc_compare` and
  `form_detect_fields` return rects with the origin **bottom-left**, and `text_edit`'s `dy` is **up**-positive.
- **Edits are in memory** and each is one undo step (`edit_undo` / `edit_redo`). Nothing reaches disk until
  `doc_save`. `doc_save {doc}` writes an incremental update to the same file; `doc_save {doc, path}` writes a
  full rewrite to a new file and the doc then points at that file.
- **Some tools write files directly** and leave the open doc unchanged: `doc_combine {out}`, `doc_create_multiple
  {out}`, `page_extract`, `doc_split`, `doc_reduce`, `doc_optimize`, `doc_export_*`, `comments_summarize`,
  `doc_compare_report`, `action_run`, `doc_batch`. `sign_document` always saves to `out`; the doc then shows that file.
- **App commands map to tools.** `command_run {id, params}` runs a menu command id through its tool (`params` are the
  tool's arguments); `command_batch {steps:[{id, params}]}` runs many and reports per-step `ok`/`error`. Only ids
  with a tool work headless (see `references/actions-and-commands.md`). Calling the tool directly is simpler.
- Every result echoes the document state (`dirty`, `pages`, `undo`), so you can check each step.

## Tools (Hermes names them `mcp_pdfcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_open {path, password?}` / `doc_create {from: blank\|images\|text}` | Get a doc id |
| `doc_info` (= `doc_inspect {doc}`) | Metadata, page sizes and labels, bookmarks, annotations, fields, links, fonts, security |
| `page_render {page, dpi?}` / `render_preview {page?, max_side?}` | PNG of a page so you can **look** at it |
| `text_extract {pages?, rect?}` / `text_find {query}` | Reading-order text (or one column with `rect`); phrase search with rects |
| `text_word_count {pages?}` | Words and characters, per page and total |
| `text_lines` / `text_paragraphs` → `text_edit` | Rewrite existing text in place |
| `page_add_text` / `page_add_image` / `content_update` | Add new page content (helvetica, times, courier) |
| `object_list` → `object_move {objects, offset}` | Move existing text, images or added content |
| `page_rotate` `page_delete` `page_move` `page_reverse` `page_insert_blank` `page_insert_file` `page_extract` | Organize pages |
| `doc_combine {paths, out?}` / `doc_create_multiple` / `doc_split {every\|before\|bookmarks\|max_mb, out_dir}` | Merge and split files |
| `comment_add {page, type, …}` / `comment_list` / `comment_reply` | Review markup (20 types) |
| `form_fields` / `form_fill {values}` / `form_add_field` / `form_add_field_table` / `form_detect_fields` | Forms |
| `redact_mark` → `redact_apply`, `doc_audit_redactions` | Permanent redaction; find faux redactions |
| `doc_header_footer` / `doc_watermark` / `doc_background` | Page marks (remove with `doc_remove_marks`) |
| `doc_set_info {key, value}` / `bookmark_add` / `page_number` | Metadata, outline, page labels |
| `text_styles` → `bookmark_from_text_styles {levels}` | Bookmarks from heading styles in untagged PDFs |
| `attachment_add {path}` / `attachment_delete {name}` | Document-level file attachments |
| `doc_bates_multi {files}` | One Bates sequence across several files (untested) |
| `doc_reduce` / `doc_optimize` / `doc_audit_space` | Smaller files |
| `doc_batch {paths, steps: [convert, ocr, optimize], out_dir}` | Convert, OCR or shrink many files or folders |
| `doc_protect` / `doc_remove_hidden` / `doc_flatten` | Security and distribution |
| `print_readiness` / `pdfa_verify` / `accessibility_check` | Pre-flight checks (read-only) |
| `doc_export_office` / `doc_export_images` / `doc_export_text` | Word, HTML, RTF, PNG/JPEG/TIFF, .txt |
| `doc_save {path?}` / `doc_close {discard_changes?}` / `edit_undo` | Save, close, undo |

All 184 tools with every parameter are in `references/tools.md`. Grep it (`grep -n "### \`redact_" …`) rather
than reading it whole. Resources: `pdfcraft://document` (open docs), `pdfcraft://commands`,
`pdfcraft://doc/{doc}/info`, `/text`, `/page/{page}/text`, `/page/{page}/image{?dpi}`. The server has no prompts.

## Comments

`comment_add` needs `page` and `type`; the geometry depends on the type:

- `highlight` / `underline` / `strikeout` / `squiggly` / `replace`: `find: "text on the page"` (`all: true`
  for every match) or `quads`. This is the easy way: no coordinates needed.
- `note` and `caret`: `at [x,y]`. `stamp`: `at` (centre) + `stamp: draft|approved|confidential|final|…`.
- `rectangle` / `oval` / `textbox`: `rect [x0,y0,x1,y1]`. `line` / `arrow`: `from`, `to`, optional `endings`.
  `ink` and `freehand_highlight` (new; tested): `strokes` (`[[[x,y], …], …]`). `polygon` / `cloud` / `polyline`:
  `points`. `callout`: `rect` + `to`. `attachment`: `path` + `at`.
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
`form_detect_fields` to create fields from underscore blanks (tested). `doc_save {flatten_fill_sign:true}` bakes
Fill & Sign marks into the page.

### Recipe: redact and distribute (tested)

```text
redact_mark {doc:1, pattern:"email"}  ·  redact_mark {doc:1, pattern:"phone"}
redact_mark {doc:1, words:["98,000","Project Falcon"], whole_words:true}   (or find, rect + page, whole_pages)
redact_mark {doc:1, find:"98,000", overlay:"REDACTED"}       (or code_set:"foia", codes:["(b)(6)"]; page or pages, not both)
redact_apply {doc:1}                                         → applied: n
text_extract {doc:1}                                         → confirm nothing of the strings is left
doc_header_footer {doc:1, header_right:"Quarterly Report", footer_center:"Page <<1 of n>>", font_size:9}
doc_watermark {doc:1, text:"CONFIDENTIAL", opacity:0.15, color:"#cc0000"}
doc_remove_hidden {doc:1, categories:["metadata","comments"]}   (omit categories = full sanitize)
doc_set_info {doc:1, key:"Author", value:"Jane Smith"}          (after remove_hidden, which wipes it)
doc_protect {doc:1, open_password:"open123", permissions_password:"owner456", printing:"high", copy:false}
doc_save {doc:1, path:"/abs/final.pdf"}                      → AES-256, needs the password to open
```

### Recipe: find faux redactions (tested)

Black boxes drawn over text that is still in the file:

```text
doc_audit_redactions {doc:1}     → findings: [{page, kind:"covered-text"|"unapplied-mark", rect, covered_text}]
redact_mark {doc:1, page:1, rect:<the finding's rect>}       (top-left rects since 0.9.0: use them as they are)
redact_apply {doc:1}  ·  text_extract {doc:1}  ·  doc_save {doc:1, path:"/abs/fixed.pdf"}
pdfcraft-cli audit file.pdf      → same JSON from the CLI; exit 1 when it finds any
```

### Recipe: merge, reorder, split (tested)

```text
doc_combine {paths:["/abs/a.pdf","/abs/b.pdf"], out:"/abs/combined.pdf"}  (pages:["1, 3", null] picks pages)
doc_open {path:"/abs/combined.pdf"}                          → doc 2
page_move {doc:2, pages:[3], to:1}  ·  page_rotate {doc:2, pages:[2], degrees:90}   (clockwise)
page_reverse {doc:2, pages:[2,3]}                            (omit pages = the whole document)
page_delete {doc:2, pages:[5]}  ·  page_insert_blank {doc:2, at:1}
page_insert_file {doc:2, at:6, path:"/abs/b.pdf", pages:[1]}
page_number {doc:2, from:1, to:1, style:"lower-roman"}  ·  page_number {doc:2, from:2, to:6, start:1}
bookmark_add {doc:2, page:2, title:"Overview"}
page_extract {doc:2, pages:[2,3], out:"/abs/excerpt.pdf"}
doc_split {doc:2, every:2, out_dir:"/abs/parts"}             → <name>-part1.pdf, …
doc_save {doc:2, path:"/abs/reorganized.pdf"}
```

Mixed inputs: `doc_create_multiple {paths:["/abs/scan.png","/abs/notes.txt","/abs/a.pdf"], pages:[null,null,"1"],
out:"/abs/all.pdf"}` makes one PDF with a bookmark per file (tested). `doc_combine` also takes images and .txt now.

### Recipe: convert, OCR or shrink a folder (tested)

```text
doc_batch {paths:["/abs/inbox"], recursive:true, steps:["convert","optimize"], out_dir:"/abs/pdfs", ppi:150, quality:80}
          → {completed, failed, skipped, files:[{path, output, status, steps}]}
doc_batch {paths:["/abs/scans"], steps:["ocr","optimize"], out_dir:"/abs/searchable"}   (skip_text_pages:false = all pages)
```

`convert` (images, .txt) must come first; without it non-PDFs are `skipped`. Subfolders keep their layout, outputs are
never overwritten (`scan (2).pdf`), sources stay untouched. A failed file makes the result `isError`, report included.

### More building blocks (all tested on 0.18.1 except OCR)

- **New PDF:** `doc_create {from:"blank", pages:3}` + `page_add_text {page, text, at:[72,72], width:468, size, bold,
  font, color}` (`at` is the text box's top-left) + `page_add_image {page, path, rect}`; or
  `doc_create {from:"images", paths:[…]}` for a scan-like PDF.
- **Edit existing text:** `text_paragraphs {page}` → `text_edit {page, paragraph:1, text:"…"}` (rewraps), or
  `text_lines` → `text_edit {page, line:2, text}`. `text_edit` falls back to fonts that can draw Cyrillic, Greek and
  Japanese; `page_add_text` can't (see Pitfalls). `text_script {page, paragraph, range?: [start,end], script:
  "subscript"|"superscript"}` turns characters into Unicode sub/superscripts (`H2O` → `H₂O`; byte offsets of `editor_text`).
- **Copy added content:** `content_list {doc}` → `content_copy {page, index, to_page?, to_doc?}` pastes a copy.
- **Move things:** `object_list {page}` → `object_move {page, objects:[{kind, index}], offset:[dx,dy], generation}`
  (right/down positive; use the `kind` and `index` the list reports).
- **Smaller file:** `doc_reduce {path}` (Acrobat defaults) or `doc_optimize {path, color:{downsample:true, ppi:72,
  above_ppi:100, compression:"jpeg", quality:50}}`; `doc_audit_space` shows what takes the bytes.
- **Compare versions:** open both, `doc_compare {doc: newer, other: older}`, `doc_compare_report {…, path}`.
- **Sign:** `sign_id_create {name, password (≥ 8 chars), path:"/abs/id.p12"}`, then
  `sign_document {doc, id:"/abs/id.p12", password, page, rect, reason, out:"/abs/signed.pdf"}`; `sign_list` validates.
  On Windows `id:"windows:<name>"` from `sign_windows_ids` uses the certificate store.
- **Pre-flight:** `print_readiness {doc}` (image ppi, boxes, bleed, unembedded fonts), `pdfa_verify`, `accessibility_check`.
- **OCR one file:** `ocr_status` → `available: true`, then `ocr_recognize {doc}` adds invisible text to scanned pages
  so `text_find` works. Check the words (`Two` came out as `wo`). Tested on 0.9.0 only: the 0.18.1 CLI zip used here has
  no OCR models (see Setup).
- **Tag a text-only PDF:** `accessibility_autotag_apply {doc}` (Document + P tags; refuses images, comments, forms).
- **Form scripting:** `js_run {doc, script:"this.getField('name').value='X'"}` (Acrobat JS; one undo step).
- **Action Wizard:** `action_run {action:"Add Page Numbers", paths:[…], folder}` or custom `steps` (see references).
- **Exports:** `doc_export_office {path:"x.docx"|"x.html"|"x.rtf"}`, `doc_export_images {folder, dpi, format}`,
  `doc_export_text {path}`, `doc_export_all_images {folder}`.

## Formats

- **Read:** PDF (including encrypted with `password`, damaged files are repaired), XFDF/FDF/XML/CSV/TXT form
  and comment data; images (PNG, JPEG, JPEG 2000, TIFF, GIF, BMP) and .txt via `doc_create`, `doc_combine`,
  `doc_create_multiple`, `page_add_image`, `stamp_custom`.
- **Write:** PDF (incremental or full; searchable via English OCR), PDF/A-2b/3b (`pdfa_convert`, then save), .docx
  .html .rtf, PNG/JPEG/TIFF pages, .txt, XFDF/FDF/XML/CSV/TXT data, accessibility report HTML, measurement CSV, .p12 digital IDs.

## CLI (no MCP needed)

```bash
pdfcraft-cli info file.pdf [--password PW]              # JSON summary: pages, title, fields, fonts, warnings
pdfcraft-cli text file.pdf [--page N]                   # reading-order text, pages split by form feeds
pdfcraft-cli render file.pdf --page N [--dpi 96] --out p.png        # also .jpg .tif .pam
pdfcraft-cli edit in.pdf --out out.pdf [--rotate 1,3:90] [--delete 2,4] [--move 5:1] [--insert-blank 1] \
                  [--title T] [--author A] [--full]   # options run in order on the edited doc
pdfcraft-cli combine a.pdf b.pdf --out combined.pdf
pdfcraft-cli extract in.pdf --pages 1,3-5 --out out.pdf    # pages and ranges, in the order given
pdfcraft-cli split in.pdf (--every N | --before 3,7) [--out-dir DIR]      # → <name>-p1-2.pdf, <name>-p3-4.pdf …
pdfcraft-cli check <files or dirs…> [--timeout 20] [--dpi 36] [--json out.json]   # can every page be parsed and drawn
pdfcraft-cli audit file.pdf [--password PW]             # faux redactions as JSON; exit 1 when found
pdfcraft-cli batch <files or dirs…> --steps convert,ocr,optimize --out-dir DIR [--recursive] [--root DIR] [--ppi 150] \
                  [--quality 60] [--dpi 300] [--language en] [--ocr-all-pages] [--stop-on-error]  # JSON report; exit 1 if any file failed
pdfcraft-cli run --script steps.json [--root DIR] [--report]   # --report: one JSON document {ok, steps} for the run
pdfcraft-cli run doc_combine 'paths=["a.pdf","b.pdf"]' out=c.pdf   # key=value, values parse as JSON
pdfcraft-cli tools                                    # every tool with its JSON Schema
pdfcraft-cli ui --control FILE state|inspect query=…|click|type|key|command id=view.layout.two_up|open path=…|screenshot --out s.png|quit
```

All tested on 0.18.1 except `ui` (needs the desktop app; last tested on 0.9.0). `run` and `mcp` share the same tool
table, so the recipes above work as `--script` steps:
`[{"tool":"doc_open","args":{…}}, …, {"tool":"page_render","args":{…},"out":"p.png"}]` (`out` saves the image).

## Pitfalls

- **`run <tool>` is a fresh session** each time: `pdfcraft-cli run text_find doc=1 …` fails with
  `no open document with id 1 (see doc_list)`. Use `run --script` for anything that needs `doc_open` first.
- **Still `text_extract` after `redact_apply`:** the audit can't see a surviving glyph. A `rect` mark removes every
  glyph it touches, parts of neighbouring words too. In 0.18.1 the audit also reports a black-filled `rectangle`
  comment over text (`kind: "covered-text"`), before and after `doc_flatten` (tested).
- **`page_number` only sets page labels**; for visible numbers use `doc_header_footer {footer_center:"Page <<1 of n>>"}`.
- **Bottom-left rects** from `doc_compare` and `form_detect_fields`: use `y_top = page_height - y` with other tools.
- **New text is Western European, Arabic, Hebrew or Thai only:** `page_add_text` refuses Cyrillic, Greek, CJK and
  Korean: `the standard fonts can't draw "П" (U+041F); only Western European characters can be added as text for now`
  (Hebrew works in 0.18.1; tested). Comments save it but draw `?` (not re-tested). Workaround: add placeholder text,
  then `text_edit` it (tested with Cyrillic).
- Clean errors: `form_fill` → `"country" has no option "Germany" (options: Canada, France, Japan)`; `doc_close`
  unsaved → `…pass discard_changes: true`; `sign_id_create` → `the password must have at least 8 characters`.
- Encrypted files: `doc_open`, CLI `info` and `text` without the password fail with `the document is protected by a
  password`; CLI `render` says only `the document could not be parsed`. Pass `password` / `--password`.
  Copy-restricted files need the owner password for text: `text_extract` → `the document's security settings don't
  allow copying text and images; open it with the owner password…`; CLI `text` → `text: the document's permissions
  don't allow copying its text; pass the owner password with --password to extract it`. `text_find` still works.
- `doc_protect` restrictions (`printing`, `copy`, `changes`) need `permissions_password`, else e.g.
  "`copy` needs `permissions_password`: with open_password alone the document is encrypted but nothing is restricted".
- `doc_remove_hidden` with `metadata` also wipes Title/Author: set metadata afterwards. When the chosen categories
  have nothing to remove it fails with `nothing to remove: the listed categories hold nothing (see doc_hidden_info)`.
  `doc_flatten` before `doc_remove_hidden {categories:["comments"]}` keeps the markup visible as page content.
- `object_move` with the wrong `kind` (text and images you added are `kind: "added"`): `a selected object no longer
  exists; select the objects again`; a stale `generation`: `the document changed; call object_list again before moving`.
  `command_run` on a UI-only id: `command "view.layout.two_up" has no headless tool; see command_list`. Bad pages:
  `page 9 is out of range: the document has 3 pages` (CLI `edit`: `--move: page 9 does not exist; after the earlier…`).

## Verification

- `page_render {page, dpi: 72}` every changed page and look at it; `text_extract` confirms text, redactions, marks;
  `doc_info` / `form_fields` / `comment_list` / `sign_list` confirm structure; `doc_save` replies with `bytes`.
- CLI `info`, `text` and `render` independently re-open the saved file; `pdfcraft-cli audit out.pdf` before sending.

## References

- `references/tools.md`: all 184 MCP tools of 0.18.1 with every parameter, grouped by area, and the `--compact` core
  list. Grep it.
- `references/actions-and-commands.md`: Action Wizard actions and steps, and the 212 app command ids for
  `ui command` and `command_run` (the `tool` column marks the ones that run headless).
- Upstream: https://github.com/storytold/pdfcraft (README "Built for agents, too"; `docs/mcp.md`, `docs/cli-batch.md`).
