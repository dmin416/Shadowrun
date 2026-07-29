# Maximum Pursuit

Agent reference (SR5). LLM layout; Rigger 5 advanced vehicle chase rules.

**Src PDFs:** `Source/PDF/rigger5.pdf`
**Printed:** Maximum Pursuit ~Rigger 5 ch.14
**Source Text:** `Rigger 5 Condensed.md` (Maximum Pursuit section)
**See also:** [Vehicles](Vehicles.md) · [Rigging](Rigging.md) · [Combat / Action Economy](Combat/Action%20Economy.md)

**Scope:** Chase end conditions; terrain; ranges; pursuit actions; ramming DV; stunts; mixed-class modifiers
**Out of scope:** Full vehicle catalog; drone chassis stats (Encyclopedia)

## Inventory (completeness checklist)

- [x] Chase end triggers
- [x] Out of Control rule
- [x] Terrain modifier table
- [x] Chase range bands
- [x] All pursuit actions (ground, air, water, drone Swarm)
- [x] Ramming speed DV table
- [x] Stunt framework + mixed-class modifiers

---

## Schema

| Token | Meaning |
| --- | --- |
| Control Vehicle | Complex Action each Combat Turn or go Out of Control |
| Terrain | Modifier added to Vehicle Skill + Reaction [Handling] tests |
| Range band | Close / Short / Medium / Long / Extreme / Spotter |

---

## Chase framework

### End conditions

Chase ends when a vehicle:

- Escapes beyond **Extreme** range
- **Handling** reaches **0**
- **Acceleration** and **Speed** both reach **0**
- **Condition Monitor** fills

### Control each turn

Every Combat Turn: take **Control Vehicle** as **Complex Action** or become **Out of Control**:

| Out of Control | Effect |
| --- | --- |
| Occupants | -2 dice all actions next Combat Turn |
| Autopilot / GridGuide | Takes over at end of Combat Turn |
| No autopilot | Crashes eventually |

Vehicle actions = **Vehicle Skill + Reaction [Handling]** tests (usually Complex), plus Terrain and action-specific modifiers.

**Speed:** Increase up to **Acceleration** or decrease by **1** each Combat Turn.

---

## Terrain modifiers

| Terrain | Modifier | Examples |
| --- | --- | --- |
| Open | +0 | Highway, open sea |
| Light | +1 | Thoroughfare, docks, light woods, light traffic |
| Restricted | +2 | Side streets, moderate woods/traffic |
| Obstructed | +3 | Heavy traffic, riptide |
| Tight | +4 | Alleys, heavy woods, swamp |
| Impossible | +6 | Street-level city flight, hurricane waves |

---

## Range bands

| Range | Distance |
| --- | --- |
| Close | 0-2 m |
| Short | 2-10 m |
| Medium | 11-50 m |
| Long | 51-150 m |
| Extreme | 151-300 m |
| Spotter (aircraft) | 301-500 m |

---

## Pursuit actions

| Action | Range / speed | Rule |
| --- | --- | --- |
| **Bootleg Turn** | any | Terrain + target Speed; 1 net hit starts at Extreme behind; extras move closer |
| **Catch Up / Break Away** | any | Opposed: Terrain + Speed difference (or Terrain alone if fastest). Net hits shift range up to Accel. Beyond Extreme: final pursuer test; escape if still beyond |
| **Crazy Ivan** | any | Terrain reduces detection threshold |
| **Cut Off** | Short | Opposed Terrain; target avoids crash at Terrain + net hits |
| **Discreet Pursuit** | any | Terrain + range mod (Close 5, Short 3, Medium 2, Long 1, Extreme 0). Net hits raise detection threshold (max 1 + Terrain) |
| **Drive-By / Broadside** | Med/Short (optimum 2) | Terrain + Speed; net hits = Teamwork dice for passenger attacks |
| **Hold it Together** | rigger | Spend Edge each CT to operate after filled CM |
| **Zen Control** | rigger | Substitute for Control Vehicle on jumped-in craft |
| **Like a Glove** | any | Test higher terrain; success forces opponents to test it; failures +2 range and -2 Catch Up/Break Away |
| **Pickup** | Close (opt 2) | Needs entry; failure = ram result |
| **PIT Maneuver** | Short (opt 2) | Opposed Terrain; reduces Handling by net hits; 0 = pinned |
| **Ram** | Short / any | Opposed Terrain. DV by Body/Speed table + net hits. Rear: Speed difference; side: actor Speed; head-on: both speeds; rammer resists half except head-on |
| **Shake Things Up** | any | Terrain test raises follower terrain +1 within 100 m |
| **Switch the Six** | any | Opposed; target +1 die per range above Close; success swaps actor behind at Extreme, net hits move closer |
| **Clear Exit** | ground | Speed + Terrain: Simple action or Bailout |
| **Drift** | ground | +1 Catch Up/Break Away die |
| **Make a Hole** | ground | Reduces follower terrain/net hit; actor takes Body/2 + terrain damage |
| **Leaf** | aircraft | Spend Edge to reduce disabled-aircraft landing penalty |
| **Falling Leaf** | aircraft | Fixed wing stalls; range + net hits then Speed 0 |
| **Strafe** | aircraft | Net hits to vehicle weapons; bars Catch Up/Break Away |
| **Swarm** | drones Close/Short | Jumped-in controller: Terrain + drone count. Net hits Teamwork bonus later attacks; failure penalized by misses |
| **Bailout** | passenger | Simple; resist Speed x3 Stun leaving moving ground/water craft |
| **Grapple / Board** | Close | Gymnastics + Strength (Terrain); hanging requires Strength each CT |
| **Melee from vehicle** | Close | Melee gains vehicle Speed; vehicle weapon uses Body/2 as Strength + Speed |
| **Capsize** | water Close/Short | Opposed; reduces target Speed/Accel by net hits; both 0 = swamped. Land/air in deep water: target +2 dice |

---

## Ramming speed DV

| Speed | 1-2 | 3-4 | 5-6 | 7-8 | 9-10 | 11+ |
| --- | --- | --- | --- | --- | --- | --- |
| Base DV | Body/2 | Body | Body x2 | Body x3 | Body x5 | Body x10 |

---

## Stunts

Choose **Stunt rating**.

| Mode | Test |
| --- | --- |
| Alone | Complex: Vehicle Skill + Reaction [Handling] vs rating + Terrain |
| With threshold add | Rating increases action threshold |

**Failure:** immediate Vehicle Test at rating penalty or crash.

**Benefits (pick one):** rating as range-change hits; soak dice; enemy Speed/Handling reduction; attack avoidance hits; Handling for CT; dice to witnessed Social test. Custom crazy stunt costs Edge.

Across a Combat Turn: no more than **+4** dice or limit above **2x** base.

---

## Mixed classes and scale

| Rule | Detail |
| --- | --- |
| Aircraft modifiers | Use Speed x3 |
| Size terrain | Scale terrain by size difference between pursuer/pursued |
| Target size | Micro -3; Mini -2; Small -1; Body ≤8 0; Body 9-14 +1; 15-20 +2; >20 +3; +2 Body per 10 seats |
| Pedestrian vs moving vehicle | Attacker -Speed dice vs pedestrian/stationary target |
| Movement multipliers | Water x0.8; Ground x1; Rotor x3; Jet x4 |

---

## Coverage notes

- Rigger 5 Maximum Pursuit condensed rules: complete for agent chase play.
- Core vehicle combat baseline: [Vehicles](Vehicles.md).
- Drone Swarm (RCC program): [Rigging](Rigging.md).
