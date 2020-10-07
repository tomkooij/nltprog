---
layout: default
---
# Algoritmen

Computers laten pas echt zien wat ze kunnen als de oplossing van een probleem niet goed uitgedrukt kan worden door een formule. Bij programmeren werken we aan het verzinnen en uitschrijven van *algoritmes*, die precies specificeren hoe een probleem stap-voor-stap opgelost moet worden. Een belangrijk aspect van algoritmen is dat ze werken voor verschillende invoer. In het filmpje hieronder moet het algoritme het juiste antwoord opleveren als er 0, 1, 2, 3, 4, enz. mensen in de kamer zijn.

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/6hfOvs8pY1k" frameborder="0" allowfullscreen="true"></iframe>
</figure>

In het hoofdstuk [basiselementen]({{site.baseurl}}/python/basiselementen) heb je een aantal **instructies** (**statements**) geleerd waar Python mee om kan gaan:

- de `print`-instructie, om boodschappen aan de gebruiker door te geven
- de `input`-instructie, om informatie van de gebruiker op te vragen
- de `=`-operator, om variabelen te definiëren of te wijzigen

Daarnaast heb je kennis gemaakt met operators die gebruikt worden om expressies samen te stellen. Dit was al genoeg om een werkend programma te schrijven. We gaan het nu interessanter maken door uitzonderingen en herhaling toe te staan.
# Voorwaardelijke instructies

In de voorgaande programma's schreven we scriptjes die regel voor regel van boven naar beneden werden uitgevoerd. Een soort stapsgewijze handleiding. Programma's worden interessanter als we *uitzonderingen* willen beschrijven.

<figure class="video_container">
  <iframe src="https://player.vimeo.com/video/287244672" frameborder="0" allowfullscreen="true"></iframe>
</figure>

In dit filmpje wordt de volgende structuur uitgelegd, zorg dat je deze *helemaal* snapt:

    leeftijd = input("Wat is je leeftijd?")
    leeftijd = int(leeftijd)

    if leeftijd < 18 or leeftijd >= 65:
        print("Je krijgt korting!")
    else:
        print("Je krijgt helaas geen korting")

## Details

Een `if`-statement in Python kent de volgende structuur:

    if conditie:
        code

Een **voorwaarde (condition)** kent uiteindelijk maar twee mogelijke opties. In Python zijn dit `True` en `False` (dit noemen we "boolean" waardes, naar [George Boole](https://en.wikipedia.org/wiki/Boolean_algebra#Values)). In de code hierboven is deze boolean het resultaat de expressie `balance - expense > 0`. Hier wordt gebruik gemaakt van de vergelijkingsoperator `>`. Deze operator vergelijkt twee waarden, in dit geval de uitkomst van `balance - expense` en `0`, en produceert een boolean. Afhankelijk van de uitkomst, dat kan dus zijn `True` of `False`, wordt de code die bij de `if`-statement hoort uitgevoerd.

De `:` op regel 5 hierboven laat zien dat bij de `if` een **codeblok** hoort. Dat is dus precies het deel van de code dat slechts wordt uitgevoerd als aan de voorwaarde is voldaan. Zo'n blok bestaat vaak uit meerdere regels code, en om duidelijk te maken welke regels dat zijn, gebruik je **indentatie**. Dat is een aantal spaties of tabs van de kantlijn af. In de code hierboven hebben we vier spaties gebruikt om aan te geven dat regel 6 bij het `if`-statement hoort. Omdat regel 8 weer meer naar links staat, is die regel niet meer afhankelijk van de uitkomst van de conditie op regel 5. Die regel wordt dus *onvoorwaardelijk* uitgevoerd.

## Meer operatoren

Mocht je meer nodig hebben dan de vergelijkingsoperatoren hierboven:

- `==`  gelijk aan (let op: een enkele = is toekennen, een dubbele vergelijken!)
- `!=`  ongelijk aan
- `>` 	groter dan
- `>=`	groter of gelijk aan
- `<` 	kleiner dan
- `<=`	kleiner dan of gelijk aan

## Combinaties van voorwaarden

Je kunt verschillende voorwaarden combineren. Als je wilt weten of een getal zich in een bepaald bereik bevindt (bijvoorbeeld tussen de 3 en de 39) dan kun je dat doen met `and`:

    x = 15
    x_min = 3
    x_max = 39
    if x > x_min and x < x_max:
        print("het getal", x, "bevindt zich tussen", x_min, "en", x_max)

Hier zijn de drie operators om voorwaarden te combineren:

- `not` ontkenning
- `and` combinatie (allebei moeten `True` zijn)
- `or` combinatie (één van beide moet `True` zijn)
# Loops

Soms is het handig om van een hele reeks getallen te bepalen of ze aan een bepaalde eis voldoen. Omdat zulk "dom werk" precies is wat een computer zo goed kan, is dat een basiselement in bijna alle programmeertalen. We noemen dit een **loop**.

## Herhaling

Als we tien keer iets willen doen, dan ziet het er bijvoorbeeld zo uit:

    for x in range(1, 11):
        print("hallo")

We gebruiken hier het commando `range()` met een begingetal en eindgetal om aan te geven hoe vaak de loop uitgevoerd zal worden. Daarbij telt Python van het begin *tot* het einde---dus niet *tot en met*!

Verder zie je dat we net als bij `if` weer kunnen inspringen om duidelijk te maken welke regel herhaald moet worden. Er staan hier vier spaties vóór `print`: dat is dus precies de instructie die meerdere malen uitgevoerd gaat worden.

## Voorbeelden van loops

<figure class="video_container">
  <iframe src="https://vimeo.com/album/5380755/embed" frameborder="0" allowfullscreen="true"></iframe>
</figure>

In het voorbeeld wordt de volgende structuur uitgelegd. Zorg dat je dit *helemaal* snapt:

    som = 0
    for getal in range(1, 10):
        som += getal
        print('het getal is nu: ', getal)
        print('de som is nu: ', som)

    print('De eind som is: ', som)

## Stapgrootte van een loop

Je kunt met `range` ook de stapgrootte opgeven. `for` telt dan zoals voorheen van begin tot einde, en neemt niet stappen van 1, maar van de grootte die jij hebt ingesteld. Dit ziet er zo uit:

    for getal in range(1, 100, 10):
        ...

Elke stap in de `for`-loop zal dan steeds 10 verder zijn dan de vorige. Denk even na welke stappen gemaakt zouden worden bij de loop hierboven; of neem de code over en zet er een `print` in om het gedrag te bestuderen.

## Soorten loops

Afhankelijk van de toepassing kies je een soort loop, zoals je in de filmpjes hierboven hebt gezien. In feite zijn `for` en `while` ook uitwisselbaar. Deze `for`-loop:

    for i in range(10):
        print("hi", i)

is gelijk aan de volgende `while`-loop:

    i = 0
    while i < 10:
        print("hi", i)
        i = i + 1

De `for`-loop is duidelijk wat compacter en zo sneller leesbaar. Dat is dus ook de loop die het vaakst gebruikt wordt. Maar toepassingen zoals gebruikersinvoer kun je eigenlijk alleen maar met een `while`-loop schrijven, dus deze heeft ook z'n nut.
