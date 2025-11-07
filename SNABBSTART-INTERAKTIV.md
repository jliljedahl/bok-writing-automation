# 🚀 SNABBSTART: INTERAKTIVT NOIR SYSTEM

Den interaktiva webbaserade bokskrivningsplattformen är nu komplett och redo att användas!

---

## 📋 VAD ÄR KLART

✅ **Flask Backend** - REST API för alla operationer
✅ **JavaScript API** - Wrapper för enkel frontend-integration
✅ **Plot Intake Formulär** - Webbaserat formulär för att starta projekt
✅ **Feedback UI** - Interaktiva knappar och formulär för feedback
✅ **Dashboard Integration** - Allt kopplat och redo att använda

---

## 🏁 STARTA SYSTEMET (2 minuter)

### Steg 1: Installera Dependencies

```bash
cd ~/bok-writing-automation
pip install -r web/requirements.txt
```

### Steg 2: Starta Backend

```bash
python3 web/app.py
```

Du ska se:
```
* Running on http://127.0.0.1:5000
```

Låt denna terminal vara öppen!

### Steg 3: Öppna Plot Intake i Webbläsaren

Öppna i ny flik:
```
file:///home/user/bok-writing-automation/web/templates/plot-intake-form.html
```

Eller via HTTP server (rekommenderat):
```bash
# I ny terminal
cd ~/bok-writing-automation
python3 -m http.server 8001

# Öppna sedan:
http://localhost:8001/web/templates/plot-intake-form.html
```

---

## 📝 WORKFLOW: SKAPA ETT BOKPROJEKT

### 1. Fyll i Plot Intake Formuläret

Öppna: `web/templates/plot-intake-form.html`

Fyll i:
- ✅ **Projekt ID** (t.ex. "min-thriller")
- ✅ **Boktitel** (t.ex. "Skuggan i Snön")
- ✅ **Genre** (välj från dropdown)
- ✅ **Logline** (1-2 meningar om storyn)
- ✅ **Protagonist** (namn, ålder, ghost, need, fear, flaw)
- ✅ **Antagonist** (namn, motivation)
- ✅ **Konflikt** (vad är mysteriet?)
- ✅ **Plot Outline** (3-akt struktur)
- ✅ **Twist** (den stora vändningen)
- ⚠️ Övriga fält är valfria men rekommenderas

**Klicka:** "🚀 Skicka Plot & Starta Projekt"

### 2. Vad Händer Nu?

Backend kommer:
1. Skapa projektet i `books/<projekt-id>/`
2. Spara din plot data i `data.json`
3. Generera initial outline (placeholders för Harper att fylla i)
4. Skapa karaktärer från protagonist/antagonist data
5. Initiera kapitelstruktur
6. Generera dashboard

Du redirectas automatiskt till dashboard!

### 3. Granska Outline

På dashboarden:
1. Klicka på fliken **"Outline"**
2. Granska Harper's genererade outline
3. Klicka **"💬 Ge Feedback på Outline"**

### 4. Ge Feedback på Outline

I feedback-modalen:
- ⭐ Betygsätt varje sektion (Logline, Hook, Twist, Resolution) 1-10
- 💬 Skriv feedback för varje sektion
- ✅ Markera vilka sektioner som behöver ändras
- 📝 Lägg till specifika önskemål till Harper
- 📊 Ge overall score

**Välj beslut:**
- ✅ **Godkänn** → Går vidare till Fas 1 (Creative Planning)
- 🔄 **Begär Revision** → Harper reviderar baserat på din feedback
- ❌ **Avslå** → Börja om från början

### 5. Vänta på Kapitel

När outline godkänts kommer Creative Team att:
1. **Harper** - Utveckla detaljerad plotstruktur
2. **Morgan** - Skapa djupa karaktärsprofiler
3. **Quinn** - Designa distinkta röster
4. **River** - Researcha och beskriv platser
5. **Sage** - Börja skriva kapitel

### 6. Ge Feedback på Kapitel

När kapitel är skrivna:
1. Klicka på fliken **"Chapters"**
2. Klicka på ett kapitel
3. Läs kapitlet (växla mellan versioner om flera finns)
4. Klicka **"💬 Ge Feedback på Detta Kapitel"**

I kapitel-feedback:
- ⚡ **Pacing** (1-10) - Tempo och flöde
- 😰 **Tension** (1-10) - Spänning och suspense
- 💬 **Dialogue** (1-10) - Naturliga dialoger
- 🎭 **Character Consistency** (1-10) - Trovärdiga karaktärer
- ✍️ **Prose Quality** (1-10) - Språk och läsbarhet
- 📈 **Plot Advancement** (1-10) - Driver handlingen framåt
- ⚠️ **Måste Fixas** - Lista kritiska problem
- 💡 **Nice to Have** - Förslag på förbättringar

**Välj beslut:**
- ✅ **Godkänn** → Kapitlet klart, gå vidare
- 🔄 **Begär Revision** → Sage skriver om med din feedback
- ❌ **Avslå** → Kapitlet skrivs om helt

---

## 🔧 API ENDPOINTS

Backend tillhandahåller:

### Projects
- `GET /api/projects` - Lista alla projekt
- `GET /api/projects/<name>` - Hämta projektdata
- `POST /api/projects/<name>` - Skapa nytt projekt

### Plot Intake
- `POST /api/projects/<name>/plot-intake` - Submit plot och starta projekt

### Outline
- `GET /api/projects/<name>/outline` - Hämta outline
- `POST /api/projects/<name>/outline/feedback` - Submit outline feedback

