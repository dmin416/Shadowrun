# Critter and Spirit Powers

Agent reference (SR5). LLM layout; full Core critter power catalog needed to run spirits (and other critters) in play: general power rules (Type/Action/Range/Duration, Opposed Tests, astral vs physical), every power writeup used by the 6 Core spirits, and Critter Combat basics.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Critters chapter ~p.392-410 (attributes/skills, movement, powers, weaknesses, critter combat)
**Source Text:** `Core Rulebook Condensed.md` (Critters section)
**See also:** [Magic](Magic.md) (Conjuring > Spirits (Core, 6 types) for the full stat blocks that use these powers) · [Dice and Tests](Dice%20and%20Tests.md) · [Combat/Overview](Combat/Overview.md) · [Barriers](Barriers.md) (critter powers vs mana barriers)

**Scope:** General power rules (Type M/P, Action, Range, Duration, sustaining limits, astral/physical targeting); full Core writeup of every power used by the 6 Core spirits (Air/Beasts/Earth/Fire/Man/Water): Accident, Animal Control, Astral Form, Binding, Concealment, Confusion, Elemental Attack, Energy Aura, Engulf, Enhanced Senses, Fear, Guard, Influence, Innate Spell, Materialization, Movement, Natural Weapon, Noxious Breath, Psychokinesis, Sapience, Search, Venom, Weather Control (23 powers); Allergy weakness (used by Fire/Water spirits); Critter Combat basics; power-to-spirit cross-reference table.
**Out of scope:** Powers not used by any of the 6 Core spirits (Armor, Compulsion, Corrosive Spit, Dragonspeech, Dual Natured, Essence Drain, Hardened Armor, Hardened Mystic Armor, Immunity, Infection, Mimicry, Mist Form, Mystic Armor, Paralyzing Howl, Paralyzing Touch, Petrification, Regeneration; no "Flight" power exists in Core, Flight is a movement skill); full Mundane/Paranormal critter stat blocks beyond the 6 Core spirits; Weaknesses beyond Allergy (Dietary Requirement, Essence Loss, Induced Dormancy, Reduced Senses, Uneducated, Vulnerability - none used by the 6 Core spirits).

## Inventory (completeness checklist)

- [x] General power rules: Type, Action, Range, Duration, sustaining, astral/physical matching, attribute-boost cap
- [x] All 23 Core powers used by the 6 Core spirits, each with Type/Action/Range/Duration + full mechanics
- [x] Opposed Test formulas per power
- [x] Critter Combat basics
- [x] Allergy weakness pointer (Fire/Water spirit vulnerability)
- [x] Power-to-spirit cross-reference table (base vs optional)
- [x] Links to/from Magic.md

---

## Schema

| Token | Meaning |
| --- | --- |
| M / P | Mana power (no effect on nonliving targets) / Physical power (no effect in astral space or on astral forms) |
| Auto | No action needed; always on; Duration is always "Always" |
| LOS / Touch / Self / Special | Range: Line of Sight / Touch / affects only the critter / see power text |
| Instant | Resolves immediately, may leave a lasting effect (e.g. damage) |
| Sustained | No strain/dice penalty to the critter (unlike a sustained spell); critter can sustain a number of powers (or uses) at once equal to its Magic |
| Permanent | Must be maintained a set time before the effect becomes permanent |
| Special | Duration defined in the power's own text |
| Net hits | Hits scored minus the opposing side's hits on an Opposed Test; usually drives severity/duration |

---

## General Rules

**State matching:** a power can only affect a target in the same state as the critter, astral or physical. Astral forms cannot affect physical targets and vice versa. A materialized astral critter can affect physical targets while materialized; dual-natured critters interact with both planes freely.

**Type (M/P):** Mana powers do not affect nonliving targets. Physical powers cannot be used in astral space or to affect astral forms.

**Action:** Simple or Complex per power; "Auto" means no action is needed and the power is always in effect (Duration: Always).

