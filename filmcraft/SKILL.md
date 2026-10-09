---
name: filmcraft
description: "Video editing with FilmCraft (Premiere Pro-style): cut clips into a sequence, trim, razor, ripple, transitions (cross dissolve, dip to black), titles and lower thirds, music and audio levels/fades, color (Lumetri), speed changes, captions/subtitles (SRT/VTT, burn-in), transcript-based editing, and export to MP4 / ProRes / GIF / WAV or FCP XML / EDL / OTIO / AAF."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Video, Video Editing, NLE, Timeline, Captions, Subtitles, Export, MCP]
    related_skills: [storytold, storytold-install, effectcraft, soundcraft, photocraft, vectorcraft]
---

# FilmCraft

FilmCraft is a free, open-source clean-room take on Adobe Premiere Pro (storytold Crafting Apps), with its own
H.264/ProRes/AAC codecs (no FFmpeg). An agent drives it through an MCP server (`filmcraft-cli mcp`) or one-shot CLI
commands. Projects are `.fcproj` files; every edit is an undoable engine command.

## When to Use

Use it for **editing footage on a timeline**:

- assembling clips into a video: cuts, trims, ripple deletes, reordering, J/L-style audio, speed changes
- transitions (cross dissolve, dips, wipes), titles and lower thirds, simple shapes over picture
- music beds with gain and fades, audio crossfades, loudness-normalized exports
- colour correction with Lumetri, effects such as blur, crop, drop shadow
- captions/subtitles: build from a transcript, import/export SRT/VTT/SCC, burn into the export
- exporting deliverables (MP4, ProRes, DNxHR, GIF, PNG sequence, WAV) and timelines for other NLEs

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Animated graphics, kinetic type, logo reveals, keying/tracking VFX, anything keyframe-heavy | `effectcraft` (render an overlay, import it here) |
| Detailed audio work: mixing a podcast, noise cleanup, mastering | `soundcraft` |
| A still: thumbnail, poster frame retouch | `photocraft` / `vectorcraft` |

## Setup

1. If tools named `mcp_filmcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `filmcraft-cli --version`. If it's missing, load the `storytold-install` skill and
   run its `setup filmcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI (see **CLI**).

`filmcraft-cli mcp` is **headless** and starts with an **empty project** (`--project p.fcproj` or `--demo` to start
with content). For the user to watch live, they run `filmcraft --control 9876` and the server is started as
`filmcraft-cli mcp --bridge 127.0.0.1:9876`; then the `ui_*` tools work.

## Mental Model

- **Project → bins/items → sequences → tracks → clips.** Items are media (Movie, Audio, Still), sequences and graphics.
  A sequence has video tracks `V1..` (V1 at the bottom, higher tracks draw on top) and audio tracks `A1..`.
- **Ids everywhere.** `media_import` returns item ids, `timeline.place` returns clip ids (`[video, audio]` for a movie
  with sound; they are linked). Ids are plain integers; read them from replies or `doc_inspect`.
- **Time is ticks: 254016000000 per second.** Most commands also accept `seconds`, `frame` or `timecode`.
  Ticks must be **integers**. Clip `start`/`end` are sequence time; `sourceIn`/`sourceOut` are media time.
- **Every edit is a command** (675). Discover with `command_list {filter}`, run with `command_run {id, params}`, or
  several with `command_batch`. Unknown ids/tracks are errors, never a different target.
- **Linked selection is on:** an edit to a video clip also hits its linked audio (razor cuts both, gain sets both).
- **Sync lock is on for every track:** ripple edits refuse to run if they would push a clip on another track out of
  sync (see Pitfalls).

## Tools (Hermes names them `mcp_filmcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_inspect` / `project_inspect` / `sequence_inspect` | Project tree with item ids; the active sequence: tracks, clips (start/end, sourceIn/Out, speed, gainDb, effects), transitions, markers. `sequence_inspect` is long |
| `media_import {text}` | Import files: absolute paths, **one per line** in `text` → `{items, errors}` |
| `command_run {id, params}` | Run any command |
| `command_batch {steps:[{id, params}], stop_on_error?}` | Several commands in order → `{completed, failed, results}` (each its own undo step) |
| `command_list {filter?, enabled_only?}` | Find command ids and their params docs |
| `render_frame {seconds?, max_side?}` / `render_preview` | PNG of the Program frame. **Look at it** |
| *(bridge only)* `ui_inspect`, `ui_elements`, `ui_click`, `ui_drag`, `ui_key`, `ui_type`, `ui_screenshot`, `ui_control` | The live window |

