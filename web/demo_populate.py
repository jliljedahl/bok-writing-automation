#!/usr/bin/env python3
"""
Populate demo project with sample data
"""

from update_dashboard import DashboardUpdater

# Initialize demo project
updater = DashboardUpdater("demo-projekt")

# Set basic info
data = updater.load_data()
data['title'] = "Skuggornas Stad"
data['author'] = "Demo Författare"
data['structure'] = "Hybrid (18 kapitel)"
data['currentPhase'] = "Fas 2: Writing (Demo)"
updater.save_data(data)

# Add outline
outline = {
    "logline": "En utbränd kriminalinspektör i Ystad måste konfrontera sitt mörka förflutna när en serie mord avslöjar en konspirationsteori som sträcker sig in i poliskåren själv.",
    "hook": "Den första kroppen tillhör någon från Martins förflutna - en person han trodde var död sedan fem år tillbaka.",
    "twist": "Hans egen partner, som han litat på i åratal, är faktiskt den som orkesterat hela komplotten.",
    "resolution": "Martin måste offra sin karriär och säkerhet för att avslöja sanningen, men finner slutligen fred i att göra rätt, inte det enkla.",
    "acts": [
        {
            "number": 1,
            "title": "Akt I: Upptäckten",
            "description": "Martin hittar den första kroppen och dras motvilligt in i ett fall som blir allt mer personligt.",
            "beats": [
                {
                    "name": "Opening Image",
                    "description": "Martin ensam på sin lägenhet, utbränd och cynisk. Överväger pensionering.",
                    "chapter": 1
                },
                {
                    "name": "Inciting Incident",
                    "description": "Kroppen hittas - det är Emma, hans gamla vän som 'dog' för 5 år sedan.",
                    "chapter": 2
                },
                {
                    "name": "Första dörrtröskel",
                    "description": "Martin bestämmer sig för att undersöka på egen hand, trots varningar.",
                    "chapter": 4
                }
            ]
        },
        {
            "number": 2,
            "title": "Akt II: Jakten",
            "description": "Martin gräver djupare medan faran stiger. Flera twist avslöjar att ingenting är som det verkar.",
            "beats": [
                {
                    "name": "Midpoint Twist",
                    "description": "Martin upptäcker att Emmas död var arrangerad - av någon inom polisen.",
                    "chapter": 9
                },
                {
                    "name": "All Is Lost",
                    "description": "Hans partner Lisa förråder honom och han är helt ensam.",
                    "chapter": 14
                }
            ]
        },
        {
            "number": 3,
            "title": "Akt III: Konfrontationen",
            "description": "Klimax där Martin måste riskera allt för att avslöja sanningen.",
            "beats": [
                {
                    "name": "Climax",
                    "description": "Konfrontation med Lisa i nedlagda fabriksområdet. Allt avslöjas.",
                    "chapter": 17
                },
                {
                    "name": "Resolution",
                    "description": "Martin förlorar sitt jobb men vinner sin själ tillbaka. Ny början.",
                    "chapter": 18
                }
            ]
        }
    ]
}

updater.update_outline(outline)

# Add characters
characters = [
    {
        "name": "Martin Sundberg",
        "role": "Protagonist",
        "age": 42,
        "occupation": "Kriminalinspektör, Ystad Polisstation",
        "description": "Utbränd och cynisk polis med 20 års erfarenhet. Melankolisk, introvert, men har ett djupt rättvisetänk som aldrig släppt taget.",
        "arc": {
            "start": "Cynisk, isolerad, undviker känslor och relationer. Bara går igenom motionerna på jobbet.",
            "middle": "Tvingas konfrontera sitt förflutna när gamla vänner och fiender dyker upp. Börjar känna igen.",
            "end": "Accepterar sin sårbarhet och vad han måste offra för att göra rätt. Hittar mening igen."
        },
        "ghost": "Misslyckades rädda sin partner för 5 år sedan (tror han). Skulden har förlamat honom.",
        "want": "Lösa detta sista fall och gå i pension utan mer blod på sina händer.",
        "need": "Förlåta sig själv och inse att han inte kan kontrollera allt. Släppa taget om skulden."
    },
    {
        "name": "Lisa Eklund",
        "role": "Antagonist (dold)",
        "age": 38,
        "occupation": "Kriminalinspektör, Martins partner",
        "description": "Verkar vara den perfekta partnern - smart, lojal, stöttande. Men under ytan är hon briljant manipulativ.",
        "arc": {
            "start": "Verkar vara Martins enda allierad och vän. Den som håller honom vid liv.",
            "middle": "Små tecken på att något inte stämmer. Vet för mycket. Är alltid där vid fel tidpunkt.",
            "end": "Avslöjas som hjärnan bakom hela komplotten. Konfronteras och arresteras."
        },
        "ghost": "Hennes bror dödades av korrupta poliser för 10 år sedan. Hon har hämtat sig sedan dess.",
        "want": "Hämnas på de korrupta poliserna och det system som skyddade dem.",
        "need": "Släppa hatet och hitta fred (men vägrar - därför antagonist)."
    },
    {
        "name": "Emma Lindqvist",
        "role": "Offer / Katalysator",
        "age": 36,
        "occupation": "Tidigare journalist (död när boken börjar)",
        "description": "Martins gamla vän från universitetet. Grävde i korruption inom polisen. 'Dog' i bilolycka för 5 år sedan.",
        "arc": {
            "start": "Död (tror alla). Hennes kropp hittas i Kapitel 1.",
            "middle": "Genom flashbacks ser vi vad hon upptäckte om poliskorruptionen.",
            "end": "Hennes dödsorsak avslöjas - hon mördades av Lisa."
        },
        "ghost": None,
        "want": "Avslöja sanningen om korruptionen (innan hon dog).",
        "need": None
    }
]

