# NOIR - Developer & Executive Guide

**AI-Driven Book Writing System for Swedish Crime Fiction**

---

## 🎯 EXECUTIVE SUMMARY

NOIR är ett systematiskt ramverk för att skriva högkvalitativa spänningsromaner med hjälp av 10 specialiserade AI-agenter som arbetar genom 5 faser - från plot-validering till publiceringsklart manus.

**Resultat:** 80,000-120,000 ord bok, 95%+ faktaverifierad, 0 kontinuitetsfel, bestseller-kvalitet.

**Tid:** 125-210 timmar totalt (motsvarar 3-5 veckors heltidsarbete).

**Inspirerat av:** Beprövad metodik från "Tre år med AI"-projektet (12 kapitel, 77,000 ord, kvalitetsbetyg 8.0-9.8/10).

---

## 🏗️ SYSTEMARKITEKTUR

### Tre-lagers Agent-hierarki

```
┌──────────────────────────────────────────────────────┐
│  FAS 0: NARRATIVE VALIDATION (Författaren godkänner) │
│  - Synopsis, Beat Sheet, Emotional Journey           │
│  - GO/NO-GO beslut innan skrivning börjar            │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│  CREATIVE TEAM (Fas 1: Kreativ Planering)           │
│  ├─ Harper (Plotarkitekt)                           │
│  ├─ Morgan (Karaktärpsykolog)                       │
│  ├─ Quinn (Dialogmästare)                           │
│  └─ River (Miljöspecialist)                         │
│                                                       │
│  Output: Komplett kreativ grund för boken           │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│  WRITING TEAM (Fas 2: Skrivning)                    │
│  ├─ Sage (Huvudförfattare)                          │
│  └─ Blake (Scenbyggare/Polering)                    │
│                                                       │
│  Output: Draft v1 av kapitel                        │
└──────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────┐
│  QUALITY TEAM (Fas 3-4: Revision & QA)              │
│  ├─ Ellis (Utvecklingsredaktör) → Draft v2          │
│  ├─ Finley (Faktaverifierare)                       │
│  ├─ Gray (Kontinuitetsansvarig)                     │
│  └─ Jordan (Spänningsanalytiker)                    │
│                                                       │
│  Output: FINAL (publiceringsklart)                  │
└──────────────────────────────────────────────────────┘
```

---

## 👥 AGENT-SPECIFIKATIONER

### 1. Harper - Plotarkitekt
**Roll:** Skapar treaktstruktur, plot beats, red herrings, spänningskurva
**Specialitet:** Svensk deckartradition (Mankell, Larsson, Läckberg)
**Input:** Plot-intake från författare
**Output:**
- Detaljerad plotstruktur (12-30 kapitel)
- Beat sheet med spänningsnivåer
- Red herrings map
- Foreshadowing plan

**Verktyg:** `read`, `write`, `edit`, `websearch`, `webfetch`, `todowrite`

---

### 2. Morgan - Karaktärpsykolog
**Roll:** Skapar djupa personporträtt, motivationer, character arcs
**Specialitet:** Psykologisk trovärdighet, svenska personlighetstyper
**Input:** Plot-intake, Harpers plotstruktur
**Output:**
- Protagonistprofil (psykologi, backstory, arc)
- Antagonistprofil (komplex motivation)
- Supporting cast profiler
- Relationsdynamik-karta

**Verktyg:** `read`, `write`, `edit`, `websearch`, `todowrite`

---

### 3. Quinn - Dialogmästare
**Roll:** Skapar distinkta röster per karaktär, autentiska svenska dialoger
**Specialitet:** Regional variation, svensk språklig subtilitet, subtext
**Input:** Morgans karaktärsprofiler
**Output:**
- Röstprofil per karaktär (ordval, rytm, dialekt)
- Dialogmallar för scentyper
- Svenska konventioner (du/ni, formality)
- Signaturfraser per karaktär

**Verktyg:** `read`, `write`, `edit`, `websearch`, `todowrite`

---

