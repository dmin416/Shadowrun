# Cyberdecks and Programs

Agent reference (SR5). Compact layout; full mechanical detail for cyberdecks, deck modules, common/hacking cyberprograms, agents, and related deck software.

**Src PDFs / extracts:** Core Street Gear `Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md` + Matrix `13 - The Matrix.md` - DT `Source/_extract/elec_dt.txt` - KC `Source/_extract/elec_kc.txt` - RF Decker PACKs `Source/_extract/rf_decker_packs.txt` (from Run Faster pp. 248-249).
**Books:** Core - DT (Killer Apps / Guts) - KC (Dips & Chips) - RF (Decker PACK bundles only).
**See also:** `Encyclopedia/Commlinks and Electronics.md` (commlinks, dongles, form factors, MOS, Datajack Plus, consumer softs, device mods) - `Encyclopedia/Rigger Gear.md` (RCC program copies; cannot cross-run with deck programs) - `Encyclopedia/Cyberware.md` (implanted cyberdeck wrapper) - `Encyclopedia/Tools Kits and Survival.md` (Software / Hardware kits used in RF Decker PACKs) - `Encyclopedia/Grenades and Explosives.md` (Self-Destruct module = fragmentation grenade profile) - `Mechanics/Matrix.md`.

**Out of scope:** consumer software / datasofts / shopsofts / tutorsofts (Electronics) - DT commlink apps / dongles / form-factor buy procedure (Electronics; deck form-factor deltas noted below) - MOS / booster clouds / Faceless / Trode Patch / specialty links / PI-Tac tac-apps (Electronics) - RCC cyberprograms and Swarm (Rigger) - Complex Forms / Echoes (technomancer; Mechanics / Magic-TM docs) - host IC - Matrix ammo (Ammunition).

## Inventory checklist (every buy SKU)

| Group | Count | Names |
| --- | --- | --- |
| Core decks | 9 | Erika MCD-1, Microdeck Summit, Microtrónica Azteca 200, Hermes Chariot, Novatech Navigator, Renraku Tsurugi, Sony CIY-720, Shiawase Cyber-5, Fairlight Excalibur |
| DT standard decks | 6 | Radio Shack PCD-500, Little Hornet, Microtrónica Azteca 300, Xiao MPG-1, Shiawase Cyber-4, Fairlight Paladin |
| DT specialty decks | 6 | MCT Trainee, C-K Analyst, Aztechnology Emissary, Yak Killer, Ring of Light Special, Ares Echo Unlimited |
| KC custom | 2 series | Fuchi Cyber-N, Fuchi Cyber-Ex (attribute buy tables) |
| KC security | 4 | Guard, Shield, Fortress, Great Wall |
| KC hunter | 4 | Fox, Wolf, Tiger, Shark |
| KC named | 5 | Shadow Warrior, Sublime, Destiny Blade, Defender, Kitbashed Sleeper |
| Implant wrapper | 1 | Cyberdeck (implant) |
| DT modules | 7 | Hardening, Induction Receiver, Multidimensional Coprocessor, Overwatch Mask, Program Carrier, Self-Destruct, Vectored Signal Filter |
| Agents | 1 product / 2 bands | Agent Rating 1-3; Agent Rating 4-6 |
| Core common programs | 7 | Browse, Configurator, Edit, Encryption, Signal Scrub, Toolbox, Virtual Machine |
| Core hacking programs | 19 | Armor, Baby Monitor, Biofeedback, Biofeedback Filter, Blackout, Decryption, Defuse, Demolition, Exploit, Fork, Guard, Hammer, Lockdown, Mugger, Shell, Sneak, Stealth, Track, Wrapper |
| DT common programs | 3 | Bootstrap, Search, Shredder |
| DT hacking programs | 13 | Cat's Paw, Cloudless, Crash, Detonator, Evaluate, Fly on a Wall, Hitchhiker, Nuke-from-Orbit, Paintjob, Smoke-and-Mirrors, Swerve, Tantrum, Tarball |
| KC specialty | 1 | Cry Wolf (no Avail/Cost printed) |
| RF Decker PACKs | 5 | Intro to Hacking; Basic Decker; Advanced Decker; Basic Cyberdeck Programs; Advanced Cyberdeck Programs |
| Form-factor mods | 2 | Non-standard; Weapon (deltas, not models) |

