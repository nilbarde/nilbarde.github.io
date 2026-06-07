MONTREAL DOT OFFLINE DEPLOYMENT — CRISIS EXECUTION WITH VINDICATED JUDGMENT

**Project Type**: Major architectural shift — port Derq's cloud-first/AWS-based platform to a fully offline/air-gapped deployment for a single client.
**Role on paper**: Systems & Software engineer pulled in for the final sprint.
**Role in practice**: De-facto delivery lead for the sprint — cross-team coordination ran through me; PM and Full Stack lead made client-build-stage decisions with me directly.
**Client**: Montreal Department of Transportation (Canada).
**Other people in this story**:

- **Abhishek** — former teammate on Systems & Software; did the initial Montreal development months earlier; left the company ~2 months before the final sprint; gave KT to Akash and prepared onboarding docs.
- **Akash** — my manager. Initially believed my estimates were inflated and didn't act on my deadline flag; later acknowledged in writing that I was right.
- **Arijit Bose** — product manager on this project, and the same Arijit who wrote my LBS LOR (Senior PM, Oxford MBA). Saw this execution in real time. Apologized in writing for not acting on my early risk flags.
- **Harshal** — current teammate on Systems & Software; nominally co-owner for the sprint but pulled to another project for the first two days; later did real work but I asked him to rest during the overnight deployment.

**Timeline**: Final sprint = 10 business days. Deployment day = end of sprint. Overnight stabilization to ~5:30 AM Saturday after deadline. Weekend client monitoring. Post-mortem the following Mon/Tue with manager, PM, then CTO + 3× HR.

**Headline result**:

- Backend / Systems & Software stack — the part I owned — was production-ready ~6 hours before the deadline and deployed cleanly with zero failures on client side.
- Full Stack side (configuration tool, dashboard) had not been tested against client infrastructure and failed on client networks at deployment; I stepped in cross-team and stayed on until ~5:30 AM Saturday.
- ~20 hours of continuous work the day of deployment (lunch + dinner at the desk; mom kept the food coming).
- Through the next month of production monitoring: **zero failures attributable to my (Systems & Software) side.**
- Surfaced an architectural gap that had been latent in the product for ~8 years (no proper APIs to manage the backend software) — CTO and team leads asked me to lead the research and proposal for fixing it.
- Manager + PM both apologized in writing for ignoring my early estimation flag.
- Triggered an organizational review: long call with CTO + three calls with HR on planning failure and sustainable engineering. I framed the discussions as process improvement, not blame.

---

THE PROBLEM — CLOUD-FIRST PRODUCT, OFFLINE-FIRST CLIENT

Derq's standard architecture is cloud-connected:

- Online configuration via AWS.
- Deploy configs to edge units.
- Edge processes data and sends results back to AWS.
- Customers see events on an online dashboard.

Montreal DOT wanted the opposite: a fully offline system. They would do all configuration locally, deploy edge units themselves, and view data on their own server with a local dashboard — all with no internet dependency in production. Internet would be available only during initial installation; after install, the system had to be effectively air-gapped.

This was not a feature toggle — it was an architectural shift. Installation paths, configuration workflows, data flow, and dashboard delivery all had to be re-thought for an offline operating mode.

PROJECT HISTORY — INHERITED, PAUSED, AND HANDED DOWN

The project had started months earlier. Abhishek, then on my team, did the initial development. It was put on hold because of shifting priorities and dependencies on other teams that hadn't completed their pieces. Abhishek left the company about two months before the final sprint, doing KT with Akash (my manager) and writing onboarding/KT documentation before he went.

When the project came back live, I was pulled in for the **final sprint — 10 business days from deadline.** Harshal was the other named owner from Systems & Software.

INITIAL ALLOCATION — 20 + 20 HOURS, WHICH I DIDN'T BELIEVE

Akash assigned 20 hours to me and 20 hours to Harshal — 40 engineering hours total to finish a project I had never seen before, on an architectural shift the team had already paused once, with the original developer gone.

