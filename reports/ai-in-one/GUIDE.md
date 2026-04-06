# AI-in-One Dashboard — Expert Interpretation Guide

## What This Report Measures

The AI-in-One Dashboard provides a **single view of all Microsoft AI and Copilot activity** across an organization. It tracks three distinct user populations:
1. **M365 Licensed Copilot users** — people with paid M365 Copilot licenses using AI in Outlook, Teams, Word, Excel, PowerPoint, etc.
2. **Unlicensed Copilot Chat users** — people accessing Copilot Chat for free (Microsoft 365 Copilot Chat in browser or Teams, formerly Bing Chat Enterprise)
3. **Agent users** — people interacting with custom or Microsoft-provided agents via Copilot interfaces

**Data source:** Microsoft Purview audit logs + Entra ID org data + M365 Admin Center licensed user list

---

## Typical Dashboard Pages

| Page | What It Shows |
|---|---|
| **Overall Summary** | Top KPIs across all three Copilot surfaces; total active users, MoM trends |
| **M365 Copilot Trends** | DAU/WAU/MAU trends for licensed Copilot over time |
| **M365 Copilot Leaderboard** | Top departments/users by Copilot actions; license utilization |
| **M365 Copilot Habits** | Engagement tiers: light (1–2 days/wk), moderate (3–4), habitual (5+) |
| **Unlicensed Chat Trends** | Copilot Chat usage trends; who's using free AI |
| **Chat Priority Candidates** | High-activity unlicensed users — license conversion candidates |
| **Chat Engagement** | Session depth, prompts per session for Chat users |
| **Agent Activity Trends** | Agent interaction volume over time |
| **Agent Leaderboard** | Most-used agents, top agent teams |
| **Agent Intelligence** | Agent variety and adoption breadth |
| **License Utilization** | Seats assigned vs. seats actively used; underutilized license alerts |
| **Cross-Platform** | Users active on multiple AI surfaces |

---

## Key Metrics and Benchmarks

### M365 Copilot Active Rate
**Definition:** % of licensed users who used any Copilot feature in the period
- 🔴 **< 40%** — Concerning. Many users not engaging. Focus: activation campaign + manager engagement
- 🟡 **40–60%** — Below potential. Analyze which teams are dragging the average down
- 🟢 **60–80%** — Healthy. Shift focus to depth (super users, specific workflows)
- 🌟 **> 80%** — Excellent. Story is depth and value, not activation

### Super User % (of active M365 Copilot users)
**Definition:** Active users who are 5+ days/week with 3+ features
- 🔴 **< 10%** — Early stage. Habit formation not yet systemic
- 🟡 **10–20%** — Building. Identify bright spots to replicate
- 🟢 **20–35%** — Strong. These users are your proof points for ROI
- 🌟 **> 35%** — Outstanding. Champions program impact visible

### Agent Adoption % (of total AI users)
**Definition:** % of any AI users who interacted with at least one agent
- 🔴 **< 10%** — Early. AI use is still "chat only"
- 🟡 **10–25%** — Growing. Agent awareness needs boost
- 🟢 **25–50%** — Significant. Agents becoming part of workflows
- 🌟 **> 50%** — Advanced. Org is embracing agentic AI — expand and govern

### MoM Growth (Active Users)
- 🔴 **Negative** — Investigate: license churn, enablement gap, or data issue
- 🟡 **0–3%** — Plateauing. May need a new activation push
- 🟢 **3–8%** — Healthy organic growth
- 🌟 **> 8%** — Strong momentum. Document what's working

### Unlicensed Chat / Licensed Copilot Ratio
- **High ratio** (e.g., 3:1 chat to licensed): Large addressable market for licenses; prioritize conversion
- **Low ratio**: Licensed seats are the primary AI surface; focus on depth

### License Utilization Rate
- 🔴 **< 60%** — Licenses being wasted. Fix before requesting more
- 🟡 **60–80%** — Acceptable but room to activate more
- 🟢 **> 80%** — Good. Re-licensing or expansion is justified

---

## Interpretation Patterns

