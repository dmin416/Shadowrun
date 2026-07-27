# Seattle Sprawl (Emerald Shadows)

District / locale guide. PDF: `Source/PDF/seattlesprawl.pdf` (90 pages).
Cover/title pages PDF idx 0-1 are image-only.

Source Texts extracted via `Source/_extract/extract_seattle_sprawl.py` (pymupdf).
Formatting: `format_seattle_sprawl_headings.py` + `format_seattle_sprawl_full.py` (paragraph reflow, JackPoint comments, At a Glance tables, subheads).

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-5 |
| 2 | [Whirlwind Tour](02%20-%20Whirlwind%20Tour.md) | 6-9 |
| 3 | [Emerald Shadows](03%20-%20Emerald%20Shadows.md) | 10-12 |
| 4 | [Downtown](04%20-%20Downtown.md) | 13-17 |
| 5 | [Bellevue](05%20-%20Bellevue.md) | 18-23 |
| 6 | [Tacoma](06%20-%20Tacoma.md) | 24-29 |
| 7 | [Everett](07%20-%20Everett.md) | 30-33 |
| 8 | [Renton](08%20-%20Renton.md) | 34-38 |
| 9 | [Auburn](09%20-%20Auburn.md) | 39-44 |
| 10 | [Snohomish](10%20-%20Snohomish.md) | 45-51 |
| 11 | [Fort Lewis](11%20-%20Fort%20Lewis.md) | 52-56 |
| 12 | [Redmond](12%20-%20Redmond.md) | 57-61 |
| 13 | [Puyallup](13%20-%20Puyallup.md) | 62-66 |
| 14 | [Council Island](14%20-%20Council%20Island.md) | 67-71 |
| 15 | [Outremer](15%20-%20Outremer.md) | 72-82 |
| 16 | [The Seattle Underground](16%20-%20The%20Seattle%20Underground.md) | 83-87 |

## District chapter pattern (typical)

Most district chapters use: At a Glance table - Special Occasions - Crime Scene - Where to Shop - Where to Squat - You Won't Find This Elsewhere - Opposition Report - Help Wanted.

Outremer (ch. 15) covers Bainbridge, Vashon, Fox, McNeil, and Anderson Islands.

## Related

- Encyclopedia INDEX: adventure/locale kit, not a core gear catalog
- Serrated Edge: Denver adventure extract (same Source Texts pipeline)

## Pipeline status

- [x] Extract (raw chapter markdown from PDF)
- [x] Format (paragraph reflow, JackPoint blockquotes, At a Glance tables, H2/H3 subheads, sidebar smash fixes)
- [x] Loss-check vs PDF (body ch. 02-16 ratio ~1.00; hyphen-joins OK; TOC names present; ch. 01 condensed TOC by design; Council Island no Help Wanted in print)
- [ ] Done-check
