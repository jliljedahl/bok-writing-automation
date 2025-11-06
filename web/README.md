# NOIR Web Dashboard

Webgränssnittet för att följa bokprojektets framsteg i realtid.

## 📊 Översikt

Web dashboard visar:
- **Progress tracking**: Total framgång, kapitel klara, ordantal, kvalitetspoäng
- **Outline**: Berättelsens struktur, akter, plot beats
- **Karaktärer**: Alla karaktärer med profiler och character arcs
- **Kapitel**: Kapitel-för-kapitel med versionshantering (Draft v1, v2, FINAL)

## 🚀 Snabbstart

### Skapa nytt projekt

```bash
cd /home/user/noir-book-system/web
python update_dashboard.py mitt-projekt init
```

Detta skapar:
- `/books/mitt-projekt/data.json` - Projektdata
- `/books/mitt-projekt/dashboard.html` - Projektets dashboard

### Öppna dashboard

Öppna filen i din webbläsare:

```
file:///home/user/noir-book-system/books/mitt-projekt/dashboard.html
```

Eller från Mac (om du klonat projektet):

```
open ~/Claude-Code-exp/bok-writing-automation/books/mitt-projekt/dashboard.html
```

### Lista projekt

```bash
python update_dashboard.py list
```

## 📁 Filstruktur

```
noir-book-system/
├── web/
│   ├── dashboard.html          # Dashboard template
│   ├── data-template.json      # Data template för nya projekt
│   ├── update_dashboard.py     # Python script för uppdateringar
│   └── README.md               # Denna fil
└── books/
    └── mitt-projekt/
        ├── data.json           # Projektdata (JSON)
        └── dashboard.html      # Projektspecifik dashboard
```

## 🔄 Uppdatera Dashboard

Dashboard uppdateras automatiskt när agenter arbetar, men du kan också uppdatera manuellt.

### Uppdatera kapitel

```python
from web.update_dashboard import DashboardUpdater

updater = DashboardUpdater("mitt-projekt")

# Lägg till Draft v1
updater.update_chapter(
    chapter_number=1,
    version_name="Draft v1",
    text="Kapiteltext här...",
    metadata={
        "author": "Sage",
        "quality": 7.2,
        "pov": "Martin Sundberg",
        "location": "Ystad",
        "factVerification": 95
    }
)

# Lägg till Draft v2
updater.update_chapter(
    chapter_number=1,
    version_name="Draft v2",
    text="Förbättrad text...",
    metadata={
        "author": "Sage (efter Ellis feedback)",
        "quality": 8.0
    }
)

# Lägg till FINAL
updater.update_chapter(
    chapter_number=1,
    version_name="FINAL",
    text="Final text...",
    metadata={
        "author": "Sage (efter QA)",
        "quality": 8.3
    }
)
```

### Uppdatera outline

```python
outline = {
    "logline": "En utbränd polis måste konfrontera sitt förflutna...",
    "hook": "Kroppen tillhör någon från hans förflutna.",
    "twist": "Hans partner är antagonisten.",
    "resolution": "Han accepterar sin sårbarhet.",
    "acts": [
        {
            "number": 1,
            "title": "Akt I: Setup",
            "description": "Etablera Martin och inciting incident.",
            "beats": [...]
        }
    ]
}

updater.update_outline(outline)
```

### Uppdatera karaktärer

```python
characters = [
    {
        "name": "Martin Sundberg",
        "role": "Protagonist",
        "age": 42,
        "occupation": "Kriminalinspektör",
        "description": "Utbränd polis...",
        "arc": {
            "start": "Cynisk och isolerad",
            "middle": "Tvingas konfrontera förflutet",
            "end": "Accepterar sårbarhet"
        },
        "ghost": "Misslyckades rädda partner",
        "want": "Lösa fallet och pensionera sig",
        "need": "Förlåta sig själv"
    }
]

updater.update_characters(characters)
```

### Sätt aktuell fas

```python
updater.set_phase("Fas 1: Creative Planning")
```

## 📋 Data Format

### Projektdata struktur (data.json)

```json
{
  "title": "Bokens Titel",
  "author": "Författarens Namn",
  "currentPhase": "Fas 0: Narrative Validation",
  "structure": "Hybrid (18 kapitel)",
  "targetWords": 80000,
  "totalWords": 0,
  "lastUpdated": "2025-11-06T12:00:00Z",
  "outline": { ... },
  "characters": [ ... ],
  "chapters": [ ... ]
}
```

### Kapitel struktur

