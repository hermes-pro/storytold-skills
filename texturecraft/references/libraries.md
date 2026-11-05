# TextureCraft libraries and ids

Generated from the live MCP server (TextureCraft 0.3.2): `material.list`, `mask.smart.list`, `export.presets` +
`export.preset.get`, `project.templates`, `brush.preset.list`, `alpha.list`, `filter.list`. The id lists at the end
(channels, mesh maps, procedurals, blend modes, generators) come from the 0.3.2 source, because their errors
(`unknown procedural \`x\``) don't list the choices. Ids and labels both work where a command takes a name
(case, spaces and underscores ignored for channels, procedurals and blend modes). Grep this file.

## Materials (72) — `command_run material.apply {material}`

One fill layer, procedural, any resolution:

`steel` (Steel), `steel_stainless` (Steel Stainless), `steel_dark` (Steel Dark), `iron` (Iron Raw), `cast_iron` (Cast Iron), `copper` (Copper), `copper_hammered` (Copper Hammered), `brass` (Brass), `bronze` (Bronze), `gold_polished` (Gold Polished), `silver` (Silver), `aluminium` (Aluminium Raw), `aluminium_brushed` (Aluminium Brushed), `steel_brushed_aniso` (Steel Brushed Anisotropic), `chrome` (Chrome), `titanium` (Titanium), `nickel` (Nickel), `platinum` (Platinum), `zinc` (Zinc), `cobalt` (Cobalt), `galvanized` (Steel Galvanized), `rust` (Rust), `wood` (Wood Varnished), `wood_oak` (Oak), `wood_walnut` (Walnut), `wood_pine` (Pine), `plywood` (Plywood), `bark` (Bark), `wood_maple` (Maple), `wood_cherry` (Cherry), `bamboo` (Bamboo), `wood_painted` (Wood Painted), `concrete` (Concrete), `brick` (Brick Red), `tiles_ceramic` (Tiles Ceramic), `marble` (Marble), `marble_black` (Marble Black), `granite` (Granite), `asphalt` (Asphalt), `clay` (Clay Earthenware), `slate` (Slate), `sandstone` (Sandstone), `terrazzo` (Terrazzo), `sand` (Sand), `mud` (Mud), `cobblestone` (Cobblestone), `gravel` (Gravel), `plaster` (Plaster), `plastic_glossy` (Plastic Glossy), `plastic_matte` (Plastic Matte), `plastic_textured` (Plastic Textured), `rubber` (Rubber), `carbon_fiber` (Carbon Fiber), `fabric` (Fabric Cotton), `denim` (Denim), `leather` (Leather), `leather_black` (Leather Black), `velvet` (Velvet), `linen` (Linen), `wool` (Wool), `ceramic` (Ceramic White), `glass` (Glass Clear), `glass_frosted` (Glass Frosted), `ice` (Ice), `car_paint` (Car Paint), `skin` (Skin), `wax` (Candle Wax), `cork` (Cork), `paper` (Paper), `snow` (Snow), `bone` (Bone), `moss` (Moss)

## Smart materials (21) — `material.apply {material}`

A folder of fill layers with generator masks (edge wear, dirt, …). Bake first, or the masks read flat maps:

`steel_painted_worn` (Steel Painted Worn), `steel_painted_rust` (Steel Painted Rust Leaks), `military_paint` (Military Paint), `iron_rusted` (Iron Rusted), `aluminium_scratched` (Aluminium Scratched), `copper_patina` (Copper Oxidized), `bronze_statue` (Bronze Statue), `brass_tarnished` (Brass Tarnished), `gold_dirty` (Gold Dirty), `chrome_smudged` (Chrome Smudged), `wood_weathered` (Wood Weathered), `wood_chipped_paint` (Wood Chipped Paint), `concrete_dirty` (Concrete Dirty), `brick_mossy` (Brick Mossy), `plastic_dusty` (Plastic Dusty), `plastic_scuffed` (Plastic Scuffed), `leather_worn` (Leather Worn), `stone_mossy` (Stone Mossy), `paint_sun_faded` (Paint Sun Faded), `steel_water_stained` (Steel Water Stained), `plastic_grimy` (Plastic Grimy)

