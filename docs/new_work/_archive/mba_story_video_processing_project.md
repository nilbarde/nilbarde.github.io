# MBA Story Repository — Video-Processing Project

> **Status:** Fact-gathering in progress. This is a structured record of events, not a drafted essay. Themes are flagged at the bottom for later use.

---

## 1. Project & Organizational Context

- The project involved processing **recorded traffic videos** for a client — **NDS** (traffic analytics domain). NDS is a middleman that works with multiple U.S. states; see §13.
- The company's core platform was designed and optimized to process **live traffic camera feeds**, not previously recorded footage.
- Some clients can't provide live feeds and instead submit recorded video. Running analytics on this required **special handling** outside the standard workflow.
- Over the years, engineers had repeatedly **adapted live-processing pipelines** to handle recorded video on a case-by-case basis. These were special-case implementations, never part of the original product design.

**Frequency & ownership of knowledge**
- Recorded-video requests are rare — roughly **once every six months**.
- Over ~4 years, I worked on about **five** such projects.
- The company never formally invested in dedicated workflow, tooling, or documentation for these.
- Each project surfaced a *different* set of challenges → no repeatable playbook existed.
- As a result, most practical knowledge about these engagements **resided with me**.

**My standing position going in**
The organization needed to make a strategic choice:
1. Decline / avoid investing heavily in one-off requests, **or**
2. If these engagements were expected to continue, allocate time to document recurring issues, build tooling, and create a repeatable process.

Because requests were sporadic and treated as exceptions, product and project teams **consistently deprioritized** this investment. No dedicated engineering time went to documentation, tooling, or fixing underlying technical gaps.

---

## 2. Strategic Importance of This Opportunity

This engagement differed from prior video-processing projects:
- The client was willing to **pay a meaningful amount**.
- The client indicated interest in **future engagements** spanning both recorded-video processing and the company's traditional live-processing solutions.
- Because of the revenue potential and a possible long-term relationship, **product leadership and executives decided to pursue it**.

---

## 3. Estimation Phase

- Once the company committed to exploring the project, product leadership approached **my manager and me** for an engineering effort estimate.
- Given my prior experience, my manager gave me **significant autonomy** to evaluate and estimate.
- I built the estimate on the **actual workflow** I expected would be required, accounting for:
  - Known limitations of the existing platform
  - Historical challenges from previous video-processing projects
  - Likelihood of uncovering *new* issues during execution
  - The manual effort typically needed to adapt live pipelines for recorded footage
- Goal: a realistic assessment grounded in **operational experience**, not theoretical assumptions.

---

## 4. Conflict #1 — The Estimation Dispute

- The **engineering manager** reviewed my estimate and disagreed, calling it overly conservative.
- He argued the work should require substantially less effort.
- Despite my experience, the estimate was **cut by ~50%** before being shared with the product team.

This created tension at the very start:
- I believed the estimate reflected true complexity.
- Leadership was committing to a timeline/budget based on a significantly reduced number.
- The project was entering execution with expectations misaligned with the real technical risks.

---

## 5. Escalation & Initial Leadership Alignment Against Me

- The discrepancy was large enough that the **product manager** was unsure which assessment to trust.
- The PM convened a discussion group: **PM, CTO, Engineering Manager, My Manager, Me.**
- In the discussion, the engineering manager reiterated that the project could be done in ~half my estimate.
- **The CTO initially sided with the engineering manager.**
- I was now in a tough spot: the two most senior technical leaders questioned my estimate, while I was relying on hands-on experience.
- Decision point: rather than arguing from authority or experience alone, I chose to **support my position with evidence**.

---

## 6. Building a Structured, Risk-Based Estimate

I created a detailed breakdown of the full workflow. For every stage I documented:
- The specific task
- Why it was necessary
- Expected effort
- Historical issues from prior projects
- Risks associated with each stage

Stages covered included: downloading and validating client data; data sanitization and prep; converting client data into pipeline-compatible formats; running processing workflows; troubleshooting failures; validating outputs; re-processing when required.

I shared the document with all stakeholders and explained the estimate was **cumulative real effort**, not arbitrary buffer.

**Highlighting historical patterns**
- Video-processing projects consistently behaved differently from standard engineering work.
- Across ~5 prior projects: new issues emerged almost every time; no two behaved alike; unexpected complications were the norm.
- I warned that even *my* estimate might not fully capture eventual effort, and that there was a **high probability of at least one new, never-before-seen issue**.
- I argued for building in **contingency** rather than assuming ideal execution.

