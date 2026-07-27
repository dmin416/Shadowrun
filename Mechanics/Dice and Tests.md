# Dice and Tests

Agent reference (SR5). LLM layout; full mechanical detail. Prefer this file when resolving any dice test.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Concepts Hits/Tests/Limits ~p.44-49; Skills defaulting/specs/ratings/attr-only ~p.129-152; Knowledge thresholds; Limit formulas (chargen); Combat Opposed/graze/Init (pointers)
**Source Text:** `06 - Shadowrun Concepts.md` · `09 - Skills.md` · `11 - Combat.md` · `23 - Important Tables.md`
**See also:** `Mechanics/Edge.md` (spends, Edge-as-dice, bans) · Combat files when filled

**Scope:** pools, hits, thresholds, buy hits, glitches, limits, Success / Opposed / Extended / Teamwork, retry, rounding, defaulting, substitution, specializations, attribute-only, Knowledge thresholds, combat Opposed/graze note, Initiative = face-sum (not hits)
**Out of scope:** Full Edge spend text; combat modifier tables; skill writeups; Matrix/magic special tests beyond Limit/Edge hooks

## Inventory (completeness checklist)

**Concepts:** hits; thresholds; net hits (≥4 optional perk); buy hits; glitch / crit (more than half 1s); Success; Opposed; Extended (attrition, pause, glitch -1D6 / crit fail); Teamwork (Limit+1 / die+hit / caps / assistant glitch); inherent + gear Limits; retry -2; round up; Combat Turn ≈3s
**Skills:** specialization +2; default Attr-1; Unaware / Untrained; substitution; Composure / Judge Intentions / Lift / Carry / Memory; Knowledge Skill Table; rating ladder
**Combat overlays (must apply when fighting):** Opposed attacker vs defender; **tie = grazing hit** (not “defender wins” for contact); Defense often Reaction+Intuition **no Limit**; Accuracy as Limit on weapon attacks; Init Score = Attr + face sum (not hits)
**Edge hooks:** Push/Second Chance/Close Call/Smackdown; Reaction+Edge suppression (see Edge.md); skillsoft/spirit/group Edge (Edge.md)

## Schema

| Token | Meaning |
| --- | --- |
| Pool | Dice rolled |
| Hit | Face 5 or 6 (hits tests only) |
| Limit | Max usable hits (Skill+Attr tests) |
| Threshold | Hits needed (Success / Extended) |
| Net hits | Usable hits - requirement (or - opponent usable hits) |
| Interval | Time between Extended rolls |
| Face sum | Sum of die faces (Initiative); **not** a hits test |

---

## Procedure (hits tests)

1. Build **Pool** (Skill+Attr ± mods; or default Attr-1; or Attr / Attr+Attr; or special e.g. Reaction+Edge).
2. Note **Limit** if Skill+Attr (inherent or gear). Attr-only / dual-Attr / many combat Defense tests: **no Limit**.
3. Roll **or** buy hits (GM OK). Count hits (5-6) and 1s.
4. Usable hits = min(hits, Limit) unless Edge ignores Limit.
5. Compare to threshold or opponent usable hits.
6. Net hits = usable hits above requirement.

**Initiative is not this procedure.** See Initiative (face sum) below.

---

## Dice pool

| Rule | Detail |
| --- | --- |
| Die | d6; **ND6** = N dice |
| Standard | Skill + linked Attribute ± situational mods (wounds, visibility, tools, etc.) |
| Specialization | **+2** when that subset applies. Notation `Skill (Spec) R (+2)`. **Not** allowed on skill groups |
| Wound mods | From Physical + Stun monitors → DP (and Init Attr; see Combat) |
| Pool ≤ 0 | No roll unless **Push the Limit** adds Edge Attr dice |

### Defaulting

| Case | Result |
| --- | --- |
| No ranks, skill **can** default | Pool = Attribute **-1** |
| Cannot default (italics, Active Skill List Core p.151) | No roll; fail |
| **Unaware** (no rating; e.g. Incompetent) | Cannot default; never attempt |
| **Untrained** (rating 0) | Default OK |
| Edge while defaulting | Push OK unless GM: complete loss |

### Skill substitution (GM)

| Swap | OK? |
| --- | --- |
| Related Active → Active (penalty) | Yes |
| Active → Knowledge (penalty) | Yes |
| Knowledge → Active | **Never** |

### Skill rating ladder