## Smart masks (24) — `mask.smart.apply {name, layer?}`

`edge_wear` (Edges Worn), `edge_chipped` (Edges Chipped), `dirt_cavities` (Dirt in Cavities), `dust_top` (Dust from Top), `ground_dirt` (Ground Dirt), `rust_leaks` (Rust Leaks), `scratches` (Scratches), `grunge` (Grunge Blotches), `paint_chips` (Paint Chips), `fingerprints` (Fingerprints), `edges_soft` (Edges Soft), `edges_sharp` (Edges Sharp), `exposed` (Exposed Areas), `thin_areas` (Thin Areas), `dust_cavities` (Dust in Cavities), `moss_top` (Moss from Top), `water_stains` (Water Stains), `sun_faded` (Sun Faded), `snow_top` (Snow from Top), `moss_ground` (Moss from Ground), `rust_cavities` (Rust in Cavities), `edge_scratches` (Edge Scratches), `dirt_streaks` (Dirt Streaks), `occluded` (Occluded Areas)

## Project templates (4) — `project_new {template}`

- `PBR - Metallic Roughness`: channels baseColor, metallic, roughness, normal, height; normals openGl; 2048 px
- `PBR - Specular Glossiness`: channels baseColor, normal, height, specular, glossiness; normals openGl; 2048 px; specular/glossiness shader
- `PBR - Metallic Roughness Alpha blend`: channels baseColor, metallic, roughness, normal, height, opacity; normals openGl; 2048 px
- `Unlit - Emissive`: channels baseColor, emissive, opacity; normals openGl; 2048 px

## Export presets (10) — `textures_export {dir, preset}`

Files are named from the pattern: `$mesh` = the project's mesh file stem (`mesh` for an imported file, the built-in id
such as `rounded_cube` otherwise), `$textureSet` = the texture set (material) name, `$channel` = the channel id.
Maps whose channels the set doesn't have are skipped. `export.plan {preset}` lists the files without writing.

### Document channels + Normal + AO (21 maps)

- `$mesh_$textureSet_$channel` png 8-bit: R=BaseColor G=BaseColor B=BaseColor
- `$mesh_$textureSet_$channel` png 8-bit: L=Metallic
- `$mesh_$textureSet_$channel` png 8-bit: L=Roughness
- `$mesh_$textureSet_$channel` png 16-bit: L=Height
- `$mesh_$textureSet_$channel` png 8-bit: R=Emissive G=Emissive B=Emissive
- `$mesh_$textureSet_$channel` png 8-bit: L=Opacity
- `$mesh_$textureSet_$channel` png 8-bit: L=SpecularLevel
- `$mesh_$textureSet_$channel` png 8-bit: R=Specular G=Specular B=Specular
- `$mesh_$textureSet_$channel` png 8-bit: L=Glossiness
- `$mesh_$textureSet_$channel` png 8-bit: L=CoatWeight
- `$mesh_$textureSet_$channel` png 8-bit: L=CoatRoughness
- `$mesh_$textureSet_$channel` png 8-bit: L=SheenWeight
- `$mesh_$textureSet_$channel` png 8-bit: R=SheenColor G=SheenColor B=SheenColor
- `$mesh_$textureSet_$channel` png 8-bit: L=SheenRoughness
- `$mesh_$textureSet_$channel` png 8-bit: L=AnisotropyLevel
- `$mesh_$textureSet_$channel` png 8-bit: L=AnisotropyAngle
- `$mesh_$textureSet_$channel` png 8-bit: L=ScatterWeight
- `$mesh_$textureSet_$channel` png 8-bit: L=Transmission
- `$mesh_$textureSet_$channel` png 8-bit: R=CoatNormal G=CoatNormal B=CoatNormal
- `$mesh_$textureSet_normal` png 8-bit: R=Normal G=Normal B=Normal
- `$mesh_$textureSet_ambientOcclusion` png 8-bit: L=AoMixed

