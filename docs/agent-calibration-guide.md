# AGENT CALIBRATION GUIDE

**Syfte:** Justera agent-instruktioner när output inte når kvalitetsmål.

**När använda:** Efter Quality Gate failure eller Pilot Chapter evaluation visar svagheter.

---

## 🎯 KALIBRERINGS-FILOSOFI

**Agents är INTE perfekta från början.**

De behöver:
- Tydligare instruktioner
- Bättre exempel
- Mer specifik guidance
- Iterativ förbättring

**Kalibrering ≠ Misslyckande**
**Kalibrering = Optimering**

---

## 📊 DIAGNOSTIK: Identifiera problemet

### STEG 1: Vilket agent har problemet?

Titta på Quality Gate scores per agent:

| Agent | Score | Status | Problem? |
|-------|-------|--------|----------|
| Harper | 8.5/10 | 🟢 | Nej |
| Morgan | 7.2/10 | 🟡 | JA - Under minimum 7.5 |
| Quinn | 9.0/10 | 🟢 | Nej |
| ... | ... | ... | ... |

**Identifierad problemagent:** Morgan

---

### STEG 2: VAD är problemet specifikt?

**Dåligt:**
> "Morgan's output är dålig"

**Bra:**
> "Morgan's karaktärsarcs är för ytliga - protagonisten har ingen tydlig transformation från Akt I till Akt III. Ghost/trauma är nämnt men inte integrerat i beteende."

**Specifika diagnostik-frågor per agent:**

#### Harper (Plotarkitekt):
- [ ] Är plotstrukturen obalanserad? (Akt-proportioner fel)
- [ ] Saknas viktiga plot beats?
- [ ] Är spänningskurvan platt?
- [ ] Är red herrings för uppenbara/svaga?
- [ ] Är twist inte hintat tillräckligt?

#### Morgan (Karaktärpsykolog):
- [ ] Är karaktärsarcs för ytliga?
- [ ] Saknar karaktärer Ghost/trauma?
- [ ] Är antagonisten endimensionell?
- [ ] Är alla karaktärer för lika varandra?
- [ ] Är motivationer ologiska?

#### Quinn (Dialogmästare):
- [ ] Låter alla karaktärer likadana?
- [ ] Är dialekter felaktiga/stereotyper?
- [ ] Saknas subtext?
- [ ] Är dialoger för "on the nose"?
- [ ] För mycket exposition i dialog?

#### River (Miljöspecialist):
- [ ] Är platsbeskrivningar för generiska?
- [ ] Saknas sensoriska detaljer (bara visuellt)?
- [ ] Är väder/årstid inkonsekvent?
- [ ] Känns det inte svenskt?
- [ ] För lite atmosfär?

#### Sage (Huvudförfattare):
- [ ] För mycket "tell", för lite "show"?
- [ ] Är pacing monotont?
- [ ] Följer inte Creative Team's material?
- [ ] Svaga hooks?
- [ ] Platt språk?

#### Blake (Scenbyggare):
- [ ] Action-scener är förvirrande?
- [ ] Saknas spatial awareness?
- [ ] För långsamma (inte kinetic)?
- [ ] Amerikansk action (inte svensk kontext)?

#### Ellis (Utvecklingsredaktör):
- [ ] Feedback är för vag?
- [ ] Missar stora problem?
- [ ] Ratings är inkonsistenta?

#### Finley (Faktaverifierare):
- [ ] Missar uppenbara faktafel?
- [ ] Verifierar inte tillräckligt?
- [ ] Fel källor?

#### Gray (Kontinuitetsansvarig):
- [ ] Missar kontinuitetsfel?
- [ ] Kontinuitets-databas inte uppdaterad?
- [ ] Tracking är ofullständig?

#### Jordan (Spänningsanalytiker):
- [ ] Spänningsbedömning är off?
- [ ] Missar pacing-problem?
- [ ] Förslag är inte användbara?

---

## 🔧 KALIBRERINGSSTRATEGIER

### STRATEGI 1: Förtydliga instruktioner

**Problem:** Agent förstår inte VAD som förväntas