**Range:** LOS, Touch, or Self (critter only). Spellcasting LOS rules also apply to critter powers. Unless stated otherwise, a power affects only one target at a time.

**Duration:**
- **Instant** - resolves immediately (may still cause lasting effects like damage).
- **Sustained** - critters take no strain or dice penalty for sustaining (unlike a sustained spell), even while damaged; LOS need not be maintained once the effect takes hold; a critter can sustain a number of powers (or multiple uses of the same power) at once equal to its Magic.
- **Permanent** - must be maintained for a set time (noted in the power) before it becomes permanent.
- **Special** - defined in the individual power's text.

**Attribute boosts:** any power that boosts an attribute (its own or a target's) is capped by the normal maximum attribute boost rule (Core p.94, augmented maximum).

**Opposed Tests:** most active powers resolve as an Opposed Test between the critter's attributes (usually Magic + a second attribute) and the target's defending attributes; net hits typically set the effect's severity or duration. See each power below for its exact pool.

**Critter Combat:** critters (and spirits) fight using the same rules as characters: roll attribute + attack skill, same Attack/Defense/Damage Resistance sequence as any combatant. A critter with no skill for an action uses standard defaulting rules.

---

## Powers (Core, used by the 6 Core spirits)

#### Accident

**Type:** P **Action:** Complex
**Range:** LOS **Duration:** Instant

Causes a seemingly normal accident; the exact nature is the gamemaster's call based on what the target is doing. Opposed Test: critter's **Magic + Willpower** vs target's **Reaction + Intuition**. If the critter wins, treat it as if the target had rolled a glitch on his next test; 4+ net hits makes it a critical glitch instead. A critter can target a number of victims at once equal to its Magic.

#### Animal Control

**Type:** M **Action:** Complex
**Range:** LOS **Duration:** Sustained

Controls the behavior of an animal or group of animals, limited to behavior normal for that species (a flock of birds can't steal a car, but can attack, follow, or flee). If the target leaves the critter's line of sight, it can no longer be commanded but continues following its last order for the critter's Charisma in minutes. Controls a number of small animals (cats, rats, etc.) equal to Charisma x 5, or larger animals (wolves, lions, bears, etc.) equal to Charisma. Cannot be used on a critter that has the Sapience power.

#### Astral Form

**Type:** M **Action:** Auto
**Range:** Self **Duration:** Always

The critter exists only on the astral plane. Only astral attacks or mana spells/powers can hurt it; physical attacks/spells/powers have no effect, and it can likewise only affect dual-natured beings or those astrally projecting/perceiving. Critters with this power may manifest on the physical plane the same way an astrally projecting magician does.

#### Binding

**Type:** P **Action:** Complex
**Range:** Special **Duration:** Instant

Sticks the target to a surface it is touching (often the critter itself), via webbing, a sticky tongue, or magical force. The target may try to break free with a Complex Action: **Strength + Body** vs the critter's **Magic + Willpower**. Success escapes; failure leaves the target immobilized until its next attempt. Range depends on the critter's method: LOS (shoots webbing), Touch (sticky body), or Self (just good at sticking to things).

#### Concealment

**Type:** P **Action:** Simple
**Range:** LOS **Duration:** Sustained

Mystically hides the critter, others, or objects someone is searching for. Subtracts dice equal to the critter's Magic from any Perception Test to locate the concealed subject. Can be used at once on a number of metahuman-sized targets equal to the critter's Magic, or much smaller targets (cats, babies, rats, etc.) equal to Magic x 5. Concealed subjects can see each other if the critter allows it. Lasts until the target is spotted or the critter stops sustaining.

#### Confusion

**Type:** M **Action:** Complex
**Range:** LOS **Duration:** Sustained

Renders the target indecisive, forgetful, and befuddled. Opposed Test: critter's **Magic + Willpower** vs target's **Willpower + Logic**. Any net hits become a negative dice pool modifier on every action the target takes.

#### Elemental Attack

**Type:** P **Action:** Complex
**Range:** Special **Duration:** Instant

A damaging ranged blast of a specific element (e.g. spirits of Fire have Elemental Attack (Fire)). Attack roll: critter's **Exotic Ranged Weapon + Agility [Physical]**, range increments of (Magic) meters. DV is **(Magic x 2)P**, AP is **-(critter's Magic)**, plus the appropriate elemental damage effect (per the critter's statistics).

#### Energy Aura

**Type:** P **Action:** Auto
**Range:** Self **Duration:** Always

The critter is wreathed in damaging energy of a specific element (e.g. spirits of Fire have Energy Aura (Fire)). Adds the critter's Magic to the DV of its own melee attacks, AP **-(critter's Magic)**, with the element's damage type. Anyone who successfully melee-attacks the critter also takes a Damage Resistance Test against DV **(Magic x 2)**, AP **-(critter's Magic)**. Always on unless the critter's own description says otherwise.