### glTF PBR Metal Roughness (6 maps)

- `$mesh_$textureSet_BaseColor` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_OcclusionRoughnessMetallic` png 8-bit: R=AoMixed G=Roughness B=Metallic
- `$mesh_$textureSet_Normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl
- `$mesh_$textureSet_Emissive` png 8-bit: R=Emissive G=Emissive B=Emissive
- `$mesh_$textureSet_Clearcoat` png 8-bit: R=CoatWeight G=CoatRoughness
- `$mesh_$textureSet_Sheen` png 8-bit: R=SheenTint G=SheenTint B=SheenTint A=SheenRoughness

### Unreal Engine (Packed) (3 maps)

- `$mesh_$textureSet_BaseColor` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_OcclusionRoughnessMetallic` png 8-bit: R=AoMixed G=Roughness B=Metallic
- `$mesh_$textureSet_Normal` png 8-bit: R=NormalDirectX G=NormalDirectX B=NormalDirectX

### Unity HDRP (Mask Map) (3 maps)

- `$mesh_$textureSet_BaseMap` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_MaskMap` png 8-bit: R=Metallic G=AoMixed B=constant 0 A=Glossiness
- `$mesh_$textureSet_Normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl

### Unity Standard (Metallic Smoothness) (4 maps)

- `$mesh_$textureSet_Albedo` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_MetallicSmoothness` png 8-bit: R=Metallic G=constant 0 B=constant 0 A=Glossiness
- `$mesh_$textureSet_Normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl
- `$mesh_$textureSet_Occlusion` png 8-bit: L=AoMixed

### Blender (Principled BSDF) (7 maps)

- `$mesh_$textureSet_BaseColor` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_Metallic` png 8-bit: L=Metallic
- `$mesh_$textureSet_Roughness` png 8-bit: L=Roughness
- `$mesh_$textureSet_Normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl
- `$mesh_$textureSet_Height` png 16-bit: L=Height
- `$mesh_$textureSet_Emission` png 8-bit: R=Emissive G=Emissive B=Emissive
- `$mesh_$textureSet_Specular` png 8-bit: L=SpecularLevel

### Godot 4 (ORM) (4 maps)

- `$mesh_$textureSet_albedo` png 8-bit: R=BaseColor G=BaseColor B=BaseColor A=Opacity
- `$mesh_$textureSet_orm` png 8-bit: R=AoMixed G=Roughness B=Metallic
- `$mesh_$textureSet_normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl
- `$mesh_$textureSet_emission` png 8-bit: R=Emissive G=Emissive B=Emissive

### OpenPBR (separate maps) (15 maps)

- `$mesh_$textureSet_base_color` png 8-bit: R=BaseColor G=BaseColor B=BaseColor
- `$mesh_$textureSet_base_metalness` png 8-bit: L=Metallic
- `$mesh_$textureSet_specular_roughness` png 8-bit: L=Roughness
- `$mesh_$textureSet_specular_roughness_anisotropy` png 8-bit: L=AnisotropyLevel
- `$mesh_$textureSet_coat_weight` png 8-bit: L=CoatWeight
- `$mesh_$textureSet_coat_roughness` png 8-bit: L=CoatRoughness
- `$mesh_$textureSet_fuzz_weight` png 8-bit: L=SheenWeight
- `$mesh_$textureSet_fuzz_color` png 8-bit: R=SheenColor G=SheenColor B=SheenColor
- `$mesh_$textureSet_fuzz_roughness` png 8-bit: L=SheenRoughness
- `$mesh_$textureSet_transmission_weight` png 8-bit: L=Transmission
- `$mesh_$textureSet_subsurface_weight` png 8-bit: L=ScatterWeight
- `$mesh_$textureSet_emission_color` png 8-bit: R=Emissive G=Emissive B=Emissive
- `$mesh_$textureSet_geometry_opacity` png 8-bit: L=Opacity
- `$mesh_$textureSet_geometry_normal` png 8-bit: R=NormalOpenGl G=NormalOpenGl B=NormalOpenGl
- `$mesh_$textureSet_height` png 16-bit: L=Height