### 4. River - Miljöspecialist
**Roll:** Researchar och beskriver svenska miljöer, atmosfär
**Specialitet:** Årstider, väder, regional autenticitet
**Input:** Plot-intake, Harpers plotstruktur
**Output:**
- Detaljerad beskrivning av 10-15 nyckelplatser
- Sensoriska detaljer (alla 5 sinnen)
- Väder och årstidstidslinje
- Svenska autenticitet-check

**Verktyg:** `read`, `write`, `edit`, `websearch`, `webfetch`, `todowrite`

---

### 5. Sage - Huvudförfattare
**Roll:** Väver samman allt till färdig prosa
**Specialitet:** Narrativ flow, pacing, stilistisk konsekvens
**Input:** Allt från Creative Team (Harper, Morgan, Quinn, River)
**Output:**
- Draft v1 (4,000-7,000 ord/kapitel)
- Draft v2 (efter Ellis feedback)
- FINAL (efter QA feedback)

**Verktyg:** `read`, `write`, `edit`, `todowrite`

---

### 6. Blake - Scenbyggare
**Roll:** Polerar action-scener, spänningssekvenser
**Specialitet:** Snabb pacing, kinetic language, spatial awareness
**Input:** Sage's draft v1
**Output:**
- Polerade action-scener
- Förbättrad choreografi
- Svenska action-kontext (realistiska vapen/procedurer)

**Verktyg:** `read`, `edit`, `write`, `todowrite`

---

### 7. Ellis - Utvecklingsredaktör
**Roll:** Strukturell redigering, feedback
**Specialitet:** Plot logic, pacing, emotional impact
**Input:** Sage's draft v1
**Output:**
- Utvecklingsredaktion-rapport
- Betyg per metrik (struktur, karaktär, emotion, pacing, show/tell)
- Prioriterad TODO-lista för Sage
- Combined rating X/10

**Verktyg:** `read`, `write`, `todowrite`

---

### 8. Finley - Faktaverifierare
**Roll:** Verifierar all fakta (svenska förhållanden, procedurer, geografi)
**Specialitet:** Polisprocedurer, juridik, svensk kontext
**Input:** Sage's draft v2
**Output:**
- Faktakontroll-rapport
- Kritiska fel (MÅSTE fixas)
- Mindre fel (BORDE fixas)
- 95%+ verifierade claims

**Verktyg:** `read`, `write`, `websearch`, `webfetch`, `todowrite`

---

### 9. Gray - Kontinuitetsansvarig
**Roll:** Spårar allt, säkerställer 0 kontinuitetsfel
**Specialitet:** Karaktärsminne, tidslinje, object tracking
**Input:** Alla FINAL kapitel, kontinuitets-databas
**Output:**
- Kontinuitetsrapport per kapitel
- Uppdaterad kontinuitets-databas
- 0 kontinuitetsfel garanti

**Verktyg:** `read`, `write`, `edit`, `todowrite`

---

### 10. Jordan - Spänningsanalytiker
**Roll:** Maximerar page-turner factor
**Specialitet:** Pacing, hooks, spänningskurva, reader engagement
**Input:** Sage's draft v2
**Output:**
- Spänningsanalys-rapport
- Betyg (opening hook, cliffhanger, stakes, engagement)
- Konkreta förbättringsförslag
- Page-turner verdict

**Verktyg:** `read`, `write`, `todowrite`

---

## 📋 5-FAS PRODUKTIONSPROCESS

### **FAS 0: NARRATIVE VALIDATION** 🆕
**Tid:** 3-5 timmar (kan itereras)
**Syfte:** Validera berättelsen INNAN skrivning börjar
**Agenter:** Harper + Morgan

**Process:**
1. Författaren fyller i `plot-intake.md`
2. Harper skapar:
   - Full synopsis (5-10 sidor)
   - Beat sheet med spänningskurva
   - Twist validation
3. Morgan skapar:
   - Emotional journey map
   - Character arc visualization
4. **FÖRFATTAREN GODKÄNNER:**
   - ✅ GO → Fortsätt till Fas 1
   - 🔄 REVISE → Justera plot-intake → Kör Fas 0 igen
   - ❌ NO-GO → Ny idé behövs

**Output:**
- `phase0/synopsis.md`
- `phase0/beat-sheet.md`
- `phase0/emotional-journey.md`
- `phase0/character-arcs.md`
- `phase0/author-approval.md`

