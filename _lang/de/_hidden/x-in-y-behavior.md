---
nav_title: X in Y Filter-Verhalten
permalink: /x-in-y-behavior/
---

# Aktuelles X in Y Filter-Verhalten

Das Verhalten dieser Filter bleibt weitgehend gleich und wird durch die folgenden Merkmale definiert:

- Legen Sie Kalendertage fest (die um Mitternacht enden).
- "Tage" sind in UTC definiert.
- Der aktuelle UTC-Tag ist als "0" definiert.

## Anwendungsfall

Die folgende Kampagne wird am 16\. April um 21 Uhr gesendet. Die Segmentierung der Zielgruppe lautet "Mehr als 2 Käufe in den letzten 3 Tagen".

![Zeitplan der Kampagne][1]

9 pm ET am 16\. April ist 1 Uhr UTC am 17\. April.

Der 17\. April wäre der Tag "0", der 16\. April wäre der Tag "1", der 15\. April wäre der Tag "2" und der 14\. April wäre der Tag "3".

Der Verlauf von 12 Uhr UTC am 14\. April bis zum aktuellen Zeitpunkt (1 Uhr UTC am 17\. April).
Dies würde zu einem Fenster führen, das 73 Stunden der Historie des Benutzers umfasst.

## An Kalendertagen

Kalendertage werden in mehr Funktionen als nur in den "X in Y"-Filtern verwendet:

- Nachrichtenplanung
- Frequenzkappung
- "X in Y"-Filter

`Calendar Days` beziehen sich auf den Zeitraum innerhalb eines nummerierten Tages, der um 12:00 Uhr beginnt und um 23:59 Uhr desselben Tages endet (12:00 Uhr am 8. Juni bis 23:59 Uhr am 8. Juni wäre ein einzelner Kalendertag).

### Frequenzkappung

Kalendertage werden verwendet, wenn Sie unter `Frequency Capping`"Tage" oder "Wochen" auswählen.

- `Every 1 day` begrenzt die Begrenzung auf den aktuellen Kalendertag in der Ortszeit Ihres Benutzers (bis Mitternacht Ortszeit).
- `Every 2 days` begrenzt die Kappung auf den vorherigen und den aktuellen Kalendertag in der Ortszeit Ihres Benutzers (und endet um Mitternacht Ortszeit am aktuellen Kalendertag).

### Unternehmen & Ortszeit

Der aktuelle Kalendertag in der Zeitzone des Unternehmens zählt als Tag `0`.

`Send in 1 Calendar days at 11:05 am company time` oder `send in 1 Calendar days at 11:05 am local time` würde den Tag `1` zum aktuellen Kalendertag in der Zeitzone des Unternehmens bzw. der lokalen Zeitzone hinzufügen und die Nachricht dann für den nächsten Tag um 11:05 Uhr Unternehmenszeit planen.

Wenn die Unternehmens- oder Ortszeit Pazifische Zeit ist und der Benutzer den Canvas-Schritt um 8:00PM PT am 13.4\. eingibt, plant Braze diesen Canvas-Schritt für 11:05 Uhr PT am 14.4\. ein.

## Vorheriges X in Y Filter-Verhalten

Braze verfügt über eine spezielle Kategorie von Segmentierungsfiltern mit der Bezeichnung "X in Y-Filter". Diese Filter haben alle eine ähnliche Funktionalität, die durch die folgenden Merkmale definiert ist:

- Legen Sie Kalendertage fest (die um Mitternacht enden).
- "Tage" sind in UTC definiert.
- Der aktuelle UTC-Tag ist als "1" definiert.



[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
