# FilmCraft effects and transitions

Generated from `effects.list {detail: true}` (FilmCraft 0.4.0, 303 entries). Apply a clip effect with `command_run effects.apply {clips: [id], effect: <id or name>}`, then set params with `effects.setParam {clip, effect: <id or index>, param, value, time?}`. Transitions go on with `sequence.applyVideoTransition {clip, edge, effect, frames}` / `sequence.applyAudioTransition {clip, effect, frames}`. Choice params take an index (options listed). `*` = not animatable. Format: `id` **Name**: `param` (default), …

## Video effects

### (built-in)

- `motion` **Motion**: `position` ([x,y]), `scale` (100), `scale_width` (100), `uniform_scale`* (true), `rotation` (0), `anchor` ([x,y]), `anti_flicker` (0)
- `opacity` **Opacity**: `opacity` (100), `blend`* (0: 0=Normal/1=Dissolve/2=Darken/3=Multiply/4=Color Burn/5=Linear Burn/6=Darker Color/7=Lighten/8=Screen/9=Color Dodge/10=Linear Dodge (Add)/11=Lighter Color/12=Ove)
- `graphic_shape` **Shape**: `name`* (""), `shape`* (0: 0=Rectangle/1=Ellipse/2=Polygon/3=Path), `size` ([400,200]), `sides` (6), `corner_radius` (0), `points`* ([]), `fill`* (true), `fill_color` (#ffffff), `stroke`* (false), `stroke_color` (#000000), `stroke_width` (4), `stroke_type`* (0: 0=Outer/1=Center/2=Inner), `stroke2`* (false), `stroke2_color` (#ffd933), `stroke2_width` (10), `stroke2_type`* (0: 0=Outer/1=Center/2=Inner), `background`* (false), `background_color` (#000000), `background_opacity` (75), `background_size` (12), `background_radius` (0), `shadow`* (false), `shadow_color` (#000000), `shadow_opacity` (75), `shadow_angle` (135), `shadow_distance` (10), `shadow_size` (0), `shadow_blur` (40), `position` ([x,y]), `anchor` ([0,0]), `scale` (100), `scale_width` (100), `uniform_scale`* (true), `rotation` (0), `opacity` (100)
- `graphic_text` **Text**: `name`* (""), `text` (""), `font`* ("Inter"), `font_style`* ("Regular"), `size` (100), `align`* (0: 0=Left/1=Center/2=Right/3=Justify), `tracking` (0), `kerning`* (true), `ligatures`* (true), `leading` (0), `baseline_shift` (0), `faux_bold`* (false), `faux_italic`* (false), `caps`* (0: 0=Normal/1=All Caps/2=Small Caps), `underline`* (false), `box_width` (0), `box_height` (0), `vertical`* (false), `fill`* (true), `fill_color` (#ffffff), `stroke`* (false), `stroke_color` (#000000), `stroke_width` (4), `stroke_type`* (0: 0=Outer/1=Center/2=Inner), `stroke2`* (false), `stroke2_color` (#ffd933), `stroke2_width` (10), `stroke2_type`* (0: 0=Outer/1=Center/2=Inner), `background`* (false), `background_color` (#000000), `background_opacity` (75), `background_size` (12), `background_radius` (0), `shadow`* (false), `shadow_color` (#000000), `shadow_opacity` (75), `shadow_angle` (135), `shadow_distance` (10), `shadow_size` (0), `shadow_blur` (40), `position` ([x,y]), `anchor` ([0,0]), `scale` (100), `scale_width` (100), `uniform_scale`* (true), `rotation` (0), `opacity` (100)
- `time_remap` **Time Remapping**: `speed` (100)

### Adjust

- `extract` **Extract**: `black` (0), `white` (255), `softness` (0), `invert`* (false)
- `levels` **Levels**: `in_black` (0), `in_white` (255), `out_black` (0), `out_white` (255), `gamma` (100)
- `lighting_effects` **Lighting Effects**: `l1_type`* (3: 0=None/1=Directional/2=Omni/3=Spotlight), `l1_color` (#ffffff), `l1_center` ([x,y]), `l1_major` (20), `l1_minor` (20), `l1_angle` (0), `l1_intensity` (20), `l1_focus` (50), `l2_type`* (0: 0=None/1=Directional/2=Omni/3=Spotlight), `l2_color` (#ffffff), `l2_center` ([x,y]), `l2_major` (20), `l2_minor` (20), `l2_angle` (0), `l2_intensity` (20), `l2_focus` (50), `l3_type`* (0: 0=None/1=Directional/2=Omni/3=Spotlight), `l3_color` (#ffffff), `l3_center` ([x,y]), `l3_major` (20), `l3_minor` (20), `l3_angle` (0), `l3_intensity` (20), `l3_focus` (50), `l4_type`* (0: 0=None/1=Directional/2=Omni/3=Spotlight), `l4_color` (#ffffff), `l4_center` ([x,y]), `l4_major` (20), `l4_minor` (20), `l4_angle` (0), `l4_intensity` (20), `l4_focus` (50), `l5_type`* (0: 0=None/1=Directional/2=Omni/3=Spotlight), `l5_color` (#ffffff), `l5_center` ([x,y]), `l5_major` (20), `l5_minor` (20), `l5_angle` (0), `l5_intensity` (20), `l5_focus` (50), `ambient_color` (#ffffff), `ambient` (20), `gloss` (0), `material` (0), `exposure` (0), `bump_height` (0), `white_high`* (true)
- `proc_amp` **ProcAmp**: `brightness` (0), `contrast` (100), `hue` (0), `saturation` (100)

### Blur & Sharpen

- `bokeh_blur` **Bokeh Blur**: `amount` (10), `shape`* (4: 0=Circle/1=Triangle/2=Square/3=Pentagon/4=Hexagon/5=Octagon), `rotation` (0), `highlight` (50), `threshold` (80)
- `channel_blur` **Channel Blur**: `red` (0), `green` (0), `blue` (0), `alpha` (0), `repeat_edge`* (false), `dimensions`* (0: 0=Horizontal and Vertical/1=Horizontal/2=Vertical)
- `compound_blur` **Compound Blur**: `layer`* (0: 0=None/1=Video 1/2=Video 2/3=Video 3/4=Video 4/5=Video 5/6=Video 6/7=Video 7/8=Video 8), `max` (20), `stretch`* (true), `invert`* (false)
- `directional_blur` **Directional Blur**: `direction` (0), `length` (0)
- `focus_blur` **Focus Blur**: `shape`* (0: 0=Radial/1=Linear), `center` ([x,y]), `angle` (0), `size` (200), `feather` (200), `amount` (20), `show`* (false)
- `gaussian_blur` **Gaussian Blur**: `blurriness` (0), `dimensions`* (0: 0=Horizontal and Vertical/1=Horizontal/2=Vertical), `repeat_edge`* (false)
- `reduce_interlace_flicker` **Reduce Interlace Flicker**: `softness` (0)
- `sharpen` **Sharpen**: `amount` (0)
- `unsharp_mask` **Unsharp Mask**: `amount` (50), `radius` (1), `threshold` (0)

### Color Correction

- `asc_cdl` **ASC CDL**: `r_slope` (1), `r_offset` (0), `r_power` (1), `g_slope` (1), `g_offset` (0), `g_power` (1), `b_slope` (1), `b_offset` (0), `b_power` (1), `saturation` (1)
- `brightness_contrast` **Brightness & Contrast**: `brightness` (0), `contrast` (0)
- `lumetri` **Lumetri Color**: `basic_on`* (true), `input_lut`* (""), `temperature` (0), `tint` (0), `exposure` (0), `contrast` (0), `highlights` (0), `shadows` (0), `whites` (0), `blacks` (0), `saturation` (100), `hdr_white` (1000), `hdr_specular` (0), `creative_on`* (true), `look`* (0: 0=None/1=Teal & Orange/2=Warm Film/3=Cool Blue/4=Bleach Bypass/5=Faded Matte/6=Monochrome/7=Golden Hour/8=Night), `look_lut`* (""), `look_intensity` (100), `faded_film` (0), `sharpen` (0), `vibrance` (0), `creative_sat` (100), `shadow_tint` (#808080), `highlight_tint` (#808080), `curves_on`* (true), `curve_luma`* ([[0.0, 0.0], [1.0, 1.0]]), `curve_red`* ([[0.0, 0.0], [1.0, 1.0]]), `curve_green`* ([[0.0, 0.0], [1.0, 1.0]]), `curve_blue`* ([[0.0, 0.0], [1.0, 1.0]]), `hue_vs_sat`* ([]), `hue_vs_hue`* ([]), `hue_vs_luma`* ([]), `luma_vs_sat`* ([]), `sat_vs_sat`* ([]), `curves_hdr_range` (1000), `wheels_on`* (true), `wheel_shadows` ([0,0]), `wheel_shadows_l` (0), `wheel_midtones` ([0,0]), `wheel_midtones_l` (0), `wheel_highlights` ([0,0]), `wheel_highlights_l` (0), `hsl_on`* (false), `hsl_hue` (0), `hsl_hue_range` (30), `hsl_sat_min` (10), `hsl_luma_min` (5), `hsl_luma_max` (95), `hsl_soft` (20), `hsl_show_mask`* (0: 0=Off/1=Color/Gray/2=Color/Black/3=White/Black), `hsl_denoise` (0), `hsl_blur` (0), `hsl_temp` (0), `hsl_tint` (0), `hsl_sat` (100), `hsl_hue_shift` (0), `vignette_on`* (true), `vignette_amount` (0), `vignette_midpoint` (50), `vignette_roundness` (0), `vignette_feather` (50)
- `tint` **Tint**: `black` (#000000), `white` (#ffffff), `amount` (100)
- `video_limiter` **Video Limiter**: `clip_level`* (0: 0=100 IRE/1=101 IRE/2=102 IRE/3=103 IRE/4=104 IRE/5=105 IRE/6=106 IRE/7=107 IRE/8=108 IRE/9=109 IRE), `compression`* (1: 0=None/1=3%/2=5%/3=10%/4=20%), `axis`* (3: 0=Luma/1=Chroma/2=Luma and Chroma/3=Smart Limit), `gamut_warning`* (false), `warning_color` (#ff0000)
- `vignette` **Vignette**: `amount` (-50), `midpoint` (50), `roundness` (0), `feather` (50), `color` (#000000)

### Distort

- `corner_pin` **Corner Pin**: `upper_left` ([x,y]), `upper_right` ([x,y]), `lower_left` ([x,y]), `lower_right` ([x,y])
- `lens_distortion` **Lens Distortion**: `curvature` (0), `v_decentering` (0), `h_decentering` (0)
- `magnify` **Magnify**: `shape`* (0: 0=Circle/1=Square), `center` ([x,y]), `magnification` (200), `size` (100), `feather` (0), `opacity` (100), `mode`* (0: 0=Normal/1=Add/2=Screen/3=Multiply/4=Overlay)
- `mirror` **Mirror**: `center` ([x,y]), `angle` (0)
- `spherize` **Spherize**: `radius` (0), `center` ([x,y])
- `turbulent_displace` **Turbulent Displace**: `displacement`* (0: 0=Turbulent/1=Bulge/2=Twist/3=Turbulent Smoother/4=Bulge Smoother/5=Twist Smoother/6=Vertical Displacement/7=Horizontal Displacement/8=Cross Displacement), `amount` (50), `size` (100), `offset` ([x,y]), `complexity` (1), `evolution` (0), `cycle`* (false), `cycle_revs` (1), `seed` (0), `pinning`* (1: 0=None/1=Pin All/2=Pin Horizontal/3=Pin Vertical), `antialias`* (0: 0=Low/1=High)
- `twirl` **Twirl**: `angle` (50), `radius` (30), `center` ([x,y])
- `warp_stabilizer` **Warp Stabilizer**: `result`* (0: 0=Smooth Motion/1=No Motion), `smoothness` (50), `method`* (1: 0=Position/1=Position, Scale, Rotation/2=Perspective/3=Subspace Warp), `preserve_scale`* (false), `framing`* (2: 0=Stabilize Only/1=Stabilize, Crop/2=Stabilize, Crop, Auto-scale/3=Stabilize, Synthesize Edges), `max_scale` (150), `action_safe` (0), `additional_scale` (100), `detailed`* (false), `crop_less` (50)
- `wave_warp` **Wave Warp**: `height` (10), `width` (40), `direction` (90), `speed` (1)

### Generate

- `four_color_gradient` **4-Color Gradient**: `c1` (#ffff00), `c2` (#00ff00), `c3` (#ff00ff), `c4` (#0000ff), `blend` (100), `opacity` (100)
- `gradient` **Gradient**: `start` ([x,y]), `start_color` (#000000), `end` ([x,y]), `end_color` (#ffffff), `shape`* (0: 0=Linear/1=Radial/2=Reflected/3=Diamond), `scatter` (0), `midpoint` (50), `blend` (0)

### Image Control

- `black_white` **Black & White**
- `channel_mix` **Channel Mix**: `rr` (100), `rg` (0), `rb` (0), `rc` (0), `gr` (0), `gg` (100), `gb` (0), `gc` (0), `br` (0), `bg` (0), `bb` (100), `bc` (0), `monochrome`* (false)
- `color_pass` **Color Pass**: `color` (#ff0000), `similarity` (10), `reverse`* (false)
- `color_replace` **Color Replace**: `similarity` (10), `solid`* (false), `target` (#ff0000), `replace` (#0000ff)
- `gamma_correction` **Gamma Correction**: `gamma` (10)
- `invert` **Invert**: `channel`* (0: 0=RGB/1=Red/2=Green/3=Blue/4=Alpha), `blend` (0)
- `rounded_crop` **Rounded Crop**: `left` (0), `top` (0), `right` (0), `bottom` (0), `radius` (40), `feather` (0), `border` (0), `border_color` (#ffffff)

### Immersive Video

- `vr_blur` **VR Blur**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `blurriness` (0)
- `vr_chromatic_aberrations` **VR Chromatic Aberrations**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `red` (0), `green` (0), `blue` (0), `center_x` (0), `center_y` (0), `falloff` (50), `inverse`* (false)
- `vr_color_gradients` **VR Color Gradients**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `c1` (#ff4040), `p1_lon` (-120), `p1_lat` (20), `c2` (#40ff66), `p2_lon` (0), `p2_lat` (-20), `c3` (#4d66ff), `p3_lon` (120), `p3_lat` (20), `blend` (50), `opacity` (100), `mode`* (0: 0=Normal/1=Add/2=Screen/3=Multiply/4=Overlay)
- `vr_denoise` **VR De-Noise**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `amount` (0), `noise_type`* (0: 0=Fast/1=Slow), `show_noise`* (false)
- `vr_digital_glitch` **VR Digital Glitch**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `amplitude` (0), `distortion` (20), `rate` (10), `color` (50), `scanlines` (0), `seed` (0)
- `vr_fractal_noise` **VR Fractal Noise**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `fractal_type`* (0: 0=Basic/1=Turbulent Smooth/2=Turbulent Sharp), `invert`* (false), `contrast` (100), `brightness` (0), `scale` (100), `complexity` (6), `evolution` (0), `opacity` (100), `mode`* (0: 0=Normal/1=Add/2=Screen/3=Multiply/4=Overlay)
- `vr_glow` **VR Glow**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `threshold` (70), `radius` (30), `brightness` (1), `saturation` (1), `use_tint`* (false), `tint` (#ffffff)
- `vr_plane_to_sphere` **VR Plane to Sphere**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `scale` (60), `pan` (0), `tilt` (0), `roll` (0), `feather` (0)
- `vr_projection` **VR Projection**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `fov` (360), `tilt` (0), `pan` (0), `roll` (0), `stretch`* (true)
- `vr_rotate_sphere` **VR Rotate Sphere**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `tilt` (0), `pan` (0), `roll` (0)
- `vr_sharpen` **VR Sharpen**: `frame_layout`* (0: 0=Monoscopic/1=Stereoscopic - Over/Under/2=Stereoscopic - Side by Side), `amount` (0)

### Keying

- `alpha_adjust` **Alpha Adjust**: `opacity` (100), `ignore`* (false), `invert`* (false), `mask_only`* (false)
- `color_key` **Color Key**: `color` (#0000ff), `tolerance` (0), `thin` (0), `feather` (0)
- `logo_cutout` **Logo Cutout**: `background`* (0: 0=White/1=Black/2=Custom Color), `color` (#ffffff), `threshold` (5), `softness` (10), `unmultiply`* (true), `invert`* (false)
- `luma_key` **Luma Key**: `threshold` (0), `cutoff` (0)
- `track_matte` **Track Matte Key**: `matte`* (0: 0=None/1=Video 1/2=Video 2/3=Video 3/4=Video 4/5=Video 5/6=Video 6/7=Video 7/8=Video 8), `composite`* (0: 0=Matte Alpha/1=Matte Luma), `reverse`* (false)
- `ultra_key` **Ultra Key**: `key_color` (#00cc33), `output`* (0: 0=Composite/1=Alpha Channel/2=Color Channel), `setting`* (0: 0=Default/1=Relaxed/2=Aggressive/3=Custom), `transparency` (45), `highlight` (10), `shadow` (50), `tolerance` (50), `pedestal` (10), `choke` (0), `soften` (0), `spill` (50), `contrast` (0), `mid_point` (50), `desaturate` (25), `range` (50), `spill_luma` (50), `cc_saturation` (100), `cc_hue` (0), `cc_luminance` (100)

### Lights & Glows

- `echo_glow` **Echo Glow**: `threshold` (60), `echoes` (4), `radius` (12), `spread` (1.8), `intensity` (100), `decay` (50), `color` (#ffd999)
- `edge_glow` **Edge Glow**: `threshold` (20), `width` (2), `radius` (10), `intensity` (150), `color` (#4dccff), `only`* (false)
- `glint` **Glint**: `threshold` (75), `rays`* (1: 0=2/1=4/2=6/3=8), `length` (60), `rotation` (45), `intensity` (100), `color` (#ffffff), `colorize` (0)
- `lens_flare` **Lens Flare**: `center` ([x,y]), `brightness` (100), `blend` (0), `lens_type`* (0: 0=50-300mm Zoom/1=35mm Prime/2=105mm Prime/3=Anamorphic), `color` (#ffe5bf), `size` (100), `ghosts` (3)
- `light_leaks` **Light Leaks**: `c1` (#ff731a), `c2` (#ff2659), `intensity` (70), `scale` (100), `direction` (30), `speed` (1), `seed` (0), `mode`* (0: 0=Screen/1=Add/2=Overlay)
- `rgb_split` **RGB Split**: `mode`* (0: 0=Linear/1=Radial), `amount` (10), `angle` (0), `center` ([x,y]), `blend` (0)
- `volumetric_rays` **Volumetric Rays**: `center` ([x,y]), `threshold` (60), `length` (50), `intensity` (100), `color` (#fff2cc), `only`* (false)
- `wonder_glow` **Wonder Glow**: `threshold` (60), `radius` (25), `intensity` (100), `saturation` (100), `use_color`* (false), `color` (#ffcc80), `mode`* (0: 0=Add/1=Screen)

### Noise & Grain

- `noise` **Noise**: `amount` (0), `color`* (true), `clip`* (true), `grain_size` (1)

### Obsolete

- `bevel_alpha` **Bevel Alpha**: `thickness` (2), `angle` (-60), `color` (#ffffff), `intensity` (40)
- `cell_pattern` **Cell Pattern**: `pattern`* (0: 0=Bubbles/1=Crystals/2=Plates/3=Static Plates/4=Crystallize/5=Pillow/6=Mixed Crystals/7=Tubular), `invert`* (false), `contrast` (100), `overflow`* (0: 0=Clip/1=Soft Clamp/2=Wrap Back), `disperse` (1), `size` (60), `offset` ([0,0]), `evolution` (0), `seed` (0)
- `change_to_color` **Change to Color**: `from` (#ff0000), `to` (#0000ff), `hue_tol` (5), `softness` (50)
- `checkerboard` **Checkerboard**: `anchor` ([x,y]), `width` (64), `height` (64), `square`* (true), `feather` (0), `color` (#ffffff), `opacity` (100), `mode`* (0: 0=None/1=Normal/2=Add/3=Multiply/4=Screen/5=Overlay)
- `circle` **Circle**: `center` ([x,y]), `radius` (75), `color` (#ffffff), `opacity` (100)
- `clip_name` **Clip Name**: `position` ([x,y]), `size` (15)
- `color_balance` **Color Balance**: `shadow_r` (0), `shadow_g` (0), `shadow_b` (0), `mid_r` (0), `mid_g` (0), `mid_b` (0), `hi_r` (0), `hi_g` (0), `hi_b` (0), `preserve`* (false)
- `echo` **Echo**: `time` (-0.033), `count` (1), `start` (1), `decay` (1), `operator`* (0: 0=Add/1=Maximum/2=Minimum/3=Screen/4=Composite In Back/5=Composite In Front/6=Blend)
- `ellipse` **Ellipse**: `center` ([x,y]), `width` (200), `height` (200), `thickness` (8), `softness` (15), `inside` (#ffffff), `outside` (#0080ff), `composite`* (false)
- `emboss` **Emboss**: `direction` (45), `relief` (1.8), `contrast` (100), `blend` (0)
- `grid` **Grid**: `size` (60), `border` (2), `color` (#ffffff), `opacity` (100)
- `leave_color` **Leave Color**: `amount` (0), `color` (#ff0000), `tolerance` (15), `softness` (0)
- `lightning` **Lightning**: `start` ([x,y]), `end` ([x,y]), `segments` (7), `amplitude` (10), `detail` (2), `detail_amplitude` (0.3), `branching` (0.3), `speed` (10), `width` (10), `core` (0.4), `outside` (#594dff), `inside` (#ffffff), `seed` (0), `mode`* (1: 0=Normal/1=Add/2=Screen/3=Multiply/4=Overlay)
- `median` **Median**: `radius` (0)
- `paint_bucket` **Paint Bucket**: `point` ([x,y]), `selector`* (0: 0=Color & Alpha/1=Straight Color/2=Transparency/3=Opacity), `tolerance` (10), `invert`* (false), `color` (#ff0000), `opacity` (100), `mode`* (0: 0=Normal/1=Behind/2=Add/3=Multiply/4=Screen)
- `timecode` **Timecode**: `position` ([x,y]), `size` (15), `opacity` (100)
- `write_on` **Write-on**: `brush` ([x,y]), `color` (#ffffff), `size` (8), `hardness` (75), `opacity` (100), `stroke_length` (0), `spacing` (0.01), `style`* (0: 0=On Original Image/1=On Transparent/2=Reveal Original Image)

### Perspective

- `basic_3d` **Basic 3D**: `swivel` (0), `tilt` (0), `distance` (0)
- `drop_shadow` **Drop Shadow**: `color` (#000000), `opacity` (50), `direction` (135), `distance` (5), `softness` (0), `only`* (false)
- `long_shadow` **Long Shadow**: `angle` (135), `length` (100), `color` (#000000), `opacity` (50), `fade`* (true), `only`* (false)

### Stylize

- `brush_strokes` **Brush Strokes**: `angle` (135), `size` (2), `length` (10), `density` (1), `randomness` (1), `surface`* (0: 0=Paint On Original Image/1=Paint On Transparent/2=Paint On White/3=Paint On Black), `blend` (0)
- `color_emboss` **Color Emboss**: `direction` (45), `relief` (1), `contrast` (100), `blend` (0)
- `find_edges` **Find Edges**: `invert`* (false), `blend` (0)
- `mosaic` **Mosaic**: `horizontal` (10), `vertical` (10), `sharp`* (false), `softness` (0)
- `posterize` **Posterize**: `levels` (7)
- `roughen_edges` **Roughen Edges**: `edge_type`* (0: 0=Roughen/1=Roughen Color/2=Cut/3=Spiky/4=Rusty/5=Rusty Color/6=Photocopy/7=Photocopy Color), `edge_color` (#cc8033), `border` (8), `sharpness` (1), `influence` (1), `scale` (100), `stretch` (0), `offset` ([0,0]), `complexity` (2), `evolution` (0), `seed` (0)
- `strobe` **Strobe Light**: `color` (#ffffff), `blend` (0), `duration` (0.05), `period` (0.5)

### Time

- `posterize_time` **Posterize Time**: `rate` (12)

### Transform

- `rotate_3d` **3D Rotate**: `rot_x` (0), `rot_y` (0), `rot_z` (0), `perspective` (50), `z` (0), `hide_back`* (false)
- `auto_reframe` **Auto Reframe**: `preset`* (1: 0=Slower Motion/1=Default/2=Faster Motion), `offset` ([0,0]), `zoom` (100), `aspect`* (0: 0=Sequence/1=Vertical 9:16/2=Square 1:1/3=Vertical 4:5/4=Horizontal 16:9)
- `camera_shake` **Camera Shake**: `amount` (20), `rotation` (1), `zoom` (5), `frequency` (4), `complexity` (3), `motion_blur` (0), `seed` (0)
- `grow` **Grow**: `from` (100), `to` (120), `center` ([x,y]), `easing`* (0: 0=Linear/1=Ease In/2=Ease Out/3=Ease In and Out)
- `horizontal_flip` **Horizontal Flip**
- `move` **Move**: `from` ([-100,0]), `to` ([0,0]), `easing`* (3: 0=Linear/1=Ease In/2=Ease Out/3=Ease In and Out), `motion_blur` (0)
- `offset` **Offset**: `shift` ([x,y]), `blend` (0)
- `shrink` **Shrink**: `from` (120), `to` (100), `center` ([x,y]), `easing`* (0: 0=Linear/1=Ease In/2=Ease Out/3=Ease In and Out)
- `spacer` **Spacer**: `left` (40), `top` (40), `right` (40), `bottom` (40), `uniform`* (true), `radius` (0), `fill`* (false), `color` (#000000)
- `spin` **Spin**: `amount` (360), `center` ([x,y]), `easing`* (3: 0=Linear/1=Ease In/2=Ease Out/3=Ease In and Out), `scale` (100)
- `transform` **Transform**: `anchor` ([x,y]), `position` ([x,y]), `uniform_scale`* (true), `scale_height` (100), `scale_width` (100), `skew` (0), `skew_axis` (0), `rotation` (0), `opacity` (100), `shutter_angle` (0)
- `vertical_flip` **Vertical Flip**
- `wiggle` **Wiggle**: `frequency` (2), `amount` (20), `rotation` (0), `scale` (0), `dimensions`* (0: 0=Horizontal and Vertical/1=Horizontal/2=Vertical), `seed` (0)

### Utility

- `auto_align` **Auto Align**: `horizontal`* (2: 0=None/1=Left/2=Center/3=Right), `vertical`* (2: 0=None/1=Top/2=Center/3=Bottom), `margin_x` (0), `margin_y` (0)
- `cineon_converter` **Cineon Converter**: `conversion`* (0: 0=Log to Linear/1=Linear to Log/2=Log to Log), `black10` (95), `black_internal` (0), `white10` (685), `white_internal` (255), `gamma` (1.7), `rolloff` (20)
- `clone` **Clone**: `columns` (2), `rows` (1), `gap` (0), `mirror`* (false)
- `simple_text` **Simple Text**: `text`* ("Simple Text"), `position` ([x,y]), `size` (64), `font`* (0: 0=Inter/1=JetBrains Mono), `alignment`* (1: 0=Left/1=Center/2=Right), `color` (#ffffff), `bg_opacity` (0)
- `stroke` **Stroke**: `color` (#ffffff), `width` (4), `position`* (0: 0=Outside/1=Center/2=Inside), `opacity` (100), `only`* (false)

### Video

- `metadata_burnin` **Metadata & Timecode Burn-in**: `source`* (0: 0=Sequence Timecode/1=Media Timecode/2=Clip Name/3=File Name/4=Frame Count/5=Sequence Name), `position` ([x,y]), `alignment`* (0: 0=Bottom Center/1=Bottom Left/2=Bottom Right/3=Top Center/4=Top Left/5=Top Right/6=Custom), `size` (6), `color` (#ffffff), `opacity` (60), `prefix`* ("")

### Video Effects

- `alpha_glow` **Alpha Glow**: `glow` (30), `brightness` (252), `start_color` (#ffffff), `end_color` (#ffffff), `use_end`* (false), `fade_out`* (true)
- `block_dissolve` **Block Dissolve**: `completion` (0), `block_w` (1), `block_h` (1), `feather` (0), `soft`* (true)
- `camera_blur` **Camera Blur**: `percent` (0)
- `crop` **Crop**: `left` (0), `top` (0), `right` (0), `bottom` (0), `zoom`* (false), `feather` (0)
- `directional_blur_legacy` **Directional Blur (Legacy)**: `direction` (0), `length` (0)
- `edge_feather` **Edge Feather**: `amount` (0)
- `gaussian_blur_legacy` **Gaussian Blur (Legacy)**: `blurriness` (0), `dimensions`* (0: 0=Horizontal and Vertical/1=Horizontal/2=Vertical)
- `gradient_wipe_legacy` **Gradient Wipe (Legacy)**: `completion` (0), `softness` (0), `layer`* (0: 0=None/1=Video 1/2=Video 2/3=Video 3/4=Video 4/5=Video 5/6=Video 6/7=Video 7/8=Video 8), `placement`* (2: 0=Tile Gradient/1=Center Gradient/2=Stretch Gradient to Fit), `invert`* (false)
- `linear_wipe_legacy` **Linear Wipe (Legacy)**: `completion` (0), `angle` (90), `feather` (0)
- `magnify_legacy` **Magnify (Legacy)**: `shape`* (0: 0=Circle/1=Square), `center` ([x,y]), `magnification` (200), `size` (100), `feather` (0), `opacity` (100), `mode`* (0: 0=Normal/1=Add/2=Screen/3=Multiply/4=Overlay)
- `mosaic_legacy` **Mosaic (Legacy)**: `horizontal` (10), `vertical` (10), `sharp`* (false)
- `noise_legacy` **Noise (Legacy)**: `amount` (0), `color`* (true), `clip`* (true)
- `ramp` **Ramp**: `start` ([x,y]), `start_color` (#000000), `end` ([x,y]), `end_color` (#ffffff), `shape`* (0: 0=Linear Ramp/1=Radial Ramp), `blend` (0)
- `replicate` **Replicate**: `count` (2)
- `twirl_legacy` **Twirl (Legacy)**: `angle` (50), `radius` (30), `center` ([x,y])

## Video transitions

### Animation

- `block_motion` **Block Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `blocks`* (6), `motion_blur`* (50)
- `flip_motion` **Flip Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `perspective`* (50), `motion_blur`* (50)
- `fold_motion` **Fold Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `perspective`* (50)
- `pop_motion` **Pop Motion**: `overshoot`* (20), `motion_blur`* (50)
- `pull_motion` **Pull Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `motion_blur`* (50)
- `spin_motion` **Spin Motion**: `rotation`* (360), `spin`* (0: 0=Clockwise/1=Counter-clockwise), `motion_blur`* (50)
- `spring_motion` **Spring Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `bounce`* (40), `motion_blur`* (50)
- `travel_motion` **Travel Motion**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `zoom`* (40), `motion_blur`* (50)

### Dissolve

- `additive_dissolve` **Additive Dissolve**
- `blur_dissolve` **Blur Dissolve**: `blur`* (40)
- `burn_alpha` **Burn Alpha**: `burn_color`* (#ff731a), `softness`* (25), `seed`* (1)
- `cross_dissolve` **Cross Dissolve**
- `dip_to_black` **Dip to Black**
- `dip_to_color` **Dip to Color**: `color`* (#d93333), `hold`* (0)
- `dip_to_white` **Dip to White**
- `film_dissolve` **Film Dissolve**
- `luma_fade` **Luma Fade**: `source`* (0: 0=Outgoing/1=Incoming), `softness`* (20), `invert`* (false)
- `morph_cut` **Morph Cut**
- `mosaic_transition` **Mosaic**: `block_size`* (64), `dissolve`* (true)

### Grunge & Distort

- `chaos` **Chaos**: `amount`* (60), `seed`* (1)
- `earthquake` **Earthquake**: `shake`* (40), `seed`* (1), `motion_blur`* (50)
- `flicker` **Flicker**: `flickers`* (8), `seed`* (1)
- `glass` **Glass**: `cell_size`* (90), `refraction`* (40), `seed`* (1)
- `glitch` **Glitch**: `amount`* (60), `seed`* (1)
- `grunge` **Grunge**: `scale`* (120), `edge_color`* (#382414), `edge_width`* (12), `seed`* (1)
- `kaleidoscope` **Kaleidoscope**: `segments`* (6), `zoom`* (30)
- `liquid_distortion` **Liquid Distortion**: `amount`* (60), `scale`* (200), `seed`* (1)
- `tv_power` **TV Power**: `glow_color`* (#d9f2ff), `line`* (4)
- `vhs_damage` **VHS Damage**: `amount`* (60), `seed`* (1)

### Immersive Video

- `vr_chroma_leaks` **VR Chroma Leaks**: `amount`* (70), `seed`* (1)
- `vr_gradient_wipe` **VR Gradient Wipe**: `softness`* (20), `invert`* (false)
- `vr_iris_wipe` **VR Iris Wipe**: `center`* ([x,y]), `feather`* (8), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `vr_light_leaks` **VR Light Leaks**: `amount`* (70), `seed`* (1)
- `vr_light_rays` **VR Light Rays**: `center`* ([x,y]), `amount`* (70)
- `vr_mobius_zoom` **VR Mobius Zoom**: `zoom`* (60), `twist`* (180)
- `vr_random_blocks` **VR Random Blocks**: `block_size`* (80), `softness`* (10), `seed`* (1)
- `vr_spherical_blur` **VR Spherical Blur**: `blur`* (60)

### Lights & Blurs

- `burn_chroma` **Burn Chroma**: `amount`* (80)
- `chroma_leak` **Chroma Leak**: `amount`* (70), `seed`* (1)
- `cross_zoom` **Cross Zoom**: `center`* ([x,y]), `strength`* (60)
- `directional_blur_transition` **Directional Blur**: `angle`* (90), `blur`* (160)
- `flare` **Flare**: `color`* (#ffcc8c), `amount`* (80), `angle`* (20)
- `flash` **Flash**: `color`* (#ffffff), `intensity`* (100)
- `glow` **Glow**: `radius`* (40), `intensity`* (80)
- `lens_blur` **Lens Blur**: `radius`* (30)
- `light_leak` **Light Leak**: `color`* (#ff8c33), `amount`* (80), `seed`* (1)
- `light_sweep` **Light Sweep**: `angle`* (70), `width`* (160), `color`* (#fff7e5), `amount`* (80)
- `phosphor` **Phosphor**: `color`* (#8cff99), `decay`* (50)
- `radial_blur` **Radial Blur**: `center`* ([x,y]), `angle`* (40)
- `ray` **Ray**: `center`* ([x,y]), `amount`* (80), `length`* (50)
- `solarize` **Solarize**: `amount`* (100)
- `stripe` **Stripe**: `stripes`* (8), `angle`* (30), `color`* (#ffffff)
- `zoom_blur` **Zoom Blur**: `center`* ([x,y]), `strength`* (50)

### Slide

- `roll_3d` **3D Roll**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `perspective`* (50)
- `film_roll` **Film Roll**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `gap`* (40), `gap_color`* (#080808), `motion_blur`* (50)
- `push` **Push**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `motion_blur`* (50)
- `roll` **Roll**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `motion_blur`* (50)
- `slide` **Slide**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `motion_blur`* (50)
- `split` **Split**: `orientation`* (0: 0=Horizontal/1=Vertical), `motion_blur`* (50)
- `stretch` **Stretch**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)
- `whip` **Whip**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `blur`* (80)

### Smart Tools

- `motion_camera` **Motion Camera**: `zoom`* (40), `rotation`* (8), `motion_blur`* (50)
- `motion_tween` **Motion Tween**: `scale`* (15)
- `shape_dissolve` **Shape Dissolve**: `shape`* (0: 0=Circle/1=Square/2=Diamond/3=Star/4=Heart/5=Triangle/6=Hexagon), `size`* (120), `softness`* (2), `rotation`* (0), `order`* (0: 0=Random/1=Left to Right/2=Center Out), `seed`* (1)
- `shape_flow` **Shape Flow**: `shape`* (0: 0=Circle/1=Square/2=Diamond/3=Star/4=Heart/5=Triangle/6=Hexagon), `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `softness`* (4)

### Text

- `text_animator` **Text Animator**: `columns`* (24), `rows`* (10)
- `typewriter` **Typewriter**: `columns`* (32), `rows`* (12), `cursor`* (true)

### Transformers

- `spin_3d` **3D Spin**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `perspective`* (50)
- `spinback_3d` **3D Spinback**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `depth`* (60)
- `frame` **Frame**: `frame_width`* (24), `frame_color`* (#ffffff), `scale`* (60)
- `louver` **Louver**: `slats`* (8), `orientation`* (0: 0=Horizontal/1=Vertical)
- `mirror_transition` **Mirror**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)
- `page_peel` **Page Peel**: `corner`* (2: 0=Top Left/1=Top Right/2=Bottom Right/3=Bottom Left), `radius`* (60), `shadow`* (true)
- `slice` **Slice**: `slices`* (8), `angle`* (20), `motion_blur`* (50)
- `wave` **Wave**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `amplitude`* (60), `wavelength`* (300)

### Video Transitions

- `additive_dissolve_legacy` **Additive Dissolve (Legacy)**
- `band_slide` **Band Slide**
- `barn_doors` **Barn Doors**: `orientation`* (1: 0=Horizontal/1=Vertical), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `center_split` **Center Split**
- `checker_wipe` **Checker Wipe**
- `clock_wipe_legacy` **Clock Wipe (Legacy)**
- `cross_dissolve_legacy` **Cross Dissolve (Legacy)**
- `cross_zoom_legacy` **Cross Zoom (Legacy)**
- `cube_spin` **Cube Spin**
- `dip_to_black_legacy` **Dip to Black (Legacy)**
- `dip_to_white_legacy` **Dip to White (Legacy)**
- `film_dissolve_legacy` **Film Dissolve (Legacy)**
- `flip_over` **Flip Over**
- `gradient_wipe` **Gradient Wipe**: `softness`* (10)
- `inset` **Inset**: `corner`* (0: 0=Top Left/1=Top Right/2=Bottom Right/3=Bottom Left), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `iris_box` **Iris Box**: `center`* ([x,y]), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `iris_cross` **Iris Cross**: `center`* ([x,y]), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `iris_diamond` **Iris Diamond**: `center`* ([x,y]), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `iris_round` **Iris Round**: `center`* ([x,y]), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `non_additive_dissolve` **Non-Additive Dissolve**
- `page_turn` **Page Turn**
- `push_legacy` **Push (Legacy)**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)
- `radial_wipe_legacy` **Radial Wipe (Legacy)**
- `slide_legacy` **Slide (Legacy)**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)
- `split_legacy` **Split (Legacy)**
- `venetian_blinds` **Venetian Blinds**
- `whip_legacy` **Whip (Legacy)**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)
- `wipe` **Wipe**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West)

### Wipe

- `clock_wipe` **Clock Wipe**: `center`* ([x,y]), `start`* (0), `feather`* (0), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `linear_wipe` **Linear Wipe**: `angle`* (90), `feather`* (0), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `neon_wipe` **Neon Wipe**: `angle`* (90), `color`* (#33e5ff), `glow`* (40), `amount`* (100)
- `panel_wipe` **Panel Wipe**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `panels`* (6), `feather`* (0), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `plateau_wipe` **Plateau Wipe**: `angle`* (90), `plateaus`* (5), `feather`* (4), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `radial_wipe` **Radial Wipe**: `corner`* (0: 0=Top Left/1=Top Right/2=Bottom Right/3=Bottom Left), `feather`* (0), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `soft_wipe` **Soft Wipe**: `angle`* (90), `feather`* (300)
- `star_wipe` **Star Wipe**: `center`* ([x,y]), `points`* (5), `inner`* (45), `rotation`* (0), `feather`* (0), `border_width`* (0), `border_color`* (#000000), `antialias`* (1: 0=Off/1=Low/2=Medium/3=High)
- `stretch_wipe` **Stretch Wipe**: `direction`* (3: 0=From North/1=From East/2=From South/3=From West), `stretch`* (200)

## Audio effects

### (built-in)

- `balance_a` **Balance**: `balance` (0)
- `channel_volume` **Channel Volume**: `bypass`* (false), `left` (0), `right` (0)
- `mute` **Mute**: `mute` (false)
- `panner` **Panner**: `balance` (0)
- `volume` **Volume**: `bypass`* (false), `level` (0)
- `volume_a` **Volume**: `bypass`* (false), `level` (0)

### Amplitude and Compression

- `amplify` **Amplify**: `gain` (0)
- `channel_mixer_a` **Channel Mixer**: `l_from_l` (100), `l_from_r` (0), `invert_l`* (false), `r_from_l` (0), `r_from_r` (100), `invert_r`* (false)
- `channel_volume_a` **Channel Volume**: `left` (0), `right` (0)
- `deesser` **DeEsser**: `frequency` (6000), `threshold` (-12), `reduction` (8)
- `dynamics_rack` **Dynamics**: `gate_on`* (false), `gate_threshold` (-50), `gate_attack` (2), `gate_release` (100), `gate_hold` (50), `comp_on`* (true), `comp_threshold` (-20), `comp_ratio` (2), `comp_attack` (10), `comp_release` (100), `comp_auto`* (false), `comp_makeup` (0), `exp_on`* (false), `exp_threshold` (-60), `exp_ratio` (2), `lim_on`* (false), `lim_threshold` (-1), `lim_release` (50), `soft_clip`* (false), `output` (0)
- `dynamics` **Dynamics Processing**: `threshold` (-20), `ratio` (4), `attack` (10), `release` (100)
- `hard_limiter` **Hard Limiter**: `max` (-0.1), `boost` (0), `lookahead` (7), `release` (100)
- `multiband_compressor` **Multiband Compressor**: `xo1` (120), `xo2` (2000), `xo3` (10000), `b1_threshold` (-18), `b1_ratio` (3), `b1_attack` (10), `b1_release` (100), `b1_gain` (0), `b1_solo`* (false), `b1_bypass`* (false), `b2_threshold` (-18), `b2_ratio` (3), `b2_attack` (10), `b2_release` (100), `b2_gain` (0), `b2_solo`* (false), `b2_bypass`* (false), `b3_threshold` (-18), `b3_ratio` (3), `b3_attack` (10), `b3_release` (100), `b3_gain` (0), `b3_solo`* (false), `b3_bypass`* (false), `b4_threshold` (-18), `b4_ratio` (3), `b4_attack` (10), `b4_release` (100), `b4_gain` (0), `b4_solo`* (false), `b4_bypass`* (false), `output` (0), `lim_on`* (false), `lim_threshold` (-0.1), `lim_release` (50), `link`* (true)
- `single_band_compressor` **Single-band Compressor**: `threshold` (-20), `ratio` (4), `attack` (10), `release` (100), `output` (0)
- `tube_compressor` **Tube-modeled Compressor**: `threshold` (-20), `ratio` (4), `attack` (10), `release` (100), `output` (0)

### Delay and Echo

- `analog_delay` **Analog Delay**: `mode`* (0: 0=Tape/1=Tape/Tube/2=Analog), `dry` (100), `wet` (40), `delay` (250), `feedback` (40), `trash` (0), `spread` (0)
- `delay` **Delay**: `delay` (1), `feedback` (0), `mix` (50)
- `multitap_delay` **Multitap Delay**: `delay1` (250), `feedback1` (0), `level1` (-6), `delay2` (500), `feedback2` (0), `level2` (-9), `delay3` (750), `feedback3` (0), `level3` (-12), `delay4` (1000), `feedback4` (0), `level4` (-15), `mix` (50)

### Filter and EQ

- `bandpass` **Bandpass**: `center` (1000), `q` (1)
- `bass` **Bass**: `boost` (0)
- `fft_filter` **FFT Filter**: `p1_freq` (40), `p1_gain` (0), `p2_freq` (100), `p2_gain` (0), `p3_freq` (250), `p3_gain` (0), `p4_freq` (600), `p4_gain` (0), `p5_freq` (1500), `p5_gain` (0), `p6_freq` (4000), `p6_gain` (0), `p7_freq` (9000), `p7_gain` (0), `p8_freq` (16000), `p8_gain` (0), `interp`* (1: 0=Linear/1=Smooth)
- `graphic_eq` **Graphic Equalizer (10 Bands)**: `b1` (0), `b2` (0), `b3` (0), `b4` (0), `b5` (0), `b6` (0), `b7` (0), `b8` (0), `b9` (0), `b10` (0), `gain` (0)
- `graphic_eq_20` **Graphic Equalizer (20 Bands)**: `b1` (0), `b2` (0), `b3` (0), `b4` (0), `b5` (0), `b6` (0), `b7` (0), `b8` (0), `b9` (0), `b10` (0), `b11` (0), `b12` (0), `b13` (0), `b14` (0), `b15` (0), `b16` (0), `b17` (0), `b18` (0), `b19` (0), `b20` (0), `gain` (0)
- `graphic_eq_30` **Graphic Equalizer (30 Bands)**: `b1` (0), `b2` (0), `b3` (0), `b4` (0), `b5` (0), `b6` (0), `b7` (0), `b8` (0), `b9` (0), `b10` (0), `b11` (0), `b12` (0), `b13` (0), `b14` (0), `b15` (0), `b16` (0), `b17` (0), `b18` (0), `b19` (0), `b20` (0), `b21` (0), `b22` (0), `b23` (0), `b24` (0), `b25` (0), `b26` (0), `b27` (0), `b28` (0), `b29` (0), `b30` (0), `gain` (0)
- `highpass` **Highpass**: `cutoff` (80)
- `lowpass` **Lowpass**: `cutoff` (8000)
- `notch` **Notch Filter**: `n1_on`* (false), `n1_freq` (60), `n1_gain` (-30), `n2_on`* (false), `n2_freq` (120), `n2_gain` (-30), `n3_on`* (false), `n3_freq` (180), `n3_gain` (-30), `n4_on`* (false), `n4_freq` (240), `n4_gain` (-30), `n5_on`* (false), `n5_freq` (300), `n5_gain` (-30), `n6_on`* (false), `n6_freq` (360), `n6_gain` (-30), `width`* (0: 0=Narrow/1=Very Narrow/2=Super Narrow)
- `parametric_eq` **Parametric Equalizer**: `master_gain` (0), `hp_on`* (false), `hp_freq` (30), `hp_slope`* (0: 0=12 dB/oct/1=24 dB/oct/2=36 dB/oct/3=48 dB/oct), `low_on`* (true), `low_freq` (100), `low_gain` (0), `low_q` (0.71), `b1_on`* (true), `b1_freq` (200), `b1_gain` (0), `b1_q` (1), `b2_on`* (true), `b2_freq` (500), `b2_gain` (0), `b2_q` (1), `mid_on`* (true), `mid_freq` (1000), `mid_gain` (0), `mid_q` (1), `b4_on`* (true), `b4_freq` (2000), `b4_gain` (0), `b4_q` (1), `b5_on`* (true), `b5_freq` (5000), `b5_gain` (0), `b5_q` (1), `high_on`* (true), `high_freq` (8000), `high_gain` (0), `high_q` (0.71), `lp_on`* (false), `lp_freq` (18000), `lp_slope`* (0: 0=12 dB/oct/1=24 dB/oct/2=36 dB/oct/3=48 dB/oct)
- `scientific_filter` **Scientific Filter**: `type`* (1: 0=Bessel/1=Butterworth/2=Chebyshev/3=Elliptical), `mode`* (0: 0=Low Pass/1=High Pass/2=Band Pass/3=Band Stop), `order`* (6), `cutoff` (1000), `high_cutoff` (4000), `ripple`* (1), `stop_atten`* (60), `gain` (0)
- `simple_notch` **Simple Notch Filter**: `center` (1000), `q` (10)
- `simple_eq` **Simple Parametric EQ**: `center` (1000), `q` (1), `boost` (0)
- `treble` **Treble**: `boost` (0)

### Modulation

- `chorus_flanger` **Chorus/Flanger**: `mode`* (0: 0=Chorus/1=Flanger), `speed` (0.8), `width` (50), `intensity` (30), `transience` (0), `mix` (50)
- `flanger` **Flanger**: `initial_delay` (1), `final_delay` (5), `stereo_phasing` (90), `feedback` (50), `rate` (0.5), `inverted`* (false), `special`* (false), `sinusoidal`* (true), `mix` (50)
- `phaser` **Phaser**: `stages`* (4), `intensity` (100), `depth` (70), `rate` (0.5), `phase_diff` (90), `upper_freq` (2500), `feedback` (0), `mix` (50), `output` (0)

### Noise Reduction/Restoration

- `declicker` **Automatic Click Remover**: `threshold` (30), `complexity` (16)
- `dehummer` **DeHummer**: `freq`* (1: 0=50 Hz/1=60 Hz), `gain` (-40), `harmonics`* (5), `q` (30)
- `denoise` **DeNoise**: `amount` (40)
- `dereverb` **DeReverb**: `amount` (50), `rt60` (0.8)
- `speech_enhance` **Enhance Speech**: `mix` (100), `tone`* (0: 0=Low Tone/1=High Tone)

### Reverb

- `convolution_reverb` **Convolution Reverb**: `impulse`* (1: 0=Small Room/1=Medium Room/2=Large Hall/3=Cathedral/4=Plate/5=Ambience/6=Vocal Booth), `mix` (30), `room_size`* (100), `damping_lf`* (10), `damping_hf`* (20000), `predelay` (0), `width` (100), `gain` (0)
- `studio_reverb` **Studio Reverb**: `room` (50), `decay` (50), `damping` (50), `dry` (90), `wet` (35)
- `surround_reverb` **Surround Reverb**: `center_input` (100), `room_size` (50), `decay` (1.5), `predelay` (20), `damping` (40), `early` (40), `low_cut` (20), `high_cut` (12000), `width` (100), `dry` (80), `wet` (30)

### Special

- `binauralizer` **Binauralizer - Ambisonics**: `angle` (30), `head_size` (17.5), `mix` (100)
- `distortion` **Distortion**: `drive` (12), `curve`* (0: 0=Soft Clip/1=Hard Clip/2=Tube/3=Foldback), `symmetry` (0), `tone` (20000), `output` (0), `mix` (100)
- `fill_left` **Fill Left with Right**
- `fill_right` **Fill Right with Left**
- `guitar_suite` **GuitarSuite**: `compressor` (30), `distortion` (40), `dist_type`* (0: 0=Soft/1=Hard/2=Fuzz), `amp`* (1: 0=None/1=Clean Combo/2=British Stack/3=Tweed/4=Modern High Gain), `filter`* (0: 0=None/1=Low Pass/2=High Pass/3=Band Pass), `filter_freq` (2000), `filter_res` (20), `mix` (100), `output` (0)
- `invert_a` **Invert**
- `loudness_radar` **Loudness Meter**: `target` (-23)
- `mastering` **Mastering**: `eq_low` (0), `eq_mid_freq` (1000), `eq_mid` (0), `eq_high` (0), `reverb` (0), `exciter` (0), `exciter_mode`* (1: 0=Retro/1=Tape/2=Tube), `widener` (100), `loudness` (0), `output` (0)
- `panner_ambisonics` **Panner - Ambisonics**: `pan` (0), `tilt` (0), `roll` (0)
- `swap_channels` **Swap Channels**
- `vocal_enhancer` **Vocal Enhancer**: `mode`* (0: 0=Male/1=Female/2=Music)

### Stereo Imagery

- `stereo_expander` **Stereo Expander**: `center_pan` (0), `expand` (100)
- `stereo_width` **Stereo Width**: `width` (100)

### Time and Pitch

- `pitch_shifter` **Pitch Shifter**: `semitones` (0), `cents` (0)

## Audio transitions

### Crossfade

- `constant_gain` **Constant Gain**
- `constant_power` **Constant Power**
- `exponential_fade` **Exponential Fade**
