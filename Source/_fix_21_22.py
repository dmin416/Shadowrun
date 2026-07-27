"""Rebuild Street Gear and Index chapters with cleaner formatting."""
from __future__ import annotations

import re
from pathlib import Path
from pypdf import PdfReader

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source Texts\Shadowrun Fifth Edition Core Rulebook")

FOOTER = re.compile(
    r"(?:\d{2,3}\s+)?(?:GEAR RATINGS|BUYING GEAR|STREET GEAR|GEAR LISTING|"
    r"ELECTRONICS|AUGMENTATION|SHADOWRUN,? FIFTH EDITION|MASTER INDEX|"
    r"TABLES|IMPORTANT TABLES)"
    r"(?:\s*(?:>>|<<))?(?:\s*\d{2,3})?",
    re.I,
)
SIDEBAR = re.compile(r"(?:<<|>>).{0,40}")
PAGE_REF = re.compile(r"\bP\s*\.\s*\d+\b", re.I)


def walk(items, depth=0, acc=None):
    if acc is None:
        acc = []
    for it in items:
        if isinstance(it, list):
            walk(it, depth + 1, acc)
        else:
            title = (getattr(it, "title", None) or str(it)).strip()
            try:
                page = reader.get_destination_page_number(it)
            except Exception:
                page = None
            acc.append((depth, title, page, it))
    return acc


def clean_line(s: str) -> str:
    s = SIDEBAR.sub("", s)
    s = FOOTER.sub("", s)
    s = PAGE_REF.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("\u2014", " - ").replace("\u2013", "-")
    return s


def extract_range(start: int, end: int) -> list[str]:
    lines = []
    for i in range(start, end):
        t = reader.pages[i].extract_text() or ""
        for line in t.splitlines():
            c = clean_line(line)
            if not c:
                continue
            if re.fullmatch(r"\d+", c):
                continue
            lines.append(c)
    return lines


def join_hyphens(lines: list[str]) -> list[str]:
    out = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        while cur.endswith("-") and i + 1 < len(lines):
            cur = cur[:-1] + lines[i + 1]
            i += 1
        out.append(cur)
        i += 1
    return out


def build_street_gear():
    # collect headings under Street Gear
    flat = walk(reader.outline)
    headings = []
    capturing = False
    base = 0
    for d, t, p, _ in flat:
        if t == "Street Gear":
            capturing = True
            base = d
            continue
        if capturing:
            if d <= base:
                break
            headings.append((d - base, t))

    heading_map = {re.sub(r"[^a-z0-9]+", "", t.lower()): (d, t) for d, t in headings}

    lines = join_hyphens(extract_range(420, 472))
    paras: list[str] = []
    buf = ""

    def flush():
        nonlocal buf
        if buf:
            paras.append(buf.strip())
            buf = ""

    for line in lines:
        key = re.sub(r"[^a-z0-9]+", "", line.lower())
        # ALL CAPS heading match
        matched = None
        for hk, (depth, title) in sorted(heading_map.items(), key=lambda x: -len(x[0])):
            tu = title.upper()
            if line.upper().startswith(tu) and (
                line.isupper()
                or line.upper() == tu
                or (line[: len(title)].isupper() and len(line) >= len(title))
            ):
                # verify uppercase span
                if not line[: len(title)].replace(" ", "").isupper() and line.upper() != tu:
                    # allow exact title-case alone
                    if key != hk:
                        continue
                rest = line[len(title) :].lstrip(" :.-")
                if line[: len(title)].isupper() or key == hk:
                    matched = (depth, title, rest)
                    break

        if matched is None and key in heading_map and key == re.sub(r"[^a-z0-9]+", "", line.lower()):
            depth, title = heading_map[key]
            matched = (depth, title, "")

        if matched:
            flush()
            depth, title, rest = matched
            paras.append("#" * min(depth + 1, 4) + f" {title}")
            if rest:
                buf = rest
            continue

        if not buf:
            buf = line
        else:
            if line.startswith('"') or (
                buf.endswith((".", "!", "?", '"')) and re.match(r"^[A-Z\"]", line)
            ):
                flush()
                buf = line
            else:
                buf += " " + line
    flush()

    # drop leading Street Gear title duplicate
    while paras and re.sub(r"[^a-z0-9]+", "", paras[0].lower()) in {"streetgear", "1streetgear"}:
        paras = paras[1:]

    body = "\n\n".join(paras)
    # light cleanup of doubled spaces and leftover junk
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)

    md = (
        "# Street Gear\n\n"
        "Nothing to fear if you've got the gear!\n\n"
        + body
        + "\n"
    )
    # if intro already present, avoid double intro - check
    if body.lstrip().lower().startswith("nothing to fear"):
        md = "# Street Gear\n\n" + body + "\n"

    path = OUT / "21 - Street Gear.md"
    path.write_text(md, encoding="utf-8")
    print("Street Gear", path.stat().st_size, "heads", sum(1 for p in paras if p.startswith("#")))


def build_index():
    lines = join_hyphens(extract_range(472, 494))
    # Index is A-Z entries: "Topic .... page" patterns
    text = " ".join(lines)
    text = FOOTER.sub(" ", text)
    text = SIDEBAR.sub(" ", text)
    text = re.sub(r"\s+", " ", text)

    # Split roughly on patterns like "Word 123" / "Word, 123" / "Word .... 123"
    # Better: go line by line from pages and group by starting letter
    entries: list[str] = []
    buf = ""
    for line in lines:
        line = FOOTER.sub("", line).strip()
        line = SIDEBAR.sub("", line).strip()
        if not line or re.fullmatch(r"\d+", line):
            continue
        if re.match(r"^(?:SHADOWRUN|MASTER INDEX|INDEX)\b", line, re.I):
            continue
        # new entry often starts with capital letter after a page number ended previous
        if buf and re.match(r"^[A-Z]", line) and re.search(r"\d\s*$", buf):
            entries.append(buf.strip())
            buf = line
        elif not buf:
            buf = line
        else:
            buf += " " + line
    if buf:
        entries.append(buf.strip())

    # Group by first letter
    by_letter: dict[str, list[str]] = {}
    for e in entries:
        e = re.sub(r"\s+", " ", e).strip()
        if len(e) < 2:
            continue
        # strip trailing book codes noise a bit
        letter = e[0].upper()
        if not letter.isalpha():
            letter = "#"
        by_letter.setdefault(letter, []).append(e)

    parts = [
        "# Index",
        "",
        "Alphabetical index from the Core Rulebook (Master Index Edition). "
        "Entries may reference other Fifth Edition books as well as this core book.",
        "",
    ]
    for letter in sorted(by_letter.keys()):
        parts.append(f"## {letter}")
        parts.append("")
        for e in by_letter[letter]:
            # format: try to put page refs in backticks-ish plain
            parts.append(f"- {e}")
        parts.append("")

    path = OUT / "22 - Book Index.md"
    path.write_text("\n".join(parts), encoding="utf-8")
    print("Index", path.stat().st_size, "letters", len(by_letter), "entries", sum(len(v) for v in by_letter.values()))


reader = PdfReader(str(PDF))
build_street_gear()
build_index()
