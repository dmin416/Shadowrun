# Character Creation - Life Modules

Agent reference (SR5). LLM layout; Run Faster Life Module character generation.

**Src PDFs:** `Source/PDF/runfaster.pdf`
**Printed:** Construction Kits ~p.63-88
**Source Text:** `08 - Construction Kits.md`
**See also:** [Priority System](Priority%20System.md) · [Overview](Overview.md) · [Attributes](Attributes.md) · [Skills](Skills.md) · [Qualities](Qualities.md) · [Finishing Touches](Finishing%20Touches.md)

**Scope:** Life Module method (750 Karma start); nationality/region; all module phases with costs; finishing rules; metatype costs; magical type Karma costs
**Out of scope:** Extended metatype attribute tables (Metatype.md); every discipline skill line (see source for full skill bundles)

## Inventory (completeness checklist)

- [x] 750 Karma pool + module deduction flow
- [x] Active skill cap 7 / Knowledge cap 9
- [x] Metatype Cost Table
- [x] Magical/Resonance quality costs
- [x] All nationalities + regions (15 Karma)
- [x] Formative Years (40 Karma each)
- [x] Teen Years (50 Karma each)
- [x] Further Education (40-115 Karma)
- [x] Real Life (100 Karma; multi-select)
- [x] Tours of Duty + finishing Karma balance

---

## Schema

| Token | Meaning |
| --- | --- |
| Module | Background package; Karma cost buys attrs, skills, qualities |
| Phase order | Nationality → Formative (age 10) → Teen (17) → Further Ed **or** skip → Real Life (4 years each) |
| Quality Karma in module | Denotes quality **level**, not extra cost to character |

---

## Method overview

| Rule | Detail |
| --- | --- |
| Starting Karma | **750** (lower than Point Buy due to module benefits) |
| First step | Buy metatype (Metatype Cost Table); set attrs to racial minimums |
| Nationality + region | **15** Karma; pick nation then region/demographic |
| Modules | Each deducts listed Karma; grants attrs, skills, qualities per module text |
| Active skills | **Max 7** during modules; excess ranks lost |
| Knowledge skills | **Max 9** |
| Skill groups | If prior picks split group ranks, add +1 to each skill in group when a group module is taken |
| Magic / Resonance | **Not** in modules; buy Adept/Magician/etc. at Point Buy costs (below) when desired |
| Freebies | Same free Knowledge/Language + Contacts as Priority (Overview p.89, p.98) |
| Finish | Spend remaining Karma on attrs/skills/qualities/contacts/gear (Karma→¥ max **235** at 1 Karma = 2,000¥) |
| Leftover Karma | Use or lose at chargen |
| Carryover ¥ | Max **5,000**; roll starting ¥ per purchased lifestyle |
| Negative qualities | Max **25** Karma worth after all modules; may buy off negatives then add new ones |
| Duplicate quality | If same quality twice and cannot tier up, pick another of same Karma cost |
| SIN | Highest-value SIN from modules replaces lower SINs |

Advancement after creation: standard Karma rules (p.103, SR5).

---

## Metatype Cost Table (Life Modules / Point Buy)

| Metatype | Karma |
| --- | --- |
| Human | 0 |
| Elf | 40 |
| Dwarf | 50 |
| Ork | 50 |
| Troll | 90 |
| Centaur | 60 |
| Cyclops | 100 |
| Dryad | 90 |
| Fomorian | 100 |
| Giant | 90 |
| Gnome | 50 |
| Hanuman | 100 |
| Hobgoblin | 40 |
| Koborokuru | 70 |
| Menehune | 50 |
| Minotaur | 100 |
| Naga | 95 |
| Nartaki | 40 |
| Nocturna | 60 |
| Ogre | 40 |
| Oni | 50 |
| Pixie | 70 |
| Sasquatch | 90 |
| Satyr | 50 |
| Shapeshifter Bovine/Vulpine | 100 |
| Shapeshifter Canine/Falconine | 110 |
| Shapeshifter Lupine/Equine | 120 |
| Shapeshifter Pantherine/Tigrine | 150 |
| Shapeshifter Ursine/Leonine | 160 |
| Wakyambi | 70 |
| Xapiri Thëpë | 80 |

---

## Magical / Resonance types (buy separately)

| Type | Karma |
| --- | --- |
| Adept | 20 |
| Aspected Magician | 15 |
| Technomancer | 15 |
| Magician | 30 |
| Mystic Adept | 35 |

Each grants Magic or Resonance 1; raise with Karma. Adept: free PP = Magic. Mystic Adept: PP cost 5 Karma each, max = Magic.

