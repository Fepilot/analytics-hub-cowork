# Copilot Chat & Agent Intelligence — Expert Interpretation Guide

## What This Report Measures

The **Copilot Chat & Agent Intelligence** report contains two purpose-built templates:
1. **Chat Intelligence** — Deep analytics on Copilot Chat sessions: prompt volume, session patterns, and engagement progression
2. **Agent Intelligence** — Which agents are being used, by whom, adoption trending

Use this report when you want to go beyond the all-up AI-in-One view and understand the *quality and depth* of AI engagement, not just who is using it.

**Data source:** Microsoft Purview audit logs + Entra ID

---

## Typical Dashboard Pages

### Chat Intelligence Template

| Page | What It Shows |
|---|---|
| **Chat Overview** | Total sessions, prompts, users, MoM trend |
| **Session Depth** | Avg prompts per session, short vs. multi-turn sessions |
| **Engagement Progression** | Users segmented by chat intensity: light, moderate, habitual |
| **Chat Use Case Signals** | Topic/intent patterns (where available) — what people are asking Copilot |
| **User Leaderboard** | Top users by sessions and prompts |
| **Active Day Distribution** | Days per week chart — spotting consistent vs. occasional users |

### Agent Intelligence Template

| Page | What It Shows |
|---|---|
| **Agent Overview** | Total agent users, agent interactions, agents deployed, MoM |
| **Agent Activity Trends** | Agent interaction volume over time |
| **Agent Leaderboard** | Most-used agents ranked by interactions and unique users |
| **Agent Adoption by Team** | Which departments are leading in agent usage |
| **Agent Variety** | How many different agents users are interacting with |
| **Adoption Stage** | Users segmented by agent engagement (trialing vs. habitual agent users) |

---

## Key Metrics and Benchmarks

### Average Prompts per Session (Chat)
**Definition:** Total prompts ÷ total sessions in the period
- 🔴 **< 2 prompts/session** — Very shallow. Users are "one-shot" querying, not having conversations
- 🟡 **2–4 prompts/session** — Getting there. Some multi-turn dialogue
- 🟢 **4–7 prompts/session** — Good depth. Users are iterating on queries, refining responses
- 🌟 **> 7 prompts/session** — Deep engagement. Copilot is being used as a thinking partner, not just a search tool

**Why this matters:** Session depth is the strongest proxy for actual value extracted from AI. Low depth = transactional use. High depth = workflow integration.

### Chat Habitual Users (5+ chat sessions/week)
- 🔴 **< 5% of chat users** — Very few with integrated daily habit
- 🟡 **5–15%** — Small nucleus of power users
- 🟢 **15–30%** — Strong core; enablement is working
- 🌟 **> 30%** — Exceptionally high engagement rate

### Agent Active Users (% of total AI users)
- 🔴 **< 10%** — Agent awareness is low; org is still in "chat only" phase
- 🟡 **10–25%** — Agents are known but not yet embedded in workflows
- 🟢 **25–50%** — Significant agent integration; AI is becoming task-specific
- 🌟 **> 50%** — Advanced. Agents are the primary AI interaction mode for many

### Agent Variety (avg agents per agent user)
- 🔴 **1 agent** — Users know one agent only (often the default)
- 🟡 **1–2 agents** — Limited discovery
- 🟢 **2–4 agents** — Users are exploring different agents for different tasks
- 🌟 **> 4 agents** — Agent catalog is being actively used; good sign of workflow integration

### MoM Agent Growth
- 🔴 **Flat or declining** — Adoption stalled; investigate awareness or accessibility issues
- 🟡 **< 10% MoM** — Slow growth; may benefit from discovery campaign
- 🟢 **10–25% MoM** — Strong organic growth
- 🌟 **> 25% MoM** — Explosive adoption; likely tied to a new agent launch or org-wide push

---

## Interpretation Patterns

### Pattern 1: "High Volume, Low Depth"
**Signals:** Many sessions, many users, but avg prompts/session < 3
**Interpretation:** Chat is being used for simple lookup tasks, not deep work
**Narrative:** "Chat volume looks impressive, but session depth of [X] prompts/session reveals mostly one-shot queries. The opportunity is teaching users to *converse* with Copilot — use iterative prompting to solve complex tasks, draft and refine, or explore scenarios. Session depth is the metric to watch."

