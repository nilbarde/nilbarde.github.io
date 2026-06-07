CONFLICT PREDICTION AT DUBLIN ROUNDABOUT — FLAGSHIP USE CASE, PM-CUM-TECH-LEAD DELIVERY

**Project Type**: New ML-backed safety feature (real-time conflict prediction)
**Role on paper**: Lead Developer. **Role in practice**: PM-cum-tech-lead with full client-interaction freedom.
**Client**: Ohio Department of Transportation, City of Dublin (Ohio — not Dublin, Ireland)
**Collaborator**: Arijit Bose (Senior PM, Oxford MBA) — product owner who delegated full client ownership.
**Timeline**: February 2025 – March 2025 (~2 months end-to-end)
**Result**: 97% accuracy (vs 95% requirement); 40ms latency (vs 100ms requirement); delivery time compressed from 7 working days to <1 day; 100% client satisfaction with zero change requests after the first version; flagship use case for the product.

---

THE PROBLEM — A COMPLEX ROUNDABOUT WITH FREQUENT ACCIDENTS

The Ohio Department of Transportation operated a roundabout in the City of Dublin that was plagued by frequent accidents. The underlying issue was driver confusion: at busy roundabouts with multiple incoming directions, drivers misread other vehicles' paths, hesitate, change lanes late, or yield when they shouldn't — and these moments produce conflicts.

The DoT didn't just want crash data after the fact. They wanted a system that could **predict conflicts in real time** — anticipate when two vehicles' paths were converging dangerously and surface the risky zones before incidents occurred.

This was a step beyond Derq's existing detection products (which identify events as they happen). Prediction means inferring intent: where is this vehicle likely to be in the next few seconds, given its current trajectory? And: which other vehicles' likely trajectories intersect with it?

THE ROLE I WAS GIVEN — FULL CLIENT FREEDOM

Arijit Bose was the product owner for this engagement. Following the pattern established on earlier projects (API Integration, ATSPM), he gave me **full freedom to interact with the client directly** — to gather requirements, define scope, negotiate constraints, and present results.

On paper, my title for this project was Lead Developer. In practice, the role was PM-cum-tech-lead: I owned the technical direction, the client conversation, and the delivery — with Arijit available as escalation rather than as a layer between me and the customer. Same pattern as the API Integration story (`04b_*`), but compressed into a tighter timeline and with a more demanding accuracy bar.

This level of trust from a Senior PM toward a developer is unusual at this experience level. It worked because the earlier projects had already built the track record: ATSPM redesign (15% faster revenue, flagship status), API Integration (70%+ NPS, 25% cycle reduction), Blinking Traffic Signs (25% faster delivery, government adoption). Arijit's view: where his colleagues would have optimized incrementally, my comprehensive understanding consistently produced market differentiators. Conflict Prediction was an opportunity to extend that pattern into ML-heavy territory.

REQUIREMENT GATHERING — DIRECT WITH THE CLIENT

I led the client conversations directly. The Ohio DoT had a clear performance bar:

- **Accuracy ≥ 95%** on conflict identification (false positives erode trust; missed conflicts erode safety value).
- **Latency ≤ 100ms** end-to-end — slow predictions are useless predictions when vehicles are moving.
- **Coverage**: all 4 incoming directions of the roundabout, with conflicts identified per-direction.
- **Real-time visualization** so the client could intuitively understand the on-ground scenarios.

The 95%/100ms requirements were stated. The harder requirement was unstated: the client needed to **trust** the system enough to act on its outputs (adjusting signage, lane markings, or rules). Trust comes from transparency. If they couldn't see what the system was predicting and why, the accuracy number on a slide deck wouldn't matter.

That insight drove a key design decision later in the project.

LEVERAGING SELF-DRIVING CAR BACKGROUND

The path-prediction problem at the heart of conflict prediction is the same problem I worked on at IIT Bombay's self-driving car project (`02_*`): given current state (position, velocity, heading), predict the trajectory over the next 1–3 seconds. The difference is the perspective — the self-driving car predicts its own and others' paths from inside the vehicle; conflict prediction does the same from a roadside camera.

I led the model evaluation in close collaboration with the ML team. The models we evaluated were standard motion-prediction techniques, ranked from simple to complex:

- **Constant Velocity (CV)** — baseline.
- **Constant Acceleration (CA)** — accounts for braking/acceleration.
- **Constant Curvature & Acceleration (CCA)** — handles curved paths.
- **Constant Turning Rate & Acceleration (CTRA)** — better at turns.
- **Constant Turning Rate & Velocity (CTRV)** — common in tracking literature.
- **LSTM** — learned trajectory prediction.

The choice was not the most sophisticated model — it was the model that delivered the accuracy requirement at the latency budget, on the available compute, while remaining explainable to the client. We optimized for the operating constraints, not for paper-perfect accuracy.

