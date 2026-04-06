# 📊 Analytics Hub Deck Generator — Copilot Cowork Edition

> Turn your Power BI Analytics Hub reports into polished executive presentations — using Copilot Cowork.

This repo is the **Copilot Cowork** counterpart to [`analytics-hub-deck`](https://github.com/Fepilot/analytics-hub-deck) (the GitHub Copilot / Claude Code version). It solves the core limitation that makes the original workflow fail in Cowork.

---

## Why the PDF Approach Fails in Cowork

If you've tried attaching a Power BI PDF directly to Cowork, you likely hit this:

> *"I can see the file exists, but I can only read the first page / can't extract its contents."*

**Root cause:** Power BI PDF exports are **rasterized** — every page is a screenshot image baked into the PDF with no text layer. When Cowork's PDF skill processes it, it receives limited visual context from the model (often just page 1). There's no way to programmatically loop through all pages the way GitHub Copilot can via `temp/page_*.png`.

Additionally, Cowork **cannot run Python scripts**, so the original `convert.py --prepare` workflow doesn't apply.

**The fix:** Pre-extract the PDF once locally using `prepare.py`, then feed all individual PNG images directly to Cowork. Cowork handles images natively and processes them all.

---

## Architecture Comparison

| | GitHub Copilot / Claude Code | **Copilot Cowork** |
|---|---|---|
| PDF processing | `python convert.py --prepare` (local) | `python prepare.py` (local) |
| Image delivery | AI reads `temp/page_*.png` from filesystem | User drags PNGs into Cowork chat |
| Analysis | AI writes `temp/insights.json` | Cowork analyzes images directly |
| PPTX generation | `python convert.py --build` | Cowork's native PowerPoint skill |
| Instructions | `INSTRUCTIONS.md` (repo root) | `SKILL.md` (OneDrive) |
| Execution environment | Local terminal | Microsoft 365 cloud |

---

## Setup (One Time)

### 1. Clone this repo

```bash
git clone https://github.com/Fepilot/analytics-hub-cowork.git
cd analytics-hub-cowork
```

### 2. Install Poppler (required for PDF extraction)

Poppler is the PDF rendering library used by `pdf2image`.

**Windows:**
1. Download the latest release from: https://github.com/oschwartz10612/poppler-windows/releases/
2. Extract to `C:\poppler\`
3. Add `C:\poppler\Library\bin` to your `PATH`

**Mac:**
```bash
brew install poppler
```

**Linux:**
```bash
sudo apt install poppler-utils
```

### 3. Install the Cowork custom skill

This is what teaches Cowork how to create the decks.

1. Open your OneDrive
2. Navigate to `Documents` → create a folder `Cowork` → inside it create `Skills` → inside it create `analytics-hub-deck`
3. Full path: `OneDrive/Documents/Cowork/Skills/analytics-hub-deck/`
4. Copy `SKILL.md` from this repo into that folder

Cowork will **automatically discover and load** this skill at the start of every conversation.

---

## Usage (Per Report)

### Step 1 — Put your PDF in the uploads/ folder

Export your Power BI report as a PDF:
- **Power BI Desktop:** `File → Export → Export to PDF`
- **Power BI Service:** `File → Export → PDF`

Drop it in the `uploads/` folder.

### Step 2 — Run the prep script

```bash
python prepare.py uploads/your-report.pdf
```

This extracts every PDF page as a PNG image into `temp/your-report/`.

```
temp/
└── your-report/
    ├── page_1.png
    ├── page_2.png
    ├── page_3.png
    └── ...
```

The script prints exactly what to do next.

**Optional — create a ZIP too:**
```bash
python prepare.py uploads/your-report.pdf --zip
```

### Step 3 — Open Copilot Cowork

Go to https://m365.cloud.microsoft/ → Select **Cowork**

### Step 4 — Attach your images and type your prompt

**Option A (Easiest):** Drag ALL PNG files from `temp/your-report/` into the Cowork chat, then type:

> Create an executive deck for my AI-in-One Copilot report. I've attached all 12 dashboard images.

**Option B (OneDrive):** Upload the `temp/your-report/` folder to your OneDrive, then tell Cowork:

> Create an executive deck from my AI-in-One Copilot report. The dashboard images are in my OneDrive at Documents/CoworkAssets/your-report/

### Step 5 — Cowork builds your deck

Your custom SKILL.md is loaded automatically. Cowork will:
1. Confirm it sees all N images
2. Tell you which page it's analyzing as it goes
3. Synthesize insights across all pages
4. Use its PowerPoint skill to create the PPTX
5. Save the result to your OneDrive Cowork output folder

---

## Prompt Reference

| Deck type | Prompt |
|---|---|
| Executive deck, auto-detect | `Create an executive deck for my Copilot report. [N] images attached.` |
| Analyst guide | `Create an analyst guide for my Super Usage Adoption report. All [N] pages attached.` |
| Specific audience | `Create an exec deck for our CISO from my AI-in-One report. [N] images attached.` |
| Focused analysis | `Build an executive deck focused on agent adoption. AI-in-One dashboard, [N] images attached.` |
| Post to Teams | `Create the deck and post a 3-bullet summary to our #ai-adoption Teams channel.` |

---

## Supported Reports

| Report | Coverage |
|---|---|
| 🤖 AI-in-One Dashboard | M365 Copilot + Chat + Agents all-in-one |
| ⚡ Super Usage Adoption | Habit formation and super user journey |
| 🏆 Super User Impact | ROI and productivity measurement |
| 💬 Chat & Agent Intelligence | Session patterns and agent depth |
| 🐙 GitHub Copilot Impact | Developer analytics |
| 📊 M365 Copilot Readiness | License readiness scoring |

---

## Output

Cowork produces a PowerPoint saved to your OneDrive Cowork folder.

**Executive mode:** 15–20 slides  
- Cover with top 6 KPIs
- Strategic insights per dashboard section
- Cross-platform analysis
- 5 data-backed recommendations
- Closing with call to action

**Analyst mode:** 25–35 slides  
- Everything above + methodology, deep-dives, benchmarks, action planning template

---

## Cowork vs GitHub Copilot — When to Use Which

| Scenario | Use |
|---|---|
| You want to run this in VS Code from your terminal | [analytics-hub-deck](https://github.com/Fepilot/analytics-hub-deck) |
| You want Cowork to build the deck AND email/post results | **this repo** |
| You want to schedule a recurring monthly deck | **this repo** (Cowork scheduled prompts) |
| You're setting this up for non-technical users | **this repo** |

---

## File Structure

```
analytics-hub-cowork/
├── README.md               ← This file
├── SKILL.md                ← Copy to OneDrive/Documents/Cowork/Skills/analytics-hub-deck/
├── prepare.py              ← Run locally to extract PDF → PNG images
├── requirements.txt
├── uploads/                ← Drop your PDF here
├── temp/                   ← Auto-created by prepare.py (gitignored)
└── reports/
    ├── ai-in-one/GUIDE.md         ← Optional: reference guides per report type
    ├── super-usage-adoption/GUIDE.md
    ├── super-user-impact/GUIDE.md
    ├── chat-agent-intelligence/GUIDE.md
    ├── github-copilot-impact/GUIDE.md
    └── m365-readiness/GUIDE.md
```

---

## Known Cowork Limitations (as of April 2026)

- **No local file access** — Cowork can only read from OneDrive/SharePoint; it cannot access your local disk.
- **No script execution** — Cowork cannot run Python. That's why `prepare.py` must run locally.
- **PDF visual extraction is partial** — Power BI PDFs are image-only; the PDF skill can read some pages but not all. Always use extracted PNGs.
- **200 MB file size limit** — Large reports with many high-resolution pages may exceed this. The default 150 DPI in `prepare.py` keeps files small; use `--dpi 100` if needed.
- **Encrypted PDFs cannot be read** — Cowork cannot open encrypted files even with valid permissions.

---

## Related Resources

- [Microsoft Analytics Hub](https://github.com/microsoft/Analytics-Hub)
- [AI-in-One Dashboard](https://github.com/microsoft/AI-in-One-Dashboard)
- [Original analytics-hub-deck (GitHub Copilot version)](https://github.com/Fepilot/analytics-hub-deck)
- [Copilot Cowork documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/)
- [Copilot Cowork custom skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork#create-custom-skills)

---

MIT License — Free to use within your organization.