### Pattern 2: "Agent Concentration Risk"
**Signals:** Agent leaderboard shows one agent responsible for 70%+ of all interactions
**Interpretation:** Org is dependent on one agent; others haven't been discovered
**Narrative:** "One agent — [name if visible] — accounts for [X%] of all agent interactions. This indicates agents aren't being discovered broadly. An internal agent catalog and use-case-specific agent recommendations would diversify value and reduce concentration risk."

### Pattern 3: "Chat → Agent Migration"
**Signals:** Chat usage flat or slightly declining, agent usage growing fast
**Interpretation:** Power users are migrating from general chat to specific agents for their workflows
**Narrative:** "General Copilot Chat usage is plateauing as the most advanced users move to agents suited to specific tasks. This is a healthy maturity signal — the organization is graduating from 'what can AI do?' to 'which AI is right for this task?'"

### Pattern 4: "Habitual Chat Converting"
**Signals:** High % of chat habitual users (daily), growing agent adoption
**Interpretation:** The chat habit is the gateway to agent adoption
**Narrative:** "The [X] habitual chat users — those using Copilot Chat 5+ days/week — are converting to agents at [Y%] rate. Investment in deepening the chat habit (prompting skills, use case discovery) indirectly accelerates agent adoption."

---

## Executive Summary Framing

For Chat & Agent Intelligence, prioritize:
1. Session depth headline (quality of engagement)
2. Agent adoption trajectory
3. Top agent(s) and use case signal
4. Habitual user percentage (stickiness of AI habit)
5. Biggest opportunity: either session depth improvement (Chat) or agent discovery (Agents)

**Good examples:**
- "Copilot Chat sessions average 5.3 prompts — above the 4-prompt threshold that signals workflow integration vs. basic search"
- "Agent active users grew 38% MoM, reaching 29% of all AI users — the org is entering the agentic AI phase"
- "The HR Onboarding Agent and Procurement Helper account for 58% of all agent interactions — a clear signal of early ROI in high-volume, repetitive workflows"
- "31% of chat users engage 4+ days/week — this habitual base is the most likely cohort to become early agent power users"

---

## Recommendations Templates

**Chat Intelligence:**
1. **Session depth:** "Launch a 'Power Prompting' microlearning series targeting the [X] users in the light-use segment; goal: increase avg prompts/session from [current] to [target] over 60 days"
2. **Use case expansion:** "Publish the top 5 detected chat use case patterns as prompt templates in the internal Copilot resource page — lower the barrier for new users to engage deeply"
3. **Habitual conversion:** "Design a 21-day Copilot Chat challenge targeting moderate users (2–3 sessions/week) to push them to daily habit — focus on the [highest-volume role types] in the data"

**Agent Intelligence:**
1. **Discovery:** "Build and publish an internal agent catalog featuring the top [N] agents with one-sentence value propositions for each — most users don't know what agents exist"
2. **Concentration:** "Run agent discovery sessions for the [Y] departments showing < 5% agent adoption; showcase the top-used agents from leading departments"
3. **Use case matching:** "Match the top [3 agents] visible in this report to their optimal user profiles and proactively recommend them in onboarding materials"

---

## Analyst Mode — Extra Slides

1. **Methodology**: What Purview captures (interaction metadata, not content), what "session" means technically, audit log retention
2. **Session depth distribution**: Not just average, but the full distribution — what % of sessions are 1-prompt, 2-3, 4-6, 7+
3. **Agent taxonomy**: Categories of agents present (productivity, search, line-of-business, etc.) with usage breakdown
4. **User journey**: From first chat login → habitual chat → first agent → multi-agent user; how many users are at each stage
5. **Prompt quality proxy**: If topic data is available, categorize by intent type (lookup, creation, analysis, planning)
6. **Governance note**: For analyst audience — highlight any agent categories that warrant IT governance attention (e.g., third-party agents, agents accessing sensitive data)

---

## Common Questions This Report Answers

- "Are people actually getting value from AI chat or just playing with it?" → Session depth, habitual user %
- "Which agents are delivering the most value?" → Agent leaderboard rankings
- "Is our agent strategy working?" → Agent adoption MoM, agent variety
- "Who should get licensed Copilot next?" → High-engagement unlicensed Chat users (if this data is in the report)
- "What use cases are people gravitating toward?" → Chat topic signals, top agents
- "Are we at risk of AI becoming a fad?" → Habitual user %, session depth trends
