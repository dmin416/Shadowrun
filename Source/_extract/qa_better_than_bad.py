# -*- coding: utf-8 -*-
"""Loss-check / done-check Better Than Bad Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "better-than-bad-pdf.pdf"
FOLDER = ROOT / "Source Texts" / "Better Than Bad"
REPORT = ROOT / "Source" / "_extract" / "better_than_bad_qa_report.md"
EXTRACTOR = ROOT / "Source" / "_extract" / "extract_better_than_bad.py"

MUST_HAVE = [
    "hooder",
    "Pretoria",
    "Grey Mana",
    "GreyWare",
    "Black Star",
    "Robin Hood",
    "Paydubfau",
    "Blight",
    "Social Chameleon",
]


def load_sections() -> list[tuple[str, str, int, int]]:
    text = EXTRACTOR.read_text(encoding="utf-8")
    m = re.search(r"SECTIONS\s*=\s*\[(.*?)\n\]", text, re.S)
    if not m:
        return []
    rows = re.findall(
        r'\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*(\d+)\s*,\s*(\d+)\s*\)',
        m.group(1),
    )
    return [(a, b, int(c), int(d)) for a, b, c, d in rows]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def sample_tokens(text: str, n: int = 10) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    skip = {
        "that", "this", "with", "from", "have", "were", "they", "them",
        "their", "when", "what", "your", "into", "than", "then", "some",
        "will", "would", "could", "about", "there", "these", "those",
        "shadowrun", "page", "contents", "credits", "better",
    }
    out: list[str] = []
    seen: set[str] = set()
    for w in words:
        lw = w.lower()
        if lw in skip or lw in seen:
            continue
        seen.add(lw)
        out.append(w)
        if len(out) >= n:
            break
    return out


def main() -> None:
    sections = load_sections()
    doc = fitz.open(str(PDF_PATH))
    n_pages = doc.page_count
    issues: list[str] = []
    notes: list[str] = []
    chapter_rows: list[str] = []

    idx = FOLDER / "INDEX.md"
    if not idx.exists():
        issues.append("Missing INDEX.md")
    else:
        idx_text = idx.read_text(encoding="utf-8")
        for fname, _, _, _ in sections:
            if fname.replace(" ", "%20") not in idx_text and fname not in idx_text:
                title = fname.split(" - ", 1)[-1].replace(".md", "")
                if title not in idx_text:
                    issues.append(f"INDEX may not link {fname}")

    all_parts: list[str] = []
    for fname, title, start, end in sections:
        path = FOLDER / fname
        if not path.exists():
            issues.append(f"Missing {fname}")
            chapter_rows.append(f"| {fname} | FAIL | missing |")
            continue
        body = path.read_text(encoding="utf-8")
        all_parts.append(body)
        chap_issues: list[str] = []
        if path.stat().st_size < 200:
            chap_issues.append(f"thin ({path.stat().st_size}B)")
        if not body.startswith("# "):
            chap_issues.append("no H1")
        if body.count("\u00ad"):
            chap_issues.append("soft hyphens")
        if body.count("\u2014") or body.count("—"):
            chap_issues.append("em dashes")
        giant = sum(1 for ln in body.splitlines() if len(ln) >= 1200)
        if giant:
            notes.append(f"{fname}: {giant} paras >=1200 chars (format residual)")

        body_n = normalize(body)
        sample_idxs = [start]
        if end - start > 3:
            sample_idxs.append(start + (end - start) // 2)
        for si in sample_idxs:
            if si >= n_pages:
                continue
            page_txt = doc[si].get_text("text") or ""
            if len(page_txt.strip()) < 40:
                continue
            upper = page_txt.upper()
            cut = upper.find(title.upper().split(",")[0][:12])
            sample_src = page_txt[cut:] if cut >= 0 else page_txt
            # Shared pages: prefer INTRODUCTION portion for ch03
            if fname.startswith("03 -"):
                cut2 = upper.find("INTRODUCTION")
                if cut2 >= 0:
                    sample_src = page_txt[cut2:]
            tokens = sample_tokens(sample_src, 8)
            if len(tokens) < 3:
                notes.append(f"{fname}: sparse sample at PDF idx {si} (skipped)")
                continue
            hits = sum(1 for tok in tokens if normalize(tok) in body_n)
            if tokens and hits < max(2, len(tokens) // 3):
                chap_issues.append(
                    f"loss vs PDF idx {si}: {hits}/{len(tokens)} "
                    f"({', '.join(tokens[:5])})"
                )

        status = "PASS" if not chap_issues else "FAIL"
        detail = "; ".join(chap_issues) if chap_issues else "ok"
        chapter_rows.append(f"| {fname} | {status} | {detail} |")
        for c in chap_issues:
            issues.append(f"{fname}: {c}")

    all_n = normalize("\n".join(all_parts))
    missing = [m for m in MUST_HAVE if normalize(m) not in all_n]
    if missing:
        issues.append(f"Missing must-have markers: {', '.join(missing)}")

    ok = not issues
    lines = [
        "# Better Than Bad QA report",
        "",
        f"PDF: `{PDF_PATH.name}` ({n_pages} pages)",
        f"Folder: `Source Texts/Better Than Bad/`",
        f"Overall: **{'PASS' if ok else 'FAIL'}**",
        "",
        "## Chapters",
        "",
        "| File | Status | Notes |",
        "| --- | --- | --- |",
        *chapter_rows,
        "",
        "## Issues",
        "",
    ]
    if issues:
        lines.extend(f"- {x}" for x in issues)
    else:
        lines.append("- None")
    lines += ["", "## Notes", ""]
    notes.append(
        "Residual: some gear tables / JackPoint handles still inline in Building a Hooder; "
        "Hooder Runs dice tables are code-blockish not markdown tables."
    )
    lines.extend(f"- {x}" for x in notes)
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Overall: {'PASS' if ok else 'FAIL'} ({len(issues)} issues)")
    for x in issues[:25]:
        print(" -", x)
    print("wrote", REPORT)
    doc.close()


if __name__ == "__main__":
    main()
