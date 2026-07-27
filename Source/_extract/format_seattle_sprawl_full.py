# -*- coding: utf-8 -*-
"""Full formatting pass for Seattle Sprawl Source Texts chapters."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")
SKIP = {"01 - Contents and Credits.md", "INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"))

JUNK_LINE = re.compile(
    r"^(?:"
    r">>\s*SEATTLE SPRAWL\s*<<"
    r"|<<\s*SEATTLE SPRAWL\s*>>"
    r"|SHADOWRUN:\s*SEATTLE SPRAWL"
    r"|EMERALD\s*SHADOWS"
    r"|EMERALD$"
    r"|SHADOWS$"
    r"|THE SEATTLE\s*$"
    r"|UNDERGROUND\s*$"
    r")$",
    re.I,
)

GLANCE_START = re.compile(
    r"^(?:.*?)((?:[A-Z][A-Z /'-]+)\s+AT A GLANCE)\s*$",
    re.I,
)

EDU_END = re.compile(
    r"^(?:Advanced Degrees? and (?:Certificates|Certification)|Advanced Degree and Certification|"
    r"College Equivalency|College Degree)\s*:\s*",
    re.I,
)

SECTION_H2 = {
    "overview",
    "the shape of the city",
    "the culture",
    "special occasions",
    "crime scene",
    "where to shop",
    "where to squat",
    "you won't find this elsewhere",
    "you wont find this elsewhere",
    "opposition report",
    "help wanted",
    "gangs",
    "organized crime",
}


def clean_dashes(s: str) -> str:
    for a, b in DASHES:
        s = s.replace(a, b)
    return s


def title_case_heading(s: str) -> str:
    s = s.strip()
    if re.search(r"won't find this elsewhere", s, re.I):
        return "You Won't Find This Elsewhere"
    small = {"of", "the", "a", "an", "and", "to", "for", "in", "on", "at"}
    words = re.split(r"(\s+)", s)
    out: list[str] = []
    word_i = 0
    for w in words:
        if not w.strip():
            out.append(w)
            continue
        core = w
        if core.isupper() or (core[:1].isupper() and core[1:].islower() is False and any(c.isalpha() for c in core)):
            # normalize ALL CAPS / mixed caps titles
            tl = core.title()
            # fix McNeil etc.
            tl = re.sub(r"\bMcneil\b", "McNeil", tl)
            tl = re.sub(r"\bO'Malley\b", "O'Malley", tl, flags=re.I)
            if word_i > 0 and tl.lower() in small:
                tl = tl.lower()
            out.append(tl)
        else:
            out.append(core)
        word_i += 1
    return "".join(out)


def is_all_caps_title(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 70:
        return False
    if s.startswith("#") or s.startswith(">") or s.startswith("**"):
        return False
    if s.startswith("(") and s.endswith(")"):
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return False
    # allow digits, punctuation in titles
    if not re.match(r"^[A-Z0-9][A-Z0-9 /,'\".:&()-]*$", s):
        return False
    # skip if looks like a sentence fragment with too many lowercase (already filtered)
    return True


def join_hyphen(a: str, b: str) -> str:
    a = a.rstrip()
    b = b.lstrip()
    if a.endswith("-") and b and b[0].islower():
        return a[:-1] + b
    if a.endswith("-") and b and b[0].isalpha():
        # chaot- / ic nature OR poi- / son
        return a[:-1] + b
    if not a:
        return b
    return a + " " + b


def reflow_prose(lines: list[str]) -> str:
    if not lines:
        return ""
    paras: list[str] = []
    buf = lines[0].strip()
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        if buf.endswith("-") and s[0].isalpha():
            buf = buf[:-1] + s
            continue
        # new paragraph after sentence end when next starts capital / quote
        if re.search(r'[.!?]"?$', buf) and (s[0].isupper() or s[0] in "\"'"):
            paras.append(buf)
            buf = s
            continue
        buf = buf + " " + s
    if buf:
        paras.append(buf)
    return "\n\n".join(paras)


def parse_glance_stats(block_lines: list[str]) -> tuple[str, list[tuple[str, str]]]:
    title = "At a Glance"
    rows: list[tuple[str, str]] = []
    i = 0
    if block_lines:
        m = re.search(r"(.+?)\s+AT A GLANCE", block_lines[0], re.I)
        if m:
            title = title_case_heading(m.group(1).strip()) + " at a Glance"
            # remnant before glance on same line (e.g. poi)
            pre = block_lines[0][: m.start()]
            if pre.strip():
                # handled by caller via leftover
                pass
            i = 1
        elif "AT A GLANCE" in block_lines[0].upper():
            i = 1
    # species lines sometimes smashed: Human: 4%Dwarf: 5%
    body = "\n".join(block_lines[i:])
    body = re.sub(r"%([A-Z])", r"%\n\1", body)
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.lower().startswith("education"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            rows.append((k.strip(), v.strip()))
    return title, rows


def format_glance_md(title: str, rows: list[tuple[str, str]]) -> list[str]:
    out = ["", f"## {title}", ""]
    if not rows:
        return out
    out.append("| Stat | Value |")
    out.append("| --- | --- |")
    for k, v in rows:
        out.append(f"| {k} | {v} |")
    out.append("")
    return out


def extract_glances(text: str) -> tuple[str, list[tuple[str, list[tuple[str, str]]]]]:
    """Pull AT A GLANCE sidebars out of the body. Returns (new_text, glances)."""
    lines = text.splitlines()
    glances: list[tuple[str, list[tuple[str, str]]]] = []
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # smashed: (poiUNDERGROUND AT A GLANCE
        m = re.search(r"AT A GLANCE\s*$", line, re.I)
        if m or re.search(r"AT A GLANCE", line, re.I):
            # prefix before glance title on same line
            prefix = re.sub(r".*?AT A GLANCE\s*$", "", line, flags=re.I)
            # also handle smashed without newline: poiUNDERGROUND AT A GLANCE
            smashed = re.match(r"^(.*?)([A-Z][A-Z /'-]*AT A GLANCE)\s*$", line)
            if smashed:
                prefix = smashed.group(1)
                glance_header = smashed.group(2)
            else:
                glance_header = line[line.upper().find(line.upper().split("AT A GLANCE")[0].split()[-1] if False else 0) :]
                # simpler:
                gm = re.search(r"([A-Z][A-Z /'-]+\s+AT A GLANCE)\s*$", line)
                if gm:
                    prefix = line[: gm.start()]
                    glance_header = gm.group(1)
                else:
                    glance_header = "AT A GLANCE"
                    prefix = re.sub(r"AT A GLANCE.*$", "", line, flags=re.I)

            if prefix.strip():
                # e.g. (poi  -> keep incomplete; join later
                out.append(prefix.rstrip())

            block = [glance_header]
            i += 1
            # consume until after last education row (usually 1-2 lines after Education:)
            edu_seen = False
            edu_rows = 0
            while i < len(lines):
                L = lines[i]
                if L.strip().startswith("#"):
                    break
                if re.match(r"^##\s+", L):
                    break
                # stop if we hit clear prose after education block
                if edu_seen and edu_rows >= 1 and L.strip() and not re.match(
                    r"^(Less|High|College|Advanced|Population|Human|Elf|Dwarf|Ork|Troll|Other|Per|Corporate|Education)",
                    L.strip(),
                    re.I,
                ):
                    # likely prose resume (e.g. "son is far more...")
                    break
                if JUNK_LINE.match(L.strip()):
                    i += 1
                    continue
                if re.match(r"^THE SEATTLE$", L.strip(), re.I) or re.match(r"^UNDERGROUND$", L.strip(), re.I):
                    i += 1
                    continue
                block.append(L)
                if re.match(r"^Education\s*:?\s*$", L.strip(), re.I) or L.strip().lower().startswith("education:"):
                    edu_seen = True
                if edu_seen and re.match(
                    r"^(Less than|High School|College|Advanced)", L.strip(), re.I
                ):
                    edu_rows += 1
                    if edu_rows >= 4:
                        i += 1
                        break
                i += 1
            title, rows = parse_glance_stats(block)
            glances.append((title, rows))
            continue
        out.append(line)
        i += 1

    body = "\n".join(out)
    # fix poi- / son split (various smash forms)
    body = re.sub(r"\(poi\s*\n+\s*son\b", "(poison", body, flags=re.I)
    body = re.sub(r"\(poi\s+son\b", "(poison", body, flags=re.I)
    body = re.sub(r"\(poison\s*\n+\s*son\b", "(poison", body, flags=re.I)
    body = re.sub(r"pockets\s*\(poi\s*$", "pockets (poison", body, flags=re.M)
    # mid-word running-header smash
    body = re.sub(r"([a-z])SHADOWRUN:\s*SEATTLE SPRAWL\s*\n+", r"\1", body)
    body = re.sub(r"descrip\s*\n+##\s*Fort Lewis\s*\n+tion\b", "description", body, flags=re.I)
    body = re.sub(r"chaot-\s*\n+ic\b", "chaotic", body)
    return body, glances


def format_comments_and_prose(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    prose_buf: list[str] = []
    title_buf: list[str] = []

    def flush_prose() -> None:
        nonlocal prose_buf
        if prose_buf:
            out.append(reflow_prose(prose_buf))
            out.append("")
            prose_buf = []

    def flush_title() -> None:
        nonlocal title_buf
        if not title_buf:
            return
        flush_prose()
        joined = " ".join(t.strip() for t in title_buf)
        # COLORS / TURF lines stay with gang name
        heading = title_case_heading(joined)
        low = heading.lower()
        if low in SECTION_H2 or low.replace("'", "") in {s.replace("'", "") for s in SECTION_H2}:
            out.append(f"## {heading}")
        else:
            out.append(f"### {heading}")
        out.append("")
        title_buf = []

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()

        # preserve existing markdown headers
        if s.startswith("#"):
            flush_title()
            flush_prose()
            # normalize ### POSTED BY
            if re.match(r"^###\s*POSTED BY:", s, re.I):
                out.append(s)
            elif s.startswith("## "):
                out.append(s)
            elif s.startswith("# "):
                out.append(s)
            else:
                out.append(s)
            out.append("")
            i += 1
            continue

        if not s:
            flush_title()
            flush_prose()
            if out and out[-1] != "":
                out.append("")
            i += 1
            continue

        if JUNK_LINE.match(s):
            i += 1
            continue

        # JackPoint comment
        if s == ">":
            flush_title()
            flush_prose()
            i += 1
            comment: list[str] = []
            while i < len(lines) and lines[i].strip() != ">":
                if lines[i].strip() and not JUNK_LINE.match(lines[i].strip()):
                    comment.append(lines[i].strip())
                i += 1
            speaker = ""
            if i < len(lines) and lines[i].strip() == ">":
                i += 1
                if i < len(lines):
                    cand = lines[i].strip()
                    # speaker: short, not starting a long prose paragraph usually
                    if cand and not cand.startswith("#") and len(cand) <= 40 and not cand.endswith((".", "?", "!")):
                        # allow ! in Slamm-0!
                        speaker = cand
                        i += 1
                    elif cand and len(cand) <= 40 and re.match(r"^[\w .'\\-]+!?$", cand):
                        speaker = cand
                        i += 1
            body = reflow_prose(comment) if comment else ""
            if body:
                out.append(f"> {body}")
            if speaker:
                out.append(">")
                out.append(f"> {speaker}")
            out.append("")
            continue

        # TURF / COLORS under a gang heading
        if re.match(r"^\(COLORS:", s, re.I) or re.match(r"^TURF:", s, re.I) or re.match(r"^COLORS:", s, re.I):
            flush_title()
            flush_prose()
            out.append(f"*{s}*")
            out.append("")
            i += 1
            continue

        # ALL CAPS titles (possibly multi-line)
        if is_all_caps_title(s) and "AT A GLANCE" not in s.upper():
            flush_prose()
            # section labels like DOWNTOWN GANGS stay alone
            if re.search(r"\bGANGS$", s, re.I) or s.upper() in {
                "ORGANIZED CRIME",
                "DOWNTOWN GANGS",
                "RENTON GANGS",
            }:
                title_buf.append(s)
                flush_title()
                i += 1
                continue
            # skip false running-header leftovers mistaken as titles
            if s.upper() in {"EMERALD SHADOWS", "EMERALD", "SHADOWS", "SEATTLE SPRAWL"}:
                i += 1
                continue
            title_buf.append(s)
            i += 1
            while i < len(lines) and is_all_caps_title(lines[i].strip()) and "AT A GLANCE" not in lines[i].upper():
                nxt = lines[i].strip()
                if re.search(r"\bGANGS$", nxt, re.I) or nxt.upper() in {"EMERALD SHADOWS", "EMERALD", "SHADOWS"}:
                    break
                # don't glue gang section label to gang name
                if title_buf and re.search(r"\bGANGS$", title_buf[-1], re.I):
                    break
                title_buf.append(nxt)
                i += 1
            flush_title()
            continue

        # normal prose
        flush_title()
        prose_buf.append(s)
        i += 1

    flush_title()
    flush_prose()
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def process_file(path: Path) -> None:
    raw = clean_dashes(path.read_text(encoding="utf-8"))
    # split header
    lines = raw.splitlines()
    header: list[str] = []
    body_start = 0
    if lines and lines[0].startswith("# "):
        header.append(lines[0])
        body_start = 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1
        if body_start < len(lines) and lines[body_start].startswith("**Source:**"):
            header.append("")
            header.append(lines[body_start])
            body_start += 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1

    body = "\n".join(lines[body_start:])
    body, glances = extract_glances(body)
    body = format_comments_and_prose(body)

    # drop redundant ## SameAsH1 right after header
    h1 = header[0][2:].strip() if header else ""
    body_lines = body.splitlines()
    if (
        h1
        and body_lines
        and body_lines[0].startswith("## ")
        and body_lines[0][3:].strip().lower() == h1.lower()
    ):
        body_lines = body_lines[1:]
        while body_lines and not body_lines[0].strip():
            body_lines = body_lines[1:]
        body = "\n".join(body_lines).strip() + "\n"

    # insert glances after poster / early comments if any, else after header
    glance_md: list[str] = []
    for title, rows in glances:
        glance_md.extend(format_glance_md(title, rows))

    parts = header + [""]
    if glance_md:
        # Prefer glance after POSTED BY block if present at top
        bl = body.splitlines()
        insert_at = 0
        if bl and bl[0].startswith("### POSTED BY"):
            # skip poster + following comments until first ## or long prose paragraph that's not comment
            insert_at = 1
            while insert_at < len(bl):
                if bl[insert_at].startswith("## "):
                    break
                if bl[insert_at].startswith(">"):
                    insert_at += 1
                    continue
                if bl[insert_at].strip() == "":
                    insert_at += 1
                    continue
                # first non-comment prose: put glance before it
                break
            parts.append("\n".join(bl[:insert_at]).rstrip())
            parts.append("")
            parts.extend(glance_md)
            parts.append("\n".join(bl[insert_at:]).lstrip())
        else:
            parts.extend(glance_md)
            parts.append(body.rstrip())
    else:
        parts.append(body.rstrip())

    final = "\n".join(parts)
    final = clean_dashes(final)
    final = re.sub(r"\n{3,}", "\n\n", final).strip() + "\n"
    # fix leftover (poison without closing if needed - leave as-is from source)
    path.write_text(final, encoding="utf-8")
    print(f"formatted {path.name} ({path.stat().st_size} bytes, glances={len(glances)})")


def main() -> None:
    for path in sorted(ROOT.glob("*.md")):
        if path.name in SKIP:
            print("skip", path.name)
            continue
        process_file(path)


if __name__ == "__main__":
    main()
