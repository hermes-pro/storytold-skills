# PdfCraft Action Wizard and app commands

Generated from `action_list` and `command_list` (PdfCraft 0.4.0).

## Built-in actions (`action_run {action: <name>, paths, folder}`)

- **Prepare for Distribution**: Remove hidden information and flatten comments and form fields, so recipients see only the pages. Steps: remove_hidden_information, flatten_comments, flatten_fields
- **Optimize Scanned Documents**: Make scans searchable, then make them smaller. Steps: recognize_text, reduce_file_size
- **Add Page Numbers**: Number every page in the footer. Steps: add_footer("Page <<1>> of <<n>>")
- **Mark as Confidential**: A diagonal CONFIDENTIAL watermark on every page. Steps: add_watermark("CONFIDENTIAL")
- **Sanitize Documents**: Remove hidden information, metadata, scripts and embedded content, and rewrite the files. Steps: sanitize

## Steps for custom actions (`action_run {steps: [{step, arg?}], paths, folder}`)

- `recognize_text`: Recognize text
- `reduce_file_size`: Reduce file size
- `remove_hidden_information`: Remove hidden information
- `sanitize`: Sanitize document
- `flatten_comments`: Flatten comments
- `flatten_fields`: Flatten form fields
- `add_watermark`: Add watermark (takes `arg`)
- `add_header`: Add header (takes `arg`)
- `add_footer`: Add footer (takes `arg`)
- `set_title`: Set document title (takes `arg`)
- `detect_form_fields`: Detect form fields
- `run_javascript`: Run a JavaScript (takes `arg`)

## App commands (178)

Ids for the live desktop app (`pdfcraft-cli ui --control FILE command id=<id>`). The `tool` column names the
MCP tool that does the same thing headlessly; prefer the tool.

