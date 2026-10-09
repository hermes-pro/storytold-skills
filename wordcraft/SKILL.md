---
name: wordcraft
description: "Word processing with WordCraft (Word-style): write, format and edit documents — reports, letters, memos, résumés, proposals, manuals. Headings and styles, lists, tables, pictures, headers/footers, page numbers, TOC, footnotes, comments, track changes, mail merge. Open and save .docx, export PDF; also ODT, RTF, HTML, Markdown, TXT."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Office, Document, Word, Docx, Writing, Report, Letter, PDF, MCP]
    related_skills: [storytold, storytold-install, deckcraft, gridcraft, designcraft, pdfcraft, vectorcraft]
---

# WordCraft

WordCraft is a free, open-source clean-room take on Microsoft Word (storytold Crafting Apps). An agent
drives it through an MCP server (`wordcraft-cli mcp`) or one-shot CLI commands. It reads and writes real
`.docx` that opens in Word, and exports PDF with selectable text.

## When to Use

Use it for **flowing, text-first documents**:

- reports, memos, letters, résumés, proposals, handbooks, minutes, contracts
- turning Markdown/notes into a formatted `.docx` or PDF
- editing an existing `.docx`: find/replace, restyle, add sections, comments, tracked changes
- mail merge (letters, labels, envelopes from CSV)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Slides or a presentation | `deckcraft` |
| Spreadsheets, calculations, data tables as the deliverable | `gridcraft` |
| Designed layouts: brochures, magazines, flyers with free-placed frames | `designcraft` |
| Editing pages, forms or annotations of an existing PDF | `pdfcraft` |
| Logos, diagrams or illustrations to place in the document | `vectorcraft` (export PNG, then insert it) |

## Setup

1. If tools named `mcp_wordcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `wordcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup wordcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

The server is **headless** by default (no window). Everything works except `screenshot`, `click`, `key` and
`ui_inspect`. For the user to watch live: `wordcraft --control 7981`, then `wordcraft-cli mcp --connect 127.0.0.1:7981`.

## Mental Model

- **One active document**, edited like a person would: a **caret/selection**, and every edit is a **command**
  (389 of them) that acts at the caret or on the selection. `execute {command, params}` runs one,
  `batch {commands: [...]}` runs many in one call (stops at the first error unless `keepGoing`).
- **Write top to bottom:** type a paragraph, style it, `text.newParagraph`, repeat. The paragraph after a
  heading comes back as `Normal`.
- **Positions** are `{story: "body" | {part: n}, path: [block, row, cell, block…], off: byteOffset}`. Every
  command returns the new selection, so you can see where the caret went. Headers, footers, footnotes and
  comments are separate *parts*; commands that create them **move the caret into the part**.
- **Styles first, direct formatting second.** Use `para.style {style: "Heading 1"}` (names or ids like
  `Heading1`), and change the look document-wide with `styles.modify`, `design.theme`, `design.styleSet`.
- **Units are points** (72 per inch). Letter page 612 × 792, 1-inch margins by default.

## Tools (Hermes names them `mcp_wordcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `new_document {template?}` | `blank`, `sample`, `letter`, `resume`, `report` (templates have placeholder text to replace) |
| `open_document {path}` / `save_document {path}` | .docx .odt .rtf .md .html .txt .json in; save picks the format from the extension: docx, pdf, odt, rtf, html, md, txt, png |
| `type_text {text, paragraphs?}` | Type at the caret, replacing the selection. `paragraphs: true` turns `\n` into new paragraphs |
| `select_text {text, occurrence?}` | Select the n-th match (1-based). Then format it, or type to replace it |
| `execute` / `batch` | Run commands (see **Commands**) |
| `get_text` | Plain text of the story the caret is in (normally the body) |
| `inspect_document` | Blocks with style, runs, lists, tables (cell text), objects, sections, parts, pages, words |
| `render_page {page?, scale?}` | A page as PNG so you can **look** at it (1-based page) |
| `list_commands {query}` | Find command ids and params |
| `parity` | Feature coverage report (rarely needed) |
| `screenshot`, `click`, `key`, `ui_inspect` | Desktop app only (`--connect`) |