Resources: `filmcraft://document` (as `doc_inspect`) and `filmcraft://commands` (as `command_list`).

## Editing building blocks

- **Sequence:** `file.newSequence {name, width, height, fps}` → `{sequence}`. Defaults are 1920×1080, **23.976 fps**,
  3 video + 3 audio tracks. `sequence.open {item}` makes a sequence active after `file.open`.
- **Place:** `timeline.place {item, track: "V1"|"A2", seconds | time | frame, insert?: bool, sourceIn?, duration?}`.
  Overwrite by default; `insert: true` ripples later clips. An audio track as `track` places sound only.
- **Cut and trim:** `timeline.razor {seconds, track?}` (all unlocked tracks), `timeline.trim {clip, edge: in|out,
  mode: regular|ripple, delta: ticks | deltaFrames}`, `edit.rippleDelete {clips}`, `edit.clear {clips}`,
  `sequence.closeGap {track, time}`, `timeline.move {moves:[{clip, track, time}]}`.
- **Speed:** `clip.speedDuration {clips, speed: 200, ripple: true, reverse?}`.
- **Transitions:** `sequence.applyVideoTransition {clip, edge: "out", effect: "Cross Dissolve", frames: 20}` on the
  outgoing clip (it ends at the cut). `sequence.applyAudioTransition {clip, frames}` goes on the clip's **in** edge, so
  pass the incoming clip for a crossfade at the cut (`constant_power` by default).
- **Titles / graphics:** `graphics.newText {text, position: [x, y], size, seconds, track, time}` → `{clip, layer}`.
  `position` is the alignment point on the first baseline and text is **left-aligned** by default. Style it with
  `graphics.set {clip, layer?, props: {align: "center", font: "Inter", font_style: "Bold", fill_color: "#ffcc00",
  shadow: true, background: true, stroke: true, size, tracking, opacity}}`. Add shapes to the same graphic with
  `graphics.newRectangle {clip, position, size}` (lower-third bars). `graphics.list {clip}` shows layers and bounds.
- **Audio:** `clip.audioGain {clips, mode: "set"|"adjust", db}`, `timeline.setTrack {track, volumeDb?, muted?, syncLock?}`,
  `essentialSound.generateDucking`, export `loudnessLufs: -14`.
- **Effects & keyframes:** `effects.apply {clips, effect}` (id or name), then `effects.setParam {clip, effect: id|index,
  param, value}`. To animate: `effects.toggleAnimation {clip, effect, param}` first, then `effects.setParam` with
  `seconds` or `time` (sequence time) per key. Built-ins on every clip: `motion` (position, scale, rotation, anchor),
  `opacity` (opacity, blend), `volume` (level, dB). Grep `references/effects.md` for ids and params.
- **Color:** `effects.apply {clips, effect: "Lumetri Color"}`, then `effects.setParam {clip, effect: "lumetri",
  param: "saturation"|"exposure"|"contrast"|"temperature"…, value}`.
- **Markers:** `markers.add {time, name, color, comment}`.

## Procedure

1. **Plan** the cut: order of shots, target length, where titles/music go, deliverable format and size.
2. **Set up:** `file.newSequence` with the delivery size and fps; `media_import` everything; note the item ids.
3. **Assemble on V1/A1** with `timeline.place` (or `command_batch`), then trim/razor/ripple.
4. **Transitions and titles**, then **music last** (on A2) so ripple edits aren't blocked by sync lock.
5. **Mix:** set gains, add fades (volume keyframes or audio transitions).
6. **Look:** `render_frame` at each cut, title and transition; summarize `sequence_inspect` (clip start/end per track).
7. **Save** `file.save {path: "/abs/x.fcproj"}`, **export** `file.exportMedia {path, wait: true}`, verify the file.

