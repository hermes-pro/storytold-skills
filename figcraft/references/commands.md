# FigCraft command catalog

Generated from `figcraft-cli commands --json` (FigCraft 0.6.0, 552 commands). Run one with
`run_command {command, params}` or several as one undo step with `batch {commands: [...]}`; check one live with
`list_commands {filter}` or read `figcraft://command/<id>`. `?` = optional, `a|b` = choices, `→ {...}` = what it
returns. `*` = undoable (changes the document). Most commands take `ids?` and act on the selection without it.
Coordinates are page units (px), y down, x/y relative to the parent frame. `node.set` keys are in
`node-properties.md`. Grep this file rather than reading it whole.

Groups: align (6), annotation (8), app (2), arrange (8), bool (5), branch (7), codeConnect (4), collab (20), command (1), comment (14), component (21), dev (4), devResource (4), distribute (2), doc (5), edit (15), effect (4), export (3), file (20), fill (5), frame (3), grid (3), guide (5), help (4), image (5), inspect (5), instance (8), layers (1), layout (4), libraries (2), library (18), measure (2), node (5), object (27), page (8), paint (1), plugin (11), plugins (2), pref (10), proto (20), section (1), select (21), shape (6), shapeBuilder (4), stroke (6), style (10), template (1), text (52), tool (21), transform (9), variable (18), vector (40), version (8), view (48), widget (3), window (2)

## align

- `align.left`* (Arrange › Align left, Alt+A): {ids?}
- `align.hcenter`* (Arrange › Align horizontal centers, Alt+H): {ids?}
- `align.right`* (Arrange › Align right, Alt+D): {ids?}
- `align.top`* (Arrange › Align top, Alt+W): {ids?}
- `align.vcenter`* (Arrange › Align vertical centers, Alt+V): {ids?}
- `align.bottom`* (Arrange › Align bottom, Alt+S): {ids?}

## annotation

- `annotation.add`* (Add annotation): {id? (default the first selected layer), label? (the note), properties?: [width|height|top|left|rotation|opacity|cornerRadius|direction|gap|padding|alignment|fontFamily|fontStyle|fontSize|lineHeight|letterSpacing|textAlign|fill|stroke|strokeWeight|effects], category? (id or name)} → {id, index} (a note, pinned properties or both)
- `annotation.edit`* (Edit annotation): {id?, index, label?, properties?: [..] (replaces the pinned properties), category? (id or name; null: none)}
- `annotation.remove`* (Remove annotation): {id?, index? (omit: every annotation on the layer)}
- `annotation.list` (List annotations): {ids? | id? (those layers), page? (page id, or "all"; default the current page), category? (id or name, or "none": only those)} → {annotations: [{id, name, index, label, category?: {id, name, color}, properties: [{property, label, value (null when the layer has none), token?, color?}]}]}
- `annotation.categories` (Annotation categories): {} → {categories: [{id, name, color, count (annotations in it, every page)}]}
- `annotation.addCategory`* (Add annotation category): {name, color? (default the first unused colour)} → {id}
- `annotation.editCategory`* (Edit annotation category): {id (id or name), name?, color?} (rename and/or recolour)
- `annotation.removeCategory`* (Delete annotation category): {id (id or name)} → {id, uncategorized (how many annotations were in it)} (its annotations stay, without a category)

## app

- `app.preferences` (Preferences › Preferences, Cmd+,): {}
- `app.actions` (Tools › Actions, Cmd+K): {}

## arrange

