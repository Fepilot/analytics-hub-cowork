# Super Usage Adoption — Expert Interpretation Guide

## What This Report Measures

The **Super Usage Adoption** report (from [DecodingSuperUsage](https://github.com/microsoft/DecodingSuperUsage)) uses **Viva Insights** behavioral data to map the journey from first-time Copilot user to super user. It answers: *Who are your super users, how did they get there, and how do you make more of them?*

This is primarily a **change management and enablement report** — use it to design targeted interventions, identify champions, and measure whether your adoption programs are working.

**Data source:** Viva Insights organizational behavioral data (person-level, de-identified for manager+)

---

## Typical Dashboard Pages

| Page | What It Shows |
|---|---|
| **Organization Overview** | Top-line KPIs: total Copilot users, super user %, active rate, top teams |
| **Adoption Journey Funnel** | Users segmented by engagement level: Aware → Trial → Habitual → Super User |
| **Super User Profiles** | What super users do differently: which features, how often, which teams |
| **Feature Usage Breakdown** | Which Copilot features are most/least used; breadth vs. depth per team |
| **Team Leaderboard** | Departments ranked by super user % and active rate |
| **Time to Habit Formation** | Days from first Copilot use to habitual engagement; distribution curve |
| **Engagement Tiers** | Population breakdown: light (1–2 days/wk), moderate (3–4), habitual/super (5+) |
| **Champions Opportunity** | Teams with high potential but lagging activation — intervention targets |

---

## Key Metrics and Benchmarks

### Super User Rate (% of active users)
**Definition:** Users active 5+ days/week AND using 3+ distinct Copilot features
- 🔴 **< 10%** — Very early. Most users haven't formed a habit
- 🟡 **10–20%** — Building. Habit formation is happening but not systemic
- 🟢 **20–35%** — Strong. Champions program is likely working
- 🌟 **> 35%** — Excellent. Org has cracked habit formation at scale

### Time to Habit Formation (median days)
**Definition:** Days from first Copilot interaction to 5-consecutive-days-active status
- 🔴 **> 90 days** — Slow. Users need clearer workflow entry points
- 🟡 **60–90 days** — Average. Typical without active enablement
- 🟢 **30–60 days** — Good. Active enablement program is compressing time
- 🌟 **< 30 days** — Excellent. Likely a structured onboarding + champions model

### Feature Breadth (avg features per active user)
**Definition:** How many distinct Copilot capabilities an average active user uses
- 🔴 **1–2** — Very narrow. Users likely using only one workflow (e.g., meeting summaries only)
- 🟡 **2–3** — Limited. Common starting point
- 🟢 **3–5** — Healthy breadth. Users exploring multiple workflows
- 🌟 **> 5** — Deep adoption. These are your super users

### Team Concentration (% of teams with at least one super user)
- 🔴 **< 25%** — Super users are siloed in 1–2 departments
- 🟡 **25–50%** — Champions exist but distribution is uneven
- 🟢 **50–75%** — Broad coverage. Champions program is distributing well
- 🌟 **> 75%** — Organization-wide. Super users are across all major teams

### Habitual User Rate (5+ days/wk, any features)
This is a broader metric than super users. Benchmark similar to super users but expect 5–10 points higher.

---

## The Adoption Journey Framework

Use this to frame the narrative around funnel data:

```
AWARE (heard about Copilot, may have logged in once)
    ↓
TRIAL (used Copilot 1–4 days in a month, exploring)
    ↓
HABITUAL (active 3–4 days/week consistently, 2+ features)
    ↓
SUPER USER (active 5+ days/week, 3+ features, workflow integration)
```

**Key intervention points:**
- **Aware → Trial**: Activation campaign, manager nudge, first-use prompt
- **Trial → Habitual**: Workflow tutorials, use case cards, peer examples
- **Habitual → Super**: Champions program, advanced training, recognition
- **Attrition at any stage**: Usually indicates workflow mismatch or lack of relevant use cases

---

## Interpretation Patterns

### Pattern 1: "Strong Start, Stalling Midway"
**Signals:** High % reach "Trial" stage, low % reach "Habitual", very low super users
**Interpretation:** Users try Copilot but don't find a "sticky" workflow
**Narrative:** "78% of users tried Copilot in the first month, but only 23% reached habitual use. The trial-to-habit conversion gap is the primary opportunity. Use case specificity — matching Copilot to each team's actual work — is the lever."

### Pattern 2: "Islands of Excellence"
**Signals:** 1–2 departments with very high super user %, most departments below 10%
**Interpretation:** Pockets of self-organized adoption, not yet scaled
**Narrative:** "Engineering and Sales have cracked the habit code — their super user rates (28% and 31%) are 2x the company average. The tools and patterns are there; the challenge is replication, not discovery."

### Pattern 3: "Fast Formers"
**Signals:** Very low median time to habit (< 35 days)
**Interpretation:** Strong enablement infrastructure — onboarding, training, manager coaching working
**Narrative:** "Users are forming Copilot habits in just [X] days — roughly half the typical 60-day timeline. This signals a well-designed enablement program and strong managerial reinforcement."

### Pattern 4: "Feature Desert"
**Signals:** High activation rate, low feature breadth (< 2.5 avg features per user)
**Interpretation:** Most users are one-trick users (e.g., meeting summaries only) — shallow adoption despite numbers looking good
**Narrative:** "Adoption breadth tells a nuanced story: while 72% of users are active, the average user only engages 1.8 Copilot features. True workflow integration — and the productivity gains that come with it — require broadening to at least 3+ use cases per user."

---

## Executive Summary Framing

For Super Usage Adoption, prioritize:
1. Overall super user % vs. benchmark
2. Time to habit formation signal
3. Top performing team / bright spot to replicate
4. Feature breadth observation
5. Biggest opportunity (lowest team, largest gap)

**Good examples:**
- "23% of active Copilot users have reached super user status — above the 20% benchmark and growing 3pp MoM"
- "Median habit formation time of 45 days — 25% faster than the industry average — reflects a strong champions program"
- "Engineering leads with 31% super users; Legal and Finance trail at 8% — a 23-point gap representing the highest-value intervention target"
- "Users average 2.4 features per week; super users average 6.8 — tripling feature breadth is the most direct path to tripling value"

---

## Recommendations Templates

1. **Champions (replicate bright spots):** "Deploy the [top 3 super user use cases from Engineering/Sales] as bite-sized tutorials for the [bottom 3 departments]; target bringing habit rates from [X%] to [25%] over 60 days"
2. **Compressed onboarding:** "Redesign Copilot onboarding to compress trial-to-habit time: target [30 days] vs. current [X days] using role-specific workflow guides created by existing super users"
3. **Feature breadth:** "Run a 30-day 'Feature-a-Week' campaign for the [N] habitual users currently using < 2 features; focus on the top 3 underused features visible in this report"
4. **Manager engagement:** "Require managers of [bottom quartile teams] to [weekly team check-in on Copilot use cases] — the data shows manager activity correlates with 2x higher team activation"
5. **Champions recognition:** "Formally recognize the [N] super users visible in the leaderboard as AI Champions — give them speaking slots in all-hands and monthly Copilot spotlights"

---

## Analyst Mode — Extra Slides

1. **Viva Insights Methodology**: What data is used, person-level privacy thresholds, opt-in/opt-out considerations
2. **Cohort Analysis**: If available, compare cohorts onboarded in different months
3. **Feature Taxonomy**: Which features count toward each adoption tier
4. **Department-level table**: All departments with adoption metrics — not just top/bottom
5. **Change Management Action Plan**: For each adoption stage, a 30/60/90 day intervention plan
6. **Champions Program Blueprint**: Specific slide on what a structured champions program looks like based on the bright spots in this report

---

## Common Questions This Report Answers

- "How many of our Copilot users are getting real value?" → Super user %, habitual user %
- "How long does it take to form a habit?" → Time to habit formation median
- "Which teams should be our champions?" → Team leaderboard top
- "Which teams need the most help?" → Team leaderboard bottom, long tail
- "Are people exploring different features or stuck in one?" → Feature breadth per user
- "Is our enablement program working?" → Time to habit YoY or MoM trend
