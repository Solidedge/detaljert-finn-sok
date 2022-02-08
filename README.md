# Detaljert Finn.no søk
Enkelte jobber har ikke universale stillingstitler, og kan være vanskelig å finne uten å leite gjennom en mengde urelevante stillinger. Andre stillinger drukner i en mengde urelevante stillinger med samme ord. Dette skriptet genererer en URL til finn.no og åpner den i ønsket nettleser. Søket består av konkrete og definerte søkeord og mangel av enkelte søkeord. Styrken til skriptet kommer til rette når søkene blir lange og komplekse. Her forholder man seg til en enkelt linje om gangen.


## Eksempel
Ta utgangspunkt i at du har utdanning innen elektronikk. Et ordinært søk vil gi en haug med stillinger som butikkmedarbeider hos Elkjøp, Power og kanskje noen el.-installatører. For å eliminere de urelevante stillingene legger man inn "NOT" og "AND" i søket.


## Hvordan bruke skriptet
Fyll inn søkefraser i txt-filen "search_phrases.txt". Hver linje kombineres med ELLER-logikk.

| Frase # (linje i txt)   | Søkefrase |
|----------|---------------|
| 1 | Elektronikk NOT Elkjøp |
| Resultat | (Elektronikk NOT Elkjøp) |

| Frase # (linje i txt)   | Søkefrase |
|----------|---------------|
| 1 | Elektronikk NOT Elkjøp |
| 2 | Musikk NOT Platekompaniet |
| 3 | Elektronikk AND Kretsdesign |
| 4 | "C-programmering" |
| Resultat | (Elektronikk NOT Elkjøp) OR (Musikk NOT Platekompaniet) OR (Elektronikk AND Kretsdesign) OR ("C-programmering") |

Anførselstegn kan brukes for å finne eksakte ord kombinasjoner. For å forenkle prosessen med å sette sammen flere søkefraser, så kan man legge inn en #, for å stoppe sammenslåingen av frasene. Slik at man kan se resultatet av en og en linje.


### Altomfattende Ikke-fraser
For en elektronikk ingeniør er nok butikkmedarbeiderstillinger hos en forbrukerelektronikk butikk alltid uinterressant. Disse frasene kan legges inn i txt-filen "no_no_words.txt".
