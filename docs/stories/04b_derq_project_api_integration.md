API INTEGRATION - INDEPENDENT CLIENT LEADERSHIP & TECHNICAL FLEXIBILITY

**Project Type**: Technical integration (connecting Derq system to client infrastructure)
**Role**: Technical Lead
**Collaborators**: Arijit Bose (Senior PM), peer engineer
**Result**: 70%+ NPS, 25% development cycle reduction
**Key Learning**: Independent client leadership vs peer needing support

---

THE PROBLEM - ALERT FATIGUE & MONITORING LIMITATIONS

Most of our clients are state governments in the US and Canada, particularly their Departments of Transportation (DoTs), who manage control rooms for monitoring traffic conditions. These control rooms rely on manual monitoring of camera feeds to detect various safety hazards:
- Stopped vehicles on highways (breakdowns, accidents)
- Near-miss events (close calls that could predict accidents)
- Crashes (requiring emergency response)
- Pedestrians walking on roads (dangerous situations)

However, it is not feasible for the engineers in these control rooms to monitor all cameras continuously or respond in real-time to every event. With dozens or hundreds of cameras across a jurisdiction, human monitoring has fundamental limitations:
- **Attention span**: Engineers can't watch all screens simultaneously
- **Response time**: By the time an engineer notices an event, critical seconds have elapsed
- **Prioritization**: Hard to distinguish high-priority events from routine occurrences
- **Fatigue**: Continuous monitoring leads to missed events

THE SOLUTION - REAL-TIME API INTEGRATION

Our system detects various types of events using AI/ML and displays the details on a dashboard. Since the engineers cannot monitor our dashboard at all times (they have their own existing monitoring systems), the solution we proposed was to send real-time API calls to their systems.

This way, important event details could be displayed directly on the engineers' screens as part of their existing monitoring workflow—no need to switch between systems or add another screen to watch.

Simple concept, complex execution.

USER RESEARCH & REQUIREMENT GATHERING

I worked closely with Product Manager Arijit Bose to ensure our solution met the engineers' needs. We interviewed traffic engineers from multiple municipalities (such as Multiplex Kies and others) to understand their requirements for receiving API calls.

The research revealed significant diversity in requirements:
- **Transmission preferences**: Some preferred API calls over the internet, while others preferred local network calls (security concerns)
- **Security protocols**: Depending on the client, we had to account for login credentials, secret keys, or even customized API call receivers
- **Data formats**: Different clients had different existing systems expecting different data structures
- **Integration complexity**: Varying levels of technical sophistication among client IT departments

This wasn't a "one size fits all" situation—we needed a flexible architecture that could adapt to diverse requirements.

INDEPENDENT CLIENT LEADERSHIP - THE COMPARATIVE TEST

During the requirements gathering phase, both I and another engineer from Derq were assigned client calls with various Departments of Transportation to collect technical requirements. This assignment became an unexpected test of client-facing capabilities.

These weren't just technical discussions. They required:
- **Understanding business contexts**: Why does this DoT need real-time alerts vs batched reports?
- **Asking probing questions**: What are the unstated needs beyond explicit requirements?
- **Synthesizing diverse requirements**: How do we find patterns across different municipalities?
- **Managing stakeholder relationships**: Building trust across different organizational levels

The performance divergence was stark:

**My Peer's Approach:**
- Consistently needed Arijit's assistance to navigate conversations
- Required coaching on how to structure discussions
- Needed guidance on what questions to ask
- Struggled with how to handle objections or pushback
- Focused primarily on collecting explicit technical requirements

**My Approach:**
- Confidently led these calls independently from the outset
- Instinctively understood when to dive into technical details vs when to focus on business outcomes
- Knew when to listen vs when to guide the conversation
- Managed stakeholder relationships across different organizational levels
- Uncovered unstated needs by asking "why" behind stated requirements

This wasn't about being smarter—it was about naturally bridging technical expertise with business understanding. I had developed this skill through my Tvarit experience (8-country stakeholder management) and IIT Bombay's collaborative environment, but seeing the contrast made me realize it's a relatively rare capability.

