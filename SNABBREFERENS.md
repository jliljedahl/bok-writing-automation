# NOIR Dashboard - Snabbreferens

## 🚀 Vanligaste Kommandona

### Öppna Demo Dashboard
```bash
cd ~/Claude-Code-exp/bok-writing-automation/books/demo-projekt
python3 -m http.server 8000
# Öppna: http://localhost:8000/dashboard.html
```

### Skapa Nytt Projekt
```bash
cd ~/Claude-Code-exp/bok-writing-automation/web
python3 update_dashboard.py PROJEKTNAMN init
```

### Lista Alla Projekt
```bash
cd ~/Claude-Code-exp/bok-writing-automation/web
python3 update_dashboard.py list
```

### Regenerera Dashboard
```bash
cd ~/Claude-Code-exp/bok-writing-automation/web
python3 update_dashboard.py PROJEKTNAMN generate
```

## 📝 Uppdatera Dashboard via Python

### Lägg Till Kapitel
```python
from update_dashboard import DashboardUpdater

updater = DashboardUpdater("mitt-projekt")

updater.update_chapter(
    chapter_number=1,
    version_name="Draft v1",
    text="Kapiteltext här...",
    metadata={
        "author": "Sage",
        "quality": 7.5,
        "pov": "Protagonist",
        "location": "Ystad"
    }
)
```

### Uppdatera Outline
```python
outline = {
    "logline": "En kort beskrivning...",
    "hook": "Det som fångar läsaren...",
    "twist": "Den stora vändningen...",
    "resolution": "Hur det slutar...",
    "acts": [
        {
            "number": 1,
            "title": "Akt I: Setup",
            "description": "...",
            "beats": [
                {
                    "name": "Opening Image",
                    "description": "...",
                    "chapter": 1
                }
            ]
        }
    ]
}

updater.update_outline(outline)
```

### Uppdatera Karaktärer
```python
characters = [
    {
        "name": "Namn Namnsson",
        "role": "Protagonist",
        "age": 42,
        "occupation": "Yrke",
        "description": "Beskrivning...",
        "arc": {
            "start": "Hur karaktären är i början",
            "middle": "Förändring under berättelsen",
            "end": "Hur karaktären är i slutet"
        },
        "ghost": "Traumatisk händelse från förr",
        "want": "Vad karaktären tror hen vill",
        "need": "Vad karaktären verkligen behöver"
    }
]

updater.update_characters(characters)
```

### Sätt Aktuell Fas
```python
updater.set_phase("Fas 2: Writing")
```

## 🌐 Starta Webbserver

### Vanlig Metod
```bash
cd ~/Claude-Code-exp/bok-writing-automation/books/PROJEKTNAMN
python3 -m http.server 8000
```

### Annan Port
```bash
python3 -m http.server 8001  # Port 8001 istället
```

### Stoppa Servern
Tryck `Ctrl+C` i terminalen

## 📁 Filstruktur

```
bok-writing-automation/
├── web/
│   ├── dashboard.html          # Dashboard template
│   ├── data-template.json      # Data template
│   ├── update_dashboard.py     # Python API
│   ├── demo_populate.py        # Demo generator
│   └── README.md              # Full dokumentation
├── books/
│   ├── demo-projekt/
│   │   ├── dashboard.html     # Projektets dashboard
│   │   └── data.json          # All projektdata
│   └── mitt-projekt/
│       ├── dashboard.html
│       └── data.json
└── docs/
    ├── quality-gates.md
    ├── pilot-chapter-system.md
    ├── agent-calibration-guide.md
    └── chapter-structure-guide.md
```

## 🔧 Troubleshooting

### Dashboard visar inget innehåll
```bash
# Kolla JavaScript-konsolen (Cmd+Option+J)
# Kolla att data.json finns:
ls -la books/PROJEKTNAMN/data.json

# Regenera projektet:
cd web
python3 update_dashboard.py PROJEKTNAMN generate
```

### "Fetch failed" fel
**Problem:** Webbläsare blockerar fetch() från file:// URLs

**Lösning:** MÅSTE använda lokal webbserver:
```bash
cd books/PROJEKTNAMN
python3 -m http.server 8000
# Öppna: http://localhost:8000/dashboard.html
```

### Kapiteltext visas inte
```bash
# Kolla att versioner finns i data.json:
cat books/PROJEKTNAMN/data.json | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Kapitel 1 versioner: {len(data[\"chapters\"][0][\"versions\"])}')"

# Om 0 versioner, uppdatera kapitel igen
```

### Port redan använd
```bash
# Använd annan port:
python3 -m http.server 8001

# Eller hitta vad som använder port 8000:
lsof -i :8000
# Döda processen:
kill -9 PID
```

## 📊 Data Format

### Minimal Chapter
```json
{
  "number": 1,
  "title": "Kapitel 1",
  "status": "pending",
  "words": 0,
  "quality": null,
  "versions": [],
  "metadata": {}
}
```

### Full Chapter
```json
{
  "number": 1,
  "title": "Kapitel 1: Titel",
  "status": "completed",
  "words": 5420,
  "quality": 8.3,
  "tension": 7,
  "synopsis": "Kort sammanfattning",
  "versions": [
    {
      "name": "Draft v1",
      "date": "2025-11-06T10:00:00Z",
      "author": "Sage",
      "quality": 7.2,
      "text": "Full kapiteltext här..."
    },
    {
      "name": "FINAL",
      "date": "2025-11-06T12:00:00Z",
      "author": "Sage (efter QA)",
      "quality": 8.3,
      "text": "Final kapiteltext här..."
    }
  ],
  "metadata": {
    "pov": "Protagonist",
    "location": "Ystad",
    "factVerification": 98,
    "continuityErrors": 0
  }
}
```

## 🎯 Tips

1. **Använd ALLTID lokal webbserver** - Fetch fungerar inte från file://
2. **Backup data.json** innan stora ändringar
3. **Ett projekt per bok** - Lättare att hålla ordning
4. **Versionsnamn:** Draft v1, Draft v2, Draft v3, FINAL
5. **Kvalitet:** 1-10 skala (7.0+ är bra, 8.0+ är excellent)

## 📚 Nästa Steg

1. **Läs full dokumentation:** `web/README.md`
2. **Validation framework:** `docs/quality-gates.md`
3. **Pilot testing:** `docs/pilot-chapter-system.md`
4. **Agent calibration:** `docs/agent-calibration-guide.md`
5. **Chapter structure:** `docs/chapter-structure-guide.md`

---

**Spara denna fil för snabb tillgång till vanliga kommandon! 📌**