**Dedicated session with engineering leadership**
- The engineering manager remained unconvinced and scheduled a focused discussion with my manager and me.
- Beforehand, I walked **my manager** through the full workflow, history, and rationale. He **supported my assessment**, reasoning that my multi-year track record made me best positioned to estimate.
- In the meeting, I justified each component systematically.

**The recurring point of disagreement — client data**
- Engineering manager's view: clients get submission guidelines → clients should follow them → engineering effort shouldn't include time to fix client mistakes.
- My experience: clients **rarely** submit data exactly as requested. Even with clear guidelines, data arrives with formatting issues, missing info, inconsistencies, or structural differences that block direct processing.
- That leaves two options: (1) reject and wait for the client to fix it, or (2) spend effort sanitizing/adapting it to keep the timeline.
- Historically, projects almost always required option 2.
- My argument: ignoring this effort in estimation **doesn't eliminate the work — it just hides it until execution.**
- The discussion kept returning to the same split: **planning on ideal client behavior vs. planning on actual historical experience.**

---

## 7. Influencing Through Documentation → Approval

- Full agreement was never reached in the discussions, but I summarized the rationale, risks, and assumptions **in writing** for the broader group.
- After reviewing it, the **CTO ultimately approved my original estimate.**
- The PM created project tickets based on those estimates.
- I documented one final written warning: even with the approved estimate, additional effort remained likely if previously unseen issues emerged.
- This created a **documented record of risk before work began**, aligning expectations as much as possible with reality.

---

## 8. Execution Begins

- The PM assigned an engineer **from a different team** to do hands-on implementation (coding, system config, running workflows, technical tasks).
- My role: **subject matter expert** — transferring knowledge from prior projects, guiding technical decisions, reviewing code/implementation, troubleshooting, ensuring the correct workflow.
- I set up **daily working sessions** with the engineer for (1) knowledge transfer and (2) ongoing review and guidance.

**Competing responsibilities at the same time**
- Supporting the **Montreal deployment** (a separate live client project needing ongoing maintenance and multi-team coordination).
- So simultaneously: supporting a live deployment, coordinating with clients/internal teams, acting as primary expert for the video project, and mentoring the engineer.

---

## 9. Sudden Priority Shift — NJDOT / FIFA World Cup

- ~1 week after the video project began, a **non-negotiable, deadline-driven NJDOT project** emerged that had to be completed before the FIFA World Cup.
- The challenge:
  - A major software feature still needed development (~**3 sprints** of work).
  - Only **1 sprint** remained before the deadline.
  - Additional configuration work was also pending.
- Because of my delivery track record, **I was assigned the critical development work**.
- The engineer I was mentoring on the video project was **reassigned** to NJDOT configuration work.
- Net effect: the **two primary contributors** to the video project suddenly became unavailable.

---

## 10. Attempt to Renegotiate the Deadline

- Recognizing the conflict, I recommended **extending the video-processing timeline**.
- The PM asked the client; **the client refused.**
- Client's reasoning: the request came only one week before the agreed deadline; significant planning was already done; postponement wasn't acceptable.
- The project stayed active despite reduced capacity.

---

## 11. Challenges Reassigning Ownership

- Management explored assigning **another engineer** to take over. Problems:
  - Specialized, undocumented knowledge.
  - The new engineer had no prior video-processing experience.
  - The NJDOT deadline left little time for me to onboard/train.
  - Numerous historical caveats and edge cases, hard to transfer quickly.
- Before reporting to management, the engineer **consulted me directly**. I explained the project was more complex than it looked, that prior engagements consistently revealed surprises, and that success under the timeline wasn't guaranteed even with guidance.
- The engineer **independently reached the same conclusion** and told management that taking over carried substantial risk.
- Business stakeholders still maintained the client commitment had to be honored.

---

## 12. Pressure + Early Data Validation

- Both the engineer and I began getting **pressure from product/project stakeholders** to keep progressing despite limited capacity.
- Rather than proceeding blindly, I chose to **validate the client's data early**, before significant effort went in.
- This took extra hours outside normal project activity — I reviewed the dataset to judge whether it was even processable.

**Data validation reveals problems**
- The review **immediately** surfaced issues.
- The client's submission **did not conform** to the data-prep guidelines that had been provided.
- The problems were significant enough that direct processing would likely fail later in the workflow.
- **This validated a core concern I'd raised during estimation** — the exact "clients don't follow guidelines" scenario the engineering manager had dismissed.