LATENCY ENGINEERING — 100ms BUDGET, 40ms DELIVERED

The 100ms end-to-end latency requirement was the binding constraint. Real-time conflict prediction means: camera capture → vehicle detection → trajectory prediction → conflict scoring → output, all within budget, every frame, even at peak traffic.

What I delivered:

- **40ms overall end-to-end latency** — 60ms of headroom against the 100ms requirement.
- **2ms module-level latency at peak traffic** — the conflict-prediction module itself adds negligible time on top of the upstream perception stack.

The headroom matters more than the headline number. A system that just barely meets the latency requirement at typical traffic will break at peak. Engineering for 40ms typical / 2ms peak module ensures the system stays inside its budget at the worst times, not just the best.

ACCURACY — 97% vs 95% REQUIREMENT

On-the-ground accuracy averaged **97%** across the four incoming directions — comfortably above the 95% bar. We achieved this through model selection plus careful tuning against real Dublin traffic data, not synthetic benchmarks.

The four conflict zones (one per incoming direction) were validated independently. Per-zone accuracy let the client identify which approaches contributed most to incidents — turning the prediction system into an actionable diagnostic tool, not just a real-time alert.

REAL-TIME VERIFICATION — INNOVATION IN QA

A defining innovation on this project was the **real-time data verification approach** I introduced to QA.

Typical product delivery cycle at Derq for a feature of this complexity is around 7 working days — heavily back-loaded with manual validation. The QA team has to replay scenarios, compare predictions to ground truth, and certify each release before deployment. This is necessary for safety-critical features but slow.

For Conflict Prediction, I built **real-time verification directly into the validation pipeline**. Instead of replay-and-compare, predictions and ground-truth events were checked live as data flowed through the system. This had three effects:

1. **Delivery time compressed from ~7 working days to <1 day.** The bulk of validation became automated and continuous.
2. **A more realistic, intuitive client experience.** Live verification meant we could demo accuracy in the same conditions the system would run in production — no synthetic dressing.
3. **Faster iteration loops.** When an edge case surfaced, the fix-and-revalidate cycle dropped from days to hours.

This isn't a one-project trick. The same instinct shows up in the Fire Detection standardization work — turn a one-time engineering effort into a reusable pattern. Conflict Prediction's automated QA is the same pattern applied to validation.

VISUALIZATION — RTSP REUSE AND ENGINEERING ECONOMY

The client needed a real-time visualization of predicted vehicle paths and conflict zones — they wanted to *see* what the system was predicting, not just receive alerts.

The pragmatic choice: the client was comfortable receiving an RTSP video stream, and Derq had a ready-to-use RTSP publisher module from prior work. Rather than building a custom visualization tool, I used the existing module to publish annotated frames as an RTSP feed.

This saved engineering resources for the real work (model selection, latency engineering, validation pipeline) while still delivering the client a visual artifact they could open in any standard video player. The visualization had the largest single impact on client satisfaction — they reported that watching predictions overlaid on live traffic gave them confidence in the system more than any accuracy number on a report.

**Client outcome:** zero change requests after the first version. The system delivered visibly worked.

DOWNSTREAM IMPACT — RISK AREAS AND TRAFFIC RULES

The Ohio DoT used the conflict reports to **identify high-risk zones at the roundabout and implement additional traffic rules** — adjustments to signage, lane markings, and right-of-way conventions targeted at the specific conflict patterns the system surfaced.

This is what closing the loop looks like: prediction system → identified risk areas → operational changes → reduced incidents. The system moved from "interesting analytics" to "infrastructure-decision support" — which is the use case Derq's product portfolio is built around.

CHALLENGES — TIMELINE AND SECURITY

The two real challenges weren't algorithmic — they were operational:

1. **Compressed timeline with parallel obligations.** The two-month window overlapped with ongoing work on other modules (NearMiss, ATSPM, API integrations). Delivering a new ML-backed module while maintaining ongoing ownership of multiple long-term products required tight time allocation. The automated QA pipeline was as much a self-protective decision as a quality decision — manual validation simply wouldn't have fit.
2. **Exposing network ports for RTSP while staying inside client security regulations.** Ohio DoT had strict regulations around what could be exposed externally. Working out the network configuration that delivered live video while meeting their security posture required iteration with their IT team — a reminder that government clients are as much a security-engineering problem as a product problem.

PRODUCT IMPACT — FLAGSHIP USE CASE

The system is **still deployed and in use** at the Dublin roundabout. The internal framing within Derq is that Conflict Prediction has become a **flagship use case** for the product — the example we lead with when describing real-time analytics to new prospects, alongside ATSPM (the flagship product for performance measures).

Whether the Dublin engagement led directly to contract expansion is something the business team would have better visibility on; from the engineering side, the deliverable was clean and the client was satisfied enough to leave the system running without requested changes.

