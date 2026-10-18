---
name: filmcraft
description: "Video editing with FilmCraft (Premiere Pro-style): cut clips into a sequence, trim, razor, ripple, transitions (cross dissolve, dip to black), titles and lower thirds, music and audio levels/fades, color (Lumetri), speed changes, captions/subtitles (SRT/VTT, burn-in), transcript-based editing, text-to-speech narration, and export to MP4 / ProRes / GIF / WAV / FLAC or FCP XML / EDL / OTIO / AAF."
version: 0.4.0
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
- a quick scratch voice-over: text-to-speech narration clips (built-in robotic voices)
- exporting deliverables (MP4, ProRes, DNxHR, GIF, PNG/EXR sequence, WAV, FLAC, AAC) and timelines for other NLEs

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
- **Every edit is a command** (701). Discover with `command_list {filter}`, run with `command_run {id, params}`, or
  several with `command_batch`. Unknown ids/tracks are errors, never a different target.
- **Linked selection is on:** an edit to a video clip also hits its linked audio (razor cuts both, gain sets both).
  To act on one side only, select it with `timeline.select {clips: [v], linked: false}`, then run the edit with no
  `clips` (e.g. `edit.clear {}` removes the picture and keeps the sound).
- **Sync lock is on for every track:** ripple edits refuse to run if they would push a clip on another track out of
  sync (see Pitfalls).

## Tools (Hermes names them `mcp_filmcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_inspect` / `project_inspect` / `sequence_inspect` | Project tree with item ids; the active sequence: tracks, clips (start/end, sourceIn/Out, speed, gainDb, effects), transitions, markers. `sequence_inspect` is long |
| `media_import {paths: [..], bin?, image_sequence?}` | Import files by absolute path → `{items, errors}` |
| `command_run {id, params}` | Run any command |
| `command_batch {steps:[{id, params}], stop_on_error?}` | Several commands in order → `{completed, failed, results}` (each its own undo step) |
| `command_list {filter?, enabled_only?}` | Find command ids and their params docs |
| `render_frame {seconds?, max_side?}` / `render_preview` | PNG of the Program frame (`max_side` default 960, 0 = full size). **Look at it** |
| *(bridge only)* `ui_inspect`, `ui_elements`, `ui_click`, `ui_drag`, `ui_key`, `ui_type`, `ui_screenshot`, `ui_control` | The live window |

Resources: `filmcraft://document` (as `doc_inspect`) and `filmcraft://commands` (as `command_list`). The tools reject
unknown arguments (`unknown argument "text" for media_import; expected: bin, image_sequence, paths`).

## Editing building blocks

- **Sequence:** `file.newSequence {name, width, height, fps}` → `{sequence}`. Defaults are 1920×1080, **23.976 fps**,
  3 video + 3 audio tracks. `sequence.open {item}` makes a sequence active after `file.open`.
- **Place:** `timeline.place {item, track: "V1"|"A2"|"new", seconds | time | frame, insert?: bool, sourceIn?, duration?,
  video?: bool, audio?: bool}`. Overwrite by default; `insert: true` ripples later clips. An audio track as `track` places
  sound only; `audio: false` places picture only. `items: [8, 9]` lays several back to back in one undo step
  → `{clips, placed: [[v, a], …]}`.
- **Cut and trim:** `timeline.razor {seconds, track?}` (all unlocked tracks), `timeline.trim {clip, edge: in|out,
  mode: regular|ripple, delta: ticks | deltaFrames}`, `edit.rippleDelete {clips}`, `edit.clear {clips}`,
  `sequence.closeGap {track, time}`, `timeline.move {moves:[{clip, track, time}]}`. `edit.rippleDeleteHead {clips}`
  cuts a clip from its in point to the playhead (`playhead.set {seconds}`) and closes the gap; a playhead at or
  before the in point is refused (`the playhead is at or before the clip's in point`).
- **Speed:** `clip.speedDuration {clips, speed: 200, ripple: true, reverse?}`.
- **Transitions:** `sequence.applyVideoTransition {clip, edge: "out", effect: "Cross Dissolve", frames: 20}` on the
  outgoing clip (it ends at the cut). `sequence.applyAudioTransition {clip, frames}` goes on the clip's **in** edge, so
  pass the incoming clip for a crossfade at the cut (`constant_power` by default). `sequence.setTransition {transition,
  frames?, align?, params?}` edits one, `sequence.removeTransition {transitions: [id]}` deletes it.