**Additional business insight**
- A second issue: the client's goal was to analyze potential crash scenarios (**near-miss events**).
- But the sample footage appeared to contain **very low traffic volumes**.
- My assessment: generating statistically meaningful crash-risk / near-miss analysis from this data would be **extremely difficult**, even if processing technically succeeded — the analytics might not deliver the insights the client expected.

**Communicating the findings**
- I documented both observations: (1) data non-compliance, (2) insufficient traffic volume for meaningful near-miss analysis.
- The PM communicated these to the client.
- The team expected the client would need to **correct and resubmit** before further work.
- From my view, this temporarily created **breathing room** while again validating the risks I'd flagged at the start.

---

## 13. No Breathing Room — The Real Client Picture

- The PM/project managers asked the client to extend the deadline since the data was not correct.
- The project manager came back with new context: **the client (NDS) is actually a middleman** who works with a number of states.
- This engagement was a **sample project** the middleman needed to deliver to a **Department of Transportation**.
- Because of where it sat in the chain, the deadline **could not be extended at all** — the data had to be processed and *something usable* generated regardless.
- The PM relayed: **we cannot move this deadline again.**

---

## 14. The CTO Call — Strategic Trade-off

I had a call with the CTO who laid out the bigger picture:

- He confirmed the project manager's stand — **the deadline could not move.**
- He knew I was also assigned the **NJDOT** work.
- His strategic framing:
  - If we don't deliver the **video-processing project**, we risk losing this potential client **and the multiple future projects** the middleman could bring.
  - But missing the **NJDOT** deadline is *more dangerous* — it would damage our **standing in the market** by failing to deliver on time on a high-visibility commitment.
- His instruction: he could "deal with" the video-processing situation, but I **should not jeopardize the NJDOT deadline.**

**My commitment**
- Weighing that we could miss multiple future opportunities, I told the CTO **I'd take on the video-processing project and try to get results for the client.**
- The CTO's condition: only if I could manage it **without** compromising NJDOT.
- I assured him the **NJDOT deal would not suffer from my side**, and that I'd try to deliver **both**, since both mattered to the business and our market standing.

---

## 15. Technical Breakthrough — Engineering My Way to Events

- I started working through the video-based data.
- As I'd already warned the PM and CTO, it was **genuinely hard to surface any near-miss / crash events** in the given footage — and that's exactly what happened: **no events were coming through, and processing was failing.**
- Rather than accept the dead end, I **designed a new mechanism and upgraded our software** so it could **tune/learn the parameters** to detect more events.
- This was a decision to **add new functionality to the product itself**, and it **worked**.
- The cost: I worked until ~**4 AM**. After the software changes, we **started receiving events** — a positive sign that we could go back to the client with real data.
- I had **everything set up by ~6 AM** and was able to generate the data.

---

## 16. The Engineering Manager's Apology

- The engineering manager works from the **US**, so he was online in his late evening (my early morning).
- He saw my channel messages reporting that we were now receiving events / good signal on the near-miss data.
- He **DM'd me to apologize** — acknowledging his mistake in assuming my estimates were bloated, and that he **hadn't realized the risks** I'd flagged early in the project. He said it wouldn't happen again and owned it directly.
- Because he came to me **on his own**, I told him there was **no need to dwell** on what had happened — the focus should be **forward**, on not putting ourselves in a position where we're working till 4–5 AM to get things done.
- We ended on good terms and had a warm, personal chat about his **newborn baby** and how things were going for him.

---

## 17. Outcomes & Resolution

**Client / business outcome**
- Even the **middleman didn't expect much** from the given data — but he was **happy we produced near-miss events**, which his end client needed.
- He has **already sent more videos** and opened up **more opportunities with more clients** — we are now getting **ongoing business** from this relationship. (This is the exact upside the CTO had weighed during the trade-off call.)
- **Revenue (approximate):** no exact figure available, but this relationship is expected to contribute on the order of **~10% of the company's total annual business**. *(Estimate — verify the basis/number before putting it in an essay.)*

**NJDOT deadline**
- *To be developed as a separate story.* Short version: **completed on time**, with **good testing**, and **everyone was happy with the results** — i.e., I delivered both projects as I'd assured the CTO.

**The improvement is in production**
- The near-miss product improvement I built is **live in production**.
- It was **validated by both the researchers** who own the core near-miss logic **and the product managers** — sign-off from both the technical and product sides.

**Strategic decision — and a seat at the table**
- The org has decided to **go ahead with building this into a product** (reversing the long-standing deprioritization described in Section 1).
- The **CTO and other executives are now discussing the strategy directly with me**: whether to take on these projects, what the risks are, and how to **deliver better and faster than competitors**.
- I'm **giving input and developing ideas with the CTO** on how to **improve our processing pipelines** to meet video-processing needs.

