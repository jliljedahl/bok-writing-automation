# Feedback & Revision Workflow - NOIR System

## 🔄 ÖVERSIKT

Detta dokument definierar **exakt** hur du ger feedback och hur revision fungerar i NOIR-systemet.

---

## 📋 TRE NIVÅER AV FEEDBACK

### Nivå 1: OUTLINE & NARRATIVE (Fas 0)
**När:** Efter Harper har genererat outline från din plot intake
**Vad du granskar:** Logline, hook, twist, resolution, plot beats
**Beslut:** GO / REVISE / NO-GO

### Nivå 2: CHARACTER & DIALOGUE (Fas 1)
**När:** Efter Morgan och Quinn har skapat karaktärsprofiler
**Vad du granskar:** Character arcs, ghost, want/need, dialogstilar
**Beslut:** APPROVE / REQUEST CHANGES

### Nivå 3: CHAPTERS (Fas 2-4)
**När:** Efter varje kapitel version (Draft v1, v2, FINAL)
**Vad du granskar:** Faktisk text, pacing, tension, kvalitet
**Beslut:** APPROVE / REVISE / REWRITE

---

## 🎯 NIVÅ 1: OUTLINE FEEDBACK (Fas 0)

### Steg 1: Granska Outline

**Öppna dashboard** → **Outline tab**

Du ser:
- Logline
- Hook
- Twist
- Resolution
- 3 Akter med plot beats

### Steg 2: Skapa Feedback Fil

```bash
cd books/PROJEKTNAMN
cp ../../templates/feedback-outline-template.json feedback-outline.json
```

### Steg 3: Fyll I Feedback

**Format: `feedback-outline.json`**

```json
{
  "feedbackType": "outline",
  "date": "2025-11-07",
  "phase": "Fas 0: Narrative Validation",
  "decision": "REVISE",
  "overallScore": 7,
  "comments": {
    "logline": {
      "score": 8,
      "feedback": "Bra! Men kan du göra stakes tydligare?",
      "changeRequested": true
    },
    "hook": {
      "score": 9,
      "feedback": "Perfekt! Fångar läsaren direkt.",
      "changeRequested": false
    },
    "twist": {
      "score": 6,
      "feedback": "För förutsägbar. Kan vi ha något mer shocking?",
      "changeRequested": true
    },
    "resolution": {
      "score": 7,
      "feedback": "OK men känns lite rushed. Kan vi utforska emotional payoff mer?",
      "changeRequested": true
    },
    "act1": {
      "score": 8,
      "feedback": "Setup fungerar bra. Inciting incident är stark.",
      "changeRequested": false
    },
    "act2": {
      "score": 7,
      "feedback": "Midpoint är bra men 'All Is Lost' behöver mer emotional impact.",
      "changeRequested": true
    },
    "act3": {
      "score": 9,
      "feedback": "Climax är perfekt! Resolution kan förbättras (se ovan).",
      "changeRequested": false
    }
  },
  "specificRequests": [
    "Twist: Kan antagonisten vara någon närmare protagonist? Nuvarande twist känns för distanserad.",
    "Resolution: Låt protagonist offra något viktigt för att vinna. Nuvarande slutet är för 'clean'.",
    "Act II midpoint: Lägg till en personal betrayal, inte bara plot discovery."
  ],
  "strengthsToKeep": [
    "Hook är excellent - behåll!",
    "Protagonist's character arc är övertygande",
    "Setting och atmosphere är perfekt"
  ],
  "nextSteps": "Harper reviderar outline. Skicka tillbaka inom 24h."
}
```

### Steg 4: Processar Feedback

```bash
cd web
python3 process_feedback.py PROJEKTNAMN outline
```

**Detta:**
1. Läser din feedback
2. Uppdaterar dashboard med status "REVISION REQUESTED"
3. Genererar instruktioner till Harper
4. Harper reviderar outline
5. Du får ny outline att granska

### Steg 5: Beslut

**Decision Options:**

#### 🟢 GO (Score ≥8 overall, inga critical changes)
```json
{
  "decision": "GO",
  "overallScore": 9,
  "nextSteps": "Move to Fas 1: Creative Planning"
}
```
→ Systemet går vidare till Fas 1

