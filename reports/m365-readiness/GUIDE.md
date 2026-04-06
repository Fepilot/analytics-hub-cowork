# M365 Copilot Readiness — Expert Interpretation Guide

## What This Report Measures

The **M365 Copilot Readiness Report** uses M365 activity data to produce a **ranked, prioritized view of which users are most likely to get value from a Copilot license**. It answers: *Who should get licenses next, and in what order?*

This is primarily a **license strategy and enablement planning report** — use it with IT administrators, HR leaders, and business decision-makers who are managing a limited or staged license rollout.

**Data source:** Microsoft Purview M365 activity data + Entra ID org data
**Key output:** A **Licensing Priority (LP) score** per user — a composite of their M365 app usage intensity

---

## Typical Dashboard Pages

| Page | What It Shows |
|---|---|
| **Overview / Score Distribution** | LP score histogram; how many users fall into each readiness tier |
| **Top Candidates** | Ranked list of unlicensed users with highest LP scores |
| **Department Breakdown** | LP score distribution by department; which orgs have the most ready users |
| **Application Usage Heatmap** | Activity intensity by M365 app (Teams, Outlook, Word, Excel, PowerPoint) for each user segment |
| **LP Score Weighting Sliders** | Interactive sliders adjusting weights for each M365 app (for modeling scenarios) |
| **License Optimization** | Existing Copilot licensees whose usage is low — candidates for reallocation |

---

## The LP Score Explained

The **Licensing Priority (LP) score** is a composite index (typically 0–100) calculated from a user's activity across M365 applications. Higher = more ready to benefit from Copilot.

### Component weights (default — users can adjust with sliders):
| App | Why it matters for Copilot |
|---|---|
| **Microsoft Teams** | Meeting summaries, chat drafting, meeting recording analysis |
| **Outlook** | Email drafting, summarization, calendar prep |
| **Word** | Document drafting, rewriting, summarization |
| **Excel** | Data analysis, formula generation, insight extraction |
| **PowerPoint** | Presentation generation, design, summarization |

**High LP score users** = heavy M365 users across multiple apps → they'll immediately have Copilot available in the tools they use most → fastest time to value.

**Low LP score users** = light M365 users → giving them Copilot first is likely wasted investment.

---

## Key Metrics and Benchmarks

### LP Score Distribution Shape
The distribution tells the story:
- **Right-skewed (most users low, few high)**: Most users are light M365 users — licensing should be highly selective
- **Normal/bell curve**: Broad range of readiness — tier-based rollout works well
- **Left-skewed (most high)**: Organization is a heavy M365 shop — broad licensing is justified

### % of Users in "High Readiness" Tier (LP > 70)
- 🔴 **< 5%** — Very narrow addressable market for immediate licensing
- 🟡 **5–15%** — Focus on this cohort first
- 🟢 **15–30%** — Strong pool; phased rollout over 2–3 waves
- 🌟 **> 30%** — Large ready population; license-at-scale is justified

### License Utilization Rate (if existing Copilot licenses are shown)
- 🔴 **< 60%** — Licenses being underused — reallocation before expansion is essential
- 🟡 **60–80%** — Moderate utilization
- 🟢 **> 80%** — Good; expansion is justified

### Top Department LP Score Average
Identifies which business unit should receive the next wave of licenses.

---

## Interpretation Patterns

### Pattern 1: "Clear First Wave"
**Signals:** A well-defined cluster of high-LP users (top 10–20%) clearly separated from the rest
**Interpretation:** Natural first cohort for licensing — high confidence in ROI
**Narrative:** "The LP score distribution reveals [N] users in the 'high readiness' tier — the natural first cohort. These are your heaviest M365 users, already deeply embedded in Teams, Outlook, and Word. Giving them Copilot first maximizes immediate ROI and generates internal proof points for the broader rollout."

### Pattern 2: "Underutilized Licenses"
**Signals:** Existing Copilot licensees showing low LP scores or low activity
**Interpretation:** Licenses allocated to wrong people — reallocation opportunity
**Narrative:** "[N] current Copilot license holders score below [X] on the LP scale — meaning [comparable number] of unlicensed users are demonstrably better candidates. Reallocating these [N] licenses before purchasing new ones could deliver immediate ROI improvement at zero incremental cost."

