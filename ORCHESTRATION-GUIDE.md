# 🎬 NOIR Orchestration System

## ✨ VAD ÄR NYTT

Nu har NOIR ett **komplett orkestreringsystem** som faktiskt koordinerar AI-agenter!

### Tidigare (mock):
- Agenter fanns som `.md` filer (bara instruktioner)
- Ingen faktisk AI-integration
- Hårdkodad demo-data

### Nu (riktigt):
- ✅ Fullständig agent-implementation i Python
- ✅ LLM-integration (Claude, OpenAI, eller mock för test)
- ✅ Automatisk koordinering mellan agenter
- ✅ Komplett pipeline från plot brief → färdig bok

---

## 📂 NY FILSTRUKTUR

```
bok-writing-automation/
├── run_noir.py                    # ⭐ HUVUDFIL - Kör NOIR
├── example-plot-brief.json        # Exempelbrief att utgå från
│
├── agents/                        # AI-agent implementation
│   ├── __init__.py
│   ├── base_agent.py             # Basklass för alla agenter
│   ├── llm_client.py             # Claude/OpenAI API-klient
│   ├── orchestrator.py           # Koordinerar alla agenter
│   │
│   ├── creative/                 # Creative Team
│   │   ├── __init__.py
│   │   ├── harper_agent.py       # Plot Architect
│   │   ├── morgan_agent.py       # Character Psychologist
│   │   ├── quinn_agent.py        # Voice Designer
│   │   └── river_agent.py        # World Builder
│   │
│   ├── writing/                  # Writing Team
│   │   ├── __init__.py
│   │   └── sage_agent.py         # Lead Writer
│   │
│   └── quality/                  # Quality Team
│       ├── __init__.py
│       └── ellis_agent.py        # Quality Reviewer
│
└── (gamla filer finns kvar...)
```

---

## 🚀 SNABBSTART

### 1. Installera Dependencies

```bash
# För mock-läge (test utan API):
pip install -r web/requirements.txt

# För riktiga AI-agenter:
pip install anthropic  # Claude
# ELLER
pip install openai     # GPT-4
```

### 2. Sätt API-nyckel (om du vill använda riktiga AI)

```bash
# För Claude:
export ANTHROPIC_API_KEY='your-api-key-here'

# För OpenAI:
export OPENAI_API_KEY='your-api-key-here'
```

### 3. Kör NOIR!

#### Variant A: Test med Mock (ingen API)

```bash
python3 run_noir.py \
  --project min-thriller \
  --brief example-plot-brief.json \
  --provider mock
```

#### Variant B: Riktiga AI-agenter med Claude

```bash
python3 run_noir.py \
  --project min-thriller \
  --brief example-plot-brief.json \
  --provider claude \
  --full
```

Detta kör **hela pipelinen**:
1. Harper genererar plot struktur
2. Morgan skapar karaktärer
3. River bygger setting
4. Quinn designar röst
5. Sage skriver Kapitel 1
6. Ellis granskar Kapitel 1

---

## 💡 ANVÄNDNINGSEXEMPEL

### Skapa Ny Bok (Endast Phase 0)

```bash
# Skapa din egen plot-brief.json:
{
  "title": "Min Bok",
  "genre": "noir",
  "plotIdea": "Din råa idé här (2-5 stycken)...",
  "targetAudience": "30-60 år",
  "wordCount": 80000
}

# Kör Phase 0 (Creative Planning):
python3 run_noir.py \
  --project min-bok \
  --brief plot-brief.json \
  --provider claude
```

Detta genererar:
- ✅ Komplett plot outline
- ✅ Djupa karaktärsprofiler
- ✅ Detaljerad setting
- ✅ Röst och ton-guidelines

### Skriv Specifikt Kapitel

```bash
python3 run_noir.py \
  --project min-bok \
  --chapter 1 \
  --provider claude
```

Detta:
1. Sage skriver kapitlet (2000-3000 ord)
2. Ellis granskar och ger feedback
3. Sparar i dashboard

### Kör Full Pipeline (Demo)

```bash
python3 run_noir.py \
  --project min-bok \
  --brief plot-brief.json \
  --provider claude \
  --full
```

Detta kör **allt** från början till slut med Kapitel 1 som demo.

### Kolla Status

```bash
python3 run_noir.py --project min-bok --status
```

Output:
```
📊 PROJECT STATUS

Title: Min Bok
Phase: Phase 3: QA - Chapter 1 reviewed
Words: 2,543
Chapters: 1/12
Last Updated: 2025-11-08T10:30:00
```

---

## 🤖 HUR AGENTERNA JOBBAR

### Phase 0: Creative Planning

```
Du → plot brief (JSON)
  ↓
Harper → Analyserar brief → Skapar plot struktur
  ↓
Morgan → Läser plot → Skapar karaktärer med ghost/want/need
  ↓
River → Läser plot + karaktärer → Bygger setting
  ↓
Quinn → Läser allt → Definierar röst och ton
  ↓
Dashboard uppdateras med allt
```

### Phase 1-2: Writing

```
Du (eller orchestrator) → "Skriv kapitel 1"
  ↓
Sage → Läser outline + karaktärer + tidigare kapitel
     → Skriver 2000-3000 ord prosa
     → Följer plot beats
     → Använder rätt röst
  ↓
Kapitel sparat med version
```

### Phase 3: Quality

```
Sage's kapitel
  ↓
Ellis → Läser kapitlet
      → Bedömer 7 kategorier (pacing, tension, dialogue, etc.)
      → Ger konkret feedback
      → Beslutar: APPROVE / NEEDS_REVISION / REJECT
  ↓
Feedback sparad, författare kan revidera
```

---

