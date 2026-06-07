# Current Role at Derq — Work Data Extract
Source: chat transcript saved as `raw_conversation_data.md` (May 2026).
Purpose: factual record of Nihal's current work at Derq — modules, scope, outcomes, technical wins, real client situations. **Facts, not framing.** Pull from this for any future MBA essay, story update, or resume bullet.

---

## 1. Current Role — Facts

- Backend software engineer at Derq.
- Primary stack: **C++** for backend; **Python** for testing, tooling, automation.
- Works across the full lifecycle: requirement clarification → development → ML integration → QA → deployment → site support.
- Acts as a **connective point between the ML, QA, and project teams**.
- Participates in sprint planning, backlog refinement, daily stand-ups, cross-team coordination.

**Self-described strengths:**
- Strong analytical skills.
- Fast development speed.
- End-to-end module ownership across multiple parallel modules.

---

## 2. Modules Owned or Contributed To

### 2.1 NearMiss & Crash Events
- Detects incidents between two vehicles, or between a vehicle and a vulnerable road user (VRU), when they were about to crash. Imminent-collision detection.
- **Sole active developer from the systems/software team** on this module. Complete development + debugging responsibility.
- Safety-critical, core-value module — directly supports the product's collision-prevention value proposition.
- Long-term ongoing ownership.
- ⚠️ Stronger framing than what's currently in `stories/04d_derq_project_near_miss_detection.txt` — back-port the "sole developer" line.

### 2.2 ATSPM (Automated Traffic Signal Performance Measures)
- Industry-standard product area in traffic.
- Owns development and continuous improvement of **all reports** in ATSPM (the full reports suite).
- Long-term ongoing ownership.
- ATSPM redesign backstory is already detailed in `stories/04c_derq_project_atspm_redesign.txt`; this is the ongoing-reports work that continues post-redesign.

### 2.3 V2X & Sensor Fusion
- Vehicle-to-Everything (V2X) and sensor fusion across multiple sensors (currently multiple cameras).
- Continuous collaborative work with ML and QA teams.
- Long-term ongoing.

### 2.4 ROW Intrusion (Right-of-Way Intrusion)
- Custom safety-detection work for a specific client.
- Approach: minimal changes to core product; custom work to meet client deadlines; full QA loop with the core QA team.
- **Outcome:** client very satisfied. **Repeat business expected** — more projects from this client are anticipated.

### 2.5 API Event Reporter (Parsons + other integrations)
- Push-API event reporting to different clients' downstream systems.
- **Parsons integration: two sprints of planned scope delivered in one sprint.**
- Unblocked the client-side integration earlier than committed.

### 2.6 Fire Detection
- Detects fire in image feeds.
- Tech: SigLIP-based detection.
- Set up the module + standardized coding practices by developing new modules.
- **Debugging win:** Diagnosed a dev/prod inconsistency rooted in **JPG vs PNG compression** affecting SigLIP model performance. Fix restored detection reliability.
- The **standardized module structure** developed here is now reused across similar ML integrations — i.e., this work created a reusable pattern for future ML-backed features.
- Nihal's own assessment of business impact: "meh." But the technical/standardization story is strong (clean STAR-format material).

### 2.7 Image Quality Analyzer
- Determines quality of the video feed.

### 2.8 Conflict Prediction (Dublin roundabout)
- Determines if there is a risky situation at a roundabout — proactive identification of risky situations.
- Client: **Ohio Department of Transportation, City of Dublin** (not Dublin, Ireland — clarified in `conflict_prediction_questions.txt`).
- **Flagship use case for the product.**
- Detailed metrics (from `conflict_prediction_questions.txt`):
  - Accuracy: **97% average** (requirement: 95%).
  - Latency: **40ms overall** (requirement: 100ms); **2ms module latency at peak traffic**.
  - Delivery: typical product = 7 working days; this delivery = **<1 day** via automated QA validation.
  - 4 conflict zones (one per incoming direction).
  - Timeline: **Feb 2025 – Mar 2025**.
  - Arijit was the product owner and gave full client-interaction freedom.
  - On paper title: Lead Developer. Actual: PM-cum-tech-lead.

### 2.9 TNL Report
- Detects conflicts between different signals in the same corridor (cross-signal conflict detection within a corridor).

