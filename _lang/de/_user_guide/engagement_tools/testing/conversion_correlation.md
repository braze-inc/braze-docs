---
nav_title: Konversionskorrelation
article_title: Konversionskorrelation
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Dieser Referenzartikel erklärt die Conversion-Korrelationsanalyse auf der Seite Campaign Analytics."
tool: 
  - Reports
  
---

# Konversionskorrelation

> Die Analyse der Konversionskorrelation auf der Seite **Kampagnenanalyse** gibt Ihnen Aufschluss darüber, welche Benutzerattribute und Verhaltensweisen die von Ihnen für Kampagnen festgelegten Ergebnisse fördern oder beeinträchtigen. 

## Übersicht

Für jede Kampagne prüft Braze eine Liste von Attributen und Benutzerverhalten und berechnet, ob Benutzer statistisch signifikant mit einem Anstieg oder einem Rückgang der von Ihnen für die Kampagne ausgewählten [Konversionsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) verbunden sind. Wir berechnen auch, wie viel wahrscheinlicher oder unwahrscheinlicher es ist, dass Nutzer mit dem gegebenen Attribut oder Verhalten konvertieren, und wenn dies signifikant ist, zeigen wir dies auf der entsprechenden Seite der Tabelle an. Nutzer mit jedem Attribut oder Verhalten von Interesse werden mit den Raten für die gesamte Zielgruppe der Kampagne verglichen. Verhaltensweisen und Attribute, die keine signifikante Korrelation mit der Konversion aufweisen, sind in der Tabelle nicht aufgeführt.

Um eine Konversions-Korrelationsanalyse durchzuführen, wählen Sie das Konversions-Event von Interesse aus dem Dropdown-Menü aus.

Das Panel "Konversions-Korrelation" zeigt ein Beispiel, bei dem "Wählen Sie ein Konversions-Event" auf "Primäres Konversions-Event - A" eingestellt ist und die Ereigniseinstellung "Kauf innerhalb von 12 Stunden getätigt (Jedes Produkt)" lautet.]({% image_buster /assets/img/convcorr.png %})

## Was wird kontrolliert?

Wir überprüfen die folgenden Attribute, indem wir sie als kategorische Variablen behandeln. Mit anderen Worten, ein:e Nutzer:in hat entweder jeden möglichen Wert dieser Attribute oder nicht, und wir testen, ob sie die Konversionsrate beeinflussen.

-  Land
-  Sprache
-  Geschlecht

Wir prüfen auch, ob die folgenden Faktoren die Konversionsrate beeinflussen:

- Ausführen beliebiger benutzerdefinierter Ereignisse
- In den letzten 30 Tagen eingegangene Kampagnen und Werbemittel (außer der Kampagne, die gerade bewertet wird)

Schließlich überprüfen wir mehrere Verhaltensvariablen, die mehrere Werte annehmen können. Wir unterteilen die folgenden Angaben in vier Bereiche oder Quartile und messen dann, inwieweit die Zugehörigkeit zu einem Quartil mit einem Anstieg oder Rückgang der Konversion verbunden ist:

- Alter
- Insgesamt ausgegebene Dollar
- Anzahl der Sitzungen

## Wann kann ich diese Analyse überprüfen?

Diese Analyse ist frühestens 24 Stunden nach dem Versand einer Kampagne verfügbar und berücksichtigt nur Versendungen, die in den letzten 30 Tagen stattgefunden haben. Wenn keine Verhaltensweisen oder Attribute in signifikanter Weise mit einem der Conversion-Ereignisse der Kampagne korrelieren, wird das Dropdown-Menü deaktiviert und Sie erhalten eine entsprechende Meldung.

## So prüft Braze auf Signifikanz

Wir prüfen die statistische Signifikanz mit Hilfe des [Wilson-Konfidenzintervalls](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Wir ermitteln mit 95%iger Sicherheit die Rate, mit der die gesamte Zielgruppe der Kampagne konvertiert hat. Dies wird als Basissatz bezeichnet. 

Dann berechnen wir für jede der Variablen auch die Rate, mit der Nutzer:innen mit dem betreffenden Attribut oder Verhalten mit 95%iger Sicherheit konvertiert sind. Indem wir dies durch den Basissatz teilen, können wir das Verhältnis messen. Wenn der Wert viel größer als 1 ist, ist die Wahrscheinlichkeit höher, dass Nutzer mit diesem Attribut oder Verhalten konvertieren. Wenn es viel weniger ist, sind sie unwahrscheinlicher. Wir zeigen den Wert des Verhältnisses selbst in der Tabelle an. Der Wert wird nur angezeigt, wenn er weit genug von 1 entfernt ist, um mit einem Konfidenzniveau von 95 % signifikant zu sein.

