# Project: Nihal's MBA Application Corpus

All source material for Nihal's MBA applications (LBS, HEC, INSEAD, IMD) lives under `docs/`. This file is the orientation guide for working inside that corpus. Two longer docs you should know exist:

- `docs/README.md` — folder map and quick-lookup
- `docs/ORGANIZATION.md` — full structural proposal, the integration pipeline, naming conventions, decisions worth making once

Read those if you're doing structural work. For day-to-day editing, the rules below should be enough.

---

## Mental model

The corpus has four kinds of folders:

| Folder | What it is | Edit it? |
| --- | --- | --- |
| `docs/stories/` | Canonical, numbered story modules — the spine of the corpus | **Yes** — this is where truth lives |
| `docs/common/` | Cross-cutting frameworks and rollups (not stories themselves) | Yes, when a story-level fact changes |
| `docs/<SCHOOL>_<YEAR>/` | Submitted application drafts and LORs | **No** — historical record. Edits go upstream into `stories/` |
| `docs/new_work/` | Staging area for raw chat transcripts and unintegrated notes | Yes, but the goal is to drain it into `stories/` and archive the raw |

**Single source of truth.** Each fact has exactly one canonical home (a `stories/` file). Everything else references it. If you find yourself duplicating content across files, stop and link instead.

**One topic per file.** Don't extend an existing `stories/` file with a new project — give it its own letter-suffix file (`04a_`, `04b_`, ...).

---

## The integration pipeline

This is the most important workflow in the corpus. When the user drops new material (chat transcript, voice note, ad-hoc paragraph) into `new_work/`:

1. **Raw file in `new_work/`** — name it after the topic, not the date (`montreal_conversation_raw.md`, not `2026-05-29_chat.md`).
2. **Factual extract** — optional intermediate file capturing data without essay framing. Sometimes the raw file is clean enough that this step is skipped.
3. **Identify the target story file(s)** — usually a new `stories/04<letter>_*.md` for a new Derq project, or edits to an existing module.
4. **Integrate** — write/update the canonical story file. Back-port supporting changes to `04_*` (role expansion list), `06_*` (Why MBA evidence), `00_INDEX.md` (essay-type matrix, metrics), `README.md` ("What's new") as applicable.
5. **Log and archive** — add an entry to `docs/new_work/INBOX.md` under "Archived" and `mv` the raw file into `docs/new_work/_archive/`. **Do not delete raw files** — they are kept for traceability.

Before starting an integration, ask the user the questions a story file needs to answer that the raw material doesn't fully decide: client name yes/no, name people or anonymize, headline framing, integrate-now vs queue.

---

## Story-file conventions

- **Numbering**: `01_` through `08_` for top-level topics. Sub-projects under a numbered topic use a letter suffix (`04a_`, `04b_`, ..., `04f_`).
- **Extension**: `.md` for everything now. (Older versions used `.txt` for narrative and `.md` for index; the corpus has converged on `.md`.)
- **Naming**: `lowercase_with_underscores.md`. Topic-descriptive, not date-stamped.
- **Legacy ALL-CAPS section headers** — most story files use `SECTION NAME` as a heading rather than `## Section Name`. This is consistent across the corpus and works fine for its actual purpose (raw material for essay copy). It triggers markdown-lint warnings (MD022/MD026/MD032/MD041). **Do not "fix" this** as part of an unrelated edit — it is a separate, optional cleanup that is currently parked.
- **Structure within a story file** is usually STAR+I (Situation, Task, Action, Result, Impact) with explicit sections for metrics, skills demonstrated, key learnings, essay applications, connections to other stories, and "cautionary notes for essay use" where relevant.

---

## Where to start, by task

| Task | First file to open |
| --- | --- |
| User has an essay prompt, picking which stories to use | `docs/stories/00_INDEX.md` (essay-type matrix) |
| Need a specific metric | `docs/stories/00_INDEX.md` "KEY METRICS" or `docs/common/impact_stories_quick_reference.md` |
| New chat transcript landed in `new_work/` | `docs/new_work/INBOX.md` to see state, then follow the pipeline above |
| Structural change to how the corpus is organized | `docs/ORGANIZATION.md` |
| Understanding what changed since LBS 2025 | `docs/README.md` "What's new" section |

---

## Don'ts

- **Don't edit `LBS_2025/` (or any submitted-application folder).** Those are historical. Improvements go upstream into `stories/`.
- **Don't delete raw files from `new_work/`** after integrating. Move them to `new_work/_archive/`.
- **Don't combine topics into one file.** A new Derq project gets its own `04<letter>_*.md`.
- **Don't blame named individuals in story content** without flagging it. When real names appear (Akash, Arijit, Harshal, Abhishek, Gopal), the story file should include a "Cautionary Note for Essay Use" section reminding future-Nihal to frame the system, not the people. Arijit in particular wrote the LBS LOR and is a close colleague.
- **Don't paraphrase metrics.** Use the numbers as they appear in the raw material; if a number is uncertain, mark it `~` or note the source.
- **Don't claim WebFetch can read ChatGPT or Claude.ai share links.** Both render client-side and return only login prompts. Ask the user to paste the transcript into a file under `new_work/` instead.

---

## Active context (check `INBOX.md` for live state)

- Three Derq story files added in the 2026 cycle: `04e_*` (Conflict Prediction), `04f_*` (Montreal Offline Crisis), `08_*` (Hiring).
- `04f` Montreal is currently the corpus's strongest material for disagreement-with-authority, crisis execution, leadership without authority, constructive postmortem, and surfacing architectural gaps. Arijit (LBS LOR writer) was the PM on this project — a rare LOR/essay corroboration.
- The user has flagged additional Derq work updates still to come. Pipeline is ready to absorb them.
- `docs/new_work/INBOX.md` is the live tracker — read it at the start of any session that involves `new_work/`.

---

## Working style

- Short responses. The user reads the diff; trailing "here's what I did" summaries are noise.
- Ask the integration-decision questions (name client? name people? headline framing? integrate now or queue?) **before** writing a new story file, not after.
- When edits span multiple files, list the files you touched and the one-line reason at the end. That's the only kind of summary worth writing.
- Use the AskUserQuestion tool for genuine decisions, not for confirmation of obvious moves.
