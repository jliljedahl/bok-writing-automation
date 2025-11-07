# 📚 KOMPLETT STARTGUIDE - NOIR Book Writing System

## 🎯 ALLT DU BEHÖVER VETA FÖR ATT KOMMA IGÅNG

---

## STEG 1: FÖRBEREDELSER (EN GÅNG)

### På Din Mac:

```bash
# 1. Gå till projektet
cd ~/Claude-Code-exp/bok-writing-automation

# 2. Hämta senaste uppdateringar från GitHub
git pull origin claude/book-writing-setup-011CUqN79J576EJL63L6TZpT

# 3. Kolla att allt finns
ls -la web/
ls -la docs/
ls -la templates/
```

---

## STEG 2: SE DEMO-PROJEKTET (Lär dig systemet)

### A. Starta Lokal Webbserver

**VIKTIGT!** Du måste använda lokal webbserver, inte öppna file:// direkt.

```bash
# Från projektroten
cd ~/Claude-Code-exp/bok-writing-automation

# Regenera demo-projektet med senaste fixar
cd web
python3 demo_populate.py

# Starta webbserver för demo
cd ../books/demo-projekt
python3 -m http.server 8000
```

Du ser:
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

### B. Öppna Dashboard

**Öppna webbläsare** → **Gå till:**
```
http://localhost:8000/dashboard.html
```

### C. Utforska Dashboard

**Översikt Tab:**
- Progress: 6% (1 av 18 kapitel klart)
- 358 ord totalt
- Kvalitet: 8.5/10

**Outline Tab:**
- Logline: "En utbränd kriminalinspektör i Ystad..."
- 3 Akter med plot beats
- Hook, Twist, Resolution

**Karaktärer Tab:**
- **Martin Sundberg** (Protagonist)
  - Kolla Character Arc (start → middle → end)
  - Ghost, Want, Need
- **Lisa Eklund** (Antagonist)
- **Emma Lindqvist** (Offer)

**Kapitel Tab:**
- **Klicka på "Kapitel 1: Den Första Kroppen"**
- Modal öppnas
- **Se 3 versioner:** Draft v1, Draft v2, FINAL
- **Klicka på Draft v1** → Se texten
- **Klicka på FINAL** → Se final version
- **Läs texten:** "Kroppen hittades en tisdag..."

✅ **Om du ser allt detta fungerar systemet!**

---

## STEG 3: SKAPA DITT EGET PROJEKT

### A. Kopiera Plot Intake Template

```bash
cd ~/Claude-Code-exp/bok-writing-automation

# Skapa nytt projekt
mkdir -p books/min-thriller

# Kopiera plot intake template
cp templates/plot-intake.md books/min-thriller/

# Öppna och fyll i
open books/min-thriller/plot-intake.md
# Eller: nano books/min-thriller/plot-intake.md
```

### B. Fyll I Din Plot

**Öppna `plot-intake.md`** och fyll i:

1. **Grundinfo:** Titel, genre, målordantal
2. **Logline:** Hela berättelsen i 1-2 meningar
3. **Protagonist:** Namn, ghost, want, need, fatal flaw
4. **Antagonist:** Vem, varför, motivation
5. **Konflikt:** Centrala mysteriet, stakes
6. **Setting:** Plats, årstid, varför
7. **Plot Struktur:** Act I, II, III med beats
8. **Twist:** Den stora vändningen
9. **Tematik:** Vad handlar boken om på djupet?

**Ta dig tid!** Detta är foundation för hela boken.

### C. Processar Plot Intake

```bash
cd web
python3 process_intake.py min-thriller
```

Detta skapar:
- `books/min-thriller/data.json` - Projektdata
- `books/min-thriller/dashboard.html` - Din dashboard
- Initial outline (placeholder, väntar på godkännande)

### D. Öppna Ditt Projekt

```bash
cd ../books/min-thriller
python3 -m http.server 8001  # Annan port än demo (8000)
```

**Öppna:** http://localhost:8001/dashboard.html

---

## STEG 4: GRANSKA OCH GE FEEDBACK PÅ OUTLINE

### A. Se Outline i Dashboard

**Dashboard** → **Outline Tab**

Du ser (genererad från din plot intake):
- Logline
- Hook
- Twist
- Resolution
- 3 Akter