- **Titles / graphics:** `graphics.newText {text, position: [x, y], size, seconds, track, time}` → `{clip, layer}`.
  `position` is the alignment point on the first baseline and text is **left-aligned** by default. Style it with
  `graphics.set {clip, layer?, props: {align: "center", font: "Inter", font_style: "Bold", fill_color: "#ffcc00",
  shadow: true, background: true, stroke: true, size, tracking, opacity}}`. Add shapes to the same graphic with
  `graphics.newRectangle {clip, position, size}` (lower-third bars), or give a shape its own clip with
  `{position, size, seconds, track, time}` and no `clip`. `graphics.list {clip}` shows layers and bounds.
- **Audio:** `clip.audioGain {clips, mode: "set"|"adjust", db}`, `timeline.setTrack {track, volumeDb?, muted?, syncLock?}`,
  `essentialSound.generateDucking`, export `loudnessLufs: -14`.
- **Effects & keyframes:** `effects.apply {clips, effect}` (id or name), then `effects.setParam {clip, effect: id|index,
  param, value}`; a choice param takes its index or its option name (`blend: "Multiply"`). To animate, pass
  `keyframe: true` with `seconds` or `time` (sequence time) on each key, or call `effects.toggleAnimation {clip, effect,
  param}` once first. The reply counts the param's keyframes (`{keyframes: 2}`). `effects.resetParam` resets one.
  Built-ins on every clip: `motion` (position, scale, rotation, anchor), `opacity` (opacity, blend), `volume` (level, dB).
  Grep `references/effects.md` for ids and params.
- **Color:** `effects.apply {clips, effect: "Lumetri Color"}`, then `effects.setParam {clip, effect: "lumetri",
  param: "saturation"|"exposure"|"contrast"|"temperature"…, value}`.
- **Markers:** `markers.add {time, name, color, comment}`; `markers.exportCsv {path}` writes them all.
- **Narration (text-to-speech):** `tts.create {text, voice?, pitch?, pace?, track: "A1", seconds | time, dir}` writes a
  WAV, imports it and places it → `{clip, item, path, duration}`. `[pause 1s]` in the text inserts a pause.

## Procedure

1. **Plan** the cut: order of shots, target length, where titles/music go, deliverable format and size.
2. **Set up:** `file.newSequence` with the delivery size and fps; `media_import {paths}` everything; note the item ids.
3. **Assemble on V1/A1** with `timeline.place` (or `command_batch`), then trim/razor/ripple.
4. **Transitions and titles**, then **music last** (on A2) so ripple edits aren't blocked by sync lock.
5. **Mix:** set gains, add fades (volume keyframes or audio transitions).
6. **Look:** `render_frame` at each cut, title and transition; summarize `sequence_inspect` (clip start/end per track).
7. **Save** `file.save {path: "/abs/x.fcproj"}`, **export** `file.exportMedia {path, format, wait: true}`, verify the file.

### Recipe: two-clip edit with dissolve, title, music and fade (tested)

Fresh session, a 8 s / b 5 s / music 12 s: sequence `7`; items 8/9/10; clips a=12/13, b=15/16; transitions 20/21;
title 23; music 25 (every object shares one id counter, so read yours from the replies).

