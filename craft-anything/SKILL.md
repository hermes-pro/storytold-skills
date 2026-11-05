---
name: craft-anything
description: "Study how a website, app or game works with Craft Anything (evidence-first inspection, clean-room by default), then build your own original version and check it against the original: capture a site's pages at desktop/tablet/phone widths with design tokens, layout per width and opened menus; record a brief, plan, hypotheses, findings and open questions with evidence ids; compare your build's screenshots with the original's (layout and perceptual likeness); write Markdown/HTML reports. Deep mode reads programs, APKs, .NET/Java, Electron, firmware and game files. Can also run a whole Study → Build → Check → Refine rebuild with a coding agent."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Reverse Engineering, Website, Rebuild, Clone, Clean Room, Evidence, Inspection, Web Design, Games, MCP]
    related_skills: [storytold, storytold-install, figcraft, vectorcraft, photocraft]
---

# Craft Anything

Craft Anything is a free, open-source inspection engine (storytold Crafting Apps, pure Rust) for finding out how a
website, desktop app, phone app or game works, with the evidence behind every answer. An agent drives it through an
MCP server (`craft-anything-cli mcp`) or CLI one-shots. It studies the original, keeps an investigation (brief, plan,
findings, open questions) on disk, and measures how alike a new build is to the original. Its own `rebuild` workflow
can also have a coding agent build a new project and refine it until it is close.

This skill is tested against Craft Anything 0.3.0 (early alpha).