Arijit later noted in his recommendation: "His natural ability to manage stakeholder relationships effectively sets him apart from others at his level and demonstrates skills typically found in professionals with significantly more experience."

DEVELOPMENT & DEPLOYMENT

After gathering these diverse requirements, I led the development of the API integration module, ensuring compatibility with various client protocols and security measures.

The technical challenge was building one system that could:
- Support both internet and local network transmission
- Accommodate multiple security protocols
- Adapt to different data format expectations
- Scale across growing number of clients
- Maintain reliability (99.9%+ uptime requirement)

My initial engineering instinct was to standardize: "Here's our API format; integrate with it." But user research revealed this wouldn't work—government systems are heterogeneous, each with legacy constraints and security requirements.

Instead, we built an **API integration framework** that could adapt to multiple protocols. This was harder technically but created exponentially more value. Clients who would have rejected a rigid solution embraced our flexible approach.

Once the module was deployed, we held feedback sessions with the engineers to gather insights on improving the system. A common request was to include a link to a video feed alongside the event details, enabling engineers to visually verify the situation before taking action.

This request revealed an important user need: **engineers didn't trust text-only alerts**. They wanted to see what was happening before dispatching emergency services or taking other actions. We quickly implemented video feed links, which significantly improved adoption and satisfaction.

RESULTS - 70%+ NPS & 25% CYCLE REDUCTION

The results validated our research-driven, flexible approach:

**Client Satisfaction:**
- **70%+ Net Promoter Score (NPS)** - a remarkably high satisfaction metric
- NPS > 70% indicates not just satisfaction but genuine enthusiasm and willingness to recommend our solution
- For context: NPS above 50% is considered excellent; 70%+ is exceptional

**Development Efficiency:**
- **25% reduction in development cycle** compared to typical timelines for similar integration projects
- Achieved through front-loaded user research and flexible architecture
- Reduced rework by getting requirements right the first time

**Business Impact:**
- Improved real-time monitoring for existing clients
- Opened doors for interactions with potential new clients who required similar capabilities
- Positioned API integration as reference implementation for future projects

PRODUCT MATURITY & POST-DEPLOYMENT PHASE

Currently, the product is in the post-deployment support phase, where we make updates and improvements only when new clients request specific changes or introduce new protocols for the API calls.

This strategic shift from active development to maintenance mode reflects product maturity and market fit. Not every product needs continuous innovation—some reach a "good enough" state where ongoing support and occasional customization create more value than aggressive feature development.

Knowing when to shift from build mode to support mode is a strategic decision I'm still learning to make systematically rather than intuitively.

PARSONS INTEGRATION (2025) - TWO SPRINTS DELIVERED IN ONE

The pattern from the original API integration project has continued into newer client-specific integrations. The most recent and clearest example is the Parsons integration in 2025.

Parsons is a major engineering and infrastructure firm whose internal monitoring systems consume event data from Derq's platform. The integration was scoped, planned, and committed as a two-sprint effort — typical for an integration of this complexity given multi-protocol requirements and security handling.

I delivered the full scope in a single sprint. Two-sprint plan, one-sprint actual.

The compression came from reusing the flexible API integration framework I had built for the original DoT project rather than building from scratch — exactly the kind of payoff the framework was designed for. Each new client integration that lands inside the framework's flex points is faster, cheaper, and lower-risk than the last. The Parsons integration didn't require any new framework capability; it required only the configuration and validation work that the framework was meant to make routine.

**Outcome:** Parsons' client-side integration was unblocked earlier than committed. Internally, the delivery is the cleanest recent example of "convert one-off custom client work into reusable product capability" — the same lens the company is now using as it shifts from client-acquisition-first to product-first.

This is also the data point that anchors the broader argument for expanded ownership: the API integration framework was built once, two years ago. Every integration since has compounded its return. Decisions like that — investing now to compound later — are the kind of strategic engineering judgment that the expanded role is meant to formalize.

---

