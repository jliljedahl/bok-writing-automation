# NOIR - Novel Orchestration & Intelligent Rendering

Ett professionellt AI-drivet bokskrivningssystem för spänningsromaner och deckare.

## 🎯 Projektöversikt

NOIR är ett återanvändbart ramverk för att skriva högkvalitativa spänningsromaner med hjälp av AI-subagenter. Systemet är inspirerat av svenska deckarförfattare och bygger på beprövad metodologi från "Tre år med AI"-projektet.

## 📚 Status

**Version:** 1.0.0 (Beta)
**Datum:** 2025-11-05
**Typ:** Spänningsroman/Deckare-system

## 🏗️ Arkitektur

### Tre-lagers Agentstruktur

```
┌─────────────────────────────────────────────────────┐
│           CREATIVE TEAM (Kreativt lag)              │
│  - Harper (Plotarkitekt)                            │
│  - Morgan (Karaktärpsykolog)                        │
│  - Quinn (Dialogmästare)                            │
│  - River (Miljöspecialist)                          │
├─────────────────────────────────────────────────────┤
│           WRITING TEAM (Skrivlag)                   │
│  - Sage (Huvudförfattare)                           │
│  - Blake (Scenbyggare)                              │
├─────────────────────────────────────────────────────┤
│           QUALITY TEAM (Kvalitetslag)               │
│  - Ellis (Utvecklingsredaktör)                      │
│  - Finley (Faktaverifierare)                        │
│  - Gray (Kontinuitetsansvarig)                      │
│  - Jordan (Spänningsanalytiker)                     │
└─────────────────────────────────────────────────────┘
```

## 🎭 Specialiserade Agenter

### CREATIVE TEAM

#### Harper (Plotarkitekt)
- **Roll:** Treaktstruktur, plot twists, red herrings, upplösning
- **Specialitet:** Svensk deckartradition (Mankell, Larsson, Läckberg)
- **Output:** Detaljerad kapitelstruktur, spänningskurva, plotpunkter

#### Morgan (Karaktärpsykolog)
- **Roll:** Djupa personporträtt, bakgrundshistorier, karaktärsutveckling
- **Specialitet:** Psychologisk trovärdighet, motivationer, inre konflikter
- **Output:** Karaktärprofiler, relationsdynamik, utvecklingsarcs

#### Quinn (Dialogmästare)
- **Roll:** Autentiska dialoger, svenska dialekter, röstkaraktär
- **Specialitet:** Regionala variationer, sociala koder, subtext
- **Output:** Dialogmallar, röstguider per karaktär

#### River (Miljöspecialist)
- **Roll:** Autentiska svenska miljöer, atmosfär, setting
- **Specialitet:** Research om specifika platser, väderbeskrivningar, lokalhistoria
- **Output:** Detaljerade miljöbeskrivningar, platsrecherche

### WRITING TEAM

#### Sage (Huvudförfattare)
- **Roll:** Väver samman allt till färdig prosa
- **Specialitet:** Narrativ flow, pacing, stilistisk konsekvens
- **Output:** Draft-versioner av kapitel

#### Blake (Scenbyggare)
- **Roll:** Action-sekvenser, spänningsscener, takt
- **Specialitet:** Visuellt berättande, sensoriska detaljer
- **Output:** Polerade actionscener, höjdpunkter

### QUALITY TEAM

#### Ellis (Utvecklingsredaktör)
- **Roll:** Strukturell redigering, narrativ kvalitet, pacing
- **Specialitet:** Story arcs, plotlogik, emotionell impact
- **Output:** Strukturella granskningar, förbättringsförslag

#### Finley (Faktaverifierare)
- **Roll:** Kontrollerar all fakta (platser, tidslinje, kriminaltekniska detaljer)
- **Specialitet:** Svenska förhållanden, polisprocedurer, rättsväsende
- **Output:** Faktakontrollrapporter, källförteckning

#### Gray (Kontinuitetsansvarig)
- **Roll:** Kontinuitet, karaktärsminne, plotkonsistens
- **Specialitet:** Tracking av alla detaljer genom hela boken
- **Output:** Kontinuitetsrapporter, karaktärspårning