**Scope.** It is for learning how something works and building **your own original version**: the same structure,
layout and behaviour, with your own text, names, pictures and code. Don't copy logos, photos, brand names or long
passages of text unless the person owns the original or has permission (the app's own builder prompt says the same).
Use it on software the person owns or is allowed to examine. It never bypasses DRM, logins or anti-cheat. Clean room
(the default) never reads anything inside the original: it works from what a visitor sees.

## When to Use

- "How is this site laid out / styled?": capture a page at 1440, 768 and 390 px with its colours, fonts, text sizes,
  spacing, radii, content widths, the layout of each section per width, headings, links, form outlines and the
  menus/pop-ups/collapsible sections it opens
- building your own page or app modelled on an existing one, and checking it: how alike it is per width, and what
  differs (padding, heading sizes, colours, items per row, sideways scroll)
- keeping a careful investigation with evidence ids, open questions and a handoff, and turning it into a report
- Deep mode (opt-in): what a program, library, APK, .NET/Java app, Electron app, WebAssembly, firmware image, packet
  capture, SQLite file or game archive contains (functions, strings, pseudo-C, classes, resources)
- handing a whole rebuild to Craft Anything and a coding agent (`rebuild`), when the person has one set up

Pick a different tool when:

| The job is… | Use |
|---|---|
| Designing a new screen or design system from scratch (no original to study) | `figcraft` |
| A logo, icon or illustration for your version | `vectorcraft` |
| Editing or making photos and pictures for your version | `photocraft` |
| Questions about source code you already have | read the source directly |

## Setup

1. Tools from the `craft-anything` MCP server are preferred. Hermes turns the hyphen into `_`: current Hermes names
   them `mcp__craft_anything__<tool>` (older releases `mcp_craft_anything_<tool>`). This skill uses bare tool names.
2. Otherwise check for the CLI with `craft-anything-cli --version`. If it's missing, or the MCP tools are, load the
   `storytold-install` skill and run its `setup craft-anything`. Then ask the user to start a new session or run
   `/reload-mcp`.
3. Until the MCP tools appear, use the CLI: every tool is a subcommand (`craft-anything-cli web-pixels-compare
   --json '{...}'`). Website tools need one MCP session, though (see **Pitfalls**).
4. `craft-anything-cli doctor` checks the install, a Chromium browser (`engine:chromium`, needed for websites), the
   optional engines (Ghidra, adb, JADX, Frida…) and the MCP self-test (`29 tools listed`).

Don't run Craft Anything's own `craft-anything-cli setup --client hermes`: besides registering the server it installs
its own skill named `craft-anything` into `~/.hermes/skills`, which collides with this one. If the person wants it,
add `--no-skill`. Try `--dry-run` first.

**Server flags** (`craft-anything-cli mcp [flags]`), all optional:

| Flag | Effect |
|---|---|
| (none) | Clean room, the Essentials tools only (29 listed); everything else via `list_toolsets` / `enable_toolset` |
| `--allow-run` | Treat tools that run code or change a device as approved. **Without it `web_site_open` and `web_page_states_capture` fail with `consent_required`**, because loading a site runs its scripts. Ask the person before you restart the server with it |
| `--project DIR.cany` | Keep evidence, the investigation memory and the journal in that folder (created if missing), so they survive restarts. Without it they live only in the session |
| `--deep` / `--clean-room` | Mode for this server, whatever Settings say |
| `--all-tools` | List every tool (102 in Clean room, 315 in Deep) instead of Essentials |
| `--inbox DIR` | A folder where `core_person_ask` / approvals are posted for the desktop app to answer |

Settings live in the config folder (`CRAFT_ANYTHING_CONFIG_DIR` overrides it); `settings_show` / `settings_set {key,
value}` read and change them (`deep_mode`, `ask_before_running`, `build.good_enough` (90), `build.web_widths`
([1440, 768, 390]), `projects_dir`, `assets.budget_usd`…). The desktop app is `craft-anything` (not needed here).

## What needs AI, keys or money

Nothing in **Study**, the evidence tools, the investigation memory, reports or comparisons needs an AI or a key. These
do, and none of them was run with a real AI or key for this skill:

- `rebuild` / `rebuild_start` and follow-ups: a coding agent writes the code. Claude Code (the person's own `claude`
  and subscription) is the supported one; Codex, Copilot, ACP agents (Gemini CLI, Qwen Code, opencode, goose, Hermes,
  Maki) and API-key backends (Anthropic, OpenAI, OpenRouter, Gemini, local OpenAI-compatible) exist but are mostly
  unverified upstream. Usage is billed to the person.
- `chat` (CLI) and `ai test`: an AI backend.
- `assets_image_generate` / `assets_model_generate`: a fal.ai key, paid per picture/model within `assets.budget_usd`.
  Without a key: `No fal.ai key is set up, so pictures and 3D models can't be generated.`
- `ai extractor`: an API backend (e.g. through OpenRouter) that pulls a Deep-mode game's files out.

Never add a backend or key, or start a build, without the person saying so.

## Mental Model

- **Two modes.** **Clean room** (default): only what a visitor sees: screenshots, visible text, measured layout and
  computed styles, opened menus. `core_target_open`, `triage`, page HTML/CSS/JS, decompilers and the like are
  refused. **Deep**: every tool, for private use; a site capture adds `page.html`, the CSS `breakpoints` (e.g.
  `max-width 720px`), assets, requests and console errors. Say which mode a claim came from.
- **Evidence.** Every analysis call returns a record with an `id` (`ev_<sha256>`), `confidence` (`observed`,
  `derived`, `inferred`), `coverage` and `limitations`. Big results come back as a summary; page them with
  `core_evidence_browse {source:{kind:"saved", evidence_id}, show:{kind:"part"|"rows"|…}}`. Cite ids; a claim
  without one is a hypothesis.
- **Investigation memory** (one per `--project`): brief → plan → hypotheses → findings (each needs real evidence ids)
  → open questions (`unknowns`) → handoff. `core_investigation_show` reads it all; `core_report_write` turns it into a
  report. Files: `<project>.cany/investigation/{brief,plan,findings,hypotheses,handoff}.md`, `evidence/`, `journal/`.
- **Toolsets.** `core` (Essentials) is listed at first. `list_toolsets` shows the 17 groups; `enable_toolset
  {toolset}` adds one (the server sends `tools/list_changed`; Hermes refreshes). Calling a tool from a group that isn't
  enabled enables it. Website tools are `browser`; rebuild projects are `projects`; the builder's file tools `build`.
- **A rebuild project** (from `rebuild` / `rebuild_start`) is a folder with `craft.json` (request, target, status,
  checks), `capture/` (the original: `README.md`, `capture.json`, `screenshot-<w>.png`, `states/`, `states-390/`),
  `app/` (the new project), `checks/round-<n>/` (each check's screenshots; round 0 is the builder's own check),
  `checks/asks/`, `investigation.cany/`, `inbox/`, `build-activity.log`.
- **Likeness** of a website = mean of `layout_similarity` (16 px tiles of matching mean colour) and
  `perceptual_similarity` (SSIM of brightness), per width, averaged. Good enough is 90%. The check's note also lists
  text, structure, colours, fonts, text sizes and per-width padding/heading/items-per-row differences, and claims
  (no sideways scroll, landmarks present, each opened menu opens in the build).

## Two ways to work as an agent

**A. You (Hermes) write the code; Craft Anything is the study, evidence and check side.** Use this when the person
asks you to build it. No AI key is involved on Craft Anything's side.

1. Study the original with the `browser` tools into a folder (recipe 1), and record what you learn (recipe 2).
2. Write your own project. Take exact values from `capture.json` (`design`, `layouts`) and look at every screenshot
   and state picture. Use your own copy, names and placeholder pictures.
3. Serve your build on `127.0.0.1` (a static server that exits when you kill it), capture it the same way, and
   compare each width with `web_pixels_compare {common_area:true}` (recipe 3). Fix, recapture, compare again.
4. Record the result as a `derived` finding and write the report.

**B. Craft Anything runs the rebuild with a coding agent** (needs an AI; see above). `rebuild <url|path|-> "<request>"
--backend <name>` (CLI, asks in the terminal) or `rebuild_start` (MCP, needs consent). It studies, starts the builder
in the project folder with a long brief, checks after each turn and refines up to `--rounds` (CLI default 2).
Hermes itself can be that builder: `craft-anything-cli ai add hermes --kind agent_cli --model hermes` makes it run
`hermes -z "<brief>"` in the project folder. Hermes then uses its own registered `craft-anything` server, so it must
pass `project` to `rebuild_check`. Hermes's `-z` turns off its approvals, so Clean room's approval rule doesn't reach
it (upstream note): keep to the brief's rule of never opening the original's files or code. While a run is building,
the builder calls `rebuild_check {project}` to get the same check mid-turn (recipe 4).

## Tools (bare names; see Setup for Hermes's prefix)

| Tool | Use it for |
|---|---|
| `core_investigation_show` / `core_session_show` | Start or resume: memory, mode, open targets, evidence counts |
| `core_brief_write {question, purpose?, targets?, constraints?, done_when?}` | The question and what "done" means. First |
| `core_plan_update {steps:[{title, status: todo\|doing\|done\|blocked, why?}], based_on_revision?}` | Replace the plan |
| `core_hypothesis_record {claim, prediction?, evidence_for?, evidence_against?}` / `core_hypothesis_update` | A claim being tested |
| `core_finding_record {statement, confidence: observed\|derived\|inferred, evidence_ids}` | A settled answer; ids are checked |
| `core_unknown_add {question, severity?, domain?, probes?, evidence_for?}` | An open question and what would settle it → `unk_…` |
| `core_unknown_edit {unknown_id, based_on_revision, status?, resolution?, evidence_for?}` / `core_unknown_verify {unknown_id}` | Resolve it; verify checks it cites intact evidence |
| `core_handoff_write {text}` | Where things stand, next steps, traps. End of every turn |
| `core_evidence_show {detail:"summary"}` / `core_evidence_browse` / `core_journal_read` | What's recorded; page big records |
| `core_report_write {path?, format: markdown\|html, include_evidence?}` | Report from findings + ledger (no `path`: text back) |
| `core_report_save {path, text}` | Save a report you composed (`.md`, `.html`, `.htm`, `.txt`) |
| `core_evidence_export {path}` / `core_evidence_import {path}` | Evidence bundle JSON; tampered records are rejected |
| `web_site_open {url, width?, height?, settle_ms?}` | Private headless Chrome on the page (needs approval) |
| `web_site_capture {output_directory, widths?, noise_pass?, max_height?}` | Screenshots + `capture.json` + `README.md` into a **new** folder |
| `web_page_states_capture {output_directory, width?, max_states?}` | Click open up to 8 menus/tabs/`<details>`, photograph each (needs approval) |
| `web_page_screenshot_take` | One PNG of the current page, **inline base64** (large; prefer `web_site_capture`) |
| `web_pixels_compare {before, after, common_area?, tolerance?, ignore?}` | `{path}` PNGs → `layout_similarity`, `perceptual_similarity`, diff box |
| `web_site_close` | Close the browser and delete its profile |
| `rebuild_check {project, wait_minutes?}` | Builder's mid-turn check; answered only by a running build |
| `project_show` / `rebuild_status` / `rebuild_activity_show {project}` | A rebuild project's checks, status, activity log |
| `core_person_ask {question, choices?}` | Ask the person through the app (needs `--inbox`) |
| `list_toolsets` / `enable_toolset {toolset}` | Show and add tool groups |

All 315 tools with params, toolset and marks (listed by default, allowed in Clean room, read-only, needs approval,
needs a target): `${HERMES_SKILL_DIR}/references/tools.md`.

## Procedure

1. `core_investigation_show`. If there's a handoff, continue from it.
2. `core_brief_write` with the purpose ("learning; build our own version") and constraints ("clean room", "no copying
   text, logos or images"), then `core_plan_update`.
3. Study with the focused tools; after each batch, update the plan. Record what you can't see as unknowns.
4. Build (yourself, way A) or let a run build (way B). Compare per width; fix the largest differences first.
5. Findings with evidence ids, `core_handoff_write`, `core_report_write`. Tell the person what differs and why
   (your own text and pictures lower the likeness on purpose).

### Recipe 1: study a website in Clean room (tested)

Server: `craft-anything-cli mcp --allow-run --project /abs/work/site.cany`. Target: a page served on
`http://127.0.0.1:8761/`.

```text
web_site_open {url:"http://127.0.0.1:8761/", width:1440, settle_ms:500}   → ev_…, title, facts {links, images, forms, height}
web_site_capture {output_directory:"/abs/work/cap-orig", widths:[1440,390]}
    → screenshot-1440.png, screenshot-390.png, capture.json, README.md; result.design {fonts, font_sizes,
      text_colors, backgrounds, radii, spacing, max_widths, shadows}
web_page_states_capture {output_directory:"/abs/work/states-orig", width:390}
    → state-1.png (Menu, menu, "expanded"), state-2.png (Do you ship?, section, "section opened"), states.json
web_site_close
```

`README.md` summarises it: fonts, sizes, colours, spacing, content widths, and per width each section's padding,
gap, items per row and content column (`section "Green": padding 0 48 96 48, gap 24, 3 per row, column 1100 px`).
Look at every PNG with your image tool. The output folder must not exist yet. Clean room keeps no HTML and no CSS
breakpoints: capture extra widths (e.g. 768) to find where the layout switches.

### Recipe 2: keep the investigation and write a report (tested)

```text
core_brief_write {question:"How is the start page laid out…", purpose:"learning; build our own version",
    targets:["http://127.0.0.1:8761/"], constraints:["clean room","no copying text, logos or images"], done_when:"…"}
core_plan_update {steps:[{title:"Capture the original", status:"doing"}, {title:"Build our own page"}, …]}
core_unknown_add {question:"At what width does the header switch to the Menu button?", severity:"medium",
    probes:["capture at 600, 720 and 768 px"], evidence_for:["ev_…capture"]}             → unk_cac052ac776d4696
core_hypothesis_record {claim:"One breakpoint near 720 px", prediction:"…", evidence_for:["ev_…"]}  → hyp_1
core_finding_record {statement:"At 1440 px the content sits in a 1100 px column; three cards per row…",
    confidence:"observed", evidence_ids:["ev_…capture"]}                                   → fnd_1
core_unknown_edit {unknown_id:"unk_…", based_on_revision:1, status:"resolved", resolution:"…", evidence_for:["ev_…"]}
core_unknown_verify {unknown_id:"unk_…"}                                                    → valid:true
core_handoff_write {text:"Captured original and build 1. Next: …"}
core_report_write {path:"/abs/work/report.md"}            → {bytes, findings:3, open_questions:1, evidence_records:7}
core_report_write {path:"/abs/work/report.html", format:"html", include_evidence:false}
```

The report has the question, what was looked at, each finding with its confidence ("Seen it (observed)", "Worked it
out (derived)") and cited evidence, open questions, mode and limitations, the handoff and an evidence ledger. With
`--project` everything was still there in a new server process. CLI: `craft-anything-cli --project
/abs/work/site.cany report --out report.md` (`--html`, `--no-evidence`).

### Recipe 3: check your own build against the original (tested)

Serve your build (e.g. `python3 -m http.server 8762 --bind 127.0.0.1` in its folder), then:

```text
web_site_open {url:"http://127.0.0.1:8762/"}  ·  web_site_capture {output_directory:"/abs/work/cap-build", widths:[1440,390]}  ·  web_site_close
web_pixels_compare {before:{path:"/abs/work/cap-orig/screenshot-1440.png"},
                    after:{path:"/abs/work/cap-build/screenshot-1440.png"}, common_area:true, tolerance:8}
  → "Over the shared 1440×975 area the layout is 91% alike and the detail 84% …"
    result {layout_similarity:0.913, perceptual_similarity:0.840, changed_bounding_box, sizes{before,after}}
```

Likeness ≈ (layout + detail) / 2 per width (here 88% at 1440, 96% at 390); aim for 90%. Compare the two
`capture.json` `design` and `layouts` blocks to find the cause (here `56px` vs `48px` heading, `96px` vs `72px` hero
padding, a different accent colour). Pass `ignore:{path:"…/noise-1440.png"}` (from `noise_pass:true`) for carousels
and videos. Record the comparison as a `derived` finding.

### Recipe 4: `rebuild_check` while Craft Anything builds (tested with a stand-in builder)

A real builder needs an AI; this was tested with a script registered as the builder (`ai add stub --kind agent_cli
--model hermes`, `ai program stub /abs/stub`), which wrote `app/index.html` and called the tool:

```text
craft-anything-cli rebuild http://127.0.0.1:8761/ "Make my own tea shop page with the same layout" \
    --backend stub --projects-dir /abs/work/projects --rounds 0 --unattended
  [Study] Opening … · Photographing the page … · Opening its menus, pop-ups and tabs…
  [Build] Building the first version…
builder → rebuild_check {project:"/abs/work/projects/127-0-0-1", wait_minutes:3}
  → {project, report:"web-visual: passed, 87% alike (needs 90%) — 1440 px: 88% alike (layout 91%, detail 84%; page
     height 1031 vs 975 px); 768 px: 78% …; text 93% alike; missing headings: …; colours the original uses that the
     build doesn't: #1f6f5c …; at 1440 px: top heading 48 px, the original's 56 px; … padding 72 48 72 48 vs the
     original's 96 48 96 48 | opened menus … \nPictures of your build …: checks/round-0/screenshot-1440.png …
     \nNot good enough yet: fix what it lists, build again, and check again with rebuild_check."}
  [Check 1] 87% alike …   [Ready] Ready: about 87% like the original, 9 of 9 claims hold.
```

A plain static `app/index.html` needs no build step. The builder's brief (worth reading as a checklist even in way A)
says: work from `capture/` only, match exact values, never let a phone page scroll sideways, change files only in
`app/`, never start dev servers, record unknowns, use neutral placeholders instead of logos/photos/long text.

### Recipe 5: Deep mode on a file (tested)

Server with `--deep`: `core_target_open {path:"/abs/file"}` → `{target_id, kind, sha256}`;
`core_target_triage` → `{kind, plain_english, recommended_toolsets, next_steps}`; then enable the toolset it names
(`native`, `android`, `javascript`…) and follow `next_steps`. Only on files the person owns or may examine.

## Formats

- **Capture folder:** `screenshot-<width>.png` (full page, cut at `max_height` 12000), `capture.json` (`design`,
  `layouts`, `outline`, `headings`, `links`, `forms` (never values), `text`, `a11y`, `assets`; Deep adds
  `breakpoints`, `health`, `meta`, `page.html`), `README.md`; `noise-<width>.png` with `noise_pass`.
- **States folder:** `state-<n>.png`, `states.json` (`label`, `kind`: menu/section/tab…, `changed`).
- **Reports:** Markdown or self-contained HTML. **Evidence bundle:** JSON (`core_evidence_export`).
- **Investigation project:** a `*.cany` folder. **Rebuild project:** a folder with `craft.json` (see Mental Model).

## CLI (no MCP needed)

```bash
craft-anything-cli doctor                       # install, browser, engines, MCP self-test
craft-anything-cli capabilities                 # toolsets and which tools are available in this mode
craft-anything-cli commands                     # every tool: command, toolset, needs_target, summary
craft-anything-cli web-pixels-compare --json '{"before":{"path":"/abs/a.png"},"after":{"path":"/abs/b.png"},"common_area":true}'
craft-anything-cli --format text <tool> …       # readable output; --output-format after a tool with its own --format
craft-anything-cli --project /abs/x.cany report --out report.md [--html]
craft-anything-cli --deep triage /abs/file      # Clean room refuses it
craft-anything-cli rebuild <url|/abs/path|-> "<request>" --backend <name> [--rounds N] [--build-with godot|unity|unreal|rust|<stack>]
    [--projects-dir DIR | --project-folder DIR --existing edit|start-from] [--continue-in DIR [--resume]] [--unattended]
craft-anything-cli ai list | ai detect          # backends; `ai add`, `ai builder`, `ai model` change them (ask first)
```

Global flags go before the subcommand: `--format json|jsonl|md|text|csv|tsv`, `--project`, `--allow-run`, `--deep`,
`--clean-room`. A tool's params go as `--json '{...}'`, `@params.json` or `-` (stdin).

## Pitfalls

- **Website tools need approval:** without `--allow-run`, `web_site_open` returns `consent_required`: `Open a website
  runs code or changes a device, so it needs your OK first.` Ask the person, then restart the server with
  `--allow-run` (or add it in the Hermes registration).
- **Each CLI command has its own browser:** `web-site-capture` after a separate `web-site-open` fails with `no website
  is open` (`Each CLI command starts its own browser and closes it when it ends…`). Use one MCP session.
- **`rebuild` picks a coding agent by itself:** with no backend configured it adds the first agent app it finds on PATH
  (e.g. Claude Code, the person's subscription) and builds. Always pass `--backend <name>` and get the person's OK.
- **`rebuild_check` only works during a Craft Anything build:** with no `project`: `No project given.`; a folder
  without `craft.json`: `… isn't a project folder: …/craft.json: No such file or directory (os error 2)`; nobody
  building: after `wait_minutes` (1..=60) `No answer: no build is running for this project, or the check took too
  long.` In way A, use recipe 3 instead.
- **Clean room refusals** come as `feature_missing` with `details.reason: "clean_room"`: `This looks inside the
  original (its code, files or page source), which Clean room never does.` Tell the person the question needs Deep
  mode; don't work around it.
- **The likeness check counts text:** your own copy shows up as `missing headings` / `missing words` and costs a few
  points. That's expected; don't copy the original's text to reach 90%.
- **Param names are exact** and unknown ones are refused with the list: `unknown field \`id\`, expected
  \`unknown_id\``; `unknown field \`supporting\`, expected one of \`claim\`, \`prediction\`, \`evidence_for\`,
  \`evidence_against\``; `assets_image_generate` takes `prompt`, `save_as`, `shape`.
- **Findings need real ids:** `Unknown evidence id ev_nope` (`Cite ids returned by analysis tools`).
- **Output folders must be new** absolute paths for `web_site_capture` and `web_page_states_capture`.
- **`web_page_screenshot_take` returns the PNG inline** (about 50 KB of base64 for a small page): it floods context.
- **`core_person_ask` without `--inbox`** doesn't reach anyone: it answers with a note to decide yourself (start
  your reply with "I decided:") or fails with `nobody is available to answer questions in this session`. Ask the
  person in chat instead.
- `project_list` only lists projects in `projects_dir` (default `~/Documents/Craft Anything`) and remembered folders;
  one made with `--projects-dir` isn't listed. Pass its folder to `project_show`.
- The README says 320 tools; this build lists 315 (`list_toolsets` and `enable_toolset` are extra).
- Early alpha: upstream marks behaviour checks for apps and games, non-Claude builders and some engine tools as
  partly verified. Treat their results as evidence to check, not as proof.

## Verification

- Look at the original's and your build's screenshots side by side at every width, and at each state picture.
- `web_pixels_compare` per width (or the `rebuild_check` report): 90% or better, no sideways scroll at 390 px, every
  menu/section the original opens also opens in yours.
- `core_investigation_show`: every plan step done or blocked, each conclusion matches a finding with evidence ids,
  open unknowns listed. `core_unknown_verify` on resolved ones. Then `core_report_write` and read the report.

## References

- `${HERMES_SKILL_DIR}/references/tools.md`: all 315 tools in 17 toolsets with params, defaults, choices, and marks
  for listed / Clean room / read-only / needs approval / needs a target / needs an engine. Grep it
  (`grep -n 'web_\|rebuild_' ${HERMES_SKILL_DIR}/references/tools.md`).
- Upstream: https://github.com/storytold/craft-anything (`README.md`, `docs/tools.md`, `docs/STATUS.md`,
  `docs/claude-code.md`).