```text
command_run file.newSequence {name:"Edit", width:1280, height:720, fps:30}
media_import {paths:["/abs/a.mp4", "/abs/b.mp4", "/abs/music.wav"]}                 → {items:[8,9,10]}
command_run timeline.place {item:8, track:"V1", seconds:0}                           → {clips:[12,13]}
command_run timeline.place {item:9, track:"V1", seconds:5}                           → {clips:[15,16]}
command_run timeline.trim {clip:12, edge:"out", mode:"ripple", delta:-254016000000}  # a: 0–4 s, b slides to 4 s
command_run timeline.trim {clip:15, edge:"in",  mode:"ripple", deltaFrames:15}       # drop b's first 0.5 s
command_run sequence.applyVideoTransition {clip:12, edge:"out", effect:"Cross Dissolve", frames:20}
command_run sequence.applyAudioTransition {clip:16, frames:20}                      # crossfade at the cut
command_run graphics.newText {text:"MY TRIP", position:[640,380], size:120, seconds:3, track:1, time:0}  → {clip:23}
command_run graphics.set {clip:23, props:{align:"center", font:"Inter", font_style:"Bold", fill_color:"#ffcc00", shadow:true}}
command_run timeline.place {item:10, track:"A2", seconds:0}                          → {clips:[25]}
command_run timeline.trim {clip:25, edge:"out", mode:"regular", delta:-889056000000} # music ends with the picture (8.5 s)
command_run clip.audioGain {clips:[25], mode:"set", db:-12}
command_run effects.toggleAnimation {clip:25, effect:"volume", param:"level"}
command_run effects.setParam {clip:25, effect:"volume", param:"level", value:0,   seconds:7}    → {keyframes:2}
command_run effects.setParam {clip:25, effect:"volume", param:"level", value:-60, seconds:8.5}  → {keyframes:3}
command_run markers.add {time:1016064000000, name:"Scene 2", color:"green"}
render_frame {seconds:1} · render_frame {seconds:3.83}                               → look at title and dissolve
command_run file.save {path:"/abs/edit.fcproj"}
command_run file.exportMedia {path:"/abs/edit.mp4", format:"h264", wait:true}        → H.264 + AAC, 255 frames, 8.5 s
```

### Recipe: transcript cleanup and burned-in captions (tested)