- `arrange.tidy`* (Arrange › Tidy up, Ctrl+Alt+Shift+T): {ids?, spacing?}
- `arrange.packH`* (Arrange › Pack horizontal): {ids?}
- `arrange.packV`* (Arrange › Pack vertical): {ids?}
- `arrange.roundToPixels`* (Arrange › Round to pixels): {ids?}
- `arrange.front`* (Object › Bring to front, Shift+Cmd+]): {ids?}
- `arrange.forward`* (Object › Bring forward, Cmd+]): {ids?}
- `arrange.backward`* (Object › Send backward, Cmd+[): {ids?}
- `arrange.back`* (Object › Send to back, Shift+Cmd+[): {ids?}

## bool

- `bool.union`* (Object › Boolean groups › Union selection, Alt+Shift+U): {ids?} — layers inside boolean groups: sets their own operation (how each combines with the operands below it); one boolean group: sets its operation (every operand follows it); otherwise wraps the layers in a new boolean group
- `bool.subtract`* (Object › Boolean groups › Subtract selection, Alt+Shift+S): {ids?} — layers inside boolean groups: sets their own operation (how each combines with the operands below it); one boolean group: sets its operation (every operand follows it); otherwise wraps the layers in a new boolean group
- `bool.intersect`* (Object › Boolean groups › Intersect selection, Alt+Shift+I): {ids?} — layers inside boolean groups: sets their own operation (how each combines with the operands below it); one boolean group: sets its operation (every operand follows it); otherwise wraps the layers in a new boolean group
- `bool.exclude`* (Object › Boolean groups › Exclude selection, Alt+Shift+E): {ids?} — layers inside boolean groups: sets their own operation (how each combines with the operands below it); one boolean group: sets its operation (every operand follows it); otherwise wraps the layers in a new boolean group
- `bool.flatten`* (Object › Boolean groups › Flatten boolean): {ids?}

## branch

- `branch.create` (File › Create branch): {name?} a copy of the file to work on separately, opened in a new tab; it remembers the file as it is now (its base) → {id, name, index (its tab)}
- `branch.list` (List branches): {} the branches of the file shown (or of the file a branch tab belongs to), oldest first → [{id, name, time (Unix seconds), state: active|merged|archived, index? (its open tab)}]
- `branch.open` (Open branch): {id} open the branch in a tab (or switch to its tab) → {index}
- `branch.review` (Review branch): {id? (default: the branch tab shown)} what changed on the branch and on the main file since the branch was made or last updated from main, and where they conflict (the same property changed on both sides, or a layer deleted on one side and edited on the other) → {id, name, state, branch: {layers, document, truncated}, main: {…}, conflicts: [{key, id?, name, property, branch, main, deletedBy?}]}
- `branch.updateFromMain` (Update from main): {id?, resolutions? ({<conflict key>: "branch" | "main"})} bring the main file's changes since the branch was made into the branch; refused while a conflict has no resolution. Not undoable (the branch tab's undo history starts over) → {updated, changes, conflicts}
- `branch.merge` (Merge branch): {id?, resolutions? ({<conflict key>: "branch" | "main"})} merge the branch into the main file as one undo step, then archive it and show the main file; refused while a conflict has no resolution → {merged, changes, conflicts, index}
- `branch.archive` (Archive branch): {id?} set the branch aside without merging (it stays in the file and can still be opened) and close its tab

## codeConnect

- `codeConnect.set`* (Connect to code): {id? (component, set or instance; default the selection), language?: react|leptos|swiftui|compose (default react), importPath?, name? (default the generated name), template? (default a call passing every property)} links the component (its set, for a variant) to its code component; fields left out keep their current value. Placeholders: {property} (its name or parameter name) and {property ? "a" : "b"}; other {…} stay as written → {component, language, code (the snippet for the layer), unknown (placeholder names that aren't properties)}
- `codeConnect.remove`* (Disconnect from code): {id? (component, set or instance; default the selection), language? (omit: every language)} → {component, removed}
- `codeConnect.export` (Export code connections): {path? (write it there, e.g. figcraft.connect.json in the code repository)} every component's links as {version: 1, links: [{component (its name), language, importPath, name, template}]}, sorted → {text, links} or {path, links}
- `codeConnect.import`* (Import code connections): {json (the connect JSON as codeConnect.export writes it: an object or JSON text) | path (a figcraft.connect.json)} links each entry to every component or set of that name (replacing its link for the language); invalid entries and unknown components are skipped with a warning → {linked, warnings}

## collab

- `collab.diff` (Show sync changes): {against? (undo: the last undoable action, the default | saved: since the last save)} → the changes a live session would send, their count and binary size
- `collab.host` (Start live session): {port? (default 47900, else any free port), bind?: "local" (this machine, default) | "lan" (the local network) | an IP address} → the open file's session: {session, link, url (invites: they carry the secret token), address, …}; sessions are per file, so other files' sessions go on (a session this file was in ends)
- `collab.share` (Share with a join code): {via?: "online" (default: the open file is kept on the server in Preferences, `pref.publishServer`, and the server hands out the codes) | "local" (this app hosts it for people on the same network; no server), access?: "edit" (default) | "view" (online only: which code `code` is), server? (online: another server's address, with ?key=… when it needs its key), name? (online: the file's name there), port?, bind?: "lan" (default) | "local" (this machine only) | an IP address (local)} → the open file's session as `collab.peers` gives it: `code` is what others type to join (`collab.join {code}`, the Join field), `link` an invite link. Local: at once, the code carries the host's IPv4 address, port and secret (K7M2Q-…, 20 symbols). Online: status "connecting" first; once live `code` is the server's (K7M-2QX-9TD) and `share` is {via, access, shared, editCode, viewCode, editLink, viewLink}: links made for others (the file's own links in `published` stay yours); `code` stays null when the server is older than join codes (give `share.editLink` / `share.viewLink` instead). Called again while shared: only switches which code `code` is (`access`). Called after `collab.stop` on a file that is still on the server: new links and codes for that same file (nothing is published twice). `collab.stop` stops sharing
- `collab.stop` (Stop live session): {} → {ended}: the open file's session ends (a session this app hosts stops for everyone; a joined one is left). A file shared online with `collab.share` is different: its sharing stops → {ended: false, shared: false}: the links and codes others got are revoked on the server, whoever joined with them is disconnected at once (they keep their copy), and you stay in the file, which stays on the server, open only to you (`collab.share` shares it again with new codes; `collab.leave` leaves it there; `collab.manageFile {action: "remove"}` with its owner token takes it off the server)
- `collab.join` (File › Join live session): {code: a join code (K7M-2QX-9TD from a server, asked at the server in Preferences; a longer one for the local network; spaces, dashes and case don't matter, O reads as 0 and I or L as 1) | link: figcraft://join?host=…&file=…&token=…, figcraft://join?server=ws(s)://…&file=…&token=… or ws(s)://host:port/?file=…&token=… (a session an app hosts, or a server's share link; a code here works too)} → the new session: {session, status: "connecting", …}; its file opens in a tab of its own (other files' sessions go on) and `collab.peers` tells when it's live (`sessions` lists it until then, and if it fails)
- `collab.leave` (Leave live session): {} (the open file's session; the synced file stays open as a local copy) → {ended}
- `collab.publish` (File › Publish to server): {server: ws://host:port/?key=… or wss://host/path/?key=… (the server's address with its key; `figcraft-server key` prints it; without a key on a server open to the public), key? (when the address has none), name? (default: the file's name)} → status "connecting": the open file is uploaded as a new file and this tab syncs through the server; `collab.peers` then has `published: {server, file, name, edit, view, owner (published without a key: the owner token, shown once), expires (seconds since 1970, or null)}` and `hosting` (the server's operator, terms and idle expiry)
- `collab.serverInfo` (Server info): {server: ws://host:port/ or wss://host/path/} → {open (anyone may publish without the key), operator, terms (a web address), idleDays (files published without the key are deleted after this many days unopened; null: kept), maxFileMb, expires}
- `collab.manageFile` (Manage published file): {file (its id), server?, owner? (the server's address and the owner token you got when you published the file without the key; each defaults to what is recorded for one of your online files, see `collab.files`), action: links | createLink {access?: view (default) | edit, label?} | revoke {link (a link's id)} | share (others get new links and join codes) | unshare (the links and codes others got are revoked; the file stays yours on the server) | rename {name} | remove (the file is deleted from the server and leaves your online files)} → {links: [{id, access, label, created}]} | {id, access, link (a new share link, shown once)} | {shared, code, viewCode, editLink, viewLink} | {done}
- `collab.report` (Report file to server operator): {reason (a few words, at most 500 characters)} → {sent}: the file you joined on a server is reported to its operator; the session's message says when the server kept it (servers older than this app don't take reports)
- `collab.peers` (People in this file): {} → the open file's session (each open file has its own or none): {available, canHost (false in the browser: it can only join), session (its id; null: this file isn't in a session), status: off|connecting|live|reconnecting|failed, reason?, role, me, name, color, fileName, pages, link, url, address, network, access: edit|view (view: a server's view link; edits are refused), readOnly (the open file can't be edited now: view only, or being published), published (a file you published: {server, file, name, edit, view}), code (the join code to give others, when the file was shared with `collab.share`; null otherwise or while it is on its way), share ({via: online|local, access, shared (false: a file of yours on a server that nobody else gets into now), editCode, viewCode, editLink, viewLink (what others join with; null when not shared)} or null), follow, syncing, document (index of the synced open document), editing (the text layer you type in: {node, layer, caret, selection}), peers: [{id, name, color, editing (theirs, same shape, or null), presence: {cursor: [page, x, y], selection, viewport: [page, x, y, w, h], editing_text}}], sessions: [{session, document (index of its open document; null for a join on its way), status, reason, role, fileName, link, peers (how many others)}] (every session of the app)}
- `collab.follow` (Follow): {client? (a peer's id; omit to stop following)} → {follow}
- `collab.cursor` (Show cursor at): {x?, y? (page coordinates on the current page; omit both to hide)} → {cursor} (agents; in the app the pointer drives it): your pointer in the open file's session (null when the file isn't in one)
- `collab.cursorChat` (Cursor chat, /): {text? (shown next to your cursor for everyone, at most 100 characters; empty closes it; omit to open the chat box in the app)} → {chat} (or {open}); others see it fade after 5 s without changes
- `collab.spotlight` (Spotlight me): {on? (default: toggle)} → {spotlighting}: everyone in the session follows your view and page until they move theirs
- `collab.files` (Your online files): {refresh? (true: ask each server once what became of its files; default false: no network)} → {files: [{server, host, file (its id), name, created, opened (seconds since 1970), shared (others get in with a code now), code, viewCode (the join codes, while shared), state: unknown | online | gone (the server no longer has it: removed or expired), expires, session, document (the session and open document it is in now, or null), hasOwnerToken: true}], problems: [{server, host, state: offline | unsupported (a server older than this request), reason}], max}: the files you published or shared without a server key, most recently opened first, as recorded on this computer with the preferences. Owner tokens and your own links are never in the result
- `collab.openFile` (Open online file): {file (its id, from `collab.files`), server? (when files on several servers have that id)} → {session, status: "connecting", document, alreadyOpen, file, server, name}: joins the file as its owner in a tab of its own (`collab.peers` tells when it's live; `collab.share` and `collab.stop` there start and stop its sharing); a file that is open already comes to the front instead (alreadyOpen: true)
- `collab.forgetFile` (Forget online file): {file, server?} → {forgotten, file, server, onServer}: drops the file from the list on this computer only. The file stays on its server until it expires, and without its owner token it can't be managed from here again (`collab.manageFile {action: "remove"}` takes it off the server instead)
- `collab.recoverFile` (Recover online file): {path (a recovery copy of one of your online files), file, server?, session, client, seq (who the app was in the file when the copy was written, and the server's last change it had: from the note beside the copy)} → {session, status: "connecting"}: joins the file again as its owner and keeps the copy until the file arrives. Then: the server has everything in the copy → nothing more; the copy has changes of yours the server never confirmed and nothing else changed there → they are applied on top as one edit ("Recovered changes", synced to everyone); anything else changed meanwhile → the copy opens beside the file as “<name> (recovered copy)”; the file can't be joined → the copy opens as an unsaved document. The session's message says which
- `collab.registerLinks` (Open invite links in FigCraft): {on? (default: switch)} → {on, registered}: make this app the opener of figcraft:// invite links (or stop); also the Preferences checkbox

## command

- `command.batch` (Run several commands): {label?, commands: [{command, params}]} (one undo step)

## comment

- `comment.add`* (Add comment): {x, y, text, page?, author?, anchor? (node id to pin to; true = innermost frame under the point)}
- `comment.reply`* (Reply to comment): {id, text, author?}
- `comment.edit`* (Edit comment): {id, text, reply? (index; omit for the first message), author?}
- `comment.react`* (React to comment): {id, emoji, reply? (index; omit for the first message), on? (default: toggle), author?}
- `comment.resolve`* (Resolve comment): {id, resolved? (default true)}
- `comment.move`* (Move comment): {id, x, y, anchor? (default true: pin to the innermost frame under the point; false: to the page; or a node id)}
- `comment.delete`* (Delete comment): {id, reply? (index: delete one reply; omit to delete the thread), author?}
- `comment.markRead` (Mark comment as read): {id? | link? (omit: every thread), read? (default true; false marks it unread), author?}
- `comment.open` (Open comment): {id | link, view? (fit: zoom to the thread's frame, default; center: centre the pin; keep), author?}
- `comment.next` (Next comment): {id? (the thread to step from; omitted: the first or last), dir? (1 next, -1 previous; default 1), page?, filter?, sort?, query? (the list, as comment.list), author?}
- `comment.zoom` (Zoom to comments): {ids (comment ids on the current page)}
- `comment.link` (Copy link to comment): {id}
- `comment.people` (People in comments): {}
- `comment.list` (List comments): {page? (default: current; "all" for every page), filter? (all|open|resolved|mine|unread; default all), sort? (date|page; default date), query? (search text), frame? (a top-level frame id), resolved? (false hides resolved ones), author? (whose threads and read state)}

## component

- `component.create`* (Object › Create component, Alt+Cmd+K): {ids?} (one frame/group becomes a component; several layers are wrapped in one)
- `component.createMultiple`* (Object › Create multiple components): {ids?}
- `component.combineVariants`* (Object › Combine as variants): {ids? (components)}
- `component.addVariant`* (Add variant): {id? (component set or variant), property?, value?} (duplicates the variant; `property`=`value` names the new one)
- `component.exposeInstance`* (Expose nested instance): {id? (an instance inside a main component), exposed? (default true)} — its properties then show on the main's instances
- `component.makeSlot`* (Make slot): {id? (a frame inside a main component), name? (the slot property's name; the frame's by default), preferred? [component or set ids]} (its instances take any content there)
- `component.removeSlot`* (Remove slot): {id? (a slot frame of a main component)} (instances lose their own content in it)
- `component.hideWhenPublishing`* (Libraries › Hide when publishing): {ids? (components, sets or layers in them; default the selection), on? (default: toggle, hiding unless all are hidden)} keeps them out of the library this file publishes, the way a name starting with `.` or `_` does: hiding puts a `.` before the name, showing takes the leading `.` and `_` away → {ids, hidden}
- `component.detach`* (Object › Detach instance, Alt+Cmd+B): {ids?}
- `component.resetInstance`* (Object › Reset all changes): {ids?}
- `component.resetOverride`* (Reset override): {id?, group? (fills|strokes|effects|opacity|visible|name|corners|characters|textStyle|padding|gap|alignment|grids|exports|interactions|size|position|component|props|slot; all when omitted)}
- `component.goToMain` (Object › Go to main component, Ctrl+Alt+Shift+K): {id?}
- `component.pushChanges`* (Object › Push changes to main component): {id?}
- `component.restoreMain`* (Object › Restore main component): {id?} (an instance whose main was deleted becomes the main again, in its place)
- `component.addProperty`* (Add component property): {id? (component, set, or a layer inside a component: it gets bound), name, type: boolean|text|instanceSwap|variant|slot, default?, layer? (node bound to it; a frame for slots), preferred? (instance swap and slot properties: component or set ids offered first)}
- `component.editProperty`* (Edit component property): {id? (component or set), name, newName?, default? (variant properties: that variant takes the top-left place), value? + newValue? (rename a variant value), index? (variant properties: move to this place; the variants' names follow), preferred? (instance swap and slot properties: component or set ids offered first)}
- `component.deleteProperty`* (Delete component property): {id? (component or set), name}
- `component.bindProperty`* (Bind layer to property): {layer?, property (null/"" unbinds), field?: visible|characters|mainComponent|slot}
- `component.properties` (Component properties): {id? (component, set or instance)}
- `component.list` (List components): {} → [{id, name, type, page, instances, folder (the Assets panel's folders: page, frames, slash names), label, library?}]
- `component.playground` (Component playground): {id? (an instance, a component or a component set; default the selection), properties? {name: value} (variant, boolean, text and instance-swap properties, as instance.setProperties takes them), language? css|html|react|swiftui|compose (default react), path? (write the preview there as a PNG), scale? (the PNG's, default 2)} → {component, properties: [{name, type, options?, value}], language, code, width, height, path?} the component with those property values, tried on a copy: its code and its look. Nothing in the document changes

## dev

- `dev.resolveChange`* (Resolve change): {ids?, reason?} (ready-for-dev frames and sections that changed since they were marked go back to Ready for dev; the reason is kept)
- `dev.compare` (Compare changes): {id? (default the first selected layer), show? (open the compare view in the app)} → {id, name, changed, snapshot, added, removed, modified, truncated, changes: [{id, name, type, change: added|removed|changed, depth, layers, properties?: [{section, property, before, after, text}]}]} what changed in a ready-for-dev frame or section since it was marked (`snapshot` is false when that isn't known: a file from before snapshots were kept)
- `dev.focus` (Focus view): {id? (a top-level frame or section; default the selection) | direction?: next|previous (the next ready-for-dev one, across pages)} → {id, name, page, index, count} show only that layer on the canvas (Escape or `dev.unfocus` ends it)
- `dev.unfocus` (Exit focus view): {} → {focused: false}

## devResource

- `devResource.add`* (Add dev resource): {id? (default the first selected layer), url (http or https), name? (default the URL without its scheme)} a link for developers on the layer; an instance also shows its main component's → {id, index}
- `devResource.edit`* (Edit dev resource): {id?, index (of the layer's own), url?, name?} → {id, index}
- `devResource.remove`* (Remove dev resource): {id?, index? (omit: every dev resource of the layer's own)} → {removed}
- `devResource.list` (List dev resources): {id? (default the first selected layer)} the layer's links, its own first, then inherited from its main component and that component's set → [{name, url, index? (own), from? (the layer it comes from)}]

## distribute

- `distribute.horizontal`* (Arrange › Distribute horizontal spacing, Alt+Shift+H): {ids?, spacing?}
- `distribute.vertical`* (Arrange › Distribute vertical spacing, Alt+Shift+V): {ids?, spacing?}

## doc

- `doc.switch` (Switch document): {index}
- `doc.nextTab` (Next tab, Ctrl+Tab): {}
- `doc.previousTab` (Previous tab, Ctrl+Shift+Tab): {}
- `doc.list` (List documents): {}
- `doc.home` (Home): {}

## edit

- `edit.undo` (Edit › Undo, Cmd+Z): {}
- `edit.redo` (Edit › Redo, Shift+Cmd+Z): {}
- `edit.delete`* (Edit › Delete, Delete): {ids?}
- `edit.duplicate`* (Edit › Duplicate, Cmd+D): {ids?, dx?, dy? (offset; default 0 for frames-in-place... Figma offsets top-level frames to the right)}
- `edit.copy` (Edit › Copy, Cmd+C): {ids?}
- `edit.cut`* (Edit › Cut, Cmd+X): {ids?}
- `edit.paste`* (Edit › Paste, Cmd+V): {parent?, x?, y? (page coordinates of the pasted top-left)}
- `edit.pasteOver`* (Edit › Paste over selection, Shift+Cmd+V): {}
- `edit.pasteReplace`* (Edit › Paste to replace, Shift+Cmd+R): {ids?}
- `edit.copyProperties` (Edit › Copy properties, Alt+Cmd+C): {id?}
- `edit.pasteProperties`* (Edit › Paste properties, Alt+Cmd+V): {ids?}
- `edit.findReplace`* (Edit › Find and replace, Cmd+F): {find, replace? (text layers), layerNames? (bool), select? (default true)}
- `edit.setDefaultProperties` (Edit › Set default properties): {id?}
- `edit.repeat`* (Repeat last command): {}
- `edit.pickColor` (Edit › Pick color, I): {}

## effect

- `effect.add`* (Add effect): {ids?, type? (dropShadow|innerShadow|layerBlur|backgroundBlur|noise|texture|glass), effect? {..}}
- `effect.remove`* (Remove effect): {ids?, index}
- `effect.set`* (Set effect): {ids?, index, effect {..}}
- `effect.move`* (Move effect): {ids?, from, to} (indices in the effect list, bottom first)

## export

- `export.add`* (Add export setting): {ids?, setting? {size: 2x|512w|512h|{by: scale|width|height, value}, suffix?, format?: png|jpg|svg|pdf|webp, bleed? (PDF: points, or with a unit: "3mm", "0.125in", "9pt"), cropMarks?, bleedMarks?, cmyk? (PDF print options)}} (without a setting: 1x, then one scale step up with an "@2x"-style suffix)
- `export.update`* (Edit export setting): {ids?, index, size? (2x|512w|512h|{by, value}), suffix?, format? (png|jpg|svg|pdf|webp), bleed? (PDF: points, or with a unit: "3mm", "0.125in", "9pt"), cropMarks?, bleedMarks?, cmyk? (PDF print options)}
- `export.remove`* (Remove export setting): {ids?, index}

## file

- `file.new` (File › New design file, Cmd+N): {name?}
- `file.open` (File › Open, Cmd+O): {path, variables? (REST: the local variables JSON as an object, JSON text or a path; default `<name>.variables.json` or `variables.json` next to the file)} (.figcraft, .json: FigCraft or REST API file JSON, .fig (best effort), .svg, .png, .jpg …); REST and .fig imports return `warnings`
- `file.openRecent` (File › Open recent): {path? | index? (into the list), clear? (forget them all), remove? (a path: forget that one)} opens a recent file; a file that no longer exists is dropped from the list. Returns the list, newest first: {files: [{path, name, exists}]} (opening returns what `file.open` does)
- `file.save` (File › Save, Cmd+S): {path?} (programmatic saves need a path the first time)
- `file.saveAs` (File › Save as, Shift+Cmd+S): {path}
- `file.export` (File › Export, Shift+Cmd+E): {ids? (default selection, else the page), format? (png|jpg|svg|pdf|webp, or fig: the whole file as .fig, experimental, with `warnings` for what was left out; other apps may not open every file), scale? (default 1) | size? (2x|512w|512h or {by: scale|width|height, value}: a scale, or a width or height in pixels), path? (else returns base64 `data`), bleed? (PDF: points, or with a unit: "3mm", "0.125in", "9pt"), cropMarks?, bleedMarks?, cmyk? (PDF print options)}
- `file.exportLayers` (Export layers): {ids? (default the selection, else every layer on the page with export settings), assets? (true: the Inspect tab's assets in and under them instead: layers with export settings, icons as SVG, images as PNG), dir? (folder to write into; else each file comes back as base64 `data`), bleed? (PDF: points, or with a unit: "3mm", "0.125in", "9pt"), cropMarks?, bleedMarks?, cmyk? (PDF print options): for every PDF instead of each setting's own} every layer once per export setting, named `<layer><suffix>.<format>` ("@2x" when a scaled export has no suffix; repeats get " 2"; slashes in a layer name make folders). Returns {files: [{name, id, bytes, path | data}], skipped (layers without settings)}
- `file.exportSvg` (File › Export selection as SVG): {ids?, path?}
- `file.exportFramesPdf` (File › Export frames to PDF): {path?, page? (page id, default the current page), bleed? (PDF: points, or with a unit: "3mm", "0.125in", "9pt"), cropMarks?, bleedMarks?, cmyk? (PDF print options)} every top-level frame in reading order, one PDF page each; returns base64 `data` without a path
- `file.import`* (File › Import, Shift+Cmd+I): {path | data (base64) + name, x?, y?, center? (SVG: centre it on x, y), variables? (REST: the local variables JSON as an object, JSON text or a path)} SVG becomes an editable frame (shapes, text, gradients, masks, effects; with `warnings` for what it left out), images become image layers, .figcraft, REST API file JSON and .fig pages are appended with their variables and flows (REST and .fig: with `warnings`)
- `file.placeImage`* (File › Place image, Shift+Cmd+K): {path | data, x?, y?}
- `file.close` (File › Close tab, Cmd+W): {index?, force? (discard unsaved changes)}
- `file.recover` (Recover file): {path} open a recovery copy (written while the app runs, read back after a crash) as a document with unsaved changes and no path: saving asks where → {index}
- `file.rename`* (File › Rename file): {name}
- `file.colorProfile`* (File › Color profile): {profile?: srgb|displayP3, convert? (default true: convert colour values so colours keep their appearance; false: keep the values and reinterpret them)} without `profile`, returns the current one (and the app opens the dialog). Returns {profile, changed}
- `file.duplicate` (File › Duplicate file): {}
- `file.revert` (File › Revert to saved): {} leave the live session first, if any
- `file.saveVersion` (File › Save to version history, Alt+Cmd+S): {name?, description?} snapshot the document into the file's version history (on a branch tab: the branch's own history; kept when the file is saved); returns the version
- `file.versionHistory` (File › Show version history): {} opens the panel; returns the versions like `version.list`
- `file.newFromTemplate` (File › New from template): {template (an id from `template.list`), name? (the document's name; default the template's)} opens a new, unsaved document built from the template → {index, template}; without `template`, returns {templates} (and the app shows them to pick from)

## fill

- `fill.add`* (Add fill): {ids?, paint? (default #D9D9D9 or white for frames)}
- `fill.remove`* (Remove fill): {ids?, index}
- `fill.set`* (Set fill): {ids?, index?, paint | color, opacity?, visible?, blend?}
- `fill.pattern`* (Pattern fill): {source (layer id), ids?, index? (default the top fill), tile? (grid|horizontalHex|verticalHex), scale? (1 = the source's size), spacing? [x, y], align? (start|center|end), opacity?} the source layer tiled; it updates as the source changes
- `fill.move`* (Move fill): {ids?, from, to} (indices in the fill list, bottom first)

## frame

- `frame.create`* (Create frame): {preset? (name from FRAME_PRESETS), x?, y?, width?, height?, parent?, name?, props?} (a preset without x/y lands to the right of the page's frames)
- `frame.swapOrientation`* (Swap orientation): {ids?} (portrait ⇄ landscape: width and height trade places)
- `frame.presets` (List frame presets): {}

## grid

- `grid.add`* (Add layout grid): {ids?, grid? {kind: grid|columns|rows, ..}}
- `grid.remove`* (Remove layout grid): {ids?, index}
- `grid.move`* (Move layout grid): {ids?, from, to} (indices in the layout grid list, bottom first)

## guide

- `guide.add`* (Add guide): {vertical (bool), offset, frame? | page?} → {index}
- `guide.move`* (Move guide): {index, offset, frame? | page?}
- `guide.remove`* (Remove guide): {index?, frame? | page?} (no index: the selected guide)
- `guide.select` (Select guide): {index?, frame? | page?} a ruler guide to delete or nudge (deselects layers; no index: none)
- `guide.clear`* (Remove all guides): {frame? | page?}

## help

- `help.shortcuts` (Help › Keyboard shortcuts, Ctrl+Shift+?): {}
- `help.about` (Help › About FigCraft): {}
- `help.page` (Help › Help page): {}
- `help.gettingStarted` (Help › Getting started): {show? (default true; false closes them)} the Getting started tips on the home screen: shows them again (the app opens the home screen), or closes them until asked for → {shown}

## image

- `image.place`* (Place image): {data (base64) | path, x?, y?, width?, height?, parent?, mode? (fill|fit|crop|tile)} → {id, image, width, height, imageProfile (its embedded colour profile; null: taken as sRGB)}
- `image.adjust`* (Adjust image): {ids?, target? (fill|stroke, default fill), index? (default every image paint), preset? (vivid|muted|warm|cool|blackAndWhite|fade|reset, or the name of a preset saved in the file), filters? ({exposure, contrast, saturation, temperature, tint, highlights, shadows}: each -1..1, applied over the preset)} sets the adjustments of the layers' image paints; returns {changed}
- `image.savePreset`* (Save image preset): {name, filters? (default the adjustments of the first image paint of `ids`/the selection), ids?, target?, index?} saved in the file; a preset with the same name is replaced
- `image.deletePreset`* (Delete image preset): {name}
- `image.presets` (Image presets): {} → {builtIn: [{id, label, filters}], saved: [{name, filters}]}

## inspect

- `inspect.code` (Code for layer): {id?, language?: css|html|react|leptos|swiftui|compose (default css; html, react and leptos are the whole layer tree; components take their properties as parameters, instances pass their values; a component connected to code (codeConnect.set) gives its import and snippet instead), unit?: px|rem (CSS, HTML, React and Leptos; default px), rootFontSize? (rem: pixels per rem, default 16)} → {code, language, connected}
- `inspect.readyForDev` (Ready for dev): {status?: readyForDev|completed|any (default readyForDev), page? (page id; default every page)} → {items: [{id, name, page, status}]} frames and sections by handoff status (set it with `node.set {devStatus}`)
- `inspect.assets` (Inspect assets): {ids? (default the selection)} → {assets: [{id, name, kind: export|icon|image, exports}]} the layers in and under them to hand over as files: those with export settings, icons (small, vector shapes only; SVG) and images (PNG). Export them with `file.exportLayers {assets: true}`
- `inspect.properties` (Inspect properties): {id?, colorFormat?: hex|rgb|css|hsl|hsb (default hex)} → {sections: [{title, rows: [{label, value, color?, token?}]}]} layout (positions from the frame around the layer), auto layout, typography, fills, strokes and effects, with style and variable names
- `inspect.componentCode` (Component code): {id? (component, set or instance; default the selection), language?: react|leptos|swiftui|compose (default react)} → {component, name, set, properties: [{name, param, type, default, value? (instances)}], definition, usage? (instances; the connected snippet when the component is connected to code), connected: {importPath, name, template, import, code} | null}

## instance

- `instance.create`* (Create instance): {component (component or set: its default variant), x?, y?, parent?}
- `instance.place`* (Place instance): {component, x, y (page point: the instance is centred there, inside the frame under it; auto layout frames insert by position)}
- `instance.exposed` (Exposed nested instances): {id? (instance)} → the nested instance copies whose properties it exposes
- `instance.slotInsert`* (Insert into slot): {id? (a slot inside an instance, or the instance with `slot`), slot? (slot property name), component, index? (child index; on top when omitted), replace? (clear the slot first)}
- `instance.resetSlot`* (Reset slot): {id? (a slot inside an instance, or the instance with `slot`), slot?} (back to the main's default content)
- `instance.swap`* (Swap instance): {ids?, component}
- `instance.swapAt`* (Swap instance at point): {component (component or set: its default variant), x, y (page point)} swaps the instance there (preferring one showing the same component set; Alt-drop from the Assets panel); only text layers keep their overrides (by matching names)
- `instance.setProperties`* (Set instance properties): {ids?, properties {name: value}} (variant properties switch variants)

## layers

- `layers.collapseAll` (Object › Collapse layers, Alt+L): {}

## layout

- `layout.add`* (Object › Add auto layout, Shift+A): {ids?, direction? (horizontal|vertical|grid)}
- `layout.remove`* (Object › Remove auto layout, Alt+Shift+A): {ids?}
- `layout.suggest`* (Object › Suggest auto layout, Ctrl+Alt+Shift+A): {ids?}
- `layout.setTrack`* (Set grid track size): {ids?, axis: columns|rows, index (0-based), sizing: fixed|hug|fill, value? (fixed: px, default the track's current size; fill: fr, default 1)}

## libraries

- `libraries.open` (Libraries › Libraries, Alt+3): {}
- `libraries.publish` (Libraries › Publish library…): {} (opens the publish form in the Assets panel)

## library

- `library.publish`* (Publish library): {description?, include? [component/set ids, style ids, variable collection ids or names: exactly these], exclude? [same]} publishes this file's components, component sets, styles and variable collections (by default all but names starting with . or _, or what the last publish offered; variables hidden from publishing stay out unless something published uses them) as a new library version; save the file so other files see it
- `library.list` (List libraries): {assets? (also list each library's components, styles, variable collections and variables, and what this file can publish)} → enabled libraries (version, updates, errors) and this file's published library
- `library.publishToServer` (Publish library to server): {server? (an edit link of this file on a figcraft-server; omit while this file is in a live session on a server, or give the server's address with its key to keep the file there first), key?, description?, include?, exclude? (as library.publish)} publishes the library as the next version of the one kept on the server under this file (per-asset versions as library.publish); files that enabled it with a link of the file see the update → {id, version, components, styles, collections, variables, file?, edit?, view? (links when the file was kept there now)}
- `library.add`* (Add library): {path (.figcraft file published as a library, or a share link of a file on a server: a view link is enough)}
- `library.usage` (Library usage): {library? (an enabled team library: id, name or link; omit for this file's library on its server)} → what files report: {id, name, instances, files: [{name, updated, instances}], components: [{id, name, instances, files}]}
- `library.swap`* (Swap library): {from (an enabled library: id, name or path), to (another enabled library)} re-points every component instance, style and variable copied from `from` to the published one of the same name in `to` (instances keep their overrides) → {components, styles, variables, unmatched: [names still from `from`], removed (nothing of `from` is used any more: it was removed)}
- `library.remove`* (Remove library): {id (library id, name or path)} (copies still in use stay; unused ones are dropped)
- `library.updates` (Library updates): {} → the components, styles, variable collections and variables with a newer published version, and variables new to a library collection this file extends (listed without an `id`: no copy yet)
- `library.acceptUpdates`* (Accept library updates): {ids? [library ids; all when omitted]} pulls updated components, styles, variable collections and variables in (instances keep their overrides; bound layers follow)
- `library.place`* (Place library component): {library (id, name or path), component (id or name of a published component, set or variant), x?, y? (page point; default the view's centre)}
- `library.swapAt`* (Swap instance to library component): {library, component (id or name of a published component, set or variant), x, y (page point)} copies the component in and swaps the instance there to it (as instance.swapAt)
- `library.import`* (Import library component): {library, component} → {component (local, read-only main to instantiate with instance.create)}
- `library.applyStyle`* (Apply library style): {library, style (id or name of a published style), ids?, target? (fill|stroke)} copies the style in (linked, read-only) and applies it
- `library.importVariable`* (Import library variable): {library, variable (id or name of a published variable)} → {variable (local, read-only linked copy to use with variable.bind, or as an alias in variable.set)}
- `library.bindVariable`* (Bind library variable): {library, variable (id or name of a published variable), field (as variable.bind), ids?} copies the variable in (linked, read-only) and binds it
- `library.aliasVariable`* (Alias library variable): {library, alias (id or name of a published variable of the same type), variable (a local variable), mode? (default first)} copies the library variable in (linked, read-only) and makes the local variable's value an alias of it
- `library.setVariableMode`* (Set library variable mode): {library, collection (id or name of a published collection), mode (id or name), ids? (frames; the page when omitted)} copies the collection in (linked, read-only) and sets its mode on the frames
- `library.extendCollection`* (Extend library collection): {library, collection (id or name of a published collection), name? (default "<name> (extended)")} → {id}: a collection of this file with the library collection's modes and variables (they follow its updates); override their values per mode with variable.set (variable.resetOverride goes back to the inherited value) and add variables of its own

## measure

- `measure.distances` (Measure distances): {ids? (default selection), to? (layer id; default the parent)} → {lines: [{x0, y0, x1, y1, label, dashed}]} (page space; what Alt-hover shows)
- `measure.padding` (Measure auto layout padding): {id? (an auto layout frame or a child; default the selection)} → {frame, lines} (padding and gaps; what Shift+Alt-hover shows)

## node

- `node.create`* (Create layer): {type: rectangle|ellipse|polygon|star|line|arrow|vector|text|frame|section|component|slice, x?, y? (relative to the parent frame; groups don't count), width?, height?, parent? (id; default: the page), index?, name?, text? (for text), path? (SVG path data for vector), props? {node.set keys}, select? (default true)}
- `node.set`* (Set properties): see node-properties.md
- `node.get` (Get layer): {id}
- `node.reparent`* (Move layer into): {ids?, parent, index?}
- `node.reorder`* (Reorder layer): {id, index}

## object

- `object.rename`* (Object › Rename, Cmd+R): {ids?, name?} (without a name: rename the layer inline in the layers panel)
- `object.batchRename`* (Object › Batch rename): {ids?, find? (match; empty: none), regex? (find is a regular expression), replace? (for each match), name? (pattern for the whole name), start? (where $n starts and $N stops; default 1)} codes in replace and name: $& current name (or the match), $` and $' text before and after the match, $1…$9 groups, $n up, $N down, $nnn padded; layers are numbered in stacking order, bottom first
- `object.toggleVisible`* (Object › Show/Hide selection, Shift+Cmd+H): {ids?, visible?}
- `object.toggleLock`* (Object › Lock/Unlock selection, Shift+Cmd+L): {ids?, locked?}
- `object.hideOthers`* (Object › Hide other layers): {}
- `object.opacityKeys`* (Opacity from number keys): {digits ("1"…"9": 10%…90%, "0": 100%; two digits: that percentage, "45" is 45%), ids?}
- `object.removeFill`* (Object › Remove fill, Alt+/): {ids?}
- `object.removeStroke`* (Object › Remove stroke, Shift+/): {ids?}
- `object.swapFillStroke`* (Object › Swap fill and stroke, Shift+X): {ids?}
- `object.flipH`* (Object › Flip horizontal, Shift+H): {ids?} (in vector edit mode without ids: the selected points)
- `object.flipV`* (Object › Flip vertical, Shift+V): {ids?} (in vector edit mode without ids: the selected points)
- `object.rotate180`* (Object › Rotate 180°): {ids?} (in vector edit mode without ids: the selected points)
- `object.rotateLeft`* (Object › Rotate 90° left): {ids?} (in vector edit mode without ids: the selected points)
- `object.rotateRight`* (Object › Rotate 90° right): {ids?} (in vector edit mode without ids: the selected points)
- `object.group`* (Object › Group selection, Cmd+G): {ids?, name?}
- `object.ungroup`* (Object › Ungroup selection, Shift+Cmd+G): {ids?}
- `object.frameSelection`* (Object › Frame selection, Alt+Cmd+G): {ids?, name?}
- `object.removeFrame`* (Object › Remove frame): {ids?}
- `object.convertToGroup`* (Convert to group): {ids?} (frames become groups in place, their layers staying where they are; what only a frame has goes: auto layout, fills, strokes, corner radius, clipping, layout grids, guides and scrolling. Groups are left alone; instances, main components, layers inside instances and empty frames are refused)
- `object.convertToFrame`* (Convert to frame): {ids?} (groups become frames of the same box in place, their layers staying where they are: no fill, not clipping. Frames are left alone; instances, main components and layers inside instances are refused)
- `object.wrapInSection`* (Wrap in new section): {ids?, name?} (layers on the page or in a section; the section wraps them with some room)
- `object.resizeToFit`* (Object › Resize to fit, Alt+Shift+Cmd+R): {ids?} (frames, sections and components shrink or grow to their contents; the contents stay put)
- `object.mask`* (Object › Use as mask, Ctrl+Alt+M): {ids?}
- `object.releaseMask`* (Object › Release mask): {ids?}
- `object.moveToPage`* (Object › Move to page): {ids?, page}
- `object.setThumbnail`* (Object › Set as thumbnail): {id?}
- `object.rasterize`* (Object › Rasterize selection): {ids?, scale? (default 2)}

## page

- `page.add`* (Add page): {name?} (a name starting with a hyphen adds a divider)
- `page.select` (Go to page): {id | index}
- `page.rename`* (Rename page): {id?, name} (an empty page named with a leading hyphen becomes a divider)
- `page.delete`* (Delete page): {id?}
- `page.duplicate`* (Duplicate page): {id?}
- `page.move`* (Move page): {id?, index}
- `page.setBackground`* (Page background): {id?, color}
- `page.list` (List pages): {}

## paint

- `paint.documentColors` (Document colours): {page?, limit? (default 21)} → solid colours used on the page, most used first

## plugin

- `plugin.list` (List plugins): {} → {plugins: [{id, name, version, main, permissions, commands, path, loaded}], last}
- `plugin.import` (Plugins › Development › Import plugin from manifest…): {path (figcraft-plugin.json or its folder) | manifest (object or JSON text), wasm (base64)} replaces a plugin with the same id
- `plugin.remove` (Remove plugin): {id}
- `plugin.run` (Run plugin): {id, command? (default: the first), params? (the command's parameters), fuel? (lower instruction budget)} one undo step → {output, logs, calls, fuel, panel}
- `plugin.ui` (Plugin panel): {id?} → plugin id's open panel (without id: the one opened last) {plugin, command, title, controls, values}, or null
- `plugin.event` (Use plugin panel control): {id, control, value? (a field's new value)} presses a button or sets a field in the plugin's open panel; the plugin is called back as one undo step → like plugin.run
- `plugin.close` (Close plugin panel): {id} → {closed}
- `plugin.directory.list` (Browse plugin directory): {server? (ws://host:port/; default: the one browsed last), query?} → {server, plugins: [{id, name, version, description, author, api, access, commands, widget, bytes, sha256, published, versions, installed, update}]}
- `plugin.directory.install` (Install plugin from directory): {id, version? (default: the latest), confirm: true (required: installing runs the plugin's code), server?, sha256? (the one shown)} downloads, checks the SHA-256 and installs or updates it → {installed, name, version, permissions, sha256, path, source, replaced}
- `plugin.directory.publish` (Publish plugin to directory): {path (a plugin folder or its figcraft-plugin.json) | plugin (an installed plugin's id), server (ws://host:port/?key=…)} → {published: entry, server}
- `plugin.directory.unpublish` (Unpublish plugin from directory): {id, version? (default: every version), server (ws://host:port/?key=…)} → {id, removed: [versions]}

## plugins

- `plugins.runLast` (Plugins › Run last plugin, Ctrl+Alt+Shift+P): {}
- `plugins.manage` (Plugins › Manage plugins…): {} opens the plugins window; returns the list like `plugin.list`

## pref

- `pref.keepTool` (Preferences › Keep tool selected after use): {on?}
- `pref.highlightHover` (Preferences › Highlight layers on hover): {on?}
- `pref.renameDuplicates` (Preferences › Rename duplicated layers): {on?}
- `pref.showDimensions` (Preferences › Show dimensions on objects): {on?}
- `pref.numberKeysOpacity` (Preferences › Use number keys for opacity): {on?}
- `pref.reduceMotion` (Reduce motion): {on?}
- `pref.nudge` (Preferences › Nudge amount): {small?, big?}
- `pref.userName` (Your name in comments): {name (blank: the default, "You")}
- `pref.publishServer` (Server for online sharing): {url?: ws://host:port/ or wss://host/path/ (no key; empty: online sharing off; omit: back to the built-in server)} → {url, default (the built-in server)}: where Share ▸ Online keeps files and where join codes are asked
- `pref.language` (Interface language): {language: system|en|es|es-419|fr|de|pt-BR|ja|ko|zh-Hans|…; else English}

## proto

- `proto.interaction.add`* (Add interaction): {id?, trigger? {type: onClick|onHover|onPress|onDrag|mouseEnter|mouseLeave|mouseDown|mouseUp|afterDelay {ms}|keyPress {key (a key or a combination: Shift+K, Ctrl+Alt+Delete; or a controller button: Gamepad A|B|X|Y|LB|RB|LT|RT|View|Menu|LS|RS|Up|Down|Left|Right|Home)}}, action {type: navigate {preserveScroll?}|back|scrollTo {offset? [x, y] (where the layer ends up from the top-left)}|openOverlay {position?, offset? [x, y] (position manual: the overlay's top-left from the top-left of the layer that opens it; without it, right below that layer), close_on_outside? (default true), background?}|swapOverlay|closeOverlay|openUrl {url}|changeTo|setVariable {variable, value | expression (text, e.g. "count + 1")}|setVariableMode {collection, mode}|conditional {blocks [{condition? | expression? (text, e.g. "count >= 3"), actions}]}, dest?}, actions? [..], transition? {type: instant|dissolve|smartAnimate|moveIn|moveOut|push|slideIn|slideOut, direction?: left|right|top|bottom}, durationMs?, easing? linear|easeIn|easeOut|easeInOut|easeInBack|easeOutBack|easeInOutBack|gentle|quick|bouncy|slow|{customBezier {x1, y1, x2, y2}}|{customSpring {mass, stiffness, damping}}}, delayMs? (mouse enter, leave, down and up: how long after the gesture the actions run, up to 600000)} — or {id, dest} for a click-navigate. Returns {index}
- `proto.interaction.clear`* (Remove all interactions): {ids?}
- `proto.interaction.remove`* (Remove interaction): {id?, index}
- `proto.interaction.set`* (Edit interaction): {id?, index, interaction {..}} replaces it; or patch fields: {id?, index, trigger?, action? (first action), actions?, transition?, durationMs?, easing?, delayMs?}
- `proto.flow.add`* (Add flow starting point): {start? (top-level frame id; default selection), name?}
- `proto.flow.rename`* (Rename flow): {start, name?, description?}
- `proto.flow.remove`* (Remove flow): {start}
- `proto.settings`* (Prototype settings): {device? (a device name, "Custom size" or "None"), background?, rotation? portrait|landscape (or 0|90; phones and tablets turn), color? (one of the device's colours by name), width?, height? (the custom size's screen, 1–10000 points; picks "Custom size"), responsive? bool (frames resize to the screen and their constraints and auto layout respond)}
- `proto.present` (Present, Alt+Cmd+Enter): {start? (frame id; default: the selected frame, else the first flow, else the first frame)}
- `proto.preview` (Open prototype preview, Shift+Space): {start? (frame id; default as proto.present)} a floating preview pane over the canvas that follows edits live
- `proto.closePreview` (Close prototype preview): {}
- `proto.presentOptions` (Presentation options): {scale? fit|fitWidth|fill|actual, deviceFrame? bool, hotspotHints? bool, inspect? bool} how the presenter sizes the prototype (Fit scales down to fit, Fit width fills the width, Fill covers the window, Actual shows it at 100%), whether it draws the device, whether a click where nothing reacts flashes the hotspots (on by default) and whether the Inspect panel shows the properties of the layer under the pointer; kept for later presentations
- `proto.action.add`* (Add prototype action): {id?, index (interaction), path? (where it goes: [n] appends to an interaction with n actions, [i, b, j] inside block b of the conditional i; default: after the last action), action {type: …, as proto.interaction.add; setVariable takes `expression` text, conditional blocks take `expression` or `condition`}} → {path}
- `proto.action.set`* (Edit prototype action): {id?, index, path [action, block, action, …], action {…}} replaces the action there
- `proto.action.remove`* (Remove prototype action): {id?, index, path} (an interaction keeps at least one action: remove the interaction instead)
- `proto.action.move`* (Reorder prototype action): {id?, index, path, to (its new index in the same list)} → {path}
- `proto.conditional.addBlock`* (Add else if / else): {id?, index, path (a conditional action), else? bool (add the else block; default: an else if before it), expression? (text, e.g. "count >= 3") | condition? (expression JSON); default condition: the first variable equal to its value} → {block}
- `proto.conditional.setCondition`* (Edit condition): {id?, index, path (a conditional action), block, expression (text) | condition (expression JSON)} the condition must give true or false
- `proto.conditional.removeBlock`* (Remove if / else if / else): {id?, index, path (a conditional action), block} removing the if when only an else (or nothing) is left removes the whole conditional action → {removedAction}
- `proto.evaluate` (Evaluate prototype expression): {expression (text, e.g. "count + 1", "accent[Dark]", "mode(Theme) == 'Dark'") | expr (expression JSON), id? (the layer it runs on: variables resolve in its modes; default: the document's default modes)} → {value, type, text} without changing anything

## section

- `section.toggleContents`* (Hide/Show section contents): {ids?, hidden? (default: hide unless all are hidden)} (a hidden section shows only its name and outline; its layers aren't drawn or hit)

## select

- `select.set` (Select): {ids: [..]} (replace the selection)
- `select.add` (Add to selection): {ids}
- `select.remove` (Remove from selection): {ids}
- `select.layersAt` (Layers at a point): {x, y (page coordinates)} → {layers: [{id, name, type, depth}]} (every layer under the point, front-most first; what the context menu's Select layer lists)
- `select.all` (Edit › Select all, Cmd+A): {}
- `select.none` (Edit › Select none, Escape): {}
- `select.inverse` (Edit › Select inverse, Shift+Cmd+A): {}
- `select.area` (Select area, Ctrl+Space): {x, y, width, height (page units; a marquee from x, y), add? (toggle like a Shift marquee), deep? (nested layers, like Cmd/Ctrl)} → {selection}; with no box: draw one from the keyboard in the app (arrows move it, Cmd/Ctrl+arrows or Shift+arrows size it, Enter selects, Escape cancels)
- `select.children` (Object › Select layer › Select children, Enter): {}
- `select.parent` (Object › Select layer › Select parent, Shift+Enter): {}
- `select.next` (Object › Select layer › Select next sibling, Tab): {}
- `select.previous` (Object › Select layer › Select previous sibling, Shift+Tab): {}
- `select.matching` (Edit › Select matching layers, Alt+Cmd+A): {}
- `select.sameFill` (Edit › Select all with same › Select same fill): {}
- `select.sameStroke` (Edit › Select all with same › Select same stroke): {}
- `select.sameEffect` (Edit › Select all with same › Select same effect): {}
- `select.sameText` (Edit › Select all with same › Select same text properties): {}
- `select.sameFont` (Edit › Select all with same › Select same font): {}
- `select.sameInstance` (Edit › Select all with same › Select same instance): {}
- `select.sameProperties` (Edit › Select all with same › Select same properties): {}
- `select.byName` (Select layers by name): {query, page? (default current; "all" for every page)}

## shape

- `shape.rectangle`* (Rectangle): {x, y, width, height, parent?, props?}
- `shape.ellipse`* (Ellipse): {x, y, width, height, parent?, props?}
- `shape.polygon`* (Polygon): {x, y, width, height, parent?, props? {pointCount}}
- `shape.star`* (Star): {x, y, width, height, parent?, props? {pointCount, innerRadius}}
- `shape.line`* (Line): {x, y, width (length), parent?, props? {rotation}}
- `shape.arrow`* (Arrow): {x, y, width (length), parent?, props?}

## shapeBuilder

- `shapeBuilder.regions` (Shape builder regions): {ids?} → {sources (bottom to top), regions: [{index, path (SVG, page), sources (top-most first), parts: [{id, stroke}] (the fills and outlined strokes covering it, top-most first), bounds [x, y, w, h], point [x, y] inside}]} — visible strokes take part as their outlined areas, so stroked lines and open paths split regions
- `shapeBuilder.merge`* (Merge regions): {ids?, regions?: [i, ...], points?: [[x, y], ...] (page)} → {id, changed, removed, outlines, regions} — one new shape from the regions, styled like the top-most fill or stroke over the first; the shapes lose those areas (strokes of the shapes involved become outlined vectors: `outlines`)
- `shapeBuilder.remove`* (Remove regions): {ids?, regions?: [i, ...], points?: [[x, y], ...] (page)} → {changed, removed, outlines, regions} — the shapes (and strokes) covering the regions lose them
- `shapeBuilder.mode` (Shape builder mode): {mode: merge|remove} (what a click does; Alt does the other)

## stroke

- `stroke.add`* (Add stroke): {ids?, paint? (default black)}
- `stroke.remove`* (Remove stroke): {ids?, index}
- `stroke.set`* (Set stroke): {ids?, index?, paint | color, opacity?, visible?, blend?}
- `stroke.widthProfile`* (Width profile): {ids?, preset? (uniform|wedge|taper|eye|rounded|pinch) | points? [[t (0-1 along each subpath), scale (× stroke weight)], ...]} — none = uniform
- `stroke.brush`* (Brush): {ids?, preset (taper|ink|ribbon|bristle: stretched along the path; dots|stars|confetti|leaves: scattered along it | null: plain), spacing? (× weight), sizeJitter? (0-1), rotationJitter? (0-1), scatter? (0-4 × weight), seed?} layers without a stroke get a black one
- `stroke.move`* (Move stroke): {ids?, from, to} (indices in the stroke list, bottom first)

## style

- `style.create`* (Create style): {type: paint|text|effect|grid, name, from? (node id; default first selected), description?, value? (paints/effects/grids/text style JSON)}
- `style.apply`* (Apply style): {ids?, style (id or name), target? (fill|stroke; paint styles), start?, end? (text styles: these chars; while editing text, the selected chars)}
- `style.detach`* (Detach style): {ids?, which: fill|stroke|effect|grid|text, start?, end? (text: these chars; while editing text, the selected chars)}
- `style.update`* (Edit style): {style, name?, description?, value?, from? (node id: redefine from it)}
- `style.bind`* (Bind variable in style): {style, field, variable? (id or name; none: unbind)} bind a variable to a field of the style's value: a paint style's `fills/<i>/color` (or `fill`: its first paint) and `fills/<i>/stops/<j>/color`, an effect style's `effects/<i>/<color|radius|spread|offsetX|offsetY|startRadius>`, a grid style's `layoutGrids/<i>/<size|count|gutter|offset>`, a text style's `fontSize|lineHeight|letterSpacing` (numbers, px) and `fontFamily|fontStyle` (strings). Every layer using the style shows the field resolved in its own modes; the style keeps it resolved in the default modes
- `style.duplicate`* (Duplicate style): {style} → {id} (right below it, named "<name> copy")
- `style.move`* (Move styles): {styles [ids], before? (style id; default: the end), folder? ("Brand/Blog"; "" = no folder: the styles are renamed into it)}
- `style.renameFolder`* (Rename style folder): {folder ("Brand/Blog"), name ("Brand/News")} (renames the styles in it)
- `style.delete`* (Delete style): {style}
- `style.list` (List styles): {type?}

## template

- `template.list` (List templates): {} the starter templates: [{id, name, description, kind (app|website|kit|media), size}]

## text

- `text.create`* (Text): {text, x, y, parent?, width? (fixed width wraps), props? (fontSize, fontFamily, …)}
- `text.onPath`* (Text on path): {text? (text layer), path? (vector or shape layer; default: the selected text and other layer), start? (0..1 along the path), flip?} the text follows the path and the path layer is removed → {id}
- `text.pathOptions`* (Text path options): {start? (0..1 along the path), flip?, ids?} for text on a path
- `text.removeFromPath`* (Remove text from path): {ids?} text on a path back to a line of auto-width text
- `text.bold`* (Text › Bold, Cmd+B): {ids?}
- `text.italic`* (Text › Italic, Cmd+I): {ids?}
- `text.underline`* (Text › Underline, Cmd+U): {ids?}
- `text.strikethrough`* (Text › Strikethrough, Shift+Cmd+X): {ids?}
- `text.link`* (Text › Create link, Shift+Cmd+U): {url, ids?}
- `text.bulletList`* (Text › Bulleted list, Shift+Cmd+8): {ids?} while editing: the selected paragraphs
- `text.numberList`* (Text › Numbered list, Shift+Cmd+7): {ids?} while editing: the selected paragraphs
- `text.alignLeft`* (Text › Alignment › Align left, Alt+Cmd+L): {ids?}
- `text.alignCenter`* (Text › Alignment › Align center, Alt+Cmd+T): {ids?}
- `text.alignRight`* (Text › Alignment › Align right, Alt+Cmd+R): {ids?}
- `text.alignJustify`* (Text › Alignment › Justify, Alt+Cmd+J): {ids?}
- `text.sizeUp`* (Text › Adjust › Increase font size, Shift+Cmd+.): {ids?}
- `text.sizeDown`* (Text › Adjust › Decrease font size, Shift+Cmd+,): {ids?}
- `text.weightUp`* (Text › Adjust › Increase font weight, Alt+Cmd+.): {ids?}
- `text.weightDown`* (Text › Adjust › Decrease font weight, Alt+Cmd+,): {ids?}
- `text.lineHeightUp`* (Text › Adjust › Increase line height, Alt+Shift+.): {ids?}
- `text.lineHeightDown`* (Text › Adjust › Decrease line height, Alt+Shift+,): {ids?}
- `text.trackingUp`* (Text › Adjust › Increase letter spacing, Alt+.): {ids?}
- `text.trackingDown`* (Text › Adjust › Decrease letter spacing, Alt+,): {ids?}
- `text.caseOriginal`* (Text › Case › Original case): {ids?}
- `text.caseUpper`* (Text › Case › Uppercase): {ids?}
- `text.caseLower`* (Text › Case › Lowercase): {ids?}
- `text.caseTitle`* (Text › Case › Title case): {ids?}
- `text.caseSmallCaps`* (Small caps): {ids?}
- `text.case`* (Letter case): {case: original|upper|lower|title|smallCaps, ids?}
- `text.decoration`* (Decoration): {decoration: none|underline|strikethrough, ids?}
- `text.listStyle`* (List style): {style: none|bulleted|numbered, ids?} while editing: the selected paragraphs
- `text.paragraphIndent`* (Paragraph indent): {indent (px), ids?}
- `text.paragraphSpacing`* (Paragraph spacing): {spacing (px), ids?}
- `text.maxLines`* (Max lines): {lines (0 = no limit; truncates), ids?}
- `text.setFeatures`* (OpenType features): {features: {tag: bool | null (font default)}, replace? (clear others first), id?/ids?}
- `text.setVariations`* (Variable font axes): {variations: {axis: number | null (style default)}, replace? (clear others first), id?/ids?}; while editing: the selected range
- `text.preview` (Preview text change): {command: style.apply|library.applyStyle|text.setVariations|text.style, params} shows what the command would do on the canvas without an undo step (a hovered text style or named instance, a dragged axis slider), in place of an earlier preview; text.endPreview or any other command ends it, so running the command for real commits it as one undo step
- `text.endPreview` (End text preview): {} puts the document back as it was before text.preview → {ended}
- `text.set`* (Set text): {id?, characters}
- `text.style`* (Style text range): {id?, start?, end?, fontFamily?, fontStyle?, fontWeight?, fontSize?, lineHeight?, letterSpacing?, textDecoration?, textCase?, hyperlink?, textFills?}
- `text.edit.begin` (Edit text): {id, caret? (char index; default select all)}
- `text.edit.insert`* (Type text): {text}
- `text.edit.key`* (Text key): {key: Backspace|Delete|Left|Right|Up|Down|Home|End|Enter|Tab|Escape|SelectAll, shift?, alt?, cmd?} in a list, Tab nests the item and Shift+Tab, Enter on an empty item or Backspace at its start move it out
- `text.listIndent`* (Indent list, Cmd+]): {} while editing: the selected list items a level deeper
- `text.listOutdent`* (Outdent list, Cmd+[): {} while editing: the selected list items a level out
- `text.edit.caret` (Set caret): {index, extend?}
- `text.edit.selectWord` (Select word): {index}
- `text.edit.selectLine` (Select line): {index}
- `text.edit.preedit` (Compose text (IME)): {text (empty = cancel), cursor? (chars into text)}; shown at the caret, committed by text.edit.insert
- `text.edit.selection` (Text selection): {}
- `text.edit.end` (Stop editing text): {}
- `text.fonts` (List fonts): {family? (list its styles), style?, features? (the face's OpenType features), axes? (the face's variation axes and named instances)}

## tool

- `tool.set` (Choose tool): {tool: move|scale|hand|frame|section|slice|rectangle|line|arrow|ellipse|polygon|star|pen|pencil|text|comment|shapeBuilder}
- `tool.place` (Place with the tool): {tool? (a shape or frame tool; default the current one), x?, y? (its centre, page coords; default the middle of the view)} — what a click with the tool makes, selected (Enter with the tool chosen)
- `tool.pencilBrush` (Pencil brush): {preset? (taper|ink|ribbon|bristle|dots|stars|confetti|leaves | null: plain), spacing?, sizeJitter?, rotationJitter?, scatter?, seed?} (the brush new Pencil strokes get; omit `preset` to read it)
- `tool.scaleAnchor` (Scale anchor): {anchor?: tl|t|tr|l|c|r|bl|b|br} (the point of the selection that stays put when the Scale tool scales; omit to read it)
- `tool.move` (Tools › Move, V): {}
- `tool.scale` (Tools › Scale, K): {}
- `tool.hand` (Tools › Hand, H): {}
- `tool.frame` (Tools › Frame, F): {}
- `tool.section` (Tools › Section, Shift+S): {}
- `tool.slice` (Tools › Slice, S): {}
- `tool.rectangle` (Tools › Rectangle, R): {}
- `tool.line` (Tools › Line, L): {}
- `tool.arrow` (Tools › Arrow, Shift+L): {}
- `tool.ellipse` (Tools › Ellipse, O): {}
- `tool.polygon` (Tools › Polygon): {}
- `tool.star` (Tools › Star): {}
- `tool.pen` (Tools › Pen, P): {}
- `tool.pencil` (Tools › Pencil, Shift+P): {}
- `tool.text` (Tools › Text, T): {}
- `tool.comment` (Tools › Comment, C): {}
- `tool.shapeBuilder` (Tools › Shape builder, Shift+M): {}

## transform

- `transform.nudge`* (Nudge): {dx, dy, big? (use the big nudge amount)} (auto layout children move one place instead: along the flow, between wrapped rows, to the next grid cell, or into the neighbouring nested auto layout frame)
- `transform.nudgeSize`* (Resize by nudge): {dw, dh, big?} (grow or shrink the selection by the nudge amount, top-left fixed)
- `transform.move`* (Move): {ids?, dx, dy} (page units)
- `transform.moveTo`* (Move to): {ids?, x, y} (page coordinates of the selection's top-left)
- `transform.rotate`* (Rotate): {ids?, degrees, cx?, cy? (pivot, page coords; default the selection's rotation origin, else its centre)}
- `transform.rotationOrigin` (Move rotation origin, Alt+R): {on? (default: toggles)} — shows the selection's rotation origin to drag (Escape hides it); not saved
- `transform.setRotationOrigin` (Set rotation origin): {x, y (page coords) | reset: true} — the point the selection turns about (default its centre); kept while the selection lasts, not saved
- `transform.scale`* (Scale): {ids?, factor, cx?, cy? (pivot; default top-left)} — scales size, strokes, effects, text (the K tool)
- `transform.resize`* (Resize): {ids?, width?, height?, anchor? (tl|t|tr|l|c|r|bl|b|br)}

## variable

- `variable.createCollection`* (Create variable collection): {name, modes? [names]}
- `variable.addMode`* (Add mode): {collection, name, from? (mode id or name to duplicate; default: the default mode)}
- `variable.create`* (Create variable): {collection, name, type: color|number|string|boolean, value (default mode) | values {modeName: value}}
- `variable.set`* (Set variable value): {variable, mode? (name or id; default first), value | {alias: variable} (same type, no loops)}
- `variable.delete`* (Delete variable): {variable} (bound layers keep their values; variables aliasing it take its values)
- `variable.bind`* (Bind variable): {ids?, field (fill|stroke (first paint)|fills/<i>/color|strokes/<i>/color|fills/<i>/stops/<j>/color (gradient stops)|effects/<i>/<offsetX|offsetY|radius|startRadius|spread|color>|layoutGrids/<i>/<size|count|gutter|offset>|componentProperties/<name> (instances: boolean/text properties; variant properties take string variables naming a value)|width|height|opacity (percent)|cornerRadius|gap|paddingHorizontal|characters|visible|fontSize…; list indices bottom first), variable (null unbinds)}
- `variable.setMode`* (Set variable mode): {ids? (frames/page), collection, mode (id or name; null: Auto, inherited from the parent)}
- `variable.list` (List variables): {}
- `variable.update`* (Edit variable): {variable, name?, description?, scopes? ([scope ids]; null or ["ALL_SCOPES"] = every supported property, [] = hidden from pickers), hiddenFromPublishing? (left out when the file is published as a library), codeSyntax? {WEB?, iOS?, ANDROID?: name code uses ("" clears)}}
- `variable.duplicate`* (Duplicate variable): {variable} → {id}
- `variable.renameMode`* (Rename mode): {collection, mode, name}
- `variable.removeMode`* (Delete mode): {collection, mode} (a collection keeps at least one mode)
- `variable.moveMode`* (Move mode): {collection, mode, to (index; 0 = the default mode, layers on Auto follow it)}
- `variable.renameCollection`* (Rename collection): {collection, name}
- `variable.deleteCollection`* (Delete collection): {collection} (with its variables; bound layers keep their values)
- `variable.resetOverride`* (Reset variable override): {variable (a variable of an extended collection inherited from the collection it extends), mode? (id or name; every overridden mode when omitted)} the value follows the inherited one again
- `variable.export` (Export variables): {collections? [ids or names; default every collection of this file, not library copies], format? (json (default): the local variables JSON that variable.import reads | css: custom properties, the default mode on :root and each other mode on [data-<collection>="<mode>"]), path? (write it there)} → {text}, or {path} when written
- `variable.import`* (Import variables): {variables (the local variables JSON, as variable.export writes it: an object, JSON text or a path)} collections join this file's collection of the same name (values by mode name; new modes and variables are added, a variable of another type is skipped), others are added → {collections (added), variables (added), updated, warnings}

## vector

- `vector.create`* (Vector): {path (SVG path data) | points [[x,y],..], closed?, x?, y?, parent?, props?}
- `vector.flatten`* (Object › Flatten, Alt+Shift+F): {ids?}
- `vector.outlineStroke`* (Object › Outline stroke, Alt+Cmd+O): {ids?}
- `vector.reverse`* (Vector › Reverse path direction): {ids?}
- `vector.simplify`* (Vector › Simplify vector): {ids?, tolerance?}
- `vector.offset`* (Vector › Offset path): {ids?, offset}
- `vector.join`* (Vector › Join selection, Cmd+J): {ids?} (in vector edit mode: joins the selected points)
- `vector.smoothJoin`* (Vector › Smooth join selection, Shift+Cmd+J): {ids?} (in vector edit mode: joins the selected points smoothly)
- `vector.edit.begin` (Edit vector): {id? | ids?} (default the selection; several layers are edited at once, the first active; converts shapes to vectors)
- `vector.edit.end` (Done editing): {}
- `vector.edit.state` (Vector edit state): {} → page-space overlay plus the local network
- `vector.edit.tool` (Vector edit tool): {tool: move|pen|bend|paint|lasso|cut|eraser|width}
- `vector.edit.select` (Select points): {vertices?: [i, ...], segments?: [i, ...], handles?: [[segment, start], ...], regions?: [i, ...] (filled regions, with their points), id? (an edited layer, made active), add?}
- `vector.edit.selectAll` (Select all points): {} (in every edited layer)
- `vector.edit.moveVertices`* (Move points): {vertices?, dx, dy} (local units; default the selected points of every edited layer)
- `vector.edit.nudge`* (Nudge points): {dx, dy} (page units; the selected points of every edited layer)
- `vector.edit.position`* (Point position): {x?, y?} (the selected points' top-left, in the parent's coordinates)
- `vector.edit.setHandle`* (Set handle): {segment, start (bool), x, y (local), independent?}
- `vector.edit.moveHandles`* (Move handles): {dx, dy (page units), handles?: [[segment, start], ...] (default the selected handles), independent?}
- `vector.edit.mirroring`* (Handle mirroring): {mode: none|angle|angleAndLength, vertices?}
- `vector.edit.smooth`* (Smooth or sharpen points): {vertices?, smooth? (default true)}
- `vector.edit.bend`* (Bend segment): {segment, t (0..1), x, y (page point the curve passes through)}
- `vector.edit.addVertex`* (Add point): {segment, t (0..1)}
- `vector.deleteHeal`* (Vector › Delete and heal selection, Shift+Delete): {vertices?} (default the selected points of every edited layer)
- `vector.edit.delete`* (Delete points): {vertices?, segments?} (default the selection in every edited layer)
- `vector.edit.cornerRadius`* (Point corner radius): {radius, vertices?}
- `vector.edit.strokeCap`* (Point stroke cap): {cap: none|round|square|lineArrow|triangleArrow|reversedTriangle|circleFilled|diamondFilled|null (the layer's), vertices?} — where the stroke ends at these points
- `vector.edit.strokeJoin`* (Point stroke join): {join: miter|bevel|round|null (the layer's), vertices?} — how the stroke turns at these points
- `vector.edit.paint`* (Paint bucket): {x, y} | {points: [[x, y], ...]} (page points: fills or unfills the closed area under the first, and does the same to the areas under the rest, like a drag)
- `vector.edit.cut`* (Cut path): {segment, t?} | {vertex} | {from: [x, y], to: [x, y]} (page: cuts every path the line crosses; parts that come apart move to layers of their own)
- `vector.edit.erase`* (Erase): {points: [[x, y], ...] (page), radius? (page units, default 8)} — removes the parts of paths the brush passes over
- `vector.edit.connect`* (Connect points): {a, b} (adds a straight segment)
- `vector.edit.lasso` (Lasso select): {points: [[x, y], ...] (page), add?}
- `vector.edit.pen`* (Pen point): {x, y (page), dx?, dy? (handle drag)} — continues from the pen's open end; clicking a point connects to it
- `vector.edit.penEnd` (End pen path): {}
- `vector.edit.bounds` (Selected points' bounds): {} → {x, y (top-left in the parent's coordinates), width, height (in the vector's axes), corners (page), points}
- `vector.edit.resize`* (Resize points): {width?, height?, center? (about the centre; default keeps the top-left)} — scales the selected points' box in the vector's axes
- `vector.edit.rotate`* (Rotate points): {angle (degrees, counter-clockwise), cx?, cy? (page pivot; default the box centre)}
- `vector.edit.transform`* (Transform points): {matrix: [a, b, c, d, e, f] (page space), vertices? (default the selected points)}
- `vector.edit.widthPoint`* (Width point): {action?: add|set|remove, index?, t? (0-1 along the path), width? (px) | scale? (× stroke weight)} — add needs t (width defaults to the current one); set moves or resizes point `index`; with `side` only that side of the path changes (looking along it): `width` is then the distance from the centre line to that edge and `scale` that side's scale (× stroke weight, as if both sides were that wide)

## version

- `version.list` (List versions): {} the version history, oldest first: [{id, index, name, description, time (Unix seconds), auto?, previewing?}]
- `version.restore`* (Restore version): {id | index} replace the design with the version (one undo step; the file name and the comments stay; the design as it was is kept in the history first, unless a version of it was just saved or restored)
- `version.rename` (Rename version): {id | index, name, description?} a titled autosave becomes a named version
- `version.delete` (Delete version): {id | index}
- `version.preview` (View version): {id | index} show the version on the canvas in place of the document (read-only; `version.restore` keeps it, `version.exitPreview` goes back)
- `version.autosave` (Autosave version): {} save an automatic checkpoint when the document has unsaved changes since the last version (the app does this every 30 minutes); keeps the newest 20 autosaves → {saved, version?}
- `version.exitPreview` (Back to current version): {} end a version preview
- `version.duplicate` (Duplicate version): {id | index} open the version as a new document; returns its tab `index`

## view

- `view.zoomIn` (View › Zoom in, Cmd+=): {}
- `view.zoomOut` (View › Zoom out, Cmd+-): {}
- `view.zoom100` (View › Zoom to 100%, Shift+0): {}
- `view.zoom50` (View › Zoom to 50%): {}
- `view.zoom200` (View › Zoom to 200%): {}
- `view.zoomFit` (View › Zoom to fit, Shift+1): {}
- `view.zoomSelection` (View › Zoom to selection, Shift+2): {}
- `view.set` (Set view): {zoom?, cx?, cy? (page coordinate at the centre), vw?, vh? (viewport size)}
- `view.zoomAt` (Zoom tool): {x, y (page point kept in place), out? (zoom out a step), width?, height? (an area to fit instead)}
- `view.get` (Get view): {}
- `view.prevFrame` (View › Zoom to previous frame, Shift+N): {}
- `view.nextFrame` (View › Zoom to next frame, N): {}
- `view.prevPage` (View › Previous page, PageUp): {}
- `view.nextPage` (View › Next page, PageDown): {}
- `view.pixelGrid` (View › Pixel grid, Shift+'): {on?}
- `view.layoutGrids` (View › Layout grids, Shift+G): {on?}
- `view.rulers` (View › Rulers, Shift+R): {on?}
- `view.slices` (View › Slices): {on?}
- `view.comments` (View › Comments, Shift+C): {on?}
- `view.multiplayerCursors` (View › Multiplayer cursors, Alt+Cmd+\): {on?} others' cursors in a live session
- `view.pan` (Pan the view): {dx, dy (arrow-key steps, e.g. 1 or -1), big? (ten times as far, like Shift)}
- `view.outlines` (View › Outlines › Outlines, Shift+Cmd+O): {on?}
- `view.outlinesSelection` (View › Outlines › Outlines for selection): {on?} outline mode for the selected layers only
- `view.outlinesHiddenLayers` (View › Outlines › Include hidden layers in outlines): {on?} outline mode (and outlines for the selection) outlines hidden layers too; they can be clicked there
- `view.outlinesObjectBounds` (View › Outlines › Include object bounds in outlines): {on?} outline mode also draws each layer's box (groups, text, vectors); a click on a box's edge picks its layer
- `view.maskOutlines` (View › Mask outlines): {on?}
- `view.pixelPreview` (View › Pixel preview, Ctrl+Alt+P): {on?, scale? (1|2: rendered pixels per page pixel; turns it on)}
- `view.frameOutlines` (View › Frame outlines): {on?}
- `view.proofSrgb` (View › Soft-proof sRGB): {on?} mark the colours of a Display P3 file that sRGB screens and files can't show
- `view.snapGeometry` (Preferences › Snap to geometry): {on?}
- `view.snapObjects` (Preferences › Snap to objects): {on?}
- `view.snapPixel` (Preferences › Snap to pixel grid, Shift+Cmd+'): {on?}
- `view.toggleUi` (View › Panels › Show/Hide UI, Cmd+\): {on?}
- `view.fullscreen` (View › Full screen, F11): {on?} the window fills the screen (the desktop app; a no-op headless)
- `view.layers` (View › Panels › Layers panel, Alt+1): {}
- `view.assets` (View › Panels › Assets panel, Alt+2): {}
- `view.design` (View › Panels › Design panel, Alt+8): {}
- `view.prototype` (View › Panels › Prototype panel, Alt+9): {}
- `view.designPrototype` (Switch between Design and Prototype, Shift+E): {}
- `view.devMode` (Dev Mode, Shift+D): {}
- `view.leftSidebar` (Show/Hide left sidebar, Shift+Cmd+\): {}
- `view.panelWidths` (View › Panels › Reset panel widths): {left?, right? (the panels' widths in pixels, kept within their limits)} without either, both go back to their default width (a double-click on a panel's edge does it for that panel)
- `view.nextRegion` (Focus next region, F6): {}
- `view.previousRegion` (Focus previous region, Shift+F6): {}
- `view.contextMenu` (Show context menu, Shift+F10): {} the selection's context menu at its layer row (when the layers panel has the keyboard) or on the canvas; the menu takes the keyboard
- `view.themeLight` (View › Theme › Light theme): {}
- `view.themeDark` (View › Theme › Dark theme): {}
- `view.themeSystem` (View › Theme › Follow system theme): {}

## widget

- `widget.insert` (Insert widget): {plugin (a widget plugin's id), x?, y? (top-left; default: centred in the view), fuel?} the plugin draws it; one undo step → {id, plugin, state, targets, output, logs, calls, fuel}
- `widget.click` (Click widget): {id (a widget or a layer in one), target (see widget.list), fuel?} calls the widget's plugin back, which redraws it; one undo step → like widget.insert
- `widget.list` (List widgets): {} → {widgets: [{id, plugin, name, page, state, targets}]}

## window

- `window.new` (File › New window): {path?, index?} a new window with a new file, the file at `path`, or open file `index` moved into it
- `window.focus` (Bring window to front): {id} a window id (control channel `window.list`)
