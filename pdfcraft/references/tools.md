# PdfCraft MCP tools

Generated from the live `pdfcraft-cli mcp` server (PdfCraft 0.7.1, 161 tools). Hermes names them
`mcp_pdfcraft_<tool>`. The same names work in `pdfcraft-cli run <tool> key=value` and `run --script`.
With `pdfcraft-cli mcp --compact` only a core set is listed; run any other tool here with
`tool_call {name, arguments}` (and `tool_search {name}` returns its full schema).
Almost every tool takes `doc` (the id from `doc_open` / `doc_create`); it is left out of the lists below.
Grep for a tool name or a keyword; don't read the whole file. `?` = optional, `a | b` = choices, (=x) = default.
Coordinates are points with the origin at the top-left of the displayed page, y down, unless a tool says bottom-left.

## Documents: open, create, save, metadata, history

### `doc_open`
Open a PDF file and return its document id, page count and whether it can be edited.
- `password`?: string — User or owner password for encrypted files.
- `path`: string

### `doc_create`
Create a new, unsaved document and return it like doc_open: `blank` (pages, width, height in points; default 1 US Letter page), `images` (paths of PNG, JPEG, TIFF (every page), GIF or BMP files, one page each at the image's resolution) or `text` (a .txt path, or `text` directly; Western European (WinAnsi) characters only, others are refused). Save it with doc_save and a path.
- `dpi`?: number [min 1, max 1200] — For images: override the embedded resolution without resampling. 72 gives one point per pixel; omit to use each image's resolution (72 when absent).
- `from`: blank \| images \| text
- `height`?: number [min 3]
- `name`?: string — Name for the new document (default derived from the source).
- `pages`?: integer [min 1, max 10000]
- `path`?: string
- `paths`?: [string]
- `text`?: string
- `width`?: number [min 3]

### `doc_list` (read-only)
List the open documents with their ids, page counts and unsaved state.
- (no parameters)

### `doc_info` (read-only)
Metadata, page sizes and labels, bookmarks, annotations, form fields, links, layers, attachments, fonts, security and repair notes.
- (no parameters besides `doc`)

### `doc_close`
Close a document. Fails if it has unsaved changes unless discard_changes is true.
- `discard_changes`?: boolean

### `doc_save`
Save to its own file (an incremental update, which keeps signatures valid) or to a new path (a full rewrite). The write is atomic. flatten_fill_sign bakes Fill & Sign text, marks and signatures into the page first and removes those annotations; other comments and form fields stay. Omit it, or pass false, to leave them editable.
- `flatten_fill_sign`?: boolean — Bake Fill & Sign marks into the page before writing. Default false.
- `full`?: boolean — Force a full rewrite (or, with false, an incremental update).
- `path`?: string — Save as this file. Omit to save in place.

### `doc_set_info`
Set a document information entry such as Title, Author, Subject or Keywords. Undoable.
- `key`: string
- `value`: string

### `doc_initial_view`
Read or change how the document opens (Document Properties ▸ Initial View) and its reading options: navigation (page, bookmarks, pages, attachments, layers), layout (default, single, continuous, two_up, two_up_continuous, two_up_cover, two_up_continuous_cover), magnification (default, actual, fit_page, fit_width, fit_height, fit_visible, or a percentage), page, window options (fit_window, center_window, full_screen, display_title), interface options (hide_menubar, hide_toolbar, hide_window_ui), language and binding (left, right). Only the given ones change; returns the result. Undoable.
- `binding`?: left \| right
- `center_window`?: boolean
- `display_title`?: boolean
- `fit_window`?: boolean
- `full_screen`?: boolean
- `hide_menubar`?: boolean
- `hide_toolbar`?: boolean
- `hide_window_ui`?: boolean
- `language`?: string
- `layout`?: default \| single \| continuous \| two_up \| two_up_continuous \| two_up_cover \| two_up_continuous_cover
- `magnification`?: any
- `navigation`?: page \| bookmarks \| pages \| attachments \| layers
- `page`?: integer [min 1]

### `doc_revisions`
List the document's saved revisions (oldest first): each incremental update is one. Returns revision number, where it ends in the file and its size, and which signatures sign exactly that revision.
- (no parameters besides `doc`)

### `doc_open_revision`
Open saved revision `revision` (1 = the oldest) of a document as a new, unsaved document, to see the file as it was then.
- `revision`: integer [min 1]

### `edit_undo`
Undo the last edit of a document.
- (no parameters besides `doc`)

### `edit_redo`
Redo the last undone edit of a document.
- (no parameters besides `doc`)

### `doc_inspect` (read-only)
With doc, return doc_info; otherwise return information for every open document (empty documents array when none are open).
- (no parameters besides `doc`)

### `doc_create_multiple`
Convert several files (PDFs, PNG/JPEG/JPEG 2000/TIFF/GIF/BMP images, .txt files) to PDF in one run. mode "combine" (default) joins them, in order, into one PDF with a bookmark per file; pages optionally chooses each file's pages, in step with paths (a range such as "1-3, 6" or null). mode "separate" writes one PDF per file into out_dir (files that are already PDFs are skipped; existing files are never overwritten) and reports each file's result.
- `mode`?: combine \| separate
- `open`?: boolean — Also open the result as a new document (default: only when out is omitted).
- `out`?: string — File to write. Omit to open the result as a new unsaved document instead.
- `out_dir`?: string — Folder for mode "separate".
- `pages`?: [string/null]
- `paths`: [string]

### `view_reading_colors`
Set the document's reading colours (Acrobat's Replace Document Colors, in the Reading Options): solid text and line-art paints are remapped for readability and the page clears to the background colour in page_render. A view setting: the file doesn't change. mode is one of: off, black-on-white, white-on-black, yellow-on-black, green-on-black, or custom (which takes text and background as #RRGGBB). only_black maps only near-black paints (default false) and line_art also maps line-art paints (default true); both override the mode's preset. A flag that differs from the mode's preset default makes the returned mode read custom, because the resulting params no longer match any preset. Returns the resulting setting.
- `background`?: string — With mode custom: the background colour, #RRGGBB.
- `line_art`?: boolean — Also map line-art paints. Default true.
- `mode`: off \| black-on-white \| white-on-black \| yellow-on-black \| green-on-black \| custom
- `only_black`?: boolean — Map only near-black paints. Default false.
- `text`?: string — With mode custom: the text colour, #RRGGBB.

### `command_list` (read-only)
Every registered PdfCraft command with its menu, shortcut, whether it is enabled now, and the tool that automates it.
- `enabled_only`?: boolean
- `filter`?: string

### `command_run`
Run a registry command through its headless tool. Pass that tool's arguments in params (see command_list). Unknown params are ignored with warnings; path confinement still applies.
- `id`: string
- `params`?: object

### `command_batch`
Run steps in order (at most 1000). Returns completed/failed counts and per-step ok/result/error; stop_on_error defaults to true.
- `steps`: [{id, params}]
- `stop_on_error`?: boolean

## Reading: render, text, find

### `page_render` (read-only)
Render one page to a PNG image (default 96 dpi, at most 600).
- `dpi`?: number [min 1, max 600]
- `hide_text_block`?: integer [min 1] — Render an inline editor background without this paragraph (index from text_paragraphs). Does not modify the document.
- `page`: integer [min 1]

### `render_preview` (read-only)
Render a PNG bounded by max_side (default 1024), without changing or saving the document. Page defaults to 1; doc may be omitted when exactly one document is open.
- `max_side`?: integer [min 1, max 4096]
- `page`?: integer [min 1]

### `text_extract` (read-only)
Extract the text of some or all pages, in reading order. With rect, only the text inside that rectangle on each page, as Column select takes it: one row per visual line, side-by-side pieces (table cells) separated by a tab.
- `pages`?: [integer] — 1-based page numbers to extract (default: all).
- `rect`?: [4 numbers] — Column select: [x0, y0, x1, y1] in points from the top-left of the displayed page; a glyph counts when its centre is inside.

### `text_find` (read-only)
Find a phrase (case-insensitive, whitespace-normalised) and return each match, in page order, with its page and line rectangles in points (origin top-left). Pages are read only until the limit is reached.
- `limit`?: integer [min 1] — Maximum matches (default 500). The search stops once it has this many; `complete` says whether every match was returned, and when it is false `next` holds the start_page and skip that continue the search.
- `query`: string
- `skip`?: integer [min 0] — Matches to pass over on start_page before returning any (default 0).
- `start_page`?: integer [min 1] — Page to start searching from (default 1).

### `text_lines` (read-only)
The lines of existing text on a page (Edit a PDF ▸ Edit text): number, text, box (top-left-origin points), font and size. Use the number with text_edit.
- `page`: integer [min 1]

### `text_paragraphs` (read-only)
The paragraphs on a page (adjacent source runs grouped into aligned visual rows, including mixed fonts, sizes and colours): number, text, editor_text (visual rows separated by newlines), rows and source line numbers, box (top-left-origin points), font and size. Use the number with text_edit's paragraph.
- `page`: integer [min 1]