#### 🟡 REVISE (Score 6-7, några changes requested)
```json
{
  "decision": "REVISE",
  "overallScore": 7,
  "nextSteps": "Harper reviderar baserat på feedback"
}
```
→ Du får reviderad outline att granska igen

#### 🔴 NO-GO (Score <6, fundamental issues)
```json
{
  "decision": "NO-GO",
  "overallScore": 4,
  "reason": "Plot doesn't work. Need new approach or different story.",
  "nextSteps": "Gå tillbaka till plot intake. Fundera om detta är rätt story att berätta."
}
```
→ Tillbaka till rittbordet

---

## 🎭 NIVÅ 2: CHARACTER FEEDBACK (Fas 1)

### Steg 1: Granska Karaktärer

**Dashboard** → **Karaktärer tab**

Du ser:
- Alla karaktärer med profiler
- Character arcs (start → middle → end)
- Ghost, Want, Need
- Dialogstilar (från Quinn)

### Steg 2: Feedback Format

**`feedback-characters.json`:**

```json
{
  "feedbackType": "characters",
  "date": "2025-11-07",
  "phase": "Fas 1: Creative Planning",
  "decision": "APPROVE_WITH_MINOR_CHANGES",
  "characters": [
    {
      "name": "Martin Sundberg",
      "score": 9,
      "feedback": "Excellent! Character arc är övertygande. Ghost är powerful.",
      "changes": []
    },
    {
      "name": "Lisa Eklund",
      "score": 7,
      "feedback": "Bra men antagonist motivation känns lite svag.",
      "changes": [
        "Kan vi ge henne mer personal connection till protagonist?",
        "Hennes 'why' behöver vara mer emotionally resonant."
      ]
    },
    {
      "name": "Emma Lindqvist",
      "score": 8,
      "feedback": "Fungerar bra som catalyst. No changes needed.",
      "changes": []
    }
  ],
  "dialogStyleFeedback": {
    "martin": "Perfect! Kort, brutal, cynisk. Behåll.",
    "lisa": "Bra men kanske lite för lik Martin? Kan hon vara lite mer verbose?",
    "emma": "N/A (död i flashbacks)"
  },
  "nextSteps": "Morgan reviderar Lisa. Quinn justerar hennes dialog-stil."
}
```

### Steg 3: Processar

```bash
python3 web/process_feedback.py PROJEKTNAMN characters
```

---

## 📖 NIVÅ 3: CHAPTER FEEDBACK (Fas 2-4)

**DETTA ÄR VIKTIGAST!** Du granskar varje kapitel i flera versioner.

### Workflow per Kapitel

```
Sage skriver Draft v1
  ↓
DU GRANSKAR Draft v1
  ↓
[Feedback] → Ellis granskar strukturellt
  ↓
Sage skriver Draft v2 (med dina + Ellis feedback)
  ↓
DU GRANSKAR Draft v2
  ↓
[Godkänd?] → Finley + Gray + Jordan QA
  ↓
Sage skriver FINAL
  ↓
DU GRANSKAR FINAL
  ↓
[Godkänd?] → KAPITEL KLART ✅
```

### Steg 1: Läs Kapitel i Dashboard

**Dashboard** → **Kapitel tab** → **Klicka på Kapitel X**

Modal öppnas med:
- Versioner (Draft v1, v2, FINAL)
- Metadata (ord, kvalitet, POV, location)
- Full text

### Steg 2: Ge Feedback

**Format: `feedback-chapter-X.json`**

