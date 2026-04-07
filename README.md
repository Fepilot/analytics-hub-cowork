# AI-in-One Executive Deck Generator — for Copilot Cowork

> Transform your AI-in-One Dashboard Power BI export into a polished executive PowerPoint — using [Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/). No scripts, no installs, no code.

This repo contains the **complete instructions and domain knowledge** that Copilot Cowork needs to analyze your [AI-in-One Dashboard](https://github.com/microsoft/AI-in-One-Dashboard) images and build a data-driven executive deck. You share this repo link with Cowork, attach your dashboard images, and Cowork does the rest.

---

## What You Get

| Input | Output |
|---|---|
| PNG images exported from your AI-in-One Power BI Dashboard | **17-slide executive deck** (or 25+ slide analyst guide) saved to your OneDrive |

Your deck includes:
- KPI scorecards benchmarked against Microsoft's Frontier Firm standards
- Department leaderboard analysis with top/bottom performers
- Adoption pattern diagnosis (Wide but Shallow, Deep but Narrow, etc.)
- Agent ecosystem analysis with diversity metrics
- Unlicensed chat conversion opportunity sizing
- 5 strategic recommendations with WHO + WHAT + measurable outcome
- 30/60/90 day action roadmap

---

## How to Use

### Step 1 — Export your dashboard as PNG images

1. In **Power BI Service**: File → Export → **PowerPoint** → Download the `.pptx`
2. Open the `.pptx` in **PowerPoint**
3. **File → Export → Change File Type → PNG Portable Network Graphics → Save As**
4. PowerPoint asks *"Every Slide?"* → click **Every Slide**
5. This creates a folder with `Slide1.png`, `Slide2.png`, ... one per dashboard page

> **Alternative:** File → Save As → change type to PNG → Save → Every Slide

### Step 2 — Open Copilot Cowork

Go to [m365.cloud.microsoft](https://m365.cloud.microsoft) and open **Cowork**.

Start a **new conversation** from the Cowork home page.

### Step 3 — Give Cowork the context and your images

Drag **all** the PNG files into the chat, then send:

```
Read the instructions at https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/INSTRUCTIONS.md
and the accuracy rules at https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/DASHBOARD_READING_RULES.md
Then analyze my AI-in-One dashboard images and create an executive deck.
I've attached all [N] slides.
```

> **Why raw URLs?** Cowork's web fetch cannot render GitHub's JavaScript UI. The `raw.githubusercontent.com` links return plain text that Cowork reads directly.

### Prompt Variations

| What you want | Prompt |
|---|---|
| **Executive deck** (default, 17 slides) | `Read https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/INSTRUCTIONS.md and https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/DASHBOARD_READING_RULES.md — create an executive deck from my attached AI-in-One dashboard images.` |
| **Analyst guide** (25+ slides, deep dives) | `Read https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/INSTRUCTIONS.md and https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/DASHBOARD_READING_RULES.md — create an analyst guide from my attached AI-in-One dashboard images.` |
| **For a specific audience** | `Read https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/INSTRUCTIONS.md — create an executive deck for our CIO from my AI-in-One dashboard. [N] images attached.` |
| **Department-level focus** | `Read https://raw.githubusercontent.com/Fepilot/analytics-hub-cowork/main/INSTRUCTIONS.md — create a department-level analysis deck from my AI-in-One dashboard images. Focus on the bottom 5 and top 5 teams.` |

---

## Repo Structure

```
analytics-hub-cowork/
├── README.md                     ← You are here
├── INSTRUCTIONS.md               ← Complete analysis workflow for Cowork
├── DASHBOARD_READING_RULES.md    ← Data accuracy rules (12 rules + checklist)
└── LICENSE
```

| File | What Cowork reads from it |
|---|---|
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | Persona, workflow steps, metric definitions with benchmark bands, adoption patterns, slide structure, recommendation templates, audience framing, expert analysis rules |
| [DASHBOARD_READING_RULES.md](DASHBOARD_READING_RULES.md) | 12 data accuracy rules to prevent misreading numbers, filters, axes, and labels |

---

## What the Instructions Cover

### 8 Metrics with Full Benchmark Bands

| Metric | Excellent | Healthy | Below Potential | Concerning |
|---|---|---|---|---|
| M365 Copilot Active Rate | > 80% | 60–80% | 40–60% | < 40% |
| Super User % | > 35% | 20–35% | 10–20% | < 10% |
| Agent Adoption % | > 50% | 25–50% | 10–25% | < 10% |
| MoM Growth | > 8% | 3–8% | 0–3% | Negative |
| License Utilization | > 90% | 80–90% | 60–80% | < 60% |
| Agent Diversity | > 3/user | 2–3/user | 1–2/user | < 1/user |
| M365 App Diversity | > 5/user | 3–5/user | 2–3/user | < 2/user |

### 5 Adoption Patterns Diagnosed

1. **Wide but Shallow** — High activation, low depth
2. **Deep but Narrow** — Strong power users, low reach
3. **Agent Early Stage** — Solid M365 base, untapped agent opportunity
4. **License Waste** — Utilization < 60%, financial risk
5. **Balanced Frontier** — All signals healthy, time to scale and govern

### Output Modes

| Mode | Slides | When to use |
|---|---|---|
| **Executive** | 17 | CIO/CTO briefings, QBRs, steering committees |
| **Analyst** | 25+ | IT teams, change management, deep dives |

---

## Requirements

- Microsoft 365 Copilot license with [Frontier program](https://adoption.microsoft.com/en-us/copilot/frontier-program/) access (for Cowork)
- Power BI Service access to export the AI-in-One Dashboard

---

## Why PNG Images Instead of PDF?

Power BI PDF exports are **fully rasterized** — every page is an image baked into the PDF with no text layer. When Cowork processes the PDF, it often only reads the first page.

The fix: export via PowerPoint → save as PNG → Cowork handles each image individually and analyzes them all.

---

## Related

| Resource | Link |
|---|---|
| AI-in-One Dashboard (official) | https://github.com/microsoft/AI-in-One-Dashboard |
| AI-in-One Exec Deck (GitHub Copilot / Claude version) | https://github.com/Fepilot/ai-in-one-exec-deck |
| Copilot Cowork documentation | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| Frontier Firm Playbook | https://adoption.microsoft.com/files/copilot/FrontierFirmPlaybook.pdf |
| Work Trend Index | https://www.microsoft.com/en-us/worklab/work-trend-index |

---

MIT License
