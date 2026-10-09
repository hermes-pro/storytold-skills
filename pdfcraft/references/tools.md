# PdfCraft MCP tools

Generated from the live `pdfcraft-cli mcp` server (PdfCraft 0.4.0, 131 tools). Hermes names them
`mcp_pdfcraft_<tool>`. The same names work in `pdfcraft-cli run <tool> key=value` and `run --script`.
Almost every tool takes `doc` (the id from `doc_open` / `doc_create`); it is left out of the lists below.
Grep for a tool name or a keyword; don't read the whole file. `?` = optional, `a | b` = choices, (=x) = default.
Coordinates are points with the origin at the top-left of the displayed page, y down, unless a tool says bottom-left.

## Documents: open, create, save, metadata, history

### `doc_open`
Open a PDF file and return its document id, page count and whether it can be edited.
- `password`?: string — User or owner password for encrypted files.
- `path`: string

### `doc_create`
Create a new, unsaved document and return it like doc_open: `blank` (pages, width, height in points; default 1 US Letter page), `images` (paths of PNG, JPEG, TIFF (every page), GIF or BMP files, one page each at the image's resolution) or `text` (a .txt path, or `text` directly). Save it with doc_save and a path.
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
Save to its own file (an incremental update, which keeps signatures valid) or to a new path (a full rewrite). The write is atomic.
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

### `command_list` (read-only)
Every registered PdfCraft command with its menu, shortcut, whether it is enabled now, and the tool that automates it.
- (no parameters besides `doc`)

## Reading: render, text, find

### `page_render` (read-only)
Render one page to a PNG image (default 96 dpi, at most 600).
- `dpi`?: number [min 1, max 600]
- `page`: integer [min 1]

### `text_extract` (read-only)
Extract the text of some or all pages, in reading order.
- `pages`?: [integer] — 1-based page numbers to extract (default: all).

### `text_find` (read-only)
Find a phrase (case-insensitive, whitespace-normalised) and return each match with its page and line rectangles in points (origin top-left).
- `limit`?: integer [min 1] — Maximum matches (default 500).
- `query`: string

### `text_lines` (read-only)
The lines of existing text on a page (Edit a PDF ▸ Edit text): number, text, box (top-left-origin points), font and size. Use the number with text_edit.
- `page`: integer [min 1]

### `text_paragraphs` (read-only)
The paragraphs on a page (lines grouped by font, size, alignment and spacing): number, text, its line numbers, box (top-left-origin points), font and size. Use the number with text_edit's paragraph.
- `page`: integer [min 1]

### `page_images` (read-only)
The images a page draws (Edit a PDF): number, box (top-left-origin points), pixel size and resource name.
- `page`: integer [min 1]

### `image_save`
Write one of a page's images to path: JPEG images unchanged, others as PNG (the extension is added when missing).
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
Combine PDFs, in order, into one (bookmarks are kept under one entry per file). pages optionally chooses each file's pages, in step with paths: a range such as "1-3, 6" or null for all pages.
- `open`?: boolean — Also open the result as a new document (default: only when out is omitted).
- `out`?: string — File to write. Omit to open the result as a new unsaved document instead.
- `pages`?: [string/null]
- `paths`: [string]

### `doc_split`
Split into several files written to out_dir: every N pages, before given pages, at top-level bookmarks (bookmarks: true; files named after them), or by file size (max_mb). Files are <name>-partK.pdf.
- `before`?: [integer] — 1-based page numbers that start a new part.
- `bookmarks`?: boolean
- `every`?: integer [min 1]
- `max_mb`?: number
- `out_dir`: string

## Editing page content

### `page_add_text`
Add text as page content (not a comment). Place it with at [x, y] (top-left, points from the top-left of the displayed page) and width (wrap width, default 200), or rect. Newlines start new lines; long lines wrap. Style: font helvetica/times/courier, size, bold, italic, color (#RRGGBB or a name), align left/center/right. It stays editable with content_update. Undoable.
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

### `text_edit`
Replace the text of one paragraph (paragraph, from text_paragraphs: rewrapped to the paragraph's width with its line spacing) or one line (line, from text_lines) in place, keeping position, size and colour. For a paragraph, also change its formatting: font (helvetica, times, courier) with bold/italic, size (points), color (#rrggbb), align (left, center, right, justify), underline, line_spacing (× size), char_spacing (points) and scale (horizontal, percent), or move it (dx, dy in points; up is +dy) and rewrap it to a new width (points); text may then be omitted. Its own font is reused when it can show every character; otherwise the line is set in Helvetica (the result shows the font used). Text that no available font can show is refused. Undoable.
- `align`?: left \| center \| right \| justify
- `bold`?: boolean
- `char_spacing`?: number — Points.
- `color`?: string — #rrggbb
- `dx`?: number — Paragraph only: move right by this many points (negative: left).
- `dy`?: number — Paragraph only: move up by this many points (negative: down).
- `font`?: helvetica \| times \| courier
- `italic`?: boolean
- `line`?: integer [min 1]
- `line_spacing`?: number — Multiple of the font size (1.2 is ordinary).
- `page`: integer [min 1]
- `paragraph`?: integer [min 1]
- `scale`?: number — Horizontal scale in percent.
- `size`?: number
- `text`?: string
- `underline`?: boolean
- `width`?: number — Paragraph only: rewrap to this width in points (dragging the box's edge).

### `image_edit`
Change one of a page's images (number from page_images): action move (rect: new box in top-left-origin points), rotate (quarters clockwise, default 1), flip_horizontal, flip_vertical, replace (path: an image file, drawn in the same place) or delete. Undoable.
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
Add a watermark to pages: text, or a picture from `file` (an image, or page `file_page` of a PDF) at `scale` of the page (default 0.5); rotated (degrees counter-clockwise, default 45), semi-transparent (opacity 0–1, default 0.5), text fitted to the page unless font_size is given, on top unless behind: true. replace: true swaps out existing ones. Undoable.
- `behind`?: boolean
- `color`?: string
- `file`?: string
- `file_page`?: integer [min 1]
- `font_size`?: number
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
The bookmark tree with each bookmark's path, title, target page and open state.
- (no parameters besides `doc`)

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
Remove every link in the document. Undoable.
- (no parameters besides `doc`)

## Comments and review

### `comment_list` (read-only)
Every comment (annotation other than links, form widgets and pop-ups) with its page, index, id, type, author, text, date, rectangle, colour, review status and replies.
- `page`?: integer [min 1] — Only this page.

### `comment_add`
Add a comment as Acrobat's commenting tools do. Geometry is in points with the origin at the top-left of the displayed page, y down (as in page_render images at 72 dpi and text_find rects). note: `at` [x, y] (icon top-left). stamp: `at` [x, y] (its centre) and `stamp`: approved, completed, confidential, draft, final, for comment, for public release, information only, not approved, not for public release, preliminary results, void, accepted, initial here, rejected, sign here, witness; dynamic: true for the dynamic approved/confidential/received/reviewed/revised stamps with a By … at … line. highlight/underline/strikeout/squiggly: `find` (text on the page to mark; every match with all: true) or `quads`. rectangle/oval/textbox: `rect` [x0, y0, x1, y1]. line/arrow: `from`, `to`. ink: `strokes` [[[x, y], …], …]. polygon/cloud/polyline (connected lines): `points` [[x, y], …]. callout: `rect` (its text box), `to` (the point the arrow touches), optional `knee`. caret (inserted text): `at`, the insertion point on the baseline. replace (Replace Text): `find` or `quads` like highlight, `contents` the replacement. attachment: `path` (the file), `at`, optional `icon` (PushPin, Paperclip, Graph, Tag). Undoable.
- `all`?: boolean — Mark every match of `find` on the page, not just the first.
- `at`?: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `author`?: string
- `color`?: string — #RRGGBB or a name: yellow, red, orange, green, blue, purple, pink, black, gray, white.
- `contents`?: string — The comment text (what a text box shows).
- `dynamic`?: boolean
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
Change a comment's text, colour, opacity, line width, rectangle (rectangle/oval/text box) or position (`move` [dx, dy] in points). One undo step.
- `color`?: string — #RRGGBB or a name: yellow, red, orange, green, blue, purple, pink, black, gray, white.
- `contents`?: string
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

### `stamp_custom`
Stamp a picture: a PDF page (file_page, default 1) or an image file, centred at at [x, y] (points from the top-left of the displayed page) at its natural size, at most 200 pt. name labels it (default: the file name). Undoable.
- `at`: [2 numbers]
- `author`?: string
- `file_page`?: integer [min 1]
- `name`?: string
- `page`: integer [min 1]
- `path`: string

### `fill_sign_add`
Fill in a form that has no fields, as Acrobat's Fill & Sign does: type text (`text`, 10 pt), place a check, cross, dot or line, today's date, or a typed signature or initials (`text` drawn in a script font as filled outlines; at is its left edge, centred vertically), at `at` [x, y] in points from the top-left of the page (the text's top-left; a mark's centre). Creates movable, undoable annotations.
- `at`: [2 numbers] — [x, y] in points from the top-left of the displayed page.
- `author`?: string
- `page`: integer [min 1]
- `text`?: string
- `type`: text \| check \| cross \| dot \| line \| date \| signature \| initials

### `doc_flatten`
Merge comment and/or form field appearances into the page content, so they print and display everywhere but can no longer be edited. Undoable until saved.
- `comments`?: boolean — Default true.
- `fields`?: boolean — Default true.

## Forms

### `form_fields` (read-only)
Every interactive form field: name, type (text, checkbox, radio, combo, list, button, signature), value, options, page and rect (top-left-origin points), read-only and required flags.
- (no parameters besides `doc`)

### `form_fill`
Set several fields at once (one undo step). values maps field names (from form_fields) to: a string for text fields, combo boxes and radio groups (an option), true/false for check boxes, an array of strings for multi-select lists. Appearances are regenerated so every viewer shows the values.
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
Change a field's properties (General and Options tabs): name (renames it), tooltip, read_only, required, multiline, max_length (0 = no limit), options (combo/list items), font_size (0 = auto), rect (position), format, validate, calculate (Acrobat's Format/Validate/Calculate tabs, run natively: values are checked, formatted and recalculated as in Acrobat). Options tab: align (left, center, right), default (the value Reset form restores; for check boxes and radio buttons their on state, "" for off), flags { scroll, rich_text, password, file_select, spell_check, comb (needs max_length), sort, editable, multi_select, commit_immediately }, check_style (check boxes and radio buttons: check, circle, cross, diamond, square, star). Only the given ones change. Undoable.
- `align`?: left \| center \| right
- `appearance`?: object — Appearance tab: border, fill, text_color (#RRGGBB, a name or "none"), width (1 thin, 2 medium, 3 thick), style (solid, dashed, beveled, inset, underline), font (helvetica, times, courier).
- `calculate`?: any — Calculate tab: {"op": "sum"|"product"|"average"|"min"|"max", "fields": ["a", "b"]}, {"notation": "Price * Qty"} (simplified field notation), or "none".
- `check_style`?: check \| circle \| cross \| diamond \| square \| star — Check boxes and radio buttons: the mark shown when on.
- `default`?: string
- `field`: string — The field's current name.
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
- `tooltip`?: string
- `validate`?: any — Validate tab: {"min": 0, "max": 100} (either may be left out) or "none".

### `form_set_image`
Show an image file (PNG, JPEG, TIFF, GIF or BMP) in an image field or button, scaled to fit and centred (what clicking an image field does). Undoable.
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
Write comments and/or form data to path; the extension picks the format: .xfdf or .fdf (comments and/or fields), .xml, .csv or .txt (form data). what: all (default), comments, fields.
- `path`: string
- `what`?: all \| comments \| fields

### `doc_import_data`
Import comments and/or field values from an XFDF, FDF, XML, CSV or tab-delimited text file (detected from its content). Comments with the same name are replaced; values go through the form's formats and validation. Undoable.
- `path`: string

## JavaScript

### `js_run`
Run Acrobat JavaScript in the document, as the JavaScript console does (or as push button `field`'s Mouse Up script when field is given; on a laid-out XFA form, `field` runs that button's XFA click script instead, which can add and remove rows and show or hide subforms). The form object model is available: this/getField, event, app, util, console, display, color, and the document-level scripts. Field changes and resetForm are applied as one undoable step; returns the script's alerts, console output, requests (print, page, url, submit) and error.
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
Mark content for redaction (nothing is removed until redact_apply). One of: rect [x0, y0, x1, y1] (points from the top-left of the displayed page) with page; find (text, every match); pattern (phone, email, credit-card, ssn, date: every match, Acrobat's Search & Redact patterns); whole_pages: true. find, pattern and whole_pages work on pages (default all). overlay: text shown on the box once applied; fill: box colour (default black). Undoable.
- `author`?: string
- `fill`?: string — #RRGGBB or a colour name.
- `find`?: string
- `overlay`?: string
- `page`?: integer [min 1]
- `pages`?: [integer] — 1-based page numbers to search or mark (default: all).
- `pattern`?: phone \| email \| credit-card \| ssn \| date
- `rect`?: [4 numbers]
- `whole_pages`?: boolean

### `redact_apply`
Apply the redaction marks (all, or those on pages): text, images, vectors, comments and form fields under them are removed for good and boxes are drawn in their place. A verification pass fails the operation if anything readable remains. Undoable until saved; the saved file no longer contains the content.
- `pages`?: [integer] — 1-based page numbers whose marks to apply (default: all).

### `redact_clear`
Remove every redaction mark without applying it. Undoable.
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

### `sign_document`
Sign with a digital ID (a .p12/.pfx path, or on macOS a Keychain identity: "keychain:<common name or fingerprint>" from sign_keychain_ids) and save the signed file to `out` (signing always saves, as in Acrobat; the document then shows the signed file). Sign an existing empty signature field (`field`), or a new one on `page` at `rect` (omit rect for an invisible signature). certify: no_changes, form_fill or comments makes a certification signature. PAdES B-B, SHA-256 (SHA-384 for P-384 keys).
- `certify`?: no_changes \| form_fill \| comments
- `contact`?: string
- `field`?: string
- `id`: string — Path of the digital ID (.p12 / .pfx).
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
Write pages as PNG, JPEG or TIFF files (`<name>_page_<n>.png|jpg|tif`) into a folder, at a resolution (default 150 dpi). JPEG and TIFF are flattened onto white paper. Includes unsaved edits.
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
Export a PDF ▸ Word (.docx), HTML (.html, one file with images inline) or RTF (.rtf), chosen by path's extension: paragraphs in reading order, headings from larger text, bold and italic, images where they fall, a page break between pages.
- `path`: string

### `doc_reduce`
Write a smaller copy of the document to `path` with Acrobat's Reduce File Size choices: images above 225 ppi downsampled to 150 ppi and JPEG-compressed (medium quality), thumbnails dropped, identical fonts and images merged, unused objects dropped, compressed object streams. The open document is unchanged.
- `path`: string

### `doc_optimize`
Write an optimized copy to `path` (Acrobat's PDF Optimizer). color / gray: { downsample, ppi, above_ppi, compression: jpeg|zip|retain, quality 1–100 } (defaults: downsample to 150 ppi above 225, JPEG 60). Images are measured where pages draw them and replaced only when smaller. discard_*: thumbnails (default true), alternate_images (true), tags, print_settings; flate_unencoded (true); remove_invalid_links and remove_unreferenced_dests (true). discard: Remove Hidden Information categories (metadata, attachments, comments, form-fields, hidden-text, hidden-layers, bookmarks, links-actions-scripts, private-data). Signed documents are refused. The open document is unchanged.
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
Print with Acrobat's Print dialog options, or save the print-ready PDF. pages: a range such as "1-3, 6, 9-" (page labels allowed; default all); subset odd/even; reverse. layout: fit (default), actual, shrink, custom (scale %), multiple (per_sheet 2/4/6/9/16, order, border, auto_rotate; cut-stack order arranges single-sided sheets for cutting into piles and stacking left to right, top to bottom, keeping sheet order within each pile; duplex must be off), booklet (booklet_subset both/front/back, binding left/right), poster (scale %, overlap pt, cut_marks). orientation auto/portrait/landscape; comments_forms document / document-and-markups (default) / document-and-stamps / form-fields-only; paper Letter/Legal/Tabloid/A3/A4/A5. Then path (save) or printer (a name or "default") with copies, collate, duplex off/long-edge/short-edge, grayscale.
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

## OCR

### `ocr_status` (read-only)
Whether text recognition is available (its models are installed: run `cargo xtask models` or set PDFCRAFT_MODELS), where it looks for them, and the languages it reads.
- (no parameters)

### `ocr_recognize`
Scan & OCR ▸ Recognize text: render pages, read the words in them and add them as invisible text over the page image, so scanned pages become searchable and selectable (a searchable image; the image is not changed). Pages that already have text are skipped unless skip_text_pages is false. Returns each page's recognised text, word count or why it was skipped. Needs the OCR models (ocr_status). Undoable as one step.
- `dpi`?: number [min 72, max 600] — Resolution pages are read at (default 300; a scanned page is read at most at its own resolution).
- `language`?: en — Document language (default en).
- `pages`?: [integer] — 1-based page numbers to recognise (default: all).
- `skip_text_pages`?: boolean — Leave pages that already contain text alone (default true).

### `ocr_recognize_files`
Scan & OCR ▸ Recognize text ▸ In multiple files: read every page of each PDF in paths and write the searchable result into folder under the same name (pages that already have text are left alone). Returns, per file, the output path, word count and skipped pages, or the error.
- `dpi`?: number [min 72, max 600]
- `folder`: string
- `language`?: en
- `paths`: [string]

## Accessibility and PDF/A

### `accessibility_check` (read-only)
Run the Accessibility Checker's full check (32 rules in 7 categories: document, page_content, forms, alternate_text, tables, lists, headings). Each rule is passed, failed (with findings and pages), manual (needs a person) or skipped. Colour contrast is off unless all is true; rules (ids such as tagged-pdf, figures-alt-text) or categories narrow the check; pages limit the page rules.
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