### Pattern 1: "Wide but Shallow"
**Signals:** High activation rate (>70%), low super user % (<12%), low avg actions/user
**Interpretation:** Many people have tried Copilot, few have made it a daily habit
**Narrative:** "We've won the awareness battle — now we must win the habit battle. Targeted workflow-based training for moderate users should be priority."

### Pattern 2: "Deep but Narrow"
**Signals:** Low active rate (<45%), high super user % among actives (>30%), concentrated in 1–2 departments
**Interpretation:** A small team of power users are getting great value, but most of the org hasn't activated
**Narrative:** "Champions are proving the value — but 55% of licensed users haven't engaged. Use the champions' use cases as proof points for the rest of the org."

### Pattern 3: "Agent-Led Growth"
**Signals:** M365 Copilot flat/slow, but Agent users growing fast (>15% MoM)
**Interpretation:** Users are shifting to agentic workflows — this is an inflection point
**Narrative:** "The org is entering the agentic AI phase. Ensure governance, agent catalog visibility, and workflow integration support are in place."

### Pattern 4: "Chat Conversion Opportunity"
**Signals:** Large unlicensed Chat user base (>40% of org), high chat engagement
**Interpretation:** Proven AI demand without licenses — prioritize these users for Copilot licensing
**Narrative:** "X% of the organization is already using free Copilot Chat daily. These users have demonstrated AI readiness — they are the highest-value licensing candidates."

---

## Executive Summary Framing

When writing `executive_summary` bullets for AI-in-One, prioritize:
1. Overall adoption rate headline
2. Super user / depth signal
3. Agent adoption trend
4. Unlicensed chat conversion opportunity
5. MoM momentum or concern

**Good examples:**
- "78% of M365 Copilot licensees active in March — exceeding the 70% benchmark for this adoption stage"
- "Super users represent 22% of active users but generate 61% of all actions — the ROI case rests on expanding this group"
- "Agent adoption doubled MoM to 34% — Engineering and Customer Success are leading the agentic transition"
- "1,840 unlicensed Chat users averaging 8 prompts/session: the highest-value expansion opportunity in the organization"

---

## Recommendations Templates for AI-in-One

Use these as starting points — customize with actual numbers from the report:

1. **Activation:** "Launch a 30-day activation sprint for the [bottom 3 departments] where active rates trail by [X] points; target: 60% active by [next period]"
2. **Habit formation:** "Roll out the [top 3 super user use cases from this report] as workflow tutorials for moderate users in [top 2 departments by user count]"
3. **Agent expansion:** "Publish an internal agent catalog featuring the top [X] agents by usage; run discovery sessions for the [Y] teams with zero agent interaction"
4. **License conversion:** "Prioritize the top [X] unlicensed Chat users (identified in the Priority Candidates page) for M365 Copilot license allocation in the next cycle"
5. **Champions:** "Formalize the [N] super users visible in the leaderboard as AI Champions — give them visibility, resources, and a monthly spotlight session"

---

## Analyst Mode — Extra Slides to Include

For analyst mode, add these beyond the executive deck:

1. **Data Source Methodology**: Purview audit logs → what's captured, retention period, privacy notes
2. **Metric Definitions**: Define "active user" (1+ interaction in period), "super user" threshold, "agent interaction" criteria
3. **Page-by-page deep dive**: For each report page, a slide with the screenshot + methodology note + benchmark context
4. **Segmentation deep dive**: If departmental data is visible, one slide per major department cluster
5. **Change Management Angle**: For each finding, add a "change management implication" — what this means for training, comms, manager coaching
6. **Data Quality Notes**: Flag any pages where numbers seemed inconsistent or unclear
7. **Action Planning Template**: Table with columns: Finding | Recommended Action | Owner | Timeline | Success Metric

---

## Common Leadership Questions This Report Answers

- "Are our Copilot investments paying off?" → Active rate, super user %, actions per user
- "Where should we focus enablement?" → Leaderboard gaps, engagement tiers, dept-level activation
- "Should we buy more licenses?" → Unlicensed Chat volume, license utilization rate
- "Are agents ready for prime time?" → Agent adoption %, variety, growth MoM
- "Which teams should we hold up as examples?" → Top departments + super user concentration
- "What's the risk of doing nothing?" → MoM trends, plateauing teams, declining active rates