```json
{
  "feedbackType": "chapter",
  "chapterNumber": 1,
  "version": "Draft v1",
  "date": "2025-11-07",
  "decision": "REVISE",
  "overallScore": 7,
  "categories": {
    "pacing": {
      "score": 8,
      "feedback": "Bra tempo. Opening är stark. Midpoint lite slow."
    },
    "tension": {
      "score": 6,
      "feedback": "Behöver mer tension i mitten. Slutet är bra men could escalate faster."
    },
    "characterVoice": {
      "score": 9,
      "feedback": "Martin's röst är perfekt. Dialog känns authentic."
    },
    "showDontTell": {
      "score": 7,
      "feedback": "Bra övergripande men några ställen är lite för expository. Se line comments."
    },
    "hook": {
      "score": 9,
      "feedback": "Excellent hook! 'Kroppen hittades en tisdag' - perfekt opening."
    }
  },
  "lineComments": [
    {
      "location": "Paragraph 3",
      "issue": "Too much exposition. Show Martin's exhaustion via action, not description.",
      "suggestion": "Instead of 'Han var trött', visa him fumbling with coffee, rubbing eyes, etc."
    },
    {
      "location": "Dialog exchange between Martin and Lisa",
      "issue": "Feels a bit on-the-nose. They're stating plot.",
      "suggestion": "More subtext. What are they NOT saying?"
    },
    {
      "location": "Ending",
      "issue": "Great cliffhanger but came too abruptly.",
      "suggestion": "Add 1-2 paragraphs to build up to it. Escalate tension gradually."
    }
  ],
  "strengths": [
    "Opening är powerful",
    "Martin's voice är consistent",
    "Atmosphere är excellent - vintern, mörker, känns authentiskt svenskt",
    "Dialog mellan Martin och Lisa känns natural"
  ],
  "mustFix": [
    "Reduce exposition i paragraph 3-5",
    "Add more subtext to dialog",
    "Build tension gradual mot cliffhanger"
  ],
  "niceToHave": [
    "Mer sensory details (hur luktar brottsplatsen?)",
    "Lite mer inner monologue från Martin (men inte too much)"
  ],
  "nextSteps": "Sage reviderar till Draft v2 baserat på denna feedback + Ellis structural review."
}
```

### Steg 3: Processar Feedback

```bash
python3 web/process_feedback.py PROJEKTNAMN chapter 1
```

### Steg 4: Granska Draft v2

Sage har nu reviderat baserat på:
- Din feedback
- Ellis structural feedback

**Dashboard** → **Kapitel 1** → **Välj "Draft v2"**

Läs igen. Ge ny feedback:

```json
{
  "version": "Draft v2",
  "decision": "APPROVE_FOR_QA",
  "overallScore": 8.5,
  "improvementFromV1": "Significant! Exposition reducerad, dialog har mer subtext, tension build är mycket bättre.",
  "remainingIssues": [],
  "readyForQA": true
}
```

### Steg 5: FINAL Version

Efter QA (Finley + Gray + Jordan), Sage skapar FINAL.

**Du granskar en sista gång:**

```json
{
  "version": "FINAL",
  "decision": "APPROVE",
  "overallScore": 9,
  "readyToPublish": true,
  "finalComments": "Excellent! Detta kapitel är färdigt. Move to next chapter."
}
```

✅ **KAPITEL KLART!**

---

## 🔧 TEKNISK IMPLEMENTATION

### Skapa Feedback

```bash
# För outline
cp templates/feedback-outline-template.json books/PROJEKT/feedback-outline.json
# Fyll i feedback
python3 web/process_feedback.py PROJEKT outline

# För karaktärer
cp templates/feedback-characters-template.json books/PROJEKT/feedback-characters.json
# Fyll i feedback
python3 web/process_feedback.py PROJEKT characters

# För kapitel
cp templates/feedback-chapter-template.json books/PROJEKT/feedback-chapter-1.json
# Fyll i feedback
python3 web/process_feedback.py PROJEKT chapter 1
```

### Dashboard Integration

**Dashboard visar:**
- 🟢 GREEN: Approved, no changes needed
- 🟡 YELLOW: Revision requested, in progress
- 🔴 RED: Major issues, needs rework

**Feedback Panel i Dashboard:**

Varje kapitel har en "Feedback" knapp som visar:
- All din tidigare feedback
- Nuvarande status (approved/revision/pending)
- Vad som ändrats mellan versioner
- Nästa steg

---

## 📊 DECISION FRAMEWORK

### När Ska Jag Säga GO vs REVISE vs NO-GO?