### 2.10 Bellevue Use Cases — No Turn on Right + Dynamic Left Turn
- Detects risky situations for left- and right-turning vehicles, using different methodologies for each.
- Client profile: **"very nosey"** — high-scrutiny client that pays close attention to product behavior.
- **No Turn on Right:** deployed; the client has **never complained** about it.
- **Dynamic Left Turn:** needs to be **re-developed**. Reason (internal-only, not for external mention): the product project team gathered the wrong requirements from the client.

---

## 3. Cross-Functional / Bridging Work

- Consistently translates ML research outputs into production-grade modules.
- Originated standardized coding practices for ML-backed modules (started with SigLIP fire detection); now reused across similar integrations.
- Sits between ML (research), the product project team (client requirements), and QA (quality gates).
- One observed structural problem: requirements often reach engineering after key decisions are already locked in, creating rework — Nihal is positioned to close that gap.

---

## 4. Concrete Outcomes / Wins

- **ROW Intrusion** — tight-deadline custom delivery; client very satisfied; repeat business expected.
- **Bellevue No Turn on Right** — clean deployment for a notoriously scrutinizing client; no complaints since.
- **Parsons API integration** — 2 sprints' worth of work delivered in 1 sprint.
- **Conflict Prediction (Dublin/Ohio)** — flagship product use case; 97% accuracy vs 95% required; 40ms latency vs 100ms required; delivery cycle compressed from 7 days to <1 day via automated QA.
- **NearMiss** — sole developer from systems/software keeping a safety-critical module moving forward.
- **Fire Detection** — root-caused dev/prod mismatch (image-compression issue) that was degrading SigLIP performance; created reusable module pattern for future ML integrations.

---

## 5. Current Company Context (relevant to Nihal's situation, not for essays)

- Company is shifting **from client-acquisition-first to product-first**.
- Org structure is changing **from function-based teams (software, ML, FS) to product-based teams**.
- Nihal is **highly likely to be placed on the analytics team** in the new structure.
- More senior members from other departments are likely to lead the analytics team; Nihal does **not** want to compete for that lead role.
- Company is **unaware of Nihal's MBA applications**.

What Nihal actually wants out of the next phase:
- More leadership in product development.
- More client exposure.
- More involvement in product decision-making.
- Broader engineering leadership across modules — not confined to analytics.

(These are useful as honest career-direction context for "why MBA / why now" reflection, even if they're not stated directly in any internal company doc.)

---

## 6. MBA Application Hooks

Story-worthy items surfaced by this work, in priority order:

1. **Conflict Prediction (Dublin/Ohio DoT)** — already has its own draft (`conflict_prediction.txt`) + Q&A (`conflict_prediction_questions.txt`); needs to be promoted into a `stories/04e_*` file. Strongest single new project.
2. **Parsons "2 sprints → 1 sprint"** — concrete, quantified delivery win. Short, clean story.
3. **Fire Detection debug** — clean STAR-format bullet:
   - **S:** SigLIP fire detection working in dev, failing in prod.
   - **T:** Root-cause the dev/prod mismatch.
   - **A:** Traced it to JPG vs PNG image compression upstream of the model.
   - **R:** Restored reliability; created standardized module pattern reused across subsequent ML integrations.
4. **NearMiss sole-developer ownership** — strong adcom line: "sole developer from systems/software team on a safety-critical collision-detection module." Should be back-ported into `stories/04d_*`.
5. **ROW Intrusion** — client-satisfaction → repeat-business story; supports the "demanding-client satisfaction" pattern that already appears in the API Integration story (`stories/04b_*`).
6. **Bellevue No Turn on Right** — adaptability under high client scrutiny; clean-deployment evidence.
7. **Cross-team bridging** — the consistent thread across NearMiss, Fire Detection, Conflict Prediction, ATSPM: translating ML research into production and standardizing how it gets done. This is what's actually new since the existing `stories/` files were written.

---

## 7. Cross-References

- `new_work/conflict_prediction.txt` — original Dublin/Ohio narrative.
- `new_work/conflict_prediction_questions.txt` — detailed metrics + Arijit's role.
- `new_work/hiring.txt` — unrelated, but also pending integration into stories.
- `stories/04c_derq_project_atspm_redesign.txt` — the ATSPM redesign backstory (this extract covers ongoing reports work).
- `stories/04d_derq_project_near_miss_detection.txt` — NearMiss redesign backstory; **needs back-port** of "sole developer" framing.
- `stories/04b_derq_project_api_integration.txt` — API Integration story; the Parsons + Bellevue + ROW Intrusion items are the next wave of this same pattern.
