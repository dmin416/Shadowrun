# -*- coding: utf-8 -*-
"""Fix concrete errors found in audit: em/en dashes + Forbidden Arcana structure."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")


def fix_dashes_in_tree(rel: str) -> int:
    n = 0
    for p in (ROOT / rel).rglob("*.md"):
        t = p.read_text(encoding="utf-8")
        newt = t.replace("\u2014", "-").replace("\u2013", "-")
        if newt != t:
            p.write_text(newt, encoding="utf-8")
            n += t.count("\u2014") + t.count("\u2013")
            print(f"  dashes {p.relative_to(ROOT)}: {t.count(chr(0x2014))+t.count(chr(0x2013))}")
    return n


# Mastery qualities / tradition section headers often appear as ALL CAPS then Karma
KARMA_HEADER = re.compile(
    r"(?<![A-Za-z])"
    r"([A-Z][A-Z0-9][A-Z0-9 \-'/\[\]]{1,60}?)"
    r"\s+"
    r"(\d+\s+KARMA(?:\s+PER LEVEL)?(?:\s*\([^)]{0,40}\))?)"
    r"(?=\s+(?:Minimum Requirements?:|REQUIREMENTS?:|A character|An adept|Characters|This quality|Using this|When |All |Along |The |Magicians|Adepts))",
)

SECTION_HEADERS = [
    "TRADITION UPDATES",
    "RELATED MENTOR SPIRITS",
    "PREFERRED SPELLS",
    "NOTABLE TEACHERS",
    "GAME INFORMATION",
    "NEW METAMAGICS",
    "NEW RITUALS",
    "NEW SPELLS",
    "COMBAT SPELLS",
    "DETECTION SPELLS",
    "HEALTH SPELLS",
    "ILLUSION SPELLS",
    "MANIPULATION SPELLS",
    "EXPANDED ASPECTS",
    "FOCUSED AWAKENED",
    "ADVANCED ALCHEMY",
    "BLOOD MAGIC",
    "SEEING THE INVISIBLE WORLD",
    "WHERE THE WILD THINGS ARE",
    "ALCHEMICAL ARMORER",  # sometimes appears without karma nearby due to prose lead-in
]

# Running headers glued into body
RUNNING = re.compile(
    r"\s*FORBIDDEN ARCANA(?:\s+[A-Z][A-Z \-]{2,40})?\s*\d{1,3}\s*(?:[A-Z][A-Z \-]{2,40}\s*>>)?\s*",
    re.I,
)
RUNNING2 = re.compile(
    r"\s*\d{1,3}\s+[A-Z][A-Z \-]{2,40}\s*>>\s*",
)
RUNNING3 = re.compile(
    r"\s*<<\s*[A-Z][A-Z \-]{2,40}\s+\d{1,3}\s*",
)


def title_case(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at"}
    parts = []
    for i, w in enumerate(s.split()):
        # keep [BRACKET] tags
        if w.startswith("[") and w.endswith("]"):
            parts.append(w[0] + w[1:].title() if len(w) > 2 else w)
            continue
        lw = w.lower().strip("()")
        if i > 0 and lw in small:
            parts.append(lw)
        else:
            core = re.sub(r"[^A-Za-z0-9'].*$", "", w)
            rest = w[len(core) :]
            if not core:
                parts.append(w)
            else:
                parts.append(core[:1].upper() + core[1:].lower() + rest)
    return " ".join(parts)


def fix_ocr_spacing(text: str) -> str:
    # p. 1 71 -> p. 171 ; p. 1 70 -> p. 170
    text = re.sub(r"\bp\.\s*(\d)\s+(\d{2})\b", r"p. \1\2", text)
    # years like 201 7 -> 2017, 206 4 -> 2064
    text = re.sub(r"\b(20\d)\s+(\d)\b", r"\1\2", text)
    # Jack - Pointers -> JackPointers (book uses JackPointers / JackPoint)
    text = text.replace("Jack - Pointers", "JackPointers")
    text = text.replace("Jack - Point", "JackPoint")
    return text


def promote_fa_headers(text: str) -> str:
    # Strip source header block to protect
    m = re.match(r"(?s)^(#[^\n]+\n\n\*\*Source:\*\*[^\n]+\n\n)(.*)$", text)
    if not m:
        return text
    head, body = m.group(1), m.group(2)

    body = RUNNING.sub(" ", body)
    body = RUNNING2.sub(" ", body)
    body = RUNNING3.sub(" ", body)

    def karma_sub(m: re.Match) -> str:
        name = m.group(1).strip()
        karma = m.group(2).strip()
        # skip if name looks like a sentence fragment
        if name.count(" ") > 8:
            return m.group(0)
        if any(x in name for x in ("THE ", "THIS ", "WHEN ", "WITH ", "FROM ")):
            # allow known quality names that start with those? rare
            if name not in {"THE TRANSPORTER"}:
                return m.group(0)
        return f"\n\n### {title_case(name)}\n\n**{karma}**\n\n"

    body = KARMA_HEADER.sub(karma_sub, body)

    # Promote known section headers when they appear as ALL CAPS words mid-flow
    for sec in SECTION_HEADERS:
        # already a markdown header?
        pat = re.compile(rf"(?<!# )\b{re.escape(sec)}\b")
        body = pat.sub(lambda _m, s=sec: f"\n\n## {title_case(s)}\n\n", body)

    # Tradition name pattern: BLACK MAGIC (UPDATE) DESCRIPTION
    body = re.sub(
        r"\b([A-Z][A-Z0-9 \-'/]{2,40}?)\s+\((UPDATE|NEW)\)\s+DESCRIPTION\b",
        lambda m: f"\n\n## {title_case(m.group(1))} ({title_case(m.group(2))})\n\n### Description\n\n",
        body,
    )

    # Lone ALL-CAPS subsection labels
    for lab in ("DESCRIPTION", "IDEALS", "SORCERY", "CONJURING", "ENCHANTING", "RULES"):
        body = re.sub(
            rf"(?<!# )\b{lab}\b(?=\s+[A-Z]|\s+[A-Za-z])",
            f"\n\n### {title_case(lab)}\n\n",
            body,
            count=20,
        )

    body = fix_ocr_spacing(body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return head + body.strip() + "\n"


def fix_forbidden_arcana() -> None:
    d = ROOT / "Source Texts" / "Forbidden Arcana"
    for p in sorted(d.glob("*.md")):
        if p.name == "INDEX.md":
            continue
        t = p.read_text(encoding="utf-8")
        newt = promote_fa_headers(t)
        # also dash fix
        newt = newt.replace("\u2014", "-").replace("\u2013", "-")
        if newt != t:
            p.write_text(newt, encoding="utf-8")
            h2 = len(re.findall(r"^## ", newt, re.M))
            h3 = len(re.findall(r"^### ", newt, re.M))
            print(f"  FA {p.name}: H2={h2} H3={h3}")


def fix_serrated_maps() -> None:
    """Clarify image-only map stubs (not recoverable as text)."""
    d = ROOT / "Source Texts" / "Serrated Edge"
    denver = d / "14 - Denver Map.md"
    med = d / "16 - Medical Center Map.md"
    denver.write_text(
        """# Denver Map

