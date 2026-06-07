# How This Corpus Is Organized — Proposal

A working proposal for how `/workspace/further/docs/` should be structured as it grows. The goal: any piece of information has exactly one canonical home, and the path from a chat transcript → integrated story → school-specific essay is well-defined.

The current state is in good shape but has accumulated some redundancy and unfinished back-port work. This document lays out the target structure, the rules for placing new material, and a concrete migration plan to get there.

---

## 1. Core Principles

**Single source of truth.** Each fact, story, or metric lives in exactly one canonical file. Everything else references it.

**One topic per file.** `stories/` modules are short enough that they can be read end-to-end in one pass and self-contained enough that you can grab one without needing five others for context.

**Raw → integrated → reusable.** New material follows a fixed pipeline:

1. Captured in a chat or written ad-hoc → lands in `new_work/`.
2. Distilled into a factual extract (no formatting for a target audience) → still in `new_work/`.
3. Integrated into the relevant `stories/` file → removed from `new_work/`.
4. Drawn from `stories/` when writing school-specific applications → result lands in `<SCHOOL>_<YEAR>/`.

**School-specific files are downstream and immutable.** Once an application is submitted, that school's folder is a historical record. Edits go upstream into `stories/`.

**Frameworks and rollups live in `common/`.** Story-specific content doesn't.

---

## 2. Target Folder Structure

```text
docs/
├── README.md                       # Top-level index and quick-lookup
├── ORGANIZATION.md                 # This file
│
├── stories/                        # Canonical story modules
│   ├── 00_INDEX.md                 # Navigator + metrics rollup
│   ├── 01_*.md … 08_*.md           # Numbered modules
│   ├── 04*.md                      # Derq subprojects (one file per project)
│   └── _archive/                   # Retired files (e.g. full_story, UPDATES_TO_APPLY)
│
├── common/                         # Shared frameworks and reference
│   ├── structured_narrative_framework.md
│   ├── impact_stories_quick_reference.md
│   └── lbs_v1_v2_v3_evolution_learnings.md
│
├── new_work/                       # Staging area
│   ├── *.md                        # Factual extracts kept as quick-lookup
│   ├── INBOX.md                    # One-line tracker of what's pending
│   └── _archive/                   # Raw sources retained after integration
│
└── <SCHOOL>_<YEAR>/                # Per-application folders
    ├── essay_v*.txt                # Drafts
    ├── lor_*.txt                   # Letters of recommendation
    └── prompts.md                  # School's actual essay prompts captured verbatim
```

---

## 3. Where Things Should Go

### Canonical work / life stories → `stories/`

The numbered modules are the spine. If a fact about Nihal's life or work would appear in any essay, it belongs in a `stories/` file.

**Naming:**

- Two-digit prefix for ordering: `01_`, `02_`, …, `07_`.
- Sub-projects under a numbered topic use a letter suffix: `04a_`, `04b_`, `04c_`, `04d_`, `04e_` …
- Use `lowercase_with_underscores.txt` for narrative files, `.md` for index/meta files.

**One file, one topic.** Resist combining. If a new Derq project comes along, give it its own `04<letter>_*.txt`.

### Cross-cutting frameworks → `common/`

Files that **don't tell a story** but help **work with stories**: narrative frameworks, quick-reference tables, evolution notes from one application cycle to the next.

The line: if removing it would leave a gap in the narrative itself, it's a story (goes in `stories/`). If it just makes working with the stories easier, it's `common/`.

### School-specific drafts → `<SCHOOL>_<YEAR>/`

One folder per application cycle per school. Holds the school's essay drafts (v1, v2, v3, final), the LOR text, and ideally a `prompts.md` capturing the school's actual prompt text. Once submitted, these are historical.

### Raw / unintegrated material → `new_work/`

The staging area. Anything from a chat transcript, ad-hoc note, or new event lands here first. The expectation is that material in `new_work/` eventually gets:

- **Promoted** — useful pieces integrated into a `stories/` file (or new file under `stories/`).
- **Removed** — the raw file is deleted once everything useful has been pulled out.

`new_work/` should not be where things go to live forever.

---

## 4. The Integration Pipeline (rules of the road)

When a chat or new note creates raw material:

**Step 1 — Drop the raw file in `new_work/`.**

- Name it after the topic, not the conversation date: `current_role_and_promotion_data.md`, not `2026-05-16_chat.md`.
- If multiple files come from the same source, prefix consistently.

**Step 2 — Write a factual extract alongside the raw file (in `new_work/`).**

- Goal: capture **all data** without formatting for any specific audience.
- No essay framing. No corporate framing. Facts, metrics, real outcomes, real context.
- The extract is what gets pulled from later. The raw file is for traceability.

**Step 3 — Identify the target story file(s).**

- New project at Derq → likely a new `stories/04<letter>_*.txt`.
- Update to an existing story (new metric, new framing) → edit the relevant `stories/*` file.
- New life event or trait → may justify a new `stories/0X_*.txt` if it's substantial.

**Step 4 — Integrate.**

- Edit the target `stories/` file(s).
- Update `stories/00_INDEX.md` if metrics, length, or essay-fit changes.
- Update any rollup in `common/` (`impact_stories_quick_reference.md` cheat sheet) if a headline metric is new.

**Step 5 — Retire the raw file.**

- Once everything useful is integrated, delete the raw file from `new_work/`.
- Keep the factual extract if it's still useful as quick-lookup; otherwise also delete.

---

## 5. Current State vs Target — Migration Plan

### Pending back-ports from the LBS v3 evolution

