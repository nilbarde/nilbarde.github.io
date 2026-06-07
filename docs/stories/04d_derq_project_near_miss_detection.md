NEAR-MISS & CRASH EVENT DETECTION - ITERATIVE DEVELOPMENT WITH SUBJECTIVE REQUIREMENTS

**Project Type**: New safety feature development
**Role**: Technical Lead — **sole active developer from the systems/software team**
**Original team**: Arijit Bose (Senior PM), Usman (Project Lead), Bilal (QA Engineer), me as backend technical lead
**Current ownership**: Complete development and debugging responsibility; single point of continuity for a safety-critical, core-value module
**Challenge**: Highly subjective requirements varying by client
**Approach**: Continuous iteration and client co-creation

---

OWNERSHIP STATUS - SOLE DEVELOPER

Across Derq's product portfolio, NearMiss & Crash Event detection is one of the modules most directly tied to the product's core value proposition — preventing collisions and reducing injuries on roads. It is also the module on which the ownership shape has narrowed over time.

As of the current scope, **I am the sole active developer on this module from the systems and software team**. The cross-functional collaborators (Arijit, Usman, Bilal) continue to provide product, project, and QA support, but the day-to-day development and debugging responsibility — what gets built, what gets fixed, what ships — sits entirely with me from the engineering side.

This is unusual within the team for two reasons:

1. **Safety-criticality.** Most safety-critical modules at Derq have multiple engineers covering them precisely because the bus factor matters. NearMiss has narrowed to a single owner not because it's deprioritized, but because the surface area is well-understood and the iteration speed is faster with a single technical owner staying close to the client conversations on severity.
2. **Continuity.** Several clients have very different definitions of high-severity events (see below). Sustaining a coherent technical direction through that subjectivity is easier with one person carrying the thread than with rotating engineers each interpreting fresh client input.

The framing for any future essay or resume bullet: **sole active developer from the systems/software team on a safety-critical collision-detection module**. That sentence stands on its own.

PROJECT BACKGROUND

This project focuses on detecting near-miss and crash events, which are critical for enhancing road safety. Understanding the distinction is important:

**Near-Miss Events:**
- Situations where two objects come very close to colliding but do not actually make contact
- Examples: Vehicle swerving to avoid collision, pedestrian narrowly avoiding being hit, two cars braking hard to prevent accident
- These are **predictive indicators** of future crashes
- Identifying near-miss hotspots allows preventive action before actual accidents occur

**Crash Events:**
- Actual collisions between vehicles, or between vehicles and vulnerable road users (VRUs)
- Require emergency response
- But by then, damage is done

These events typically occur at intersections in high-traffic areas, where cameras are deployed to monitor the surroundings. Our system analyzes live camera feeds to detect both actual crashes and near-miss events that could predict future accidents.

COLLABORATIVE TEAM APPROACH

I am collaborating with:
- **Arijit Bose**: Product Manager (strategy, client relationships, business priorities)
- **Usman**: Project Lead (overall project coordination, timeline management)
- **Bilal**: QA Engineer (testing protocols, quality assurance, deployment validation)
- **Me**: Technical lead for backend system development and client technical discussions

Our team is focused on developing a system on the backend to detect these high-risk events from live camera feeds. The technical challenge is significant: real-time video processing, distinguishing near-misses from routine traffic, and determining event severity.

THE CORE CHALLENGE - SUBJECTIVE SEVERITY DEFINITIONS

In parallel with technical development, we are engaging in discussions with clients to define the severity of these events—distinguishing between high and low-severity incidents.

This is where the project gets complex. Unlike other projects with clear technical specifications, **severity is inherently subjective**:

**What One Client Considers High-Severity:**
- Any near-miss involving a pedestrian
- Close calls at school zones
- Events during peak traffic hours

**What Another Client Considers High-Severity:**
- Only near-misses with closing speeds > 40 mph
- Events at historically dangerous intersections
- Incidents involving commercial vehicles

