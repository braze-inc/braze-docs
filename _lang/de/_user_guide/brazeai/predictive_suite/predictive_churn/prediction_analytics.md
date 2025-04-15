---
nav_title: Vorhersage-Analytik
article_title: Vorhersage-Analytik
description: "Dieser Referenzartikel behandelt die verschiedenen Komponenten der Seite Churn Prediction Analytics und zeigt, wie Sie diese nutzen können, um aufschlussreiche, zielgerichtete Entscheidungen zu treffen."
page_order: 2

---

# Vorhersage-Analytik

> Nachdem Ihre Vorhersage erstellt und trainiert wurde, haben Sie Zugriff auf die Seite **Vorhersageanalyse**. Diese Seite hilft Ihnen bei der Entscheidung, welche Benutzer Sie auf der Grundlage ihres _Churn Risk Score_ oder ihrer Kategorie ansprechen sollten. 

Sobald das Training der Vorhersage abgeschlossen und diese Seite gefüllt ist, können Sie einfach [Filter]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) in Segmenten oder Kampagnen verwenden, um die Ergebnisse des Modells zu nutzen. Wenn Sie jedoch Hilfe bei der Entscheidung benötigen, wen Sie ansprechen und warum, kann Ihnen diese Seite auf der Grundlage der historischen Genauigkeit des Modells und Ihrer eigenen Geschäftsziele helfen. 

