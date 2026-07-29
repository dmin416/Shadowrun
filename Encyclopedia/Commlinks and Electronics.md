# Commlinks and Electronics

Agent reference (SR5). Compact; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `datatrails.pdf` · `killcode.pdf` · `runandgun.pdf` · `runfaster.pdf` (PACK notes) · `rigger5.pdf` (vehicle sat/retrans pointer)
**Books:** Core · DT · KC · RnG · RF (PACKs) · R5 (pointer)
**Printed:** Core Electronics 438-443; Matrix devices/Noise 219-234; DT Killer Apps & Guts 55-67; KC Dips & Chips 48-75; RnG PI-Tac 104-105; weapon link/personality accessories 53-54
**See also:** `Encyclopedia/Cyberdecks and Programs.md` · `Encyclopedia/Rigger Gear.md` · `Encyclopedia/Sensors and Optics.md` · `Encyclopedia/Identity and Documentation.md` · `Encyclopedia/Security and Surveillance.md` · `Encyclopedia/Cyberware.md` · `Encyclopedia/Bioware.md` · `Encyclopedia/Weapon Accessories.md` · `Encyclopedia/Grenades and Explosives.md` · `Encyclopedia/Ammunition.md` (Zapper/Looper/Fuzzy/ArrowLink) · `Mechanics/Matrix.md`

**In scope:** commlinks (Core/DT/KC), sim modules, electronics accessories, RFID, communications/countermeasures, consumer software, skillsofts, DT apps/dongles/form factors, electronic parts & device mods, KC MOS/Faceless/trode patch/boosters/Matrix grenades, KC specialty links, PI-Tac + Pantheon tac-apps/accessories, weapon-mounted link/personality, Matrix-related headware listed here with full stats.
**Out of scope (pointers):** cyberdecks, deck modules, cyberprograms, agents as deck tools → Cyberdecks and Programs.md; RCC base catalog / autosofts / personal drone rack as rigger mount → Rigger Gear (KC Cyber-6 / Skirmisher included here as buy rows + pointer); credsticks/fake SIN → Identity and Documentation; cameras/sensors → Sensors; maglocks/sequencers → Security; Matrix *ammo* / ArrowLink cords → Ammunition; R5 vehicle Satellite Link / Retrans Unit → Rigger Gear (jumped-in/network mods) and Vehicle and Drone Modifications.

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / DT / KC / RnG / RF |
| DR | Device Rating |
| DP / FW | Data Processing / Firewall (Core links: both = DR unless custom) |
| Avail / Cost | Street Availability / nuyen. `-` = none |
| Rules | Full mechanical notes |

## Common rules

### Devices and Matrix attrs (Core)

- Nearly every gear item is wireless-capable and has a Device Rating (if unspecified, use Device Ratings table).
- Commlinks / most devices: Matrix attrs **Data Processing** and **Firewall** only. Default: both = Device Rating.
- PAN: slave up to (master Device Rating x 3) devices to a master link/deck.
- Noise: distance + situation - noise reduction; leftover Noise = dice pool penalty on Matrix actions (not defense).
- Wireless bonus only while Matrix-connected and Noise from situation (not distance) ≤ item DR.
- Toggle wireless off (one device or all): Free Action. Lose wireless bonuses; cannot be wirelessly hacked.
- **Throwback:** no wireless. Buy as throwback, or Hardware + Logic [Mental] (8, 10 min) Extended to strip wireless.
- Direct connection (cable / data tap / cable-tap dongle): ignore Noise and grid modifiers between connected devices.
- Universal data cable: ~**5¥ per meter** (Core Matrix). Decks/datajacks include ~1 m retractable microfilament.

| Device Ratings (if unspecified) | DR | Examples |
| --- | --- | --- |
| Simple | 1 | Appliances, public terminals, entertainment |
| Average | 2 | Standard personal electronics, basic cyber, vehicles, drones, weapons, residential security |
| Smart | 3 | Security vehicles, alphaware, corp security devices |
| Advanced | 4 | High-end, betaware, military vehicles/mil-spec security |
| Cutting Edge | 5 | Deltaware, credsticks, black-ops vehicles/security |
| Bleeding Edge | 6 | Billion-nuyen experimental, spacecraft |

### Commlinks (Core 438-439)

- Swiss-army communicator: AR Matrix browse, phone/radio talk/text, music, micro trid, touchscreen, cameras, image/text/RFID scanners, GPS, chip player, credstick reader, retractable earbuds, voice dialing, TTS/STT, shock/water resistant case.
- Persona for Matrix use in AR; VR needs sim module + DNI (trodes, datajack, or implanted link).
- Can run apps: up to **half Device Rating, rounded up** (DT).