### Separate maps (21 maps)

- `$mesh_$textureSet_$channel` png 8-bit: R=BaseColor G=BaseColor B=BaseColor
- `$mesh_$textureSet_$channel` png 8-bit: L=Metallic
- `$mesh_$textureSet_$channel` png 8-bit: L=Roughness
- `$mesh_$textureSet_$channel` png 8-bit: R=Normal G=Normal B=Normal
- `$mesh_$textureSet_$channel` png 16-bit: L=Height
- `$mesh_$textureSet_$channel` png 8-bit: R=Emissive G=Emissive B=Emissive
- `$mesh_$textureSet_$channel` png 8-bit: L=Opacity
- `$mesh_$textureSet_$channel` png 8-bit: L=AmbientOcclusion
- `$mesh_$textureSet_$channel` png 8-bit: L=SpecularLevel
- `$mesh_$textureSet_$channel` png 8-bit: R=Specular G=Specular B=Specular
- `$mesh_$textureSet_$channel` png 8-bit: L=Glossiness
- `$mesh_$textureSet_$channel` png 8-bit: L=CoatWeight
- `$mesh_$textureSet_$channel` png 8-bit: L=CoatRoughness
- `$mesh_$textureSet_$channel` png 8-bit: L=SheenWeight
- `$mesh_$textureSet_$channel` png 8-bit: R=SheenColor G=SheenColor B=SheenColor
- `$mesh_$textureSet_$channel` png 8-bit: L=SheenRoughness
- `$mesh_$textureSet_$channel` png 8-bit: L=AnisotropyLevel
- `$mesh_$textureSet_$channel` png 8-bit: L=AnisotropyAngle
- `$mesh_$textureSet_$channel` png 8-bit: L=ScatterWeight
- `$mesh_$textureSet_$channel` png 8-bit: L=Transmission
- `$mesh_$textureSet_$channel` png 8-bit: R=CoatNormal G=CoatNormal B=CoatNormal

### Mesh maps (10 maps)

- `$mesh_$textureSet_$channel` png 16-bit: R=Normal G=Normal B=Normal
- `$mesh_$textureSet_$channel` png 16-bit: R=WorldNormal G=WorldNormal B=WorldNormal
- `$mesh_$textureSet_$channel` png 16-bit: R=Id G=Id B=Id
- `$mesh_$textureSet_$channel` png 16-bit: L=AmbientOcclusion
- `$mesh_$textureSet_$channel` png 16-bit: L=Curvature
- `$mesh_$textureSet_$channel` png 16-bit: R=Position G=Position B=Position
- `$mesh_$textureSet_$channel` png 16-bit: L=Thickness
- `$mesh_$textureSet_$channel` png 16-bit: L=Height
- `$mesh_$textureSet_$channel` png 16-bit: R=BentNormal G=BentNormal B=BentNormal
- `$mesh_$textureSet_$channel` png 16-bit: L=Opacity

## Brush presets (18) — `command_run brush.preset.apply {preset}`

- Basic: `basic_hard` (Basic hard), `basic_soft` (Basic soft), `airbrush` (Airbrush), `square` (Square), `dots` (Dots)
- Wear and grunge: `dry_brush` (Dry brush), `chalk` (Chalk), `spray` (Spray), `grunge` (Grunge), `splatter` (Splatter), `scratches` (Scratches), `chips` (Chips), `cracks` (Cracks), `drips` (Drips)
- Details: `stars` (Stars), `stitches` (Stitches), `rivets` (Rivets), `fur` (Fur)

## Brush alphas — `tool.brush {alpha}`

Procedural (`alpha: "<name>"`): `Round`, `Square`, `Spray`, `Grunge`, `Cloud`, `Star`, `Dry streaks`.

Library (67; `alpha: {library: id}`):