Resources: `wordcraft://document` (same as inspect) and `wordcraft://commands`.

## Commands you'll use most

- **Text & caret:** `text.insert {text}`, `text.newParagraph`, `text.lineBreak`, `text.tab` (next table cell),
  `text.pageBreak`, `caret.docStart`/`caret.docEnd`/`caret.end`, `select.text {text}`, `select.all`, `select.collapse`.
- **Paragraph:** `para.style {style}`, `para.heading1..3`, `para.normal`, `para.align {value}`,
  `para.spacing {before, after}`, `para.indents {left, right, firstLine}`, `para.lineSpacing {value}`,
  `para.bullets {kind?, off?}`, `para.numbering {kind?, off?}`, `para.listLevel {level}`, `para.keepNext`.
- **Character:** `format.bold|italic|underline {value?}`, `format.font {name}`, `format.size {size}`,
  `format.color {color: "RRGGBB"}`, `format.highlight {color: "yellow"}`, `format.charStyle {style}`, `format.clear`.
- **Styles:** `styles.list`, `styles.modify {style, chr?, para?}`, `styles.create {name, basedOn?}`.
- **Insert:** `insert.table {rows, cols, style?}`, `insert.picture {path, width?, alt?}`, `insert.link {url, text?}`,
  `insert.header {text?}`, `insert.footer {text? | preset: "pageNumber"}`, `insert.pageNumber {position, align, format?: "x of y"}`,
  `insert.closeHeader`, `insert.coverPage {title, subtitle?, author?}`, `insert.shape`, `insert.textBox`.
- **References:** `references.toc {levels?}` + `references.updateToc`, `references.footnote {text}`,
  `references.caption {label, text}`, `references.citation`, `references.bibliography`.
- **Page:** `layout.margins {preset | top…}`, `layout.orientation {value}`, `layout.size {name}`,
  `layout.columns {count}`, `layout.break {kind: "nextPage"|"continuous"…}`, `layout.differentFirstPage`.
- **Design:** `design.theme {name}` (`design.themes`: Craft, Studio, Gallery, Atelier, Darkroom, Sketchbook),
  `design.styleSet {name}`, `design.watermark {text, diagonal?}`, `design.pageColor`, `design.pageBorders`.
- **Review:** `edit.replaceAll {text, with, matchCase?, wholeWord?, regex?}`, `review.newComment {text}`,
  `review.trackChanges`, `review.changes`, `review.acceptAll`, `review.wordCount`.
- **Tables (caret inside):** `table.style {style}`, `table.look {headerRow, bandedRows…}`, `table.insertRowBelow`,
  `table.merge`, `table.columnWidth {width}`, `table.autofit {mode}`, `table.sort`.

Table style ids: `TableGrid`, `PlainTable1`, `GridTable1Light`, `GridTable4Accent{Blue|Orange|Green|Purple}`,
`ListTable3Accent{Blue|Orange|Green|Purple}`. Everything else: grep `references/commands.md`.

## Procedure

1. **Plan** the outline (headings), what needs a table, list, picture, and the deliverable formats.
2. **Start:** `new_document {template}`, `open_document`, or convert Markdown (fastest for long text, see below).
3. **Build in one `batch` per section**: insert → style → new paragraph. Keep ids/paths from the replies.
4. **Look:** `inspect_document` for structure, `render_page` for each page. Fix overflow, stray empty
   paragraphs, wrong styles.
5. **Save** `.docx` (editable master), then export `.pdf` if needed. Absolute paths only.

### Recipe: formatted report (tested)

