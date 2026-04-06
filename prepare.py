#!/usr/bin/env python3
"""
Analytics Hub — CoWork Prep Script
===================================
Extracts a Power BI PDF report into individual PNG images,
ready to drag into Copilot Cowork.

Usage:
    python prepare.py uploads/my-report.pdf
    python prepare.py uploads/my-report.pdf --zip          # also create a ZIP
    python prepare.py uploads/my-report.pdf --onedrive     # open OneDrive upload folder

The PNG files land in:  temp/<report-stem>/page_1.png, page_2.png, ...
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Dependency bootstrap — same pattern as original repo
# ---------------------------------------------------------------------------

def _ensure_deps():
    required = {"pdf2image": "pdf2image", "PIL": "Pillow"}
    missing = [pkg for mod, pkg in required.items() if not _can_import(mod)]
    if missing:
        print(f"Installing: {', '.join(missing)}")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet"] + missing
        )
        print("Done.\n")


def _can_import(module):
    try:
        __import__(module)
        return True
    except ImportError:
        return False


_ensure_deps()

# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

from pdf2image import convert_from_path  # noqa: E402
from PIL import Image  # noqa: E402 (unused but validates Pillow install)


TEMP_ROOT = Path("temp")


def extract(pdf_path: Path, dpi: int = 150) -> Path:
    """Convert every page of the PDF to a numbered PNG. Returns output folder."""
    out_dir = TEMP_ROOT / pdf_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  Extracting: {pdf_path.name}")
    print(f"  Output dir: {out_dir}/")
    print(f"{'='*60}\n")

    pages = convert_from_path(str(pdf_path), dpi=dpi)
    if not pages:
        print("ERROR: No pages could be extracted. Is poppler installed?")
        print("  Install: https://github.com/oschwartz10612/poppler-windows/releases/")
        sys.exit(1)

    saved = []
    for i, page in enumerate(pages, start=1):
        out_file = out_dir / f"page_{i}.png"
        page.save(str(out_file), "PNG")
        print(f"  Saved page {i:>3} → {out_file}")
        saved.append(out_file)

    print(f"\n  Total: {len(saved)} page(s) extracted.\n")
    return out_dir


def make_zip(out_dir: Path) -> Path:
    """Zip the output folder — handy for OneDrive upload."""
    zip_path = TEMP_ROOT / f"{out_dir.name}.zip"
    shutil.make_archive(str(zip_path.with_suffix("")), "zip", str(out_dir))
    print(f"  ZIP created → {zip_path}")
    return zip_path


def print_cowork_instructions(out_dir: Path, pdf_name: str, zip_path: Path | None):
    page_count = len(list(out_dir.glob("page_*.png")))

    print("\n" + "=" * 60)
    print("  NEXT STEPS FOR COPILOT COWORK")
    print("=" * 60)
    print(f"\n  {page_count} page images are ready in:  {out_dir}/\n")

    print("  ── Option A: Drag images directly into Cowork (easiest) ──")
    print(f"  1. Open Copilot Cowork at https://m365.cloud.microsoft/")
    print(f"  2. Select 'Cowork'")
    print(f"  3. Drag ALL {page_count} PNG files from  {out_dir}/  into the chat")
    print(f"  4. Type your prompt (copy one from below)")
    print()

    if zip_path:
        print("  ── Option B: Upload as ZIP to OneDrive ──")
        print(f"  1. Upload {zip_path} to OneDrive > Documents > CoworkAssets")
        print(f"  2. Open Cowork, attach the ZIP from OneDrive")
        print(f"  3. Type your prompt (copy one from below)")
        print()

    print("  ── Prompt examples ──")
    print()
    print(f'  "Create an executive deck for my AI-in-One report. I\'ve attached')
    print(f'   all {page_count} dashboard images."')
    print()
    print(f'  "Create an analyst guide for my Super Usage Adoption report.')
    print(f'   All {page_count} pages are attached."')
    print()
    print(f'  "Build an executive deck for {pdf_name} focused on agent adoption.')
    print(f'   The {page_count} dashboard images are attached."')
    print()
    print("=" * 60 + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract Power BI PDF pages to PNG for Copilot Cowork"
    )
    parser.add_argument("pdf", help="Path to the PDF file (e.g. uploads/report.pdf)")
    parser.add_argument(
        "--zip",
        action="store_true",
        help="Also create a ZIP of the output folder",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="Image resolution (default: 150 DPI — good balance of quality vs file size)",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"ERROR: File not found: {pdf_path}")
        sys.exit(1)

    out_dir = extract(pdf_path, dpi=args.dpi)
    zip_path = make_zip(out_dir) if args.zip else None
    print_cowork_instructions(out_dir, pdf_path.name, zip_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