#### 🟢 GO (Fortsätt)
**Criteria:**
- Overall score ≥ 8/10
- Inga critical issues
- Du är excited om resultatet
- Ready to move forward

**Exempel:**
```json
{
  "decision": "GO",
  "reason": "Outline är excellent. Jag är excited att se Harper, Morgan, Quinn, River utveckla detta!"
}
```

#### 🟡 REVISE (Förbättra)
**Criteria:**
- Score 6-7/10
- Några issues men fixable
- Rätt direction men needs polish
- Eller: Great men några specifika changes requested

**Exempel:**
```json
{
  "decision": "REVISE",
  "reason": "Bra foundation men twist känns för predictable. Låt oss få något mer shocking."
}
```

#### 🔴 NO-GO (Börja Om)
**Criteria:**
- Score <6/10
- Fundamental issues
- Fel direction entirely
- Eller: Du inser denna story doesn't work

**Exempel:**
```json
{
  "decision": "NO-GO",
  "reason": "Efter att se outline inser jag att protagonist inte har clear enough arc. Vi behöver fundera om detta är rätt story."
}
```

---

## 🎯 BEST PRACTICES

### 1. Var Specifik

❌ **Dålig feedback:**
```json
{
  "feedback": "Det känns inte bra."
}
```

✅ **Bra feedback:**
```json
{
  "feedback": "Twist är för förutsägbar. Jag gissade att Lisa var antagonist i kapitel 3. Kan vi plantera fler red herrings eller göra twisten mer shocking? Kanske antagonisten är någon vi inte misstänker alls?"
}
```

### 2. Balansera Kritik Med Strengths

Alltid inkludera:
- Vad som FUNGERAR (behåll detta!)
- Vad som INTE fungerar (ändra detta)

### 3. Prioritera

Använd:
- **mustFix**: Critical issues
- **niceToHave**: Minor improvements

### 4. Ge Konkreta Exempel

Istället för "mer tension", säg:
- "Add a ticking clock - protagonist har 48 timmar innan mördaren slår till igen"
- "Escalate stakes - om Martin misslyckas, någon han älskar dör"

### 5. Lita På Processen

- Draft v1 kommer INTE vara perfekt
- Det är OK att begära 2-3 revisions
- Feedback är en konversation, inte en order

---

## 📁 FILSTRUKTUR

```
books/PROJEKT/
├── plot-intake.md              # Din original plot
├── feedback-outline.json       # Din outline feedback
├── feedback-characters.json    # Din character feedback
├── feedback-chapter-1.json     # Kapitel 1 feedback
├── feedback-chapter-2.json     # Kapitel 2 feedback
├── ...
└── data.json                   # All data (inkl feedback status)
```

---

## 🔄 ITERATION EXEMPEL

### Iteration 1: Outline
```
Harper genererar outline
  ↓
DU: "Twist är för predictable. Score 6/10. REVISE."
  ↓
Harper reviderar
  ↓
DU: "Much better! Score 8.5/10. GO!"
  ↓
Move to Fas 1
```

### Iteration 2: Kapitel 1
```
Sage Draft v1
  ↓
DU: "Bra start men too much exposition. Score 7/10. REVISE."
  ↓
Ellis + Sage → Draft v2
  ↓
DU: "Excellent! Reduced exposition, better pacing. Score 8.5/10. APPROVE FOR QA."
  ↓
QA (Finley + Gray + Jordan)
  ↓
Sage → FINAL
  ↓
DU: "Perfect! Score 9/10. APPROVE."
  ↓
KAPITEL 1 KLART ✅
```

---

## 🎉 SAMMANFATTNING

**Feedback/Revision Workflow i 3 Steg:**

1. **GRANSKA** (Dashboard eller JSON fil)
2. **GE FEEDBACK** (feedback-X.json med scores, comments, requests)
3. **BESLUT** (GO / REVISE / NO-GO)

**Systemet:**
- Processar din feedback
- Agents reviderar baserat på dina instructions
- Du får ny version att granska
- Repeat till du är nöjd

**Du har FULL KONTROLL!** Ingenting går vidare utan ditt godkännande. ✅

---

**Frågor? Se templates/ för exempel-feedback filer!**
