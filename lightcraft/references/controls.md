# LightCraft develop controls

Generated from `lightcraft-cli controls --json` (LightCraft 0.4.0, 114 sliders). Set them with
`set_develop {values: {"<id>": number}}` (or `run_command develop.set`). Format: `id` Label: min..max (default).

## profile

- `profile.amount` Amount: 0..200 (100)

## color

- `wb.temp` Temp: 2000..50000 (6500)
- `wb.tint` Tint: -150..150 (0)
- `color.vibrance` Vibrance: -100..100 (0)
- `color.saturation` Saturation: -100..100 (0)

## light

- `light.exposure` Exposure: -5..5 (0)
- `light.contrast` Contrast: -100..100 (0)
- `light.highlights` Highlights: -100..100 (0)
- `light.shadows` Shadows: -100..100 (0)
- `light.whites` Whites: -100..100 (0)
- `light.blacks` Blacks: -100..100 (0)

## curve

- `curve.highlights` Highlights: -100..100 (0)
- `curve.lights` Lights: -100..100 (0)
- `curve.darks` Darks: -100..100 (0)
- `curve.shadows` Shadows: -100..100 (0)
- `curve.splitShadows` Shadows split: 10..70 (25)
- `curve.splitMid` Midtones split: 20..80 (50)
- `curve.splitHighlights` Highlights split: 30..90 (75)
- `curve.refineSaturation` Refine Saturation: 0..100 (100)

## mixer

- `mixer.red.hue` Red Hue: -100..100 (0)
- `mixer.red.sat` Red Saturation: -100..100 (0)
- `mixer.red.lum` Red Luminance: -100..100 (0)
- `mixer.orange.hue` Orange Hue: -100..100 (0)
- `mixer.orange.sat` Orange Saturation: -100..100 (0)
- `mixer.orange.lum` Orange Luminance: -100..100 (0)
- `mixer.yellow.hue` Yellow Hue: -100..100 (0)
- `mixer.yellow.sat` Yellow Saturation: -100..100 (0)
- `mixer.yellow.lum` Yellow Luminance: -100..100 (0)
- `mixer.green.hue` Green Hue: -100..100 (0)
- `mixer.green.sat` Green Saturation: -100..100 (0)
- `mixer.green.lum` Green Luminance: -100..100 (0)
- `mixer.aqua.hue` Aqua Hue: -100..100 (0)
- `mixer.aqua.sat` Aqua Saturation: -100..100 (0)
- `mixer.aqua.lum` Aqua Luminance: -100..100 (0)
- `mixer.blue.hue` Blue Hue: -100..100 (0)
- `mixer.blue.sat` Blue Saturation: -100..100 (0)
- `mixer.blue.lum` Blue Luminance: -100..100 (0)
- `mixer.purple.hue` Purple Hue: -100..100 (0)
- `mixer.purple.sat` Purple Saturation: -100..100 (0)
- `mixer.purple.lum` Purple Luminance: -100..100 (0)
- `mixer.magenta.hue` Magenta Hue: -100..100 (0)
- `mixer.magenta.sat` Magenta Saturation: -100..100 (0)
- `mixer.magenta.lum` Magenta Luminance: -100..100 (0)

## bwMix

- `bw.red` Red: -100..100 (0)
- `bw.orange` Orange: -100..100 (0)
- `bw.yellow` Yellow: -100..100 (0)
- `bw.green` Green: -100..100 (0)
- `bw.aqua` Aqua: -100..100 (0)
- `bw.blue` Blue: -100..100 (0)
- `bw.purple` Purple: -100..100 (0)
- `bw.magenta` Magenta: -100..100 (0)

## grading

