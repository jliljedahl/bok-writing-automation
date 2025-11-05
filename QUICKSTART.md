# NOIR - Snabbstartsguide

## 🎯 Starta ditt första bokprojekt

### Steg 1: Fyll i Plot Intake
```bash
cd books
mkdir min-forsta-bok
cd min-forsta-bok
mkdir plot characters research chapters tracking

# Kopiera plot-intake mallen
cp ../../templates/plot-intake.md plot/plot-intake.md

# Fyll i plotten i din editor
```

### Steg 2: Kör Fas 1 - Kreativ Planering (3-5 timmar)

**Använd Claude Code med Task-verktyget:**

```
"Jag har fyllt i plot-intake för min bok. Kör FAS 1 med alla fyra agenter:

1. Harper - Skapa plotstruktur baserat på min plot-intake
2. Morgan - Utveckla djupa karaktärsprofiler  
3. Quinn - Skapa dialogguider per karaktär
4. River - Research och beskriv alla viktiga platser

Använd agentdefinitionerna i agents/ och följ workflows/phase1-creative.md"
```

**Förväntat resultat:**
- `plot/plotstruktur.md` från Harper
- `characters/protagonist.md`, `antagonist.md`, `supporting-cast.md` från Morgan
- `characters/dialogue-guides.md` från Quinn
- `research/miljöguide.md` från River

### Steg 3: Skriv Kapitel 1 - Fas 2 (6-10 timmar)

```
"Nu ska jag skriva Kapitel 1. Kör FAS 2:

1. Sage läser allt material från Fas 1
2. Sage planerar kapitlet (scene list, hooks)
3. Sage skriver Draft v1 (4,000-7,000 ord)
4. Blake polerar action-scener
5. Sage integrerar Blakes förbättringar

Följ workflows/phase2-writing.md och spara i chapters/chapter-01/"
```

### Steg 4: Revidera - Fas 3 (2-3 timmar)

```
"Kapitel 1 Draft v1 är klar. Kör FAS 3:

1. Ellis granskar strukturen och ger feedback
2. Sage reviderar till Draft v2 baserat på Ellis

Följ workflows/phase3-revision.md"
```

### Steg 5: Kvalitetssäkra - Fas 4 (2-3 timmar)

```
"Kapitel 1 Draft v2 är klar. Kör FAS 4:

1. Finley verifierar alla fakta
2. Gray kontrollerar kontinuitet
3. Jordan analyserar spänning
4. Sage skapar FINAL med alla fixes

Följ workflows/phase4-qa.md"
```

### Steg 6: Upprepa för alla kapitel

**Kapitel 2-12:** Fas 2 → Fas 3 → Fas 4

**Total tid för 12 kapitel:** 125-210 timmar

---

## 💡 Tips för bästa resultat

### För Creative Team (Fas 1):
- **Var specifik i plot-intake** - ju mer detaljer, desto bättre output
- **Svenskt fokus** - ange region, stad, specifika platser
- **Komplex antagonist** - ge dem djup motivation

### För Writing Team (Fas 2):
- **Följ materialet** - Sage ska använda ALLTfrån Fas 1
- **Show don't tell** - visa genom handling, inte förklara
- **Blake för action** - låt Blake polera alla höjdpunkter

### För Quality Team (Fas 3-4):
- **Ta feedback seriöst** - Ellis ser vad som kan förbättras
- **Fixa alla kritiska fel** - Finley och Gray hittar fel som måste fixas
- **Spänning är nyckeln** - Jordan ser vad som gör boken page-turner

---

## 📊 Förväntat kvalitet

**Progression:**
- Draft v1: 7.0-7.5/10
- Draft v2: 7.5-8.5/10  
- FINAL: 8.0-9.0/10

**Måttstrecken:**
- 95%+ faktaverifierade påståenden
- 0 kritiska kontinuitetsfel
- Dynamisk spänningskurva
- Distinkta karaktärsröster
- Autentiskt svenskt

---

## 🚀 Avancerad användning

### Parallella agents (Fas 1):
```
"Kör Harper, Morgan, Quinn och River SAMTIDIGT i Task-verktyget med parallella calls"
```

### Återanvänd för ny bok:
1. Skapa ny mapp i `books/`
2. Kopiera plot-intake
3. Fyll i ny plot
4. Kör Fas 1-4 igen!

---

## ❓ Felsökning

**Problem:** Agenter följer inte svenska konventioner
**Lösning:** Referera explicit till agentdefinitioner (`agents/creative/harper.md` etc.)

**Problem:** Kontinuitetsfel uppstår
**Lösning:** Se till att Gray uppdaterar kontinuitets-databas efter varje kapitel

**Problem:** Spänningen är för platt
**Lösning:** Låt Jordan analysera tidigt och justera innan många kapitel skrivits

---

**Lycka till med din bok!** 📚✍️