#### Jordan (Spänningsanalytiker)
- **Roll:** Analyserar spänningskurva, pacing, hooks
- **Specialitet:** Reader engagement, sidvändartakt
- **Output:** Spänningsanalyser, pacing-grafer

## 🔄 4-Fas Produktionsprocess

### Fas 1: KREATIV PLANERING (Parallel)
**Agenter:** Harper, Morgan, Quinn, River
**Tid:** 3-5 timmar
**Output:**
- Detaljerad plotstruktur (Harper)
- Karaktärprofiler (Morgan)
- Dialogguider (Quinn)
- Miljöbeskrivningar (River)

### Fas 2: SKRIVNING
**Agenter:** Sage, Blake
**Tid:** 6-10 timmar per kapitel
**Output:**
- Draft v1 (Sage)
- Polerade actionscener (Blake)

### Fas 3: STRUKTURELL REVISION
**Agenter:** Ellis → Sage
**Tid:** 2-3 timmar
**Output:**
- Strukturell granskning (Ellis)
- Draft v2 med förbättringar (Sage)

### Fas 4: KVALITETSSÄKRING
**Agenter:** Finley, Gray, Jordan → Sage
**Tid:** 2-3 timmar
**Output:**
- Faktakontroll (Finley)
- Kontinuitetskontroll (Gray)
- Spänningsanalys (Jordan)
- FINAL draft (Sage)

## 📖 Bokstruktur

### Standard Deckare/Thriller-struktur

```
Prolog (valfritt)
├── Hook (första 3 sidor)
├── Offerscen eller mysterium-setup
└── Ton och atmosfär

Akt I: SETUP (25%)
├── Protagonist introduceras
├── Normal värld etableras
├── Inciting incident (10%)
├── Centralt mysterium presenteras
└── Stakes etableras

Akt II: KONFRONTATION (50%)
├── Investigation och discovery
├── Falskt spår (red herrings)
├── Relationer fördjupas
├── Midpoint twist (50%)
├── Protagonist under press
├── Darkest moment (75%)
└── All is lost moment

Akt III: RESOLUTION (25%)
├── Genombrott i fallet
├── Climax-konfrontation
├── Twist reveal
├── Emotionell upplösning
└── Ny normalitet

Epilog (valfritt)
└── Vad hände sedan
```

## 🛠️ Verktyg för Agenter

Alla agenter har tillgång till:
- `bash` - För systemkommandon
- `read` - För att läsa filer
- `write` - För att skapa nya filer
- `edit` - För att redigera befintliga filer
- `multiedit` - För att göra flera ändringar samtidigt
- `task` - För att delegera till andra agenter
- `todowrite` - För att spåra uppgifter
- `webfetch` - För research från specifika URLs
- `websearch` - För allmän research

## 📁 Projektstruktur

```
noir-system/
├── agents/                    # Agent-definitioner
│   ├── creative/
│   │   ├── harper.md         # Plotarkitekt
│   │   ├── morgan.md         # Karaktärpsykolog
│   │   ├── quinn.md          # Dialogmästare
│   │   └── river.md          # Miljöspecialist
│   ├── writing/
│   │   ├── sage.md           # Huvudförfattare
│   │   └── blake.md          # Scenbyggare
│   └── quality/
│       ├── ellis.md          # Utvecklingsredaktör
│       ├── finley.md         # Faktaverifierare
│       ├── gray.md           # Kontinuitetsansvarig
│       └── jordan.md         # Spänningsanalytiker
├── templates/                 # Mallar
│   ├── plot-intake.md        # Plot intake-formulär
│   ├── character-profile.md  # Karaktärsmall
│   ├── chapter-template.md   # Kapitelmall
│   └── scene-template.md     # Scenmall
├── workflows/                 # Arbetsflöden
│   ├── phase1-creative.md    # Kreativ planering
│   ├── phase2-writing.md     # Skrivfas
│   ├── phase3-revision.md    # Revision
│   └── phase4-qa.md          # Kvalitetssäkring
├── books/                     # Bokprojekt
│   └── [book-name]/
│       ├── plot/             # Plotdokumentation
│       ├── characters/       # Karaktärsprofiler
│       ├── research/         # Research-material
│       ├── chapters/         # Kapitel
│       │   ├── chapter-01/
│       │   │   ├── draft-v1.md
│       │   │   ├── draft-v2.md
│       │   │   ├── final.md
│       │   │   └── reviews/
│       │   └── chapter-02/
│       └── tracking/         # Spårning
│           ├── continuity.md
│           ├── timeline.md
│           └── tension-graph.md
└── docs/                      # Dokumentation
    ├── agent-guide.md        # Guide för att använda agenter
    ├── svenska-deckare.md    # Svensk deckartradition
    └── best-practices.md     # Best practices
```