### `page_images` (read-only)
The raster images and grouped Form artwork a page draws (Edit a PDF): number, full placement rect and visible_rect after page/path clipping (top-left-origin points; null if fully hidden), kind (image/form), pixel size ([0,0] for forms) and resource name. Forms include nested graphics and are edited as a whole. Numbers count forms and images together in drawing order, so a page with forms numbers its images differently than before forms were listed: always take numbers from a fresh page_images call.
- `page`: integer [min 1]

### `image_hit` (read-only)
List image/Form numbers whose placement and all clipping paths contain point [x,y] in top-left-origin points. Bezier curves, even-odd/nonzero fill and holes are respected. Read only.
- `page`: integer [min 1]
- `point`: [2 numbers]

### `object_list` (read-only)
List existing paragraphs, Image/Form artwork and added content once, with source kind/index references, displayed rectangles and document generation. Indexes change when content changes; use generation in object_move to reject stale references.
- `page`: integer [min 1]

### `image_save`
Write one of a page's raster images (number from page_images; forms are refused) to path: JPEG images unchanged, others as PNG (the extension is added when missing).
- `image`: integer [min 1]
- `page`: integer [min 1]
- `path`: string

### `doc_export_text`
Write the reading-order text of pages to a .txt file (pages separated by form feeds).
- `pages`?: [integer] — 1-based page numbers to export (default: all).
- `path`: string

## Pages: organize, combine, split

### `page_rotate`
Rotate pages by a multiple of 90 degrees (positive is clockwise): the listed pages (default all), filtered like Acrobat's Rotate Pages by subset (all, even, odd page numbers) and orientation (all, landscape, portrait). Undoable.
- `degrees`: integer
- `orientation`?: all \| landscape \| portrait
- `pages`?: [integer] — 1-based page numbers to rotate (default: all).
- `subset`?: all \| even \| odd

### `page_delete`
Delete pages. Undoable until saved.
- `pages`: [integer] — 1-based page numbers to delete.

### `page_move`
Move pages so the first of them lands at position `to` (1-based, counted before the move). Undoable.
- `pages`: [integer] — 1-based page numbers to move.
- `to`: integer [min 1]

### `page_insert_blank`
Insert a blank page so it becomes page `at`. Size defaults to the neighbouring page. Undoable.
- `at`: integer [min 1]
- `height`?: number — Points.
- `width`?: number — Points.

### `page_insert_file`
Insert pages of another PDF so the first becomes page `at`. Undoable.
- `at`: integer [min 1]
- `pages`?: [integer] — 1-based page numbers of the source file (default: all).
- `path`: string

### `page_replace`
Replace the content of pages with pages of another PDF (same count). Links, comments, form fields and bookmarks on the original pages stay, as in Acrobat. Undoable.
- `from_pages`?: [integer] — 1-based page numbers of the other file, in order (default: its first pages).
- `pages`: [integer] — 1-based page numbers to replace.
- `path`: string — A file path (relative to --root when set).

### `page_duplicate`
Insert copies of pages after the last of them (fonts and images are shared, not copied). Undoable.
- `pages`: [integer] — 1-based page numbers to duplicate.

### `page_extract`
Copy pages into a new PDF (links, bookmarks, fields and layers that belong to them come along). separate: true writes each page as its own file into out_dir; delete: true removes the pages from this document afterwards (undoable).
- `delete`?: boolean
- `open`?: boolean — Also open the result as a new document (default: only when out is omitted).
- `out`?: string — File to write. Omit to open the result as a new unsaved document instead.
- `out_dir`?: string
- `pages`: [integer] — 1-based page numbers to extract.
- `separate`?: boolean

### `page_set_box`
Set a page box (crop by default; also trim, bleed, art, media) on pages: either margins in points from the media box [left, bottom, right, top], or an absolute rect in points from the top-left of the displayed page. Omit both to reset the box to its default. Undoable.
- `box`?: crop \| trim \| bleed \| art \| media
- `margins`?: [4 numbers]
- `pages`?: [integer] — 1-based page numbers to change (default: all).
- `rect`?: [4 numbers]

### `page_number`
Label a range of pages (e.g. i, ii, iii for front matter, or A-1, A-2 for an appendix). Later pages keep their labels. Undoable.
- `from`: integer [min 1]
- `prefix`?: string
- `start`?: integer [min 1] — Number of the first page in the range (default 1).
- `style`?: decimal \| upper-roman \| lower-roman \| upper-alpha \| lower-alpha \| none — Numbering style (default decimal; none = prefix only).
- `to`: integer [min 1]

### `doc_combine`
Combine files, in order, into one PDF (bookmarks are kept under one entry per file). Images (PNG, JPEG, TIFF, GIF, BMP, JPEG 2000) and .txt files are made into PDFs first. pages optionally chooses each file's pages, in step with paths: a range such as "1-3, 6" or null for all pages. passwords, also in step with paths, opens encrypted files (the open password, or the permissions password where a file's security doesn't allow copying pages; null for none). The result is not encrypted. Passwords are never echoed back. groups, also in step with paths, splits a file around others: entries with the same number (they must name the same path) are one file, copied once, so it keeps one bookmark at its first page, its links and its form fields; null for a file of its own. A group uses its first entry's password. When two files' forms name the same field, field_conflicts says what happens: "rename" (the default) keeps the fields separate by renaming the later one (Text1 becomes Text1-1) and the result lists renamed_fields as [[old, new], …] — scripts that refer to the old name are not rewritten; "merge" makes them one field, as before.
- `field_conflicts`?: rename \| merge
- `groups`?: [integer/null]
- `open`?: boolean — Also open the result as a new document (default: only when out is omitted).
- `out`?: string — File to write. Omit to open the result as a new unsaved document instead.
- `pages`?: [string/null]
- `passwords`?: [string/null]
- `paths`: [string]

### `doc_split`
Split into several files written to out_dir: every N pages, before given pages, at top-level bookmarks (bookmarks: true; files named after them, repeated titles get -2, -3), or by file size (max_mb). Files are <name>-partK.pdf.
- `before`?: [integer] — 1-based page numbers that start a new part.
- `bookmarks`?: boolean
- `every`?: integer [min 1]
- `max_mb`?: number
- `out_dir`: string

## Editing page content

