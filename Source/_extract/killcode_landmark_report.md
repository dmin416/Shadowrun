# Kill Code landmark sweep

| # | File | Missing landmarks | Em | Verdict |
|---|---|---|---|---|
| 01 | 01 - Contents and Credits.md | 0 | 0 | PASS |
| 02 | 02 - Introduction.md | 0 | 0 | PASS |
| 03 | 03 - Double Decker.md | 0 | 0 | PASS |
| 04 | 04 - So You Want To Be A Hacker.md | 0 | 0 | PASS |
| 05 | 05 - Dips & Chips.md | 0 | 0 | PASS |
| 06 | 06 - Disk Jockeys & Lightstream Riders.md | 0 | 0 | PASS |
| 07 | 07 - Parallel Processing.md | 0 | 0 | PASS |
| 08 | 08 - Data Streams.md | 0 | 0 | PASS |
| 09 | 09 - In the Flow.md | 0 | 0 | PASS |
| 10 | 10 - A Million Icons Bloom.md | 0 | 0 | PASS |
| 11 | 11 - Diving Under.md | 0 | 0 | PASS |
| 12 | 12 - Infinite Realms.md | 0 | 0 | PASS |
| 13 | 13 - Null Sign.md | 0 | 0 | PASS |
| 14 | 14 - Into the Wild.md | 0 | 0 | PASS |
| 15 | 15 - The Core of Consciousness.md | 0 | 0 | PASS |
| 16 | 16 - Rule Index.md | 1 | 0 | FIX landmarks |

## Ch16 missing
- `Cyberdecks`

## Targeted spot checks
- Ch04 `Cybercombat + Logic` near Denial Of Service: OK
- Ch04 `Computer + Intuition` near Denial Of Service: OK
- Ch04 `every 10 points of Overwatch` near Patrol IC: OK
- Ch05 `Cry Wolf` near Cry Wolf: OK
- Ch06 `device rating` near Rootkit: OK
- Ch08 `LOTO` near LOTO: OK
- Ch15 `W` near Power Munger: OK
- Ch16 `aVRse` near aVRse: OK

## JackPoint structure issues
- Ch04: consecutive empty JP pairs=0; orphan/malformed=0
- Ch05: consecutive empty JP pairs=0; orphan/malformed=0
- Ch08: consecutive empty JP pairs=0; orphan/malformed=0
- Ch10: consecutive empty JP pairs=0; orphan/malformed=0
- Ch13: consecutive empty JP pairs=0; orphan/malformed=44 e.g. ['> **Glitch** (body not quoted)', '> **Puck** (body not quoted)', '> **Glitch** (body not quoted)']
- Ch14: consecutive empty JP pairs=0; orphan/malformed=0
- Ch15: consecutive empty JP pairs=0; orphan/malformed=0
