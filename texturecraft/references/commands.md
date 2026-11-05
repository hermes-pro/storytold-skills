# TextureCraft command catalog

Generated from the MCP server's `command_list` (TextureCraft 0.3.2, 162 commands; the same list as
`texturecraft-cli commands`). Run one with `command_run {id, params}`, several with `command_batch {steps:
[{id, params}]}`, or from a shell with `texturecraft-cli run <input> <id> '<json>' -o out.tcraft`. Programmatic
calls never open a dialog. `?` = optional, `a\|b` = choices, `→ {...}` = what it returns. Ids: layers and
effects are integers from `layer.list` / `session_inspect`; `ts` is a texture set index. Colors are
`"#rrggbb"` or linear `[r, g, b]` 0..1. Viewport points are pixels in the session viewport (1280×800 unless
`viewport: [w, h]` is given). **[path: CLI/app only]** marks commands that take a host `path`/`dir`: MCP
`command_run` refuses them (`` `file.save` with host paths is disabled for automation; … ``); use the MCP
workspace tools (`project_open`, `project_save`, `mesh_import`, `mesh_reimport`, `mesh_export`,
`bake_mesh_add`, `resource_import`, `material_save`, `material_load`, `textures_export`) or the CLI.
Grep this file rather than reading it whole, e.g. `grep -n '^- `mask' commands.md`.

Groups: Edit (3), Project and templates (5), Files (11), Texture sets and mesh maps (15), Layers (26), Masks and smart masks (10), Effects (15), Filters (1), Materials (8), Tools, brush and strokes (26), Viewport, camera and display (20), Bake (12), Export (5), Resources and text (5)

## Edit (undo, history)

- `edit.undo` (Edit › Undo, Ctrl+Z): {steps?: 1 (as many as there are)} → {undone: the last step undone, steps}
- `edit.redo` (Edit › Redo, Ctrl+Y): {steps?: 1 (as many as there are)} → {redone: the last step redone, steps}
- `edit.history` (History): {} → {undo: steps, oldest first, redo: undone steps, next first}

## Project and templates