| R | Level | R | Level |
| --- | --- | --- | --- |
| none | Unaware | 6 | Professional (typical chargen max) |
| 0 | Untrained | 7 | Veteran |
| 1 | Beginner | 8 | Expert |
| 2 | Novice | 9 | Exceptional |
| 3 | Competent | 10 | Elite |
| 4 | Proficient | 11 | Legendary |
| 5 | Skilled | 12-13 | Apex (13 needs Aptitude) |

---

## Hits / thresholds / net hits

| Term | Rule |
| --- | --- |
| Hit | Face **5 or 6** |
| Threshold | Hits needed |
| Net hits | Usable hits beyond need. Often raise effect (e.g. +DV). GM may grant small extra for **≥4** net hits |

### Success Test Thresholds

| Difficulty | Threshold |
| --- | --- |
| Easy | 1 |
| Average | 2 |
| Hard | 4 |
| Very Hard | 6 |
| Extreme | 8-10 |

Prefer skill-listed thresholds; else this table.

### Knowledge Skill Table (Memory recall uses this)

| Seek | Threshold |
| --- | --- |
| General Knowledge | 1 |
| Detailed Knowledge | 2 |
| Intricate Knowledge | 4 |
| Obscure Knowledge | 6+ |

---

## Buying hits

| Rule | Detail |
| --- | --- |
| Rate | **1 hit / 4 dice** in pool, round **down** |
| Scope | Entire pool buy **or** entire pool roll. No mix |
| Gate | **GM approval**. Skip if glitch would matter; GM may forbid |

---

## Glitches

| Result | Condition | Effect |
| --- | --- | --- |
| Glitch | Number of **1s** is **more than half** the dice rolled | Complication (GM). Can occur **with** success. Often worse if few hits |
| Critical glitch | Glitch **and** **0 hits** | Serious failure / disaster. Prefer scramble over instant PC death |

**Half examples:** pool 8 → need **≥5** ones (more than 4). Pool 5 → need **≥3** ones (more than 2.5). Count the dice actually rolled (incl. Edge dice if Push added them).

| Edge | Interaction |
| --- | --- |
| Close Call | Negate one glitch **or** crit→glitch. No hits created. Cannot 2× Edge to fully erase a crit |
| Second Chance | **Cannot** negate glitch/crit (glitch stands even if 1s are rerolled) |

**Guideline:** glitch = harder life, not auto job-fail; crit = plan wrecked.

---

## Limits

| Rule | Detail |
| --- | --- |
| Effect | Hits above Limit do not count |
| Apply | Pool = **Skill + Attribute** |
| Do not apply | Single Attr; two Attrs; typical Defense (Rea+Int); many resistance rolls |
| Gear Limit | Accuracy / deck attrs / Force / etc. **replaces** inherent (↑ or ↓) |
| Weapon attacks | Use weapon **Accuracy** as Limit (Unarmed / unarmed items: **Physical** Limit) |
| Ignore | Push the Limit; Teamwork Limit bumps; other printed effects |

### Inherent Limits (÷3, round **up**)

| Limit | Formula |
| --- | --- |
| Mental | [(Logic × 2) + Intuition + Willpower] / 3 |
| Physical | [(Strength × 2) + Body + Reaction] / 3 |
| Social | [(Charisma × 2) + Willpower + Essence] / 3 |

Essence loss lowers Social.

---

## Test types

Need: **type** · **pool** · **Limit?** · **threshold?**

### Success (Simple)

| | |
| --- | --- |
| Goal | Usable hits ≥ threshold |
| Notation | `Perception + Intuition [Mental] (2)` → Skill + Attr [Limit] (Threshold) |

### Opposed

| | |
| --- | --- |
| Goal | More usable hits than opponent |
| Notation | `Sneaking + Agility [Physical]` Opposed |
| Limit | Apply **before** compare |
| Threshold | None |
| General tie | Neither has more → status quo (non-combat) |
| **Combat tie** | **Grazing hit** (Core Combat): no DV from net hits, but **contact** occurs (poisons, shock gloves, touch spells, etc. still apply) |
| Combat hit | Attacker usable hits **>** defender → hit; net hits = difference. Defender **>** → miss |

Defense (typical): Reaction + Intuition ± mods, **no Limit**. Attacker: Combat Skill + Attr [Accuracy or Physical].

### Extended

| | |
| --- | --- |
| Goal | Bank usable hits to threshold |
| Notation | `Automotive Mechanic + Logic [Mental] (10, 1 hour)` |
| Per roll | Hits ≤ Limit count (unless Edge ignores Limit) |
| Attrition | After each roll: **-1 die** permanently from this Extended pool |
| Pause | Stop/resume; bank keeps |
| End | Threshold; abandon; or 0 dice |

#### Extended thresholds