### B. Skapa Feedback

```bash
cd ~/Claude-Code-exp/bok-writing-automation

# Kopiera feedback template
cp templates/feedback/feedback-outline-template.json books/min-thriller/feedback-outline.json

# Öppna och fyll i
open books/min-thriller/feedback-outline.json
```

### C. Fyll I Feedback

**Exempel `feedback-outline.json`:**

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
      "feedback": "Bra! Men stakes kunde vara tydligare.",
      "changeRequested": true
    },
    "hook": {
      "score": 9,
      "feedback": "Excellent! Fångar läsaren direkt.",
      "changeRequested": false
    },
    "twist": {
      "score": 6,
      "feedback": "För förutsägbar. Kan vi göra något mer shocking?",
      "changeRequested": true
    },
    "resolution": {
      "score": 7,
      "feedback": "OK men lite rushed. Mer emotional payoff?",
      "changeRequested": true
    }
  },
  "specificRequests": [
    "Twist: Kan antagonisten vara närmare protagonist? Mer personal betrayal?",
    "Resolution: Låt protagonist offra något viktigt för att vinna."
  ],
  "strengthsToKeep": [
    "Hook är excellent!",
    "Character arc är övertygande"
  ],
  "nextSteps": "Harper reviderar outline baserat på feedback."
}
```

### D. Processar Feedback

```bash
cd web
python3 process_feedback.py min-thriller outline
```

Du ser:
```
📝 Processar outline feedback för: min-thriller
🟡 REVISION BEGÄRD. Harper kommer revidera outline...

📊 FEEDBACK SAMMANFATTNING:
   Decision: REVISE
   Overall Score: 7/10
   Changes Requested: 3
```

### E. Granska Reviderad Outline

**Dashboard** uppdateras med:
- Status: "REVISION REQUESTED"
- Din feedback synlig
- Reviderad outline (när Harper är klar)

**Granska igen** → Ge ny feedback → Repeat till **DECISION: GO**

När **GO**:
```json
{
  "decision": "GO",
  "overallScore": 9,
  "nextSteps": "Move to Fas 1: Creative Planning"
}
```

✅ **Outline godkänd!** Systemet går vidare till Fas 1.

---

## STEG 5: FAS 1 - CREATIVE PLANNING

**När outline är godkänd:**

Systemet kör Creative Team:
- **Harper:** Detaljerad plotstruktur, spänningskurva
- **Morgan:** Djupa karaktärsprofiler
- **Quinn:** Distinkta dialogstilar per karaktär
- **River:** Svenska settings, atmosfär

**Dashboard visar:**
- Karaktärer Tab → Alla profiler
- Outline Tab → Detaljerad beat sheet

**Du granskar och godkänner:**
```bash
cp templates/feedback/feedback-characters-template.json books/min-thriller/feedback-characters.json
# Fyll i feedback
python3 web/process_feedback.py min-thriller characters
```

---

## STEG 6: FAS 2-4 - SKRIVA KAPITEL

### Workflow Per Kapitel:

```
Sage skriver Draft v1
  ↓
DU GRANSKAR (Dashboard → Kapitel Tab → Klicka kapitel)
  ↓
Ge feedback: cp templates/feedback/feedback-chapter-template.json books/min-thriller/feedback-chapter-1.json
  ↓
python3 web/process_feedback.py min-thriller chapter 1
  ↓
Sage + Ellis → Draft v2
  ↓
DU GRANSKAR Draft v2
  ↓
[Godkänd?] → QA (Finley + Gray + Jordan)
  ↓
Sage → FINAL
  ↓
DU GRANSKAR FINAL
  ↓
[Godkänd?] → KAPITEL KLART ✅
```

### Granska Kapitel:

**Dashboard** → **Kapitel Tab** → **Klicka "Kapitel 1"**

Modal visar:
- Metadata (ord, kvalitet, POV, location)
- Versioner (Draft v1, v2, FINAL)
- **Växla mellan versioner** med knapparna
- **Läs full text**

### Ge Kapitel-Feedback:

```bash
# Kopiera template
cp templates/feedback/feedback-chapter-template.json books/min-thriller/feedback-chapter-1.json

