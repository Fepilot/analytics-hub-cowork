# AI-in-One Analytics Advisor — Copilot Cowork Custom Skill

> A custom Cowork skill that turns your AI-in-One Dashboard Power BI export into a polished executive deck — zero scripts, zero installs.

---

## What is a Cowork Custom Skill?

[Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/) (Microsoft 365 Frontier) supports **custom skills**: Markdown files you place in your OneDrive that give Cowork a specialized persona, domain knowledge, and workflow. Cowork discovers and loads them automatically at the start of each conversation.

You can create up to 20 custom skills. Each skill lives at:

```
OneDrive/Documents/Cowork/Skills/<folder-name>/SKILL.md
```

This repo contains the **AI-in-One Analytics Advisor** skill — a Senior Copilot Analytics Advisor persona specialized in the [AI-in-One Dashboard](https://github.com/microsoft/AI-in-One-Dashboard).

---

## What This Skill Does

When activated, Cowork becomes a **Senior Microsoft Copilot Analytics Advisor** and will:

- Analyze all 13 pages of your AI-in-One Dashboard export
- Interpret every metric against benchmark bands (Excellent / Healthy / Below Potential / Concerning)
- Diagnose your organization's adoption pattern (Wide but Shallow, Deep but Narrow, Agent Early Stage, etc.)
- Build a **17-slide executive deck** using Cowork's native PowerPoint skill
- Automatically fetch Microsoft's official AI-in-One Interpretation Guide, Frontier Firm Playbook, and Work Trend Index via Deep Research
- Save the final deck directly to your OneDrive

---

## Installation (One-time, ~2 minutes)

1. Open your **OneDrive** in the browser
2. Navigate to **Documents**
3. Create this exact folder path: `Cowork/Skills/analytics-hub-deck/`
4. Download [`SKILL.md`](SKILL.md) from this repo
5. Upload it to: `Documents/Cowork/Skills/analytics-hub-deck/SKILL.md`

That's it. Cowork discovers it automatically at the start of your next conversation.

> **Tip:** The folder name (`analytics-hub-deck`) can be anything — Cowork identifies the skill by the `name:` field inside SKILL.md.

---

## Customer Workflow (Zero-Code)

### Step 1 — Export from Power BI

In **Power BI Service**: File → Export → **PowerPoint** → Download the `.pptx`

### Step 2 — Convert to PNG images

Open the downloaded `.pptx` in **PowerPoint**:

**File → Export → Change File Type → PNG Portable Network Graphics → Save As**

PowerPoint asks *"Every Slide?"* → click **Every Slide**

This creates a folder with `Slide1.png`, `Slide2.png`, ... — one image per dashboard page.

> **Alternative:** File → Save As → change file type to PNG → Save → Every Slide

### Step 3 — Analyze in Cowork

1. Go to [m365.cloud.microsoft](https://m365.cloud.microsoft) → open **Cowork**
2. Start a **new conversation** from the Cowork home page
3. Drag **all** the PNG files into the chat
4. Send:

   > *"Analyze my AI-in-One dashboard and create an executive deck"*

Cowork activates the skill, analyzes every slide in order, and builds a 17-slide PowerPoint saved to your OneDrive.

---

## ⚠️ Important: Start in the Right Place

Custom skills **only activate in free-form Cowork conversations** — not inside built-in Task templates.

| Where to start | Works? |
|---|---|
| Cowork home page → new conversation ("What should we tackle next?") | ✅ |
| `Cowork > Tasks > [any built-in task]` | ❌ Skills are ignored inside Tasks |

---

## What the Skill Covers

### Metrics (with full benchmark bands)

| Metric | What it measures |
|---|---|
| M365 Copilot Active Rate | % of licensed users who used Copilot in the last 28 days |
| Super User % | % of actives meeting the 5+ apps AND 50+ interactions threshold |
| Agent Adoption % | % of users who interacted with at least one Copilot Agent |
| Unlicensed Chat Users | Users accessing free Copilot Chat (conversion candidates) |
| MoM Growth | Month-over-month change — leading indicator of momentum |
| License Utilization | % of purchased licenses actively generating value |
| Agent Diversity | Average agents per user — signals multi-workflow integration |
| M365 App Diversity | Average Copilot apps per user — predicts renewal intent |

### Adoption Patterns Diagnosed

1. **Wide but Shallow** — High activation, low depth
2. **Deep but Narrow** — Strong power users, low reach
3. **Agent Early Stage** — Solid M365 base, untapped agent opportunity
4. **License Waste** — Utilization < 60%, financial risk
5. **Balanced Frontier** — All signals healthy, time to scale

### Output Deck (17 slides, Executive Mode)

Cover → TOC → Executive Summary → Adoption Landscape → M365 Trends → Department Leaderboard → Super Users → Agent Adoption → Agent Leaderboard → Agent Insights → Unlicensed Chat Opportunity → Cross-Platform Patterns → Adoption Pattern Diagnosis → License Health → Strategic Recommendations → 30/60/90 Roadmap → Closing

---

## Requirements

- Microsoft 365 Copilot license
- Cowork access via the [Frontier program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)
- Power BI Service access to export the AI-in-One Dashboard

---

## Related Resources

| Resource | URL |
|---|---|
| AI-in-One Dashboard (official) | https://github.com/microsoft/AI-in-One-Dashboard |
| Cowork documentation | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| Frontier Firm Playbook | https://adoption.microsoft.com/files/copilot/FrontierFirmPlaybook.pdf |
| Copilot Adoption Hub | https://adoption.microsoft.com/en-us/copilot/ |
| Work Trend Index | https://www.microsoft.com/en-us/worklab/work-trend-index |

---

## Why the Direct PDF Approach Fails in Cowork

If you tried attaching a Power BI PDF directly to Cowork, you likely saw:

> *"I can see the file exists, but I can only read the first page."*

**Root cause:** Power BI PDF exports are **fully rasterized** — every page is a screenshot baked into the PDF with no text layer. Cowork's PDF skill receives limited visual context (often only page 1). Cowork also cannot run Python scripts.

**The fix:** Use the zero-code PNG export path described above. PowerPoint converts every slide to a separate PNG in seconds — no installs required.

---


---

MIT License — Free to use and share within your organization.