The 0.9.0 release still has **no speech-to-text** (`transcript.generate`: "command `transcript.generate` is not
available right now: speech-to-text is not available in this build (built without the `whisper` feature); import a
transcript with transcript.set instead"). Bring word timings from elsewhere:

```text
command_run transcript.set {item:8, transcript:{language:"en", speakers:[{name:"Host"}],
            words:[{text:"Hello", start:50803200000, end:152409600000, speaker:0}, …]}}   # ticks, media time
command_run transcript.inspect {}                    → words with sequence times, paragraphs
command_run transcript.search {query:"welcome to"}   → {matches:[{from, to, start, end}]}
command_run transcript.removeFillers {}              → {removed:1, seconds:0.17}  ripple-deletes um/uh/… on all tracks
command_run transcript.removePauses {minSeconds:0.8, keepSeconds:0.2}  → {removed:1, seconds:0.93}
command_run transcript.createCaptions {maxChars:32, lines:1}         → {captions:3, track:20}
command_run captions.export {path:"/abs/talk.srt"}
command_run file.exportMedia {path:"/abs/talk.mp4", format:"h264", burnCaptions:true, wait:true}
```

`captions.import {path: "x.srt"}` brings existing subtitles in; `transcript.extract {from, to}` cuts words out by index.
`captions.setStyle {track: "C1", font, size, color, anchor, margin}` styles the burned-in look.

### Recipe: scratch narration (tested)

Built-in voices only: `basic-female` (default) and `basic-male`, robotic. The natural `kokoro-*` voices that
`tts.voices` lists fail with "natural voices are not available in this build (built without the `kokoro` feature)".

```text
command_run tts.voices {}                                        → voices, pitches, pace 0.5–2, "[pause 1s]" marker
command_run tts.create {text:"Hello and welcome. [pause 1s] Let's begin.", voice:"basic-male", track:"A1",
            seconds:0, dir:"/abs/narration"}                    → {clip:9, item:8, path:".../Narration 1.wav", duration}
command_run tts.edit {clip:9, text:"A longer new line.", pitch:"low", pace:1.2}  → {clip:9, item:12, duration, fileDuration}
command_run timeline.trim {clip:9, edge:"out", mode:"ripple", delta:<fileDuration - duration>}  # see Pitfalls
command_run tts.inspect {clip:9}                                 → text, voice, pitch, pace
command_run tts.preview {text:"Try this", path:"/abs/try.wav"}   # renders a WAV without touching the timeline
```

Place the picture with `timeline.place {item, track:"V1", audio:false}` so its own sound doesn't fight the voice.

## Export and formats

- `file.exportMedia {path, format, wait: true, preset?, width?, height?, fps?, quality?, bitrateKbps?,
  bitrateMode?: cbr|vbr1Pass|vbr2Pass|crf, crf?: 0..51, audio?, audioCodec?: aac|pcm|flac, range?: entire|inOut|workArea|custom,
  startSeconds?, endSeconds?, burnCaptions?, captionSidecar?: srt|vtt, loudnessLufs?, proresProfile?, alpha?}`.
  **Pass `format`** (`h264`, `prores`, `dnxhr`, `gif`, `png`, `exr`, `wav`, `flac`, `aac`, …): through MCP the extension
  is not used, and `x.wav` without `format` becomes an H.264 `x.wav.mp4`. A `preset` sets the format too. Without
  `wait` it returns `{job}` at once; poll `jobs.list`. Image sequences write `name000.png`, `name001.png`, ….
- Tested on 0.9.0: `h264` (+ `crf`), `prores` (.mov, HQ + PCM), `gif`, `png` sequence, `wav`, `flac`, `aac` (.m4a),
  `loudnessLufs: -14` (measured -14.0 LUFS), preset "YouTube 1080p Full HD". `file.exportFrame {path, format: "jpeg",
  time}` writes one still.
- **32-bit audio:** `settings: {audio: {bits: 32, float: true}}` writes 32-bit float PCM (tested: WAV → `pcm_f32le`);
  `bits` takes 16, 24 or 32. WAV, AIFF and QuickTime PCM take float; FLAC and MXF refuse it ("unsupported: FLAC audio
  has no 32 bit float samples: choose 16, 24 or 32 bit").
- Presets: `filmcraft-cli export --list-presets youtube` (e.g. "YouTube 1080p Full HD"). The query matches the name or
  the format id (`--list-presets prores` lists the 8 ProRes presets).
- Encode: H.264, ProRes, DNxHR, APV, MJPEG, MXF, PNG/TIFF/BMP/JPEG/TGA/DPX/EXR sequences, GIF, WAV/AIFF/FLAC/AAC.
  HEVC export needs a hardware encoder (NVENC, VA-API). Decode adds HEVC, VP9, AV1, MP3/Ogg, MPEG-2, animated GIF/APNG.
- Interchange (tested): `file.exportInterchange {format: xml|fcpxml|otio|edl|aaf|omf, path}` → `{bytes, report}`;
  the `report` lists what the format can't carry (graphics become clips without media or gaps, FCPXML keeps
  transitions on V1 only, an EDL holds one video track). Import an FCP XML/OTIO/EDL with
  `file.import {paths}` (adds its sequences), AAF with `file.importAaf`. `file.open` only opens `.fcproj`.

## CLI (no MCP needed)

```bash
filmcraft-cli --project p.fcproj export /abs/out.mp4 [--start 0 --end 3] [--scale 0.5] [--preset "…"] [--no-audio]
                 [--format f] [--settings '{json}'] [--allow-offline]    # format from the extension (.wav → WAV)
filmcraft-cli --project p.fcproj render --seconds 1 --out /abs/f.png --scale 0.5
filmcraft-cli --project p.fcproj --save exec timeline.razor seconds=2 track=V1
filmcraft-cli --project p.fcproj --save import a.mov b.wav
filmcraft-cli --project p.fcproj inspect sequence            # or: inspect project
filmcraft-cli --project p.fcproj --save run edits.jsonl      # one {"id","params"} per line
filmcraft-cli commands razor · filmcraft-cli describe timeline.trim · filmcraft-cli probe /abs/clip.mov
```

`key=value` values parse as JSON when they can; `--compact` prints one-line JSON. Edits are discarded unless you pass
`--save` / `--save-as`. `export` and `render` exit 1 when a clip's media is offline (placeholder frames) unless
`--allow-offline`. The extension picks the format for `.mp4`, `.mov`, `.wav`, `.aiff`, `.m4a`, `.aac`, `.gif`, but not
`.flac` ("give --preset or --format (unknown extension)"): pass `--format flac`. `--end` needs `--start` too.
A `--preset` sets the format: `out.mov` with an H.264 preset becomes `out.mov.mp4`.

## Pitfalls

- **Paths:** absolute everywhere (`media_import`, `file.save`, exports, `tts.create dir`). The server's cwd is not yours.
- **MCP exports ignore the extension.** `file.exportMedia {path: "x.wav"}` writes H.264 to `x.wav.mp4` (the reply's
  `path` shows it). Always pass `format` (or a `preset`). The CLI `export` does go by the extension (except `.flac`).
- **Ripple edits and sync lock:** with music already on A2, `timeline.trim … mode:"ripple"` fails with `edit failed: this
  edit would break sync: A2 is sync-locked and has a clip in the way (turn off its sync lock, or lock the track, to
  make this edit)`. `edit.rippleDeleteHead` and title tracks (V2) block the same way. Place music and titles last, or
  `timeline.setTrack {track:"A2", syncLock:false}`.
- **Ticks must be integers.** `delta: -889056000000.0` (a float) is silently ignored (`{"delta": 0}`). Use integer
  ticks, `deltaFrames`, or `seconds`.
- **Keyframes need the stopwatch:** `effects.setParam` with `seconds` on a non-animated param just sets the static
  value (reply `{keyframes: 0}`; a "fade" to -60 dB mutes the whole clip). Pass `keyframe: true` or call
  `effects.toggleAnimation` first.
- **`graphics.newText` `track` is a 0-based index** (`track: 1` is V2), unlike `"V1"` names elsewhere. A name such as
  `track: "V3"` is silently ignored and the title lands on the first free track (V2). A shape on a busy track fails with
  `V2 is not free here`. Text is left-aligned on `position` until `graphics.set {props:{align:"center"}}`.
- **Linked clips:** razor and moves apply to the linked video+audio pair. Transcript edits (`removeFillers`,
  `removePauses`) ripple every track, so the picture stays in sync with the speech.
- **Exporting an empty sequence "succeeds"** with a 1-frame file. Check `frames` in the export result.
- **`tts.edit` keeps the clip's old length.** A longer new line is cut off: the reply shows `duration` (the clip) and
  `fileDuration` (the new WAV). Extend it with `timeline.trim {clip, edge:"out", mode:"ripple", delta: fileDuration -
  duration}`. `tts.edit`/`tts.inspect` need `clip` once the selection has moved (`tts.edit`: "command `tts.edit` is
  not available right now: select a narration clip"; `tts.inspect`: "pass `item` or `clip`, or select a narration
  clip"). Without `dir`, an unsaved project writes narrations to `%TEMP%\FilmCraft\Narrations`; a saved one next to
  the `.fcproj`.
- `sequence_inspect` dumps every clip's effects; extract `start/end/sourceIn/sourceOut` per track instead of reading it all.
- Many edit commands return `null` on success; that's normal. `render_frame` returns the image plus "rendered frame".
- Release builds (0.9.0 too) have no speech models: `transcript.generate` (no `whisper` feature),
  `transcript.downloadModel` ("model downloads are not available in this build (built without the `speech-download`
  feature)"), `tts.downloadVoices` (no `neural-voices` feature) and the `kokoro-*` voices (no `kokoro` feature). `transcript.models` reports `available: false`. Use `transcript.set` or
  `captions.import`, and the `basic-*` voices.

## Verification

- `render_frame` at each cut, transition midpoint and title; look at the images.
- Summarize `sequence_inspect`: expected clips per track, no gaps, total duration as planned.
- After export: `ffprobe -v error -show_entries format=duration:stream=codec_name,width,height out.mp4`, extract
  frames (`ffmpeg -ss 2 -i out.mp4 -frames:v 1 f.png`) and look; check audio with `-af volumedetect`.

## References

- `references/commands.md`: all 701 commands with params, grouped by prefix (`timeline`, `clip`, `sequence`,
  `graphics`, `captions`, `transcript`, `tts`, `export`…). Grep it rather than reading it whole.
- `references/effects.md`: 130 video effects, 112 video transitions, 58 audio effects, 3 audio transitions with param
  ids and defaults. Grep it too.
- Upstream docs: https://github.com/storytold/filmcraft/tree/main/docs (`agents.md`, `transcripts.md`, `captions.md`,
  `graphics.md`, `control-protocol.md`).