# Fyll i:
{
  "chapterNumber": 1,
  "version": "Draft v1",
  "decision": "REVISE",
  "overallScore": 7,
  "categories": {
    "pacing": {
      "score": 8,
      "feedback": "Bra tempo!"
    },
    "tension": {
      "score": 6,
      "feedback": "Behöver mer tension i mitten."
    }
  },
  "mustFix": [
    "Reduce exposition i paragraph 3-5",
    "Add more subtext to dialog"
  ],
  "niceToHave": [
    "Mer sensory details"
  ]
}

# Processar
python3 web/process_feedback.py min-thriller chapter 1
```

**Repeat för varje version** till FINAL är godkänd.

---

## 📊 DASHBOARD ÖVERSIKT

### Tabs:

1. **📊 Översikt**
   - Progress bar
   - Kapitel klara
   - Totalt ord
   - Kvalitetspoäng
   - Kapitel-grid (klickbar)

2. **📋 Outline**
   - Logline, Hook, Twist, Resolution
   - Akter med plot beats
   - Feedback status

3. **👥 Karaktärer**
   - Alla karaktärer med profiler
   - Character arcs
   - Ghost, Want, Need
   - Dialogstilar

4. **📖 Kapitel**
   - Lista alla kapitel
   - Klicka för att öppna modal
   - Versioner (Draft v1, v2, FINAL)
   - Full text
   - Metadata

---

## 🔧 VANLIGA KOMMANDON

```bash
# Starta webbserver för projekt
cd books/PROJEKTNAMN
python3 -m http.server 8000

# Processar plot intake
cd web
python3 process_intake.py PROJEKTNAMN

# Processar feedback
python3 process_feedback.py PROJEKTNAMN outline
python3 process_feedback.py PROJEKTNAMN chapter 1

# Lista alla projekt
python3 update_dashboard.py list

# Regenerera dashboard
python3 update_dashboard.py PROJEKTNAMN generate
```

---

## 🆘 TROUBLESHOOTING

### Dashboard visar inte innehåll

**Problem:** Öppnade `file:///...dashboard.html` direkt
**Lösning:** MÅSTE använda lokal webbserver

```bash
cd books/PROJEKTNAMN
python3 -m http.server 8000
# Öppna: http://localhost:8000/dashboard.html
```

### Kapiteltext visas inte

1. Öppna JavaScript-konsolen (Cmd+Option+J)
2. Kolla för fel
3. Verifiera data.json finns:
   ```bash
   ls -la books/PROJEKTNAMN/data.json
   cat books/PROJEKTNAMN/data.json | python3 -m json.tool | head -50
   ```

### Port redan använd

```bash
# Använd annan port:
python3 -m http.server 8001

# Eller hitta vad som använder porten:
lsof -i :8000
kill -9 PID
```

---

## 📚 DOKUMENTATION

- **`LÄSMIGFÖRST.md`** - Quick start
- **`SNABBREFERENS.md`** - Vanliga kommandon
- **`docs/feedback-revision-workflow.md`** - Detaljerad feedback-guide
- **`docs/quality-gates.md`** - Kvalitetsgrindar
- **`docs/pilot-chapter-system.md`** - Testa på 3 kapitel först
- **`web/README.md`** - Dashboard-dokumentation

---

## 🎯 SAMMANFATTNING

**För att skriva en bok med NOIR:**

1. ✅ **Fyll i plot-intake** (`templates/plot-intake.md`)
2. ✅ **Processar intake** (`python3 process_intake.py`)
3. ✅ **Granska outline** i dashboard
4. ✅ **Ge feedback** (`feedback-outline.json`)
5. ✅ **Godkänn** (decision: GO)
6. ✅ **Granska karaktärer** (Fas 1)
7. ✅ **Skriv & granska kapitel** (Fas 2-4)
8. ✅ **Repeat för varje kapitel** till boken är klar!

**Du har FULL KONTROLL!** Ingenting händer utan ditt godkännande. ✅

---

## 🚀 BÖRJA NU!

```bash
cd ~/Claude-Code-exp/bok-writing-automation
git pull origin claude/book-writing-setup-011CUqN79J576EJL63L6TZpT
cd web
python3 demo_populate.py
cd ../books/demo-projekt
python3 -m http.server 8000
```

**Öppna:** http://localhost:8000/dashboard.html

**Utforska demo → Skapa ditt projekt → Börja skriva! 📚✍️**