---

## Nationality + Region (15 Karma each)

Pick **one** nationality, then **one** region/demographic within it.

### UCAS

Primary: English (N). Secondary (pick one @ 1): Spanish, German, Italian, French, Mandarin, Polish, Yiddish.  
Universal: Computer +1, Knowledge: History +1, Knowledge: UCAS +1.

| Region | Bonuses |
| --- | --- |
| General UCAS | Logic +1, Etiquette +1, Knowledge: [City] +2, Language +2, SINner (5) |
| Canada | Body +1, Navigation +1, Survival +1, Etiquette +1, SINner (5) |
| Denver (UCAS sector) | Intuition +1, Knowledge: Denver +2, Negotiation +1, Etiquette +1, SINner (5) |
| Seattle | Reaction +1, Perception +1, Intimidation +1, Knowledge: Seattle +2, SINner (5) |
| SINless | Agility +1, Knowledge: [City] +1 |

### CAS

Primary: English (N). Secondary: Spanish, German, Polish, Yiddish.  
Universal: Etiquette +1, Knowledge: History +1, Knowledge: CAS +1.

| Region | Bonuses |
| --- | --- |
| General CAS | Charisma +1, Computer +2, SINner (5) |
| Denver | Intuition +1, Knowledge: Denver +2, Negotiation +1, Computer +1, SINner (5) |
| SINless | Body +1, Knowledge: [City] +1 |

### NAN

Primary language from region list. See source for tribal language lists per nation.

| Region (summary) | Key bonuses |
| --- | --- |
| Algonkian-Manitou | Outdoor +1, Perception +1, Blades +1, Unarmed +1, Street Knowledge: [Tribe] +1, SINner (5) |
| Athabaskan Council | Body +1, Survival +1, SINner (5) |
| Pueblo Corporate Council | Electronics group +1, Etiquette +2, Professional Knowledge: Business +1, SINner (5) |
| Salish-Shidhe | Logic +1, Survival +1, SINner (5) |
| Sioux Nation | Outdoor +1, Blades +2, Street Knowledge: Sioux Culture +1, SINner (5) |
| Trans-Polar Aleut | Exotic Melee (Harpoon) +2, Perception +1, Survival +1, Professional Knowledge: Polar Critters +2, SINner (5) |
| Tsimshian Nation | Strength +1, Blades +1, Allergy Uncommon Mild (5) |
| Denver | Intuition +1, Computer +1, SINner (5) |
| Las Vegas | Perception +1, Con +2, Etiquette +1, Street Knowledge: Gambling +2, SINner (5) |
| Salt Lake City | Artisan +1, Computer +1, Etiquette +1, Negotiation +1, Perception +1, Street Knowledge: Mormons +2, SINner (5) |

### Tír Tairngire

Primary: Sperethiel (N). Secondary: English 2.  
Universal: Etiquette +1, Knowledge: History +1, Street Knowledge: Tír Tairngire +1.

| Demographic | Bonuses |
| --- | --- |
| Elves/Humans | Charisma +1, Computer +2, SINner (5) |
| Orks/Trolls/Dwarfs | Con +2, Disguise +1, Intimidation +1, Sneaking +1, Perception +1, Street Knowledge: Counterculture +2, SINner (5) |

---

## Formative Years (40 Karma each; age 10)

| Module | Attributes | Qualities | Skills (summary) |
| --- | --- | --- | --- |
| **Arcology Living** | Logic +1, Charisma +1 | Limited Corporate SIN (15) | Electronics group +2, Etiquette +2, Perception +1, Academic Knowledge: [Corporation] +3 |
| **Corp Drone** | Logic +1, Charisma +1 | - | Electronics group +2, Etiquette +2, Perception +1, Academic Knowledge: [Corporation] +3 |
| **Farm Living** | Body +1, Strength +1 | Uneducated (8), Toughness (9) | Industrial Mechanic +1, Professional Knowledge: Farming +5 |
| **Fugitive** | Reaction +1, Willpower +1, Intuition +1 | Paranoia (7), Criminal SIN (10), Bad Rep (7) | Acting group +2, Perception +1, Sneaking +1, Street Knowledge: [City] +2 |
| **Isolated Rural Upbringing** | Body +1, Strength +1 | Uncouth (14), Uneducated (8), Toughness (9) | Blades +1, Outdoors group +2, Running +1, Unarmed +1, Knowledge: Farming +2 |
| **Military Brat** | Strength +1, Reaction +1 | Uncouth (14) | Close Combat group +2, Negotiation +1, Perception +1, Professional Knowledge: Military +3, Interest: Military History +2 |
| **Orphan** | Willpower +1 | - | Computer +1, Perception +2, Sneaking +2, Survival +1, Street Knowledge: [City] +3, Professional Knowledge: Foster System +3 |
| **Rich Kid** | Charisma +1 | Trust Fund (10), Prejudiced Poor (-7) | Artisan +1, Leadership +2, Computers +2, Interest Knowledge: [Any] +3, Language +3 |
| **Street Urchin** | Body +1, Willpower +1 | Paranoia (7), Flashbacks (7), Uneducated (8), Toughness (9) | Close Combat group +2, Perception +1, Running +1, Sneaking +1, Street Knowledge: [City] +3 |
| **White Collar** | Logic +1, Charisma +1 | - | Etiquette (Professional spec), Negotiation +1, Interest Knowledge: [Any] +3, Language +3 |