**Kvalitetskontroll:**
- [ ] Spänningskurva är dynamisk
- [ ] Character arc är övertygande
- [ ] Twist är shocking men logisk
- [ ] Emotional payoff finns
- [ ] Berättelsen kan sälja

---

### **FAS 1: KREATIV PLANERING**
**Tid:** 3-5 timmar (engångskostnad för hela boken)
**Syfte:** Skapa komplett kreativ grund
**Agenter:** Harper, Morgan, Quinn, River (parallellt)

**Process:**
1. **Harper** skapar plotstruktur baserat på godkänd Fas 0
2. **Morgan** utvecklar karaktärsprofiler (baserat på Fas 0 arcs)
3. **Quinn** skapar dialogguider (behöver Morgans profiler)
4. **River** researchar miljöer (behöver Harpers plotstruktur)

**Output:**
- `plot/plotstruktur.md` (Harper)
- `characters/protagonist.md`, `antagonist.md`, `supporting-cast.md` (Morgan)
- `characters/dialogue-guides.md` (Quinn)
- `research/miljöguide.md` (River)

**Kvalitetskontroll:**
- [ ] Plotstruktur är balanserad (Akt I: 25%, II: 50%, III: 25%)
- [ ] Alla huvudkaraktärer har djupa profiler
- [ ] Varje karaktär har distinkt röst
- [ ] Alla viktiga platser är detaljerade

---

### **FAS 2: SKRIVNING** (per kapitel)
**Tid:** 6-10 timmar per kapitel
**Syfte:** Producera draft v1
**Agenter:** Sage + Blake

**Process:**
1. **Sage** läser allt material från Fas 1 (30 min)
2. **Sage** planerar kapitlet (scene list, hooks) (30-60 min)
3. **Sage** skriver draft v1 (4-6 timmar)
4. **Blake** identifierar och polerar action-scener (1-2 timmar)
5. **Sage** integrerar Blakes förbättringar (30 min)

**Output:**
- `chapters/chapter-XX/draft-v1.md`

**Kvalitetskontroll:**
- [ ] Alla plot points från Harper täckta
- [ ] Karaktärer agerar enligt Morgan
- [ ] Dialog följer Quinn
- [ ] Miljöer från River integrerade
- [ ] Opening hook är stark (Jordan skulle ge 7+/10)
- [ ] Ending hook driver till nästa kapitel
- [ ] Ordantal: 4,000-7,000 ord (traditionell) eller 2,500-4,000 (modern momentum)

---

### **FAS 3: STRUKTURELL REVISION** (per kapitel)
**Tid:** 2-3 timmar per kapitel
**Syfte:** Förbättra struktur och kvalitet
**Agenter:** Ellis → Sage

**Process:**
1. **Ellis** granskar draft v1 (1-1.5 timmar)
   - Strukturell kvalitet
   - Karaktärsutveckling
   - Emotionell impact
   - Pacing
   - Show vs Tell
2. **Sage** läser feedback (15 min)
3. **Sage** reviderar till draft v2 (1-1.5 timmar)

**Output:**
- `chapters/chapter-XX/ellis-review.md`
- `chapters/chapter-XX/draft-v2.md`

**Kvalitetskontroll:**
- [ ] Combined rating förbättrats (typiskt +0.3-0.5 poäng)
- [ ] Alla MÅSTE-fixes från Ellis gjorda
- [ ] Strukturella problem lösta

---

### **FAS 4: KVALITETSSÄKRING** (per kapitel)
**Tid:** 2-3 timmar per kapitel
**Syfte:** Finalpolering till publiceringsstandard
**Agenter:** Finley + Gray + Jordan (parallellt) → Sage

**Process:**
1. **Finley, Gray, Jordan** granskar draft v2 parallellt (1-2 timmar)
   - Finley: Faktaverifiering
   - Gray: Kontinuitet
   - Jordan: Spänning och engagement
2. **Sage** läser alla tre rapporter (30 min)
3. **Sage** skapar FINAL med alla fixes (1 timme)

**Output:**
- `chapters/chapter-XX/finley-faktakontroll.md`
- `chapters/chapter-XX/gray-kontinuitet.md`
- `chapters/chapter-XX/jordan-spanningsanalys.md`
- `chapters/chapter-XX/FINAL.md`