**Lösning:** Gör instruktioner mer explicit och specifik

**Exempel - Morgan's karaktärsarcs:**

**FÖRE (vag):**
```
Skapa karaktärsutveckling genom berättelsen
```

**EFTER (specifik):**
```
Skapa karaktärsutveckling enligt följande template:

1. AKT I (WHO THEY ARE):
   - Startpunkt: Konkret beskrivning av protagonists beteende, värderingar
   - Ghost: Specifik händelse från förr (inte vag "trauma")
   - Want: Vad protagonist tror hen vill (ytligt)
   - Need: Vad protagonist faktiskt behöver (djupt)

2. AKT II (WHO THEY BECOME):
   - Plot events som DRIVER förändring (inte random)
   - Inre konflikt: Want vs Need collision
   - Gradvis förändring (inte sudden)

3. AKT III (WHO THEY ARE NOW):
   - Transformation: Konkret hur protagonist är annorlunda
   - Want vs Need resolution: Fick hen båda? Bara Need?
   - Earned growth: Bevisat genom actions, inte bara sagt

EXEMPEL:
Protagonist Martin:
- START: Cynisk, isolerad, "jag gör bara mitt jobb"
- EVENT (Kap 3): Upptäcker offer var barndomsvän → personal
- CONFLICT: Vill bara lösa fallet (Want) vs behöver konfrontera sitt eget trauma (Need)
- END: Öppnar sig, accepterar sitt förflutna, "vissa saker är värda att slåss för"
```

---

### STRATEGI 2: Ge konkreta exempel

**Problem:** Agent förstår konceptet men inte HUR

**Lösning:** Ge "good" vs "bad" exempel

**Exempel - Quinn's dialog differentiation:**

**FÖRE:**
```
Varje karaktär ska ha distinkt röst
```

**EFTER:**
```
Varje karaktär ska ha distinkt röst. Test: Kan du gissa VEM som sa detta utan attribut-tag?

❌ BAD (alla låter samma):
"Jag tror att vi borde undersöka detta närmare."
"Jag håller med. Vi borde verkligen göra det."
"Ja, det verkar vara en bra idé."

✅ GOOD (distinkta röster):
MARTIN (cynisk, kortfattad): "Kolla det."
EMMA (formell, reflektiv): "Det vore intressant att undersöka vidare, tycker jag."
BENGT (gammal, dialekt): "Jodå, man får väl ta en titt då."

Märker du skillnaden?
- Martin: Kommando, 2 ord, inga artighetsfraser
- Emma: Längre, "tycker jag", reflektiv
- Bengt: Norrländska "jodå", "man får väl", tystlåten
```

---

### STRATEGI 3: Lägg till checklista

**Problem:** Agent glömmer viktiga element

**Lösning:** Konkret checklista att följa

**Exempel - River's platsbeskrivningar:**

**FÖRE:**
```
Beskriv platser detaljerat
```

**EFTER:**
```
För varje plats, följ denna checklista:

MUST-HAVES:
- [ ] Visuell beskrivning (färger, former, ljus)
- [ ] Ljud (vad HÖRS här?)
- [ ] Lukt (vad LUKTAR det?)
- [ ] Känsel (temperatur, vind, textur)
- [ ] Atmosfär (vilken KÄNSLA ger platsen?)
- [ ] Årstid-specifika detaljer (snö? löv? blomning?)
- [ ] Tidsspecifikt (morgon? kväll? påverkar ljus)
- [ ] Minst ETT unikt detalj som gör platsen minnesvärd

SVENSKA KONTEXT:
- [ ] Realistiskt för svensk region
- [ ] Väder stämmer för årstid
- [ ] Arkitektur är svensk (inte amerikansk suburbs)

Om ALLA checklist-items inte är täckta → gå tillbaka och fyll i!
```

---

### STRATEGI 4: Höj quality gate minimums

**Problem:** Agent når minimum men inte excellent

**Lösning:** Höj ribban gradvis

**Exempel:**

**Första iteration:**
- Morgan minimum: 7/10 → Når 7.2/10 → OK men inte great