---

KEY ACHIEVEMENTS:

- Delivered conflict prediction system for Ohio DoT (City of Dublin) in ~2 months end-to-end.
- 97% accuracy vs 95% requirement (per-direction validated across 4 conflict zones).
- 40ms overall latency vs 100ms requirement; 2ms module-level latency at peak traffic.
- Compressed delivery cycle from ~7 working days to <1 day via automated real-time verification.
- 100% client satisfaction; zero change requests after the first version.
- Introduced real-time data verification as a QA pattern reusable across future ML features.
- Reused existing RTSP publisher module for visualization — engineering economy.
- Acted as PM-cum-tech-lead under a Lead Developer title; Arijit gave full client-interaction freedom.
- Direct application of self-driving-car trajectory-prediction background (IIT Bombay → production).
- Flagship use case status for the product.
- Downstream operational impact: client identified risk zones and implemented new traffic rules.

QUANTIFIABLE METRICS:

- **97% accuracy** (requirement: 95%)
- **40ms end-to-end latency** (requirement: 100ms)
- **2ms module-level latency** at peak traffic
- **4 conflict zones** identified (one per incoming direction)
- **~2 months** total delivery (Feb 2025 – Mar 2025)
- **7 days → <1 day** delivery cycle compression via automated QA
- **0 change requests** post-delivery (client satisfaction proxy)
- **Flagship use case** designation within product portfolio

SKILLS DEMONSTRATED:

- ML model selection under operating constraints (latency, compute, explainability)
- Real-time systems engineering (latency budgeting and headroom)
- Cross-functional leadership (ML, QA, client IT/security)
- Independent client management (PM-cum-tech-lead under a developer title)
- Process innovation (real-time QA verification pattern)
- Engineering economy (reuse over rebuild for visualization)
- Translating research-style algorithms into production-grade modules
- Government-client security engineering (RTSP under regulatory constraints)
- Direct application of prior expertise (self-driving car path prediction → roadside prediction)

KEY LEARNINGS:

"Client trust comes from seeing the system work, not from reading the accuracy number on a slide. Visualization isn't a nice-to-have — it's the proof."

"Engineer for headroom, not for the spec. 40ms typical / 2ms peak module means the system stays inside budget when traffic is worst, not when it's best."

"Real-time validation isn't just faster QA — it's a different relationship with the product. Replay-and-compare puts QA at the end of the cycle; live verification puts it inside the cycle."

"Reusing the RTSP publisher saved a week of work and produced a better client experience than a custom tool would have. Sometimes the right engineering choice is to use what's already there."

CONNECTION TO OTHER STORIES:

- **`02_iit_bombay_self_driving_car_leadership.md`** — same trajectory-prediction problem from a different vantage point (in-vehicle then; roadside now). Direct continuity of expertise.
- **`04b_derq_project_api_integration.md`** — same pattern of independent client leadership; same pattern of research-driven design over default conventional choices.
- **`04c_derq_project_atspm_redesign.md`** — same outcome shape (flagship status, faster-than-typical delivery).
- **`04d_derq_project_near_miss_detection.md`** — same problem family (event detection / prediction at intersections), different methodology.
- **Fire Detection** (in `04_*` role expansion): same "one engineering win → reusable pattern" instinct (Fire: standardized SigLIP module structure; Conflict Prediction: real-time QA verification).

ESSAY APPLICATIONS:

- Independent client leadership / "PM under a developer title"
- Innovation / process improvement (real-time QA verification)
- Engineering excellence under operating constraints (latency budgeting)
- Customer-centric design (visualization as trust-building, not feature)
- Continuity of expertise (IIT self-driving car → production prediction system)
- Cross-functional leadership (ML, QA, client IT)
- Delivering measurable results against demanding bars (97% vs 95%, 40ms vs 100ms)

CONNECTION TO MBA GOALS:

This project compresses three threads I'm hoping the MBA will help me scale:

1. **Strategic-vs-tactical product decisions.** The choice to invest in automated real-time verification (instead of grinding through the 7-day cycle) was the highest-leverage decision on the project. It compressed delivery, gave the client a better experience, and created a reusable pattern. But it was an intuitive call. MBA strategy frameworks will let me make calls of that shape consistently, across products I haven't built yet.
2. **Earning the role by doing the role.** On paper a Lead Developer, in practice a PM-cum-tech-lead. The MBA is the equivalent move at the industry level — earning the credibility (and the title) for the work I'm already doing.
3. **Founder-shape thinking.** Reusing the RTSP module instead of building a visualization tool is engineering economy. Real-time QA verification is process innovation. Both are founder instincts — solve the customer problem with what's already there, then turn the win into a reusable asset. The MBA, plus the long-term vision in `06_*`, is about scaling that mode from one project to one company.