**Kvalitetskontroll:**
- [ ] 95%+ faktaverifierade påståenden
- [ ] 0 kritiska faktafel
- [ ] 0 kontinuitetsfel
- [ ] Spänningskurva dynamisk
- [ ] Opening hook minst 7/10
- [ ] Combined quality rating minst 8.0/10
- [ ] **PUBLICERINGSKLART**

---

## 📊 DATAFLÖDE & SAMARBETE

### Agent-dependencies (i vilken ordning körs de)

```
FAS 0:
  Harper (solo) ─┐
                 ├─→ Författaren godkänner
  Morgan (solo) ─┘

FAS 1:
  Harper (solo) ──────────┐
                          ├─→ Sage kan börja skriva
  Morgan (solo) ──┐       │
                  │       │
  Quinn (behöver Morgan) ─┤
                          │
  River (behöver Harper) ─┘

FAS 2:
  Sage (behöver allt från Fas 1) ──→ Draft v1
                                      │
  Blake (behöver Sage v1) ───────────┘

FAS 3:
  Ellis (behöver Sage v1) ──→ Feedback
                               │
  Sage (behöver Ellis) ────────┘ → Draft v2

FAS 4:
  Finley (behöver Sage v2) ─┐
  Gray (behöver Sage v2) ───┼─→ Sage (behöver alla tre) → FINAL
  Jordan (behöver Sage v2) ─┘
```

### Kontinuitets-databas (Gray's persistence layer)

```
gray_continuity_db/
├── characters.md          # Master character tracking
├── plot_events.md         # All events chronologically
├── objects.md             # Important object tracking
├── timeline.md            # Date/time consistency
├── places.md              # Location consistency
└── established_facts.md   # All facts stated in book

Uppdateras: Efter varje kapitel FINAL
Används av: Gray (kontinuitets-check), Finley (fakta-check)
```

---

## 🎯 KVALITETSMETRIKER & KPI:er

### Per kapitel (FINAL):
- **Faktaverifiering:** ≥95% claims verifierade
- **Kritiska faktafel:** 0
- **Kontinuitetsfel:** 0
- **Opening hook rating:** ≥7/10
- **Cliffhanger rating:** ≥7/10 (utom sista kapitlet)
- **Spänningskurva:** Dynamisk (inte platt)
- **Combined quality rating:** ≥8.0/10

### Hela boken:
- **Ordantal:** 80,000-120,000 ord
- **Kapitel:** 12-30 (beroende på momentum-strategi)
- **Konsistent kvalitet:** Alla kapitel ≥8.0/10
- **Svensk autenticitet:** 100% (inga amerikanismer, korrekta procedurer)
- **Diversitet:** Balanserad representation (kön, region, generation)

---

## 🔧 TEKNISK IMPLEMENTATION

### Verktyg som agenter använder:

Alla agenter har tillgång till:
- `bash` - Systemkommandon
- `read` - Läsa filer
- `write` - Skapa nya filer
- `edit` - Redigera befintliga filer
- `task` - Delegera till andra agenter (för coordination)
- `todowrite` - Spåra arbetsuppgifter
- `webfetch` - Hämta från specifika URLs
- `websearch` - Allmän research

### Filstruktur per bokprojekt:

```
books/[book-name]/
├── phase0/                    # Narrative validation
│   ├── synopsis.md
│   ├── beat-sheet.md
│   ├── emotional-journey.md
│   ├── character-arcs.md
│   └── author-approval.md
├── plot/                      # Fas 1: Harper
│   └── plotstruktur.md
├── characters/                # Fas 1: Morgan + Quinn
│   ├── protagonist.md
│   ├── antagonist.md
│   ├── supporting-cast.md
│   └── dialogue-guides.md
├── research/                  # Fas 1: River
│   └── miljöguide.md
├── chapters/                  # Fas 2-4: Per kapitel
│   ├── chapter-01/
│   │   ├── draft-v1.md
│   │   ├── ellis-review.md
│   │   ├── draft-v2.md
│   │   ├── finley-faktakontroll.md
│   │   ├── gray-kontinuitet.md
│   │   ├── jordan-spanningsanalys.md
│   │   └── FINAL.md
│   └── chapter-02/
│       └── [samma struktur...]
└── tracking/                  # Gray's kontinuitets-databas
    ├── continuity-db.md
    ├── timeline.md
    └── character-tracking.md
```

