# -*- coding: utf-8 -*-
"""Loss-check and done-check Source Texts chapters vs PDFs."""
from __future__ import annotations

import re
from pathlib import Path

import pypdf

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_DIR = ROOT / "Source" / "PDF"
TXT_DIR = ROOT / "Source Texts"

BOOKS = [
    {
        "name": "Rigger 5",
        "pdf": "rigger5.pdf",
        "folder": "Rigger 5",
        "extractor": "extract_rigger5.py",
        # Major TOC markers that must appear somewhere in extracts
        "must_have": [
            "RIGGING 101",
            "DEMOLITION DERBY",
            "RULING THE WAVES",
            "AIR SUPERIORITY",
            "THE AUTOMATED ARMY",
            "BUILDING THE PERFECT BEAST",
            "MAXIMUM PURSUIT",
            "Mack Hellhound",
            "CONTROL RIG",
            "Rigger Cocoon",
        ],
    },
    {
        "name": "Street Grimoire",
        "pdf": "streetgrimoire.pdf",
        "folder": "Street Grimoire",
        "extractor": "extract_streetgrimoire.py",
        "must_have": [
            "MAGICAL TRADITIONS",
            "EXPANDED GRIMOIRE",
            "BLOOD MAGIC",
            "INSECT SPIRITS",
            "SHADOW RITUALS",
            "ADEPTS IN THE SIXTH WORLD",
            "ALLY SPIRITS",
            "Background Count",
            "Mana Storm",
        ],
    },
    {
        "name": "Forbidden Arcana",
        "pdf": "forbiddenarcana.pdf",
        "folder": "Forbidden Arcana",
        "extractor": "extract_forbiddenarcana.py",
        "must_have": [
            "MAGIC MASTERY",
            "TEA & SYMPATHY",
            "BLOOD MAGIC",
            "ADVANCED ALCHEMY",
            "WILD SPIRITS",
            "Necro Magic",
            "Mentor Spirit",
            "Reagent",
        ],
    },
    {
        "name": "Run Faster",
        "pdf": "runfaster.pdf",
        "folder": "Run Faster",
        "extractor": "extract_runfaster.py",
        "must_have": [
            "DECADE",
            "CONSTRUCTION KITS",
            "SUM TO TEN",
            "INTO THE NIGHT",
            "HMHVV",
            "PACK YOUR KIT",
            "A DUMP OF ONE",
            "BOSSES AND BETRAYERS",
            "Metagenic",
        ],
    },
    {
        "name": "Street Lethal",
        "pdf": "streetlethal.pdf",
        "folder": "Street Lethal",
        "extractor": "extract_streetlethal.py",
        "must_have": [
            "EXPANDED ARSENAL",
            "MILITARY",
            "CORPSEC",
            "AT SEA",
            "LETHAL ARTS",
            "ADVENTURE HOOKS",
            "Narcoject",
            "Krime",
        ],
    },
    {
        "name": "Howling Shadows",
        "pdf": "howlingshadows.pdf",
        "folder": "Howling Shadows",
        "extractor": "extract_howlingshadows.py",
        "must_have": [
            "MUNDANE CRITTERS",
            "PARANORMAL ANIMALS",
            "MUTANT",
            "EXTRAPLANAR",
            "TECHNOCRITTERS",
            "PROTOSAPIENTS",
            "DRAKES",
            "CRITTER TABLES",
            "BUILDING MAN",
        ],
    },
]


def load_sections(extractor_path: Path) -> list[tuple[str, str, int, int]]:
    text = extractor_path.read_text(encoding="utf-8")
    # SECTIONS = [ ("file", "title", start, end), ... ]
    m = re.search(r"SECTIONS\s*=\s*\[(.*?)\n\]", text, re.S)
    if not m:
        return []
    block = m.group(1)
    rows = re.findall(
        r'\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*(\d+)\s*,\s*(\d+)\s*\)',
        block,
    )
    return [(a, b, int(c), int(d)) for a, b, c, d in rows]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def pdf_page_text(pdf: pypdf.PdfReader, i: int) -> str:
    return pdf.pages[i].extract_text() or ""


def sample_tokens(text: str, n: int = 12) -> list[str]:
    # Meaningful tokens from a page for presence checks
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    out = []
    seen = set()
    for w in words:
        lw = w.lower()
        if lw in {
            "that", "this", "with", "from", "have", "were", "they", "them",
            "their", "when", "what", "your", "into", "than", "then", "some",
            "will", "would", "could", "about", "there", "these", "those",
            "shadowrun", "page", "contents", "credits",
        }:
            continue
        if lw not in seen:
            seen.add(lw)
            out.append(w)
        if len(out) >= n:
            break
    return out