#### Engulf

**Type:** P **Action:** Complex
**Range:** Touch **Duration:** Sustained

A melee attack that draws the target into the critter (or terrain it controls). On a hit, inflicts damage equal to **Magic x 2** (+ net hits), resisted with **Body + Armor**, AP **-(critter's Magic)**, and the target becomes engulfed (trapped, cannot move). On each of the target's later Action Phases while engulfed, the critter automatically inflicts the same damage again (target resists each time); the target may instead spend a Complex Action to escape via Opposed Test: **Strength + Body** vs critter's **Magic + Body**. Winning ends the engulf with no further damage.

Elemental secondary effects:
- **Air Engulf:** victim resists as Stun from an inhalation-vector toxin; armor doesn't help (other protective gear might); Stun overflow becomes Physical if the victim is knocked out.
- **Earth Engulf:** victim resists Physical damage.
- **Fire Engulf:** victim resists Fire damage.
- **Water Engulf:** victim resists Stun damage; Stun overflow becomes Physical if the victim is knocked out.

#### Enhanced Senses

**Type:** P **Action:** Auto
**Range:** Self **Duration:** Always

Grants one or more improved/augmented senses beyond normal human range (low-light vision, thermographic vision, improved hearing/smell, sonar, heat sensing, etc.), as specified in the critter's own description. If the enhanced sense doesn't already carry a specific effect (thermographic vision, for instance), it grants a **+2 dice pool** modifier and **+1 limit** to tests made using that sense.

#### Fear

**Type:** M **Action:** Complex
**Range:** LOS **Duration:** Special

Fills the victim with overwhelming terror; the victim flees until safely away and out of the critter's sight. Opposed Test: critter's **Willpower + Magic** vs target's **Willpower + Logic**. Terror lasts **1 Combat Turn per net hit**. Even after the fear fades, the target must pass a **Willpower + Logic (critter's net hits)** Test to face the critter again.

#### Guard

**Type:** P **Action:** Complex
**Range:** LOS **Duration:** Sustained

Protects against normal environmental accidents/hazards (natural or from the Accident power), such as heatstroke or drowning, and can be used to prevent a glitch from occurring. Can cover a number of characters at once equal to the critter's Magic. Each accident averted or glitch prevented counts as a service if used by a spirit.

#### Influence

**Type:** M **Action:** Complex
**Range:** LOS **Duration:** Instant

Implants a suggestion in the target's mind. Opposed Test: critter's **Magic + Charisma** vs target's **Willpower + Logic**. On a critter win, the target acts on the suggestion as if it were his own idea. If later confronted with the wrongness of the suggestion, the target may make a Willpower Test to overcome it, the same way mental manipulation spells can be overcome.

#### Innate Spell

**Type:** As spell **Action:** Complex
**Range:** As spell **Duration:** As spell

Lets the critter instinctively cast a single, specific spell; the critter must have the Spellcasting skill. Innate Spells are chosen from the standard magician spell list, and magicians can oppose them with Counterspelling as normal. They produce Drain as normal and suffer the usual -2 penalty for sustaining. Critters and spirits resist Drain with either Intuition or Charisma, gamemaster's discretion.

#### Materialization