```text
new_document {template: "blank"}
batch {commands: [
  {command:"text.insert", params:{text:"Q3 Business Review"}}, {command:"para.style", params:{style:"Title"}},
  {command:"text.newParagraph"},
  {command:"text.insert", params:{text:"Highlights"}}, {command:"para.heading1"}, {command:"text.newParagraph"},
  {command:"text.insert", params:{text:"The quarter closed ahead of plan."}}, {command:"text.newParagraph"},
  {command:"para.bullets"},                                      ← turn the list on BEFORE typing items
  {command:"text.insert", params:{text:"Revenue up 12%"}}, {command:"text.newParagraph"},
  {command:"text.insert", params:{text:"Churn down to 2.1%"}}, {command:"text.newParagraph"},
  {command:"para.bullets", params:{off:true}}, {command:"para.normal"},
  {command:"text.insert", params:{text:"Revenue by region"}}, {command:"para.heading2"}, {command:"text.newParagraph"},
  {command:"insert.table", params:{rows:3, cols:3, style:"GridTable4AccentBlue"}},   ← caret lands in cell (0,0)
  {command:"text.insert", params:{text:"Region"}}, {command:"text.tab"}, … fill row by row with text.tab …
  {command:"caret.docEnd"},                                      ← leaves the table (an empty paragraph follows it)
  {command:"insert.picture", params:{path:"/abs/chart.png", width:300, alt:"Revenue trend"}},
  {command:"caret.end"},                                         ← the new picture is SELECTED; collapse first
  {command:"para.alignCenter"}, {command:"text.newParagraph"}, {command:"para.alignLeft"},
  {command:"text.insert", params:{text:"Next steps"}}, {command:"para.heading1"}, {command:"text.newParagraph"},
  {command:"para.numbering"}, {command:"text.insert", params:{text:"Hire two account managers"}},
  {command:"select.text", params:{text:"Q3 Business Review"}}, {command:"caret.end"}, {command:"text.newParagraph"},
  {command:"references.toc", params:{levels:2}}, {command:"references.updateToc"},   ← TOC last, once headings exist
  {command:"insert.header", params:{text:"Northwind Ltd - Confidential"}}, {command:"insert.closeHeader"},
  {command:"insert.pageNumber", params:{position:"bottom", align:"center", format:"x of y"}}, {command:"insert.closeHeader"},
  {command:"file.properties", params:{title:"Q3 Business Review", author:"Strategy Team"}} ]}
render_page {page: 1}  →  look  ·  save_document {path:"/abs/report.docx"}  ·  save_document {path:"/abs/report.pdf"}
```

### Recipe: from Markdown, then polish (tested)

Write the content as Markdown (headings, `**bold**`, lists, pipe tables, links, `>` quotes, code fences), then:

```text
open_document {path:"/abs/memo.md"}                     (or CLI: wordcraft-cli convert memo.md memo.docx)
select_text {text:"Freeze writes"} → execute para.numbering        ← "1." lists import as bullets; fix them
select_text {text:"<a cell's text>"} → execute table.style {style:"ListTable3AccentGreen"}
execute table.look {headerRow:true, bandedRows:true}               ← imported tables are plain TableGrid
select_text {text:"the tracker"} → execute format.charStyle {style:"Hyperlink"}   ← links keep the URL but not the look
execute caret.docStart → execute insert.coverPage {title, subtitle, author}
execute insert.footer {preset:"pageNumber"} → execute insert.closeHeader → execute layout.differentFirstPage
save_document {path:"/abs/memo.docx"} · save_document {path:"/abs/memo.pdf"}
```

### Recipe: edit an existing .docx (tested)

```text
open_document {path:"/abs/report.docx"}
execute edit.replaceAll {text:"Lisbon", with:"Porto"}                → {replaced: n}; formatting is kept
execute styles.modify {style:"Heading 1", chr:{color:{Rgb:[139,30,63]}, bold:true, size:20}, para:{spaceBefore:24}}
select_text {text:"ahead of plan"} → execute format.bold → execute format.highlight {color:"yellow"}
execute review.newComment {text:"Confirm with finance"}             ← comment on the selection
select_text {text:"Churn down to 2.1%"} → execute caret.end → execute references.footnote {text:"Trailing twelve months."}
execute design.watermark {text:"DRAFT", diagonal:true} · execute design.theme {name:"Atelier"}
save_document {path:"/abs/report-v2.docx"}
```

For a letter, start from `new_document {template:"letter"}` and swap the placeholders with `edit.replaceAll`.
Tracked edits: `execute review.trackChanges`, then `select_text` + `type_text` (insert and delete are recorded
and saved as `w:ins`/`w:del`); `review.changes` lists them.

## Formats

