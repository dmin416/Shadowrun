# Edge

Agent reference (SR5). LLM layout; full mechanical detail. Prefer this file for all Edge spends, burns, Edge-as-dice, and Edge bans.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `Source/PDF/runandgun.pdf`
**Printed:** Concepts Edge ~p.56-57; Combat Init Edge ~p.160-161; Suppression Reaction+Edge ~p.179; RnG Combat Edge ~p.125-126
**Source Text:** `06 - Shadowrun Concepts.md` · `11 - Combat.md` · `08 - Killshots and More.md` · `17 - Magic.md` · `20 - Helps and Hindrances.md` · `21 - Street Gear.md` · `08 - Creating A Shadowrunner.md`
**See also:** `Mechanics/Dice and Tests.md` · [Called Shots and Special](Combat/Called%20Shots%20and%20Special.md) · [Martial Arts](Combat/Martial%20Arts.md)

**Scope:** Core spends/burns + RnG Combat Edge; Init Edge; Reaction+Edge; spirits; Group Edge; bans; chargen pointers
**Out of scope:** Full suppression zone geometry (Combat); quality full text (Lucky/Bad Luck/Insomnia/Loss of Confidence)

## Inventory (completeness checklist)

**Spends (6):** Push the Limit; Second Chance; Seize the Initiative; Blitz; Close Call; Dead Man’s Trigger  
**Burn (2):** Smackdown; Not Dead Yet  
**RnG Combat (5):** Lucky Move; Miracle Shot; Lucky Duck; Sixth Sense; Lucky Cover  
**Meta:** ≤1 point/test; own actions only; Extended per-roll; rest +1; GM +1; cap = Attr  
**Edge-as-dice (not a spend):** Reaction + Edge (suppression; vehicle escape); ERIC uses Edge Attr  
**Other actors:** spirits (summoner spends); grunts (Group Edge = Prof Rating); lieutenants share Group Edge  
**Bans:** skillsoft; skilljack; alchemy prep trigger; Loss of Confidence skill; Bad Luck inversion (quality)

## Schema

| Field | Meaning |
| --- | --- |
| Cost | Points spent (temp) or Attr burned (permanent) |
| Timing | When declare |
| Effect | Mechanical result |
| Limit / Ro6 | Limit ignore? Rule of Six? |

---

## Attribute vs points

| Term | Rule |
| --- | --- |
| Edge **attribute** | Permanent rating / max. Unchanged by spending points. Drops only if **burned**. Used as dice in Reaction+Edge and ERIC |
| Edge **points** | Spendable luck. Cap = Attr. Spent = unavailable until refresh |
| Minimum | Every PC has Edge (metatype starting value ≥1 typical; humans start higher). Concepts: every character has at least one point of Edge available to build |

### Hard constraints (spends)

| Constraint | Rule |
| --- | --- |
| Whose | **Own** actions only; never spend for another PC/NPC (exception: **summoned/bound spirits**, below) |
| Per test/action | **≤ 1** Edge point |
| Extended | 1 Edge allowed on **each** roll if points remain |
| Stack block | If Edge already on a test (e.g. Push), **cannot** Close Call that same test |
| Burned Attr | Burned points are gone from Attr; not usable in Reaction+Edge either |

---

## Spend effects (1 Edge point each)

### Push the Limit

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Timing | Before **or** after the roll |
| Dice | Add **Edge attribute** dice |
| Pool ≤0 | Enables the test |
| Limit | **Ignore** for this test |
| Rule of Six | Yes (6 = hit, reroll, keep exploding) |
| Ro6 scope | Before → whole pool. After → **only** added Edge dice |
| Works on | Hits tests including Damage Resistance (Core example: Body+Armor + Push) |

### Second Chance

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Timing | After a hits-test roll |
| Effect | Reroll all non-hits (faces 1-4); keep hits |
| Glitch | **Cannot** negate glitch/crit |
| Rule of Six | No |
| Limit | Unchanged |

### Seize the Initiative

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Timing | Combat initiative |
| Effect | Top of order for **entire current Combat Turn** (all Passes you have), ignoring Score |
| Multiple | Seize users first among themselves by Initiative Score, then others |
| Next Turn | Return to normal place |

### Blitz

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Timing | When rolling Initiative for a Combat Turn |
| Effect | Use **maximum 5 Initiative Dice** this Turn |