| Difficulty | Threshold |
| --- | --- |
| Easy | 6 |
| Average | 12 |
| Hard | 18 |
| Very Hard | 24 |
| Extreme | 30+ |

#### Extended intervals

| Task | Interval |
| --- | --- |
| Fast | 1 Combat Turn |
| Quick | 1 minute |
| Short | 10 minutes |
| Average | 30 minutes |
| Long | 1 hour |
| Consuming | 1 day |
| Exhaustive | 1 week |
| Mammoth | 1 month |

#### Extended glitches

| Result | Effect |
| --- | --- |
| Glitch | Delay; GM may **-1D6** banked hits; bank ≤0 → fail |
| Critical glitch | Test **fails**; work lost |

### Teamwork

| Step | Rule |
| --- | --- |
| 1 | Choose **leader**; others assistants |
| 2 | Assistants roll Skill + Attr (default if allowed) |
| 3 | Each assistant with **≥1 hit**: leader Limit **+1** |
| 4 | Each assistant **hit**: leader pool **+1 die** |
| 5 | Dice added ≤ leader **skill rating** (or highest Attr if dual-Attr test) |
| 6 | Leader rolls adjusted pool |

| Assistant result | Effect |
| --- | --- |
| Glitch | That assistant grants **no** Limit +1 |
| Critical glitch | Leader gets **no** Limit adjustments from team + crit effects |

---

## Attribute-only tests

Pool = Attr or Attr+Attr. **No Limit.**

| Test | Pool | Rules |
| --- | --- | --- |
| Composure | Wil + Cha | Threshold by severity. Repeat similar threats → may stop requiring test |
| Judge Intentions | Int + Cha vs Wil + Cha | Opposed. Gut trust/intent; not permanent |
| Lifting | Str + Bod | Free **15 kg × Str**; each hit **+15 kg**. Overhead free **5 kg × Str**; each hit **+5 kg** |
| Carrying | Str + Bod (extra) | Free **Str × 10 kg**; each hit **+10 kg** (also Carrying Gear Core p.420) |
| Memory | Log + Wil | Threshold = Knowledge Skill Table. Memorize: Log+Wil; each hit = **+1 die** later Recall. Glitch = misremember; crit = false memory believed |

---

## Initiative (not a hits test)

| Field | Rule |
| --- | --- |
| Score | Initiative attribute + **sum of Initiative Dice faces** (not 5-6 hits) |
| Base Init Dice | 1D6; magic/ware/Edge Blitz can raise (max Blitz = **5D6**) |
| Order | Highest Score first; each Pass subtract 10 from Score (Combat) |
| Tiebreak **ERIC** | compare **E**dge Attr → **R**eaction → **I**ntuition → **C**oin (or act simultaneous, GM) |
| Edge on Init | Core Combat lists **Seize the Initiative** and **Blitz** only for messing with initiative. Do **not** treat Init as a Push/Second Chance hits test |

Full Pass/Delay/wound timing → Combat Initiative.

---

## Trying again

| Rule | Detail |
| --- | --- |
| Retry | Failed Success-style: cumulative **-2** DP per retry |
| Clear | Sufficient break (GM) → reset |
| Not retry | Each attack / swing / shot = new action |

---

## Rounding

Default: **round up**, unless a rule says otherwise.

---

## Time (pointer)

| Token | Value |
| --- | --- |
| Combat Turn | ≈ **3 seconds** |
| Actions | Free / Simple / Complex / Interrupt → Action Economy |

---

## Edge interaction summary

Full rules: `Mechanics/Edge.md`.

| Topic | Rule |
| --- | --- |
| Spends on tests | Push / Second Chance / Close Call; ≤1 Edge per test |
| Damage Resistance | Push works (Core example: +Edge dice + Rule of Six on Body+Armor) |
| Suppression avoid | **Reaction + Edge Attr** (full Attr even if points spent; not burned). Threshold = suppressor’s hits. Not an Edge **spend** |
| Banned Edge boosts | Skillsoft / skilljack skills; alchemy preparation trigger casting; Loss of Confidence skill; see Edge.md |
| Spirits | No own Edge; summoner may spend own Edge on spirit tests |
| Grunts | **Group Edge** = Professional Rating (shared pool) |

---

## Coverage notes

- Concepts + Skills test engine: complete.
- Combat Opposed graze + ERIC + Init face-sum: included so agents do not mis-apply hits/tie rules in combat.
- Suppression Reaction+Edge and Edge bans: summarized; full text in Edge.md.
- Build/Repair thresholds, social tables, Matrix tests: use those chapters; same dice engine.