**Source:** Serrated Edge (Denver Adventure 1) | `Source/PDF/serratededge.pdf` | PDF page index 60-60

**Extract note:** This PDF page is a map graphic. No usable body text beyond the printed caption below.

## Caption

Note: No Aztlan sector is shown on the map, as it has not been recognized in any official capacity. The area they have moved into is the southern section of PCC territory-that is, the areas south of Sixth Avenue (Route 6).

For the map itself, open the PDF at the page above.
""",
        encoding="utf-8",
    )
    med.write_text(
        """# Medical Center Map

**Source:** Serrated Edge (Denver Adventure 1) | `Source/PDF/serratededge.pdf` | PDF page index 62-62

**Extract note:** These PDF pages are image-only map art (no extractable text via pymupdf).

For the map itself, open the PDF at the page above.
""",
        encoding="utf-8",
    )
    print("  Serrated Edge map stubs clarified")


if __name__ == "__main__":
    print("=== Em/en dashes ===")
    n1 = fix_dashes_in_tree("Encyclopedia")
    n2 = fix_dashes_in_tree("Mechanics")
    print(f"Total dash replacements: {n1 + n2}")
    print("\n=== Forbidden Arcana ===")
    fix_forbidden_arcana()
    print("\n=== Serrated Edge maps ===")
    fix_serrated_maps()