- **Open:** .docx .odt .rtf .md .html .txt .json. **Save:** .docx .pdf .odt .rtf .html .md .txt .png (page image).
- PDF has real text, links and bookmarks. `save_document` to a new path is "Save As"; omit `path` to save in place.

## CLI (no MCP needed)

```bash
wordcraft-cli convert in.md out.docx            # any pair of: docx pdf odt rtf html md txt json png
wordcraft-cli info file.docx                     # JSON: pages, words, paragraphs, properties
wordcraft-cli text file.docx                     # plain text   ·  wordcraft-cli inspect file.docx  (structure JSON)
wordcraft-cli render file.docx page.png --page 2 --scale 0.8
wordcraft-cli run --template letter --cmd 'edit.replaceAll={"text":"Dear","with":"Hello"}' \
                  --cmd 'select.text={"text":"Hello"}' --cmd format.bold --save /abs/out.docx --print
wordcraft-cli commands [--json]                  # the full command catalog
```

`run` takes `--file F` or `--template T`, then any number of `--cmd 'id={json}'`, then `--save`.

## Pitfalls

- **A new picture stays selected.** The next `text.insert`/`text.newParagraph`/`insert.picture` *replaces* it.
  Run `caret.end` (or `select.collapse`) right after `insert.picture`.
- **Caret left in a part.** `insert.header`/`insert.footer`/`insert.pageNumber`/`references.footnote` move the caret
  into that part; `get_text` then returns only that part. Run `insert.closeHeader` to get back to the body.
- **`type_text {paragraphs:true}` then `para.bullets` bullets only the last paragraph.** Turn the list on first, then type.
- **Ending a list:** an empty `text.newParagraph` ends it, but the paragraph keeps the `ListParagraph` style. Follow with `para.normal`.
- **Colours differ by command.** `format.color`, `para.shading`, `design.*` take `"RRGGBB"`; property objects
  (`styles.modify chr/para`, `format.set {props}`, `para.set {props}`) need `{"Rgb":[r,g,b]}`. A hex string there fails with
  `bad parameters: invalid type: string "8B1E3F", expected tuple struct Rgb`.
- **Unknown param keys are silently ignored** (no error). Check the effect with `format.state` or `document.paragraph {path:[i]}`.
- **Table style names:** `insert.table {style:"Grid Table 4 Accent 1"}` → `bad parameters: no table style ...`. Use the ids listed above (`styles.list`).
- `styles.create` also applies the new style to the paragraph at the caret.
- `edit.replaceAll` searches the body only, not headers or footers (edit those with `insert.editHeader`, `select.all`, `type_text`).
  It also bypasses track changes.
- **TOC page numbers can be wrong** (every entry read "1" for a 2-page report, even after `references.updateToc`). Check them
  in `get_text`; Word recomputes them on open, but a PDF keeps them.
- **Caption numbers in PDF:** `references.caption` numbers render fine in `render_page` and `.docx`, but PDF export writes
  U+FFFC instead of the number. For a PDF deliverable, type "Table 1: …" literally and style it `Caption`.
- `render_page` shows red spelling squiggles. PDF and `wordcraft-cli render` don't.
- `get_text` includes the deleted text of tracked deletions.
- **Paths:** use absolute paths. Relative ones resolve against the server's working directory.
- `file.setAuthor` needs `{name}` though the catalog lists no params.
- UI-only tools fail headless with `` `ui.screenshot` needs the desktop app: start `wordcraft --control 7981` … ``. That's expected.

## Verification

- `inspect_document`: expected styles per block, `list` on list items, `cells` filled, `objects` for pictures and fields, `pages`.
- `render_page` every page and look at it before reporting done.
- `wordcraft-cli info out.docx` and `wordcraft-cli text out.docx` confirm the saved file opens; render a PDF page with
  `wordcraft-cli render` (docx) or open the PDF in `pdfcraft`.

## References

- `references/commands.md`: all 389 commands with params, ribbon location and shortcut, grouped by area. Grep it
  (`grep -n 'insert[.]' references/commands.md`) rather than reading it whole.
- Upstream docs: https://github.com/storytold/wordcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