**Analysekomponenten**<br>
- [Abwanderung – Risiko und Kategorie](#churn_score)<br>
- [Prognosequalität](#prediction_quality)<br>
- [Geschätzte Ergebnisse](#estimated_results)<br>
- [Churn-Korrelationstabelle](#correlation_table)

## Übersicht

Die Verteilung der Punktzahlen für die gesamte Prognosegruppe wird oben auf der Seite in einem Diagramm angezeigt, das Sie nach Kategorie oder Punktzahl anzeigen können. Die Nutzer in den weiter rechts gelegenen Bereichen haben höhere Werte und werden eher abwandern. Je weiter links, desto geringer die Abwanderungswahrscheinlichkeit. Mit dem Schieberegler unterhalb des Diagramms können Sie einen Bereich von Nutzern auswählen und abschätzen, wie die Ergebnisse aussehen würden, wenn Sie Nutzer im ausgewählten Bereich des _Churn Risk Score_ oder der Kategorie ansprechen würden.

![][4]{: style="max-width:90%"}

Wenn Sie den Schieberegler verschieben, informiert Sie der Balken in der linken Hälfte des unteren Bereichs darüber, wie viele Nutzer aus der gesamten Vorhersagezielgruppe angesprochen werden sollen.

## Churn Score und Kategorie {#churn_score}

Der Prognosegruppe wird eine _Abwanderungswahrscheinlichkeit_ zwischen 0 und 100 zugewiesen. Je höher die Punktzahl, desto größer ist die Wahrscheinlichkeit der Abwanderung. 
- Benutzer mit einer Punktzahl zwischen 0 und 50 werden in die Kategorie _Geringes Risiko_ eingestuft. 
- Benutzer mit einer Punktzahl zwischen 50 und 75 bzw. 75 und 100 werden in die Kategorien _Mittleres Risiko_ bzw. _Hohes Risiko_ eingestuft. 

Die Bewertungen und die entsprechenden Kategorien werden nach dem Zeitplan aktualisiert, den Sie auf der Seite zur Modellerstellung gewählt haben. Die Anzahl der Nutzer mit Churn Scores in jedem der 20 gleich großen Buckets wird im Diagramm oben auf der Seite angezeigt. So können Sie abschätzen, wie das Abwanderungsrisiko in der Gesamtpopulation aussieht.

## Benutzer gezielt ansprechen, um die Abwanderung zu verringern

### Prognosequalität {#prediction_quality}

Um die Genauigkeit Ihres Modells zu messen, zeigt Ihnen die Metrik für _die Vorhersagequalität_, wie effektiv dieses bestimmte Modell für maschinelles Lernen zu sein scheint, wenn es mit historischen Daten getestet wird. Unter [Prognosequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) erfahren Sie mehr über diese Metrik.

Hier finden Sie unsere Empfehlungen für verschiedene Bereiche der _Vorhersagequalität_:

| Vorhersagequalität Bereich (%) | Empfehlung |
| ---------------------- | -------------- |
| 60 - 100 | Ausgezeichnet. Größtmögliche Genauigkeit. Es ist unwahrscheinlich, dass eine Änderung der Zielgruppendefinitionen einen zusätzlichen Nutzen bringt. |
| 40 - 60 | Gut. Dieses Modell generiert genaue Prognosen, aber mit anderen Zielgruppeneinstellungen können eventuell noch bessere Ergebnisse erzielt werden. |
| 20 - 40| Ausreichend. Die Genauigkeit und der Nutzen dieses Modells sind recht hoch. Dennoch empfiehlt es sich, andere Zielgruppendefinitionen auszuprobieren, um zu sehen, ob sich die Performance verbessert. |
| 0 - 20 | Schlecht. Ändern Sie die Zielgruppendefinitionen und versuchen Sie es erneut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die Vorhersage wird alle zwei Wochen erneut trainiert und zusammen mit der Metrik für die Vorhersagequalität aktualisiert, damit Ihre Vorhersagen immer auf dem neuesten Stand des Nutzerverhaltens sind. Das letzte Mal, als diese Umschulung stattfand, wird auf der Vorhersagelistenseite sowie auf der Analyseseite Ihrer Vorhersage angezeigt.

## Geschätzte Ergebnisse {#estimated_results}

![][6]{: style="float:right;max-width:30%;margin-left:15px;"}

In der rechten Hälfte der Tabelle unterhalb des Diagramms zeigen wir Schätzungen der erwarteten Genauigkeit bei der Ansprache dieses Teils der Zielgruppe. Auf der Grundlage von Daten über Nutzer in der Vorhersagezielgruppe in der Vergangenheit und der offensichtlichen Genauigkeit des Modells bei der Unterscheidung zwischen abwandernden und nicht abwandernden Nutzern auf der Grundlage dieser Daten aus der Vergangenheit schätzen diese Fortschrittsbalken eine zukünftige potenzielle Nachricht unter Verwendung der mit dem Schieberegler hervorgehobenen Zielgruppe:

1. Eine Schätzung, wie viele Abwanderer tatsächlich korrekt angesprochen werden <br><br> Natürlich kennen wir die Zukunft nicht genau, so dass wir nicht genau wissen, welche Nutzer aus der Vorhersagezielgruppe in Zukunft abwandern werden. Aber die Vorhersage ist eine zuverlässige Schlussfolgerung. Basierend auf der bisherigen Performance zeigt der Balken an, wie viele der (anhand der bisherigen Abwanderungsrate) zu erwartenden Abwanderungsfälle in der Prognosegruppe mit der aktuellen Targeting-Auswahl angesprochen werden. Wir würden erwarten, dass diese Anzahl von Nutzern abwandert, wenn Sie sie nicht mit zusätzlichen oder ungewöhnlichen Nachrichten ansprechen. <br><br>

2. Eine Schätzung, wie viele Nutzer, die eigentlich nicht abgewandert wären, fälschlicherweise angesprochen werden<br><br>Alle Modelle für maschinelles Lernen machen Fehler. Möglicherweise gibt es in Ihrer Auswahl Personen mit hohem _Abwanderungsrisiko_, die dann aber doch nicht abwandern. Diese würden auch dann nicht abwandern, wenn Sie überhaupt nichts unternehmen. Sie werden ohnehin ins Visier genommen, also ist dies ein Fehler oder "falsches Positiv". Die gesamte Breite dieses zweiten Fortschrittsbalkens steht für die erwartete Anzahl von Nutzern, die nicht abwandern werden, und der gefüllte Teil für diejenigen, die mit der aktuellen Schiebereglerposition falsch angesprochen werden.

So können Sie entscheiden, wie viele Abwanderungsfälle Sie erfassen möchten und wie hoch die Kosten falsch positiver Ergebnisse für Ihr Unternehmen sind. Wenn Sie eine hochwertige Werbeaktion starten, sollten Sie möglichst wenige Nicht-Abwanderungsgefährdete ansprechen und so viele tatsächliche Abwanderungsgefährdete einbeziehen, wie laut Modell zulässig sind. Oder wenn Sie weniger empfindlich auf Falschmeldungen reagieren und die Benutzer zusätzliche Nachrichten erhalten, können Sie mehr Nachrichten an die Zielgruppe senden, um mehr erwartete Abwanderer zu erfassen und die wahrscheinlichen Fehler zu ignorieren.

## Churn-Korrelationstabelle {#correlation_table}

Diese Analyse enthält Nutzerattribute und Verhaltensweisen, die in der Prognosegruppe in der Vergangenheit mit der Abwanderung korreliert haben. Die Tabellen sind in links und rechts für mehr bzw. weniger abwanderungsgefährdet unterteilt. Für jede Zeile wird in der rechten Spalte das Verhältnis angezeigt, in dem die Nutzer mit dem Verhalten oder Attribut in der linken Spalte eher oder weniger wahrscheinlich abwandern. Diese Zahl gibt die Abwanderungswahrscheinlichkeit bei Vorhandensein dieses Verhaltens oder Attributs gemessen an der Abwanderungswahrscheinlichkeit der gesamte Prognosegruppe an.

Diese Tabelle wird nur aktualisiert, wenn die Vorhersage neu trainiert wird und nicht, wenn die _Churn Risk Scores_ der Benutzer aktualisiert werden.

{% alert note %}
Die Korrelationsdaten für Vorhersagen werden teilweise ausgeblendet. Um diese Informationen zu erhalten, ist ein Kauf erforderlich. Kontaktieren Sie Ihren Kundenbetreuer für weitere Informationen.
{% endalert %}

[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}
[4]: {% image_buster /assets/img/churn/churnTargeting.gif %}