---

## 📈 PRODUKTIONSMETRIKER

### Tidsutnyttjande per bok (12 kapitel, 80,000 ord):

| Fas | Tid | Kostnad per kapitel | Total |
|-----|-----|---------------------|-------|
| **Fas 0** | 3-5 timmar | Engångskostnad | 3-5 timmar |
| **Fas 1** | 3-5 timmar | Engångskostnad | 3-5 timmar |
| **Fas 2** | 6-10 timmar | Per kapitel | 72-120 timmar |
| **Fas 3** | 2-3 timmar | Per kapitel | 24-36 timmar |
| **Fas 4** | 2-3 timmar | Per kapitel | 24-36 timmar |
| **TOTAL** | | | **126-202 timmar** |

**Per vecka (40 timmar):** 3-5 veckor heltidsarbete

### Kvalitetsutveckling genom process:

| Version | Typiskt rating | Vad som åtgärdats |
|---------|----------------|-------------------|
| Draft v1 | 7.0-7.5/10 | Grundberättelse täcker plot |
| Draft v2 | 7.5-8.5/10 | Struktur, pacing, emotion förbättrat |
| FINAL | 8.0-9.0/10 | Fakta, kontinuitet, spänning optimerat |

**Total förbättring:** +1.0-1.5 poäng från v1 till FINAL

---

## 🔄 ITERATION & KALIBRERING

### Om output inte når kvalitetsmål:

**Problem:** Ellis ger rating <6.0/10 på draft v1

**Lösning:**
1. Identifiera specifika problem (struktur? pacing? show/tell?)
2. Justera Sage's instruktioner eller ge mer explicit guidance
3. Kör om Fas 2 för det kapitlet
4. Om systematiskt problem: Justera Creative Team output (Fas 1)

**Problem:** Finley hittar många faktafel (>5 kritiska)

**Lösning:**
1. Förstärk Finley's research-källor
2. Lägg till specifik svensk-kontext guidance för Sage
3. Skapa checklista för vanliga svenska fel (polisprocedurer, geografi)

**Problem:** Gray hittar kontinuitetsfel

**Lösning:**
1. Verifiera att Gray uppdaterar kontinuitets-databas efter varje kapitel
2. Säkerställ att Sage läser kontinuitets-databas innan nytt kapitel
3. Om systematiskt: Implementera stronger tracking-system

---

## 🎯 SUCCESS-KRITERIER

**Projektet är framgångsrikt om:**
1. ✅ Fas 0 godkänns av författaren (berättelsen fungerar)
2. ✅ Alla kapitel når ≥8.0/10 i FINAL
3. ✅ 95%+ faktaverifierade påståenden
4. ✅ 0 kontinuitetsfel i publicerad version
5. ✅ Boken känns autentiskt svensk
6. ✅ Spänningskurva gör boken till page-turner
7. ✅ Färdig inom 125-210 timmar
8. ✅ Författaren är NÖJD med resultatet

---

## 🚀 IMPLEMENTATIONSSTRATEGI

### Fas 1: Proof of Concept (1 vecka)
1. Implementera Fas 0 (Narrative Validation)
2. Testa på EN bokidé
3. Validera att Harper + Morgan kan producera quality synopsis och beat sheet
4. **GO/NO-GO beslut:** Fungerar Fas 0?

### Fas 2: Pilot Chapter (1 vecka)
1. Implementera Fas 1-4 för ETT kapitel
2. Kör genom hela processen (v1 → v2 → FINAL)
3. Mät kvalitet (når vi ≥8.0/10?)
4. **GO/NO-GO beslut:** Når vi quality targets?

### Fas 3: Three-Chapter Test (2 veckor)
1. Skriv Kapitel 1, 6 (midpoint), och 11 (climax)
2. Validera momentum, pacing, character arcs
3. Testa Gray's kontinuitetsspårning över flera kapitel
4. **GO/NO-GO beslut:** Skalbart till hela boken?