At sprint planning, before doing any work, I flagged this:

> "Even if you're assigning 20 hours for this, I'm not really sure we can do it in 20 + 20 hours. I have literally no idea what has been done and what's needed to be done to complete this."

The flag was acknowledged but not acted on. I learned only later (from Arijit) that Akash had told Arijit that I was "overestimating" and that once I started working, the remaining effort would shrink. Because of that internal read, **Arijit didn't try to renegotiate the deadline with the client** — a decision made without my visibility, on the assumption that my warning was inflated.

I didn't know this in real time. From my side, the deadline was simply communicated as non-negotiable.

FIRST TWO DAYS — SOLO DISCOVERY UNDER A DEADLINE

Harshal was pulled to another project for the first two days because another team urgently needed his prior context there. That left me solo for the discovery phase.

In those two days I:

- Read every KT and onboarding doc Abhishek had left.
- Walked the codebase end-to-end.
- Scheduled calls with leads of every dependent team to find out what had already been tested vs what was still incomplete.
- Identified bugs in our own codebase that Abhishek hadn't been able to get to before he left — most of them not mentioned in the onboarding documents.
- Mapped out the integration and internal testing still required.

By the end of day 2, I had a defensible scope estimate: the remaining engineering work alone was **at least two sprints for two people**, not one sprint. And I flagged a second structural problem — the early phase couldn't be parallelized:

> "Adding more people early won't help. One person has to own the setup and integration discovery before tasks can be cleanly split. The first half of this is investigative; only after that does parallelization make sense."

I communicated this updated assessment to Akash and Arijit. From their side it was again interpreted as inflated. From my side, the deadline was still non-negotiable. So I went into execution.

SCOPE TRIAGE — MUST / GOOD / LATER

Since I couldn't move the deadline, I moved the scope. I broke the remaining work into three buckets:

1. **Must-have** — required for the system to be functional and stable on the client's side. Non-negotiable.
2. **Good-to-have** — improvements and minor bugs we could ship around and fix later.
3. **Future sprint** — anything that wasn't a delivery blocker; production-hardening work that could safely wait.

The principle: **don't ship anything half-baked, but don't fight the deadline on the wrong battles either.** Even after this triage the must-have bucket alone still looked like ~two sprints, but it was now actionable and the deferred items were documented with explicit risk rationale.

EXECUTION (DAYS 3–10) — BACKEND OWNER, INTEGRATOR, COORDINATOR

From day 3 I was full hands-on. The shape of the work:

- I owned the **backend/Systems & Software side** end-to-end — making the C++ backend work in the offline architecture, fixing the installation scripts (most of which assumed cloud connectivity), closing the integration gaps.
- I ran **continuous syncs with the Full Stack team**, who owned the configuration tool and the local dashboard. Their work and mine had to integrate cleanly for the end-to-end flow to function.
- I tracked every newly discovered gap, blocker, or missing piece. Whenever something became independently executable, I delegated it to Harshal (once he was free) or to other engineers across the project.
- I kept end-to-end understanding centralized with myself so I could decide what to absorb and what to delegate.

The de-facto coordination structure that emerged:

- **Arijit (PM) and the Full Stack team lead came directly to me** for client-build-stage decisions and integration prioritization. Not to Akash.
- I deliberately mirrored every external decision back to Akash — what we were committing to the client, what other teams were doing, what was changing — so he'd never feel I was bypassing him. The story here isn't taking authority; it's exercising it cleanly while protecting hierarchy.

Personal load during this stretch: **12–14 hours daily** on this project alone.

I was also tracking hours — mine and the team's — against the original 40-hour estimate. Not for justification in the moment, but as evidence for the retrospective: I wanted to be able to say *exactly* how much the real work cost vs what was planned, so the next round of planning would be better.

MID-SPRINT — MANAGEMENT QUIETLY SHIFTS

Around day 7 or 8, with most major bugs identified and the team in heavy debug/integrate mode, Akash and Arijit independently realized my original assessment had been right. Both messaged me — in writing — to apologize:

- Akash acknowledged his earlier read that my estimates were "inflated" was wrong.
- Arijit acknowledged he should have acted on my early flags and not absorbed them as engineering pessimism.

Both said they'd push to prevent the planning pattern from recurring.

I logged this. Not as a win — as a calibration point. Specifically: *my judgment was right; the system around me ignored it; the same system later acknowledged the error.* That's a useful data point about what kind of seat I'm in and what kind of seat I'm not.

DEPLOYMENT DAY — BACKEND CLEAN, FULL STACK FAILS, I STEP IN

Engineering readiness going into deadline:

- **Systems & Software (mine)**: ready ~6 hours before deadline. Integration with Full Stack was smooth on my side.
- **Full Stack**: tested only on local machines in local environments. No realistic validation against the client's actual server or network conditions.

I flagged this to the Full Stack team lead before deployment:

> "We might face problems on client side — your team hasn't tested against their network or server."

His response: he knew, but there hadn't been enough time, and the client-side testing hadn't been planned for before the sprint.

Deployment day:

- **My backend stack deployed cleanly on client side. Zero failures.** The C++ software ran exactly as designed in the offline architecture.
- **Full Stack side broke on the client environment** — network restrictions, VLAN allow/deny rules, environment-specific assumptions that hadn't surfaced in local testing.

The end-to-end client workflow — *client opens the configuration tool → deploys → sees events on the dashboard* — wasn't working at point A.

Strictly speaking, the failures were outside my ownership boundary. I stepped in anyway. I have the strongest automation/scripting fluency on the engineering team for fast diagnostic and fix-iteration work, and at that moment the team needed those skills more than it needed neat ownership boundaries.

OVERNIGHT — 20 HOURS, RESTING THE TEAMMATE

I stayed online with the Full Stack team until **~5:30 AM Saturday** until the full workflow worked end-to-end on the client's environment.

Team availability that night:

- Akash was travelling and not available.
- Harshal had already worked ~12 hours that day. I asked him to rest.
- I'd already been working ~14–16 hours that day myself when the overnight stretch started. Total continuous work that day: **~20 hours.** Meals at the desk; mom kept the food coming.

The end-to-end flow worked before I logged off. Client could configure the system, deploy it, and see events on the local dashboard.

WEEKEND — MONITORING

I spent the weekend monitoring client systems remotely. Any time a server went down or an integration hiccuped, I flagged it to the Full Stack team and they came online — including on weekends — to fix it. The system stabilized over those two days.

POST-MORTEM — CTO + HR, FRAMED AS PROCESS NOT BLAME

Monday and Tuesday of the next sprint, I had follow-up calls with Akash and Arijit. Both reiterated their earlier acknowledgments and said the planning process needed to change.

Akash escalated this himself — he asked me to talk directly to the CTO and to HR to walk them through what went wrong and what should change. I had:

- One long call with the **CTO**.
- Three calls with **HR**.

Both Akash and Arijit are close colleagues and friends. I was very deliberate during these conversations not to frame anything as "they were wrong" or "they were incapable." I framed it as:

- The **process** that produced the 40-hour estimate had blind spots.
- The **planning system** didn't act on early risk flags from engineering — that's a fixable systemic issue, not a personal failing.
- Engineering should not be repeatedly absorbing 20-hour overtime days to ship things that sales has already sold.
- Production commitments need to better reflect engineering feasibility.

The CTO and HR took my feedback at face value — same dynamic I'd had with Arijit and the Full Stack lead during the sprint itself. Nothing was dismissed or minimized.

TECHNICAL DEBT — STRUCTURED TICKETS, RISK-HORIZON SEVERITY

The "good-to-have" and "future" buckets from my early triage didn't disappear — they were always going to come due. So in the first couple of days of the sprint, while doing discovery, I'd already opened **structured tickets** for every deferred item.

The severity model was unusual: not by bug-level severity (S1/S2/S3) but by **operational risk horizon** — how long after deployment until this becomes a problem if we don't fix it.