### Sim module (Core)

- Translates computer data to neural signals for simsense / AR / VR.
- Requires DNI (trodes, datajack, or implanted link).
- Optional **hot-sim** mod: full (dangerous) VR; dumpshock and biofeedback become Physical in hot-sim (Matrix rules).

### RFID (Core 440)

- Tiny devices; hold files; adhesive; can track via GPS / Trace Icon.
- Owner can be set to "nobody" (unlike most devices).
- Erase with tag eraser or Edit File. Security tags EMP-hardened vs tag eraser.

## Shared procedures

### Form factor (DT 60-61)

| Form | Avail mod | Cost mod |
| --- | --- | --- |
| Non-standard (clothing, pen, glasses, watch, purse, hat, cane, knife, small pistol, etc.) | +2 | +20% |
| Weapon-integrated | +4R | +50% |

Still pay for the host object separately. Weapon install must survive normal weapon use.

### Dongles (DT 61-62)

- Plug into universal data port; **one dongle per link** at a time; barely increases size.

### Bug scanner (Core)

- Locate/lock wireless devices within **20 m**; measure strength; pinpoint.
- Test: Electronic Warfare + Logic [Rating] vs silent device's Logic + Sleaze.
- Any net hits = found. **Wireless:** may substitute scanner Rating for Electronic Warfare skill.

### Jammers (Core)

- Generate Noise = Device Rating (jammer Rating).
- **Area:** sphere; Rating -1 per 5 m from center.
- **Directional:** 30° cone; Rating -1 per 20 m from center.
- Affects devices/personas in area. Walls may block/reduce (GM).
- **Wireless:** whitelist devices/personas you designate.
- **Headjammer:** same jammer effect limited to wearer + their augmentations. Remove without key: Hardware + Logic [Mental] or Locksmith + Agility [Physical] (8, 1 Complex) Extended; from self: Escape Artist + Agility [Physical] (4), Complex.

### Tag eraser (Core)

- Within **5 mm** of device, push button: target takes **10 Matrix damage** (resist normally). 1 charge; wall recharge **10 seconds**. **Wireless:** full recharge in **1 hour** induction.

### White noise generator (Core)

- Perception to overhear within (Rating) m: -Rating dice. Multiple: use highest Rating only. Useless in already-noisy environments; does not jam wireless or stop video. **Wireless:** radius x3.

### Data tap (Core) / Cable tap dongle (DT)

- Clamp on data cable → UDC access; devices on tap and both cable ends are directly connected. Remove without damaging cable.
- Data tap **Wireless:** Free Action self-destruct severs direct connection, no cable harm.
- Cable tap dongle: same idea as dongle on your link.

### Device modification (DT 65-67)

- Need Hardware + Logic [Mental] (15, 15 min) Extended; Hardware tools; enough **electronic parts packs**. -4 without tools; memory/condition mods apply (Core 146).
- Unless noted, **one modification per device**.
- Scavenge: Hardware + Logic [target DR], 10 min, Hardware toolkit; each hit = 1/4 pack. Mods: +4 if cannibalizing link/deck; +0 cyberware; -4 other; -1 per Matrix damage box.