## Schema

### Decks

| Col | Meaning |
| --- | --- |
| Src | Core / DT / KC |
| DR | Device Rating |
| Array | Four numbers for Attack / Sleaze / Data Processing / Firewall. Standard decks: assign freely on boot. Specialty / security / hunter: fixed A S D F as printed |
| Prog | Concurrent program slots (any number may be stored unless Rules say otherwise) |
| Avail / Cost | Street Availability / nuyen |

### Programs / modules / agents

| Col | Meaning |
| --- | --- |
| Type | Common / Hacking / Module / Agent / Specialty |
| Avail / Cost | Street Availability / nuyen. `-` = none printed |
| Rules | Full mechanical notes |

## Common rules

### Cyberdeck basics (Core)

- Deck does all commlink functions plus Attack/Sleaze and cyberprograms. Includes illegal hot-sim module out of the box, built-in sim module, universal data connector, ~1 m retractable data cable, small status screen.
- **Device Rating** sets Matrix Condition Monitor size and other DR uses.
- **Attribute Array:** four values assigned to Attack, Sleaze, Data Processing, Firewall (ASDF).
- **Program slots:** max programs running at once. Store any number (unless a special deck limits storage).
- Commlinks have **no** space for cyberprograms (Core Matrix).

### Configure / reconfigure (Core)

- On boot: assign each array value to one ASDF attribute.
- Reconfigure: Free Action on your Action Phase (not a Matrix action). Each reconfig does **one** of: switch two Matrix attributes; swap a running program with a stored one; load a program into an empty slot; unload a program leaving a slot open.
- **DT Specialty decks:** cannot reconfigure ASDF (programs only); cheaper than standard equivalents.

### Matrix Condition Monitor (Core)

- Boxes: **8 + (Device Rating / 2)**.
- Resist Matrix damage: **Device Rating + Firewall**.
- Persona damage hits the deck Condition Monitor. Full MCM → bricked (VR → dumpshock).
- Repair: Hardware toolkit + 1 hour + Hardware + Logic [Mental]; each hit removes 1 box **or** halves time (min 1 Combat Turn). Critical glitch = permanently bricked.

### Running programs (Core)

- Benefits only while running. Cannot run more than one copy of the same program type at once (renaming copies does not help).
- Running programs appear as icons tied to the persona.
- **Crash Program** (Matrix action): Complex; 1 mark; Cybercombat + Logic [Attack] vs Intuition + Firewall; named running program scrambles (ends; cannot restart until device reboot).

### Program pricing (Core / DT)

| Category | Avail | Cost |
| --- | --- | --- |
| Cyberprogram, common use | - | 80¥ |
| Cyberprogram, hacking | 6R | 250¥ |

- Street Gear Software table preferred over Matrix chapter Programs Table (which prints hacking Avail **4R**). Flagged conflict: use **6R**.
- DT new programs do not reprint prices; Detonator text states normal hacking programs cost **250¥**. Use Core defaults unless a row overrides.
- **Detonator** costs **500¥** (twice normal hacking).
- **Nuke-from-Orbit:** Avail **12F**, Cost **250¥** (DT body omits Cost; community gear compilations list 250¥ matching other DT hacking programs at that price).
- **Cry Wolf:** no Avail/Cost printed.

### Form factors (DT; decks ≠ links)

Cyberdeck form-factor table (DT): Non-standard **+3 Avail, +20% cost**. Weapon **+6R, +50% cost**.
Commlink form factors are cheaper deltas (+2 / +4R); do not mix tables. Full procedure in Electronics.

### Deck modules (DT)

- Each deck has **1 module slot**.
- Insert/remove/swap: Hardware + Logic [Mental] (1), ~10 Combat Turns.
- If the deck is bricked, the installed module is destroyed (even if the deck is later repaired).
- Device mod "Add a Module" (Electronics) can hardwire a second module path; decks may have slot + one hardwired.

### Agents (Core)

