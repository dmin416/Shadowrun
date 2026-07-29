# Better Than Bad

Hooding / runs with a conscience; Pretoria setting.

**PDF:** `Source/PDF/better-than-bad-pdf.pdf` (170 pages; print page ≈ PDF index for body).

Extractor: `Source/_extract/extract_better_than_bad.py` (pymupdf).
Formatter: `Source/_extract/format_better_than_bad.py`.
QA: `Source/_extract/qa_better_than_bad.py` → `better_than_bad_qa_report.md` (PASS).

Note: print page 5 holds **Credits** then **Introduction**; extract splits that page.
JackPoint is print/PDF idx 4 (outline TOC listed it as 5).

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents & Credits](01%20-%20Contents%20&%20Credits.md) | 2-3 + credits from 5 |
| 2 | [JackPoint](02%20-%20JackPoint.md) | 4 |
| 3 | [Introduction](03%20-%20Introduction.md) | 5 |
| 4 | [Friends Will Be Friends](04%20-%20Friends%20Will%20Be%20Friends.md) | 6-9 |
| 5 | [Lights in the Darkness](05%20-%20Lights%20in%20the%20Darkness.md) | 10-25 |
| 6 | [Fixer-Upper Opportunities](06%20-%20Fixer-Upper%20Opportunities.md) | 26-67 |
| 7 | [Pretoria, Hurrah](07%20-%20Pretoria,%20Hurrah.md) | 68-113 |
| 8 | [Mining For Gold](08%20-%20Mining%20For%20Gold.md) | 114-117 |
| 9 | [Jacaranda Citizens](09%20-%20Jacaranda%20Citizens.md) | 118-139 |
| 10 | [Being Less Bad](10%20-%20Being%20Less%20Bad.md) | 140-155 |
| 11 | [Building a Hooder](11%20-%20Building%20a%20Hooder.md) | 156-164 |
| 12 | [Hooder Runs](12%20-%20Hooder%20Runs.md) | 165-168 |

**Condensed (mechanics + items + one-line hooks):** [Better Than Bad Condensed](Better%20Than%20Bad%20Condensed.md)

## Pipeline status

- [x] Extract
- [x] Format
- [x] Loss-check (`better_than_bad_qa_report.md` PASS)
- [x] Done-check (INDEX links, H1s, chapter spans match print TOC)

## Residual notes

- Some gear tables and JackPoint handles remain inline in **Building a Hooder**
- **Hooder Runs** dice tables are fenced line lists, not markdown tables
- Optional deeper table polish later if Encyclopedia pulls Grey Mana / GreyWare / Blight rows