| Mod | Packs needed | Effect |
| --- | --- | --- |
| Add Matrix Attribute (Attack or Sleaze only if missing) | DR x 2 | Starts at 1; can later Increase |
| Add a Module (hardwire deck module) | 2 + need the module | Most devices 1 module; decks can have slot + hardwired |
| Increase a Matrix Attribute +1 | new rating x 2 | **2 permanent irreparable Matrix damage boxes** |
| Modify Matrix Attribute (+1 one / -1 another) | 4 | Also works on deck attribute array |
| Persona Firmware | 2 | Device can run a persona (if it couldn't) |

### MOS (KC)

- Multiprogram Operating System: run programs = Rating; max Rating **4**. Cord to link/deck: **0.5 m**.
- Heat while carried and in use: in case **(Rating)S** / turn; out of case but clothed **(Rating x 2)S**; bare skin = Physical. Fire Protection resists if armor between box and body. Safe on stable non-flammable surface.

### Faceless (KC)

- Wearable accessory (pin, earring, etc.): mini-hacks nearby recorders to rewrite your face.
- Test: Rating x 2 [Rating] (Firewall + 2) instead of Edit File. Success: overwrite works until new device in range. Fail: glitchy/obvious or fail. Glitch: face on wrong person.
- Vs cybereyes / monitored systems: blur obvious unless in crowd. Max Rating **10**.
- Options: Generic face +2 Avail / +1,000¥; Specific face +4 Avail / +5,000¥.

### Booster cloud (KC)

- Aerosol can. Simple = half can (+1 dice, +1 limit); Complex = whole can (+2 dice, +1 limit) to **one** Matrix Action type for up to **3** Combat Turns (air movement may shorten). Physical-world cloud; others entering share bonus.

### Booster chips (KC; technomancer living persona)

- Pin to bare scalp skin (slotless BTL-style). Simple to attach; lasts **2** Combat Turns.
- Rating adds to linked living-persona attr (limit + dice where that attr applies; never double-count same attr on one test).
- End: (Rating)S resist Body; +2 DV per other chip still/also ending. Addiction Rating = total Ratings in use; Threshold = 2 + 1 per additional chip.

### Matrix grenades (KC)

- **Fuzzy:** Noise = Power, -1 per 2 m; lasts 2 Combat Turns; max Power 20. Avail 10R; Cost 20¥ x Power.
- **CoS:** 5 m pulse severs Matrix/wireless; VR users dumpshock; drones keep last orders. Devices alert reboot end of turn (Simple/Free DNI cancel; slaved group = one action). Reboot online end of next turn. Technos: resist **10S**, severed. Avail 10R; 500¥.
- **Douser:** 5 m nanite sphere; Rating x 2 [Rating] (Firewall) once; -1 Firewall per net hit on all devices/cyber. FW 0 → reboot alert (same cancel rules). Max Rating 10. Avail (Rating x 2)F; Rating x 50¥.
- **DumDum:** same sphere; vs Data Processing instead of Firewall. DP 0 = no processing (wireless bonuses die, freeze, etc.); must **manual** hard reboot. Avail (Rating x 2)R; Rating x 50¥.

### PI-Tac (RnG 104-105; KC tac-apps 70-74)

- Plug-in unit; integrates with a host **commlink, cyberdeck, or RCC** into a shared PAN/WAN. Wireless (hackable).
- Max subscribers (people + drones) on one net: **DR x 1.5**.
- All levels include: real-time GPS; universal image/audio link to network sensors/augs; team biomonitor; weapon status (ammo/condition/incursion); Enhanced Situational Awareness (Perception bonus by level).
- **Level I:** +1 all Perception (incl. audio/visual). Civilian-legal with permit/background in setting.
- **Level II:** Level I + host enhancement: add **half DR** to either host Firewall **or** Data Processing; trauma module (chest plate under armor; 1 dose any drug; auto-inject on user conditions); +2 Perception; +1 Sneaking; team leader coordinates combat maneuvers as **Simple** (not Complex) and may transfer **5** Initiative to one networked member; Combat Mode +1 to one chosen combat skill (Close Combat, Automatics, Longarms, Pistols, Unarmed); switch skill = Simple.
- **Level III:** Level I+II upgrades: host enhancement = **full DR** to **both** Firewall and Data Processing; team leader Initiative transfer **10** to one or **5** to two; +3 Perception; +2 Sneaking and Tracking; Combat Mode +2 to one listed combat skill; remote limited vehicle/drone dogbrain commands for leader or designated member (treat as **3 marks** while subscribed): simple go-to / attack if units operational (e.g. rigger down). Unauthorized possession: felony (setting).
- **Tac-apps (KC):** programs for PI-Tac only (not on unlinked decks). Bonuses stack with linked deck/RCC. Master loads **Level + 2** tac-apps. Unload/load from storage: **Simple**; with Tactical Program Dongle: **Free** (as deck reconfigure). One dongle per PI-Tac. Extra programs onto dongle: Software + Logic [Mental] (remaining dongle slots). Co-Pilot MK I and MK II incompatible with each other. Co-Pilot needs admin access + wireless to target vehicles/drones.

### Mercury-Alpha Battlefield Signal Booster (KC)

- Attaches to PI-Tac master, link, deck, or RCC. Components: brain (main unit ~450 g), foldable micro-dish, optional hardened fiber to link brain/dish.
- One mode at a time; switch = Simple. Stacks with tac-apps, sat links, retrans.
- **Passive:** +4 dice vs all Noise sources; **double** effective range.
- **Defensive / aggressive:** +2 on pertinent Electronic Warfare tests. Linked PI-Tacs may distribute some/all of that +2 to assist other operators **without** teamwork test (Simple).

### CCOB backpacks (KC)

- Combat Communications and Operations Backpack. Armor does **not** stack with other armor.
- Hard Case: protects contents vs **physical** damage only; internal shell for deck/RCC.

### Datajack Plus / EARRS / Cranial Shield / Biolink (KC)

- **Datajack Plus:** standard datajack DNI + Noise filter; when connected to link/deck, run Common + Hacking programs = **Rating** (max 3). Price includes Rating free preloaded programs (GM choice; swappable).
- **EARRS:** Matrix Initiative in physical encounters; move and perceive physically OK; all Physical and Social skill actions **-10** dice; Matrix Actions normal.
- **Cranial Shield:** cranial emitters; **all wireless** between in-cranium devices and outside fail; wired bypass (e.g. datajack) still works; also blocks technomancer Matrix access. No separate RULES box beyond description + buy line.
- **MCT Biolink:** bioware wireless datajack. No Resonance, no Matrix persona; DNI to wireless devices without jack/wires. Ess 0.5 / Avail 10 / 15,000¥.

## Catalog

### Commlinks (Core)

| Name | Src | DR | DP | FW | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Meta Link | Core | 1 | 1 | 1 | 2 | 100¥ | Standard link. |
| Sony Emperor | Core | 2 | 2 | 2 | 4 | 700¥ | |
| Renraku Sensei | Core | 3 | 3 | 3 | 6 | 1,000¥ | |
| Erika Elite | Core | 4 | 4 | 4 | 8 | 2,500¥ | |
| Hermes Ikon | Core | 5 | 5 | 5 | 10 | 3,000¥ | |
| Transys Avalon | Core | 6 | 6 | 6 | 12 | 5,000¥ | |
| Fairlight Caliban | Core | 7 | 7 | 7 | 14 | 8,000¥ | |
| Sim module | Core | - | - | - | - | +100¥ | Commlink upgrade. Needs DNI. |
| Sim module w/ hot-sim | Core | - | - | - | +4F | +250¥ | Hot-sim VR enabled. |

### Specialty commlinks (DT)

| Name | Src | DR | DP | FW | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EvoTech Himitsu | DT | 2 | 1 | 2 | 8R | 11,000¥ | Lunchbox-sized; looks low-end. Secret compartment ≤ pistol/cigar-box; built-in Faraday cage; integrated stealth module **Sleaze 5**. |
| MCT Blue Defender | DT | 3 | 1 | 5 | 7 | 2,000¥ | Wristband form; high Firewall for security/runners. |
| Nixdorf Sekretär | DT | 4 | 6 | 2 | 5 | 4,000¥ | Built-in **Rating 3 agent** (calendar/files/work). |
| Sekretär + Liebesekretär | DT | +1 | - | - | - | +2,000¥ | Matchmaking/date/concierge/rating package. Table lists +1 (treat as +1 DR). |

Form-factor mods (Shared procedures) apply to any link including these.

### Specialty commlinks (KC)

| Name | Src | DR | DP | FW | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Horizon Flow | KC | 5 | 5 | 5 | 12 | 4,000¥ | +2 limit and +1 dice to Data Search with this link. Optional Horizon smart-assistant algorithms (usage telemetry; disableable). |
| Wuxing Frequency | KC | 4 | 4 | 4 | 10 | 3,500¥ | +5 dice and +2 limit on Matrix Perception to identify an icon as a technomancer. Spotting a techno still needs **5** net hits (Core 241). Colors edge of icons for interpretation. |
| Saeder-Krupp Last Chance | KC | 3 | 3 | 3 | 11 | 5,000¥ | Nasal-cavity plastic sheet; inactive hard to spot. Activate via throat strip (sneezing/cough cover). ~**1 hour** battery; toggle on/off. Concealability **-8**. Extended wear (weeks): GM may impose distraction. |

### Specialty RCC (KC; also Rigger Gear)

| Name | Src | Rating | DP | FW | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Shiawase Cyber-6 RCC | KC | 5 | 5 | 5 | 12R | 72,000¥ | While jumped in: all drones commanded from console +2 Initiative and +1 limit on all tasks. Dumpshock from this console **+4** DV. |
| Spinrad Global Skirmisher RCC | KC | 4 | 5 | 5 | 8R | 50,000¥ | Drones commanded via Control Device from this RCC: +2 dice and +1 limit on Gunnery and Perception. |

### Commlink dongles (DT)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Attack dongle (1-6) | DT | (Rating x 2)R | (Rating^2) x 3,000¥ | Gives link Attack = Rating. |
| Stealth dongle (1-6) | DT | (Rating x 2)R | (Rating^2) x 3,000¥ | Gives link Sleaze = Rating. |
| Cable tap | DT | 8R | 500¥ | Split-ring on data cable; direct connect to both ends via link. |
| Stun dongle | DT | 6R | 600¥ | Contact stun weapon: Acc 4, Reach 0, DV **8S(e)**, AP -5; **3 charges**. |
| Receiver | DT | 3 | 400¥ | Noise Reduction **2** for link + all slaved devices. |

### Electronics accessories (Core)

| Name | Src | DR | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| AR Gloves | Core | 3 | - | 150¥ | Touch/hold AROs; tactile force-feedback (weight/temp/hardness). Compatible with link/deck/(GM) other electronics. |
| Biometric reader | Core | 3 | 4 | 200¥ | Fingerprint/retina/voice/tongue/etc. (not DNA). Lock electronics to biometrics. |
| Electronic paper | Core | 1 | - | 5¥ | Foldable digital sheet; wireless write/erase; touchscreen. |
| Printer | Core | 3 | - | 25¥ | Hardcopy; attached paper supply. |
| Satellite link | Core | 4 | 6 | 500¥ | LEO uplink where no local wireless; limits Noise due to distance to **-5**. Includes portable dish. |
| Simrig | Core | 3 | 12 | 1,000¥ | Record sensory/emotive simsense from wearer. Needs working sim module + DNI. |
| Subvocal mic | Core | 3 | 4 | 50¥ | Throat adhesive; -4 Perception to overhear. |
| Trid projector | Core | 3 | - | 200¥ | Hologram in 5 m cube beside/above device. |
| Trodes | Core | 3 | - | 70¥ | Headband/net/cap DNI. Headgear Capacity **2** to install. |
| Universal data cable | Core | - | - | ~5¥ / m | Direct connect; Matrix chapter. |

### KC DNI / program accessories

| Name | Src | DR/Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Trode Patch | KC | 4 | 4 | 1,250¥ | Quarter-sized (~2.5 cm) DNI = full trode rig; needs bare cranial skin contact. |
| Patch Cover | KC | - | - | 250¥ | Cosmetic cover (hair match / logos). |
| MOS (1-4) | KC | Rating | 6 | Rating x 4,000¥ | Shared procedures → MOS. Extra program slots for link/deck. |
| Faceless (1-10) | KC | Rating | (Rating x 2)F | Rating x 500¥ | Shared procedures → Faceless. |
| Faceless generic face | KC | - | +2 | +1,000¥ | Overlay option. |
| Faceless specific face | KC | - | +4 | +5,000¥ | Overlay option. |

### RFID tags (Core; prices per 10 except datachip)

| Name | Src | DR | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Standard tags | Core | 1 | - | 1¥ / 10 | Geo-tag, AR messages, tracking, registration, etc. |
| Datachip | Core | 1 | - | 5¥ each | Huge storage; **no wireless**; must plug UDC to R/W. |
| Security tags | Core | 3 | 3 | 5¥ / 10 | Implantable; access/track. **Cannot** tag-erase (EMP harden). Implanted remove: Medicine + Logic [Mental] (10, 1 min) Extended. |
| Sensor tags | Core | 2 | 5 | 40¥ / 10 | + one sensor ≤ Rating 2 (sold separate). Records ≤24 h then stop or overwrite. **Wireless:** owner real-time monitor; still keeps last 24 h. |
| Stealth tags | Core | 3 | 7R | 10¥ / 10 | Always silent; Sleaze = DR; Concealability **-2** extra; implantable like security. |

### Communications and countermeasures (Core)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Bug scanner (1-6) | Core | (Rating)R | Rating x 100¥ | Shared procedures → Bug scanner. |
| Data tap | Core | 6R | 300¥ | Shared procedures → Data tap. |
| Headjammer (1-6) | Core | (Rating)R | Rating x 150¥ | Shared procedures → Jammers (head). |
| Jammer, area (1-6) | Core | (Rating x 3)F | Rating x 200¥ | Shared procedures → Jammers. |
| Jammer, directional (1-6) | Core | (Rating x 2)F | Rating x 200¥ | Shared procedures → Jammers. |
| Micro-transceiver | Core | 2 | 100¥ | Voice to chosen micro-transceivers/links within **1 km**; earbud + adhesive subvocal mic. **Wireless:** worldwide range. |
| Tag eraser | Core | 6R | 450¥ | Shared procedures → Tag eraser. |
| White noise generator (1-6) | Core | Rating | Rating x 50¥ | Shared procedures → White noise. |

### Commlink apps (DT; no Avail/Cost table printed)

Run ≤ ceil(DR / 2). Useless for hacking devices/hosts.

| Name | Src | Rules |
| --- | --- | --- |
| AR Games | DT | Casual AR pastimes; huge variety. |
| Diagnostics | DT | PAN device vitals; attack awareness (biomonitor-like for gear). |
| P2.1 | DT | Horizon social-net aggregator; P-Score status. |
| Theme Music | DT | Mood playlist from PAN interaction data. |
| Ticker | DT | Live feed from a topic source; **halves** time for subject-related Matrix Searches. |

(PANICBUTTON! and similar commercial emergency apps: setting/contract; no shop SKU table.)

### Consumer software (Core; not cyberprograms)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Datasoft | Core | 4 | 120¥ | +1 Mental limit on related Knowledge tests. |
| Mapsoft | Core | 4 | 100¥ | Area maps/GPS; wireless self-update (trackable). GM: +1 Navigation limit in covered area. |
| Shopsoft | Core | 4 | 150¥ | Per product type; +1 Social limit on buy/sell Availability/Negotiation for that type. |
| Tutorsoft (1-6) | Core | Rating | Rating x 400¥ | Instruction Tests with pool Rating x 2. Cannot teach Magic/Resonance skills. |

**Pointer:** Agents, common/hacking cyberprograms → Cyberdecks and Programs. Autosofts → Rigger Gear.

### Skillsofts (Core; need cyberware)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Activesoft (1-6) | Core | 8 | Rating x 5,000¥ | Physical Active skills (not Magic/Resonance). Needs **skillwires**. No Edge. |
| Knowsoft (1-6) | Core | 4 | Rating x 2,000¥ | Knowledge skills. Needs **skilljack**. |
| Linguasoft (1-6) | Core | 2 | Rating x 1,000¥ | Language skills. Needs **skilljack**. |

Concurrent softs limited by jack/wires Ratings (Cyberware).

### Electronic parts and Hardware shop stock (DT)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Electronic parts, single pack | DT | - | 250¥ | One device-mod unit. |
| Electronic parts, five-pack | DT | - | 1,000¥ | |
| Hardware kit / shop / facility | Core | - / 8 / 12 | 500 / 5,000 / 50,000¥ | Generic tools (skill = Hardware). Shop ships with **2** packs; facility with **10**. |

Device mods: Shared procedures → Device modification. Deck-only modules (Hardening, etc.) → Cyberdecks file (needed if hardwiring into a device).

### Booster chips (KC; technomancer)

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Attack Booster | KC | 1-2 | - | Rating x 50¥ | Shared → Booster chips. |
| Sleaze Booster | KC | 1-2 | - | Rating x 50¥ | |
| Data Processing Booster | KC | 1-2 | - | Rating x 50¥ | |
| Firewall Booster | KC | 1-2 | - | Rating x 50¥ | |
| Armor Defeating (Attack street) | KC | 3-4 | (Rating x 4)R | Rating x 250¥ | |
| Slick Willy (Sleaze street) | KC | 3-4 | (Rating x 4)R | Rating x 250¥ | |
| Data Dynamo (DP street) | KC | 3-4 | (Rating x 4)R | Rating x 250¥ | |
| Fortified (Firewall street) | KC | 3-4 | (Rating x 4)R | Rating x 250¥ | |

### Booster clouds (KC)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Brute Force | KC | 6R | 250¥ | Shared → Booster cloud. |
| Control Device | KC | 6R | 200¥ | |
| Crack File | KC | 6R | 150¥ | |
| Crash Program | KC | 6R | 150¥ | |
| Data Spike | KC | 8R | 300¥ | |
| Edit File | KC | - | 150¥ | |
| Erase Mark | KC | 6R | 150¥ | |
| Hack on the Fly | KC | 6R | 250¥ | |
| Hide | KC | 6R | 150¥ | |
| Jam Signals | KC | 6R | 150¥ | |
| Matrix Perception | KC | - | 100¥ | |
| Reboot Device | KC | 6R | 250¥ | |
| Snoop | KC | 6R | 200¥ | |
| Spoof Command | KC | 6R | 250¥ | |
| Trace Icon | KC | 8R | 200¥ | |
| Custom Case | KC | 6 | 200¥ | Disguise aerosol housing. |

### Matrix grenades / nanite sprays (KC)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Fuzzy grenade | KC | 10R | 20¥ x Power | Shared → Matrix grenades. Power ≤ 20. |
| CoS grenade | KC | 10R | 500¥ | Shared → Matrix grenades. |
| Douser (1-10) | KC | (Rating x 2)F | Rating x 50¥ | Shared → Matrix grenades. |
| DumDum | KC | (Rating x 2)R | Rating x 50¥ | Shared → Matrix grenades. |

### PI-Tac units (RnG)

| Name | Src | Level | DR | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Renraku Taka | RnG | I | 4 | 12R | 115,000¥ | Shared → PI-Tac Level I. |
| Novatech Tactician | RnG | II | 5 | 18R | 325,000¥ | Shared → PI-Tac Level II. |
| ComPac-Esprit General | RnG | III | 6 | 18F | 855,000¥ | Shared → PI-Tac Level III. |

Optional surplus/refurb (KC): GM may cut price ~25% per lost main feature; repair Hardware/Software + Logic [Mental] (Level x 3) Extended, parts ~2% original +4 Avail; glitches can drop features; +1 box Matrix or physical damage taken.

### Pantheon tac-apps (KC; need PI-Tac)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Co-Pilot MK I | KC | 12R | 400¥ | Level III only. Control target vehicle/drone as remote cold-sim. Pilot skills auto -2 safe / -3 combat. Needs admin + wireless. Incompatible with MK II. |
| Co-Pilot MK II | KC | 12R | 400¥ | Level I/II: control drones as captain's-chair mode. Incompatible with MK I. |
| Co-Pilot MK III | KC | 12R | 400¥ | Access vehicle secondary systems no penalty; assist Pilot at -1. Sole pilot: -3. |
| Door Gunner | KC | 12R | 200¥ | Remotely fire linked powered mounts / launch weapons. No use penalties. Needs smartlink + secure wireless. Not for drones. Needs skill/skillsoft. |
| ECM-Warrior | KC | 12R | 200¥ | +3 all Electronic Warfare tests. |
| Mobile CNC | KC | 12R | 300¥ | Pool of **6** dice for navigation / teamwork / combat maneuvers; allocate across additional operators. +2 vs Noise. |
| Shield Wall | KC | 12R | 200¥ | +3 Firewall on linked cyberdeck vs offensive actions (e.g. Brute Force, Data Spike). |

### PI-Tac / combat electronics accessories (KC)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Tactical Program Dongle (Rating) | KC | 10R | Rating x 200¥ | +1 tac-app beyond Level+2; unload/load tac-app = Free. One dongle per PI-Tac. |
| Mercury-Alpha Battlefield Signal Booster | KC | 12R | 3,500¥ | DR 5. Shared → Mercury-Alpha. |
| Micro-dish transmitter | KC | 10R | 1,200¥ | Mercury-Alpha foldable/detachable dish (sold listed separately). |
| Pantheon Hard Case CCOB | KC | 12R | 1,700¥ | Armor 12 / internal shell **14***; Capacity 8. Drag handle; armored shell for deck/RCC; fiber port; quick-charge battery; 3 micro-hardpoints. Physical protect contents only; armor no stack. |
| Generic CCOB | KC | 10 | 1,000¥ | Armor 8; Capacity 8. Drag handle; micro-hardpoint; weapon holster (SMG/shotgun/AR); quick-access medkit pouch (≤ Rating 4). Armor no stack. |
| Personal Drone Rack | KC | 12R | 500¥ | Mount 3 micro or 1 small drone; needs 1 micro-hardpoint. Also Rigger Gear. |

### Weapon-mounted electronics (RnG; also Weapon Accessories)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Weapon Commlink | RnG | as link | as link + 200¥ | Underslot accessory; weapon hosts PAN. Often paired with personality. Alternate: DT weapon form factor (+4R / +50%). |
| Weapon Personality | RnG | 8 | 250¥ | Metahuman-like chat interface on the gun (hit callouts, etc.). Software personality only. |

### Matrix-related headware (KC; also Cyberware / Bioware)

| Name | Src | Type | Ess | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Datajack Plus (1-3) | KC | Cyber | 0.15 | 4 | Rating x 3,500¥ | Shared → Datajack Plus. |
| EARRS | KC | Cyber | 0.75 | 10R | 30,000¥ | Shared → EARRS. |
| Cranial Shield | KC | Cyber | 0.5 | 12 | 5,000¥ | Shared → Cranial Shield. |
| MCT Biolink | KC | Bio | 0.5 | 10 | 15,000¥ | Shared → Biolink. |

### Related Core/CF installs (pointer rows; full buy often in Cyberware)

| Item | Where | Note |
| --- | --- | --- |
| Implanted commlink | Cyberware | Ess 0.2, Cap [2], +2,000¥ + link; free sim module |
| Datajack (standard) | Cyberware | DNI + cable; wireless Noise Reduction 1 |

### RF PACK notes (composition, not unique SKUs)

| PACK | Cost / Karma | Avail | Contents (component stats above) |
| --- | --- | --- | --- |
| Eavesdropper PACK | 2,000¥ / 1 | 6R | 5 data taps; 5 micro-cameras (1) |
| Jammer PACK | 2,000¥ / 1 | 12F | Area jammer (4); tag eraser; bug scanner (5); white noise generator (5) |

(Surveillance / B&E / Decker PACKs mix sensors, security, and decks → those encyclopedia files.)

### R5 vehicle electronics (pointer)

Satellite Link (vehicle mod): Slots 1, Threshold 6, Kit, Hardware 6, 500¥. Retrans Unit: Slots 2, Threshold 4, Kit, Hardware 8, 4,000¥. Full install rules → Vehicle and Drone Modifications / Rigger Gear. Handheld Core satellite link remains above.

## Item index

**Core links:** Meta Link, Sony Emperor, Renraku Sensei, Erika Elite, Hermes Ikon, Transys Avalon, Fairlight Caliban, Sim module, hot-sim
**DT links:** EvoTech Himitsu, MCT Blue Defender, Nixdorf Sekretär (+ Liebesekretär)
**KC links:** Horizon Flow, Wuxing Frequency, S-K Last Chance
**KC RCC:** Shiawase Cyber-6, Spinrad Global Skirmisher
**Dongles:** Attack, Stealth, Cable tap, Stun, Receiver
**Accessories:** AR Gloves, Biometric reader, Electronic paper, Printer, Satellite link, Simrig, Subvocal mic, Trid projector, Trodes, data cable, Trode Patch, Patch Cover, MOS, Faceless (+ faces)
**RFID:** Standard, Datachip, Security, Sensor, Stealth
**Comms/CM:** Bug scanner, Data tap, Headjammer, Area jammer, Directional jammer, Micro-transceiver, Tag eraser, White noise generator
**Apps:** AR Games, Diagnostics, P2.1, Theme Music, Ticker
**Software:** Datasoft, Mapsoft, Shopsoft, Tutorsoft
**Skillsofts:** Activesoft, Knowsoft, Linguasoft
**Parts:** Single/five pack; Hardware kit/shop/facility; device mods
**Booster chips:** 4 commercial + 4 street
**Booster clouds:** 15 Matrix-action types + Custom Case
**Matrix grenades:** Fuzzy, CoS, Douser, DumDum
**PI-Tac:** Renraku Taka (I), Novatech Tactician (II), ComPac-Esprit General (III)
**Tac-apps:** Co-Pilot MK I/II/III, Door Gunner, ECM-Warrior, Mobile CNC, Shield Wall
**PI-Tac accessories:** Tactical Program Dongle, Mercury-Alpha, Micro-dish, Hard Case CCOB, Generic CCOB, Personal Drone Rack
**Weapon electronics:** Weapon Commlink, Weapon Personality
**Headware:** Datajack Plus, EARRS, Cranial Shield, MCT Biolink
**RF PACKs (notes):** Eavesdropper, Jammer

## Cutting Aces social / fashion electronics

**Verified from:** `Shadowrun_5E_Cutting_Aces.pdf`.

| Name | Avail | Cost | Notes |
| --- | --- | --- | --- |
| AR Nails | 2 | 200¥ | Function as AR gloves. |
| Bug Promotional Pen | 3 | 100¥ | Cap 2 sensors; optional RFID. |
| Chem Detect Nail Polish (R1–4) | Rating | Rating × 50¥ | 10 applications; liquid test. |
| Chemsniffer Ring (R1–6) | 3×Rating | Rating × 250¥ | Inhaled toxins within 1 m. |
| Concealable Surveillance Gear | 6 | 50¥ | Sensor tags in jewelry; Conceal −6. |
| Fashion Gas Mask | 3 | 300¥ | Negates −2 wrong-attire Etiquette. |
| Fashion Respirator (R1–6) | 3 | Rating × 75¥ | Same Etiquette negation. |
| Ghost Box | 6R | 600¥ | Infrasound unease; 10 m. |
| Holo Bracelet | 2 | 250¥ | Rating 3 palm hologram. |
| LRAD | 7 | 400¥ | Cap [3]; focused audio to 100 m. |
| Subliminal Subacoustics | 14F | 1,250¥ | Broadcast mood via speaker; −2 opposed actions; resist Logic+Will (2). |

**Social software subscriptions** (~250¥/month, wireless): CarnivoreGold 10F; MonaLisa 12F; Pheromone Detection 8F; Speech Template Comparison 10F; Target Tracking 5F; Thermal Mood Reading 6F; Vocal Tension Lie Detection 6F.

**Lockdown devices (no street Cost):** MADAR (ranged defense in 0.5 m; Noise −6); Crazy-Repeller (EM field vs ferals; 10 power units; settings 1–6). Prototype / MIT&T only.