def check_book(book: dict) -> dict:
    folder = TXT_DIR / book["folder"]
    pdf_path = PDF_DIR / book["pdf"]
    extractor = ROOT / "Source" / "_extract" / book["extractor"]
    sections = load_sections(extractor)
    pdf = pypdf.PdfReader(str(pdf_path))
    n_pages = len(pdf.pages)

    issues: list[str] = []
    notes: list[str] = []

    chapter_files = sorted(folder.glob("[0-9]*.md"))
    if not chapter_files:
        issues.append("No chapter markdown files found")
        return {"book": book["name"], "issues": issues, "notes": notes, "ok": False}

    # INDEX exists and links
    idx = folder / "INDEX.md"
    if not idx.exists():
        issues.append("Missing INDEX.md")
    else:
        idx_text = idx.read_text(encoding="utf-8")
        for p in chapter_files:
            # link form uses %20 encoding sometimes
            if p.name not in idx_text and p.stem.split(" - ", 1)[-1] not in idx_text:
                # try URL-encoded name check loosely
                if p.name.replace(" ", "%20") not in idx_text:
                    issues.append(f"INDEX may not link {p.name}")

    # Section coverage vs extractor map
    covered = set()
    if sections:
        for fname, title, start, end in sections:
            path = folder / fname
            if not path.exists():
                issues.append(f"Missing chapter file: {fname}")
                continue
            size = path.stat().st_size
            if size < 200:
                issues.append(f"Too thin ({size}B): {fname}")
            body = path.read_text(encoding="utf-8")
            if not body.startswith("# "):
                issues.append(f"Missing H1: {fname}")
            if "**Source:**" not in body:
                issues.append(f"Missing Source line: {fname}")
            # page span continuity
            for i in range(start, end):
                covered.add(i)

            # Loss sample: pick first content page and mid page; require some tokens present
            sample_idxs = [start]
            if end - start > 2:
                sample_idxs.append(start + (end - start) // 2)
            for si in sample_idxs:
                if si >= n_pages:
                    continue
                page_txt = pdf_page_text(pdf, si)
                if len(page_txt.strip()) < 40:
                    continue  # image/blank page
                tokens = sample_tokens(page_txt, 8)
                hits = 0
                body_n = normalize(body)
                for tok in tokens:
                    if normalize(tok) in body_n:
                        hits += 1
                if tokens and hits < max(2, len(tokens) // 3):
                    issues.append(
                        f"Possible loss in {fname} vs PDF idx {si}: "
                        f"only {hits}/{len(tokens)} sample tokens found "
                        f"({', '.join(tokens[:5])})"
                    )
        # orphan page check: pages after TOC that aren't covered
        # Ignore cover/blank early pages 0-1 and trailing copyright blanks
        body_start = min((s[2] for s in sections), default=0)
        body_end = max((s[3] for s in sections), default=n_pages)
        orphans = []
        for i in range(body_start, min(body_end, n_pages)):
            if i not in covered:
                orphans.append(i)
        if orphans:
            issues.append(f"Uncovered PDF page indices in section map: {orphans[:20]}")
        # trailing pages after last section
        last_end = max(s[3] for s in sections)
        if last_end < n_pages - 2:
            # check if trailing pages have real text
            trailing_text = 0
            for i in range(last_end, n_pages):
                trailing_text += len((pdf_page_text(pdf, i) or "").strip())
            if trailing_text > 500:
                issues.append(
                    f"Possible missed end pages: section map ends at {last_end}, "
                    f"PDF has {n_pages} pages with {trailing_text} trailing chars"
                )
            else:
                notes.append(f"Trailing pages {last_end}-{n_pages-1} mostly blank/copyright (ok)")
    else:
        issues.append(f"Could not parse SECTIONS from {extractor.name}")

    # Must-have TOC keywords across all chapter text
    all_text = "\n".join(p.read_text(encoding="utf-8") for p in chapter_files)
    all_n = normalize(all_text)
    for key in book["must_have"]:
        if normalize(key) not in all_n:
            # softer: allow partial
            parts = normalize(key).split()
            if not all(p in all_n for p in parts if len(p) > 3):
                issues.append(f"Must-have marker missing: {key}")

    # Done-check style
    em = all_text.count("\u2014") + all_text.count("—")
    if em:
        issues.append(f"Em dashes found: {em}")

    emptyish = [p.name for p in chapter_files if p.stat().st_size < 500]
    if emptyish:
        issues.append(f"Near-empty chapters: {emptyish}")

    # Heading presence (formatting done)
    h2_total = sum(1 for p in chapter_files for ln in p.read_text(encoding="utf-8").splitlines() if ln.startswith("## "))
    notes.append(f"{len(chapter_files)} chapters, {sum(p.stat().st_size for p in chapter_files)//1024}KB, {h2_total} H2s")

    return {
        "book": book["name"],
        "issues": issues,
        "notes": notes,
        "ok": len(issues) == 0,
        "chapters": len(chapter_files),
    }


def main():
    results = []
    for book in BOOKS:
        print(f"\n=== {book['name']} ===")
        r = check_book(book)
        results.append(r)
        for n in r["notes"]:
            print("NOTE:", n)
        if r["ok"]:
            print("PASS: loss-check + done-check")
        else:
            print("FAIL:")
            for i in r["issues"]:
                print(" -", i)
    print("\n===== SUMMARY =====")
    for r in results:
        print(f"{r['book']}: {'PASS' if r['ok'] else 'FAIL'} ({r.get('chapters',0)} chapters, {len(r['issues'])} issues)")


if __name__ == "__main__":
    main()