- Basic: `round_soft`, `round_hard`, `square`, `rectangle`, `triangle`, `hexagon`, `ring`, `cross`, `star_5`, `star_4`, `star_6`, `arrow`, `dots_grid`
- Grunge: `scratches`, `chips`, `splatter`, `sponge`, `grunge_spots`, `cracks`, `speckle`
- Organic: `fur`, `leaf`, `wood_knot`
- Hard surface: `rivet`, `bolt_head`, `screw_slot`, `screw_cross`, `stitches`, `vent`, `fabric`, `bricks`
- Stencil letters: `letter_a`, `letter_b`, `letter_c`, `letter_d`, `letter_e`, `letter_f`, `letter_g`, `letter_h`, `letter_i`, `letter_j`, `letter_k`, `letter_l`, `letter_m`, `letter_n`, `letter_o`, `letter_p`, `letter_q`, `letter_r`, `letter_s`, `letter_t`, `letter_u`, `letter_v`, `letter_w`, `letter_x`, `letter_y`, `letter_z`, `letter_0`, `letter_1`, `letter_2`, `letter_3`, `letter_4`, `letter_5`, `letter_6`, `letter_7`, `letter_8`, `letter_9`

An image resource works too: `alpha: {image: <resource name>}` (e.g. from `resource.text`).

## Filters (31) — `effect.add.filter {filter, …}`

"content only" filters can't go on a mask. The JSON is the parameters each starts with.

- `hsl` (HSL Perceptive, Adjustments) {"hue":0.0,"lightness":0.0,"saturation":0.0}
- `levels` (Levels, Adjustments) {"gamma":1.0,"in_high":1.0,"in_low":0.0,"out_high":1.0,"out_low":0.0}
- `contrastLuminosity` (Contrast/Luminosity, Adjustments) {"contrast":0.300,"luminosity":0.0}
- `colorBalance` (Color Balance, Adjustments) {"highlights":[0.0,0.0,0.0],"midtones":[0.0,0.0,0.0],"shadows":[0.0,0.0,0.0]}
- `gradientMap` (Gradient Map, Adjustments) {"colors":[[0.019,0.019,0.039],[0.449,0.159,0.050],[1.0,0.850,0.550]]}
- `posterize` (Posterize, Adjustments) {"levels":4.0}
- `clamp` (Clamp, Adjustments) {"max":0.800,"min":0.200}
- `histogramScan` (Histogram Scan, Adjustments) {"contrast":0.5,"position":0.5}
- `histogramRange` (Histogram Range, Adjustments) {"position":0.5,"range":0.5}
- `histogramShift` (Histogram Shift, Adjustments) {"offset":0.25}
- `invert` (Invert, Adjustments) 
- `threshold` (Threshold, Adjustments) {"level":0.5}
- `grayscale` (Grayscale, Adjustments, content only) 
- `edgeDetect` (Edge Detect, Adjustments) {"width":2.0}
- `normalInvert` (Normal Invert, Adjustments, content only) 
- `bakedLighting` (Baked Lighting, Adjustments, content only) {"ambient":0.400,"azimuth":45.0,"elevation":45.0,"light":0.800,"occlusion":1.0}
- `replaceColor` (Replace Color, Adjustments, content only) {"from":[0.5,0.050,0.050],"softness":0.150,"to":[0.050,0.150,0.5],"tolerance":0.200}
- `blur` (Blur, Blur and sharpen) {"radius":2.0}
- `blurDirectional` (Blur Directional, Blur and sharpen) {"angle":0.0,"radius":16.0}
- `slopeBlur` (Slope Blur, Blur and sharpen) {"radius":16.0,"scale":4.0,"seed":1}
- `sharpen` (Sharpen, Blur and sharpen) {"amount":1.0}
- `highPass` (High Pass, Blur and sharpen) {"radius":8.0}
- `bevel` (Bevel, Blur and sharpen) {"width":16.0}
- `glow` (Glow, Blur and sharpen) {"amount":1.0,"radius":16.0}
- `warp` (Warp, Distort) {"intensity":16.0,"scale":4.0,"seed":1}
- `warpDirectional` (Warp Directional, Distort) {"angle":0.0,"intensity":16.0,"scale":4.0,"seed":1}
- `mosaic` (Mosaic, Distort) {"size":32.0}
- `matFinishGrind` (MatFinish Grind, Material finish, content only) (material finish: roughness/height procedurals, tri-planar)
- `matFinishRaw` (MatFinish Raw, Material finish, content only) (material finish: roughness/height procedurals, tri-planar)
- `matFinishSanded` (MatFinish Sanded, Material finish, content only) (material finish: roughness/height procedurals, tri-planar)
- `matFinishHammered` (MatFinish Hammered, Material finish, content only) (material finish: roughness/height procedurals, tri-planar)

