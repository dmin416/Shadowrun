# Combat - Movement

Agent reference (SR5). LLM layout; Walk / Run / Sprint per Combat Turn.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Movement ~p.161-162; Fatigue from Running ~p.172
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Melee Combat](Melee%20Combat.md) · [Ranged Combat](Ranged%20Combat.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · `../Vehicles.md`

**Scope:** Walk/Run rates; Sprint test; metatype sprint increase; running attack mods; charging; fatigue from sprint; Climbing (Gymnastics) procedure + table; Jumping (Gymnastics) procedure
**Out of scope:** Swim full Athletics procedure ([Actions Outside Combat](../Actions%20Outside%20Combat.md)); vehicle Speed (Vehicles); detailed terrain catalog

## Inventory (completeness checklist)

- [x] Walk / Run rates; Sprint test; metatype modifiers
- [x] Running attack mods; charging; terrain
- [x] Climbing procedure + Climbing Table + failures/glitches
- [x] Jumping procedure (horizontal/vertical)

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

## Climbing (Gymnastics)

Complex Action; **Gymnastics + Strength [Physical]** Test. Hits set how far you move that Action per the Climbing Table; assisted climbing (rope, harness, climbing gear) is easier but needs prep, unassisted can be done on the fly.

### Climbing Table

| Situation | Movement per test (round up) |
| --- | --- |
| Assisted climbing down (rappelling) | 20 m + 1 m per hit |
| Assisted climbing upward | 1 m per hit |
| Assisted climbing horizontally | 1 m per 2 hits |
| Assisted climbing upside down (ceiling/overhang) | 1 m per 3 hits |
| Unassisted climbing upward | 1 m per 2 hits |
| Unassisted climbing down | 1 m per hit |

| Modifier | Dice Pool |
| --- | --- |
| Assisted climbing (gear) | +2 |
| Surface: Easily climbable (chain-link fence) | +1 |
| Surface: Broken (tree, loose stone wall) | +0 |
| Surface: Flat (brick wall, side of building) | -3 |
| Surface: Sheer (metal wall, seamless stone) | -5 |
| Surface: Slippery or wet | -2 |
| Surface: Greased or gel-treated | -4 |

### Climbing failures and glitches

| Step | Rule |
| --- | --- |
| Failed climbing/rappelling test | Progress halts; make **Reaction + Strength** Test to hold on |
| Fail that hold-on test | You start to fall (~20 m per Combat Turn) |
| Next Action Phase | May attempt to arrest the fall: **Reaction + Strength -2** |
| Other climbers | GM may allow a **Reaction + Strength** Test to grab the falling character |
| With climbing gear | Belayer rolls **Free-Fall + Logic [Mental]** vs threshold = half the faller's Body (round down); faller may spend Edge on this test. Success = gear catches, character dangles. Failure = falls |
| Hits ground | [Falling and Fatigue](../Falling%20and%20Fatigue.md) (falling damage) |

### Rappelling

**Free-Fall + Body [Physical] (2)** Success Test, Simple Action. Descend 20 m per Combat Turn, +1 m per net hit beyond the threshold. Stopping requires another Free-Fall Test at the same threshold; fail = keep falling at that rate (Falling damage if you hit bottom). Taking another Simple Action the same Phase (e.g. firing a weapon) gives **-2** to both that action and the Free-Fall Test.

Climbing past fence-top wiring (barbed/concertina/electrified/monowire): [Barriers](../Barriers.md).

---

## Jumping (Gymnastics)

**Gymnastics + Agility** Test (not separately costed in Core; GMs typically fold it into the character's movement for the Action Phase, or call for a Simple Action for an isolated leap outside normal movement). Running leaps go farther than standing jumps if there's room to build up speed first.

| Jump type | Distance per hit | Maximum |
| --- | --- | --- |
| Standing horizontal | 1 m per hit | Agility x 1.5 m |
| Running horizontal (leap) | 2 m per hit | Agility x 1.5 m |
| Vertical (standing or running) | 0.5 m per hit | Height x 1.5 |

Net hits beyond the maximum don't add distance/height, just style points (GM discretion). A failed or short jump that leaves you short of the target ends the movement there (fall/gap rules per GM; [Falling and Fatigue](../Falling%20and%20Fatigue.md) if it's a drop).

---

## Terrain / special (GM)

Difficult terrain may cut move rates (half/quarter) at GM discretion. Swim: [Actions Outside Combat](../Actions%20Outside%20Combat.md) (Swimming). Vehicles: `../Vehicles.md`.

### Prone (pointer)

Drop Prone: Free (not if surprised). Stand: Simple (wounded: Body+Wil (2)). Prone mods: [Ranged](Ranged%20Combat.md) / [Melee](Melee%20Combat.md).

---

## Coverage notes

- Core Movement Table + Sprint + running mods + sprint fatigue: complete.
- Climbing Table + failures/glitches + Rappelling, and Jumping horizontal/vertical: complete above (from Skills - Using Gymnastics).
- Intercept when moving past foes: [Called Shots and Special](Called%20Shots%20and%20Special.md).