**Type:** M **Action:** Complex
**Range:** Self **Duration:** Sustained

Lets an astral critter project itself into the physical world and form a temporary "body," letting it interact with and affect physical beings; it also gains Immunity to Normal Weapons while materialized. Both materializing and dematerializing back to the astral plane require a Complex Action.

#### Movement

**Type:** P **Action:** Complex
**Range:** LOS **Duration:** Sustained

Speeds up or slows down a target's movement rate (vehicles, characters, or critters), multiplying or dividing it by up to the critter's Magic attribute. Used on a target other than the critter itself, it only functions within terrain the critter controls; used on the critter alone, it works anywhere. Only one instance of this power may apply to a given target at a time; it ends once the target leaves the critter's terrain/domain.

**Vehicles:** critter makes a **Magic + Willpower** Test with a threshold of half the vehicle's Body (round up, minimum 2). If met, multiply the hits by the vehicle's Acceleration Rating and add/subtract the result to the vehicle's Speed next Combat Turn (as an Acceleration/Deceleration Test); the critter can keep testing each Turn it sustains the power while the vehicle stays in its domain. Sudden speed changes may call for a Crash Test.

#### Natural Weapon

**Type:** P **Action:** Auto
**Range:** Touch **Duration:** Instant

Claws, teeth, a spiked tail, or similar; the critter's description gives the attack's exact form plus its Damage Value and AP. Natural weapons can be melee or ranged and follow standard combat rules; critters use Unarmed Combat for melee natural weapons and Exotic Ranged Weapon for ranged ones. Most natural weapons count as normal weapons for Immunity to Normal Weapons purposes unless the critter's description says otherwise. A dual-natured critter with a melee Natural Weapon can use it against astral targets within reach (normal Unarmed Combat skill + physical DV); ranged natural weapons don't work on the astral plane. Critters without this power can still make an unarmed attack at DV **(STR)S**.

#### Noxious Breath

**Type:** P **Action:** Complex
**Range:** Special **Duration:** Instant

Incapacitates targets with toxic breath. Treated as a ranged attack: **Exotic Ranged Weapon + Agility [Physical]**. Damage is an inhalation-vector toxin attack (Speed: Immediate, Power: critter's Magic, Effect: Stun damage plus nausea). Armor is useless; respiratory protection helps. The blast is a cone out to (Body) meters and can catch up to two targets within one meter of each other.

#### Psychokinesis

**Type:** P **Action:** Complex
**Range:** LOS **Duration:** Sustained

Moves an object with the critter's mind, similar to the Magic Fingers spell; acts as a magical "hand" with Strength and Agility equal to the hits scored on a **Magic + Willpower** Test.

#### Sapience

**Type:** P **Action:** Auto
**Range:** Self **Duration:** Always

The critter is self-aware, capable of choice, and generally at or above the intelligence level of *Homo sapiens*. Sapient critters are treated as Untrained (rather than Unaware) for skills they don't possess, so they can default normally, and are capable of learning new skills. Most sapient critters are mundane but can Awaken and gain a Magic attribute, following normal rules for magic.

#### Search

**Type:** P **Action:** Complex
**Range:** Special **Duration:** Special

To find a target, the critter makes a **Magic + Intuition (5, 10 minutes)** Extended Test; it must have seen the target at some prior time (spirits may search for anything their summoner can provide a mental image of). Critters that can enter astral space may use this power there without materializing, even if the target is physical.

**Search Modifiers:**

| Situation | Modifier |
| --- | --- |
| Target is more than 1 kilometer away | +1 threshold per kilometer |
| Target is a nonliving object or place | +5 threshold |
| Target hidden by a Concealment power | -concealer's Magic (dice pool) |
| Target hidden behind a mana barrier | -barrier Force (dice pool) |

#### Venom

**Type:** P **Action:** Auto
**Range:** Touch **Duration:** Instant

Secretes a dangerous toxin. Typical attributes: Vector Injection, Speed 1 Combat Turn, Penetration 0, Power = critter's Magic, Effect Physical damage. Some critters have venom with different attributes; noted in their own description.

#### Weather Control

**Type:** P **Action:** Complex
**Range:** LOS **Duration:** Sustained

Manipulates local weather within realistic bounds for the environment (no snowstorms in equatorial Africa). Builds up over a **Magic + Willpower (10, 30 minutes)** Extended Test, peaking on completion. The critter doesn't directly control the weather it summons, only pushes it in a desired direction (e.g. it can summon a thunderstorm but can't aim its lightning bolts).