### Fas 4: Full Production (3-5 veckor)
1. Skriv alla 12 kapitel
2. Final assembly och book-wide QA
3. **KLAR FÖR PUBLICERING**

---

## 📚 SKALBARHET & ÅTERANVÄNDNING

**Systemet är designat för att skriva FLERA böcker:**

**Bok 1:** Initialt upplägg tar 126-202 timmar
**Bok 2:** Med justerade agents/workflows: 100-150 timmar
**Bok 3+:** Optimerat system: 80-120 timmar

**Varför snabbare:**
- Agenter lär sig från tidigare böcker
- Workflows är finslipade
- Författaren vet vad som fungerar
- Templates är beprövade

---

## 🎓 LÄRDOMAR FRÅN "TRE ÅR MED AI"-PROJEKTET

Systemet bygger på beprövad metodik:
- ✅ 4-fas process fungerar (research → writing → revision → QA)
- ✅ Specialized agents levererar bättre än general-purpose
- ✅ Kvalitet ökar konsekvent genom faserna (+0.5-1.5 poäng)
- ✅ Faktaverifiering och kontinuitet är KRITISKT för trovärdighet
- ✅ 95%+ verifierade claims är uppnåeligt
- ✅ Svenska kontext kräver dedicated focus (inte default-US)

**NYA tillägg i NOIR:**
- 🆕 Fas 0: Narrative Validation (learn before you write)
- 🆕 Blake: Action scene specialist (genre-specifikt)
- 🆕 Jordan: Tension analyzer (page-turner optimization)
- 🆕 Flexible chapter structure (momentum-optimization)

---

## 📞 SUPPORT & DOKUMENTATION

**Fullständig dokumentation:**
- `README.md` - Översikt av systemet
- `QUICKSTART.md` - Snabbstartguide för författare
- `DEVELOPER_GUIDE.md` - Denna fil (teknisk + executive)
- `agents/*/` - Detaljerade agent-instruktioner
- `workflows/*/` - Steg-för-steg process-guides
- `templates/*/` - Återanvändbara mallar

**Agent-filer:**
- `agents/creative/harper.md` - Plotarkitekt-spec
- `agents/creative/morgan.md` - Karaktärpsykolog-spec
- `agents/creative/quinn.md` - Dialogmästare-spec
- `agents/creative/river.md` - Miljöspecialist-spec
- `agents/writing/sage.md` - Huvudförfattare-spec
- `agents/writing/blake.md` - Scenbyggare-spec
- `agents/quality/ellis.md` - Utvecklingsredaktör-spec
- `agents/quality/finley.md` - Faktaverifierare-spec
- `agents/quality/gray.md` - Kontinuitetsansvarig-spec
- `agents/quality/jordan.md` - Spänningsanalytiker-spec

---

## 🎯 KONKURRENSFÖRDELAR

**Vad gör NOIR unikt:**
1. **Svensk fokus:** Inte US-centrisk (deckare-tradition, svenska förhållanden)
2. **Beprövad metodik:** Baserat på 77,000-ord lyckad bok
3. **10 specialized agents:** Inte general-purpose (varje agent expert på sitt)
4. **Narrative validation först:** Validerar story innan skrivning (sparar 100+ timmar)
5. **Quality gates:** Systematisk kvalitetssäkring varje fas
6. **Återanvändbart:** Skriv flera böcker med samma system
7. **Transparent process:** Författaren ser och godkänner varje steg

---

## 🚀 NEXT STEPS

**För att börja använda NOIR:**
1. Klona repository
2. Läs `QUICKSTART.md`
3. Fyll i `templates/plot-intake.md`
4. Kör Fas 0 (Narrative Validation)
5. Om godkänd → Kör Fas 1-4
6. **Skriv din bok!**

---

**Version:** 1.0.0
**Datum:** 2025-11-06
**Licens:** Öppen källkod
**Skapat med:** Claude Code + AI Subagents

---

**För utvecklare: Detta system demonstrerar hur specialiserade AI-agenter kan samarbeta i en strukturerad workflow för att producera högkvalitativt kreativt innehåll med konsistent kvalitet och verifierbarhet.**