## Built-in meshes — `project_new {mesh}`, CLI `builtin:<id>`

`material_ball` (default), `sphere`, `cube`, `rounded_cube`, `cylinder`, `torus`, `plane`, `crate` (three texture
sets: Crate, Lid, Handle), `udim_plane` (UV tiles; `project.new` and the CLI only).

## Display environments — `display.set {environment}`

`Studio Soft` (default), `Studio Contrast`, `Overcast`, `Sunset`, `Warehouse`, `Night`, or `resource:<image>` (an imported
HDR/EXR panorama).

## Channels (21) — `textureSet.channel.add {channel}`, `layer.fill.set {channel}`, `tool.material {channel}`

`baseColor`, `metallic`, `roughness`, `normal`, `height`, `emissive`, `opacity`, `ambientOcclusion`, `specularLevel`,
`specular`, `glossiness`, `coatWeight`, `coatRoughness`, `sheenWeight`, `sheenColor`, `sheenRoughness`,
`anisotropyLevel`, `anisotropyAngle`, `scatterWeight`, `transmission`, `coatNormal`.

## Mesh maps (10) — `bake {maps}`, `viewport.view {mode: "map:<id>"}`, `textureSet.meshMap.set {map}`

`normal`, `worldNormal`, `id`, `ambientOcclusion`, `curvature`, `position`, `thickness`, `height`, `bentNormal`,
`opacity`. Default `bake` (no `maps`): normal, worldNormal, id, ambientOcclusion, curvature, position, thickness.
Curvature comes from the baked normal map unless `bake.settings {curvatureMethod: "mesh"}`.

## Mask generators — `effect.add.generator {generator}`

`edgeWear`, `dirt`, `thinAreas`, `curvature`, `ambientOcclusion`, `position`, `direction`; params `level`, `softness`,
`noise`, `invert`.

## Procedurals (23) — `layer.fill.set {channel, procedural}`, `effect.add.fill {procedural}`

`Clouds`, `Perlin` (Perlin noise), `Noise` (Fine noise), `Cells`, `Grunge`, `Scratches`, `Checker`, `Stripes`,
`Gradient`, `Wood` (Wood grain), `Bricks`, `Tiles`, `Weave` (Fabric weave), `Twill` (Twill weave), `Leather` (Leather
grain), `Hammered`, `Brushed` (Brushed lines), `Marble` (Marble veins), `Voronoi`, `Streaks`, `Smudges`
(Fingerprints), `Pores`, `Chips` (Paint chips). Params `scale`, `seed`, `contrast`, `balance`, `invert`, and the
`low` / `high` values the pattern maps to.

## Blend modes (32) — `layer.blend {channel?, mode, opacity?}`, `effect.set {blend}`

`Normal`, `Passthrough` (folders), `Disable`, `Replace`, `Multiply`, `Divide`, `Inverse divide`, `Darken (Min)`,
`Lighten (Max)`, `Linear dodge (Add)`, `Subtract`, `Inverse Subtract`, `Difference`, `Exclusion`, `Signed addition
(AddSub)`, `Overlay`, `Screen`, `Linear burn`, `Color burn`, `Color dodge`, `Soft light`, `Hard light`, `Vivid light`,
`Linear light`, `Pin light`, `Tint`, `Saturation`, `Color`, `Value`, `Normal map combine`, `Normal map detail`,
`Normal map inverse detail`. The variant name works too (`Lighten`, `LinearDodge`, `NormalMapDetail`).