- Rating 1-6; occupy **one program slot**.
- Use host device Matrix attributes; use own Rating for non-Matrix attributes (≤6).
- Skills: Computer, Hacking, Cybercombat each = agent Rating.
- Runs as a program; can use other programs running on the same device.
- Can perform Matrix actions for you; when running, has its own persona (and icon).
- Intelligence ≈ Pilot of same Rating (Pilot Programs, Core p. 269).
- Attacks on the agent damage the **device**; agent on your deck **shares your Matrix Condition Monitor**.

### Implanted cyberdeck (Core Cyberware)

| Item | Essence | Cap | Avail | Cost |
| --- | --- | --- | --- | --- |
| Cyberdeck (implant) | 0.4 | [4] | 5R | 5,000¥ + deck cost |

Buy the deck model separately; implant is the wrapper. Full cyberware row also in Cyberware.md.

### Known print conflicts

- **Novatech Navigator Avail:** Street Gear **9R** vs Matrix Cyberdecks table **6R**. This file uses Street Gear **9R**.
- **Hacking program Avail:** Street Gear **6R** vs Matrix Programs Table **4R**. This file uses **6R**.
- **KC Tiger** preloaded list prints Hammer twice (leave as printed).

## Catalog

### Core cyberdecks (standard)

Array = four values for ASDF (assign on boot). Prog = concurrent slots.

| Name | Src | DR | Array | Prog | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Erika MCD-1 | Core | 1 | 4 3 2 1 | 1 | 3R | 49,500¥ | Entry deck |
| Microdeck Summit | Core | 1 | 4 3 3 1 | 1 | 3R | 58,000¥ | |
| Microtrónica Azteca 200 | Core | 2 | 5 4 3 2 | 2 | 6R | 110,250¥ | |
| Hermes Chariot | Core | 2 | 5 4 4 2 | 2 | 6R | 123,000¥ | |
| Novatech Navigator | Core | 3 | 6 5 4 3 | 3 | 9R | 205,750¥ | Avail conflict with Matrix table 6R; Street Gear preferred |
| Renraku Tsurugi | Core | 3 | 6 5 5 3 | 3 | 9R | 214,125¥ | |
| Sony CIY-720 | Core | 4 | 7 6 5 4 | 4 | 12R | 345,000¥ | |
| Shiawase Cyber-5 | Core | 5 | 8 7 6 5 | 5 | 15R | 549,375¥ | |
| Fairlight Excalibur | Core | 6 | 9 8 7 6 | 6 | 18R | 823,250¥ | |

All include illegal hot-sim out of the box.

### DT standard cyberdecks

| Name | Src | DR | Array | Prog | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Radio Shack PCD-500 | DT | 1 | 2 2 1 1 | 1 | 2 | 21,000¥ | Entry / training |
| Little Hornet | DT | 2 | 5 4 1 1 | 2 | 5R | 89,700¥ | Chicago; Configurator often recommended |
| Microtrónica Azteca 300 | DT | 3 | 7 5 3 1 | 3 | 9R | 200,000¥ | Upgrade path from Azteca 200 |
| Xiao MPG-1 | DT | 4 | 8 5 4 3 | 3 | 13R | 302,000¥ | Attack-focused |
| Shiawase Cyber-4 | DT | 4 | 8 6 4 2 | 3 | 12R | 331,000¥ | Undercuts CIY-720 |
| Fairlight Paladin | DT | 6 | 9 9 8 8 | 6 | 20R | 1,050,000¥ | Ultra-rare |

### DT specialty cyberdecks (fixed ASDF; no attribute reconfig)

| Name | Src | DR | A | S | DP | FW | Prog | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCT Trainee | DT | 1 | 2 | 1 | 1 | 2 | 1 | 3R | 17,250¥ | Built-in Biofeedback Filter |
| C-K Analyst | DT | 2 | 1 | 5 | 4 | 3 | 1 | 5R | 83,800¥ | HD camera/recording suite; hardwired Edit |
| Aztechnology Emissary | DT | 3 | 2 | 3 | 3 | 8 | 1 | 8R | 168,000¥ | Courier / defense / slave protection focus |
| Yak Killer | DT | 3 | 7 | 6 | 2 | 3 | 2 | 13R | 194,000¥ | Reality Hackers-style config |
| Ring of Light Special | DT | 4 | 8 | 1 | 2 | 6 | 3 | 10R | 242,000¥ | RoL events; low Sleaze |
| Ares Echo Unlimited | DT | 5 | 9 | 6 | 4 | 5 | 3 | 15R | 395,900¥ | Ruggedized combat |