### Pattern 3: "Department Concentration"
**Signals:** One or two departments have significantly higher average LP scores
**Interpretation:** Natural landing zones for first licensing waves
**Narrative:** "Sales and Marketing show the highest average LP scores ([X] vs. org average of [Y]), driven by heavy Outlook and Teams usage. They represent the lowest-risk, highest-return first licensing cohort. Engineering and Finance follow — structuring the next two waves around these departments balances ROI with breadth."

### Pattern 4: "App Desert"
**Signals:** Very low usage of one or more M365 apps across most users
**Interpretation:** Copilot value will be limited for that app — enablement must come before licensing
**Narrative:** "Excel usage is near-zero for [X%] of users — meaning one of Copilot's most powerful capabilities (data analysis, formula generation) would be immediately inaccessible. Consider a targeted Excel adoption push before or alongside licensing to maximize Copilot value per seat."

---

## Executive Summary Framing

For M365 Readiness, prioritize:
1. Size of the high-readiness cohort (immediate licensing opportunity)
2. Department(s) that should receive the first wave
3. Underutilized existing licenses (if applicable — this is always important to leadership)
4. LP score gap between top and bottom — tells the story of readiness breadth
5. App coverage signal (are users active in the right apps for Copilot?)

**Good examples:**
- "347 users score 70+ on the Licensing Priority scale — the natural first licensing cohort, offering the highest confidence in ROI"
- "Sales and Marketing account for 61% of high-readiness users — designating them as Wave 1 maximizes Copilot activation rates and early proof points"
- "18 current Copilot licensees score below 30 on the LP scale — reallocating these licenses to top-scoring unlicensed users would recover value at no additional cost"
- "Average LP score of 54 vs. top cohort average of 82 — a 28-point gap suggesting structured enablement in Teams and Outlook is needed before broad licensing"

---

## Recommendations Templates

1. **First wave:** "Prioritize the [N] users with LP scores > [X] for immediate licensing — they represent the [X%] of the workforce where Copilot ROI is most predictable; target Wave 1 activation within [30 days]"
2. **License reallocation:** "Audit the [N] license holders with LP scores < [Y] and usage < [Z threshold]; consider reallocation to the [equivalent N] highest-scoring unlicensed users before purchasing additional licenses"
3. **Department targeting:** "Structure the licensing roadmap as: Wave 1 — [top dept], Wave 2 — [second dept], Wave 3 — [third dept]; each wave timed [60 days apart] to allow enablement to land before the next expansion"
4. **M365 adoption pre-work:** "For departments assigned to Wave 2 and beyond with below-average LP scores: run an M365 [Teams/Outlook/Word] adoption nudge campaign to raise readiness scores before their licensing date"
5. **Measuring success:** "Set a target for licensed users to achieve LP score > [X] within 90 days of Copilot activation — use this as the leading indicator of realized value per license"

---

## The LP Score as Conversation Tool

A unique feature of this report is the **LP score weighting sliders**. These are powerful for stakeholder conversations:

- **With the CTO:** Increase the Teams and Excel weight → shows engineering and analyst roles
- **With the CHRO:** Increase the Outlook and Word weight → shows HR, comms, and legal roles
- **With Sales leadership:** Teams + Outlook → customer-facing roles are naturally high LP
- **For budget discussions:** Run scenarios showing LP score shifts under different weighting assumptions to demonstrate the optionality of the scoring model

Capture which weight scenarios were applied when generating this report, and note them in the deck as a methodology clarification.

---

## Analyst Mode — Extra Slides

1. **LP Score Methodology**: Full formula explanation, how weights are applied, data freshness
2. **Score Distribution Histogram**: Full distribution, not just tiers — visual tells the story
3. **Department Breakdown Table**: All departments with LP score average, % high-readiness, recommended wave
4. **Reallocation Analysis**: Current licensee LP scores ranked low-to-high — the reallocation case
5. **App Usage Deep Dive**: Per-app activity heat map — where is usage strong vs. weak
6. **Scenario Modeling**: 2–3 LP score scenarios with different weights and their licensing implications
7. **Data Privacy Note**: What M365 activity data is used, aggregation level, no content access

---

## Common Questions This Report Answers

- "Who should get Copilot licenses next?" → Top LP score users, top departments
- "Are our current licenses going to the right people?" → Existing licensees LP scores vs. unlicensed top scorers
- "Which department should be Wave 1?" → Dept average LP score ranking
- "How many licenses should we request?" → Count of users above LP threshold
- "What do users need to be 'ready' for Copilot?" → App usage profile of high-LP users
- "How long until the next wave is ready?" → LP score trends over time (if historical data available)