For example:

- *Edge unit lacks a file cleanup tool.* Not a blocker now. Will become a real operational problem in roughly a month as storage fills. So: high-priority, near-horizon — fix within the next sprint.
- *No proper APIs to manage backend software.* (More on this below.) Latent for years; high-priority, long-horizon — needs to be planned as a foundational improvement.

I presented these tickets to Akash, Arijit, and the CTO, and posted the full list to the product channel so prioritization could happen transparently and the debt wasn't quietly forgotten once the deadline pressure lifted.

THE 8-YEAR ARCHITECTURAL GAP — APIS FOR BACKEND SOFTWARE

The most consequential ticket from this set:

The product had **no proper APIs to manage the backend software.** Configuration, deployment hooks, runtime interactions — everything bypassed the kind of interface layer that a mature product would expose. This worked in the cloud-first architecture because cloud-side tooling could reach into the system in ad-hoc ways. In an offline architecture, where everything had to run within a constrained environment without cloud-side mediation, the absence of a clean API surface was a real structural weakness.

This is not a fancy or novel observation. APIs as a control plane for software is basic. **But the product had operated for ~8 years without it.** Surfacing it formally in this post-mortem context was the first time it was prioritized as a planned improvement rather than as "we'll get to it."

The CTO and team leads agreed it was the right call, and asked me to **research and propose the path forward** — which APIs, where, what changes to existing modules. As of the post-mortem this was queued as a next-cycle initiative under my involvement.

POST-RELEASE — A MONTH OF MONITORING

Over the following month/sprint, the team monitored production behavior closely. The most telling data point:

- **Zero failures originated from the Systems & Software components I owned.**

Several of the items I'd categorized as "non-blocking, fix later" did surface as legitimate stability improvements that needed prioritization — exactly what the risk-horizon ticketing was designed to capture. The fact that they surfaced predictably, rather than as surprise outages, was the system working as intended.

---

KEY ACHIEVEMENTS:

- Delivered a fully offline port of a cloud-first product to Montreal DOT under a 10-business-day final sprint, after being pulled in cold from the original developer's KT documentation.
- Owned and shipped the Systems & Software / backend portion clean — production-ready 6 hours before deadline, deployed without failure, zero post-release failures attributable to my side in the following month.
- Stepped in cross-team during deployment-night crisis (outside my ownership), stayed online until ~5:30 AM Saturday, kept the engagement deliverable instead of deferred.
- Asked an exhausted teammate (Harshal) to rest while I took the overnight; protected the team while taking the load.
- Flagged the unrealistic estimate at sprint planning, was overruled, was vindicated mid-sprint by both manager and PM in writing.
- Triaged the work into must / good / later buckets to make scope movable while the deadline wasn't.
- Tracked hours and gaps during execution to produce evidence-based retrospective material.
- Drove a constructive post-mortem with CTO + HR — framed as process improvement, not blame, despite Akash and Arijit being close colleagues.
- Surfaced an 8-year-old architectural gap (no proper backend APIs) and was asked to lead the proposal for fixing it.
- Structured technical debt tickets by **operational risk horizon** rather than conventional severity — a more useful framing for production stability planning.

QUANTIFIABLE METRICS:

- **10 business days** sprint window to deliver an inherited project I had never worked on.
- **40 hours** original engineering allocation (20 me + 20 Harshal); actual cost: multiple sprints of effort, ~12–14 hours/day for 8 days plus ~20 hours of overnight on deployment day.
- **6 hours** of buffer before deadline on my backend portion.
- **~5:30 AM Saturday** — overnight deployment stabilization point with Full Stack.
- **~20 hours** continuous work the day of deployment.
- **0 failures** from Systems & Software side in the following month of production monitoring.
- **~8 years** — duration the product had operated without proper backend-software APIs, surfaced and prioritized in this post-mortem.
- **2** management apologies in writing (Akash, Arijit) for ignoring early risk flags.
- **4** post-mortem escalation conversations (1 with CTO, 3 with HR).