### Characters
- `GET /api/projects/<name>/characters` - Hämta karaktärer
- `POST /api/projects/<name>/characters/feedback` - Submit character feedback

### Chapters
- `GET /api/projects/<name>/chapters` - Hämta alla kapitel
- `GET /api/projects/<name>/chapters/<num>` - Hämta specifikt kapitel
- `POST /api/projects/<name>/chapters/<num>/feedback` - Submit chapter feedback

---

## 🎨 ANVÄND API:ET FRÅN JAVASCRIPT

Om du vill bygga egna UI-komponenter:

```javascript
// API finns på window.NOIR.api

// Lista projekt
const projects = await NOIR.api.listProjects();

// Hämta projekt
const project = await NOIR.api.getProject('min-thriller');

// Submit plot
const plotData = {
    title: "Min Bok",
    logline: "En spännande berättelse...",
    // ... mer data
};
await NOIR.api.submitPlotIntake('min-thriller', plotData);

// Ge outline feedback
const feedback = {
    decision: "REVISE",
    overallScore: 7,
    comments: {
        logline: {
            score: 8,
            feedback: "Bra men kan förbättras",
            changeRequested: true
        }
    },
    specificRequests: ["Gör twisten mer överraskande"]
};
await NOIR.api.submitOutlineFeedback('min-thriller', feedback);

// Visa notifikationer
NOIR.ui.showNotification('Feedback skickad!', 'success');
NOIR.ui.showLoading(true); // Visa loading
NOIR.ui.showLoading(false); // Dölj loading
```

---

## 📂 FILSTRUKTUR

```
bok-writing-automation/
├── web/
│   ├── app.py                          # Flask backend (REST API)
│   ├── requirements.txt                # Python dependencies
│   ├── dashboard.html                  # Dashboard template (kopieras till projekt)
│   ├── static/
│   │   ├── noir-app.js                # API wrapper library
│   │   └── feedback-ui.js             # Feedback UI components
│   ├── templates/
│   │   └── plot-intake-form.html      # Plot intake formulär
│   ├── update_dashboard.py             # Dashboard updater (används av backend)
│   └── data-template.json              # Template för nya projekt
│
├── books/
│   └── <projekt-namn>/
│       ├── data.json                   # Projektdata (auto-genererad)
│       └── dashboard.html              # Projektets dashboard (kopierad från template)
│
└── templates/
    ├── plot-intake.md                  # Markdown template (för referens)
    └── feedback/
        ├── feedback-outline-template.json
        └── feedback-chapter-template.json
```

---

## 🐛 FELSÖKNING

### Problem: "CORS error" i konsolen

**Lösning:** Se till att Flask backend körs (`python3 web/app.py`)

### Problem: "Connection refused"

**Lösning:** Backend är inte igång. Starta med `python3 web/app.py`

### Problem: Plot-formuläret gör ingenting

**Lösning 1:** Öppna browser console (F12) och kolla efter errors
**Lösning 2:** Verifiera att backend körs på http://localhost:5000
**Lösning 3:** Testa backend direkt:
```bash
curl http://localhost:5000/api/health
# Ska returnera: {"status":"ok","service":"NOIR Backend","version":"1.0.0"}
```

### Problem: Dashboard visar inte feedback-knappar

**Lösning:** Se till att du öppnar dashboard via lokal server:
```bash
cd ~/bok-writing-automation/books/<projekt-namn>
python3 -m http.server 8000
# Öppna: http://localhost:8000/dashboard.html
```

Dashboarden behöver laddas via HTTP (inte file://) för att kunna ladda JavaScript-filerna korrekt.

### Problem: "Cannot read property 'showNotification' of undefined"

**Lösning:** noir-app.js laddades inte. Se till att:
1. Filen finns på `web/static/noir-app.js`
2. Dashboard laddas via HTTP server (inte file://)
3. Relativa paths är korrekta

---

## ✨ NÄSTA STEG

Nu när systemet är klart:

1. **Testa workflow:**
   - Fyll i plot intake för ett testprojekt
   - Ge feedback på outline
   - Ge feedback på ett testkapitel

2. **Koppla in AI-agenter:**
   - Integrera Harper för riktigt outline-generering
   - Integrera Sage för kapitelskrivning
   - Automatisera revision-loopen

3. **Utöka funktionalitet:**
   - Lägg till exportfunktioner (PDF, DOCX)
   - Lägg till collaboration features
   - Integrera version control för kapitel

---

## 📚 EXEMPEL: KOMPLETT SESSION

```bash
# Terminal 1: Starta backend
cd ~/bok-writing-automation
python3 web/app.py

# Terminal 2: Starta frontend server (valfritt men rekommenderat)
cd ~/bok-writing-automation
python3 -m http.server 8001

# Browser:
# 1. Öppna: http://localhost:8001/web/templates/plot-intake-form.html
# 2. Fyll i plot för "vintermord"
# 3. Klicka "Skicka Plot"
# 4. Redirectas till dashboard
# 5. Gå till "Outline" tab
# 6. Klicka "Ge Feedback på Outline"
# 7. Fyll i feedback och klicka "Godkänn"
# 8. Vänta på att kapitel skrivs
# 9. Gå till "Chapters" tab
# 10. Klicka på "Kapitel 1"
# 11. Klicka "Ge Feedback på Detta Kapitel"
# 12. Fyll i feedback och klicka "Godkänn" eller "Begär Revision"
```

---

## 🎉 GRATTIS!

Du har nu ett fullt fungerande interaktivt bokskrivningssystem!

**Ingen mer manuell JSON-editering!**
**Allt sköts via webgränssnittet!**

God skrivarresa! 📖✨