| id | label | menu | shortcut | tool |
|---|---|---|---|---|
| `file.open` | Open… | File | Ctrl+O | `doc_open` |
| `create.blank` | New blank PDF | File |  |  |
| `measure.distance` | Measure distance |  |  | `measure_distance` |
| `measure.perimeter` | Measure perimeter |  |  | `measure_perimeter` |
| `measure.area` | Measure area |  |  | `measure_area` |
| `measure.scale` | Set measurement scale |  |  | `measure_scale` |
| `measure.info` | Measurement information |  |  | `measure_info` |
| `measure.snap` | Measurement snapping |  |  | `measure_snap` |
| `measure.export` | Export measurements as CSV |  |  | `measure_export` |
| `page.copy` | Copy pages |  |  |  |
| `page.cut` | Cut pages |  |  |  |
| `page.paste` | Paste pages |  |  |  |
| `create.file` | Create PDF from file… | File |  |  |
| `create.images` | Create PDF from images… | File |  |  |
| `create.clipboard` | Create PDF from clipboard | File |  |  |
| `page.combine` | Combine files… | File |  | `doc_combine` |
| `file.save` | Save | File | Ctrl+S | `doc_save` |
| `file.save_as` | Save as… | File | Ctrl+Shift+S |  |
| `file.close` | Close file | File | Ctrl+W | `doc_close` |
| `file.close_all` | Close all | File | Ctrl+Shift+W |  |
| `file.revert` | Revert | File |  |  |
| `print.dialog` | Print… | File | Ctrl+P |  |
| `file.properties` | Document properties… | File | Ctrl+D | `doc_info` |
| `edit.undo` | Undo | Edit | Ctrl+Z | `edit_undo` |
| `edit.redo` | Redo | Edit | Ctrl+Shift+Z | `edit_redo` |
| `edit.find` | Find… | Edit | Ctrl+F | `text_find` |
| `edit.advanced_search` | Advanced search… | Edit | Ctrl+Shift+F |  |
| `view.palette` | Find tools and commands… | View | Ctrl+K |  |
| `view.layout.continuous` | Continuous scrolling |  |  |  |
| `view.layout.single` | Single page |  |  |  |
| `view.layout.two_up` | Two-page view |  |  |  |
| `view.layout.cover` | Show cover page in two-page view |  |  |  |
| `view.fit_width_scrolling` | Fit to width scrolling |  |  |  |
| `view.fit_one_page` | Fit one full page |  |  |  |
| `view.fit_visible` | Fit visible | View | Ctrl+3 |  |
| `view.marquee_zoom` | Marquee zoom | View |  |  |
| `edit.snapshot` | Take a snapshot | Edit |  |  |
| `view.full_screen` | Full screen mode | View | Ctrl+L |  |
| `view.read_mode` | Read mode | View | Ctrl+H |  |
| `view.theme` | Switch light / dark theme |  |  |  |
| `view.theme.system` | Use system setting |  |  |  |
| `view.theme.light` | Light gray |  |  |  |
| `view.theme.dark` | Dark gray |  |  |  |
| `comment.list` | Comments panel | View |  |  |
| `comment.note` | Add a sticky note |  |  |  |
| `comment.freetext` | Add a text box |  |  |  |
| `comment.highlight` | Highlight text |  |  |  |
| `comment.underline` | Underline text |  |  |  |
| `comment.strikeout` | Strikethrough text |  |  |  |
| `comment.squiggly` | Squiggly underline text |  |  |  |
| `comment.ink` | Draw freehand |  |  |  |
| `comment.line` | Draw a line |  |  |  |
| `comment.arrow` | Draw an arrow |  |  |  |
| `comment.square` | Draw a rectangle |  |  |  |
| `comment.circle` | Draw an oval |  |  |  |
| `comment.polygon` | Draw a polygon |  |  |  |
| `comment.polyline` | Draw connected lines |  |  |  |
| `comment.cloud` | Draw a cloud |  |  |  |
| `comment.callout` | Add a callout |  |  |  |
| `comment.caret` | Insert text |  |  |  |
| `comment.replace` | Replace text |  |  |  |
| `comment.attach` | Attach a file |  |  |  |
| `comment.eraser` | Erase drawings |  |  |  |
| `form.fields` | Form fields panel | View |  |  |
| `form.clear` | Clear form | Edit |  |  |
| `comment.flatten` | Flatten comments |  |  |  |
| `comment.import` | Import comments… |  |  |  |
| `comment.stamp` | Add a stamp |  |  | `stamp_custom` |
| `comment.export` | Export all comments to data file… |  |  |  |
| `comment.hide_all` | Hide all comments |  |  | `comments_hide` |
| `comment.summarize` | Summarize comments |  |  | `comments_summarize` |
| `form.import_data` | Import form data… |  |  |  |
| `form.export_data` | Export form data… |  |  |  |
| `standards.pdfa` | PDF/A… |  |  | `pdfa_verify` |
| `actions.wizard` | Action Wizard… |  |  | `action_list` |
| `actions.distribution` | Prepare for distribution… |  |  |  |
| `actions.optimize_scans` | Optimize scanned documents… |  |  |  |
| `doc.compare` | Compare files… |  |  | `doc_compare` |
| `form.detect` | Detect form fields |  |  | `form_detect_fields` |
| `form.merge_data` | Merge data files into spreadsheet… |  |  | `form_merge_data` |
| `form.flatten` | Flatten form fields |  |  |  |
| `form.prepare` | Prepare a form |  |  | `form_set_script` |
| `form.tab_order.row` | Tab order: by rows |  |  |  |
| `form.tab_order.column` | Tab order: by columns |  |  |  |
| `form.tab_order.structure` | Tab order: by document structure |  |  |  |
| `edit.text` | Add text |  |  | `page_add_text` |
| `edit.edit_text` | Edit text & images |  |  | `text_lines` |
| `edit.link` | Add or edit links |  |  | `link_add` |
| `edit.links_from_urls` | Create links from URLs |  |  | `links_from_urls` |
| `edit.remove_links` | Remove all links |  |  | `links_remove` |
| `edit.bates` | Add Bates numbering… |  |  |  |
| `edit.image` | Add image… |  |  | `page_add_image` |
| `redact.mark` | Redact text and images |  |  |  |
| `redact.pages` | Redact pages… |  |  |  |
| `redact.search` | Find text and redact… |  |  |  |
| `redact.properties` | Redaction properties… |  |  |  |
| `redact.apply` | Apply redactions… |  |  |  |
| `redact.clear` | Clear redaction marks |  |  |  |
| `protect.remove_hidden` | Remove hidden information… |  |  |  |
| `redact.sanitize` | Sanitize document… |  |  |  |
| `form.field.properties` | Field properties… |  |  |  |
| `form.add.text` | Add a text field |  |  |  |
| `form.add.checkbox` | Add a checkbox |  |  |  |
| `form.add.radio` | Add a radio button |  |  |  |
| `form.add.combo` | Add a drop-down list |  |  |  |
| `form.add.list` | Add a list box |  |  |  |
| `form.add.button` | Add a button |  |  |  |
| `form.add.image` | Add an image field |  |  |  |
| `form.add.date` | Add a date field |  |  |  |
| `form.add.signature` | Add a digital signature field |  |  |  |
| `sign.digital` | Digitally sign |  |  | `sign_keychain_ids` |
| `sign.certify` | Certify (visible signature) |  |  |  |
| `sign.certify_invisible` | Certify (invisible signature) |  |  |  |
| `sign.validate` | Validate all signatures |  |  |  |
| `sign.panel` | Signatures panel | View |  |  |
| `sign.fill.text` | Fill & Sign: add text |  |  | `fill_sign_add` |
| `sign.fill.check` | Fill & Sign: checkmark |  |  |  |
| `sign.fill.cross` | Fill & Sign: cross |  |  |  |
| `sign.fill.dot` | Fill & Sign: dot |  |  |  |
| `sign.fill.line` | Fill & Sign: line |  |  |  |
| `sign.fill.date` | Fill & Sign: date |  |  |  |
| `sign.fill.signature` | Fill & Sign: sign |  |  |  |
| `sign.fill.initials` | Fill & Sign: initials |  |  |  |
| `sign.fill.signature.change` | Fill & Sign: change signature |  |  |  |
| `sign.fill.signature.remove` | Fill & Sign: remove saved signature |  |  |  |
| `sign.fill.initials.remove` | Fill & Sign: remove saved initials |  |  |  |
| `sign.fill.initials.change` | Fill & Sign: change initials |  |  |  |
| `export.image` | Export to image… | File |  | `doc_export_images` |
| `optimize.reduce` | Reduce file size… | File |  | `doc_reduce` |
| `optimize.advanced` | Optimize PDF… | File |  | `doc_audit_space` |
| `export.text` | Export to text… | File |  | `doc_export_text` |
| `export.docx` | Export to Word… | File |  | `doc_export_office` |
| `export.html` | Export to HTML… | File |  |  |
| `export.rtf` | Export to RTF… | File |  |  |
| `app.preferences` | Preferences… | Edit | Ctrl+, |  |
| `tools.js_console` | JavaScript console… |  | Ctrl+J | `js_run` |
| `tools.document_js` | Document JavaScripts… |  |  | `js_document_scripts` |
| `ocr.recognize` | Recognize text… |  |  | `ocr_recognize` |
| `ocr.recognize_batch` | Recognize text in multiple files… |  |  | `ocr_recognize_files` |
| `a11y.check` | Check for accessibility… |  |  | `accessibility_check` |
| `a11y.report` | Open accessibility report |  |  | `accessibility_report` |
| `a11y.reading_options` | Change reading options… |  |  |  |
| `a11y.alt_text` | Add alternate text… |  |  | `accessibility_figures` |
| `export.all_images` | Export all images… | File |  | `doc_export_all_images` |
| `edit.header_footer` | Add header & footer… |  |  | `doc_header_footer` |
| `edit.header_footer.update` | Update header & footer… |  |  |  |
| `edit.header_footer.remove` | Remove header & footer |  |  |  |
| `edit.watermark` | Add watermark… |  |  | `doc_watermark` |
| `edit.watermark.update` | Update watermark… |  |  |  |
| `edit.watermark.remove` | Remove watermark |  |  |  |
| `edit.background` | Add background… |  |  | `doc_background` |
| `edit.background.update` | Update background… |  |  |  |
| `edit.background.remove` | Remove background |  |  |  |
| `protect.password` | Protect using password… | File |  | `doc_protect` |
| `protect.remove` | Remove security | File |  | `doc_unprotect` |
| `protect.properties` | Security properties… | File |  |  |
| `page.organize` | Organize pages | Pages |  |  |
| `bookmark.add` | New bookmark | Pages | Ctrl+B |  |
| `page.rotate` | Rotate pages clockwise | Pages |  | `page_rotate` |
| `page.rotate_ccw` | Rotate pages counterclockwise | Pages |  |  |
| `page.delete` | Delete pages | Pages |  | `page_delete` |
| `page.insert_blank` | Insert blank page | Pages |  | `page_insert_blank` |
| `page.rotate_dialog` | Rotate pages… | Pages |  |  |
| `page.duplicate` | Duplicate pages | Pages |  | `page_duplicate` |
| `page.crop` | Crop pages | Pages |  |  |
| `page.boxes` | Set page boxes… | Pages |  | `page_set_box` |
| `page.insert` | Insert pages from file… | Pages |  | `page_insert_file` |
| `page.replace` | Replace pages… | Pages |  | `page_replace` |
| `page.extract` | Extract pages… | Pages |  | `page_extract` |
| `page.split` | Split document… | Pages |  | `doc_split` |
| `page.number` | Number pages… | Pages |  |  |
| `help.shortcuts` | Keyboard shortcuts | Help |  |  |
| `help.discord` | Join the ArtCraft Discord | Help |  |  |
| `help.app_page` | PdfCraft web page | Help |  |  |
| `help.github` | PdfCraft on GitHub | Help |  |  |
| `help.website` | ArtCraft website | Help |  |  |
| `help.check_updates` | Check for updates… | Help |  |  |
| `help.about` | About PdfCraft | Help |  |  |