### Recipe: two-clip edit with dissolve, title, music and fade (tested)

Fresh session: sequence `7`; items `a.mp4`=8, `b.mp4`=9, `music.wav`=10; clips a=12/13, b=15/16 (read yours from replies).

```text
command_run file.newSequence {name:"Edit", width:1280, height:720, fps:30}
media_import {text:"/abs/a.mp4\n/abs/b.mp4\n/abs/music.wav"}                       → {items:[8,9,10]}
command_run timeline.place {item:8, track:"V1", seconds:0}                           → {clips:[12,13]}
command_run timeline.place {item:9, track:"V1", seconds:5}                           → {clips:[15,16]}
command_run timeline.trim {clip:12, edge:"out", mode:"ripple", delta:-254016000000}  # a: 0–4 s, b slides to 4 s
command_run timeline.trim {clip:15, edge:"in",  mode:"ripple", deltaFrames:15}       # drop b's first 0.5 s
command_run sequence.applyVideoTransition {clip:12, edge:"out", effect:"Cross Dissolve", frames:20}
command_run sequence.applyAudioTransition {clip:16, frames:20}                      # crossfade at the cut
command_run graphics.newText {text:"MY TRIP", position:[640,380], size:120, seconds:3, track:1, time:0}  → {clip:20}
command_run graphics.set {clip:20, props:{align:"center", font:"Inter", font_style:"Bold", fill_color:"#ffcc00", shadow:true}}
command_run timeline.place {item:10, track:"A2", seconds:0}                          → {clips:[22]}
command_run timeline.trim {clip:22, edge:"out", mode:"regular", delta:-889056000000} # music ends with the picture (8.5 s)
command_run clip.audioGain {clips:[22], mode:"set", db:-12}
command_run effects.toggleAnimation {clip:22, effect:"volume", param:"level"}
command_run effects.setParam {clip:22, effect:"volume", param:"level", value:0,   seconds:7}
command_run effects.setParam {clip:22, effect:"volume", param:"level", value:-60, seconds:8.5}
command_run markers.add {time:1016064000000, name:"Scene 2", color:"green"}
render_frame {seconds:1} · render_frame {seconds:3.83}                               → look at title and dissolve
command_run file.save {path:"/abs/edit.fcproj"}
command_run file.exportMedia {path:"/abs/edit.mp4", wait:true}                       → H.264 + AAC, 255 frames, 8.5 s
```

### Recipe: transcript cleanup and burned-in captions (tested)

This build has **no speech-to-text** (`transcript.generate`: "speech-to-text is not available in this build (built
without the `whisper` feature); import a transcript with transcript.set instead"). Bring word timings from elsewhere:

```text
command_run transcript.set {item:8, transcript:{language:"en", speakers:[{name:"Host"}],
            words:[{text:"Hello", start:50803200000, end:152409600000, speaker:0}, …]}}   # ticks, media time
command_run transcript.inspect {}                    → words with sequence times, paragraphs
command_run transcript.search {query:"welcome to"}   → {matches:[{from, to, start, end}]}
command_run transcript.removeFillers {}              → ripple-deletes um/uh/…
command_run transcript.removePauses {minSeconds:0.8, keepSeconds:0.2}
command_run transcript.createCaptions {maxChars:32, lines:1}         → new caption track
command_run captions.export {path:"/abs/talk.srt"}
command_run file.exportMedia {path:"/abs/talk.mp4", burnCaptions:true, wait:true}
```

`captions.import {path: "x.srt"}` brings existing subtitles in; `transcript.extract {from, to}` cuts words out by index.

## Export and formats

- `file.exportMedia {path, wait: true, format?, preset?, width?, height?, fps?, quality?, bitrateKbps?, audio?,
  range?: entire|inOut|workArea|custom, startSeconds?, endSeconds?, burnCaptions?, captionSidecar?: srt|vtt,
  loudnessLufs?, proresProfile?}`. The format comes from the extension (`.mp4` H.264, `.mov` ProRes, `.gif`, `.wav`).
  Without `wait` it returns `{job}` at once; poll `jobs.list`.