updater.update_characters(characters)

# Add sample chapters
chapter_1_text = """KAPITEL 1: KROPPEN

Kroppen hittades en tisdag.

Det var inte första gången Martin Sundberg såg en död människa, men det var första gången han såg en som han känt. Emma Lindqvist låg på rygg i snön, ögonen öppna, och stirrade upp mot den grå decemberhimlen. Blodet hade frusit till is runt hennes huvud.

Han visste redan då att ingenting skulle bli som det var.

"Martin?"

Lisa Eklunds röst bakom honom. Hans partner i fem år. Den enda som fortfarande orkade med honom.

"Känner du henne?"

Martin nickade långsamt. Snön föll tyst runt dem. Ystad var vackert i december, på det där melankoliska svenska sättet. Grått hav, grå himmel, vita tak.

"Hon heter Emma," sa han. "Emma Lindqvist."

"Varför känner jag igen det namnet?"

"Hon dog för fem år sedan." Martins röst var flat. "Bilolycka."

Lisa kom närmare, såg ner på kroppen. "Uppenbarligen inte."

De stod tysta en stund. Vinden drog in från havet, salt och kall. Martin drog kavajen tätare om sig. Fyrtiotvå år gammal och han frös som en gammal gubbe numera.

"Jag tar det här," sa han slutligen.

"Martin—"

"Jag tar det här." Han mötte hennes blick. "Hon var min vän."

Lisa studerade honom. Han kunde se beräkningarna i hennes ögon. Slutligen nickade hon.

"Okej. Vi gör det tillsammans."

Han skulle senare komma att tänka på den stunden. På hur naturligt hon ljög."""

updater.update_chapter(
    chapter_number=1,
    version_name="Draft v1",
    text=chapter_1_text,
    metadata={
        "author": "Sage",
        "quality": 7.8,
        "pov": "Martin Sundberg",
        "location": "Ystad, Sverige",
        "timeOfDay": "Morgon",
        "season": "December",
        "factVerification": 96,
        "continuityErrors": 0
    }
)

chapter_1_v2 = chapter_1_text + "\n\n[Förbättrad med mer sensoriska detaljer och emotionell djup]"

updater.update_chapter(
    chapter_number=1,
    version_name="Draft v2",
    text=chapter_1_v2,
    metadata={
        "author": "Sage (efter Ellis feedback)",
        "quality": 8.3
    }
)

updater.update_chapter(
    chapter_number=1,
    version_name="FINAL",
    text=chapter_1_v2,
    metadata={
        "author": "Sage (efter QA)",
        "quality": 8.5
    }
)

# Add work-in-progress chapter
chapter_2_text = """KAPITEL 2: SPÖKET

[Draft v1 - Pågående arbete]

Fem år.

Martin satt vid sitt skrivbord på polisstationen och stirrade på Emmas fil på skärmen. Bilolycka, oktober 2020. Utreds, avslutad. Inga misstankar om brott.

Men nu låg hon i bårhuset. Igen. Eller fortfarande?

"Kaffe?"

Han ryckte till. Lisa stod i dörröppningen med två muggar.

"Tack." Han tog emot den ena. Varm. Lisa visste alltid exakt hur han ville ha det.

Hon satte sig mitt emot honom, studerade skärmen.

"Vad vet vi?" frågade hon.

"Inte mycket. Kroppen... kroppen är färsk. Död sedan högst ett dygn." Han svalde. "Så antingen..."

"...antingen har hon varit gömd i fem år," avslutade Lisa. "Eller så dog hon aldrig."

Martin nickade. Huvudet värkte. Han hade inte sovit på tjugofyra timmar.

[FORTSÄTTNING PÅGÅR...]"""

updater.update_chapter(
    chapter_number=2,
    version_name="Draft v1",
    text=chapter_2_text,
    metadata={
        "author": "Sage",
        "quality": None
    }
)

# Update phase
updater.set_phase("Fas 2: Writing (2 av 18 kapitel)")

print("\n🎉 Demo-projekt populerat med exempel-data!")
print(f"\n📂 Öppna dashboard:")
print(f"   file:///home/user/noir-book-system/books/demo-projekt/dashboard.html")
print(f"\n📊 Data:")
print(f"   - 1 bok: Skuggornas Stad")
print(f"   - 3 karaktärer (Martin, Lisa, Emma)")
print(f"   - Komplett outline (3 akter, plot beats)")
print(f"   - 2 kapitel (1 färdigt, 1 pågående)")