```json
{
  "number": 1,
  "title": "Kapitel 1: Den Första Kroppen",
  "status": "completed",           // pending, in-progress, completed
  "words": 5420,
  "quality": 8.3,
  "tension": 7,
  "lastUpdated": "2025-11-06T10:00:00Z",
  "synopsis": "Martin hittar ett lik...",
  "versions": [
    {
      "name": "Draft v1",
      "date": "2025-11-05T14:00:00Z",
      "author": "Sage",
      "quality": 7.2,
      "text": "Kapiteltext..."
    },
    {
      "name": "Draft v2",
      "date": "2025-11-05T18:00:00Z",
      "author": "Sage (efter Ellis feedback)",
      "quality": 8.0,
      "text": "Förbättrad text..."
    },
    {
      "name": "FINAL",
      "date": "2025-11-06T10:00:00Z",
      "author": "Sage (efter QA)",
      "quality": 8.3,
      "text": "Final version..."
    }
  ],
  "metadata": {
    "pov": "Martin Sundberg",
    "location": "Ystad, Sverige",
    "factVerification": 98,
    "continuityErrors": 0,
    "agentScores": {
      "sage": 8.5,
      "blake": 8.0,
      "ellis": 8.2
    }
  }
}
```

## 🎨 Dashboard Features

### Översikt Tab
- Total progress (procent färdig)
- Kapitel klara (X / Y)
- Totalt ordantal
- Genomsnittlig kvalitetspoäng
- Kapitel-rutnät med status (grön = klar, gul = pågår, grå = väntande)

### Outline Tab
- Logline, hook, twist, resolution
- Akter (I, II, III) med plot beats
- Kopplade till kapitel

### Karaktärer Tab
- Alla karaktärer med profiler
- Character arcs (start, middle, end)
- Ghost, Want, Need

### Kapitel Tab
- Lista alla kapitel
- Klicka för att öppna kapitel i modal
- Versionsväxlare (Draft v1, v2, FINAL)
- Metadata: ordantal, kvalitet, POV, plats
- Full kapiteltext

## 🔧 Integration med Agents

Agents uppdaterar automatiskt dashboard via Python API.

### Exempel: Sage uppdaterar kapitel

```python
# I Sage's workflow efter att ha skrivit Draft v1:

from web.update_dashboard import DashboardUpdater

updater = DashboardUpdater(os.environ.get("BOOK_PROJECT", "default"))

# Läs kapiteltext från fil
with open(f"output/chapter_{chapter_num}_v1.md", 'r') as f:
    text = f.read()

# Uppdatera dashboard
updater.update_chapter(
    chapter_number=chapter_num,
    version_name="Draft v1",
    text=text,
    metadata={"author": "Sage", "quality": 7.5}
)
```

### Exempel: Harper uppdaterar outline

```python
# Efter Fas 1 när Harper har skapat outline:

from web.update_dashboard import DashboardUpdater

updater = DashboardUpdater(project_name)

# Läs outline från Harper's output
outline_data = load_outline_from_harper()

# Uppdatera dashboard
updater.update_outline(outline_data)
updater.set_phase("Fas 1: Creative Planning")
```

## 🌐 Öppna från Mac

Om du klonat projektet till din Mac:

```bash
# Navigera till projektet
cd ~/Claude-Code-exp/bok-writing-automation

# Öppna dashboard för specifikt projekt
open books/mitt-projekt/dashboard.html
```

Dashboard öppnas i din standardwebbläsare.

## 🎯 Best Practices

### 1. Ett projekt per bok
Skapa nytt projekt för varje bok:
```bash
python update_dashboard.py min-thriller init
python update_dashboard.py min-noir init
```

### 2. Uppdatera efter varje version
När Sage skriver ny version, uppdatera direkt:
```python
updater.update_chapter(1, "Draft v1", text, metadata)
updater.update_chapter(1, "Draft v2", text_v2, metadata)
updater.update_chapter(1, "FINAL", final_text, metadata)
```

### 3. Sätt fas tydligt
Hjälper hålla koll på progress:
```python
updater.set_phase("Fas 0: Narrative Validation")
updater.set_phase("Fas 1: Creative Planning")
updater.set_phase("Fas 2: Writing")
```

### 4. Spara ofta
Dashboard regenereras automatiskt vid varje uppdatering.

### 5. Backup data.json
```bash
cp books/mitt-projekt/data.json books/mitt-projekt/data.backup.json
```

## 🐛 Troubleshooting

### Dashboard visar "Inga kapitel ännu"
- Kontrollera att `data.json` har kapitel i `chapters` array
- Kör `python update_dashboard.py <projekt> generate`

### JavaScript error i konsolen
- Öppna browser console (F12)
- Kontrollera att `bookData` är valid JSON
- Validera data.json: `python -m json.tool books/<projekt>/data.json`

### Versioner visas inte
- Kontrollera att `versions` array finns i kapitel
- Varje version måste ha `name`, `date`, `author`, `text`

### Progress inte uppdaterad
- Kontrollera `totalWords` i data.json
- Kontrollera att `status` är satt korrekt på kapitel

## 📚 Exempel

Se `/web/data-template.json` för komplett exempel på datastruktur.

---

**Dashboard är ditt fönster in i bokproduktionen. Uppdatera ofta och följ progressen i realtid!**