- Presets: `filmcraft-cli export --list-presets youtube` (e.g. "YouTube 1080p Full HD").
- Encode: H.264, ProRes 422 HQ, DNxHR, MJPEG, MXF, PNG/TIFF/BMP sequences, GIF, WAV/AIFF. Decode adds HEVC, VP9, AV1,
  MP3/FLAC/Ogg, MXF, MPEG-2. No HEVC/AV1 export.
- Interchange (tested): `file.exportInterchange {format: xml|fcpxml|otio|edl|aaf|omf, path}` → `{bytes, report}`;
  the `report` lists what the format can't carry (graphics become offline clips). Import an FCP XML/OTIO/EDL with
  `file.import {paths}` (adds its sequences), AAF with `file.importAaf`. `file.open` only opens `.fcproj`.

## CLI (no MCP needed)

```bash
filmcraft-cli --project p.fcproj export /abs/out.mp4 [--start 0 --end 3] [--scale 0.5] [--preset "…"] [--no-audio]
filmcraft-cli --project p.fcproj render --seconds 1 --out /abs/f.png --scale 0.5
filmcraft-cli --project p.fcproj --save exec timeline.razor seconds=2 track=V1
filmcraft-cli --project p.fcproj --save import a.mov b.wav
filmcraft-cli --project p.fcproj inspect sequence            # or: inspect project
filmcraft-cli --project p.fcproj --save run edits.jsonl      # one {"id","params"} per line
filmcraft-cli commands razor · filmcraft-cli describe timeline.trim
```

`key=value` values parse as JSON when they can. Edits are discarded unless you pass `--save` / `--save-as`.

## Pitfalls

- **Paths:** absolute everywhere (`media_import`, `file.save`, exports). The server's cwd is not yours.
- **Ripple edits and sync lock:** with music already on A2, `timeline.trim … mode:"ripple"` fails with `edit failed: this
  edit would break sync: A2 is sync-locked and has a clip in the way (turn off its sync lock, or lock the track, to
  make this edit)`. Place music last, or `timeline.setTrack {track:"A2", syncLock:false}`.
- **Ticks must be integers.** `delta: -889056000000.0` (a float) is silently ignored (`{"delta": 0}`). Use integer
  ticks, `deltaFrames`, or `seconds`.
- **Keyframes need the stopwatch:** `effects.setParam` with `seconds` on a non-animated param just sets the static
  value (a "fade" to -60 dB mutes the whole clip). Call `effects.toggleAnimation` first.
- **`graphics.newText` `track` is a 0-based index** (`track: 1` is V2), unlike `"V1"` names elsewhere. Text is
  left-aligned on `position` until `graphics.set {props:{align:"center"}}`.
- **Linked clips:** gain, razor and moves apply to the linked video+audio pair (`clip.audioGain` on 2 audio clips reports `clips: 4`).
- **Exporting an empty sequence "succeeds"** with a 1-frame file. Check `frames` in the export result.
- `sequence_inspect` dumps every clip's effects; extract `start/end/sourceIn/sourceOut` per track instead of reading it all.
- Many edit commands return `null` on success; that's normal. `render_frame` returns only the image.
- `transcript.generate` and `transcript.downloadModel` are disabled in the release builds (no whisper); use `transcript.set` or `captions.import`.

## Verification

- `render_frame` at each cut, transition midpoint and title; look at the images.
- Summarize `sequence_inspect`: expected clips per track, no gaps, total duration as planned.
- After export: `ffprobe -v error -show_entries format=duration:stream=codec_name,width,height out.mp4`, extract
  frames (`ffmpeg -ss 2 -i out.mp4 -frames:v 1 f.png`) and look; check audio with `-af volumedetect`.

## References

- `references/commands.md`: all 675 commands with params, grouped by prefix (`timeline`, `clip`, `sequence`,
  `graphics`, `captions`, `transcript`, `export`…). Grep it rather than reading it whole.
- `references/effects.md`: 130 video effects, 112 video transitions, 58 audio effects, 3 audio transitions with param
  ids and defaults.
- Upstream docs: https://github.com/storytold/filmcraft/tree/main/docs (`agents.md`, `transcripts.md`, `captions.md`,
  `graphics.md`, `control-protocol.md`).