**Andra iteration (efter kalibrering):**
- Morgan minimum: 7.5/10 → Når 8.0/10 → Mycket bättre!

**Tredje iteration:**
- Morgan minimum: 8.0/10 → Når 8.3/10 → Excellent!

**Strategi:** Höj minimum med +0.5 efter varje framgångsrik iteration.

---

### STRATEGI 5: Lägg till negativa constraints

**Problem:** Agent gör specifika misstag upprepat

**Lösning:** Explicit "UNDVIK detta"

**Exempel - Sage's "show don't tell":**

**FÖRE:**
```
Show don't tell
```

**EFTER:**
```
Show don't tell. Undvik dessa vanliga "tell"-misstag:

❌ UNDVIK:
"Han var arg på henne för att hon ljög."
"Huset var gammalt och förfallet."
"Hon kände sig rädd."

✅ GÖR ISTÄLLET:
"Han mötte inte hennes blick. 'Jaså,' sa han och vände sig bort."
"Färgen flagade från fasaden. Från takrännorna hängde vissna löv."
"Hennes händer darrade när hon nådde efter dörrhandtaget."

SE SKILLNADEN?
- TELL = Säg känslor/fakta direkt
- SHOW = Visa genom beteende, detaljer, dialog

Om du hittar "var [adjektiv]" eller "kände sig [känsla]" → SKRIV OM!
```

---

### STRATEGI 6: Lägg till peer-review

**Problem:** Agent har blind spots

**Lösning:** En annan agent granskar först

**Exempel:**

**FÖRE:**
Sage skriver → Ellis granskar

**EFTER:**
Sage skriver → Blake granskar action → Quinn granskar dialog → SEDAN Ellis granskar structure

**Multi-layer QA hittar fler problem!**

---

## 📋 KALIBRERINGS-PROCESS (steg-för-steg)

### STEG 1: Diagnostik (30 min - 1 timme)
1. Identifiera vilken agent har problem
2. Specifiera exakt VAD problemet är
3. Hitta exempel på dålig output
4. Dokumentera i `calibration-log.md`

### STEG 2: Välj kalibreringsstrategi (15 min)
1. Läs igenom Strategi 1-6 ovan
2. Välj 1-3 strategier som passar problemet
3. Planera exakt vad som ska ändras

### STEG 3: Uppdatera agent-instruktioner (1-2 timmar)
1. Öppna agent-fil (t.ex. `agents/creative/morgan.md`)
2. Implementera valda strategier
3. Lägg till exempel, checklistor, constraints
4. Dokumentera vad som ändrats

### STEG 4: Testa på pilot (3-8 timmar)
1. Kör agenten på ETT test-kapitel
2. Mät kvalitet (når vi högre score?)
3. Jämför FÖRE vs EFTER

### STEG 5: Utvärdera (30 min)
**Förbättring?**
- ✅ JA (+0.3-0.5 poäng) → Behåll ändringar, fortsätt
- ⚠️ LITE (+0.1-0.2 poäng) → Mer kalibrering behövs
- ❌ NEJ (ingen förbättring) → Prova annan strategi

### STEG 6: Dokumentera (15 min)
1. Uppdatera `calibration-log.md`
2. Commit ändringar till git
3. Kommunicera till team

**Total tid för EN kalibrering: 5-12 timmar**

---

## 📝 CALIBRATION LOG TEMPLATE

