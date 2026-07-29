# Combat - Small Unit Tactics

Agent reference (SR5). LLM layout; SUT skill, Combat Maneuver Tests, RnG + Street Lethal maneuvers, PI-Tac.

**Src PDFs:** `Source/PDF/runandgun.pdf` · `Source/PDF/streetlethal.pdf`
**Printed:** RnG Tactics ~p.87-104; Street Lethal Lethal Arts ~p.126+
**Source Text:** `07 - Tactics and Tools.md` · `Street Lethal Condensed.md` (Lethal Arts)
**See also:** [Action Economy](Action%20Economy.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · [Surprise](Surprise.md) · [Vehicles](../Vehicles.md)

**Scope:** Small Unit Tactics Knowledge skill; Combat Maneuver Test procedure; all RnG combat maneuvers; Street Lethal SUT + MUT maneuvers; PI-Tac summary; tactical gear table
**Out of scope:** Full doctrine essays; mixed-unit command fiction; gear beyond listed tactical tools

## Inventory (completeness checklist)

- [x] SUT Knowledge skill + test procedure
- [x] All RnG combat maneuvers (11)
- [x] Street Lethal SUT maneuvers (5)
- [x] Street Lethal MUT maneuvers (7)
- [x] PI-Tac levels I-III
- [x] Tactical gear (paint grenade, rams, etc.)

---

## Schema

| Token | Meaning |
| --- | --- |
| SUT | Small Unit Tactics Knowledge skill |
| MUT | Mixed Unit Tactics Knowledge skill (multi-unit; Street Lethal) |
| Combat Maneuver Test | SUT + Intuition teamwork test; Free Action to order |
| Hits required | Threshold on combined hits to activate maneuver bonus |

---

## Small Unit Tactics (Knowledge)

| Field | Detail |
| --- | --- |
| Default | Intuition |
| Group | None |
| Specializations | Arctic, Desert, Forest, Jungle, Mountains, Urban |
| Use | Fire and maneuver; recognize enemy tactics; maneuver consequences (cover, concealment) |

---

## Combat Maneuver Test (RnG)

| Step | Rule |
| --- | --- |
| 1 | Designate leader (primary roller) |
| 2 | Leader: **Small Unit Tactics + Intuition** |
| 3 | Teammates with SUT join via teamwork; others default **Intuition - 1** |
| 4 | Leader may use **Leadership** on one member per maneuver (Core p.142) |
| 5 | Compare total hits to maneuver threshold |

| Timing | Action type |
| --- | --- |
| Order maneuver | **Free Action** (verbal) |
| Maneuver test | **Free Action** |
| Unfamiliar maneuver | Leader spends **Complex Action** instructing before test |
| Duration | Success lasts **one Combat Turn**; repeat test next turn to keep bonus |
| Initiative | All participants act **same Initiative Pass** |

| Result | Effect |
| --- | --- |
| Success | Bonuses apply immediately |
| Fail | Each participant: Defense penalty = maneuver's normal **bonus** this Initiative Pass |
| Glitch (success) | Only glitching member out of position (same penalty) |
| Critical glitch | Maneuver fails; penalties until **end of Combat Turn** |

**Counter-maneuver:** Opposed SUT vs SUT when both teams share Initiative Score; winner completes/disrupts first. Or eliminate key elements before maneuver completes.

---

## RnG combat maneuvers

| Maneuver | Hits req. | Effect |
| --- | --- | --- |
| **Bounding Overwatch** | 4 | Suppressive fire pins enemy: movers +3 Defense; pinned enemies -3 offense (leapfrog) |
| **Counter Peal** | 5 | +2 all Defense Tests (fighting retreat with overlapping suppressive fire) |
| **Crossfire** | 6 | Leader Simple: spot two positions; then team test. Attackers +3 attack (two directions) |
| **Diamond Formation** | 4 | +1 vs surprise/ambush; +2 Initiative (4-person 360° formation; scales for larger teams) |
| **Dog Pile** | varies | +1 attack per **3** leader hits (rounded down) |
| **Dynamic Entry (standard)** | 4 | Unseen breach +3 attack; known approach +1 |
| **Dynamic Entry (Chuck and Charge)** | 4 | As standard + grenade before entry (Throwing Weapons Test) |
| **Fire Shield** | see text | Artillery walk forward/back: +4 friendly maneuvering under shield; enemies -2. Glitch = scatter toward friendlies; crit glitch = friendly fire |
| **Marching Fire** | 6 | Unit advances under suppressive fire; +4 attack (SA/BF/FA firearms) |
| **Slicing the Pie** | varies | Searcher-only: Defense bonus = hits; 0 hits = fail; glitch -2 Defense; crit glitch = seen |
| **Traveling Overwatch** | 2 | +1 all Perception; overwatcher (leader) +2 Initiative if combat starts |

---

## Street Lethal - Small Unit Tactics maneuvers

Same Combat Maneuver Test procedure as RnG. May stack with SUT maneuvers when GM allows.

| Maneuver | Hits req. | Effect |
| --- | --- | --- |
| **Coordinated Effort** | 3 | Plan + hold same Init: +2 ranged; vehicle crews also +2 Piloting |
| **Indirect Fire** | 4 (5 map/optics, no wireless) | Spotter + shooter; blind-fighting for shooters becomes **-2** |
| **Paint the Target** | 4 | Spotters mark for aircraft undetected: aircraft Gunnery +2; ignore environmental mods |
| **Penetrating Fire** | 4 | Observer finds weak point; Called Shots same IP; best DV kept, add half AP (round up) of each other hitter; cap at Armor 0 |
| **Shield Walk** | 3 | Max 3 behind one shield (more shields = more capacity). Rear add shield Armor; each gains Defense = net hits on maneuver |

---

## Mixed Unit Tactics (Street Lethal)

For coordinating **multiple units** (military scale). Small runner teams use SUT; multi-unit ops use MUT.

| Field | Detail |
| --- | --- |
| Skill | **Mixed Unit Tactics** (Knowledge); default Intuition |
| Prerequisite | Small Unit Tactics + Leadership |
| Specializations | Aerial, Armored Infantry, Artillery, Naval, Mechanized Infantry, Standard Infantry |
| Test | Commander **MUT + Intuition** [Mental]; other unit leaders contribute teamwork |
| Order | Before combat = Free; in combat = Complex |
| Fail / glitch | Same pattern as SUT (defensive penalty = bonus; leader glitch = that unit only; crit glitch = fail) |
| Counter | Kill C2, jam comms, or Opposed MUT |

| Maneuver | Hits req. | Effect |
| --- | --- | --- |
| **Circle the Wagons** | 5 | 5+ vehicles/large drones. Pilot + Ground Craft vs terrain. Outsiders/hatch ops: Good Cover (+4 vs ranged/spells). Each vehicle +1 Body and +5 Armor per vehicle until broken |
| **Defensive Fire** | 4 (6 blind) | Immobile overlapping suppression. Perception to center (or thresh 6). +5 m width and +2 m height per extra FA/suppression weapon after first. Fail = no bonuses |
| **Envelop** | 6 | Surround: undetected +3 attack / -3 defense; aware +1 / -1. Follow-on Crossfire/Mass Fire/Penetrating Fire -2 thresh (glitch = friendly fire) |
| **Flank** | 4 | Primary + flank: +2 attack / -2 defense; follow-on Crossfire/Penetrating Fire -1 thresh |
| **Hammer and Anvil** | 5 | Hammers +3 Piloting; anvils +3 attack; defender -3 defense |
| **Move and Shoot: Group** | 4 | Same base speed: +2 ranged attack, +1 ranged defense |
| **Nap of the Earth: Group** | 5 avoid / 6 strike (+1 fixed-wing; -1 single aircraft) | Pilot Aircraft vs crash. Avoid: +3 ranged defense. Attack: +3 defense and +2 ranged (+4 separate gunners) |

PI-Tac bonuses apply to both SUT and MUT when subscribed.

---

## PI-Tac (Personal Integrated Tactical Network)

Plug-in to commlink, cyberdeck, or RCC. Wireless (hackable). Max subscribers = **DR x 1.5**.

All levels: GPS, universal image/audio link, team biomonitor, weapon status, Enhanced Situational Awareness.

| Model | Level | DR | Avail | Cost | Key benefits |
| --- | --- | --- | --- | --- | --- |
| Renraku Taka | I | 4 | 12R | 115,000¥ | +1 all Perception (audio/visual) |
| Novatech Tactician | II | 5 | 18R | 325,000¥ | + half DR to host FW **or** DP; trauma module; +2 Perception, +1 Sneak; leader maneuvers **Simple**; transfer 5 Init to one member; Combat Mode +1 one combat skill (switch Simple) |
| ComPac-Esprit General | III | 6 | 18F | 855,000¥ | Full DR to both FW and DP; transfer 10 Init to one or 5 to two; +3 Perception, +2 Sneak/Tracking; Combat Mode +2 one skill; limited remote vehicle/drone dogbrain (3 marks while subscribed) |

---

## Tactical gear (RnG)

| Item | Avail | Cost | Notes |
| --- | --- | --- | --- |
| Paint Grenade | 8R | 100¥ | 10 m radius; marks; defeats invisibility; +50¥ tracking dye |
| MOAS (mirror on stick) | 10 | 35¥ | 15 cm telescoping probe |
| Grenade-Cam | 16R | Cap x 1,500¥ | Cap 1-5; thrown sensor |
| Periscope Cam | 10R | Cap x 600¥ | Cap 1-3 |
| Standard battering ram | 10R | 2,000¥ | Exotic Melee (Battering Rams); (STR+2)P AP -1 |
| Fluid-Motion ram | 10R | 3,500¥ | (avg STR)+3 P; two users |
| Pneumatic ram | 18R | 10,000¥ | 16P AP -4 |
| Shock ram | 10R | 15,000¥ | (STR+2)P + 12S(e) AP -3 |
| Blast Shield | 8R | 20,000¥ | 20P AP -4 Target; Exotic Weapon Acc 4 |
| Ares PED Mark III | 10R | 2,500¥ | Armor 12 extraction bag; optional 1 h O2 |
| Ultra-Glide | 12 | 30¥/L | Gymnastics+Agility (3) per m crossed or Agility (4) to hold coated item |
| Hold-Fast spray | 12 | 50¥ | Acc -2; taser ranges; Strength (4) to break |

---

## Coverage notes

- RnG maneuver thresholds and benefits: complete.
- Street Lethal SUT + MUT additions: complete from Condensed.
- Doctrine/team-building prose: source chapter only; not reproduced here.
