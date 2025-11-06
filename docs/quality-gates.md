# QUALITY GATES SYSTEM

**Syfte:** Säkerställ att varje fas når minimum kvalitetsnivå innan nästa fas börjar.

---

## 🎯 VARFÖR QUALITY GATES?

**Problemet:**
- Agent producerar output, men är det BRA NOG?
- Hur vet vi om vi ska fortsätta eller göra om?
- När är "godkänt" vs "excellent"?

**Lösningen:**
Quality Gates = Minimum acceptable scores som MÅSTE uppnås innan nästa fas.

---

## 📊 QUALITY GATES PER FAS

### **GATE 0: NARRATIVE VALIDATION (Fas 0)**

**Syfte:** Författaren godkänner berättelsen innan skrivning.

#### Minimum kriterier (alla MÅSTE vara JA):

| Kriterie | Minimum | Hur bedöms? |
|----------|---------|-------------|
| **Spänningskurva är dynamisk** | JA | Varierar mellan 3-10, inte platt |
| **Character arc är övertygande** | JA | Transformation motiverad av events |
| **Twist är shocking MEN logisk** | JA | Överraskande + hintat tidigt |
| **Emotional payoff finns** | JA | Tillfredsställande resolution |
| **Författaren är EXCITED** | JA | "Jag vill skriva detta!" |
| **Marketability: Kan sälja?** | JA | Comp titles finns, unique hook |

**BESLUT:**
- ✅ **ALLA JA** → GO till Fas 1
- ⚠️ **1-2 NEJ** → REVISE plot-intake → Kör Fas 0 igen
- ❌ **3+ NEJ** → NO-GO, ny idé behövs

**Dokumentation:**
`phase0/quality-gate-0.md` - Författaren fyller i checklista

---

### **GATE 1: CREATIVE PLANNING (Fas 1)**

**Syfte:** Creative Team har producerat användbart material för skrivning.

#### Harper (Plotarkitekt) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Plotstruktur är balanserad** | 7/10 | 9/10 | Akt I: 25%, II: 50%, III: 25% |
| **Alla beats identifierade** | 100% | 100% | 15-25 plot beats mappade |
| **Spänningskurva varierar** | 7/10 | 9/10 | Inte platt, bygger mot climax |
| **Red herrings är trovärdiga** | 7/10 | 9/10 | Leder fel men logiskt |

**Harper MÅSTE uppnå:** ≥7/10 på alla metrics

---

#### Morgan (Karaktärpsykolog) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Protagonist har tydlig arc** | 8/10 | 10/10 | Start → transformation → end |
| **Antagonist är komplex** | 7/10 | 9/10 | Motivation logisk, något sympatiskt |
| **Alla karaktärer är distinkta** | 7/10 | 9/10 | Unika personligheter, inte stereotyper |
| **Backstories är etablerade** | 100% | 100% | Alla huvudkaraktärer har Ghost/trauma |

**Morgan MÅSTE uppnå:** ≥7/10 på alla metrics

---

#### Quinn (Dialogmästare) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Varje karaktär har distinkt röst** | 8/10 | 10/10 | Kan identifiera vem som pratar |
| **Svenska dialekter är korrekta** | 9/10 | 10/10 | Autentiska, inte stereotyper |
| **Subtext-tekniker finns** | 7/10 | 9/10 | Vad INTE sägs är lika viktigt |

**Quinn MÅSTE uppnå:** ≥7/10 på alla metrics

---

#### River (Miljöspecialist) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Alla nyckelplatser detaljerade** | 100% | 100% | 10-15 platser med sensoriska detaljer |
| **Svensk autenticitet** | 9/10 | 10/10 | Känns äkta svenskt |
| **Årstid/väder konsistent** | 100% | 100% | Tidslinje stämmer |

**River MÅSTE uppnå:** ≥9/10 på svenska autenticitet

---

**GATE 1 BESLUT:**
- ✅ **Alla agents ≥ minimum** → GO till Fas 2
- ⚠️ **1 agent < minimum** → Den agenten kör om
- ❌ **2+ agents < minimum** → Revidera plot-intake → Kör Fas 1 igen

**Dokumentation:**
`phase1/quality-gate-1.md` - Scorecards per agent

---

### **GATE 2: WRITING (Fas 2) - Per kapitel**

**Syfte:** Draft v1 når minimum kvalitet innan Ellis revision.

#### Sage (Huvudförfattare) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Alla plot points täckta** | 100% | 100% | Checklista från Harper |
| **Karaktärer agerar enligt profil** | 8/10 | 10/10 | Konsistent med Morgan |
| **Dialog följer röstguider** | 8/10 | 10/10 | Konsistent med Quinn |
| **Miljöer integrerade** | 8/10 | 10/10 | River's beskrivningar använda |
| **Opening hook är stark** | 7/10 | 9/10 | Fångar inom första stycket |
| **Ending hook driver framåt** | 7/10 | 9/10 | Cliffhanger eller stark closure |
| **Pacing varierar** | 7/10 | 9/10 | Inte monotont |
| **Show > Tell** | 7/10 | 9/10 | Visar genom handling |
| **Ordantal inom range** | JA | JA | 2,500-7,000 ord (beroende på strategi) |