There's no universal definition. Each jurisdiction has different priorities based on:
- Local accident history
- Political priorities (e.g., Vision Zero commitments)
- Resource constraints (can't respond to every event)
- Risk tolerance and liability concerns

Understanding the severity is crucial, as it helps the client take appropriate actions to mitigate such risks and improve road safety. But "appropriate actions" differ by client.

SAFETY SCORING & HEATMAP DEVELOPMENT

Based on these client discussions and our research, we are developing a **safety scoring system** and generating **heatmaps** to highlight areas with the highest frequency of near-miss or crash events.

**Safety Scoring System:**
- Algorithms that assign severity scores to detected events
- Factors: closing speed, vehicle types involved, location context, time of day, weather conditions
- **Configurable**: Clients can adjust weighting based on their priorities
- Not a one-size-fits-all score, but a flexible framework

**Heatmaps:**
- Visual representation of where high-risk events cluster
- Allows clients to easily identify hotspots
- Enables targeted interventions (signal timing changes, additional enforcement, infrastructure improvements)
- Updated in real-time as new events are detected

As each client has unique requirements, we continuously iterate on the system and refine our dashboard to meet their specific needs and help them enhance the safety of road users in their respective areas.

ITERATIVE DEVELOPMENT APPROACH

Since the requirements for this project are highly subjective and vary across different clients, we are engaged in **ongoing research** to improve the system and adapt our solutions to support their goals better.

This required a fundamentally different approach than other projects:

**Traditional Approach (doesn't work here):**
1. Gather requirements
2. Design solution
3. Build
4. Deploy
5. Done

**Our Approach (iterative co-creation):**
1. Gather initial requirements
2. Build configurable prototype
3. Deploy with Client A
4. Observe how they actually use it (vs how they said they would)
5. Gather feedback and adjust
6. Deploy with Client B (different priorities)
7. Identify patterns across clients
8. Refine core system while maintaining flexibility
9. Continuous improvement as more clients onboard

**Why This Matters:**
Clients can't always articulate what they need upfront. When asked "what severity threshold do you want?" they give abstract answers. But when shown actual events and asked "is this high-priority?" they can respond concretely.

This taught me that **user research isn't just upfront interviews—it's continuous observation of actual usage**.

DASHBOARD REFINEMENT & CUSTOMIZATION

The dashboard became the primary interface for clients to interact with our system. It needed to:
- Display real-time events as they occur
- Show heatmaps of historical hotspots
- Allow filtering by severity, location, time, event type
- Provide drill-down capabilities (seeing specific event details)
- Enable export for reporting to city councils, traffic safety boards

But different clients had different dashboard priorities:
- Some wanted real-time focus (What's happening now?)
- Others wanted historical analysis (Where should we invest in infrastructure?)
- Some needed simple overviews (for executives)
- Others wanted detailed data (for traffic engineers)

We built a customizable dashboard where clients could configure what they see. This flexibility was critical for adoption.

ONGOING RESEARCH & CONTINUOUS IMPROVEMENT

Our ultimate aim is to provide clients with a tool that proactively identifies near-miss events and enables them to improve safety based on actionable insights.

The "ongoing research" aspect keeps this project dynamic. Every new client deployment reveals:
- Edge cases we hadn't considered
- New severity definitions we need to accommodate
- Integration challenges with their specific systems
- Opportunities for improvement based on actual usage

This taught me an important lesson about product lifecycle: **Some products are never "finished"—they evolve continuously based on user needs and technological capabilities.**

---

KEY ACHIEVEMENTS:
- Leading near-miss & crash event detection project
- Collaborative team approach (PM, Project Lead, QA, Technical Lead)
- Backend system development for live camera feed analysis
- Client engagement for subjective severity definitions
- Safety scoring system development (configurable algorithms)
- Heatmap generation for hotspot identification
- Iterative dashboard refinement (continuous improvement)
- Customization for diverse client requirements
- Ongoing research for system improvement
- Adaptation to highly subjective needs
- Proactive safety event identification
- Actionable insights delivery to government clients

QUANTIFIABLE METRICS:
- 4 team members (Arijit, Usman, Bilal, me)
- Multiple clients with varying requirements
- Live camera feeds (real-time processing)
- 2 event types (near-miss + crashes)
- 2 severity levels (high + low, configurable)
- Multiple intersection deployments
- Continuous iteration cycles (ongoing)
- Configurable scoring algorithms
- Real-time heatmap updates

SKILLS DEMONSTRATED:
- Technical project leadership
- Cross-functional collaboration (PM, Project Lead, QA)
- Backend system architecture
- Computer vision application (live feeds)
- Client requirement gathering (subjective needs)
- Severity classification methodology
- Safety metrics development
- Data visualization (heatmaps)
- Dashboard design & iteration
- Client customization management
- Iterative development methodology
- Research-driven continuous improvement
- Adaptive solution design
- Stakeholder communication
- Proactive safety focus

KEY LEARNINGS:
"When requirements are subjective, continuous client engagement beats upfront specification."

"Clients can't always articulate needs abstractly, but they can respond concretely to specific examples. Show them real events and ask 'is this high-priority?'—much more effective than asking 'what's your severity threshold?'"

"Not every product needs to reach a 'finished' state. Some products create more value through continuous evolution than through one-time perfection."

"Configurability has a cost—more complexity to maintain. But when requirements are truly subjective across clients, the cost is worth it for adoption and satisfaction."

COMPARISON TO OTHER DERQ PROJECTS:

| Aspect | Blinking Traffic Signs | ATSPM Redesign | Near-Miss Detection |
|--------|------------------------|----------------|---------------------|
| **Requirements** | Clear (user behavior research) | Clear pain points identified | Highly subjective |
| **Approach** | Front-loaded research → Build | Questioning conventional wisdom | Continuous iteration |
| **Development Style** | Linear (research → build → deploy) | Redesign (analyze → redesign → deploy) | Iterative (build → observe → refine) |
| **"Done" State** | Clear endpoint (deployed system) | Clear endpoint (redesigned system) | Ongoing evolution |
| **Key Challenge** | Speed of execution | Questioning status quo | Managing subjectivity |

Each project taught different lessons about product development.

ESSAY APPLICATIONS:
- Teamwork & collaboration (4-person team)
- Adaptability & flexibility (subjective requirements)
- Client-centric approach (continuous engagement)
- Iterative development methodology
- Technical-business translation
- Safety & social impact focus
- Managing ambiguity (no clear "right answer")
- Ongoing learning & improvement
- Cross-functional coordination

CONNECTION TO MBA GOALS:
The near-miss detection project taught me how to handle highly subjective requirements through iterative co-creation with clients. However, it also revealed strategic challenges:

**What I Learned:**
- Can manage projects where requirements evolve continuously
- Can build configurable systems that accommodate diverse client needs
- Can collaborate effectively in cross-functional teams

**What I'm Missing (MBA Will Address):**
1. **Product Portfolio Prioritization**: This project requires ongoing investment for continuous improvement. But we have finite resources. How do I systematically decide when to invest in improving this product vs building new products? What's the framework for portfolio management?

2. **Standardization vs Customization Economics**: We built configurability to handle subjective requirements. But how much customization is sustainable? At what point does flexibility become a cost burden that erodes margins? What's the financial analysis framework for these trade-offs?

3. **Client Segmentation**: Different clients have very different needs. Should we segment our offering? Premium tier with more customization? Standard tier with less flexibility but lower cost? How do I make these strategic segmentation decisions?

4. **Build vs Partner Decisions**: The configurability challenge—should we build everything in-house, or partner with configurable platform providers? What's the framework for make-or-buy decisions in product development?

The MBA's strategy, finance, and operations courses will teach me frameworks for making these strategic decisions systematically rather than intuitively—essential for scaling from managing one project to managing product portfolios and eventually building my own venture.