**Role, title & scope**
- Not *directly* caused by this project, but it was **one of the factors** that helped me earn a **senior title**: I'm now a **Senior Software Developer** (up from Software Engineer).
- My **compensation increased** afterward.
- After discussions with the **CTO, HR, and product managers**, I'll have **more say over several of the products** we build — specifically the ones where I've worked before or have expertise.

---

## 18. Personal Takeaways (my own reflection)

**What I'd do again**
- I'd still **go above and beyond** to hit the project's goal and bring in more business. That instinct paid off.

**What I'd do differently**
1. **Document, even for "one-off" work.** I spent enough effort to get the result, but because product had said this was a one-off we'd never repeat, I **skipped documentation**. My own experience told me otherwise — the business *would* make this mistake again and more such projects *would* come (which is exactly what happened). I should have trusted that intuition and **documented the full procedure and my takeaways at the time**, even at the cost of extra hours.
2. **Sharper persuasion / framing.** I'd want **better convincing skills** — enough to give the engineering manager a **well-balanced, evidence-framed answer** that won him over on *why* I needed more time, **even before any data was available** to prove me right.

**The deeper lesson**
- You **can't convince everyone every time** — but you should build the **skills to handle these situations** when they arrive.
- Don't **feel defeated**; stay **resilient enough to get things done** regardless.

---

## Emerging Leadership Themes (for later essay selection)

Candidate angles, now firmer with the resolution in hand:

1. **Expert judgment vs. organizational assumptions** — the core early tension wasn't technical; it was defending a reality-based view against more senior leaders. *Payoff:* the engineering manager later apologized and owned that he'd missed the risks — vindication that arrived without me seeking it.
2. **Influence without authority / evidence over hierarchy** — I shifted the CTO's position not by seniority but by a structured, written, risk-based case.
3. **Forecasts that kept proving correct** — my predictions (client data quality, low traffic volume, hidden effort) all materialized. The credibility this built is the spine of the story.
4. **Decision-making under a hard constraint** — when the deadline genuinely couldn't move and the CTO named the trade-off, I committed to both projects *and* protected the higher-stakes one (NJDOT). This is a business-judgment moment, not just an engineering one.
5. **Innovating under pressure** — rather than reporting "the data can't produce events," I extended the *product itself* (parameter-tuning mechanism) to make the impossible deliverable, salvaging the client relationship.
6. **Cross-functional leadership & mentoring without direct authority** — guiding an engineer from another team via daily sessions.
7. **Resource constraints & competing priorities** — juggling Montreal, the video project, and the NJDOT/World Cup deadline simultaneously.
8. **Grace in winning** — when proven right, I chose forward-looking reconciliation over "I told you so," and turned a conflict into a repaired working relationship. A maturity/EQ signal admissions committees value.
9. **From individual contributor to strategic voice** ⭐ — the strongest arc-level theme. My early stand and execution led the org to (a) reverse a years-long deprioritization and commit to *productizing* this, and (b) pull me into **executive-level strategy discussions** on whether/how to compete in this space. This is the bridge from "engineer" to "product/business leader" — directly relevant to a PM-oriented MBA narrative.

> ⚠️ **For essay use:** the all-nighter (4 AM / 6 AM) is a vivid detail, but frame it as a one-time crunch you'd *avoid repeating* (which is what you told the EM) rather than a badge of honor — top programs read "worked till 4 AM" as a process/sustainability red flag if it's presented as the hero moment.

---

## Status & Remaining Loose Ends

*The story is now complete end-to-end: conflict → evidence-based influence → execution under a hard constraint → technical breakthrough → reconciliation → business win → productization → strategic seat at the table → promotion → honest self-reflection.*

Resolved:
- ✅ Client reaction — happy, more videos and clients, ongoing business (~10% of annual business, to verify).
- ✅ NJDOT — delivered on time, well-tested (full version is a **separate story**).
- ✅ Improvement is in production; validated by both researchers and product managers.
- ✅ Org committed to productizing; you're now in executive strategy discussions.
- ✅ Promotion to Senior Software Developer; compensation up; more product ownership.
- ✅ Personal takeaways captured (documentation, persuasion, resilience).

Last small item before drafting essays:
- If you can later get **any hard number** (revenue figure, # of new clients/projects, detection or processing improvement %), drop it in — it's the one thing that would still strengthen this. Not blocking; the story stands without it.
