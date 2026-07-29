# Combat - Initiative

Agent reference (SR5). LLM layout; Initiative Attribute, Score, Passes, Edge, form switches.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Initiative ~p.159-161; Edge Seize/Blitz ~p.160; Delaying ~p.161
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Surprise](Surprise.md) · [Action Economy](Action%20Economy.md) · `../Edge.md` · `../Dice and Tests.md` · [Rigging](../Rigging.md) / [Matrix Basics](../Matrix%20Basics.md)

**Scope:** Score = Attr + face sum; -10 per Pass; ERIC; Seize/Blitz; delayed actions; surprise Init; astral/Matrix/rigger forms; wound mods to Init immediate
**Out of scope:** Full Interrupt list costs beyond Init (Action Economy); vehicle chase Init details (Vehicles / Rigging)

## Inventory (completeness checklist)

- [x] Score = Attr + face sum; -10 per Pass; ERIC
- [x] Seize / Blitz; delayed actions; surprise Init
- [x] Astral / Matrix AR / cold / hot / rigger Jump In Init
- [x] Wound mods to Init Attr immediate

---

## Schema

| Token | Meaning |
| --- | --- |
| Initiative Attribute | Derived rating for current form (e.g. Rea+Int) |
| Initiative Dice | Base dice for form + ware/magic/drugs/Edge Blitz |
| Initiative Score | Attribute + **sum of faces** on Init Dice (not hits) |
| Initiative Pass | Act if Score > 0; then everyone -10 |
| ERIC | Tiebreak: Edge Attr → Reaction → Intuition → Coin |

---

## Initiative Attribute Chart

| Form | Attributes | Base Init Dice |
| --- | --- | --- |
| Physical | Reaction + Intuition | 1D6 |
| Astral | Intuition × 2 | 2D6 |
| Matrix: AR | Reaction + Intuition | 1D6 |
| Matrix: cold-sim VR | Data Processing + Intuition | 3D6 |
| Matrix: hot-sim VR | Data Processing + Intuition | 4D6 |
| Rigging AR | Reaction + Intuition | 1D6 |

**Jump In:** Switching into a vehicle/drone (Complex Action) changes which Init form you use; apply Attr/Dice change rules below. Full jumped-in vehicle Init: [Rigging](../Rigging.md) / Vehicles.

Extra Init Dice (ware, Increase Reflexes, drugs, etc.) stack onto the form's base per those rules (respect caps where printed).

---

## Rolling Initiative Score

```
Initiative Score = Initiative Attribute + (sum of faces on Initiative Dice)
```

| Rule | Detail |
| --- | --- |
| Not hits | Add the **numbers on the dice**, not 5s/6s-as-hits |
| Order | Highest Score acts first each Pass |
| Record | Track Scores; they drop by 10 each Pass |
| Edge Blitz | Spend Edge → roll **5D6** Init Dice this Combat Turn (`../Edge.md`) |

### Ties (ERIC)

Compare **Edge attribute** (not points), then **Reaction**, then **Intuition**. Still tied → coin toss. Or GM: simultaneous.

---

## Initiative Passes

| Step | Rule |
| --- | --- |
| 1 | Everyone with Score **> 0** gets an Action Phase this Pass (high→low) |
| 2 | After all such Phases: every combatant's Score **-10** |
| 3 | Anyone still **> 0** → another Pass |
| 4 | All ≤ 0 → new Combat Turn → re-roll Init |

| Score state | Can do |
| --- | --- |
| > 0 | Full Action Phase when your turn comes |
| ≤ 0 this Pass | **1 Free Action**; still defend vs attacks; no full Phase |

---

## Changing Initiative mid-fight

| Change | Immediate effect |
| --- | --- |
| Initiative **Attribute** changes | Apply ± difference to current **Score** |
| Init **Dice** increase | Roll the **extra** dice; add faces to Score; switch Attr if form changed |
| Init **Dice** decrease | Roll the **lost** dice; subtract faces from Score (+ Attr drop if any) |
| **Wound modifiers** | Applied to Initiative **attribute** (and thus Score) **as soon as** the wound is taken; can reorder within the Pass; does **not** grant another Phase |
| Enter mid-fight | Roll Score, then **-10 × Passes already done** this Turn |

Example: Attr 8, Score 11; implant raises Attr to 10 → Score becomes 13.

---

## Edge and Initiative

| Spend | Effect |
| --- | --- |
| **Seize the Initiative** | Act first for the **entire Combat Turn** (all Passes). Multiple Seize: those characters go first among themselves by Score. Others by normal Score. Back to normal next Turn |
| **Blitz** | 5D6 Init Dice this Combat Turn |

Full Edge rules: `../Edge.md`.

---

## Delayed Actions

| Rule | Detail |
| --- | --- |
| When declare | Step 3A of your Action Phase |
| Effect | Skip normal Phase; act later on a **lower** Score this Turn (or into a later Pass) |
| Intervene | When that Score's Phase arrives, declare insert; go **before, after, or same time** as that actor |
| Penalty | Actions taken via delay: **-1** dice pool |
| Score | Keep original Score for -10 tracking / how many Phases you get |
| End of Pass | If never act, still take the -10 |
| Act last | May go after last actor; multiple "want last" → reverse Score order (highest goes last) |
| Into next Pass | May delay to act first next Pass; still limited by own Score for number of Phases |

---

## Surprise and Initiative

| Result | Init effect |
| --- | --- |
| Fail Surprise Test (Rea+Int (3)) | **-10** to Initiative Score (at roll or immediately if mid-fight); surprised until next Action Phase |
| Surprised | No Defense Test vs attacks (Edge can buy defense; still keep the -10) |

Full: [Surprise](Surprise.md).

---

## Timed devices

| Rule | Detail |
| --- | --- |
| Default | Often resolve on the setter's Score next Turn, or GM timing if combat ended |
| PC timer | Declare interval when activated; usually on a chosen Pass / start or end of Turn |
| Ties | Timed items go **last** on tied Scores |
| Radio detonate | Use Item on your Action Phase |

---

## Coverage notes

- Init Dice sum = face total (same as Concepts / Dice and Tests).
- Rigging Jump In form details beyond AR chart: [Rigging](../Rigging.md).
- Interrupt Init costs (-5 / -10): [Action Economy](Action%20Economy.md).