```markdown
# AGENT CALIBRATION LOG

## Kalibrering #1: Morgan - Karaktärsarcs för ytliga

**Datum:** 2025-11-07
**Agent:** Morgan (Karaktärpsykolog)
**Problem:** Karaktärsarcs når bara 7.2/10, under minimum 7.5/10

### Diagnostik
**Specifikt problem:**
Protagonistens transformation från Akt I till Akt III är otydlig. Ghost/trauma nämns men inte integrerat i beteende. Want vs Need är inte tydligt separated.

**Exempel på dålig output:**
```
Protagonist Martin är utbränd i början och mindre utbränd i slutet.
```

Vad saknas: Konkret beteende, specifika events som driver change, earned transformation.

### Strategi vald
- Strategi 1: Förtydliga instruktioner (template för arcs)
- Strategi 2: Ge konkreta good/bad exempel
- Strategi 3: Checklista för character arcs

### Ändringar gjorda
**Fil:** `agents/creative/morgan.md`

**Tillagt:**
1. Explicit template för Akt I/II/III character development
2. 3 exempel på good vs bad arcs
3. Checklista för varje arc-element
4. Exempel från "Tre år med AI" projektet

**Commit:** `abc123def - Calibrate Morgan: Add detailed arc template and examples`

### Test-resultat
**Testade på:** Pilot Kapitel 1
**FÖRE-score:** 7.2/10
**EFTER-score:** 8.1/10
**Förbättring:** +0.9 poäng ✅

**Observation:**
Morgan's output är nu mycket mer strukturerad. Protagonistens arc har tydlig start, milestones drivna av plot events, och earned transformation. Want vs Need är tydligt separated.

### Beslut
✅ **BEHÅLL ÄNDRINGAR**

Kalibreringen lyckades. Morgan når nu konsekvent >8.0/10.

### Nästa steg
Monitorera Morgan's output i nästa 2-3 kapitel för att säkerställa konsistens.

---

## Kalibrering #2: ...

[Fortsätt för varje kalibrering]
```

---

## 🎯 VANLIGA KALIBRERINGSBEHOV

### Problem: "Output är för generisk"
**Agenter som ofta har detta:** Harper, River, Sage

**Lösning:**
- Lägg till krav på specificity (antal unika detaljer)
- Ge exempel på generic vs specific
- Checklista för uniqueness

---

### Problem: "Missar svenska kontext"
**Agenter som ofta har detta:** Quinn, River, Finley

**Lösning:**
- Starkare svenska autenticitet-checklista
- Negativa constraints (lista amerikanska misstag att undvika)
- Exempel från svenska deckare

---

### Problem: "Följer inte material från andra agents"
**Agenter som ofta har detta:** Sage, Blake

**Lösning:**
- Explicit requirement att läsa OCH referera till tidigare material
- Checklista: "Har jag använt X från Harper? Y från Morgan?"
- Påminnelse att integration är kritisk

---

### Problem: "Ratings är inkonsistenta"
**Agenter som ofta har detta:** Ellis, Jordan

**Lösning:**
- Förtydliga rating-scale med konkreta exempel
- Kalibrering mot externa benchmarks
- Blind rating-test (samma kapitel två gånger, ska ge samma score)

---

## 💡 BEST PRACTICES

### ✅ GÖR:
- Var specifik i diagnostik
- Testa EN ändring i taget (så du vet vad som fungerade)
- Dokumentera allt i calibration log
- Ge agenten 2-3 chanser efter kalibrering innan du ger upp
- Fira förbättringar (+0.5 poäng är STORT!)

### ❌ UNDVIK:
- Vag feedback ("gör bättre")
- Ändra allt samtidigt (vet inte vad som hjälpte)
- Ge upp efter första misslyckade kalibrering
- Glömma dokumentera (förlorar lärdomar)

---

## 📈 KALIBRERINGSKURVA

**Typisk progression:**

```
Agent Quality
10 |                            *CALIBRATED
 9 |                      *
 8 |                *
 7 |          *
 6 |    *
 5 | *
   |_____________________________
   Iter: 0  1  2  3  4  5  6

Iteration 0: Baseline (5-6/10)
Iteration 1: +1.0 poäng (first calibration, big wins)
Iteration 2: +0.5 poäng (refinement)
Iteration 3: +0.3 poäng (fine-tuning)
Iteration 4-6: +0.1-0.2 poäng each (diminishing returns)
```

**Förvänta:**
- Första kalibrering: Stora förbättringar (+0.5-1.0)
- Andra-tredje: Medium förbättringar (+0.3-0.5)
- Efter det: Små förbättringar (+0.1-0.2)

**När sluta kalibrera:** När agent konsekvent når 8.5-9.0/10.
Perfection (10/10) är orealistiskt - fokusera på "excellent enough"!

---

**Agent Calibration = Continuous improvement. Agents get better with every iteration.**