### KC custom series

#### Fuchi Cyber-N Series

Once set, attributes **cannot** change. Can only **store and run 1 program** (any Rating). Deck Rating is the **maximum** allowed for each other attribute (not a Core-style free array).

| Attribute | Src | Avail | Cost |
| --- | --- | --- | --- |
| Deck Rating | KC | (DR x 2)R | Rating x 5,000¥ |
| Attack | KC | - | Rating^3 x 500¥ |
| Sleaze | KC | - | Rating^2 x 500¥ |
| Data Processing | KC | - | Rating^2 x 500¥ |
| Firewall | KC | - | Rating^3 x 500¥ |

#### Fuchi Cyber-Ex Series

Device Rating is the **maximum** rating of every other attribute. Concurrent programs = **DR + 2**. Programs not included in price. Flavor text first says storage = **2 x runnable**, then "as many as you can afford"; rules block only caps concurrent run count.

| Attribute | Src | Avail | Cost |
| --- | --- | --- | --- |
| Deck Rating | KC | (DR x 2)R | Rating x 10,000¥ |
| Attack | KC | - | Rating^3 x 500¥ |
| Sleaze | KC | - | Rating^2 x 500¥ |
| Data Processing | KC | - | Rating^2 x 500¥ |
| Firewall | KC | (Rating x 4)R | Rating^3 x 500¥ |

### KC security decks

Fixed A S DP FW as printed (Sleaze = 1). Preloaded program allotments; changing the program block requires Logic + Hardware [Mental] (DR x 2, 1 hour) Extended. Any roll with **0 hits** bricks the deck. Concurrent slots = preloaded set size.

| Name | Src | DR | A | S | DP | FW | Prog | Avail | Cost | Preloaded |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Guard | KC | 2 | 3 | 1 | 2 | 4 | 1 | 3R | 39,000¥ | Encryption |
| Shield | KC | 4 | 4 | 1 | 3 | 5 | 2 | 6R | 98,000¥ | Encryption, Shell |
| Fortress | KC | 6 | 6 | 1 | 5 | 8 | 3 | 9R | 377,000¥ | Encryption, Shell, Armor |
| Great Wall | KC | 8 | 8 | 1 | 6 | 10 | 4 | 12R | 774,000¥ | Encryption, Shell, Armor, Biofeedback Filter |

### KC hunter decks

Fixed A S DP FW as printed (Sleaze = 1). Always hot-sim (no sim-inhibitor). May change preloaded programs, but system only allows programs useful to e-hunting (Attack- and Firewall-based actions/attrs). Prog = printed preload count (Tiger/Shark print Hammer twice).