### Close Call

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Timing | On glitch/crit (no Edge already on that test) |
| Choose | Negate **one glitch** **or** crit → glitch |
| Hits | Does not create hits |
| Forbidden | Cannot spend **two** Edge to fully erase a crit |

### Dead Man’s Trigger

| Field | Detail |
| --- | --- |
| Cost | 1 point |
| Trigger | About to fall **unconscious or die** |
| Test | **Body + Willpower (3)** |
| Success | Use any **remaining actions** for **one** single action, then black out |
| Fail | No last gasp |

---

## Combat Edge (Run & Gun)

Additional spends from Killshots chapter. Same hard cap: **≤ 1 Edge point per test/action** unless noted. Own actions only except **Lucky Duck**.

| Option | Cost | Timing | Effect |
| --- | --- | --- | --- |
| **Lucky Move** | 1 point | During combat | Use **one** Martial Arts technique untrained (clumsy but effective). Trained artists may use a technique they lack. **Once per Combat Turn** |
| **Miracle Shot** | 1 point | Called Shot attack | Remove **4** points of Called Shot penalties (Core -4 becomes 0; location shots easier) |
| **Lucky Duck** | **2** points | After attack declared on teammate | Teammate in sight/commlink range: attack **misses**. Spend **your** Edge for **their** defense |
| **Sixth Sense** | 1 point | When unaware | Get a Defense Test despite being caught unaware (mirror glimpse, lucky trip, etc.) |
| **Lucky Cover** | 1 point | Suppressive fire | Find fortunate cover (even during Enhanced or Flechette suppression); may skip Reaction+Edge or gain cover Defense bonus |

**Protecting the Principle** (Interrupt -5 Init, **1 Edge**): move up to 2 m to intercept attack on ally; no Defense Test, only Body + Armor Resistance. Once per Combat Turn. See [Action Economy](Combat/Action%20Economy.md).

---

## Rule of Six

| Applies | Does not |
| --- | --- |
| Push the Limit only | Second Chance; Seize; Blitz; Close Call; Dead Man’s Trigger; burns |

---

## Initiative Edge (Combat p.160-161)

Core lists these for “mess with initiative”:

| Spend | Role |
| --- | --- |
| Seize the Initiative | Order override (above) |
| Blitz | Max 5 Init Dice (above) |

Initiative Score = Initiative Attr + **face sum** of Init Dice (not hits). Do not apply Push/Second Chance to Initiative unless a later rule explicitly allows it.

### ERIC (Init Score ties)

Compare in order: **E**dge attribute → **R**eaction → **I**ntuition → **C**oin toss. Higher goes first. Or simultaneous (GM).

---

## Edge as dice (not spending points)

### Suppressive fire avoidance

| Field | Detail |
| --- | --- |
| Pool | **Reaction + Edge** (+ Full Defense dice if used) |
| Edge dice | Use **full Edge attribute**, even if Edge **points** were spent this session. Do **not** include burned Attr |
| Threshold | Hits scored by suppressor’s (Weapon Skill)+Agility [Accuracy] test |
| Fail | Hit; take weapon **base DV** (± special ammo). Not net-hit DV from the suppress roll |
| Safe | Full cover or prone (Free Action go prone skips the test; Hit the Dirt interrupt if Free already spent) |
| Multi-zone | Test vs each overlapping suppress; after each roll **-1** DP (multi-attacker diminish) |
| Vehicle | Driver may Reaction+Edge to exit zone with whole vehicle; passengers/cover rules in Combat |

Full zone geometry / DP penalty while adjacent: Combat.

---

## Regaining Edge points

Refresh points only. Never above Attr.

| Source | Gain | Notes |
| --- | --- | --- |
| Rest | +1 | Fulfilling meal + **≥8 hours** sleep |
| GM award | +1 | Inventive/entertaining play |

### GM award prompts (Core)

Good roleplaying; heroic self-sacrifice; important personal goals; endure crit glitch **without** Close Call (sparingly); succeed important objective; brave/smart; push story; right skills/time/place; humor/drama.

### Refresh blockers (qualities; summary)

| Quality | Effect on refresh |
| --- | --- |
| Insomnia (failed check) | May block rest refresh (10K: up to +24h; 15K: wait 24h). See quality text |
| Bad Luck | Does not block refresh; warps spends (below) |

---

## Burning Edge (permanent)

