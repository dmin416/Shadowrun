# Combat - Damage Armor and Wounds

Agent reference (SR5). LLM layout; DV/AP, Condition Monitors, wounds, elementals, knockdown.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Armor/Damage ~p.168-172; Combat Sequence damage ~p.173; Knockdown ~p.194; Elementals ~p.170-172
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Initiative](Initiative.md) · `../Healing and Injuries.md` · `../Dice and Tests.md`

**Scope:** Modified DV; AP vs Armor; P vs S cutoff; Damage Resistance; overflow; wound -1/3 boxes; elemental secondaries; grazing; knockdown
**Out of scope:** Full healing/stabilization procedures (Healing); full toxin powers (Encyclopedia/Drugs); falling/fatigue depth beyond note

## Inventory (completeness checklist)

- [x] Modified DV; AP vs Armor; P vs S cutoff
- [x] Damage Resistance Body+Armor; overflow; wound -1/3 boxes
- [x] Elemental secondary effects (elec/fire/cold/acid/etc.)
- [x] Grazing hit; knockdown; deadly overflow

---

## Schema

| Token | Meaning |
| --- | --- |
| Modified DV | Weapon DV + attacker net hits |
| Modified Armor | Armor + AP (AP often negative) |
| Wound mod | -1 per 3 boxes filled (tracks stack) |
| Overflow | Extra Physical past full track; death if > Body |

---

## Armor

| Rule | Detail |
| --- | --- |
| Which rating | Highest worn Armor piece only (other full pieces = bulk only) |
| Accessories (+Armor) | Add to Armor for Resistance; total +Armor bonus capped by **Strength**; every 2 full points over Str → -1 Agi and Rea |
| Specialized | Nonconductivity, fire resistance, etc. add vs matching damage; sum of specialty ratings ≤ armor Capacity |
| AP | Applied to Armor for Resistance; if no Armor worn, positive AP (that raises Armor) does not apply |
| AP ≤ 0 Armor | No Armor dice on Resistance; still roll Body |

---

## Damage resolution (after a hit)

1. **Modified DV** = base DV + net hits
2. **Modified Armor** = Armor + AP
3. **P vs S (Step 3B):** modified DV **≥** modified Armor → **Physical**; modified DV **<** modified Armor → **Stun**. Follow Step 3B (either direction). Armor intro only describes Physical→Stun; Harder Knock forces Physical from a Stun attack. Table may choose Armor-intro-only if preferred.
4. **Resist:** Body + modified Armor (or Body only if modified Armor ≤ 0). Each hit -1 modified DV
5. If DV ≤ 0 after resist → no boxes; no elemental secondary that requires damage
6. Else mark remaining DV as boxes on the correct track

### Grazing hit

Opposed Test **tie**: **no damage** (no Condition Monitor boxes). **Contact** still occurs (toxin, shock glove, touch spell, etc. may still apply).

---

## Condition Monitors

| Track | Boxes | Typical sources |
| --- | --- | --- |
| Physical | [Body / 2] + 8 (round up) | Guns, blades, many spells, fire |
| Stun | [Willpower / 2] + 8 (round up) | Fists, gel, tasers, concussion, some Drain |

Include Body/Wil bonuses before calculating.

### Wound modifiers

| Rule | Detail |
| --- | --- |
| Rate | -1 for every **3** boxes filled (per track) |
| Stack | Physical + Stun wound mods **add**; also stack with other penalties |
| Apply to | Most tests |
| **Do not** apply to | Damage Resistance, resisting direct combat spells, toxin resistance, and similar "reduce boxes about to take" rolls |
| Initiative | Wound mod applies to Initiative **attribute** and Score **immediately** ([Initiative](Initiative.md)) |

High Pain Tolerance / Low Pain Tolerance qualities change the "every 3 boxes" rate.

---

## Exceeding the monitors

| Overflow type | Rule |
| --- | --- |
| Stun past full | Every **2** excess Stun boxes → **1** Physical box |
| Physical past full | Enter **overflow**; overflow capacity = Body (+ Will to Live, etc.) |
| Instant death | Overflow damage **> Body** (more than Body boxes of overflow) |
| Bleeding out | If overflow not filled past Body yet: +1 Physical overflow every **Body** minutes without medical help; die if overflow exceeds Body |

Prompt medical attention can save someone in overflow ([Healing and Injuries](../Healing%20and%20Injuries.md)).

---

## Knockdown

| Trigger | Effect |
| --- | --- |
| Boxes from **one** attack (after Resistance) **> Physical Limit** | Forced Drop Prone (free) |
| ≥ **10** boxes from one attack after Resistance | Always knocked down |

Gel rounds: treat Physical Limit as -2 for the knockdown comparison. Intentional melee knockdown: Called Shot ([Called Shots and Special](Called%20Shots%20and%20Special.md)).

---

## Elemental / special damage (summary)

### Acid (Physical)

| Effect | Rule |
| --- | --- |
| Hit | Armor rating -1 |
| Ongoing | If not removed/neutralized (or spell ends): each Combat Turn base DV -1 and damage again; Armor -1 again until gone or DV 0 |
| Optional | Light Smoke near target |

### Cold (Physical)

| Effect | Rule |
| --- | --- |
| Armor | Simple Armor Test on items hit; 0 hits → armor broken (repairable); glitch → irreparable; crit glitch → breaks dangerously |

### Electricity

| Effect | Rule |
| --- | --- |
| Type | Stun or Physical by source/target |
| Armor | Nonconductivity adds full rating; other conductivity GM |
| Secondary (if any damage) | -1 DP all actions and Defense (not Resistance) for 1 Combat Turn; Init Score **-5** immediate |
| Stack | DP/Init penalty amounts do not stack; duration +1 Turn per further damaging zap |
| Electronics/drones | Always Physical; if ≥1 box → secondary Matrix damage = half Physical (round down) |
| Vehicles | Take damage; no elec secondary (systems via Called Shot) |

### Fire (Physical)

| Effect | Rule |
| --- | --- |
| Catch fire? | Armor + Fire Resistance - Fire AP vs threshold = fire attack net hits |
| Burning | End of each Turn: resist DV starting **3P**; +1 DV at start of each later Turn until out/destroyed |
| Put out | Agi + Intuition; -1 fire DV per hit |
| Fire AP | Open flame -2; fire spells -Force; flame weapons -6 |

### Other

Falling, fatigue, hunger/thirst/sleep: Core Fatigue/Falling sections; Healing for recovery.

---

## Coverage notes

- Core armor/DV/wound/overflow + acid/cold/elec/fire secondaries: complete for agent use.
- Full toxin/drug secondary tables: Encyclopedia Drugs Toxins and Chemicals.
- Stabilization / First Aid: Healing and Injuries.