## 🎯 PROVIDERS

### Mock (Default - För Test)

```bash
--provider mock
```

- ✅ Ingen API-nyckel behövs
- ✅ Snabb (inga API-anrop)
- ✅ Gratis
- ❌ Genererar placeholder-data (men strukturerad!)

**Använd för:**
- Testa systemet
- Utveckling
- Demo
- När du inte har API-nyckel

### Claude (Rekommenderat)

```bash
--provider claude
```

- ✅ Högsta kvalitet för kreativt skriv ande
- ✅ Bra på att följa instruktioner
- ✅ Förstår svenska perfekt
- 💰 Kostar pengar (per token)

**Använd för:**
- Riktiga bokprojekt
- Bästa möjliga resultat

### OpenAI

```bash
--provider openai
```

- ✅ GPT-4 är också mycket bra
- ✅ Stort ekosystem
- 💰 Kostar pengar

**Använd för:**
- Om du föredrar OpenAI
- Om du redan har API-access

---

## 📖 KOMPLETT WORKFLOW EXEMPEL

```bash
# 1. Skapa plot brief
cat > my-thriller.json << EOF
{
  "title": "Isdrottningen",
  "genre": "psykologisk-thriller",
  "plotIdea": "En före detta olympisk skridskoåkare återvänder till sin hemstad...",
  "wordCount": 80000
}
EOF

# 2. Generera outline och karaktärer (Phase 0)
python3 run_noir.py \
  --project isdrottningen \
  --brief my-thriller.json \
  --provider claude

# 3. Granska i dashboard
open books/isdrottningen/dashboard.html

# 4. Skriv kapitel 1
python3 run_noir.py \
  --project isdrottningen \
  --chapter 1 \
  --provider claude

# 5. Läs kapitlet i dashboard
open books/isdrottningen/dashboard.html
# Klicka på Kapitel 1, läs texten, se Ellis' review

# 6. Om du vill skriv om (revision):
# - Redigera kapitlet manuellt i dashboard
# - Eller be Sage skriva om baserat på feedback

# 7. Fortsätt med fler kapitel
python3 run_noir.py --project isdrottningen --chapter 2 --provider claude
python3 run_noir.py --project isdrottningen --chapter 3 --provider claude
# etc...
```

---

## 🔧 TEKNISKA DETALJER

### Agent Architecture

Alla agenter ärver från `BaseAgent`:

```python
class BaseAgent:
    def __init__(self, agent_name, agent_type, llm_client)
    def execute(self, context) -> dict
    def build_prompt(self, context) -> str
    def call_llm(self, prompt, max_tokens) -> str
    def extract_json(self, text) -> dict
```

Varje agent:
1. Läser sin `.md` fil (prompt template)
2. Injicerar kontext (plot, karaktärer, etc.)
3. Anropar LLM
4. Parsar JSON-svar
5. Returnerar strukturerad data

### Orchestrator

```python
orchestrator = Orchestrator(project_name, llm_provider, api_key)

# Phase 0: Creative Planning
data = orchestrator.phase0_narrative_validation(plot_brief)

# Phase 1: Writing
data = orchestrator.phase1_write_chapter(data, chapter_num=1)

# Phase 3: Quality
data = orchestrator.phase3_quality_review(data, chapter_num=1)

# Full pipeline
data = orchestrator.run_full_pipeline(plot_brief)
```

### Data Flow

```
plot_brief (JSON)
  ↓
Phase 0 agents
  ↓
project_data (JSON med outline, characters, setting, voice)
  ↓
Sage writer
  ↓
project_data + chapter text
  ↓
Ellis reviewer
  ↓
project_data + chapter + review
  ↓
Sparas i books/<project>/data.json
  ↓
Dashboard genereras
```

---

## 🐛 FELSÖKNING

### "ModuleNotFoundError: No module named 'anthropic'"

```bash
pip install anthropic
```

### "No ANTHROPIC_API_KEY found"

```bash
export ANTHROPIC_API_KEY='your-key'
# Eller använd --provider mock för test
```

### "Could not parse JSON from agent"

Agenten returnerade inte valid JSON. Kör med `--provider mock` först för att testa strukturen.

### Agent genererar konstiga svar

- Kontrollera att `.md` prompt-filerna finns i `agents/<type>/<name>.md`
- Testa med `--provider mock` först
- Öka `max_tokens` i agent-koden om output verkar trunkerad

---

## 📚 NÄSTA STEG

1. **Testa med mock:**
   ```bash
   python3 run_noir.py --project test --brief example-plot-brief.json --provider mock --full
   ```

2. **Testa med Claude:**
   ```bash
   export ANTHROPIC_API_KEY='...'
   python3 run_noir.py --project test --brief example-plot-brief.json --provider claude
   ```

3. **Bygg din bok:**
   - Skapa din plot-brief.json
   - Kör Phase 0
   - Granska i dashboard
   - Skriv kapitel ett i taget
   - Använd feedback för revision

4. **Utöka systemet:**
   - Lägg till fler agenter (Blake, Jordan, etc.)
   - Implementera revision-loops
   - Lägg till export till DOCX/PDF
   - Integrera med webgränssnitt

---

## 🎉 SAMMANFATTNING

Du har nu ett **komplett AI-drivet bokskrivningssystem**!

✅ **Orkestrering** - `run_noir.py` koordinerar allt
✅ **AI-Integration** - Riktiga Claude/GPT API-anrop
✅ **10 Agenter** - Fullt implementerade i Python
✅ **Pipeline** - Från brief → färdig bok
✅ **Kvalitetskontroll** - Automatisk granskning
✅ **Dashboard** - Visualisering av progress

**Börja skriva din bok nu!** 🚀📚