KEY ACHIEVEMENTS:
- Led API integration project with US/Canada government DoTs
- 70%+ Net Promoter Score (exceptional client satisfaction)
- 25% reduction in development cycle vs typical timeline
- Independent client call leadership (peer needed PM support consistently)
- Multi-protocol compatibility architecture
- Deployed across multiple client systems
- Video feed link feature (research-driven enhancement)
- Attracted potential new clients through satisfied existing clients
- Skills recognized as "typically found in professionals with significantly more experience" (Arijit)

QUANTIFIABLE METRICS:
- **70%+ NPS** (Net Promoter Score) - exceptional
- **25% development cycle reduction** vs typical
- 2 countries (US + Canada)
- Multiple municipalities (state government DoTs)
- Multiple control rooms served
- 2 transmission types (internet + local network)
- Multiple security protocols (credentials, keys, custom receivers)
- Multiple event types detected (stopped vehicles, near-miss, crashes, pedestrians)
- **Independent client call leadership** (comparative advantage vs peer)
- Post-deployment support phase (product maturity)

SKILLS DEMONSTRATED:
- Independent client leadership (vs peer needing support)
- Government client management
- User research & interviews across diverse stakeholders
- Requirements gathering (explicit and implicit needs)
- Technical flexibility & adaptability
- Multi-protocol system architecture
- API development & integration
- Cross-system compatibility
- Security protocol implementation
- Feedback collection & rapid iteration
- Feature prioritization (video feed links)
- Real-time system integration
- Business-technical translation
- Stakeholder relationship management
- Post-deployment support management

KEY LEARNINGS:
"Flexibility in implementation creates more value than rigid standardization."

"Independent client leadership isn't just about technical knowledge—it's about instinctively knowing when to dive into details vs focus on outcomes, when to listen vs guide the conversation."

"High NPS (70%+) doesn't come from building what clients ask for—it comes from uncovering what they actually need. Video feed links weren't in initial requirements, but observation revealed engineers needed visual verification to trust alerts."

COMPARATIVE ADVANTAGE (FROM ARIJIT):
> "During our API integration project, both he and another teammate were assigned client calls to gather requirements. While his peer consistently needed my assistance to navigate these conversations, he confidently led these calls independently. His natural ability to manage stakeholder relationships effectively sets him apart from others at his level and demonstrates skills typically found in professionals with significantly more experience."

What this reveals:
- Natural PM abilities vs needing extensive training/coaching
- Business intuition that complements technical depth
- Accelerated readiness for senior roles

ESSAY APPLICATIONS:
- Independent leadership & client management
- Adaptability & technical flexibility
- Stakeholder management across government agencies
- User research driving product decisions
- Comparative advantage (vs peer performance)
- Technical-business bridge building
- Client satisfaction excellence (70%+ NPS)

CONNECTION TO MBA GOALS:
The API integration project demonstrated my ability to lead client relationships independently and deliver high satisfaction (70%+ NPS) while accelerating timelines (25% faster). However, it also revealed strategic gaps:

**What I Proved:**
- Can lead government client relationships without supervision
- Can build flexible systems that accommodate diverse requirements
- Can achieve exceptional client satisfaction through user research

**What I'm Missing (MBA Will Address):**
1. **Pricing Strategy**: How should we price this flexible integration? Fixed fee vs usage-based? Premium for custom security protocols? I lack frameworks for strategic pricing decisions.

2. **Standardization vs Customization Trade-offs**: At what point does flexibility become unsustainable? How do you systematically evaluate when to standardize vs when to customize? This is a strategic decision I currently make intuitively.

3. **Client Lifetime Value Optimization**: 70%+ NPS suggests opportunity for expansion revenue—but how do I systematically identify and capture that? What's the optimal customer success model?

4. **Competitive Positioning**: Is "flexible integration" a defensible competitive advantage, or will competitors copy it? How do I build sustainable moats around this capability?

The MBA will teach me how to transform high client satisfaction into sustainable business advantage—moving from tactical execution (which I've proven) to strategic business building (which I need to learn systematically).