## 🚀 Snabbstart

### 1. Starta ett nytt bokprojekt

```bash
# Navigera till books-mappen
cd books

# Skapa nytt projekt
mkdir min-bok && cd min-bok

# Kopiera plot-intake-mallen
cp ../../templates/plot-intake.md plot/plot-intake.md

# Fyll i plotten
# Beskriv: genre, protagonist, antagonist, central konflikt,
# setting, twist, upplösning
```

### 2. Fas 1 - Kreativ planering

Kör alla kreativa agenter parallellt:

```
Harper skapar plotstruktur baserat på din plot
Morgan utvecklar djupa karaktärsprofiler
Quinn designar unika dialogstilar per karaktär
River researchar autentiska svenska miljöer
```

### 3. Fas 2-4 - Skriv boken

För varje kapitel:
1. **Skriv:** Sage + Blake producerar draft v1
2. **Revidera:** Ellis granskar → Sage skapar v2
3. **QA:** Finley + Gray + Jordan granskar → Sage skapar FINAL

### 4. Publicera

Sammanställ alla FINAL-kapitel till färdig bok!

## 🎯 Kvalitetsmål

- ✅ **Faktaverifiering:** 95%+ claims verifierade
- ✅ **Kontinuitet:** 0 kontinuitetsfel
- ✅ **Spänning:** Konsekvent pacing, hooks varje kapitel
- ✅ **Karaktärer:** Trovärdiga, utvecklade arcs
- ✅ **Svenska kontext:** Autentiska miljöer och dialoger
- ✅ **Plot:** Logisk, överraskande twist, tillfredsställande upplösning

## 🇸🇪 Svensk Deckartradition

Systemet är inspirerat av:
- **Henning Mankell:** Samhällskritik, melankolisk ton, Wallander
- **Stieg Larsson:** Komplex plot, starka kvinnliga karaktärer
- **Camilla Läckberg:** Små samhällen, mörka hemligheter
- **Arne Dahl:** Ensemble cast, internationell räckvidd
- **Viveca Sten:** Skärgårdsmiljöer, realistiska polisprocedurer

## 📊 Produktionsmetriker

**Per kapitel:**
- Kreativ planering: 0.5-1 timme (amorterat)
- Skrivning: 6-10 timmar
- Revision: 2-3 timmar
- QA: 2-3 timmar
- **Total:** 10-17 timmar per kapitel

**Hel bok (12-15 kapitel):**
- Initial kreativ planering: 3-5 timmar
- Skrivning: 120-200 timmar
- **Total:** 125-210 timmar

## 🔧 Teknisk Stack

- **Plattform:** Claude Code + Agent SDK
- **Modell:** Claude Sonnet 4.5
- **Verktyg:** bash, read, write, edit, task, todowrite, webfetch, websearch
- **Format:** Markdown för all text
- **Versionskontroll:** Git + GitHub

## 📝 Licens

Detta projekt är öppen källkod och kan användas för att skapa nya bokprojekt.

---

**Skapat med:** Claude Code + AI Subagents
**Version:** 1.0.0 Beta
**Datum:** 2025-11-05


---

**Senaste uppdatering:** 2025-11-06
**Git Credentials:** Configured with credential helper