### `page_add_text`
Add text as page content (not a comment). Place it with at [x, y] (top-left, points from the top-left of the displayed page) and width (wrap width, default 200), or rect. Newlines start new lines; long lines wrap. Style: font helvetica/times/courier, size, bold, italic, color (#RRGGBB or a name), align left/center/right. Text must be Western European (WinAnsi) characters; others are refused. It stays editable with content_update. Undoable.
- `align`?: left \| center \| right \| justify
- `at`?: [2 numbers]
- `bold`?: boolean
- `color`?: string
- `font`?: helvetica \| times \| courier
- `italic`?: boolean
- `page`: integer [min 1]
- `rect`?: [4 numbers]
- `size`?: number [min 1, max 500]
- `text`: string
- `width`?: number

### `page_add_image`
Add an image file (PNG, JPEG, TIFF, GIF, BMP) as page content: in rect (points from the top-left of the page), or centred at its natural size (shrunk to fit). Undoable; movable with content_update.
- `page`: integer [min 1]
- `path`: string
- `rect`?: [4 numbers]

### `content_list` (read-only)
Text and images added with page_add_text/page_add_image (or Edit a PDF ▸ Add content), per page with a 1-based index, rect (points from the top-left of the page), and text style.
- (no parameters besides `doc`)

### `content_update`
Move/resize (rect), retype (text) or restyle (font, size, bold, italic, color, align) an added item (page, index from content_list). Images: rotate (degrees, multiple of 90, counter-clockwise), flip_h / flip_v (toggle), crop [left, bottom, right, top] as fractions trimmed, image (a file that replaces the picture). Undoable.
- `align`?: left \| center \| right \| justify
- `bold`?: boolean
- `color`?: string
- `crop`?: [4 numbers]
- `flip_h`?: boolean
- `flip_v`?: boolean
- `font`?: helvetica \| times \| courier
- `image`?: string — Replace the picture with this file.
- `index`: integer [min 1]
- `italic`?: boolean
- `page`: integer [min 1]
- `rect`?: [4 numbers]
- `rotate`?: integer
- `size`?: number [min 1, max 500]
- `text`?: string

### `content_delete`
Delete an added item (page, index from content_list). Undoable.
- `index`: integer [min 1]
- `page`: integer [min 1]

### `object_move`
Atomically translate 1–1000 mixed references from object_list by [dx, dy] in displayed points (right/down). Preserves glyph codes, fonts, image data and relative spacing; success is one undo step. Clipping and vertical text are refused. A bad/stale reference refuses the entire move.
- `generation`?: integer [min 0] — Use generation returned by object_list to reject a stale selection.
- `objects`: [{index, kind}]
- `offset`: [2 numbers]
- `page`: integer [min 1]

### `text_edit`
Replace the text of one paragraph (paragraph, from text_paragraphs: rewrapped to the paragraph's width with its line spacing) or one line (line, from text_lines) in place, keeping position, size and colour. For a mixed-style region, editor_text supplies visual row breaks; surviving text keeps its source-run styles and inserted text inherits the surrounding run. For a paragraph, also change its formatting: font (helvetica, times, courier) with bold/italic, size (points), color (#rrggbb), align (left, center, right, justify), underline, line_spacing (× size), char_spacing (points) and scale (horizontal, percent), or move it (dx, dy in points; up is +dy) and rewrap it to a new width (points); text may then be omitted. Its own font is reused when it can show every character and no font/weight change is requested; otherwise it uses a standard font matching the source style or, for Japanese and other text no standard font can show (Cyrillic, Greek), real Mincho/Gothic fallback outlines matching the requested/source family and available weight, from a face that has every character (the result shows the font used). Missing Japanese weights use Regular, not synthetic bold; the small web build has only Gothic Regular. Paragraph bold may be set without font to keep the source family. Text that no available font can show is refused. Undoable.
- `align`?: left \| center \| right \| justify
- `bold`?: boolean
- `char_spacing`?: number — Points.
- `color`?: string — #rrggbb
- `dx`?: number — Paragraph only: move right by this many points (negative: left).
- `dy`?: number — Paragraph only: move up by this many points (negative: down).
- `font`?: helvetica \| times \| courier
- `font_resource`?: string — Explicit source/full page font resource from text_fonts or text_font_import.
- `italic`?: boolean
- `line`?: integer [min 1]
- `line_spacing`?: number — Multiple of the font size (1.2 is ordinary).
- `page`: integer [min 1]
- `paragraph`?: integer [min 1]
- `ranges`?: [{bold, char_spacing, color, font, font_resource, italic, range, scale, size, underline}] — Disjoint UTF-8 byte ranges in replacement text; unspecified source formatting survives.
- `scale`?: number — Horizontal scale in percent.
- `size`?: number
- `text`?: string
- `underline`?: boolean
- `width`?: number — Paragraph only: rewrap to this width in points (dragging the box's edge).

### `text_edit_layout` (read-only)
Measure a paragraph draft using the same PDF rewrite as Apply, without changing the document. Returns source_rect, draft_rect (top-left-origin points), overflow, and the embedded sfnt source faces available to the inline editor. Text defaults to the unchanged paragraph. Optional size, width, font_resource and disjoint UTF-8 ranges preview formatting changes.
- `font_resource`?: string
- `page`: integer [min 1]
- `paragraph`: integer [min 1]
- `ranges`?: [object]
- `size`?: number
- `text`?: string
- `width`?: number

### `text_fonts` (read-only)
List validated embedded source faces and approved full preview faces for a page. Full registered resources can be selected by text_edit.font_resource; preview_only faces are not PDF resource names.
- `page`: integer [min 1]

### `text_font_files` (read-only)
Discover openly licensed, embeddable TrueType/OpenType files on request. Optional directories (at most 16) restrict the scan; with --root, only that root is scanned by default and supplied folders must stay inside it. The scan skips symlinks, collections and invalid/licence-restricted fonts, with depth, entry and byte budgets. Select a returned path with text_font_import.
- `directories`?: [string]

### `text_font_import`
Load an explicitly selected, openly licensed full TrueType/OpenType face into a page. The program's family, embedding permissions and licence declaration are validated. Completes source subsets of the same face without replacing existing glyphs. Returns a font resource usable with text_edit.font_resource. Undoable; respects root confinement. No system-interface fallback is exported.
- `page`: integer [min 1]
- `path`: string

### `image_edit`
Change one of a page's images (number from page_images): action move (rect: new full placement box in top-left-origin points, based on page_images.rect), rotate (quarters clockwise, default 1), flip_horizontal, flip_vertical, replace (path: an image file, drawn in the same place) or delete. Undoable. The selected image crop transforms with its pixels, isolating shared path scopes while retaining neighboring painting. Text-outline clips return a clear error. Rotation/flip use the visible centre. Form artwork supports move/resize/rotate/flip/delete as a group; replace and image_save only support raster images.
- `action`: move \| rotate \| flip_horizontal \| flip_vertical \| replace \| delete
- `image`: integer [min 1]
- `page`: integer [min 1]
- `path`?: string
- `quarters`?: integer
- `rect`?: [4 numbers]

## Header, footer, watermark, background

### `doc_header_footer`
Add a header and/or footer to pages. Text boxes: header_left/center/right, footer_left/center/right. Tokens: <<1>> page number, <<n>> page count, <<1 of n>>, <<Page 1 of n>>, <<1/n>>, dates <<m/d/yyyy>> <<yyyy-mm-dd>> <<mmmm d, yyyy>> (and more), Bates <<Bates Number#6#1#PREFIX#SUFFIX>>. replace: true swaps out existing ones (Update). Undoable.
- `color`?: string — #RRGGBB or a colour name.
- `font_size`?: number
- `footer_center`?: string
- `footer_left`?: string
- `footer_right`?: string
- `header_center`?: string
- `header_left`?: string
- `header_right`?: string
- `margins`?: [4 numbers] — Top, bottom, left, right in points (default 36, 36, 72, 72).
- `pages`?: [integer] — 1-based page numbers to mark (default: all).
- `replace`?: boolean
- `start_number`?: integer [min 1]

### `doc_watermark`
Add a watermark to pages: text, or a picture from `file` (an image, or page `file_page` of a PDF) at `scale` of the page (default 0.5); rotated (degrees counter-clockwise, default 45), semi-transparent (opacity 0–1, default 0.5), text fitted to the page unless font_size is given, on top unless behind: true; moved from the page centre by `offset_x` (right) and `offset_y` (up) points (default 0). replace: true swaps out existing ones. Undoable.
- `behind`?: boolean
- `color`?: string
- `file`?: string
- `file_page`?: integer [min 1]
- `font_size`?: number
- `offset_x`?: number — Points right of the page centre (negative: left).
- `offset_y`?: number — Points above the page centre (negative: below).
- `opacity`?: number [min 0, max 1]
- `pages`?: [integer] — 1-based page numbers to mark (default: all).
- `replace`?: boolean
- `rotation`?: number
- `scale`?: number [max 1]
- `text`?: string

### `doc_background`
Fill page backgrounds with a colour, or a picture from `file` (an image, or page `file_page` of a PDF) fitted at `scale` (default 1), behind the content. Undoable.
- `color`?: string
- `file`?: string
- `file_page`?: integer [min 1]
- `opacity`?: number [min 0, max 1]
- `pages`?: [integer] — 1-based page numbers to fill (default: all).
- `replace`?: boolean
- `scale`?: number [max 1]

### `doc_remove_marks`
Remove every header and footer, watermark or background PdfCraft (or a compatible tool) added. Undoable.
- `kind`: header_footer \| watermark \| background

## Bookmarks

### `bookmark_list` (read-only)
The bookmarks in outline order, one page at a time: each with its path (1-based, as the other bookmark tools take it), title, target page and open state, and its children on the same page. next is the offset of the following page, or null at the end. Bookmarks nested deeper than 33 levels are not listed.
- `limit`?: integer [min 1, max 1000] — Bookmarks in the page (default 100)
- `offset`?: integer [min 0] — Where the page starts, counted from 0 (the previous page's next)

### `bookmark_add`
Add a bookmark that goes to a page, under a parent bookmark (or at the top level), at a position. Undoable.
- `page`: integer [min 1]
- `parent`?: [integer] — Parent bookmark (omit for the top level): 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.
- `position`?: integer [min 1] — 1-based position among the parent's children (default: last).
- `title`: string

### `bookmark_rename`
Change a bookmark's title. Undoable.
- `path`: [integer] — The bookmark: 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.
- `title`: string

### `bookmark_delete`
Delete a bookmark and the bookmarks under it. Undoable.
- `path`: [integer] — The bookmark: 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.

### `bookmark_move`
Move a bookmark (with its children) under another parent, or within its level. Undoable.
- `parent`?: [integer] — New parent (omit for the top level): 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.
- `path`: [integer] — The bookmark to move: 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.
- `position`?: integer [min 1] — 1-based position among the new parent's children, counted after the bookmark is removed (default: last).

### `bookmark_set_page`
Point a bookmark at another page. Undoable.
- `page`: integer [min 1]
- `path`: [integer] — The bookmark: 1-based positions from the top level, e.g. [2, 1] = the first child of the second bookmark.

### `bookmark_from_structure`
Make bookmarks from the document's tagged headings (H, H1-H6), nested by level under a new first bookmark titled "Untitled". Fails if the document has no tagged headings. Returns the first page of the bookmark tree (see bookmark_list). Undoable.
- (no parameters besides `doc`)

## Links

### `link_list` (read-only)
Every link: page, 1-based index (for link_edit/link_delete), rect (points from the top-left of the page), and where it goes (url or to_page).
- (no parameters besides `doc`)

### `link_add`
Add a link over rect on page that opens url or goes to to_page. Appearance: visible (rectangle), color, width 1-3, highlight none/invert/outline/inset. Undoable.
- `color`?: string
- `highlight`?: none \| invert \| outline \| inset
- `page`: integer [min 1]
- `rect`: [4 numbers]
- `to_page`?: integer [min 1]
- `url`?: string
- `visible`?: boolean
- `width`?: number

### `link_edit`
Change a link's rect, destination (url or to_page) or appearance. Undoable.
- `color`?: string
- `highlight`?: none \| invert \| outline \| inset
- `index`: integer [min 1]
- `page`: integer [min 1]
- `rect`?: [4 numbers]
- `to_page`?: integer [min 1]
- `url`?: string
- `visible`?: boolean
- `width`?: number

### `link_delete`
Delete one link (page, index from link_list). Undoable.
- `index`: integer [min 1]
- `page`: integer [min 1]

### `links_from_urls`
Find web addresses (http://, https://, www.) in the text of every page and make them clickable links. Returns the URLs. Undoable.
- (no parameters besides `doc`)

### `links_remove`
Remove every link in the document (or on the given pages). Undoable.
- `pages`?: [integer] — 1-based page numbers whose links to remove (default: all).

### `link_open`
Follow a local GoToR link in PdfCraft: open the referenced PDF as a new document, respecting --root. page and index use link_list numbering. Named destinations are reported but not applied.
- `index`: integer [min 1]
- `page`: integer [min 1]
- `password`?: string — Optional password for the linked PDF.

## Comments and review

### `comment_list` (read-only)
Every comment (annotation other than links, form widgets and pop-ups) with its page, index, id, type, author, text, date, rectangle, colour, review status and replies.
- `page`?: integer [min 1] — Only this page.

### `comment_add`
Add a comment as Acrobat's commenting tools do. Geometry is in points with the origin at the top-left of the displayed page, y down (as in page_render images at 72 dpi and text_find rects). note: `at` [x, y] (icon top-left). stamp: `at` [x, y] (its centre) and `stamp`: approved, completed, confidential, draft, final, for comment, for public release, information only, not approved, not for public release, preliminary results, void, accepted, initial here, rejected, sign here, witness; dynamic: true for the dynamic approved/confidential/received/reviewed/revised stamps with a By … at … line. highlight/underline/strikeout/squiggly: `find` (text on the page to mark; every match with all: true) or `quads`. rectangle/oval/textbox: `rect` [x0, y0, x1, y1]. line/arrow: `from`, `to`. Optional `endings` (two names: start, end) for a line, arrow or polyline, or one name for a callout: None, Square, Circle, Diamond, OpenArrow, ClosedArrow, Butt, ROpenArrow, RClosedArrow, Slash. An arrow without endings is None then OpenArrow. ink: `strokes` [[[x, y], …], …]. polygon/cloud/polyline (connected lines): `points` [[x, y], …]. callout: `rect` (its text box), `to` (the point the arrow touches), optional `knee`. caret (inserted text): `at`, the insertion point on the baseline. replace (Replace Text): `find` or `quads` like highlight, `contents` the replacement. attachment: `path` (the file), `at`, optional `icon` (PushPin, Paperclip, Graph, Tag). Undoable. Text a text box, callout or stamp draws in the standard fonts that they can't draw (Chinese, Greek) is saved as typed and drawn as `?`; `warnings` in the result says so.
- `all`?: boolean — Mark every match of `find` on the page, not just the first.
- `at`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `author`?: string
- `color`?: string — #RRGGBB or a name: yellow, red, orange, green, blue, purple, pink, black, gray, white.
- `contents`?: string — The comment text (what a text box shows).
- `dynamic`?: boolean
- `endings`?: [None \| Square \| Circle \| Diamond \| OpenArrow \| ClosedArrow \| Butt \| ROpenArrow \| RClosedArrow \| Slash] — Line endings. Two names (start, end) for a line, arrow or polyline; one name for a callout.
- `fill`?: string — #RRGGBB or a name: yellow, red, orange, green, blue, purple, pink, black, gray, white.
- `find`?: string — Text on the page to mark up (case-insensitive).
- `font_size`?: number
- `from`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `icon`?: string — note: Comment, Note, Help, Insert, Key, NewParagraph, Paragraph; attachment: PushPin, Paperclip, Graph, Tag.
- `knee`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `opacity`?: number [min 0, max 1]
- `page`: integer [min 1]
- `path`?: string — attachment: the file to attach.
- `points`?: [[2 numbers]]
- `quads`?: [[8 numbers]]
- `rect`?: [4 numbers]
- `stamp`?: string
- `strokes`?: [[[2 numbers]]]
- `to`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `type`: note \| highlight \| underline \| strikeout \| squiggly \| replace \| rectangle \| oval \| line \| arrow \| ink \| textbox \| stamp \| polygon \| cloud \| polyline \| callout \| caret \| attachment
- `width`?: number [min 0] — Line width in points.

### `comment_reply`
Add a reply to a comment's thread. Undoable.
- `author`?: string
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `page`?: integer [min 1] — With `index`, instead of `id`.
- `text`: string

### `comment_set_status`
Set a comment's review status (Acrobat: Set status), recorded as a status reply. Undoable.
- `author`?: string
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `page`?: integer [min 1] — With `index`, instead of `id`.
- `status`: none \| accepted \| rejected \| cancelled \| completed

### `comment_mark`
Mark or unmark a comment with a checkmark (Acrobat: Mark with checkmark), recorded as a private reply. Undoable.
- `author`?: string
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `marked`?: boolean — Default true.
- `page`?: integer [min 1] — With `index`, instead of `id`.

### `comment_lock`
Lock or unlock a comment (Properties ▸ Locked). Locked comments can't be moved, resized, restyled or deleted; their text stays editable. Undoable.
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `locked`?: boolean — Default true.
- `page`?: integer [min 1] — With `index`, instead of `id`.

### `comment_edit`
Change a comment's text, colour, opacity, line width, fill (rectangle/oval/polygon; "none" removes it), rectangle (rectangle/oval/text box/stamp) or position (`move` [dx, dy] in points). Stamps keep their original appearance when resized. One undo step.
- `color`?: string — #RRGGBB or a name: yellow, red, orange, green, blue, purple, pink, black, gray, white.
- `contents`?: string
- `fill`?: string — Interior colour of a rectangle, oval or polygon: #RRGGBB, a colour name, or "none" for no fill.
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `move`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `opacity`?: number [min 0, max 1]
- `page`?: integer [min 1] — With `index`, instead of `id`.
- `rect`?: [4 numbers]
- `width`?: number [min 0]

### `comment_delete`
Delete a comment with its pop-up and replies. Undoable.
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `page`?: integer [min 1] — With `index`, instead of `id`.

### `comments_hide`
Hide or show every comment on the page (fields and links still draw). A view setting: the file doesn't change.
- `hidden`?: boolean — Default true.

### `comments_summarize`
Make a PDF summarising every comment (number, author, type, date, text, replies), sorted by page, author, date or type.
- `open`?: boolean — Also open the result as a new document (default: only when out is omitted).
- `out`?: string — File to write. Omit to open the result as a new unsaved document instead.
- `sort`?: page \| author \| date \| type

### `comment_image_preview` (read-only)
Return a PNG of the page without the selected image signature/initials (layer=background, default), or its embedded image with alpha (layer=image). Includes the displayed rectangle, document rotation, image_rotation (how far clockwise the image is shown turned) and annotation opacity. Cache these layers for live placement/resizing; commit once with comment_edit. Does not change the document or undo history.
- `dpi`?: number (=96) [min 1, max 600]
- `id`?: string — The comment's id (from comment_list).
- `index`?: integer [min 1] — 1-based position on the page, as comment_list reports.
- `layer`?: background \| image (="background")
- `page`?: integer [min 1] — With `index`, instead of `id`.

### `stamp_custom`
Stamp a picture: a PDF page (file_page, default 1) or an image file, centred at at [x, y] (points from the top-left of the displayed page) at its natural size, at most 200 pt. name labels it (default: the file name). Undoable.
- `at`: [2 numbers]
- `author`?: string
- `file_page`?: integer [min 1]
- `name`?: string
- `page`: integer [min 1]
- `path`: string

### `fill_sign_add`
Fill in a form that has no fields, as Acrobat's Fill & Sign does: type text (`text`, default 10 pt; `font_size` 4–300 pt), place a check, cross, dot or line, today's date (in Preferences ▸ Date format, see fill_sign_date_format, or `format`; `font_size` also applies), or a signature or initials (either `text` drawn in a script font, or `path` to a local PNG/JPEG image up to 4 MiB and 32 megapixels, scaled down to 4 megapixels, preserving transparency; with `scan: true`, `path` is instead a photo of a signature on paper, within the same limits: the signature is found, and the paper, shadows and table around it are removed, with `sensitivity` 0–100, default 50, picking up fainter ink when higher). `at` [x, y] is in points from the top-left of the page: text's top-left, mark's centre, signature's left edge centred vertically. Image signatures fit within 150 pt wide and 32 pt tall (24 pt for initials). Creates movable, undoable annotations. Typed text the standard fonts can't draw is saved and drawn as `?` (`warnings` in the result says so); a typed signature neither the script font nor its fallback can draw is refused (pass `path` instead).
- `at`: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `author`?: string
- `font_size`?: number [min 4, max 300] — For type text or date (default 10 pt).
- `format`?: string — For type date: this pattern instead of the date-format preference, e.g. "dd.mm.yyyy".
- `language`?: string — For type date: month and weekday names in this language code (see fill_sign_date_format) instead of the preference.
- `page`: integer [min 1]
- `path`?: string — PNG or JPEG for signature/initials; pass either path or text.
- `scan`?: boolean — With path: scan a photo of a signature on paper (default false).
- `sensitivity`?: integer [min 0, max 100] — With scan: how faint ink may be, 0–100 (default 50).
- `text`?: string
- `type`: text \| check \| cross \| dot \| line \| date \| signature \| initials

### `fill_sign_date_format`
Preferences ▸ Date format: the pattern Fill & Sign dates use (default m/d/yyyy). Set it with `format` (Acrobat date codes yyyy yy mmmm mmm mm m dddd ddd dd d, other runs of y, m or d are refused; H h M s t are time letters and need \ before them; \ shows the next character as is), or read it. `language` sets the language of month and weekday names (a code from `languages`, or `auto` to follow the app's interface language; English headless). Returns the format, the language, today in them, `unwritable` (characters of today's date that Fill & Sign can't write into a PDF yet, Western European only; fill_sign_add refuses such a date), the ready-made presets and the languages.
- `format`?: string
- `language`?: string

### `doc_flatten`
Merge comment and/or form field appearances into the page content, so they print and display everywhere but can no longer be edited. Undoable until saved.
- `comments`?: boolean — Default true.
- `fields`?: boolean — Default true.

## Forms

### `form_fields` (read-only)
Every interactive form field: name, type (text, checkbox, radio, combo, list, button, signature), value, options, page, rect (top-left-origin points) and rotation (0, 90, 180 or 270 degrees counterclockwise), read-only and required flags.
- (no parameters besides `doc`)

### `form_fill`
Set several fields at once (one undo step). values maps field names (from form_fields) to: a string for text fields, combo boxes and radio groups (an option), true/false for check boxes, an array of strings for multi-select lists. Appearances are regenerated so every viewer shows the values. A value whose characters the field's font can't draw (Chinese in a Helvetica field) is still saved; `warnings` in the result names the field and character: PdfCraft draws `?` there and asks other viewers to redraw the field from its value.
- `values`: object — Field name → value.

### `form_reset`
Reset fields to their default values: all of them, or only those listed. Undoable.
- `fields`?: [string]

### `form_add_field`
Add a form field on a page. type: text, date, checkbox, radio, combo, list, button, image (a picture placeholder; fill it with form_set_image), signature. rect in points from the top-left of the displayed page [x0, y0, x1, y1]. name defaults to Acrobat's next free name (Text1, Check Box1, Group1, Dropdown1, List Box1, Button1, Image1, Signature1, Date1). Radio buttons join the radio group named by group (a new group otherwise) with the export value export. Returns the field's name. Undoable.
- `caption`?: string — Button label.
- `editable`?: boolean — Combo box accepts typed text.
- `export`?: string — Radio button export value (default Choice1).
- `group`?: string — Radio group to join.
- `multi_select`?: boolean
- `multiline`?: boolean
- `name`?: string
- `options`?: [string] — Combo box / list box items.
- `page`: integer [min 1]
- `rect`: [4 numbers]
- `type`: text \| date \| checkbox \| radio \| combo \| list \| button \| image \| signature

### `form_delete_field`
Delete a form field and all its widgets. Undoable.
- `field`: string

### `form_set_props`
Change field properties: give field for one field, or fields for a list of unique field names (1–1000). A bulk change is atomic and one Undo step; an invalid or locked field leaves every field unchanged. Only the given properties change, and partial appearance changes preserve each field's other colours and font. name (rename), rect (position) and rotation require a single field. General and Options: tooltip, read_only, required, multiline, max_length (0 = no limit), options (combo/list items), font_size (0 = auto), format, validate, calculate (Acrobat's native AF rules). Options: align (left, center, right), default (Reset form's value; check boxes/radio buttons use their on state, "" for off), flags { scroll, rich_text, password, file_select, spell_check, comb (needs max_length), sort, editable, multi_select, commit_immediately }, check_style (check boxes/radio buttons: check, circle, cross, diamond, square, star). rotation is 0, 90, 180 or 270 degrees counterclockwise and swaps width/height when the axis changes. Undoable.
- `align`?: left \| center \| right
- `appearance`?: object — Appearance tab: border, fill, text_color (#RRGGBB, a name or "none"), width (0–12 points; 1 thin, 2 medium, 3 thick), style (solid, dashed, beveled, inset, underline), font (helvetica, times, courier).
- `calculate`?: any — Calculate tab: {"op": "sum"|"product"|"average"|"min"|"max", "fields": ["a", "b"]}, {"notation": "Price * Qty"} (simplified field notation), or "none".
- `check_style`?: check \| circle \| cross \| diamond \| square \| star — Check boxes and radio buttons: the mark shown when on.
- `default`?: string
- `field`?: string — The field's current name.
- `fields`?: [string] — Apply the same changes to these fields in one atomic edit. Use either field or fields.
- `flags`?: object
- `font_size`?: number [min 0]
- `format`?: any — Format tab: {"type": "number", "decimals": 2, "currency": "$", "separator": 0-4, "negative": 0-3}, {"type": "percent"}, {"type": "date"|"time", "pattern": "mm/dd/yyyy"}, {"type": "zip"|"zip4"|"phone"|"ssn"}, {"type": "mask", "mask": "AA-9999"}, or "none".
- `locked`?: boolean — Lock the field's properties (only unlocking is accepted while locked).
- `max_length`?: integer [min 0]
- `multiline`?: boolean
- `name`?: string
- `options`?: [string]
- `read_only`?: boolean
- `rect`?: [4 numbers] — Move/resize: points from the top-left of the displayed page.
- `required`?: boolean
- `rotation`?: 0 \| 90 \| 180 \| 270 — Widget rotation in degrees, counterclockwise. Changing between horizontal and vertical swaps the rectangle around its center.
- `tooltip`?: string
- `validate`?: any — Validate tab: {"min": 0, "max": 100} (either may be left out) or "none".

### `form_set_image`
Show an image file (PNG, JPEG, TIFF, GIF or BMP) in an image field or button, scaled to fit and centred (what clicking an image field does). On an XFA form the picture is kept in its data too (base64, as Designer saves it) and the form shows it from there. Undoable.
- `field`: string
- `path`: string

### `form_tab_order`
Set the tab order of pages (default all): row (top to bottom, left to right), column, structure, or annotations (unspecified). Or order tabs manually: `field` with `move` earlier|later moves that field one place on its page. Returns the resulting order of fields. Undoable.
- `field`?: string
- `move`?: earlier \| later
- `order`?: row \| column \| structure \| annotations
- `pages`?: [integer] — 1-based page numbers to set (default: all).

### `form_detect_fields`
Prepare a form ▸ automatic field detection: find the blanks a printed form asks to be filled (underscore runs, lines, empty boxes, small squares for check boxes) and name each field from its label. With add (default true) the fields are created as one undoable step; otherwise they are only proposed. Returns page (1-based), kind, name and rect (points, origin bottom-left).
- `add`?: boolean
- `pages`?: [integer] — 1-based page numbers to look at (default: all).

### `form_actions` (read-only)
Field Properties ▸ Actions: the field's action for each trigger (mouse_up, mouse_down, mouse_enter, mouse_exit, on_focus, on_blur).
- `field`: string

### `form_set_actions`
Field Properties ▸ Actions: replace the field's actions. Each item: trigger (mouse_up, mouse_down, mouse_enter, mouse_exit, on_focus, on_blur) and one of javascript (source), url, reset (field names; [] for all), menu (Print, NextPage, PrevPage, FirstPage, LastPage), page (1-based), show / hide (field names), submit (URL). Triggers not listed lose their action. Undoable.
- `actions`: [{hide, javascript, menu, page, reset, show, submit, trigger, url}]
- `field`: string

### `form_set_script`
Field Properties ▸ Run custom script: set field's JavaScript for event keystroke, format, validate or calculate (the field's actions; calculated fields join the calculation order) or mouse_up (a button's action). Omit script to remove it. The scripts use Acrobat's object model (event.value, event.rc, getField, util.printf, …) and run when the field changes. Undoable.
- `event`: keystroke \| format \| validate \| calculate \| mouse_up
- `field`: string
- `script`?: string

### `form_merge_data`
Collect the field values of form data files (FDF, XFDF) or filled-in PDF forms into one CSV file at path: a column per field name, a row per file. Returns the row and column counts.
- `path`: string
- `paths`: [string]

### `doc_export_data`
Write comments and/or form data to path; the extension picks the format: .xfdf or .fdf (comments and/or fields), .xml, .csv or .txt (form data). For an XFA form, .xml is its data alone (rooted at the form's root data node, as Acrobat exports it) and .xdp an XML Data Package holding the whole datasets. what: all (default), comments, fields.
- `path`: string
- `what`?: all \| comments \| fields

### `doc_import_data`
Import comments and/or field values from an XFDF, FDF, XML, CSV or tab-delimited text file (detected from its content). Comments with the same name are replaced; values go through the form's formats and validation. For an XFA form, an XDP, datasets or data XML file replaces the form's data: a laid-out form is laid out again from it (rows included) and its calculations run. Undoable.
- `path`: string

## JavaScript

### `js_run`
Run Acrobat JavaScript in the document, as the JavaScript console does (or as push button `field`'s Mouse Up script when field is given; on a laid-out XFA form, `field` runs that button's XFA click script instead, JavaScript or FormCalc, which can add and remove rows and show or hide subforms). The form object model is available: this/getField, event, app, util, console, display, color, and the document-level scripts. Field changes and resetForm are applied as one undoable step; returns the script's alerts, console output, requests (print, page, url, submit) and error.
- `field`?: string — Run as this button's Mouse Up event.
- `script`: string

### `js_enabled`
Preferences ▸ JavaScript ▸ Enable Acrobat JavaScript: set it with `enabled`, or read it. With JavaScript off, field scripts other than Acrobat's AF calls don't run.
- `enabled`?: boolean

### `js_document_scripts` (read-only)
List the document-level JavaScripts (name and source), which define functions field scripts use.
- (no parameters besides `doc`)

### `js_set_document_script`
Add or replace the document-level JavaScript `name` with `script`, or delete it (script omitted). Undoable.
- `name`: string
- `script`?: string

## Redaction, sanitizing, security

### `redact_mark`
Mark content for redaction (nothing is removed until redact_apply). One of: rect [x0, y0, x1, y1] (points from the top-left of the displayed page) with page; find (text, every match); words (a list of words or phrases, every match of each; the result's matched_words says how many marks each made); pattern (phone, email, credit-card, ssn, date: every match, Acrobat's Search & Redact patterns); whole_pages: true. find and words accept case_sensitive and whole_words (both default false). find, words, pattern and whole_pages work on pages (default all). overlay: text shown on the box once applied, or code_set (foia: U.S. FOIA (b)(1)(A)…(b)(9); privacy-act: U.S. Privacy Act (d)(5), (j)(1)…(k)(7)) with codes, shown as "(b)(6), (b)(7)(C)"; fill: box colour (default black). Undoable.
- `author`?: string
- `case_sensitive`?: boolean — Match letter case for find or words (default false).
- `code_set`?: foia \| privacy-act
- `codes`?: [string] — Redaction codes from code_set, e.g. ["(b)(6)"].
- `fill`?: string — #RRGGBB or a colour name.
- `find`?: string
- `overlay`?: string
- `page`?: integer [min 1]
- `pages`?: [integer] — 1-based page numbers to search or mark (default: all).
- `pattern`?: phone \| email \| credit-card \| ssn \| date
- `rect`?: [4 numbers]
- `whole_pages`?: boolean
- `whole_words`?: boolean — Match whole words for find or words (default false).
- `words`?: [string]

### `redact_apply`
Apply the redaction marks (all, or those on pages): text, images, vectors, comments and form fields under them are removed for good and boxes are drawn in their place. A verification pass fails the operation if anything readable remains. Undoable until saved; the saved file no longer contains the content.
- `pages`?: [integer] — 1-based page numbers whose marks to apply (default: all).

### `redact_clear`
Remove every redaction mark without applying it. Undoable.
- (no parameters besides `doc`)

### `doc_audit_redactions` (read-only)
Find faux redactions: opaque filled rectangles painted over text that is still extractable, and /Redact annotations that were marked but never applied. Paint-order and colour-aware: a rectangle counts only when painted after the text and dark enough to hide it (page backgrounds and light shading are not flagged). Each finding reports the 1-based page, the kind (covered-text or unapplied-mark), the rectangle, and the hidden text. Fails closed: unreadable content is an error, never a clean bill. A properly applied redaction removes the text and never flags.
- (no parameters besides `doc`)

### `doc_hidden_info` (read-only)
What Remove Hidden Information would remove, by category (metadata, attachments, comments, form-fields, hidden-text, hidden-layers, bookmarks, links-actions-scripts, private-data) with counts.
- (no parameters besides `doc`)

### `doc_remove_hidden`
Remove the listed categories (see doc_hidden_info), or every category when none are listed (Sanitize Document). Form fields are flattened so their values stay visible. The next save rewrites the whole file. Undoable until saved.
- `categories`?: [metadata \| attachments \| comments \| form-fields \| hidden-text \| hidden-layers \| bookmarks \| links-actions-scripts \| private-data]

### `doc_protect`
Encrypt the document (applied by the next doc_save, a full rewrite). open_password is needed to open it. permissions_password is needed to change security and lifts the restrictions given by printing/changes/copy/accessibility; those restrictions (and their defaults) apply only when permissions_password is given. With open_password alone the document is encrypted and everything stays allowed, so passing a restriction without permissions_password is an error. Passwords are never echoed back. Undoable.
- `accessibility`?: boolean — Allow screen readers to read the text (needs permissions_password; default true).
- `changes`?: none \| pages \| fill-sign \| comment-fill-sign \| any-except-extract — Needs permissions_password. Default none.
- `compatibility`?: aes-256 \| aes-128 \| rc4-128 \| rc4-40 — Default aes-256 (Acrobat X and later).
- `copy`?: boolean — Allow copying text and images (needs permissions_password; default false).
- `encrypt_metadata`?: boolean — Default true.
- `open_password`?: string — Required to open the document. On its own it restricts nothing.
- `permissions_password`?: string — Required to change security; enables printing/changes/copy/accessibility and their defaults.
- `printing`?: none \| low \| high — Needs permissions_password. Default high.

### `doc_unprotect`
Remove password security (the document must have been opened with its permissions password, or have none). Applied by the next doc_save. Undoable.
- (no parameters besides `doc`)

## Digital signatures

### `sign_list` (read-only)
Every signature field with its validation: status (valid, unknown = intact but the signer isn't trusted, invalid, unsigned), signer and certificate, date, reason, location, certification level, page and rect, the revision it covers and changes made after signing (none, allowed, disallowed), with Acrobat-style explanations.
- (no parameters besides `doc`)

### `sign_id_create`
Create a self-signed digital ID and save it as a password-protected .p12 file (Acrobat: Configure a new digital ID ▸ Create a new digital ID ▸ Save to file). Default key: 2048-bit RSA, valid 5 years.
- `country`?: string — Two-letter country code.
- `email`?: string
- `key`?: rsa2048 \| rsa3072 \| rsa4096 \| p256
- `name`: string
- `organization`?: string
- `password`: string
- `path`: string — The .p12 file to write.
- `unit`?: string
- `years`?: integer [min 1, max 50]

### `sign_keychain_ids` (read-only)
macOS: the signing identities in the user's keychains (certificate details and the keychain: reference sign_document takes). The private keys stay in the Keychain, which may ask the user to allow their use.
- (no parameters)

### `sign_windows_ids` (read-only)
Windows: signing identities in the Current User Personal certificate store (certificate details and the windows: reference sign_document takes). Private keys remain in CNG; Windows may ask permission to use them. `unusable` lists the store's other certificates with why they can't sign (no private key, an unsupported key type, a key CNG can't open).
- (no parameters)

### `sign_document`
Sign with a digital ID (a .p12/.pfx path, or on macOS a Keychain identity: "keychain:<common name or fingerprint>" from sign_keychain_ids, or on Windows a store identity: "windows:<common name or fingerprint>" from sign_windows_ids) and save the signed file to `out` (signing always saves, as in Acrobat; the document then shows the signed file). Sign an existing empty signature field (`field`), or a new one on `page` at `rect` (omit rect for an invisible signature). certify: no_changes, form_fill or comments makes a certification signature. graphic shows a picture where the signer's name would be large (Acrobat: Configure Signature Appearance): {"image": path} (PNG or JPEG), {"text": name} (typed in the Fill & Sign script font) or {"strokes": [[[x, y], …], …]} (y up, the drawing pad 1 wide); it needs a visible signature. PAdES B-B, SHA-256 (SHA-384 for P-384 keys).
- `certify`?: no_changes \| form_fill \| comments
- `contact`?: string
- `field`?: string
- `graphic`?: {image, strokes, text} — Exactly one of image, text or strokes.
- `id`: string — Digital ID file (.p12 / .pfx), keychain: reference on macOS, or windows: reference on Windows.
- `location`?: string
- `out`: string — Where to save the signed document.
- `page`?: integer [min 1]
- `password`?: string
- `reason`?: string
- `rect`?: [4 numbers]

### `sign_trust`
Add certificates (.cer/.crt/.pem/.der, or the certificates in a .p12 with `password`) to the trusted certificates used to validate signatures, or clear the list (clear: true). Every open document is revalidated. Returns the trusted list.
- `clear`?: boolean
- `password`?: string
- `paths`?: [string]

## Export, optimize, print

### `doc_export_images`
Write pages as PNG, JPEG or TIFF files (`<name>_page_<n>.png|jpg|tif`) into a folder, at a resolution (default 150 dpi). JPEG and TIFF are flattened onto white paper. A page too large for the renderer at that resolution is drawn at the most it allows, listed in `lower_dpi` ({page, dpi}). Includes unsaved edits.
- `dpi`?: number [min 18, max 1200]
- `folder`: string
- `format`?: png \| jpeg \| tiff
- `pages`?: [integer] — 1-based page numbers to export (default: all).
- `quality`?: integer [min 1, max 100] — JPEG quality (default 85).

### `doc_export_all_images`
Write the images that pages use into a folder (`<name>_Page_<n>_Image_<k>.jpg|png`), each once: JPEG images unchanged, others as PNG with their soft mask as alpha. min_size skips images with fewer pixels on their shorter side. Images that can't be decoded yet (JPEG 2000, JBIG2, CCITT, separations) are listed under skipped. Includes unsaved edits.
- `folder`: string
- `min_size`?: integer [min 0] — Skip images smaller than this many pixels on their shorter side (default 0).
- `pages`?: [integer] — 1-based page numbers whose images to export (default: all).

### `doc_export_office`
Export a PDF ▸ Word (.docx), PowerPoint (.pptx, one slide per page), HTML (.html, one file with images inline) or RTF (.rtf), chosen by path's extension: text, headings, bold and italic. Word uses borderless inferred tables and positioned editable shapes on pages with artwork, rotated or large text; each source page retains its size. Font matching and vector graphics remain limited.
- `path`: string

### `doc_reduce`
Write a smaller copy of the document to `path` with Acrobat's Reduce File Size choices: images above 225 ppi downsampled to 150 ppi and JPEG-compressed (medium quality), thumbnails dropped, identical fonts and images merged, unused objects dropped, compressed object streams. If the copy wouldn't be smaller, nothing is written and `written` is false. The open document is unchanged.
- `path`: string

### `doc_optimize`
Write an optimized copy to `path` (Acrobat's PDF Optimizer). color / gray: { downsample, ppi, above_ppi, compression: jpeg|zip|retain, quality 1–100 } (defaults: downsample to 150 ppi above 225, JPEG 60). Images are measured where pages draw them and replaced only when smaller. discard_*: thumbnails (default true), alternate_images (true), tags, print_settings; flate_unencoded (true); remove_invalid_links and remove_unreferenced_dests (true); images and forms the pages list but never draw are always dropped (unused_xobjects). discard: Remove Hidden Information categories (metadata, attachments, comments, form-fields, hidden-text, hidden-layers, bookmarks, links-actions-scripts, private-data). Signed documents are refused. The open document is unchanged.
- `color`?: object
- `discard`?: [string]
- `discard_alternate_images`?: boolean
- `discard_print_settings`?: boolean
- `discard_tags`?: boolean
- `discard_thumbnails`?: boolean
- `flate_unencoded`?: boolean
- `gray`?: object
- `path`: string
- `remove_invalid_links`?: boolean
- `remove_unreferenced_dests`?: boolean

### `doc_audit_space` (read-only)
How many bytes each kind of content takes and its share of the file (PDF Optimizer ▸ Audit space usage): images, content streams, fonts, forms, comments, structure, bookmarks, … and document overhead.
- (no parameters besides `doc`)

### `doc_print`
Print with Acrobat's Print dialog options, or save the print-ready PDF. pages: a range such as "1-3, 6, 9-" (page labels allowed; default all); subset odd/even; reverse. layout: fit (default), actual, shrink, custom (scale %), multiple (per_sheet 2/4/6/9/16, order, border, auto_rotate; cut-stack order arranges single-sided sheets for cutting into piles and stacking left to right, top to bottom, keeping sheet order within each pile; duplex must be off), booklet (booklet_subset both/front/back, binding left/right), poster (scale %, overlap pt, cut_marks). orientation auto/portrait/landscape; comments_forms document / document-and-markups (default) / document-and-stamps / form-fields-only; paper Letter/Legal/Tabloid, ARCH A/B/C/D/E1/E, ANSI C/D/E, or A0/A1/A2/A3/A4/A5 (short names or full preset labels); use layout actual for 100% in the print-ready PDF; printer drivers may still substitute paper or scale. Then path (save) or printer (a name or "default") with copies, collate, duplex off/long-edge/short-edge, grayscale, and options (driver options from printer_options, CUPS).
- `auto_rotate`?: boolean
- `binding`?: left \| right
- `booklet_subset`?: both \| front \| back
- `border`?: boolean
- `collate`?: boolean
- `comments_forms`?: document \| document-and-markups \| document-and-stamps \| form-fields-only
- `copies`?: integer [min 1, max 999]
- `cut_marks`?: boolean
- `duplex`?: off \| long-edge \| short-edge
- `grayscale`?: boolean
- `layout`?: fit \| actual \| shrink \| custom \| multiple \| booklet \| poster
- `options`?: object — Printer driver options from printer_options: key → choice value.
- `order`?: horizontal \| horizontal-reversed \| vertical \| vertical-reversed \| cut-stack
- `orientation`?: auto \| portrait \| landscape
- `overlap`?: number [min 0]
- `pages`?: string
- `paper`?: string
- `path`?: string
- `per_sheet`?: integer [min 1, max 256]
- `printer`?: string
- `reverse`?: boolean
- `scale`?: number
- `subset`?: all \| odd \| even

### `printers` (read-only)
The printers the system's print spooler knows (CUPS on macOS and Linux), with the default marked.
- (no parameters)

### `printer_options` (read-only)
A printer driver's own job options (CUPS: from its PPD), such as the paper tray, paper type or finishing: key, label, group, default and choices. Pass chosen values to doc_print as options. Empty on Windows, where the driver's preferences window holds them.
- `printer`: string

### `print_readiness` (read-only)
Verification only. Reports effective image resolution where each image is drawn (not against the page size), page boxes and bleed past the trim, output intents, fonts that are not embedded, and the PDF/A-2b structural result. Does not modify the document, embed fonts, invent a press profile, or check PDF/X.
- (no parameters besides `doc`)

## Compare

### `doc_compare` (read-only)
Compare the text of two open documents: other is the older version, doc the newer. Returns counts and each change (replaced, inserted, deleted) with the old and new text, pages (1-based) and rectangles (points, origin bottom-left).
- `limit`?: integer [min 1] — List at most this many changes (default 500).
- `other`: integer — The older document (from doc_open).
- `visual`?: boolean — Also compare how pages look (page n with page n): regions that differ visually.

### `doc_compare_report`
Write the compare summary report (a PDF listing every change) to path.
- `other`: integer
- `path`: string

### `doc_compare_mark`
Add the differences from other (older) to doc (newer) as comments in doc: highlights over replaced (blue) and inserted (green) text, notes where text was deleted (red), authored Compare. Undoable.
- `other`: integer

## Scan and OCR

### `page_enhance_camera`
Straighten a photographed document (Scan & OCR ▸ Enhance ▸ Camera image): the part of the page inside the four corners (x1, y1, … x4, y4 in top-left-origin points, any order, a convex quadrilateral; when omitted, the document's edges are found automatically, or an error says they could not be) is warped to an upright rectangle that replaces what the page shows, at the page picture's own resolution (at most 600 dpi). mode is how it looks: original, colour (default), greyscale or bw (black and white, stored losslessly). level (0–100, default 0) then cleans the photo up: even lighting so the paper turns white (casts, shadows, dark edges), more contrast, and from 60 no isolated specks; colour ink stays colour. For bw the level is the threshold (higher keeps fainter strokes black). The page's comments, links and bookmarks stay. Undoable.
- `corners`?: [8 numbers]
- `level`?: integer [min 0, max 100]
- `mode`?: original \| colour \| greyscale \| bw
- `page`: integer [min 1]

### `ocr_status` (read-only)
Whether text recognition is available (its models are installed: release packages include them; a source build fetches them with `cargo xtask models`; PDFCRAFT_MODELS overrides), where it looks for them, and the languages it reads.
- (no parameters)

### `ocr_recognize`
Scan & OCR ▸ Recognize text: render pages, read the words in them and add them as invisible text over the page image, so scanned pages become searchable and selectable (a searchable image; the image is not changed). Pages that already have text are skipped unless skip_text_pages is false; then pictures on those pages are read too, and recognised words that the page's own text already has (an earlier OCR layer included) are left out and counted as already_on_page. Returns each page's recognised text, word count or why it was skipped. Needs the OCR models (ocr_status). Undoable as one step.
- `dpi`?: number [min 72, max 600] — Resolution pages are read at (default 300; a scanned page is read at most at its own resolution).
- `language`?: en — Document language (default en).
- `pages`?: [integer] — 1-based page numbers to recognise (default: all).
- `skip_text_pages`?: boolean — Leave pages that already contain text alone (default true). false also reads pictures on such pages, without adding their text again.

### `ocr_recognize_files`
Scan & OCR ▸ Recognize text ▸ In multiple files: read every page of each PDF in paths and write the searchable result into folder under the same name (pages that already have text are left alone unless skip_text_pages is false, as in ocr_recognize). Returns, per file, the output path, word count and skipped pages, or the error.
- `dpi`?: number [min 72, max 600]
- `folder`: string
- `language`?: en
- `paths`: [string]
- `skip_text_pages`?: boolean — Leave pages that already contain text alone (default true); see ocr_recognize.

## Accessibility and PDF/A

### `accessibility_check` (read-only)
Run the Accessibility Checker's full check (32 rules in 7 categories: document, page_content, forms, alternate_text, tables, lists, headings). Each rule is passed, failed (with findings and pages), manual (needs a person) or skipped. Findings on locatable figures, annotations and form widgets include bbox_user_space in PDF coordinates. Colour contrast is off unless all is true; rules (ids such as tagged-pdf, figures-alt-text) or categories narrow the check; pages limit the page rules.
- `all`?: boolean — Include rules that are off by default (colour contrast).
- `categories`?: [document \| page_content \| forms \| alternate_text \| tables \| lists \| headings]
- `pages`?: [integer] — 1-based page numbers for the page rules (default: all).
- `rules`?: [string]

### `accessibility_report`
Run the full check and write the accessibility report (HTML) to path; returns the results too. Takes the same options as accessibility_check.
- `all`?: boolean
- `categories`?: [string]
- `pages`?: [integer] — 1-based page numbers for the page rules (default: all).
- `path`: string
- `rules`?: [string]

### `accessibility_fix`
Apply the checker's automatic fix for a rule: primary-language (value: the language, e.g. en-US), title (value: the title; default the current title or file name; also shows it in the title bar) or tab-order (every page tabs in structure order). Returns the rule's new status. Undoable.
- `rule`: primary-language \| title \| tab-order
- `value`?: string

### `accessibility_figures` (read-only)
The tagged figures (Figure elements, through the role map) in document order: figure number, page, alternate text and where the figure is drawn (top-left-origin points).
- (no parameters besides `doc`)

### `accessibility_set_alt`
Set a figure's alternate text (alt; empty or omitted clears it), or mark it decorative (decorative: true: its content becomes an artifact and the figure leaves the tags). figure is a number from accessibility_figures. Returns the figures. Undoable.
- `alt`?: string
- `decorative`?: boolean
- `figure`: integer [min 1]

### `accessibility_autotag_preview` (read-only)
Propose paragraph and heading tags for visible text blocks on one page. Returns page bounds, tentative roles and reasons. Does not change the PDF or claim accessibility compliance. Images, tables, lists, annotations and existing structure require separate review.
- `page`: integer [min 1]

### `accessibility_tags` (read-only)
List reachable indirect structure tags in document order with PDF object number, generation, nearest indirect parent, depth, page, type, title, actual text, alternate text and language. Inline tag dictionaries have no stable object reference and are not listed.
- (no parameters besides `doc`)

### `accessibility_set_tag_property`
Set or clear one property of a reachable indirect structure tag. Use object and generation from accessibility_tags. Properties: type, title, actual_text, alternate_text, language. Empty or omitted value clears text properties; type requires a nonempty PDF name. Undoable.
- `generation`: integer [min 0, max 65535]
- `object`: integer [min 1]
- `property`: type \| title \| actual_text \| alternate_text \| language
- `value`?: string

### `accessibility_move_tag`
Move a reachable indirect structure tag before or after a direct sibling in their parent's /K array, changing tagged reading order without changing page appearance. Use object and generation values from accessibility_tags. Rejects distinct parents, duplicate references and positions that are already current. Undoable.
- `anchor`: integer [min 1]
- `anchor_generation`: integer [min 0, max 65535]
- `generation`: integer [min 0, max 65535]
- `object`: integer [min 1]
- `placement`: before \| after

### `accessibility_review_save`
Write a local JSON sidecar for an open PDF with rule-level human review decisions. The sidecar records the PDF SHA-256; replacing one tied to different bytes requires replace: true. Does not change the PDF or assert compliance.
- `decisions`: [{decision, note, page, rule}]
- `path`: string
- `replace`?: boolean

### `accessibility_review_load` (read-only)
Read a local review sidecar only when its recorded SHA-256 matches the open PDF. Returns the decisions without changing the PDF.
- `path`: string

### `accessibility_review_record`
Compare the same accessibility rules on two open versions of a PDF and write a JSON record to path. Includes document SHA-256 hashes, before/after rule statuses and finding counts, changed rules, and rules still needing review. Does not change either PDF or claim accessibility compliance. Open the original and edited copies as separate documents.
- `after`: integer [min 1] — Document id from doc_open or doc_list.
- `all`?: boolean — Include rules that are off by default (colour contrast).
- `before`: integer [min 1] — Document id from doc_open or doc_list.
- `path`: string

### `accessibility_review_html`
Compare two open versions of a PDF and write a self-contained HTML summary of the same evidence as accessibility_review_record: document hashes, outcome counts, rule changes, and rules still requiring review. Does not change either PDF or claim accessibility compliance.
- `after`: integer [min 1] — Document id from doc_open or doc_list.
- `all`?: boolean — Include rules that are off by default (colour contrast).
- `before`: integer [min 1] — Document id from doc_open or doc_list.
- `path`: string

### `pdfa_verify` (read-only)
Standards ▸ Verify PDF/A compliance: the PDF/A-2b or 3b rules the document breaks (ISO 19005 clause, message, page, whether Save as PDF/A can fix it), plus what it declares.
- `level`?: 2b \| 3b — Default 2b.

### `pdfa_convert`
Standards ▸ Save as PDF/A: fix what can be fixed for PDF/A-2b or 3b (XMP identification and metadata, an sRGB output intent, forbidden actions and JavaScript, annotation print flags, image interpolation, encryption). Returns what was fixed and what remains (e.g. fonts that aren't embedded). Undoable; save the document to keep it.
- `level`?: 2b \| 3b

## Measuring

### `measure_distance`
Add an undoable two-point distance annotation using the scale of the first point's viewport.
- `author`?: string
- `label`?: string
- `page`: integer [min 1]
- `points`: [[2 numbers]]

### `measure_perimeter`
Add an undoable connected-line length annotation. To include a closing edge, repeat the first point at the end.
- `author`?: string
- `label`?: string
- `page`: integer [min 1]
- `points`: [[2 numbers]]

### `measure_area`
Add an undoable area annotation from a simple polygon. The last edge closes automatically.
- `author`?: string
- `label`?: string
- `page`: integer [min 1]
- `points`: [[2 numbers]]

### `measure_info` (read-only)
Calculate a live distance, perimeter or area, deltas, angle and scale without adding an annotation. Incomplete paths are allowed.
- `page`: integer [min 1]
- `points`: [[2 numbers]]
- `type`?: distance \| perimeter \| area

### `measure_list` (read-only)
Saved measurement annotations with calculated values, scale and vertices in display coordinates. Measurements with unsupported imported formats (compound or fractional units, non-rectilinear scales) or invalid geometry are listed under unsupported with a reason.
- `page`?: integer [min 1]

### `measure_scale`
Read the scale at a point, or add a rectangular viewport using units_per_point or two calibration points and their real-world distance. Existing measurements retain their original scales. Undoable.
- `at`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `distance`?: number
- `name`?: string
- `page`: integer [min 1]
- `points`?: [[2 numbers]]
- `precision`?: integer [min 0, max 6]
- `rect`?: [4 numbers]
- `unit`?: string
- `units_per_point`?: number

### `measure_snap` (read-only)
Snap a point to vector paths, endpoints, midpoints or intersections. Coordinates and tolerance are in display points. Bounded extraction reports truncated geometry.
- `at`: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `endpoints`?: boolean
- `intersections`?: boolean
- `midpoints`?: boolean
- `page`: integer [min 1]
- `paths`?: boolean
- `tolerance`?: number [min 0, max 10000]

### `measure_export`
Atomically write saved measurement values, labels, authors and scale ratios as spreadsheet-safe CSV. Returns how many unsupported measurements were left out.
- `out`: string — A file path (relative to --root when set).

## Action Wizard (batch)

### `action_list` (read-only)
Action Wizard: the built-in actions (name, description, steps) and every step an action can use (id, label, whether it takes a text argument).
- (no parameters)

### `action_run`
Action Wizard: run a built-in action (action: its name) or a list of steps ([{step, arg}], ids from action_list) on each PDF in paths, writing the results into folder under the same names. Returns each file's step log or error.
- `action`?: string
- `folder`: string
- `paths`: [string]
- `steps`?: [{arg, step}]