---

## Teen Years (50 Karma each; age 17)

| Module | Notes |
| --- | --- |
| **Corporate Education** | Charisma +1, Logic +1; Electronics +1, Chemistry +1, Gymnastics +1; 2x Academic +1; Professional Knowledge: [Corporation] +2, [Job] +2 |
| **Farm Living** | Body +1, Intuition +1; Animal Empathy (3); Industrial Mechanics +2, Longarms +1, Pilot Ground Craft +2, Pistols +1, Professional Knowledge: Farming +1 |
| **Gang Warfare** | Body +1, Reaction +1, Willpower +1; Black Market Pipeline (10), Paranoia (7), Uneducated (8), Criminal SIN (10); Blades +2, Firearms group +1, First Aid +1, Leadership +1, Negotiation +1, Perception +1, Running +1, Sneaking +1, Survival +1, Street Knowledge: [City] +2 |
| **High School** | Charisma +1, Logic +1; Athletics +1, Computers +2, Chemistry +1, Software +2; 2x Academic +1; Language +1; Street Knowledge: [Hometown] +1 |
| **Home Tutored** | Logic +1, Willpower +1; Social Stress (8); Chemistry +1, Computers +3, Software +2; 2x Academic +3; Language +2 |
| **Isolated Rural Upbringing** | Body +1, Willpower +1; Incompetent Electronics (5); Blades +1, First Aid +1, Gymnastics +1, Longarms +1, Outdoors +1, Perception +2, Sneaking +1, Street Knowledge: Critters +2 |
| **Magical Education** | Willpower +1, Charisma +1; Corporate Limited SIN (15). Requires buying Magician/Adept/Aspected/Mystic Adept. Skill bundles by path (see source) |
| **Military School** | Body +1, Charisma +1; Military Rank (5), Code of Honor (15); Blades +1, Electronics +1, Firearms +1, First Aid +1, Leadership +1, Unarmed +1, Running +1, Swimming +1; Professional Knowledge: Military +3; Academic: Military History +3, [Any] +1; Professional Knowledge: Strategy +1 |
| **Preparatory School** | Charisma +1, Logic +1; First Impression (11); Chemistry +1, Computers +1, Etiquette +1; 2x Academic +1; Language [Any] +1. **Cannot** take if Fugitive or Isolated Rural (formative) |
| **Street Kid** | Body +1, Willpower +1; Bad Rep (7), Enemy (10); Acting +2, Clubs +1, Etiquette +1, Gymnastics +1, Intimidation +1, First Aid +1, Negotiation +1, Perception +1, Running +1, Stealth group +1, Street Knowledge: [City] +1 |

---

## Further Education (optional; then Real Life only)

Choose **Further Education** **or** go straight to **Real Life** (cannot return to Further Ed after Real Life).

| Module | Karma | Age | Notes |
| --- | --- | --- | --- |
| **Trade School / Technical College** | 40 | +2 years | Logic +1; vocation tracks (Architect, Fashion Designer, Graphic Designer, Journalist, Lawyer, Mechanic, Media Studies, Nurse, Tradesman) |
| **Community College** | 55 | +2 years | Logic +1, Willpower +1; science/arts discipline tracks (see source). May chain State College/University |
| **State University or College** | 65 | +4 years | Logic +1, Willpower +1; discipline tracks |
| **Ivy League University** | 80 | +4 years | Charisma +1, Logic +1, Willpower +1; discipline tracks |
| **Military Academy** | 115 | +4 years | Body +1, Reaction +1, Strength +1; Military Rank (20); must take Tour of Duty after |

Each discipline (Architecture, Business, Computer Science, Engineering, Law, Magic, Mathematics, Medicine, Natural Sciences, Art, History, Languages, Literature, Metahumanities, Social Sciences) grants specific skill/Knowledge bundles per source tables.