| Name | Src | DR | A | S | DP | FW | Prog | Avail | Cost | Preloaded (as printed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fox | KC | 2 | 4 | 1 | 3 | 4 | 3 | 4R | 68,500¥ | Track, Shell, Hammer |
| Wolf | KC | 4 | 5 | 1 | 4 | 5 | 4 | 8R | 133,000¥ | Track, Shell, Hammer, Decryption |
| Tiger | KC | 6 | 8 | 1 | 6 | 8 | 5 | 12R | 530,000¥ | Track, Shell, Hammer, Decryption, Hammer |
| Shark | KC | 8 | 10 | 1 | 8 | 10 | 7 | 16R | 1,032,000¥ | Track, Shell, Hammer, Decryption, Hammer, Mugger, Fork |

### KC named decks

| Name | Src | DR | Array | Prog | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Aztechnology Shadow Warrior | KC | 3 | 6 5 4 3 | 3 | 10R | 225,000¥ | +1 limit on Matrix Sleaze actions; +1 Sleaze when Sleaze is configured highest |
| Evo Sublime | KC | 4 | 7 6 5 5 | 4 | 12R | 375,000¥ | Implanted only. In VR, non-Matrix actions: -10 dice, -3 limit (min 1) |
| Fairlight Destiny Blade | KC | 4 | 7 6 5 5 | 4 | 12R | 400,000¥ | +1 Cybercombat limit; +1 Attack when Attack is configured highest |
| Aztechnology Defender | KC | 5 | 8 7 5 5 | 5 | 14R | 560,000¥ | Matrix damage taken -1 box (min 1); dumpshock -2 (min 1); Initiative Score -2 after rolling |
| Kitbashed Sleeper | KC | 4 | 7 5 5 4 | 4 | 14F | 375,000¥ | TM may perform Resonance actions (compile/thread/register) through the deck. Fade resist: Resonance + Firewall. Unresisted fade = non-repairable Matrix box on the deck; at 10 boxes the device is irreparably broken. Fade absorbed by the Sleeper does not hit the TM |

### Deck modules (DT)

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Hardening | DT | Module | 3R | 1,500¥ | Own Matrix CM **5 boxes**; takes damage before the deck; boxes **not repairable** |
| Induction Receiver | DT | Module | 10R | 1,200¥ | Place deck on a data cable → direct connection to devices on either side |
| Multidimensional Coprocessor | DT | Module | 7R | 1,400¥ | +1D6 Matrix Initiative (cap 5D6 total Initiative dice) |
| Overwatch Mask | DT | Module | 9F | 4,200¥ | Convergence OS threshold +4 (normally 40 → 44 under normal conditions) |
| Program Carrier | DT | Module | 2 | 900¥ | Permanently runs one locked program (extra slot); price includes the program; cannot change |
| Self-Destruct | DT | Module | 12F | 200¥ | On a preset condition, deck becomes a fragmentation grenade (Core grenade rules); deck unrecoverable |
| Vectored Signal Filter | DT | Module | 3 | 800¥ | Noise Reduction 2 |

### Agents (Core)

| Name | Src | Type | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Agent | Core | Agent | 1-3 | Rating x 3 | Rating x 1,000¥ | See Common rules → Agents |
| Agent | Core | Agent | 4-6 | Rating x 3 | Rating x 2,000¥ | Same. Example R6: Avail 18, 12,000¥ |

DT/KC add no new agent buy SKUs (Nixdorf Sekretar built-in agent is a specialty commlink → Electronics).

### Core common cyberprograms (80¥ each)

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Browse | Core | Common | - | 80¥ | Matrix Search time cut in half |
| Configurator | Core | Common | - | 80¥ | While running, store an alternate full deck configuration. Next reconfigure may switch to that **full** stored config (not just two attrs/programs), even if Configurator stops. Stored config persists for later recall while Configurator is running |
| Edit | Core | Common | - | 80¥ | +2 to Data Processing **limit** on Edit tests |
| Encryption | Core | Common | - | 80¥ | +1 Firewall |
| Signal Scrub | Core | Common | - | 80¥ | Rating 2 noise reduction |
| Toolbox | Core | Common | - | 80¥ | +1 Data Processing |
| Virtual Machine | Core | Common | - | 80¥ | Run +2 additional programs; whenever persona takes Matrix damage, take +1 unresistable Matrix damage box |

### Core hacking cyberprograms (6R / 250¥ each)

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Armor | Core | Hacking | 6R | 250¥ | +2 dice pool to resist Matrix damage |
| Baby Monitor | Core | Hacking | 6R | 250¥ | Always know current Overwatch Score |
| Biofeedback | Core | Hacking | 6R | 250¥ | Your Matrix damage also deals equal Stun (cold-sim) or Physical (hot-sim) biofeedback to biological targets; also when foes take damage from failing Attack actions against you. Resist biofeedback: Willpower + Firewall |
| Biofeedback Filter | Core | Hacking | 6R | 250¥ | +2 dice pool to resist biofeedback damage |
| Blackout | Core | Hacking | 6R | 250¥ | As Biofeedback, but always Stun (even vs hot-sim) |
| Decryption | Core | Hacking | 6R | 250¥ | +1 Attack |
| Defuse | Core | Hacking | 6R | 250¥ | +4 dice pool to resist Data Bomb damage |
| Demolition | Core | Hacking | 6R | 250¥ | +1 to Rating of any Data Bomb you set while running |
| Exploit | Core | Hacking | 6R | 250¥ | +2 Sleaze when attempting Hack on the Fly |
| Fork | Core | Hacking | 6R | 250¥ | One Matrix action vs two targets; one test (both targets' mods apply); each defends separately |
| Guard | Core | Hacking | 6R | 250¥ | Extra damage from marks reduced by 1 DV per mark |
| Hammer | Core | Hacking | 6R | 250¥ | +2 DV Matrix damage on your damaging Matrix actions; does **not** apply when targets take damage from failing Attack actions against you |
| Lockdown | Core | Hacking | 6R | 250¥ | When you damage a persona, they are link-locked until you stop this program or they Jack Out successfully |
| Mugger | Core | Hacking | 6R | 250¥ | Bonus damage from marks +1 DV per mark |
| Shell | Core | Hacking | 6R | 250¥ | +1 dice pool to resist Matrix and biofeedback damage; stacks with similar mods |
| Sneak | Core | Hacking | 6R | 250¥ | +2 dice vs Trace Icon (Core prose: "Trace User"); if demiGOD converges while running, they do **not** get your physical location (other convergence effects still apply) |
| Stealth | Core | Hacking | 6R | 250¥ | +1 Sleaze |
| Track | Core | Hacking | 6R | 250¥ | Either +2 Data Processing on Trace Icon tests (Core: "Trace User"), **or** negate target's Sneak +2 defense; choose one benefit, not both |
| Wrapper | Core | Hacking | 6R | 250¥ | Change Icon can make icons look like anything; Matrix Perception can reveal true nature if someone suspects and checks |

### DT common cyberprograms

Use Core common pricing (- / 80¥) unless noted.

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | DT | Common | - | 80¥* | Via Format Device, plant hidden boot-record tasks after next reboot (examples printed: announce location when connecting; force default attrs to user's choice; nag for ownership; log every action). Not limited to brick-on-reboot |
| Search | DT | Common | - | 80¥* | +2 dice on Matrix Search for specific data on a host that contains that data; no bonus if looking for something that originates outside the host. Johnsons often provide one-shot self-destruct copies |
| Shredder | DT | Common | - | 80¥* | +2 Data Processing for deleting a file with Edit File (overwrites with junk). Recovery: continuous host/grid access + Computer (File Recovery) + Logic [Mental] (18, 1 week) Extended. Same recovery path noted for Data Bomb destruction |

\*DT does not reprint common prices; Core default used.

### DT hacking cyberprograms

Default 6R / 250¥ unless overridden.

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Cat's Paw | DT | Hacking | 6R* | 250¥* | Successful Data Spike: no Matrix damage; instead target gets dice pool penalty = **2 + marks** you have on them (updates if marks are later added/removed). Fills AR/VR with spam/errors |
| Cloudless | DT | Hacking | 6R* | 250¥* | Successful Edit File Opposed Test moves a file off the Matrix into one designated device's memory only (legacy physical-media code). Opposing dice: Public grid 6 / local grids 8 / global grids 10 |
| Crash | DT | Hacking | 6R* | 250¥* | +2 Data Processing when attempting Reboot Device |
| Detonator | DT | Hacking | 6R* | **500¥** | On successful Set Data Bomb: choose how many actions may hit the file before trigger; choose Matrix damage **or** delete. Detect with Matrix Perception / disarm with Disarm Data Bomb. Vs Perception: treat as DR 3, Sleaze = [remaining actions before detonation - 1]. Costs twice normal hacking (500¥) |
| Evaluate | DT | Hacking | 6R* | 250¥* | Black-BBS paydata auction feeds estimate how much paydata is worth / how much heat taking extra generates. **No dice formula printed** |
| Fly on a Wall | DT | Hacking | 6R* | 250¥* | Requires Hide to activate. While running and performing **no** actions other than Matrix Perception: OS increases by only **1D6 per half-hour** (GM rolls secret as normal). Does not help vs other icons noticing you |
| Hitchhiker | DT | Hacking | 6R* | 250¥* | Lets you take non-hacker friends to foundations and UV hosts. **No further mechanics printed** |
| Nuke-from-Orbit | DT | Hacking | **12F** | 250¥ | Edit File delete: file unrecoverable from the Matrix (offline backups / Resonance realms only). Any OS generated from the Opposed Test is **doubled**. Cost filled from community DT gear tables (body text prints Avail only) |
| Paintjob | DT | Hacking | 6R* | 250¥* | +2 Attack for Erase Mark tests |
| Smoke-and-Mirrors | DT | Hacking | 6R* | 250¥* | Raise Sleaze by 1 to 5 (choice); add equal Noise to tests performed with the deck; that Noise also affects Trace Icon tests against you. **No effect vs Convergence** |
| Swerve | DT | Hacking | 6R* | 250¥* | +1 Firewall on the deck and PAN-connected devices when resisting Reboot Device |
| Tantrum | DT | Hacking | 6R* | 250¥* | Data Spike deals no Matrix damage; if ≥1 Matrix box would have been scored, target gets Nausea (Core p. 409) for 3 Combat Turns. Affects TMs and cold/hot sim deckers; does nothing to AR users, IC, or agents |
| Tarball | DT | Hacking | 6R* | 250¥* | Crash Program only: +2 Attack and +1 die; hits a **random** running program rather than a chosen one |

\*Avail/Cost not restated in DT; Core hacking defaults + Detonator pricing note.

### KC specialty software

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Cry Wolf | KC | Specialty | (unprinted) | (unprinted) | Creates a randomized secondary Matrix location (you do not pick it). On Convergence, GOD hits that false persona/location instead; program warns when the false Convergence fires. If GOD notices the ruse, real Convergence in another **1D6** Combat Turns (same after dealing with a false decker). **One-use signature:** after GOD is fooled once by a given copy, they remember that randomizer and skip the fake next time. Treated as felonious (on par with murder); fake licensing will not cover possession. No Avail/Cost in body or KC Misc. Items table |

### RF Decker PACKs

Discounted gear bundles (nuyen and/or Karma). Component stats are the individual SKUs above (or Tools kits). Src: Run Faster pp. 248-249 (`Source/_extract/rf_decker_packs.txt`).

| Name | Src | Cost / Karma | Avail | Contents | Notes |
| --- | --- | --- | --- | --- | --- |
| Intro to Hacking PACK | RF | 58,000¥ / 29 Karma | 3R | Microdeck Summit cyberdeck | Matches Summit list price |
| Basic Decker PACK | RF | 124,000¥ / 62 Karma | 6R | Hermes Chariot cyberdeck; Software kit; Hardware kit | Kits → Tools Kits and Survival |
| Advanced Decker PACK | RF | 346,000¥ / 173 Karma | 12R | Sony CIY-720 cyberdeck; Software kit; Hardware kit | Kits → Tools |
| Basic Cyberdeck Programs PACK | RF | 2,000¥ / 1 Karma | - | **ITEMS box print error:** PDF/book layout repeats Advanced Decker ITEMS (Sony CIY-720 + Software kit + Hardware kit), which cannot match a 2,000¥ PACK. Flavor: "stay hidden, find what you need, and hide." **Do not invent a program list** until a corrected ITEMS source is available | Incomplete ITEMS |
| Advanced Cyberdeck Programs PACK | RF | 2,000¥ / 1 Karma | 6R | Hacking cyberprograms: Armor, Biofeedback, Blackout, Guard, Hammer, Mugger, Shell | 7 named Core hacking programs |

## Cross-refs (do not duplicate full SKUs here)

| Item | Lives in | Why pointed |
| --- | --- | --- |
| Commlinks, dongles, form-factor mods, MOS, Datajack Plus, device mods (Add Attribute / Add Module) | Commlinks and Electronics | Shared Matrix gear / hardwire path |
| RCC Encryption / Signal Scrub / Toolbox / VM / Armor / Biofeedback Filter / Guard / Shell / Sneak / Wrapper; Swarm | Rigger Gear | RCC copies; cannot run on decks |
| Implanted cyberdeck Essence row | Cyberware | Headware wrapper |
| Software kit / Hardware kit | Tools Kits and Survival | RF Decker PACK components |
| Self-Destruct blast profile | Grenades and Explosives / Core grenades | Fragmentation grenade |
| Nixdorf Sekretar built-in agent | Commlinks and Electronics | Specialty commlink |
| Complex Forms / Echoes | TM / Mechanics docs | Not cyberprograms |
