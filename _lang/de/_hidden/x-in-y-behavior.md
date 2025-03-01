---
nav_title: X in Y Filter-Verhalten
permalink: /x-in-y-behavior/
---

# Aktuelles X in Y Filter-Verhalten

Das Verhalten der Filter bleibt weitgehend gleich und wird durch die folgenden Merkmale definiert:

- Legen Sie Kalendertage fest (die um Mitternacht enden).
- "Tage" sind in UTC definiert.
- Der aktuelle UTC-Tag ist als "0" definiert.

## Anwendungsfall

Die folgende Kampagne wird am 16\. April um 21 Uhr gesendet. Die Zielgruppensegmentierung lautet "Mehr als 2 Käufe in den letzten 3 Tagen".

![Kampagnenzeitplan][1]

9 pm ET am 16\. April ist 1 Uhr UTC am 17\. April.

Der 17\. April wäre der Tag "0", der 16\. April wäre der Tag "1", der 15\. April wäre der Tag "2" und der 14\. April wäre der Tag "3".

Der Verlauf von 12 Uhr UTC am 14\. April bis zum aktuellen Zeitpunkt (1 Uhr UTC am 17\. April).
Das würde zu einem Zeitfenster führen, das 73 Stunden der Nutzerhistorie umfasst.

## An Kalendertagen

Kalendertage werden in mehr Funktionen als nur in den "X in Y"-Filtern verwendet:

- Nachrichtenplanung
- Frequency-Capping
- "X in Y"-Filter

`Calendar Days` beziehen sich auf den Zeitraum innerhalb eines nummerierten Tages, der um 12:00 Uhr beginnt und um 23:59 Uhr desselben Tages endet (12:00 Uhr am 8. Juni bis 23:59 Uhr am 8. Juni wäre ein einzelner Kalendertag).

### Frequency-Capping

Kalendertage werden verwendet, wenn Sie unter `Frequency Capping` "Tage" oder "Wochen" auswählen.

- `Every 1 day` begrenzt das Limit auf den aktuellen Kalendertag in der nutzerspezifischen Ortszeit (bis Mitternacht Ortszeit).
- `Every 2 days` begrenzt die Kappung auf den vorherigen und den aktuellen Kalendertag in der Ortszeit Ihres Benutzers (und endet um Mitternacht Ortszeit am aktuellen Kalendertag).

### Unternehmen & Ortszeit

Der aktuelle Kalendertag in der Zeitzone des Unternehmens zählt als Tag `0`.

`Send in 1 Calendar days at 11:05 am company time` oder `send in 1 Calendar days at 11:05 am local time` würde den Tag `1` zum aktuellen Kalendertag in der Zeitzone des Unternehmens bzw. der lokalen Zeitzone hinzufügen und die Nachricht dann für den nächsten Tag um 11:05 Uhr Unternehmenszeit planen.

Gilt für die Unternehmens- oder Ortszeit die Pazifische Zeitzone und wird der Canvas-Schritt am 13.4\. um 20:00 Uhr PT gestartet, setzt Braze diesen Canvas-Schritt für den 14.4\. um 11:05 Uhr PT an.

## Vorheriges X in Y Filter-Verhalten

Braze enthält eine spezielle Kategorie von Segmentierungsfiltern mit der Bezeichnung "Filter X in Y". Diese Filter haben alle eine ähnliche Funktionalität, die durch die folgenden Merkmale definiert wird:

- Legen Sie Kalendertage fest (die um Mitternacht enden).
- "Tage" sind in UTC definiert.
- Der aktuelle UTC-Tag ist als "1" definiert.



[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
