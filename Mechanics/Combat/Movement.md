# Combat - Movement

Agent reference (SR5). LLM layout; Walk / Run / Sprint per Combat Turn.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Movement ~p.161-162; Fatigue from Running ~p.172
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Melee Combat](Melee%20Combat.md) · [Ranged Combat](Ranged%20Combat.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · `../Vehicles.md`

**Scope:** Walk/Run rates; Sprint test; metatype sprint increase; running attack mods; charging; fatigue from sprint
**Out of scope:** Climb/swim/jump full Athletics procedures; vehicle Speed (Vehicles); detailed terrain catalog

## Inventory (completeness checklist)

- [x] Walk / Run rates; Sprint test; metatype modifiers
- [x] Running attack mods; charging; terrain

---

## Schema

| Token | Meaning |
| --- | --- |
| Walk rate | Meters before you count as Running this Turn |
| Run rate | Max meters this Combat Turn without Sprint |
| Sprint | Complex Action; Running + Str [Physical] for extra meters |
| Combat hustle | "Running" here = jog/hustle, not all-out Sprint |

---

## Budget (per Combat Turn)

Movement is for the **whole Combat Turn** (all Passes combined), not per Pass.

| Rate | Formula (all Core metatypes) |
| --- | --- |
| Walk | Agility × **2** meters |
| Run | Agility × **4** meters |

| Rule | Detail |
| --- | --- |
| Declare | On Action Phase declare; may shorten or change direction for obstacles; cannot increase declared distance later |
| Exceed Walk | Count as **Running** for rest of Turn (even if you stop moving) |
| Running Free | Must spend a **Free Action** each Initiative Pass while considered Running |
| Cap | Cannot exceed Run rate without **Sprint** |

### Movement Table (Sprint increase)

| Metatype | Walk | Run | Sprint: meters per hit |
| --- | --- | --- | --- |
| Dwarf, Troll | Agi × 2 | Agi × 4 | **+1** m / hit |
| Elf, Human, Ork | Agi × 2 | Agi × 4 | **+2** m / hit |

---

## Sprinting

| Rule | Detail |
| --- | --- |
| Action | Complex Action |
| Test | Running + Strength [Physical] |
| Effect | Each usable hit adds Sprint Increase meters to this Turn's move budget |
| Max tests | Half Running skill per Combat Turn (round down), **minimum 1** |
| Fatigue | Consecutive Sprint Actions risk fatigue (below) |

Example: Human Agi 5 → Walk 10, Run 20. Sprint with 4 usable hits → +8 m → 28 m this Turn.

---

## Running / Sprint modifiers

| Situation | Effect |
| --- | --- |
| You are Running | -2 to all actions except the Sprint test |
| Charge into melee while Running | +2 melee attack and ignore the -2 running penalty on that melee attack (same net as Core Movement's "+4 with -2") |
| Target is Running (ranged vs them) | Attacker -2 |
| Target is Sprinting (ranged vs them) | Attacker -4 |
| Defender Running | +2 Defense ([Ranged](Ranged%20Combat.md) Defense Mods) |

Charge detail: [Melee Combat](Melee%20Combat.md).

---

## Fatigue from Running

Fatigue = Stun resisted with **Body + Willpower** (no Armor). Cannot heal while the cause continues.

| Activity | Fatigue |
| --- | --- |
| Sprint | Each consecutive Sprint Action Phase/Turn: cumulative **1S**, then 2S, 3S… |
| Running only (not Sprint) | Same ladder every **3 minutes** |

---

## Terrain / special (GM)

Difficult terrain may cut move rates (half/quarter) at GM discretion. Climb, swim, jump: Athletics / Strength tests (Skills chapter). Vehicles: `../Vehicles.md`.

### Prone (pointer)

Drop Prone: Free (not if surprised). Stand: Simple (wounded: Body+Wil (2)). Prone mods: [Ranged](Ranged%20Combat.md) / [Melee](Melee%20Combat.md).

---

## Coverage notes

- Core Movement Table + Sprint + running mods + sprint fatigue: complete.
- Intercept when moving past foes: [Called Shots and Special](Called%20Shots%20and%20Special.md).