| Field | Detail |
| --- | --- |
| Cost | Permanently **-1 Edge attribute** |
| Recover | Raise Attr later with Karma (**new rating × 5**; Edge has **no time** requirement to raise) |
| Broke | May burn with **0 points** left |

### Smackdown

| Field | Detail |
| --- | --- |
| Cost | Burn 1 Attr |
| Effect | Auto-succeed with **4 net hits** |
| Capable | Must be able to perform action. Core prose: no Automotive Mechanic without ranks. Core example: Automatics OK via **default**. **Use:** defaultable without ranks = capable; non-defaultable without ranks = not |
| Limit | Ignored; still 4 net hits |
| Attack example | No Accuracy check; no Defense roll; 4 net hits → modify DV; target still Damage Resistance |

### Not Dead Yet

| Field | Detail |
| --- | --- |
| Cost | Burn 1 Attr |
| Trigger | Otherwise certain death |
| Effect | Survive; thin pulse for stabilize/heal |
| Still happens | Lethal event still occurs |
| Details | GM |

---

## Other characters’ Edge

### Spirits (Magic)

| Rule | Detail |
| --- | --- |
| Spirit Edge | Summoned/bound spirits: **no** (usable) Edge pool |
| Summoner | May spend **own** Edge on the spirit’s tests |

### Alchemy preparations

Triggered preparation spellcasting: **no Edge** may be spent on that casting (Drain already paid by alchemist).

### Grunts / Group Edge (Helps & Hindrances)

| Rule | Detail |
| --- | --- |
| Individual Edge | Grunts have **none** |
| Group Edge | Shared pool = team **Professional Rating** (0-6 typical) |
| Spend | GM spends 1 Group Edge for **any** grunt on the team |
| Use | Critical to their goals only (guideline) |
| Refresh | GM; not more often than PCs |
| Adjust | GM may raise if recurring foes |
| Lieutenant | Also uses Group Edge (no personal). Own Init. Same Init as team → LT goes first |
| Leadership | LT may raise group Prof Rating **+1** (also **+1** Group Edge) via Leadership |

Professional Rating bands: 0 untrained; 1-2 semi; 3-4 trained; 5-6 elite (break/morale guidelines in Helps).

---

## Edge bans / warped spends

| Source | Rule |
| --- | --- |
| Skillsoft | Tests using skillsoft rating: **no Edge in any way** |
| Skilljack | Skills running through skilljack: **can’t use Edge** |
| Loss of Confidence | No Edge on tests with the affected skill |
| Bad Luck (quality) | On Edge spend, roll 1D6; on **1**, Edge spent but effect **inverts** (Push loses dice; Blitz → +0D6 / Attr only; Seize → go last; Close Call negate glitch → crit). Only **once** per session |
| Lucky (quality) | Allows Edge Attr **+1** above metatype max (does not auto-raise; still pay Karma). Not Exceptional Attribute |
| Exceptional Attribute | **Cannot** raise Edge (use Lucky) |

---

## Lookup: situation → Edge

| Need | Use |
| --- | --- |
| More dice / pool ≤0 / Limit choking / big resist | Push the Limit |
| Improve misses on a hits roll | Second Chance |
| Act first this Turn | Seize the Initiative |
| Max Init Dice | Blitz |
| Glitch / crit just happened | Close Call |
| One action before KO/death | Dead Man’s Trigger |
| Guaranteed 4 net hits | Burn Smackdown |
| Avoid certain death | Burn Not Dead Yet |
| Avoid bullets in suppress zone | Reaction + Edge (Attr as dice; not a spend) |
| Spirit needs luck | Spend **your** Edge on spirit’s test |
| Grunt needs luck | Spend Group Edge |
| Untrained MA technique once/turn | Lucky Move |
| Remove 4 Called Shot penalty | Miracle Shot |
| Teammate avoids declared hit | Lucky Duck (2 Edge) |
| Defense when unaware | Sixth Sense |
| Cover under suppression | Lucky Cover |

---

## Coverage notes

- Concepts spends/regain/burn: complete.
- Combat Init Edge + ERIC + Reaction+Edge suppression: complete for agent use; zone geometry stays in Combat.
- RnG Combat Edge (Lucky Move, Miracle Shot, Lucky Duck, Sixth Sense, Lucky Cover): complete.
- Spirits, alchemy prep, skillsoft/jack, Group Edge, quality bans: complete summaries.
- Chargen starting Edge / special Attr points: Character Creation files.
