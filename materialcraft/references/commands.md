# MaterialCraft command catalog

Generated from `materialcraft-cli commands` (= `command_list`; MaterialCraft 0.1.2, 68 commands). Run one with
`command_run {id, params}` or several with `command_batch {steps: [{id, params}]}`; the CLI takes the same ids
(`materialcraft-cli run <pkg> <id> <json>`, `batch`). `?` = optional. `(off)` = not runnable in a fresh session: the
node ones need a selection even when you pass `id` (`graph.select {ids}` first; see Pitfalls in SKILL.md). Commands that take a host `path` (`file.open`,
`file.save`, `file.saveAs`, `file.export`, `file.importBitmap`, `file.exportMaterial`, `file.sendToTextureCraft`,
`view.3d.loadMesh`, `graph.input.bind {path}`) are refused over MCP (`... with host paths is disabled for
automation`): use `package_open`, `package_save`, `outputs_export`, `bitmap_import`, or the CLI.
Grep this file rather than reading it whole.

Groups: file (9), graph (42), edit (10), view (5), library (1), session (1)

## file

- `file.new` (File › New › Graph..., Ctrl+N): {name?, template? (see graph.templates), size? (px, power of two)} adds a new graph to the package and opens it
- `file.newPackage` (File › New › Empty package): {name?} replaces the session with an empty package
- `file.open` (File › Open..., Ctrl+O): {path} opens an .sbs or .mcraft package (or a .mcmat material's source); returns `warnings` for what an SBS file holds that MaterialCraft can't read yet, and `path`, null for a file another program wrote (Save then needs a new `path`)
- `file.save` (File › Save, Ctrl+S): {path?} saves the package to its own file or `path`: SBS (.sbs, the default; appended when `path` has no package extension) or .mcraft
- `file.saveAs` (File › Save as..., Ctrl+Shift+S): {path} saves the package under a new name
- `file.export` (File › Export outputs..., Ctrl+Shift+E): {dir, format? (png|jpg|tga|tif|bmp|webp|exr|hdr), pattern? ($(graph)_$(identifier)), depth? (8|16|32), graph?} cooks the graph at full size and writes every output
- `file.importBitmap` (File › Import bitmap...): {path, name?} embeds an image file as a resource; returns its name
- `file.exportMaterial` (File › Export material...): {path, graph?, size? (px, power of two), values? {input: value}, inputs? {identifier: image path}} cooks the graph and writes a portable .mcmat material (maps, exposed inputs, source package) for TextureCraft
- `file.sendToTextureCraft` (File › Send to TextureCraft): {graph?} exports the graph as a portable material into TextureCraft's library folder (Documents/TextureCraft/library), where its shelf lists it

## graph

- `graph.templates` (Graph templates): {} lists the templates for file.new
- `graph.input.bind` (Set input preview image): {identifier, resource? | path?} shows a bitmap resource (or an image file, embedded) on the graph's input node `identifier`, e.g. a mesh map baked in TextureCraft
- `graph.input.unbind` (Clear input preview image): {identifier}
- `graph.open` (Open graph): {graph: index or name}
- `graph.rename` (Rename graph): {name, graph?}
- `graph.delete` (Delete graph): {graph?}
- `graph.duplicate` (Duplicate graph): {graph?}
- `graph.size` (Graph size): {width, height} in pixels (powers of two, 16..8192) or {log2: [w, h]}
- `graph.seed` (Random seed): {seed}
- `graph.format` (Output format): {format: u8|u16|f16|f32}
- `graph.cook` (Compute graph): {full?: bool} cooks now; returns per-node timings and errors
- `graph.attributes` (Graph attributes): {category?, description?, author?, tags?}
- `graph.frame.add` (Add Frame): {title?, rect? [x, y, w, h], color? [r,g,b,a]} around the selection when no rect
- `graph.frame.edit` (Edit frame): {id, title?, description?, rect?, color?}
- `graph.frame.delete` (Delete frame): {id}
- `graph.comment.add` (Add Comment): {text?, at? [x, y]}
- `graph.comment.edit` (Edit comment): {id, text?, at?, size?}
- `graph.comment.delete` (Delete comment): {id}
- `graph.pin.add` (Add Navigation pin): {name?, at? [x, y]}
- `graph.pin.delete` (Delete pin): {id}
- `graph.exposed.add` (Expose parameter): {id, label?, default (a typed value or number), min?, max?, group?, bind?: {node, param}}
- `graph.exposed.set` (Set input value): {id, value}
- `graph.exposed.delete` (Delete input): {id}
- `graph.preset.save` (Save preset): {name} stores the current input values as a preset (replacing one of that name)
- `graph.preset.apply` (Apply preset): {name}
- `graph.preset.delete` (Delete preset): {name}
- `graph.select` (Select nodes): {ids, add?: bool}
- `graph.selectUpstream` (off) (Select upstream nodes): {ids?}
- `graph.selectDownstream` (off) (Select downstream nodes): {ids?}
- `graph.align` (off) (Align nodes): {mode: left|right|top|bottom|hcenter|vcenter|hdistribute|vdistribute, ids?}
- `graph.createFromSelection` (off) (Create graph from selection): {name?, ids?} moves the nodes into a new graph and replaces them with an instance
- `graph.node.add` (Add node): {def (see library.list), at? [x, y], params? {id: value}, connectFrom? {node, port?} wires that output into the new node's first input, label?}
- `graph.node.move` (off) (Move nodes): {ids?, by? [dx, dy], to? [x, y] (single node)}
- `graph.node.rename` (off) (Rename node): {id?, label}
- `graph.node.disable` (off) (Disable selection, Shift+D): {ids?, disabled? (default: toggle)}
- `graph.node.param` (off) (Set parameter): {id?, param, value} (numbers, [x, y], "#rrggbb", enum index, typed {t, v})
- `graph.node.reset` (off) (Reset parameters): {id?, param? (default: all)}
- `graph.node.base` (off) (Set base parameters): {id?, sizeMode? (relativeToInput|relativeToParent|absolute), size? [w, h] (log2 offset, or log2 size when absolute), format? (inherit|u8|u16|f16|f32), seed?, tiling? bool}
- `graph.node.bind` (off) (Bind parameter to input): {id?, param, input (exposed id); input null unbinds}
- `graph.node.function` (off) (Set parameter function): {id?, param, function?: {nodes, output} (default: a constant of the current value), remove?: bool} drives a parameter with a function graph of the graph's inputs
- `graph.connect` (Connect): {from, fromPort? (output), to, toPort? (first input)}
- `graph.disconnect` (Disconnect): {to, toPort}

## edit

- `edit.undo` (off) (Edit › Undo, Ctrl+Z): {}
- `edit.redo` (off) (Edit › Redo, Ctrl+Y): {}
- `edit.copy` (off) (Copy selection, Ctrl+C): {ids?} copies nodes (and the wires between them)
- `edit.cut` (off) (Cut selection, Ctrl+X): {ids?}
- `edit.paste` (Paste, Ctrl+V): {at? [x, y], clip? (JSON from edit.copy)} pastes nodes, selected
- `edit.duplicate` (off) (Duplicate selection, Ctrl+D): {ids?} duplicates nodes with their inner wires and their inputs
- `edit.delete` (off) (Delete selection, Delete): {ids?}
- `edit.deleteRelink` (off) (Delete and relink, Backspace): {ids?} deletes nodes and joins what fed their first input to what they fed
- `edit.selectAll` (Select all, Ctrl+A): {}
- `edit.selectNone` (Deselect): {}

## view

- `view.2d` (View output in 2D view): {node?, port?, tiled?, channel? (rgba|r|g|b|a), histogram?}
- `view.3d` (3D view settings): {scene? (cube|cylinder|plane|sphere|material_ball|rounded_cube|torus), tiling?, yaw?, pitch?, distance?, target? ([x, y, z] orbit point in mesh radii from its center, within the pan limit preference), environment? (studio|sunset|overcast|night), envRotation?, exposure?, heightScale?, axis?, grid?}
- `view.3d.loadMesh` (Load mesh...): {path} shows an OBJ, glTF or GLB mesh in the 3D view (scene "custom")
- `view.3d.reset` (Reset scene): {}
- `view.previewSize` (Preview size): {size: 64..8192, or 0 for full size} caps node outputs while editing

## library

- `library.list` (Library): {filter?, category?} every node definition: id, label, category, inputs, outputs, parameters

## session

- `session.inspect` (Inspect): {graph?} the package, the open graph (nodes, wires, parameters, errors, timings), views and history