---

## Weaknesses (used by Core spirits)

#### Allergy

Treated as the Allergy Negative quality (see [Character Creation/Qualities](Character%20Creation/Qualities.md)). Among the 6 Core spirits: spirits of Fire have Allergy (Water, Severe); spirits of Water have Allergy (Fire, Severe).

---

## Power-to-Spirit Cross-Reference (Core, 6 types)

Base = comes with the spirit automatically. Optional = counts against the spirit's optional-power slots (1 per 3 full points of Force, fixed at summoning). Full stat blocks: [Magic](Magic.md#spirits-core-6-types).

| Power | Air | Beasts | Earth | Fire | Man | Water |
| --- | --- | --- | --- | --- | --- | --- |
| Accident | Base | | | Base | Base | Optional |
| Animal Control | | Base | | | | |
| Astral Form | Base | Base | Base | Base | Base | Base |
| Binding | | | Base | | | Optional |
| Concealment | Base | Optional | Optional | | Base | Base |
| Confusion | Base | Optional | Optional | Base | Base | Base |
| Elemental Attack | Optional | | Optional | Base | | Optional |
| Energy Aura | Optional | | | Base | | Optional |
| Engulf | Base | | Optional | Base | | Base |
| Enhanced Senses | | Base | | | Base | |
| Fear | Optional | Base | Optional | Optional | Optional | |
| Guard | Optional | Optional | Base | Optional | Base | Optional |
| Influence | | | | | Base | |
| Innate Spell | | | | | Optional | |
| Materialization | Base | Base | Base | Base | Base | Base |
| Movement | Base | Base | Base | | Optional | Base |
| Natural Weapon | | Optional | | | | |
| Noxious Breath | Optional | Optional | | Optional | | |
| Psychokinesis | Optional | | | | Optional | |
| Sapience | Base | Base | Base | Base | Base | Base |
| Search | Base | Optional | Base | Optional | Base | Base |
| Venom | | Optional | | | | |
| Weather Control | | | | | | Optional |

---

## Quick cheat sheet

| Power | Opposed Test (critter side vs target side) |
| --- | --- |
| Accident | Magic + Willpower vs Reaction + Intuition |
| Animal Control | No test (behavior control within limits) |
| Binding (escape) | Target's Strength + Body vs Magic + Willpower |
| Concealment | Passive dice penalty (Magic) to target's Perception |
| Confusion | Magic + Willpower vs Willpower + Logic |
| Elemental Attack | Exotic Ranged Weapon + Agility [Physical] attack roll |
| Energy Aura (return damage) | Attacker resists DV (Magic x 2), AP -(Magic) |
| Engulf (attack) | Melee attack roll; target resists Body + Armor |
| Engulf (escape) | Target's Strength + Body vs Magic + Body |
| Fear | Willpower + Magic vs Willpower + Logic |
| Influence | Magic + Charisma vs Willpower + Logic |
| Movement (vehicle) | Magic + Willpower vs threshold (half vehicle Body, round up, min 2) |
| Psychokinesis | Magic + Willpower (hits = effective Strength/Agility) |
| Search | Magic + Intuition (5, 10 minutes) Extended Test |
| Weather Control | Magic + Willpower (10, 30 minutes) Extended Test |

---

## See also

[Magic](Magic.md) - full spirit stat blocks (Conjuring > Spirits (Core, 6 types)), summoning/binding/banishing, services, spirit combat basics. [Barriers](Barriers.md) - how mana barriers interact with always-on critter powers.