- `grading.shadows.hue` Shadows Hue: 0..360 (0)
- `grading.shadows.sat` Shadows Saturation: 0..100 (0)
- `grading.shadows.lum` Shadows Luminance: -100..100 (0)
- `grading.midtones.hue` Midtones Hue: 0..360 (0)
- `grading.midtones.sat` Midtones Saturation: 0..100 (0)
- `grading.midtones.lum` Midtones Luminance: -100..100 (0)
- `grading.highlights.hue` Highlights Hue: 0..360 (0)
- `grading.highlights.sat` Highlights Saturation: 0..100 (0)
- `grading.highlights.lum` Highlights Luminance: -100..100 (0)
- `grading.global.hue` Global Hue: 0..360 (0)
- `grading.global.sat` Global Saturation: 0..100 (0)
- `grading.global.lum` Global Luminance: -100..100 (0)
- `grading.blending` Blending: 0..100 (50)
- `grading.balance` Balance: -100..100 (0)

## effects

- `effects.texture` Texture: -100..100 (0)
- `effects.clarity` Clarity: -100..100 (0)
- `effects.dehaze` Dehaze: -100..100 (0)

## vignette

- `vignette.amount` Vignette: -100..100 (0)
- `vignette.midpoint` Midpoint: 0..100 (50)
- `vignette.roundness` Roundness: -100..100 (0)
- `vignette.feather` Feather: 0..100 (50)
- `vignette.highlights` Highlights: 0..100 (0)

## grain

- `grain.amount` Grain: 0..100 (0)
- `grain.size` Size: 0..100 (25)
- `grain.roughness` Roughness: 0..100 (50)

## detail

- `detail.sharpenAmount` Sharpening: 0..150 (0)
- `detail.sharpenRadius` Radius: 0.5..3 (1)
- `detail.sharpenDetail` Detail: 0..100 (25)
- `detail.sharpenMasking` Masking: 0..100 (0)
- `detail.nrLuminance` Noise Reduction: 0..100 (0)
- `detail.nrDetail` Detail: 0..100 (50)
- `detail.nrContrast` Contrast: 0..100 (0)
- `detail.nrColor` Color Noise Reduction: 0..100 (0)
- `detail.nrColorDetail` Detail: 0..100 (50)
- `detail.nrColorSmoothness` Smoothness: 0..100 (50)

## optics

- `optics.distortion` Distortion: -100..100 (0)
- `optics.vignetting` Vignetting: -100..100 (0)
- `optics.vignettingMidpoint` Midpoint: 0..100 (50)
- `optics.profileDistortion` Profile Distortion: 0..200 (100)
- `optics.profileVignetting` Profile Vignetting: 0..200 (100)
- `optics.defringePurple` Purple Amount: 0..20 (0)
- `optics.defringePurpleHueLo` Purple Hue Low: 0..90 (30)
- `optics.defringePurpleHueHi` Purple Hue High: 10..100 (70)
- `optics.defringeGreen` Green Amount: 0..20 (0)
- `optics.defringeGreenHueLo` Green Hue Low: 0..90 (40)
- `optics.defringeGreenHueHi` Green Hue High: 10..100 (60)
- `optics.caRed` Red/Cyan Fringe: -100..100 (0)
- `optics.caBlue` Blue/Yellow Fringe: -100..100 (0)

## geometry

- `geometry.vertical` Vertical: -100..100 (0)
- `geometry.horizontal` Horizontal: -100..100 (0)
- `geometry.rotate` Rotate: -10..10 (0)
- `geometry.aspect` Aspect: -100..100 (0)
- `geometry.scale` Scale: 50..150 (100)
- `geometry.offsetX` Offset X: -100..100 (0)
- `geometry.offsetY` Offset Y: -100..100 (0)
- `crop.angle` Straighten: -45..45 (0)

## calibration

- `calibration.shadowsTint` Shadows Tint: -100..100 (0)
- `calibration.redHue` Red Hue: -100..100 (0)
- `calibration.redSat` Red Saturation: -100..100 (0)
- `calibration.greenHue` Green Hue: -100..100 (0)
- `calibration.greenSat` Green Saturation: -100..100 (0)
- `calibration.blueHue` Blue Hue: -100..100 (0)
- `calibration.blueSat` Blue Saturation: -100..100 (0)