SKILLS DEMONSTRATED:

- **Crisis execution under inherited context.** Cold pickup of a paused, partially-developed project from documentation alone, delivering the must-have scope on time.
- **Risk escalation and estimation discipline.** Flagged unrealistic estimate proactively at sprint planning with the rationale that justified it. Maintained position when overruled. Tracked execution data to validate it after the fact.
- **Cross-functional leadership without formal authority.** PM and Full Stack lead routed client-build-stage decisions through me — not because of title, but because operational fluency made me the most useful coordination point.
- **Upward management.** Continuously mirrored cross-team decisions back to my manager so my de-facto coordination role never created hierarchical friction.
- **Scope triage.** Must / good / later framing with explicit risk rationale, plus risk-horizon-based ticketing for deferred items.
- **Stepping outside ownership boundary.** Took on Full Stack debugging during deployment-night failure because the engagement needed it, even though it wasn't my surface.
- **Protecting the team during crunch.** Sent Harshal to rest while taking the 20-hour shift myself.
- **Sustained execution under load.** ~12–14 hours/day for the active sprint, ~20 hours on deployment day, weekend monitoring.
- **Constructive post-mortem framing.** Walked the CTO and HR through systemic process failures while protecting Akash and Arijit (close friends) from being framed as the cause.
- **System-level technical insight.** Surfaced an 8-year architectural gap during a crisis sprint, structured the proposal for fixing it.
- **Engineering trust-capital.** Same trust dynamic at execution layer (PM, Full Stack lead, teammates) and at leadership layer (CTO, HR) — feedback heard at face value, not minimized.

KEY LEARNINGS:

"Engineering estimates from someone who's read the code are not the same as estimates from someone who hasn't. When the system overrules the read-the-code estimate, the system is the part that needs to change."

"Deadlines are non-negotiable from leadership's side only until they're not. Scope is the lever — must / good / later, with the deferred items ticketed by *when* they'll cause a problem, not by some abstract severity."

"Cross-functional trust isn't permission you ask for. It's the residue of people watching you make decisions they would have made themselves."

"Manage up not by hiding the work, but by mirroring every external commitment back into the hierarchy. The manager keeps the seat; you do the work."

"Post-mortems with friends are still post-mortems. Frame the system, not the people. The system is what changes; the people stay."

"Surface foundational gaps from inside the work, not from outside it. The 8-year API gap was always there. Nobody fixed it because nobody had the platform to call it out and stay credible. Crisis delivery gave me that platform."

"Risk-horizon ticketing — 'this is fine for ~a month, then it isn't' — is more useful for production debt than abstract severity rankings."

CONNECTION TO OTHER STORIES:

- **`04_derq_overview_and_role.md`** — Montreal is one of the modules in the 2025-2026 role-expansion list. The role-expansion section also notes the structural-insight observation (teams operating in sequence rather than parallel) — Montreal is a concrete instance of that pattern: the original Abhishek work, the pause, the late hand-down, the cross-team dependency that wasn't ready when scheduled.
- **`04b_derq_project_api_integration.md`** — same client-leadership-through-trust pattern (Arijit delegating direct client coordination). Different stakes — that one was sustained client engagement; this one was crisis execution.
- **`04e_derq_project_conflict_prediction.md`** — same product manager (Arijit), same operating model (full coordination freedom under a developer title), same theme of "PM and Full Stack lead route work through me by choice, not by org chart." 04e is the positive-pressure version (clean delivery, flagship use case); 04f is the negative-pressure version (crisis, delivered but at human cost).
- **`arijit_lor_insights_and_additions.md`** — Arijit wrote my LBS LOR. He was the PM on this story in real time. The execution patterns the LOR describes (comprehensive understanding, market-differentiator-quality thinking, independent client management) are not theoretical for him — he watched them play out under the worst conditions on this project.
- **`08_hiring_team_building.md`** — same operating principle: respect the hierarchy publicly while actually doing the work that needs doing. (08 was the salary-negotiation version under team-building; here it's the cross-team coordination version under crisis.)
- **`06_career_goals_why_mba.md`** — Montreal feeds the "earning the role by doing the role" thread *and* the "structural-insight gap" thread (the 8-year API gap is the concrete artifact). The fact that the CTO and HR took my feedback at face value is the evidence that the seat I'm earning is structural; the gap is what tells me I need MBA-grade frameworks to fill that seat consistently.

ESSAY APPLICATIONS:

- **Disagreement with authority that turned out to be right.** Strong material for "tell us about a time you disagreed with a manager / senior stakeholder." Most candidates have one of: (a) disagreed and won by force, or (b) deferred and the senior was right. The unusual version here is: disagreed, was overruled, executed the senior's plan anyway, was vindicated by results, *and* drove a constructive systemic fix afterward.
- **Crisis execution / firefighting under deadline.** The 10-day inherited-project + ~20-hour deployment day is unusually concrete crisis material.
- **Leadership without formal authority.** The de-facto coordination role for PM and Full Stack lead while keeping the manager in the loop is a clean illustration.
- **Ownership / accountability.** Stepping into Full Stack failures on deployment night despite being outside ownership boundary; sending Harshal to rest while taking the overnight.
- **Constructive postmortem / influence with senior leadership.** CTO + HR conversations framed as process improvement when the easy framing would have been blame.
- **System-level / strategic thinking under tactical pressure.** Surfacing the 8-year API gap *during* a crisis sprint, not after the dust settled.
- **Failure / what would you do differently.** Strong candidate: the failure is partly the system's (planning ignored the flag) but also partly mine (the flag could have been escalated harder, written down rather than verbal, escalated to PM rather than only to manager). Honest failure-essay material.
- **Resilience.** 12-14 hour days for 8 days followed by a 20-hour deployment day with meals at the desk. Don't lead with this — lead with the judgment that made the time investment count.
- **Process innovation.** Risk-horizon ticketing is a small but specific operational innovation.
- **Sustainable engineering / care for team.** Pairs with `08_*` (hiring policy advocacy) and `05_*` (mentorship) as a consistent throughline of advocating for the engineering org's sustainability, not just shipping.

CONNECTION TO MBA GOALS:

Three threads from `06_*` show up explicitly in this project:

1. **Earning the role by doing the role.** I had no formal authority to coordinate Full Stack and Backend at the client-build-stage level. Arijit and the Full Stack lead chose to route decisions through me anyway. The CTO and HR chose to take my post-mortem feedback at face value. None of that came from a title. It came from a track record. The MBA is the industry-scale version of the same move — earning the credibility (and the title) for work I'm already doing.
2. **Structural-insight gap.** The 8-year API observation is concrete evidence of the pattern. I can see the foundational shape of a problem at engineering level. What I'm missing — and what the MBA is for — is the frameworks to do this on strategy, market, and org questions with the same confidence I have on engineering ones. Right now my structural-insight reach ends at the edge of the technical surface; I want it to keep going.
3. **Founder-shape thinking.** The risk-horizon ticketing, the must/good/later triage, the deliberate scope-vs-deadline tradeoff, the constructive post-mortem framing — these are operator instincts, not engineer instincts. The MBA + the long-term smart-eyewear vision is about scaling these instincts from one project to one company.

CAUTIONARY NOTE FOR ESSAY USE:

This story has high-impact material, but two angles need careful handling:

- **Don't frame Akash or Arijit as the problem.** Frame the *planning system* as the problem. Both have apologized, both are close colleagues, Arijit wrote my LOR. The respectful framing is also the truthful one — they were operating in a system that didn't surface engineering risk well, and they're now working to fix it.
- **Don't lead with hours.** "I worked 20 hours" is what 5,000 other applicants will write. Lead with judgment (the must/good/later triage, the risk-horizon ticketing, the cross-team trust, the post-mortem framing). The hours are the supporting detail, not the headline.