---

## Real Life (100 Karma each; 4 years; multi-select, no duplicate module)

| Module | Prerequisites / notes |
| --- | --- |
| **Bounty Hunter** | Body +1, Willpower +1, Intuition +1; combat/tracking skills |
| **Celebrity** | Charisma +1 + two other attrs; Fame (8); Con +1, Escape Artist +1, +6 flex skill points |
| **Combat Correspondent** | Charisma +1, Willpower +1; Guts (10); journalism/combat skills |
| **Corporate** | Logic +1, Intuition +1; Limited Corporate SIN (15); job tracks: Company Man, Hacker/Decker, Security Guard, Security Rigger, Wage Mage, Wage Slave |
| **Covert Operations** | Intuition +1, Willpower +1; Hawk Eye (3), Poor Link (8); spy skill package |
| **Drifter** | +1 any two separate attrs; High Pain Tolerance (7), Sense of Direction (3); street survival skills |
| **Ganger** | Body +1, Strength +1; Criminal SIN (10); gang combat skills |
| **Government Agent** | Intuition +1, Reaction +1; SINner (5); influence/pistol skills |
| **Law Enforcement** | Body +1, Reaction +1, Willpower +1; branches: Beat Cop, Cyber Crime, Cyber Division, Mage Division, Rigger, SWAT |
| **Organized Crime** | Made Man (5), Criminal SIN (10); syndicate skills |
| **Political Activist** | Charisma +1, Willpower +1; Criminal SIN (10); activist skills |
| **Postgraduate Studies** | Logic +1, Intuition +1, Charisma +1; +10 to education skills |
| **Private Investigator** | Requires prior Tour, Law Enforcement, Covert Ops, Shadow Work, Government Agent, or Corporate. In Debt (5); PI skills |
| **Regular Job** | Charisma +1, Logic +1, Willpower +1; +6 vocational skill points |
| **Shadow Work** | Body +1; roles: Face, Decker, Smuggler, Street Samurai, Weapon Specialist (each with quality/skill bundle) |
| **Street Magic** | Willpower +1; paths: Aspected Magician, Occult Investigator, Eco-Shaman, Street Mage, Street Shaman, Talismonger |
| **Terrorist** | Logic +1, Willpower +1; Criminal SIN (10); demolitions/combat |
| **Think Tank** | Willpower +1, Logic +2; Analytical Mind (5); academic skills |

### Tours of Duty (100 Karma; 5-year commitment; reserves 3 years after)

Requires Military Academy for NAN/UCAS/CAS/Tír paths where noted. **Mercenary** requires another Tour or Company Man or Shadow Work.

| Tour | Nations |
| --- | --- |
| **Tour of Duty (Mercenary)** | Branches: Air Force, Army, Engineering, Mage, Medical, Navy, Rigger, Special Forces |
| **Tour of Duty (NAN)** | SINner (5); air/army/engineer/mage/medical/navy/rigger/special branches |
| **Tour of Duty (Tír Tairngire)** | SINner (5); Air, Border Patrol, Engineering, Ghosts, Mage, Medical, Navy, Netwatch, Peacekeepers, Rigger branches |
| **Tour of Duty (UCAS, CAS, CFS)** | SINner (5); standard military branches. Medical Corps requires Nurse/Medicine Further Ed |

Rank at Tour start: Military Rank **5+** = NCO; **20+** = officer (Rank quality table p.86).

---

## Finishing Karma balance

After all modules:

1. Sum attrs/skills/qualities from modules (likely low attrs, strong skills).
2. Spend remaining Karma on attrs (Core advancement costs), skills, qualities, contacts (p.98), gear (max 235 Karma → ¥).
3. Buy off unwanted negative qualities if under 25 Karma negative cap.
4. Roll starting ¥ for lifestyle; carryover max 5,000¥.

---

## Rank quality (from Life Modules chapter)

Rank adds +1 social limit per level vs members of same organization. Military/law enforcement: also vs public under your authority.

| Karma | NCO / Beat | Officer / Management |
| --- | --- | --- |
| 5/20 | Lance Corporal / Officer / Detective | 5 Year Manager |
| 10/25 | Sergeant / Captain / Sergeant | 10 Year Area Manager |
| 15/30 | Sergeant Major / Major / Captain | 20 Year Regional Manager |

Left number = civilian rank; right = military/LE.

---

## Coverage notes

- All module names, costs, and phase rules: complete from Run Faster Construction Kits.
- Per-module full skill line items: source `08 - Construction Kits.md` when a specific bundle is needed.
- Magical Education / discipline tracks: use source tables for exact rank allocations.
