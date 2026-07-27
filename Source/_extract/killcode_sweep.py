# -*- coding: utf-8 -*-
"""Kill Code per-chapter phrase / JackPoint / table / format sweep."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF = ROOT / "Source" / "PDF" / "killcode.pdf"
MD_DIR = ROOT / "Source Texts" / "Kill Code"
OUT = ROOT / "Source" / "_extract" / "killcode_sweep_report.md"

# (num, filename, start_page_inclusive, end_page_exclusive) using fitz indices (= print page for this PDF)
CHAPTERS = [
    (1, "01 - Contents and Credits.md", 2, 5),
    (2, "02 - Introduction.md", 5, 6),
    (3, "03 - Double Decker.md", 6, 10),
    (4, "04 - So You Want To Be A Hacker.md", 10, 48),
    (5, "05 - Dips & Chips.md", 48, 76),
    (6, "06 - Disk Jockeys & Lightstream Riders.md", 76, 82),
    (7, "07 - Parallel Processing.md", 82, 86),
    (8, "08 - Data Streams.md", 86, 94),
    (9, "09 - In the Flow.md", 94, 106),
    (10, "10 - A Million Icons Bloom.md", 106, 118),
    (11, "11 - Diving Under.md", 118, 124),
    (12, "12 - Infinite Realms.md", 124, 136),
    (13, "13 - Null Sign.md", 136, 156),
    (14, "14 - Into the Wild.md", 156, 164),
    (15, "15 - The Core of Consciousness.md", 164, 187),
    (16, "16 - Rule Index.md", 187, 194),
]

CHROME = re.compile(
    r"(?im)^(?:kill code|contents?\s*&?\s*credits|so you want to be a hacker|"
    r"dips\s*&?\s*chips|disk jockeys.*?riders|parallel processing|"
    r"data streams|in the flow|a million icons bloom|diving under|"
    r"infinite realms|null signs?|into the wild|the core of consciousness|"
    r"rules?\s*index|"
    r">>.*?<<|<<.*?>>|"
    r"\d+\s+(?:so you want|dips|disk jockeys|parallel|data streams|in the flow|"
    r"a million|diving|infinite|null|into the wild|core of|rules?).*$|"
    r"^\s*\d+\s*$)"
)

SOFT_HYPHEN_SPLIT = re.compile(r"([a-z]{2,})-\s*\n\s*([a-z]{2,})", re.I)


def normalize_words(text: str) -> set[str]:
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2014", "-").replace("\u2013", "-").replace("\u2026", "...")
    text = text.replace("\u00ad", "")  # soft hyphen
    # drop chrome-ish leftovers
    text = CHROME.sub(" ", text)
    return set(re.findall(r"[A-Za-z][A-Za-z0-9']{4,}", text.lower()))


def join_soft_hyphens(text: str) -> str:
    prev = None
    while prev != text:
        prev = text
        text = SOFT_HYPHEN_SPLIT.sub(r"\1\2", text)
    return text


def extract_page_phrases(page_text: str, n: int = 8) -> list[str]:
    """Sample distinctive phrases from a page (joined lines, length 40-90)."""
    t = join_soft_hyphens(page_text)
    # strip chrome lines
    lines = []
    for line in t.splitlines():
        s = line.strip()
        if not s:
            continue
        if CHROME.match(s):
            continue
        if re.fullmatch(r"\d+", s):
            continue
        if s.startswith(">") and len(s) < 3:
            continue
        lines.append(s)
    blob = " ".join(lines)
    blob = re.sub(r"\s+", " ", blob)
    phrases = []
    # take windows of ~12 words at several offsets
    words = blob.split()
    if len(words) < 8:
        return []
    step = max(12, len(words) // (n + 1))
    for i in range(0, len(words) - 8, step):
        ph = " ".join(words[i : i + 12])
        # skip pure handles / short
        if len(ph) < 35:
            continue
        # skip if mostly uppercase chrome leftover
        if ph.isupper() and len(ph) < 50:
            continue
        phrases.append(ph)
        if len(phrases) >= n:
            break
    return phrases


def phrase_in_md(phrase: str, md_norm: str) -> bool:
    # normalize phrase similarly
    p = phrase.lower()
    p = p.replace("\u2019", "'").replace("\u2018", "'")
    p = p.replace("\u201c", '"').replace("\u201d", '"')
    p = re.sub(r"[^a-z0-9' ]+", " ", p)
    p = re.sub(r"\s+", " ", p).strip()
    # allow soft hyphen remnants by dropping internal spaces around short tokens? use word subset
    pw = [w for w in p.split() if len(w) >= 3]
    if len(pw) < 6:
        return p in md_norm
    # sliding: require 6 consecutive words present as substring
    for i in range(len(pw) - 5):
        chunk = " ".join(pw[i : i + 6])
        if chunk in md_norm:
            return True
    return False


def jackpoint_handles_pdf(text: str) -> list[str]:
    """PDF JackPoint: comment body then handle on its own line after >"""
    handles = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if s == ">" or s.startswith(">\t") or s == ">":
            # next non-empty might be handle if short
            for j in range(i + 1, min(i + 4, len(lines))):
                h = lines[j].strip()
                if not h:
                    continue
                if h.startswith(">"):
                    continue
                # handle-like: short, no period at end usually, starts with letter or /
                if len(h) <= 40 and re.match(r"^[A-Za-z0-9/!.'\- ]+$", h):
                    # not a sentence
                    if h.count(" ") <= 4 and not h.endswith((".", ",", ";")):
                        handles.append(h)
                break
    return handles


def jackpoint_handles_md(text: str) -> list[str]:
    return re.findall(r"^>\s*\*\*([^*]+)\*\*", text, re.M)


def count_tables_md(text: str) -> int:
    return len(re.findall(r"^\|[^\n]+\|\s*$", text, re.M))


def main() -> None:
    pdf = fitz.open(str(PDF))
    report = []
    report.append("# Kill Code per-chapter sweep report\n")
    report.append(
        "Method: size ratio, per-page phrase sampling (6-word chunk hits), "
        "em/en dashes + ellipsis, JackPoint handle counts, markdown table row counts, "
        "bleed of next-chapter title.\n"
    )
    report.append(
        "| # | Chapter | Loss | Size ratio | Weak pages | Em/ellip | JP PDF→MD | Tables | Notes |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
    )

    findings: list[str] = []
    next_titles = {
        1: None,
        2: "DOUBLE DECKER",
        3: "MATRIX 101",
        4: "BROUGHT TO YOU BY: ESTABAN",
        5: "POSITIVE QUALITIES",
        6: "PARALLEL PROCESSING",
        7: "DATA STREAMS",
        8: "IN THE FLOW",
        9: "A MILLION ICONS BLOOM",
        10: "DIVING UNDER",
        11: "INFINITE REALMS",
        12: "NULL SIGN",
        13: "INTO THE WILD",
        14: "THE CORE OF",
        15: "RULE INDEX",
        16: None,
    }

    for num, fname, start, end in CHAPTERS:
        md_path = MD_DIR / fname
        md = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        pages = []
        for i in range(start, min(end, pdf.page_count)):
            pages.append((i, pdf[i].get_text()))
        raw = "\n".join(t for _, t in pages)
        joined = join_soft_hyphens(raw)

        md_norm = md.lower()
        md_norm = md_norm.replace("\u2019", "'").replace("\u2018", "'")
        md_norm = re.sub(r"[^a-z0-9' \n]+", " ", md_norm)
        md_norm = re.sub(r"\s+", " ", md_norm)

        weak = []
        miss_examples = []
        for i, t in pages:
            phrases = extract_page_phrases(t, n=6)
            if not phrases:
                continue
            hits = sum(1 for p in phrases if phrase_in_md(p, md_norm))
            rate = hits / len(phrases)
            if rate < 0.8:
                weak.append(f"{i}({rate:.0%})")
                for p in phrases:
                    if not phrase_in_md(p, md_norm):
                        miss_examples.append((i, p[:80]))
                        break

        # size: strip chrome from raw for fairer ratio
        raw_words = normalize_words(joined)
        md_words = normalize_words(md)
        # missing substantial words (filter soft-hyphen fragments)
        miss_words = sorted(
            w
            for w in (raw_words - md_words)
            if len(w) >= 6
            and not w.endswith("-")
            and w
            not in {
                "contents",
                "credits",
                "posted",
                "killcode",
            }
        )
        # heuristic: soft-hyphen halves often look like truncations; ignore if stem in md
        real_miss = []
        for w in miss_words:
            # if any md word startswith w or w is prefix of joined word, skip
            if any(mw.startswith(w) or w.startswith(mw[: max(4, len(w) - 2)]) for mw in md_words):
                continue
            real_miss.append(w)
        real_miss = real_miss[:40]

        ratio = (len(md) / max(1, len(joined))) if joined else 0
        em = md.count("\u2014") + md.count("\u2013") + md.count("\u2026")
        jp_pdf = jackpoint_handles_pdf(raw)
        jp_md = jackpoint_handles_md(md)
        tables = count_tables_md(md)

        bleed = ""
        nxt = next_titles.get(num)
        if nxt and nxt.lower() in md.lower() and num not in (4,):  # ch4 mentions many
            # only flag if appears as heading-like near end
            tail = md[-800:].upper()
            if nxt in tail:
                bleed = f"possible bleed:{nxt}"

        # special: ch1/2 share page 5; ch2 shouldn't have credits list
        notes = []
        if weak:
            notes.append("weak:" + ",".join(weak[:6]))
        if em:
            notes.append(f"em={em}")
        if abs(len(jp_pdf) - len(jp_md)) > 5 and (jp_pdf or jp_md):
            notes.append(f"JPΔ pdf={len(jp_pdf)} md={len(jp_md)}")
        if ratio < 0.75 and num not in (1, 16):
            notes.append(f"thin ratio {ratio:.2f}")
        if real_miss and num not in (1, 2, 16):
            notes.append("misswords:" + ",".join(real_miss[:8]))
        if bleed:
            notes.append(bleed)

        # loss verdict
        if not md:
            verdict = "FAIL missing"
        elif weak and len(weak) > max(1, (end - start) // 4):
            verdict = "FAIL weak pages"
        elif ratio < 0.65 and num not in (1, 16):
            verdict = "FAIL thin"
        elif em:
            verdict = "FIX em"
        else:
            verdict = "PASS"

        report.append(
            f"| {num:02d} | {fname} | {verdict} | {ratio:.2f} | "
            f"{len(weak)}/{end-start} | {em} | {len(jp_pdf)}→{len(jp_md)} | {tables} | "
            f"{'; '.join(notes) if notes else '-'} |\n"
        )

        if verdict != "PASS" or miss_examples[:3]:
            findings.append(f"\n## Ch{num:02d} {fname}\n")
            findings.append(f"- Verdict: **{verdict}**\n")
            findings.append(f"- Size ratio: {ratio:.2f} (md {len(md)} / pdf {len(joined)})\n")
            findings.append(f"- Weak pages: {weak or 'none'}\n")
            findings.append(f"- JP handles PDF→MD: {len(jp_pdf)}→{len(jp_md)}\n")
            if miss_examples:
                findings.append("- Example missed phrases:\n")
                for pi, ph in miss_examples[:8]:
                    findings.append(f"  - p.{pi}: `{ph}`\n")
            if real_miss:
                findings.append(f"- Sample missing words: {', '.join(real_miss[:20])}\n")

    report.append("\n---\n")
    report.extend(findings)
    OUT.write_text("".join(report), encoding="utf-8")
    print(f"Wrote {OUT}")
    print("".join(report[: report.index("---\n") + 1] if "---\n" in report else report[:40]))


if __name__ == "__main__":
    main()
