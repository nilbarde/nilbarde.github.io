NDS VIDEO-PROCESSING PROJECT — FROM CONTESTED ESTIMATE TO A SEAT AT THE STRATEGY TABLE

**Project Type**: Recorded-video (offline footage) processing for a client, on a platform architected for live camera feeds — a long-deprioritized "one-off" category that this engagement turned into a productized line of business.
**Role on paper**: Subject-matter expert / estimator; later the hands-on developer when capacity collapsed.
**Role in practice**: The single point of knowledge for recorded-video work, the person who set the estimate the whole project hung on, the engineer who salvaged it with a product change, and now a voice in executive strategy on whether and how to compete in this space.
**Client**: **NDS** — a traffic-analytics middleman that aggregates work across multiple U.S. states and delivers to Departments of Transportation. The deliverable here was a sample project NDS owed to a DoT down the chain.
**Other people in this story**:

- **Ankit** — engineering manager (works from the US). Reviewed my estimate, judged it ~2x too conservative, cut it ~50%, argued the "clients should follow guidelines" position in review. Later DM'd me unprompted to apologize once the data problems I'd predicted materialized. Warm reconciliation; we ended on a personal note about his newborn.
- **Akash** — my manager. Gave me significant estimation autonomy on the strength of my track record, and backed my assessment to engineering leadership. (Note the inversion vs. Montreal `04f`, where Akash was the one who read my estimate as inflated — here he's on the other side of the same kind of dispute.)
- **Arijit Bose** — product manager (Senior PM, Oxford MBA; wrote my LBS LOR). Convened the CTO discussion, created the project tickets from the approved estimate, relayed the client picture, and asked the client (twice) for relief that never came.
- **Ty** — CTO. Initially sided with Ankit against my estimate; after the written risk case, approved my original estimate; later made the explicit NJDOT-vs-NDS trade-off call and gave me the latitude to attempt both.

**Timeline**: Estimation dispute → CTO-led review → approval → execution begins → ~1 week in, NJDOT/FIFA emergency pulls both primary contributors → failed deadline renegotiation → early data validation (predicted problems confirmed) → middleman reality (deadline truly immovable) → CTO trade-off call → overnight product-extension breakthrough (~4 AM events, ~6 AM data) → Ankit's apology → business win + productization + senior title.

**Headline result**:

- The org **reversed a years-long deprioritization** of recorded-video work and decided to **build it into a product** — and pulled me into **executive-level strategy** on how to deliver it faster/better than competitors. This is the arc: one contested estimate by an IC became the trigger for a strategic line of business, with that IC now in the room shaping it.
- Salvaged a near-dead deliverable by **extending the product itself** — a parameter tuning/learning mechanism so the near-miss detector could surface events the raw footage "couldn't" produce. I made this product change **on my own, overnight, without consulting the researchers or product managers** because the time crunch left no room to — a judgment call to alter the product unilaterally. **Now live in production**; once the deadline passed I walked the researchers (who own the core near-miss logic) and the PMs through it, and they reviewed and **appreciated** the improvement.
- The relationship NDS opened is now **ongoing business**, expected on the order of **~10% of annual company revenue** *(estimate — verify before essay use)*; NDS has already sent more videos and more client opportunities.
- Delivered **both** NDS and the higher-stakes NJDOT/FIFA deadline, exactly as I'd assured the CTO. (NJDOT is its own story.)
- Engineering manager apologized in writing for assuming my estimate was bloated and for missing the risks I'd flagged.

---

THE PROBLEM — A LIVE-FEED PRODUCT, AN OFFLINE-FOOTAGE REQUEST

Derq's platform is designed and optimized to process **live traffic camera feeds**. Some clients can't provide a live feed and submit **recorded video** instead, which needs special handling outside the standard workflow. Over the years engineers had repeatedly adapted live pipelines to recorded footage on a case-by-case basis — special-case implementations, never part of the original product design.

The economics of this category made it an orphan:

- Recorded-video requests are rare — roughly **once every six months**.
- Over ~4 years I'd worked on about **five** of them.
- Every one surfaced a *different* set of problems — no two alike, no repeatable playbook.
- The company never invested in dedicated tooling, workflow, or documentation. Product and project teams **consistently deprioritized** it as exception work.

Net effect: most of the practical knowledge about these engagements **lived with me.** The organization had an unmade strategic choice in front of it — decline these one-offs, or, if they were going to keep coming, invest in tooling and process. It kept choosing neither.

WHY THIS ONE WAS DIFFERENT — NDS

The NDS engagement broke the "one-off" pattern on the business side:

- NDS was willing to **pay a meaningful amount.**
- NDS signaled interest in **future engagements** spanning both recorded-video and Derq's traditional live-processing solutions.
- On revenue potential + long-term-relationship upside, **product leadership and executives decided to pursue it.**

CONFLICT #1 — THE ESTIMATE

Product leadership asked Akash and me for an engineering effort estimate. Akash gave me significant autonomy given my history with this work. I built the estimate on the **actual workflow** I expected — known platform limitations, historical challenges from prior video projects, the high likelihood of uncovering *new* issues mid-execution, and the manual effort that always goes into adapting live pipelines to recorded footage. Grounded in operational experience, not theoretical best case.

Ankit, the engineering manager, reviewed it and disagreed — called it overly conservative, argued the work should take substantially less effort, and **cut the estimate ~50%** before it went to the product team.

That set the tension at the very start: I believed the number reflected true complexity; leadership was about to commit a timeline and budget to a number half that size; the project would enter execution with expectations misaligned from the real technical risk.

ESCALATION — THE ROOM SIDES AGAINST ME FIRST

The gap was big enough that Arijit (PM) wasn't sure whose number to trust. He convened **PM, CTO (Ty), Ankit, Akash, and me.** Ankit reiterated the work could be done in ~half my estimate. **Ty initially sided with Ankit.** The two most senior technical leaders were now questioning an estimate I was holding on hands-on experience.

The decision point: I chose **not** to argue from authority or seniority of experience — I chose to argue from **evidence**.

BUILDING THE EVIDENCE — A RISK-BASED, STAGE-BY-STAGE ESTIMATE

I wrote a detailed breakdown of the full workflow. For every stage I documented the specific task, why it was necessary, expected effort, the historical issues from prior projects, and the risks. Stages: downloading and validating client data; sanitization and prep; converting client data into pipeline-compatible formats; running the processing workflows; troubleshooting failures; validating outputs; re-processing when required.

I shared it with all stakeholders and made the core point: this was **cumulative real effort, not arbitrary buffer.** I also surfaced the historical pattern explicitly — across ~5 prior projects, new issues emerged almost every time, no two behaved alike, complications were the norm. I warned there was a **high probability of at least one never-before-seen issue**, and argued for **contingency** rather than ideal-execution assumptions.

The recurring point of disagreement was **client data**:

- Ankit's view: clients get submission guidelines → clients should follow them → engineering effort shouldn't include time to fix client mistakes.
- My experience: clients **rarely** submit data exactly as requested. Even with clear guidelines, data arrives with formatting issues, missing fields, inconsistencies, or structural differences that block direct processing — leaving two options: reject and wait, or sanitize/adapt it to protect the timeline. Historically it was almost always the latter.
- My argument: **ignoring that effort in estimation doesn't eliminate the work — it hides it until execution.**

The split never fully closed in the room: **planning on ideal client behavior vs. planning on actual historical experience.** Before a dedicated session with Ankit, I walked Akash through the full workflow, history, and rationale; he backed my assessment, reasoning that my multi-year track record made me best positioned to estimate.

INFLUENCE THROUGH DOCUMENTATION — APPROVAL

Agreement was never fully reached verbally. So I summarized the rationale, risks, and assumptions **in writing** for the broader group. After reviewing it, **Ty approved my original estimate.** Arijit created the tickets from it. I added one final written warning: even at the approved number, additional effort remained likely if new issues surfaced. That created a **documented record of risk before any work began** — expectations aligned to reality as closely as they could be.

EXECUTION — SME ROLE, AND THE CAPACITY COLLAPSE

The PM assigned an engineer **from another team** for hands-on implementation. My role was **subject-matter expert** — knowledge transfer from prior projects, technical direction, code/implementation review, troubleshooting, owning the correct workflow. I set up **daily working sessions** with the engineer for KT and ongoing review. At the same time I was supporting the **Montreal deployment** (`04f`) — a live client needing maintenance and multi-team coordination. So: a live deployment, client/internal coordination, primary expert on NDS, and mentoring the engineer, all concurrently.

About **a week in**, a non-negotiable **NJDOT** project surfaced that had to ship before the **FIFA World Cup**: a major feature still needed ~**3 sprints** of work with only **1 sprint** left, plus pending configuration. On my delivery track record, I was pulled onto the critical NJDOT development; the engineer I'd been mentoring was reassigned to NJDOT configuration. **Both primary contributors to NDS vanished at once.**

I recommended **extending the NDS timeline.** Arijit asked NDS; **the client refused** — the request came only a week before the agreed deadline, planning was already done, postponement unacceptable. The project stayed active on reduced capacity.

Management explored handing NDS to **another engineer.** The blockers: specialized, undocumented knowledge; no prior video-processing experience on their side; no time for me to onboard them under the NJDOT crunch; too many historical caveats to transfer quickly. Before reporting up, that engineer **consulted me directly.** I was honest — more complex than it looks, surprises every time, success not guaranteed even with guidance. They **independently reached the same conclusion** and told management taking over carried substantial risk. Business stakeholders still held that the commitment had to be honored.

VALIDATING EARLY — THE PREDICTIONS LAND

Under pressure to "keep progressing," I chose **not** to proceed blindly. I spent extra hours validating NDS's data **before** sinking effort in. The review **immediately** surfaced problems:

- The submission **did not conform** to the data-prep guidelines provided — significant enough that direct processing would likely fail downstream. This was the **exact "clients don't follow guidelines" scenario Ankit had dismissed** at estimation.
- A second, business-level issue: NDS's goal was **near-miss / crash-scenario analysis**, but the sample footage showed **very low traffic volumes.** My read: generating statistically meaningful near-miss insight from this data would be **extremely difficult even if processing technically succeeded.**

I documented both. Arijit relayed them to NDS; the team expected NDS would need to **correct and resubmit** — which looked, briefly, like breathing room while validating the risks I'd flagged at the start.

NO BREATHING ROOM — THE MIDDLEMAN REALITY

Then Arijit came back with the real picture: **NDS is a middleman** working across several states, and this was a **sample project NDS owed to a Department of Transportation** down the chain. Because of where it sat, the deadline **could not be extended at all** — the data had to be processed and *something usable* produced regardless. **The deadline could not move again.**

THE CTO CALL — NAMING THE TRADE-OFF

Ty laid out the bigger picture directly:

- The deadline was immovable.
- He knew I was also on NJDOT.
- The strategic framing: miss **NDS** and we risk losing this client **and the multiple future projects** the middleman could bring; but miss **NJDOT** and we damage our **standing in the market** on a high-visibility, on-time commitment — *more* dangerous.
- His instruction: he could "deal with" the NDS situation, but I **should not jeopardize NJDOT.**

Weighing the multiple future opportunities at stake, I told Ty **I'd take on NDS and try to get results** — on his condition that NJDOT not be compromised. I assured him **NJDOT would not suffer from my side**, and that I'd try to deliver **both**, because both mattered to the business and our market standing.

THE BREAKTHROUGH — EXTENDING THE PRODUCT TO MAKE THE DATA WORK

I worked through the video data, and exactly as I'd warned, it was **genuinely hard to surface any near-miss / crash events** in the footage — no events coming through, processing failing. Rather than report a dead end, I **designed a new mechanism and upgraded the software** so it could **tune/learn the parameters** to detect more events — a decision to **add new functionality to the product itself.** With the deadline hours away, I made this product change **unilaterally — overnight, without looping in the researchers who own the core near-miss logic or the product managers** — because there was simply no time to convene them. Altering a shipped product on my own judgment was a real risk; I took it. It worked.

The cost: I worked until ~**4 AM**; after the changes, we **started receiving events** — real data to take back to NDS. I had everything set up by ~**6 AM** and could generate the deliverable.

THE APOLOGY — AND CHOOSING FORWARD

Ankit, online in his US late-evening (my early morning), saw my channel messages reporting we were now getting good near-miss signal. He **DM'd me to apologize** unprompted — owned that he'd assumed my estimates were bloated and **hadn't realized the risks** I'd flagged, said it wouldn't happen again. Because he came to me on his own, I told him there was **no need to dwell** — the focus should be forward, on not putting ourselves in positions where we're working till 4–5 AM to ship. We ended warm, with a personal chat about his **newborn.**

OUTCOMES & RESOLUTION

**Business**

- Even NDS **didn't expect much** from that data — but was **happy we produced near-miss events**, which the end client needed.
- NDS has **already sent more videos** and opened **more opportunities with more clients** — now an **ongoing business relationship.** This is the exact upside Ty weighed on the trade-off call.
- Revenue: no exact figure yet, but the relationship is expected to contribute on the order of **~10% of annual company business.** *(Estimate — verify the basis/number before putting it in an essay.)*

**NJDOT** — *separate story.* Short version: **delivered on time, well-tested, everyone happy** — both projects landed, as I'd assured Ty.

**The improvement is in production** — the near-miss product extension is **live.** I'd built and shipped it overnight on my own judgment under the crunch; *after* the deadline I walked the **researchers** who own the core near-miss logic and the **product managers** through what I'd changed and why. They **reviewed it and appreciated the improvement** — the after-the-fact endorsement from both technical and product sides that the unilateral call had been the right one.

**Productization + a seat at the table** — the org decided to **build this into a product**, reversing the years-long deprioritization in §1. **Ty and other executives now discuss the strategy directly with me** — whether to take these projects, what the risks are, how to **deliver better and faster than competitors.** I'm giving input and developing ideas with the CTO on **improving the processing pipelines** for video-processing needs.

**Role, title & scope** — my move to **Senior Software Developer** (from Software Engineer), the **compensation increase**, and **more say over several products** where I have expertise did **not** come from this project. They came from **consistently delivering in a collaborative environment over time, plus a handful of courageous calls** like the ones in this story (holding the estimate, the trade-off commitment, the overnight product change). NDS is one example in that pattern, not its cause — keep that attribution honest in any essay.

---

KEY ACHIEVEMENTS:

- Turned a contested, halved estimate into an **approved** one by shifting the CTO's position with a structured, written, stage-by-stage risk case — evidence over hierarchy.
- Predicted the two failure modes (non-compliant client data; insufficient traffic volume for meaningful near-miss analysis) that **both materialized** during execution — credibility built before any data existed to prove me right.
- **Salvaged a near-dead deliverable by extending the product itself** — a parameter tuning/learning mechanism to surface near-miss events the raw footage "couldn't" produce. Built and shipped it **unilaterally overnight** under the crunch (no time to consult researchers or PMs); now live in production, and **endorsed by both researchers and product after the fact.**
- Made a **business-judgment call under a hard constraint** — committed to NDS *and* protected the higher-stakes NJDOT/FIFA deadline when Ty named the trade-off; delivered both.
- Catalyzed a **strategic reversal** — the org committed to productizing recorded-video work and pulled me into **executive strategy** on how to compete in it.
- Converted a one-off into an **ongoing client relationship** (~10% of annual business, to verify) that's already bringing more videos and more clients.
- Turned a vindication into a **repaired relationship** — accepted Ankit's apology, redirected to forward-looking process change, kept the colleague.

QUANTIFIABLE METRICS:

- **~1 per 6 months** frequency of recorded-video requests; **~5** such projects over **~4 years**, with knowledge concentrated in one person (me).
- **~50%** — amount the engineering manager cut my estimate before approval was reversed back to my original number.
- **2 of 2** pre-execution risk predictions (data non-compliance, low traffic volume) confirmed during the project.
- **~3 sprints** of NJDOT work compressed into **~1** remaining sprint — the emergency that pulled both NDS contributors.
- **~4 AM** first events after the product extension; **~6 AM** deliverable generated.
- **In production** — built unilaterally overnight, then **reviewed and appreciated by both** core-logic researchers and product managers after the deadline.
- **~10%** of annual company business — expected contribution of the NDS relationship *(estimate, verify)*.
- **Senior Software Developer** title (from Software Engineer) + compensation increase + expanded product say — attributable to **consistent collaborative delivery and courageous calls over time**, not to this project alone.

SKILLS DEMONSTRATED:

- **Evidence-based influence / influence without authority.** Moved the CTO not by seniority but by a structured, written, risk-based case against two more-senior technical leaders.
- **Expert judgment under organizational skepticism.** Held a reality-grounded estimate when the room initially sided against it; the core fight was epistemic (whose model of reality), not technical.
- **Forecasting credibility.** A track record of predictions that kept proving correct — the spine that earned the eventual strategic seat.
- **Decision-making under a hard constraint.** When the deadline genuinely couldn't move, committed to both projects and protected the higher-stakes one; a business call, not just an engineering one.
- **Innovating under pressure.** Extended the product (parameter-tuning mechanism) to make an "impossible" deliverable real, instead of reporting a dead end.
- **Cross-functional leadership & mentoring without authority.** Daily KT/review sessions guiding an engineer from another team.
- **Juggling competing priorities.** Montreal (`04f`) live support + NDS SME + NJDOT critical development concurrently.
- **Grace in winning.** Chose forward-looking reconciliation over "I told you so"; turned conflict into a repaired relationship (EQ signal).
- **IC-to-strategic-voice transition.** A single early stand + execution moved the org to reverse a deprioritization and pull me into exec strategy — the bridge from engineer to product/business leader.

KEY LEARNINGS:

"Ignoring effort in an estimate doesn't eliminate the work — it just hides it until execution. The argument for contingency isn't pessimism; it's refusing to let the plan lie to itself."

"When you can't out-rank the room, out-document it. A written, stage-by-stage risk case shifted the CTO when verbal experience couldn't."

"Forecasts compound into a seat. None of the predictions individually was dramatic; the *pattern* of being right is what eventually put me in the strategy room."

"Under a hard constraint, the question isn't 'which project do I save' — it's 'how do I protect the higher-stakes one *and* still try for the other.' Naming the trade-off out loud with the CTO made that possible."

"When the dead end is the product's limit, sometimes the move is to change the product. The parameter-tuning extension is now a permanent capability, not a one-off rescue."

"When someone apologizes on their own, take the win forward, not backward. The relationship is worth more than the vindication."

"My biggest miss was believing 'one-off' when my own experience said otherwise — and skipping documentation because of it. The business *did* make the mistake again, and more projects *did* come. Trust the intuition; document even the work you're told you'll never repeat."

CONNECTION TO OTHER STORIES:

- **`04f_derq_project_montreal_offline.md`** — the closest sibling, and a deliberate **inversion** worth knowing for essay selection. Both are estimate-disputes-then-vindication. But in Montreal, **Akash** read my estimate as inflated and the deadline genuinely couldn't move; here, **Akash backs me** and **Ankit** is the skeptic, and the vindication comes through a *product breakthrough* and a *business win* rather than a crisis post-mortem. Use Montreal for "disagreement with authority / crisis execution / constructive postmortem"; use NDS for **"IC → strategic voice / evidence-based influence / innovation-under-pressure."** They should not be used in the same application for the same theme.
- **`04e_derq_project_conflict_prediction.md`** — same near-miss/conflict domain and same PM (Arijit). 04e is the clean-delivery flagship version of near-miss work; the NDS product extension here is a *new capability added to that lineage* (parameter tuning to surface events in sparse data).
- **`04d_derq_project_near_miss_detection.md`** — the core near-miss/severity logic this project extends. The researchers who signed off on my improvement are the owners of that logic.
- **`04_derq_overview_and_role.md`** — this is a new entry in the 2025–2026 role-expansion list, and a concrete instance of the structural-insight observation: I see the foundational shape of a problem (recorded-video as an un-productized orphan) and now have the platform to push it onto the roadmap.
- **`08_hiring_team_building.md` / `04f`** — same throughline of advocating for the engineering org's sustainability (the "let's not work till 4–5 AM" framing to Ankit) alongside shipping.
- **`06_career_goals_why_mba.md`** — strongest feeder for the **"earning the role by doing the role"** thread (the senior title + product ownership came from *consistent collaborative delivery and courageous calls over time*, of which this project is one example — not from one project) and the **structural-insight gap** thread (I can see the orphan-category problem and now sit in the strategy conversation — but want MBA-grade frameworks to do this on market/strategy questions with the confidence I have on engineering ones).
- **`arijit_lor_insights_and_additions.md`** — Arijit (LBS LOR writer) was the PM here too; another real-time corroboration of independent client management and market-differentiator-quality thinking.

ESSAY APPLICATIONS:

- **From individual contributor to strategic/business leader (the headline).** One IC's contested estimate + execution reversed a years-long org decision and earned a seat in executive strategy. Strong for "describe your impact," "leadership," "why MBA / why now," and PM-track narratives.
- **Influence without authority / persuading senior stakeholders.** Moving the CTO with a written risk case against two senior leaders — clean for "a time you influenced a decision" or "disagreed with leadership."
- **Innovation under pressure.** Extending the product to surface events from unworkable data — for "innovation," "creative problem-solving," "above and beyond."
- **Business judgment under constraint.** The NJDOT-vs-NDS trade-off and delivering both — for "difficult decision" / "competing priorities."
- **Resilience + EQ.** The crunch is real but should be the supporting detail; the apology-handled-with-grace beat is the maturity signal.
- **What you'd do differently.** Honest failure material: believing "one-off" and skipping documentation against my own experience — and wanting sharper, evidence-framed persuasion that could win an Ankit over *before* data exists to prove me right.

CAUTIONARY NOTE FOR ESSAY USE:

- **Don't frame Ankit (or Ty) as the antagonist.** Frame the *estimation/planning culture* — "plan on ideal client behavior vs. historical reality" — as the thing that needed to change. Ankit apologized unprompted, owned it, and we reconciled warmly; the respectful framing is also the accurate one. Ty changed his position on evidence, which is exactly what you want a CTO to do.
- **Don't lead with the all-nighter.** The ~4 AM / ~6 AM detail is vivid, but top programs read "worked till 4 AM" as a sustainability/process red flag if it's the hero moment. Lead with judgment (evidence-based influence, the product extension, the trade-off call) and let the hours be supporting texture — which is exactly the framing you used with Ankit.
- **Verify the ~10% revenue figure before it goes in an essay.** It's currently an estimate; get the basis or a harder number, or phrase it qualitatively ("a relationship that's become a meaningful, recurring share of our business").
- **NDS is a real client name.** It's named here in the canonical record per your decision; consider whether any given school essay needs the literal name or whether "a traffic-analytics middleman delivering to a U.S. DoT" is safer for the submitted copy.
- **Don't attribute the senior title/comp to this single project.** It came from *consistent collaborative delivery and a pattern of courageous decisions* over time; NDS is one illustration, not the cause. Claiming one project earned a promotion reads as inflated and isn't accurate.
- **Frame the unilateral overnight product change as judgment, not cowboy.** The right framing: under a hard constraint with no time to convene the owners, I made a calculated call to alter the product, *then* brought the researchers and PMs in and earned their endorsement after the fact. It's a story about good judgment under pressure plus accountability after — not about bypassing process.
