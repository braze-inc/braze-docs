---
nav_title: Ereignis-Analytik
article_title: Prognose-Analytics für Ereignisse
description: "Dieser Artikel befasst sich mit den verschiedenen Komponenten der Seite Predictive Events Analytics und ihrer Verwendung für fundierte Entscheidungen."
page_order: 1.3

---

# Prognostische Ereignis-Analytik

> Nachdem Ihre Vorhersage erstellt und trainiert wurde, haben Sie Zugriff auf die Seite **Vorhersageanalyse**. Diese Seite hilft Ihnen bei der Entscheidung, welche Benutzer Sie auf der Grundlage ihres Wahrscheinlichkeitswertes oder ihrer Kategorie ansprechen sollten.

## Über prognostische Event-Analytik

Sobald das Training der Vorhersage abgeschlossen und diese Seite gefüllt ist, können Sie mit der Verwendung von [Filtern]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) in Segmenten oder Kampagnen beginnen, um die Ergebnisse des Modells zu nutzen. Wenn Sie Hilfe bei der Entscheidung brauchen, wen Sie ansprechen und warum, kann Ihnen diese Seite auf der Grundlage der historischen Genauigkeit des Modells und Ihrer eigenen Geschäftsziele helfen.

Dies sind die Komponenten, aus denen die prognostische Ereignisanalyse besteht:

- [Wahrscheinlichkeitswert](#purchase_score)
- [Prognosequalität](#prediction_quality)
- [Geschätzte Genauigkeit](#estimated_results)
- [Ereigniskorrelationstabelle](#correlation_table)

Die Verteilung der Likelihood-Scores für die gesamte Prognosegruppe wird oben auf der Seite angezeigt. Benutzer in den Bereichen weiter rechts haben eine höhere Punktzahl und werden das Ereignis mit größerer Wahrscheinlichkeit durchführen. Benutzer in den weiter links liegenden Bereichen führen das Ereignis mit geringerer Wahrscheinlichkeit durch. Mit dem Schieberegler unterhalb des Diagramms können Sie einen Bereich von Nutzern auswählen und die Ergebnisse der Ansprache dieser Nutzer abschätzen.

Wenn Sie die Griffe des Schiebereglers in verschiedene Positionen bewegen, informiert Sie der Balken in der linken Hälfte des Fensters darüber, wie viele Nutzer aus der gesamten Vorhersagezielgruppe mit dem von Ihnen ausgewählten Teil der Bevölkerung angesprochen werden würden.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Wahrscheinlichkeitswert {#purchase_score}

Den Nutzern in der Vorhersagegruppe wird ein Wahrscheinlichkeitswert zwischen 0 und 100 zugewiesen. Je höher die Punktzahl ist, desto größer ist auch die Wahrscheinlichkeit, dass das Ereignis stattfindet. 

Im Folgenden sehen Sie, wie ein Benutzer je nach Wahrscheinlichkeitswert eingestuft wird:

- **Niedrig:** zwischen 0 und 50
- **Mittel:** zwischen 50 und 75
- **Hoch:** zwischen 75 und 100

Die Punktzahlen und die entsprechenden Kategorien werden entsprechend dem Zeitplan aktualisiert, den Sie auf der Seite **Erstellung der Vorhersage** ausgewählt haben. Die Anzahl der Benutzer mit Wahrscheinlichkeitswerten in jedem der 20 gleichgroßen Bereiche oder in jeder der Wahrscheinlichkeitskategorien wird in der Tabelle oben auf der Seite angezeigt.

## Geschätzte Genauigkeit {#estimated_results}

In der rechten Hälfte der Leiste unterhalb des Diagramms wird die voraussichtliche Ansprachegenauigkeit des ausgewählten Teils der Prognosezielgruppe auf zwei Weisen angezeigt: wie viele ausgewählte Nutzer das Ereignis voraussichtlich ausführen und wie viele nicht.

![Die ausgewählte Zielgruppe und die geschätzte Genauigkeit werden auf dem Braze-Dashboard angezeigt.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Erwartete Performance

Anhand der geschätzten Genauigkeit können Sie überprüfen, wie viele ausgewählte Nutzer:innen das Ereignis voraussichtlich durchführen werden.

Die Vorhersage ist nicht perfekt genau, und das ist keine Vorhersage jemals. Das bedeutet, dass Braze nicht in der Lage sein wird, jeden einzelnen zukünftigen Benutzer zu identifizieren, der das Ereignis ausführt. Die Wahrscheinlichkeitswerte sind wie eine Reihe von fundierten und zuverlässigen Vorhersagen. Der Fortschrittsbalken zeigt an, wie viele der in der Prognosezielgruppe erwarteten wahr Positiven mit der ausgewählten Zielgruppe erreicht werden. Dabei wird davon ausgegangen, dass diese Benutzeranzahl das Ereignis auch dann ausführt, wenn Sie keine Nachricht versenden.

### Keine Performance zu erwarten

Anhand der geschätzten Genauigkeit können Sie überprüfen, wie viele ausgewählte Nutzer:innen das Ereignis voraussichtlich nicht durchführen werden.

Alle Modelle für maschinelles Lernen machen Fehler. Es kann Benutzer in Ihrer Auswahl geben, die zwar eine hohe Wahrscheinlichkeitsbewertung haben, aber das Ereignis nicht tatsächlich durchführen. Sie würden das Ereignis auch dann nicht durchführen, wenn Sie gar nichts unternehmen. Sie werden ohnehin ins Visier genommen, also ist dies ein Fehler oder "falsches Positiv". Die gesamte Breite dieses zweiten Fortschrittsbalkens steht für die erwartete Anzahl von Nutzern, die das Ereignis nicht durchführen werden, und der gefüllte Teil für diejenigen, die anhand der aktuellen Schiebereglerposition falsch angesprochen werden.

Anhand dieser Informationen sollten Sie entscheiden, wie viele der wahr Positiven Sie erfassen möchten, wie viele falsch Positive hinnehmbar sind und wie hoch die Fehlerkosten für Ihr Unternehmen sind. Wenn Sie eine hochwertige Aktion starten, sollten Sie nur Nichtkäufer (also falsch Positive) ansprechen und dazu die linke Seite des Diagramms bevorzugen. Oder Sie möchten Käufer, die häufig kaufen (echte Positive), dazu ermutigen, dies wieder zu tun, indem Sie eine Gruppe von Nutzern auswählen, die die rechte Seite des Diagramms bevorzugt.

## Prognosequalität {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Ereigniskorrelationstabelle{#correlation_table}

Diese Analyse zeigt Benutzerattribute oder Verhaltensweisen an, die mit Ereignissen in der Zielgruppe der Vorhersage korreliert sind. Die bewerteten Attribute sind Alter, Land, Geschlecht und Sprache. Zu den analysierten Verhaltensweisen gehören Sitzungen, Käufe, Gesamtausgaben, benutzerdefinierte Ereignisse sowie Kampagnen und Canvas-Schritte, die in den letzten 30 Tagen empfangen worden sind.

Die Tabellen sind unterteilt in links und rechts (höhere/geringere Ereigniswahrscheinlichkeit. Für jede Zeile wird in der rechten Spalte das Verhältnis angezeigt, in dem die Benutzer mit dem Verhalten oder Attribut in der linken Spalte eher oder weniger wahrscheinlich das Ereignis ausführen. Diese Zahl ist das Verhältnis der Wahrscheinlichkeitswerte von Nutzern mit diesem Verhalten oder Attribut geteilt durch die Wahrscheinlichkeit, das Ereignis bei der gesamten Vorhersagegruppe durchzuführen.

Diese Tabelle wird nur aktualisiert, wenn die Vorhersage neu trainiert wird und nicht, wenn die Likelihood-Werte des Benutzers aktualisiert werden.

{% alert note %}
Die Korrelationsdaten für Vorhersagen werden teilweise ausgeblendet. Um diese Informationen zu erhalten, ist ein Kauf erforderlich. Kontaktieren Sie Ihren Kundenbetreuer für weitere Informationen.
{% endalert %}