**Sage MÅSTE uppnå:** ≥7/10 på alla subjektiva metrics + 100% på objektiva

---

#### Blake (Scenbyggare) - Minimum scores:

| Metric | Minimum | Excellent | Hur bedöms? |
|--------|---------|-----------|-------------|
| **Action-scener är polerade** | 8/10 | 10/10 | Tydlig choreografi, snabbt tempo |
| **Svensk kontext korrekt** | 9/10 | 10/10 | Realistiska vapen/procedurer |
| **Spatial awareness tydlig** | 8/10 | 10/10 | Vet var alla är |

**Blake MÅSTE uppnå:** ≥8/10 på alla metrics

---

**GATE 2 BESLUT:**
- ✅ **Sage + Blake ≥ minimum** → GO till Fas 3 (Ellis review)
- ⚠️ **Sage < minimum på 1-2 metrics** → Revidera dessa delar → Re-check
- ❌ **Sage < minimum på 3+ metrics** → Skriv om kapitlet

**Dokumentation:**
`chapters/chapter-XX/quality-gate-2.md`

---

### **GATE 3: REVISION (Fas 3) - Per kapitel**

**Syfte:** Draft v2 når högre kvalitet efter Ellis feedback.

#### Ellis (Utvecklingsredaktör) - Ratings:

| Metric | Minimum v2 | Excellent | Förbättring från v1 |
|--------|-----------|-----------|---------------------|
| **Strukturell kvalitet** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |
| **Karaktärsutveckling** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |
| **Emotionell impact** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |
| **Pacing** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |
| **Show vs Tell balance** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |
| **Combined rating** | 7.5/10 | 9/10 | +0.3-0.5 från v1 |

**Ellis + Sage MÅSTE uppnå:**
- v2 combined rating ≥7.5/10
- Förbättring från v1: +0.3 minimum

---

**GATE 3 BESLUT:**
- ✅ **v2 ≥ 7.5/10 + förbättring ≥0.3** → GO till Fas 4 (QA)
- ⚠️ **v2 = 7.0-7.4/10** → Targeted revision på svagaste areas → Re-check
- ❌ **v2 < 7.0/10** → Major rewrite behövs

**Dokumentation:**
`chapters/chapter-XX/quality-gate-3.md`

---

### **GATE 4: QUALITY ASSURANCE (Fas 4) - Per kapitel**

**Syfte:** FINAL når publiceringsstandard.

#### Finley (Faktaverifierare) - Minimum:

| Metric | Minimum | Excellent | Kritiskt? |
|--------|---------|-----------|-----------|
| **Claims verifierade** | 95% | 98%+ | JA |
| **Kritiska faktafel** | 0 | 0 | JA |
| **Mindre faktafel** | ≤2 | 0 | NEJ |
| **Svenska autenticitet** | 9/10 | 10/10 | JA |

**Finley MÅSTE uppnå:**
- 0 kritiska fel
- ≥95% verifierade claims
- ≥9/10 svensk autenticitet

---

#### Gray (Kontinuitetsansvarig) - Minimum:

| Metric | Minimum | Excellent | Kritiskt? |
|--------|---------|-----------|-----------|
| **Kontinuitetsfel** | 0 | 0 | JA |
| **Karaktärskonsistens** | 100% | 100% | JA |
| **Tidslinje logisk** | 100% | 100% | JA |
| **Object tracking** | 100% | 100% | NEJ (men viktigt) |

**Gray MÅSTE uppnå:**
- 0 kontinuitetsfel
- 100% karaktärs- och tidslinjes-konsistens

---

#### Jordan (Spänningsanalytiker) - Minimum:

| Metric | Minimum | Excellent | Kritiskt? |
|--------|---------|-----------|-----------|
| **Spänningskurva dynamisk** | 7/10 | 9/10 | NEJ (men viktigt) |
| **Opening hook** | 7/10 | 9/10 | NEJ |
| **Cliffhanger** | 7/10 | 9/10 | NEJ (utom sista kap) |
| **Stakes tydliga** | 8/10 | 10/10 | JA |
| **Page-turner factor** | 7/10 | 9/10 | NEJ |
| **Combined tension rating** | 7.5/10 | 9/10 | NEJ |

**Jordan MÅSTE uppnå:**
- Stakes ≥8/10 (läsaren måste bry sig!)
- Combined ≥7.5/10

---

#### Sage (FINAL version) - Overall:

| Metric | Minimum | Excellent |
|--------|---------|-----------|
| **Combined quality rating** | 8.0/10 | 9.0/10 |
| **Alla kritiska fel fixade** | 100% | 100% |
| **Publiceringsklart** | JA | JA |

**Sage FINAL MÅSTE uppnå:**
- Combined ≥8.0/10
- 0 kritiska fel (fakta + kontinuitet)

---

**GATE 4 BESLUT:**
- ✅ **ALLA minimums uppnådda** → FINAL GODKÄND ✨
- ⚠️ **1-2 metrics < minimum (ej kritiska)** → Targeted fixes → Re-check
- ❌ **Kritiska metrics < minimum** → Major revision

**Dokumentation:**
`chapters/chapter-XX/quality-gate-4.md`

---

## 🚨 ALERT LEVELS

### 🟢 GREEN (All Clear)
**Alla metrics ≥ minimum**
→ Fortsätt till nästa fas

### 🟡 YELLOW (Caution)
**1-2 non-critical metrics < minimum**
→ Targeted fixes på specifika områden
→ Re-check dessa metrics
→ Fortsätt när fixat

### 🔴 RED (Stop)
**3+ metrics < minimum ELLER critical metrics < minimum**
→ STOPP, gå inte vidare
→ Major revision eller rewrite
→ Re-kör hela fasen

---

## 📋 QUALITY GATE CHECKLISTA (per fas)

### Template: `quality-gate-template.md`

```markdown
# QUALITY GATE [X]: [Fas namn]

**Datum:** [YYYY-MM-DD]
**Kapitel:** [Om relevant]
**Bedömd av:** [Agent eller Författare]

---

## METRICS

| Metric | Target | Actual | Status | Kommentar |
|--------|--------|--------|--------|-----------|
| [Metric 1] | [Min] | [Score] | 🟢/🟡/🔴 | [Notes] |
| [Metric 2] | [Min] | [Score] | 🟢/🟡/🔴 | [Notes] |
| ... | ... | ... | ... | ... |

---

## OVERALL STATUS

**Alert Level:** 🟢 GREEN / 🟡 YELLOW / 🔴 RED

**BESLUT:**
- [ ] ✅ GODKÄND - Fortsätt till nästa fas
- [ ] ⚠️ REVIDERA - Specifika fixes krävs (lista nedan)
- [ ] ❌ STOP - Major revision/rewrite

---

## OM REVIDERING KRÄVS:

### Kritiska problem (MÅSTE fixas):
1. [Problem 1]
2. [Problem 2]

### Mindre problem (BORDE fixas):
1. [Problem 1]
2. [Problem 2]

---

## NÄSTA STEG

[Vad är nästa action?]

---

**Godkänd av:** [Namn]
**Datum godkänd:** [YYYY-MM-DD]
```

---

## 🎯 SUCCESS METRICS (hela boken)

**När hela boken är klar, måste den uppnå:**

| Overall Metric | Minimum | Excellent |
|----------------|---------|-----------|
| **Alla kapitel ≥8.0/10** | 100% | 100% |
| **Total faktaverifiering** | 95%+ | 98%+ |
| **Total kontinuitetsfel** | 0 | 0 |
| **Genomsnittlig chapter rating** | 8.0/10 | 8.5/10 |
| **Spänningskurva (book-wide)** | 8/10 | 9/10 |
| **Författaren är NÖJD** | JA | JA |

---

## 💡 ANVÄNDNING

### För varje fas:
1. Kör fasen (agents producerar output)
2. Fyll i Quality Gate checklista
3. Bedöm metrics
4. Beslut: 🟢 GO / 🟡 REVISE / 🔴 STOP
5. Dokumentera i `quality-gate-X.md`

### Iteration är OK!
**Det är NORMALT att:**
- Få 🟡 YELLOW första gången
- Göra targeted fixes
- Re-check och få 🟢 GREEN

**Kostnaden:**
- 🟡 Fixes: 30 min - 2 timmar
- 🔴 Rewrite: 3-8 timmar

**Men:**
- Fixa i Fas 1 = 1 timme
- Upptäcka samma problem i Fas 4 = 10+ timmar att fixa

**Quality Gates sparar tid!**

---

## 🔧 INTEGRATION MED WORKFLOWS

Quality Gates läggs till i alla workflow-filer:

**workflow/phase0-narrative-validation.md:**
- Lägg till "Quality Gate 0" sektion i slutet

**workflow/phase1-creative.md:**
- Lägg till "Quality Gate 1" sektion i slutet

**workflow/phase2-writing.md:**
- Lägg till "Quality Gate 2" sektion i slutet

**workflow/phase3-revision.md:**
- Lägg till "Quality Gate 3" sektion i slutet

**workflow/phase4-qa.md:**
- Lägg till "Quality Gate 4" sektion i slutet

---

**Quality Gates = Din försäkring mot att investera tid i dålig output.**