- `project.templates` (Project templates): {} → [{name, builtin, resolution, normalFormat, channels: [ids], specGloss}]
- `project.template.save` (Save project settings as template): {name} → {name, path?}: the current project's channels (active texture set), resolution, normal format and shader settings; replaces a user template of that name
- `project.new` (New project from a built-in mesh): {mesh?: material_ball\|sphere\|cube\|rounded_cube\|cylinder\|torus\|plane\|crate\|udim_plane, resolution?: 1024 (or the template's), name?, uvTiles?: bool (UDIM; default: when the UVs leave tile 1001), template?: project template name (see project.templates)}
- `project.sample` (File › Open sample project): {}
- `project.inspect` (Inspect project): {}

## Files (MCP: use the workspace tools)

- `file.importMaterialX` (File › Import MaterialX material...) **[path: CLI/app only]**: {path: a .mtlx file, material?: the surfacematerial to read (default: the first), name?: layer name} → {layer, material, channels, resources, warnings}: one fill layer with the material's textures (read from the file's folder) and values; open_pbr_surface, standard_surface and gltf_pbr are read
- `file.new` (New project from a mesh file) **[path: CLI/app only]**: {mesh: path to .glb/.gltf/.fbx/.dae/.usd/.usda/.usdc/.usdz/.abc/.obj/.ply/.stl, resolution?: 2048, name?, uvTiles?: bool (UDIM; default: when the UVs leave tile 1001), template?: project template name}
- `file.open` (File › Open..., Ctrl+O) **[path: CLI/app only]**: {path: .tcraft project or mesh file}
- `file.save` (File › Save, Ctrl+S) **[path: CLI/app only]**: {path?: .tcraft (default: the project's own file)}
- `file.saveAs` (File › Save as..., Ctrl+Shift+S) **[path: CLI/app only]**: {path}
- `file.saveCopy` (File › Save a copy...) **[path: CLI/app only]**: {path}
- `file.close` (File › Close, Ctrl+F4): {}
- `file.reimportMesh` (Edit › Reimport mesh, Ctrl+Shift+R) **[path: CLI/app only]**: {path?, preserveStrokes?: bool (painted pixels follow the surface when the UVs changed; default false)} → {preserved?: texels re-projected}
- `file.exportTextures` (File › Export textures) **[path: CLI/app only]**: {dir, preset?: built-in or user preset name, or a preset object {name, maps}, ts?: index\|"all", format?: png\|jpg\|tga\|tif\|exr\|..., bitDepth?, padding?: none\|dilation\|dilationDefault\|infinite, dilation?: px, size?: px, normalFormat?: openGl\|directX, colorSpace?: sRGB (default for 8/16-bit files)\|Linear Rec.709 (default for exr, hdr)\|ACEScg\|ACES2065-1 (colour maps are converted, data maps never are; 8/16-bit files clamp to 0-1; a chosen space is also recorded in the colour maps: an ICC profile in PNG, JPEG, TIFF and WebP, the chromaticities in EXR; TGA, BMP and HDR can't hold one and warn), materialX?: bool (also write a .mtlx OpenPBR material per texture set; needs the "OpenPBR (separate maps)" preset)}
- `file.exportMesh` (File › Export Mesh...) **[path: CLI/app only]**: {path: .obj, .glb, .usda, .usdc or .usdz file, format?: obj\|glb\|usda\|usdc\|usdz (default: from the extension, else obj); obj writes its .mtl and textures, usda/usdc their textures, next to the file} → {path, textures?}
- `file.removeUnused` (File › Remove unused resources...): {}

## Texture sets and mesh maps

- `textureSet.select` (Select texture set): {ts}
- `textureSet.list` (List texture sets): {}
- `textureSet.inspect` (Inspect texture set): {ts?} → {index, name, resolution, size: [w, h], uvTiles: [UDIM numbers] (empty: no UV tiles), tiles: [{udim, block: [x, y]}], channels, layers, baked, visible, active}
- `textureSet.resolution` (Texture set size): {ts?, resolution: 128..8192 (power of two)}
- `textureSet.channel.add` (Add channel): {ts?, channel}
- `textureSet.channel.remove` (Remove channel): {ts?, channel}
- `textureSet.visible` (Toggle texture set visibility): {ts?, visible?}
- `textureSet.visibility` (Show or hide texture sets): {mode: showAll\|hideAll\|invert\|solo, ts?} → {visible: [bool per set]}; solo shows only `ts` (the active set), or every set again when it already was the only one
- `textureSet.rename` (Rename texture set): {ts?, name}
- `textureSet.settings` (Texture set settings): {ts?, description?, heightStrength?, normalFormat?: openGl\|directX}
- `textureSet.parts` (List mesh parts): {ts?} — the mesh parts (submesh names) of a texture set, for geometry masks
- `textureSet.meshMap.set` (Use image as mesh map): {ts?, map: mesh map id (normal, ambientOcclusion, curvature, id, height…), image: resource name} → {map, resolution} — resampled to the size of the set's other mesh maps (or its bake size); a normal map is read in the project's normal format. A UV-tiled set takes one image per tile, named alike with the tile number (`image: "ao.1001.png"` finds ao.1002.png…)
- `textureSet.meshMap.clear` (Clear mesh map): {ts?, map}
- `textureSet.tile.resolution` (UV tile resolution): {ts?, tile: UDIM number, resolution: 128..8192 (power of two; the set's resolution clears the override)} → {ts, tile, resolution, size: [w, h]}
- `textureSet.uvTiles` (UV tiles mode): {ts?, enabled: bool} → {ts, uvTiles, dropped: [UDIM numbers whose pixels were left out]} (painted pixels are resampled into the new layout)

## Layers

- `layer.add.paint` (Layers › Add paint layer): {name?}
- `layer.add.fill` (Layers › Add fill layer): {name?, color?, roughness?, metallic?}
- `layer.add.group` (Layers › Add folder): {name?}
- `layer.remove` (Layers › Remove layer(s), Delete): {layer?}
- `layer.duplicate` (Layers › Duplicate layer(s), Ctrl+D): {layer?}
- `layer.group` (Layers › Group layer(s), Ctrl+G): {layer?}
- `layer.select` (Select layer): {layer, target?: content\|mask\|<effect id>}
- `layer.rename` (Rename layer): {layer?, name}
- `layer.visible` (Toggle layer visibility): {layer?, visible?}
- `layer.move` (Move layer): {layer?, index?} \| {layer?, above?: id\|null, inside?: bool} \| {layer?, delta: ±n}
- `layer.blend` (Set channel blending): {layer?, channel?: id\|all, mode?, opacity?: 0..1, enabled?}
- `layer.fill.set` (Set fill source): {layer? \| effect?: content fill effect id, channel, color?\|value?\|procedural?: kind, scale?, seed?, contrast?, balance?, invert?, low?, high?\|image?, normalFormat?: openGl\|directX (the image's normal map convention; alone, it changes the channel's image)\|anchor?: anchor effect id, anchorChannel?, enabled?, solo?: true (this channel on, every other one off)}
- `layer.fill.projection` (Set fill projection): {layer? \| effect?: content fill effect id, projection?: uv\|triplanar\|planar\|spherical\|cylindrical (default: the current one), scale?: number \| [u, v] (uv), rotation?: degrees (uv), offset?: [u, v] (uv) \| [x, y, z] (triplanar, planar), sharpness?: 1..64 (triplanar), axis?: 0\|1\|2 (planar, cylindrical)} — what is not given keeps its value
- `layer.colorTag` (Set layer color tag): {layer?, tag?: 0..7 (absent clears)}
- `layer.list` (List layers): {ts?}
- `layer.copy` (Layers › Copy layer(s), Ctrl+C): {layer?}
- `layer.cut` (Layers › Cut layer(s), Ctrl+X): {layer?}
- `layer.paste` (Layers › Paste layer(s), Ctrl+V): {} — above the selection, in the active texture set
- `layer.flatten` (Layers › Flatten layer, Ctrl+M): {layer?} — a fill or masked paint layer becomes a plain paint layer
- `layer.instantiateAll` (Layers › Instantiate across texture sets, Ctrl+Shift+D): {layer?, copy?: bool} — a linked instance of the layer on top of every other texture set (`copy`: independent copies)
- `layer.instance` (Layers › Create instance): {layer?, ts?: texture set (default active)} — a linked instance above that set's selection; edits to the source show in every instance
- `layer.pasteInstance` (Layers › Paste as instance): {} — an instance of the copied layer above the selection
- `layer.set` (Set layer properties): {layer?, heightMask?: {enabled?, contrast?: 0..64, offset?: -1..1} \| bool, geometryMask?: [part names] \| null} — mask with height: m' = saturate(m + contrast·4m(1−m)·(height + offset)); geometry mask: the mesh parts (textureSet.parts) the layer shows on, null for all
- `layer.add.image` (Add fill layer from image): {name, channel?: baseColor, projection?: uv\|triplanar\|planar, scale?}
- `layer.add.decal` (Add decal): {image: resource name, x?, y?: viewport pixels (default: the view center), viewport?: [w,h] \| position?: [x,y,z], normal?: [x,y,z], up?: [x,y,z] (the image's up; default the view's up, or the view direction when that is along the normal), size?: height \| [w,h] (world units; default a quarter of the mesh), rotation?: degrees, depth?, name?} — a fill layer projecting the image from a frame placed on the surface; seen from the front, the image reads the right way round
- `layer.decal.set` (Edit decal): {layer?, x?, y?, viewport? \| position?, normal? (re-place it), up?: [x,y,z], size?: height \| [w,h], rotation?: degrees, offset?: [right, up] (world units from where it was placed), depth?, image?, merge?: true continues the previous Edit decal undo step (drags)}

## Masks and smart masks

- `mask.add.white` (Layers › Mask › Add white mask): {layer?}
- `mask.add.black` (Layers › Mask › Add black mask): {layer?}
- `mask.add.colorSelection` (Layers › Mask › Add mask with color selection): {layer?, color?: [r,g,b] ID color, tolerance?}
- `mask.toggle` (Layers › Mask › Toggle mask): {layer?, enabled?}
- `mask.invertBackground` (Layers › Mask › Invert mask background): {layer?}
- `mask.invert` (Layers › Mask › Invert mask): {layer?}
- `mask.clear` (Layers › Mask › Clear mask): {layer?}
- `mask.remove` (Layers › Mask › Remove mask): {layer?}
- `mask.smart.apply` (Apply smart mask): {name: smart mask id or label, layer?}
- `mask.smart.list` (List smart masks): {}

## Effects (on content or mask)

- `effect.add.paint` (Layers › Effects › Add paint): {layer?, target?: mask\|content, name?}
- `effect.add.fill` (Layers › Effects › Add fill): {layer?, target?: mask\|content, name?, mask: value?: 0..1 \| procedural?: kind, scale?, seed? \| anchor?: anchor effect id, anchorChannel?: channel (height); content: color?, roughness?, metallic?, height?, opacity? (default: every layer channel); projection?}
- `effect.add.generator` (Layers › Effects › Add generator): {layer?, name?, generator?: edgeWear\|dirt\|thinAreas\|curvature\|ambientOcclusion\|position\|direction, level?, softness?, noise?, invert?}
- `effect.add.levels` (Layers › Effects › Add levels): {layer?, target?: mask\|content, name?, inLow?, inHigh?, gamma?, outLow?, outHigh?}
- `effect.add.filter` (Layers › Effects › Add filter): {layer?, target?: mask\|content, name?, filter?: id from filter.list (invert, threshold, blur, sharpen, hsl, levels, contrastLuminosity, colorBalance, gradientMap, posterize, clamp, histogramScan\|Range\|Shift, warp, blurDirectional, slopeBlur, matFinishGrind\|Raw\|Sanded\|Hammered), level?, radius?, amount?, hue?: turns -1..1, saturation?, lightness?, contrast?, luminosity?, shadows?\|midtones?\|highlights?: [r,g,b] -1..1, colors?: [[r,g,b]\|"#rrggbb", ...], levels?, min?, max?, position?, range?, offset?, intensity?, scale?, seed?, angle?} — material finishes go on the content
- `effect.add.compare` (Layers › Effects › Add compare mask): {layer?, name?, op?: lesser\|within\|greater, value?, tolerance?}
- `effect.add.anchor` (Layers › Effects › Add anchor point): {layer?, name?} (records the stack up to this layer for fills and masks above: effect.add.fill {anchor})
- `effect.set` (Edit effect): {effect, visible?, blend?, opacity?, name?, level?, softness?, noise?, noiseScale?, invert?, value?, anchor?, anchorChannel?, inLow?, inHigh?, gamma?, outLow?, outHigh?, tolerance?, filter parameters (see effect.add.filter)}
- `effect.remove` (Remove effect): {effect?: the selected effect}
- `effect.duplicate` (Duplicate effect): {effect?: the selected effect} → {effect} (the copy, just above it, pixels included)
- `effect.move` (Move effect): {effect, index: position in its stack, 0 = bottom (applied first)}
- `effect.histogram` (Effect input histogram): {effect, channel?: for content effects (default: the layer's first channel), bins?: 2..256 (64)} → {target: mask\|content, channel?, bins: [count per bucket over 0..1]}
- `effect.copy` (Copy effect): {effect?: the selected effect}
- `effect.cut` (Cut effect): {effect?: the selected effect}
- `effect.paste` (Paste effect): {layer?, target?: mask\|content (default: the selection's stack)} → {effect} — above the selected effect, or on top of the stack

## Filters

- `filter.list` (List filters): {} — the filter library: id, label, group, whether masks take it, default parameters

## Materials

- `material.apply` (Add smart material): {material: id or label, above?: layer id, inside?: bool, index?: n} — above the selection by default; `above` (+ `inside` for a folder) or `index` in the top-level stack (0 = bottom) place it
- `material.list` (List materials): {}
- `material.save` (Layers › Create smart material) **[path: CLI/app only]**: {layer?, path: .tcmat file, name?}
- `material.load` (Add smart material from file) **[path: CLI/app only]**: {path: .tcmat smart material, .mcmat MaterialCraft material or .mcraft package, above?: layer id, inside?: bool, index?: n} — above the selection by default, or placed like material.apply
- `material.link.set` (Set material parameter): {layer?, id, value (number, [..], bool, "#rrggbb" or {t, v}), cook?: true} — sets an exposed input of a MaterialCraft material layer and re-cooks its maps (cook: false only stores the value)
- `material.link.preset` (Apply material preset): {layer?, name, cook?: true} — applies a preset of a MaterialCraft material layer
- `material.link.cook` (Re-cook MaterialCraft material): {layer?} — re-cooks a MaterialCraft material layer at its texture set's resolution with the set's baked mesh maps
- `material.link.saveSource` (Save MaterialCraft package) **[path: CLI/app only]**: {layer?, path} — writes the MaterialCraft package (.mcraft) behind a material layer, to open in MaterialCraft

## Tools, brush and strokes

- `tool.paint` (Tools › Paint, 1): {}
- `tool.eraser` (Tools › Eraser, 2): {}
- `tool.projection` (Tools › Projection, 3): {}
- `tool.polygonFill` (Tools › Polygon fill, 4): {}
- `tool.smudge` (Tools › Smudge, 5): {}
- `tool.clone` (Tools › Clone, 6): {}
- `tool.colorPicker` (Tools › Color picker, P): {}
- `tool.geometryMask` (Tools › Geometry mask, 8): {} — then tool.click toggles the selected layer on the mesh part under the point
- `tool.select` (Select tool): {tool: paint\|eraser\|projection\|polygonFill\|smudge\|clone\|colorPicker\|path}
- `tool.brush` (Brush settings): {size?: 0..100, flow?: 0..100, opacity?: 0..100, spacing?: 1..1000, hardness?: 0..100, angle?, followPath?, alignment?: tangent\|camera, lazy?, jitterSize?, jitterAngle?, jitterFlow?, jitterPosition?, alpha?: procedural name \| {image: resource name} \| {library: id (alpha.list)}, backfaceCulling?, symmetryX?, symmetryY?, symmetryZ?, symmetryRadial?: 0..32 copies around symmetryAxis?: x\|y\|z (default y), minSize?, smudgeStrength?: 0..100, cloneSource?: composite\|layer (what the Clone tool copies), particles?: {enabled?, count?: 1..16, lifetime?: 1..128 steps, gravity?: 0..2}}
- `alpha.list` (List brush alphas): {} — procedural alphas and the built-in library
- `tool.material` (Tool material): {channel, color?\|value?, enabled?, solo?: true (paint this channel only)} or {maskValue?: 0..1}
- `tool.stencil` (Projection stencil): {image?: resource name, center?: [x,y] NDC, scale?: 0.01..10, rotation?: degrees, tile?, opacity?, clear?: bool}
- `tool.cloneSource` (Set clone source): {x, y, viewport?: [w,h]} a point on the mesh, or {uv: [u,v]}, or {clear: true} — the Clone tool copies from here (V + click)
- `tool.fillMode` (Polygon fill mode): {mode: triangle\|uvIsland\|mesh}
- `tool.stroke` (Paint stroke): {points: [[x,y],...] viewport pixels, viewport?: [w,h]} — paints with the current tool
- `tool.strokeUv` (Paint stroke in the 2D view): {points: [[u,v],...] texture coordinates 0..1} — paints in UV space like the 2D view
- `tool.click` (Tool click): {x, y, viewport?: [w,h]} — polygon fill / color picker / single dab
- `tool.state` (Tool state): {}
- `brush.preset.list` (List brush presets): {} — the built-in presets: id, label, category
- `brush.preset.apply` (Apply brush preset): {preset: id or label (brush.preset.list)} — sets the stroke (alpha, spacing, flow, hardness, jitters…), keeps the size
- `brush.preset.save` (Save brush preset) **[path: CLI/app only]**: {path} — the current brush as a .tcbrush file
- `brush.preset.load` (Load brush preset) **[path: CLI/app only]**: {path} — a .tcbrush file's stroke on the brush, keeping the size
- `tool.path` (Tools › Path, 7): {points?: [[x,y],...] viewport pixels on the mesh \| uvPoints?: [[u,v],...], viewport?: [w,h], closed?, fill?, commit?: bool, clear?: bool} — selects the Path tool and edits its curve; commit adds the path to the selected path sublayer (or a new one), painted with the current brush or filled when closed and filled. While a stored path is edited (path.edit), changes repaint it at once
- `path.edit` (Tools › Edit path): {effect: path sublayer id, index: path index} — loads a stored path into the Path tool (with its brush and material); changes to it repaint the sublayer live until commit or clear
- `path.remove` (Tools › Remove path): {effect: path sublayer id, index: path index} — removes a stored path and repaints its sublayer

## Viewport, camera and display

- `viewport.frame` (Viewport › Show entire mesh, F): {}
- `viewport.displayMaterial` (Viewport › Display material, M): {}
- `viewport.nextChannel` (Viewport › Display next channel, C): {}
- `viewport.previousChannel` (Viewport › Display previous channel, Shift+C): {}
- `viewport.nextMeshMap` (Viewport › Display next mesh map, B): {}
- `viewport.previousMeshMap` (Viewport › Display previous mesh map, Shift+B): {}
- `viewport.view` (Set view mode): {mode: material\|uvChecker\|mask\|<channel id>\|map:<mesh map id>, layer? (for mask)}
- `camera.set` (Set camera): {yaw?, pitch? (degrees), distance?, fov?, target?: [x,y,z], ortho?}
- `camera.get` (Get camera): {}
- `camera.orbit` (Orbit camera): {dx?, dy? (degrees)}
- `display.set` (Display settings): {environment?: <built-in>\|resource:<image resource>, exposure?, blur?, rotation?, opacity?, toneMapping?: linear\|aces, fov?, shadows?, aoIntensity?, bloom?, vignette?, sharpen?, grain?, postEffects?, taa?, specGloss?, parallax?, displacement? (the viewport moves the surface by the height channel), scatterColor?: [r,g,b] (linear) \| "#rrggbb", scatterRadius? (0..1 of the mesh radius), ior? (1..3, transmission), dof?: {enabled?, focusDistance? (view depth, world units; 0 = the orbit target), aperture? (lens radius, 0..1 of the mesh radius)}}
- `camera.list` (Cameras): {}
- `camera.add` (Save view as camera): {name?}
- `camera.select` (Select camera): {index? \| name?} (neither, or name "Default camera": the default camera framing the mesh)
- `camera.remove` (Remove camera): {index? \| name?}
- `camera.rename` (Rename camera): {index? \| name?, to}
- `viewport.focusAt` (Focus depth of field here): {x, y (viewport pixels), viewport?: [w, h]}
- `viewport.quickMask` (Viewport › Enable quick mask, Y): {enabled?: bool} — toggles when omitted
- `viewport.quickMask.edit` (Viewport › Edit quick mask, U): {editing?: bool} — toggles when omitted; editing enables the mask
- `viewport.quickMask.invert` (Viewport › Invert quick mask, Ctrl+Shift+I): {}

## Bake

- `bake.run` (Mode › Bake mesh maps): {ts?: index\|[indices]\|"all"\|"selected", cpu?: true (skip the GPU), ...any bake.settings parameter} → {baked, tracer: [where each set's rays ran]}
- `bake.settings` (Bake settings): {ts?: index\|[indices]\|"all"\|"selected" (default: the active set), model?: complete nested BakeSettings (named enum values), preserveEnabled?: keep each texture set enabled flag when replacing the model, resolution?, antialiasing?: 1\|2\|4\|8, dilation?, ao?: {rays?, maxDistance?, spread?: degrees (180 = hemisphere), distribution?: cosine\|uniform, ignoreBackface?: never\|always\|byMeshName, selfOcclusion?: always\|sameMeshName}, thickness?: {rays?, maxDistance?, spread?, distribution?}, bentNormal?: {rays?, maxDistance?, spread?, distribution?}, rays?, maxDistance? (all three ray maps), curvatureMethod?: normalMap\|mesh, positionMode?: boundingBox\|boundingSphere\|none, maps?: [ids], enabled?, useLowAsHigh?, maxFrontal?, maxRear?, averageNormals?, lowSuffix?, highSuffix?}
- `bake.highPoly.add` (Add high definition mesh) **[path: CLI/app only]**: {path} — a mesh file (glb, gltf, fbx, dae, usd, usda, usdc, usdz, abc, obj, ply, stl; base color textures from glTF, embedded FBX media, usdz packages and image files next to a .gltf or USD layer supply opacity)
- `bake.highPoly.remove` (Remove high definition mesh): {index? \| name? \| all?: true}
- `bake.highPoly.list` (List high definition meshes): {}
- `bake.cage.set` (Load cage mesh) **[path: CLI/app only]**: {path} — a mesh with the low poly's triangles
- `bake.cage.clear` (Remove cage mesh): {}
- `bake.skew.set` (Set Skew Correction) **[path: CLI/app only]**: {ts?, value?: 0..1 \| path: grayscale image}
- `bake.skew.paint` (Paint Skew Correction): {ts?, points: [[u,v],...], radius?: 0.03, value?: 1, hardness?: 0.5, strength?: 1, size?: 1024, continue?: false}
- `bake.skew.clear` (Remove Skew Correction): {ts?}
- `bake.cage.paint` (Paint Cage): {ts?, points: [[u,v],...], radius?: 0.03, value?: 1 (frontal distance multiplier, 0..1), hardness?: 0.5, strength?: 1, size?: 1024, continue?: false}
- `bake.cage.reset` (Reset Painted Cage): {ts?}

## Export

- `export.plan` (List export outputs): {preset?: name or preset object, ts?, format?, bitDepth?, size?, colorSpace?} → [{ts, map, file, format, bitDepth, warnings}]
- `export.presets` (Export presets): {} → [{name, maps, builtin}]
- `export.preset.get` (Get an export preset): {name} → {name, maps: [{file, format, bit_depth, channels}]}
- `export.preset.save` (Save a user export preset): {preset: {name, maps}, unique?: true = add " 2", " 3"… on a name clash instead of failing, rename?: name of the user preset this one replaces} → {name}
- `export.preset.remove` (Remove a user export preset): {name}

## Resources and text

- `resource.import` (File › Import resources) **[path: CLI/app only]**: {path} — an image file (png, jpg, tga, tif, bmp, webp, exr, hdr)
- `resource.list` (List resources): {}
- `resource.remove` (Remove resource): {name}
- `text.fonts` (List fonts): {} — the installed font families with their styles, and the built-in ones
- `resource.text` (Add text): {text (lines split at \n), font?: family (text.fonts; default a common sans-serif), style?: e.g. Bold (default Regular), size?: 8..1024 texels per em (default 256), color?: [r,g,b] linear or "#rrggbb" (default white), name?} — draws the text as an image resource with an alpha (white for tool.brush {alpha: {image}}, colored for layer.add.decal)