`common/lbs_v1_v2_v3_evolution_learnings.md` has a Priority 1 list that has not been fully applied to the `stories/` files. Examples:

- ISC $750,000 win → already in some `04*` files; check coverage.
- Prof. Sethi "lifelong learner" story → confirm it's in `02_*` and `05_*`.
- Scholarships as survival ("8 out of 12 years") → confirm it's in `01_*` and `05_*`.
- 15-year-old leaving home + tiny village → confirm it's in `01_*`.
- Student debt cleared → confirm it's in `07_*`.
- 2 engineers report to you → confirm it's in `04_*`.

**Action:** audit each `stories/` file against the Priority 1 list, mark missing items, apply edits.

### Completed integrations from `new_work/` (2026-05)

All pending integrations from the May 2026 cycle have been applied:

1. **Conflict Prediction** → integrated as `stories/04e_derq_project_conflict_prediction.md`. Raw sources moved to `new_work/_archive/`.
2. **Hiring** → integrated as `stories/08_hiring_team_building.md`; `stories/05_*` hiring section now points to it. Raw source moved to `new_work/_archive/`.
3. **Current role expansion** → applied across `stories/04_*` (new "Role Expansion 2025-2026" section listing ~10 parallel modules + structural-insight observation), `stories/04b_*` (Parsons 2-sprints-in-1 section), `stories/04c_*` (post-redesign continued ownership section), `stories/04d_*` (sole-developer ownership framing).
4. **Growth narrative** → applied to `stories/06_career_goals_why_mba.md` ("Current-Role Evidence — Why MBA, Why Now (2026 Update)" section).
5. **Pending:** user has flagged ~2 months of additional work updates to be written. Those will land in `new_work/` and follow the same pipeline.

### Retired files (2026-05)

Moved to archive folders rather than deleted:

- `common/full_story.txt` → `stories/_archive/full_story.md`. Original consolidated narrative; superseded by `stories/`.
- `stories/UPDATES_TO_APPLY.md` → `stories/_archive/UPDATES_TO_APPLY.md`. LOR back-port tracker; complete.
- `new_work/conflict_prediction.txt`, `new_work/conflict_prediction_questions.txt`, `new_work/hiring.txt`, `new_work/raw_conversation_data.md` → `new_work/_archive/`. Raw sources retained after their content was integrated.

### Proposed new lightweight tracker

`new_work/INBOX.md` — one-line entries tracking what's in `new_work/` and its target home. Stops `new_work/` from becoming a dumping ground.

Format:

```markdown
- [conflict_prediction.txt] → stories/04e_derq_project_conflict_prediction.txt (DRAFTING)
- [hiring.txt] → stories/08_hiring_team_building.txt (DECISION PENDING: new file vs extend 05_)
- [current_role_and_promotion_data.md] → updates to stories/04_*, 04b_*, 04c_*, 04d_*
- [raw_conversation_data.md] → reference only (transcript source for the two above; delete after integration)
```

---

## 6. Naming Conventions

| Type | Pattern | Example |
| --- | --- | --- |
| Numbered story | `NN_short_topic.txt` | `03_tvarit_ml_to_product_manager.txt` |
| Sub-project under a numbered story | `NNa_company_project_topic.txt` | `04b_derq_project_api_integration.txt` |
| Story-folder index | `00_INDEX.md` | `00_INDEX.md` |
| Cross-cutting framework | `lowercase_with_underscores.md` | `structured_narrative_framework.md` |
| School-specific application folder | `<SCHOOL>_<YEAR>/` | `LBS_2025/` |
| Essay draft within a school folder | `essay_v<N>.txt` | `essay_v3.txt` |
| LOR within a school folder | `lor_<recommender>.txt` | `lor_arijit.txt` |
| Raw chat/transcript in `new_work/` | `<topic>_raw_*.md` or as-given | `raw_conversation_data.md` |
| Factual extract in `new_work/` | `<topic>_data.md` | `current_role_and_promotion_data.md` |

---

## 7. Decisions Worth Making Once

A few choices that should be made once and applied consistently:

**Q: Should `stories/` files use `.txt` or `.md`?**

- Current: narrative files use `.txt`, meta files use `.md`. This works but is inconsistent.
- Proposal: keep as-is. `.txt` signals "long-form narrative I will write essay copy from"; `.md` signals "structured / referenced often."

**Q: Should client names appear in story files?**

- Some clients are named openly (Fremont, Franklin, Sarasota DoT, Dubai/Abu Dhabi Police). Some (Ohio DoT/Dublin) appear in `new_work/` but haven't been adjudicated for external use.
- Proposal: when integrating a story into `stories/`, capture the client name. Decide per-application whether to name in the essay itself. (Some companies treat client names as internal even on HR forms.)

**Q: Should retired files be deleted or archived?**

- Proposal: archive into `stories/_archive/` (or top-level `_archive/`). Disk is free, regret is expensive.

**Q: Where do school-specific *prompt texts* live?**

- Currently nowhere — they live in the user's head or external systems.
- Proposal: `<SCHOOL>_<YEAR>/prompts.md` capturing the verbatim prompts for that cycle. Useful for cross-school comparison and for any future re-use of drafts.

---

## 8. What This Document Is Not

- Not a record of decisions already made — those live in `stories/UPDATES_TO_APPLY.md` and the commit history of the files themselves.
- Not a content style guide — that's `common/structured_narrative_framework.md` and `common/impact_stories_quick_reference.md`.
- Not exhaustive — when in doubt, ask. The goal is to make the obvious moves consistent, not to specify every edge case.
