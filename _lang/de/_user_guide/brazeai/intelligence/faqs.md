---
nav_title: FAQ
article_title: Intelligenz FAQ
page_order: 191
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Intelligenter Kanal, Intelligente Auswahl und Intelligentes Timing."
---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf häufig gestellte Fragen zur Intelligence Suite.

## Intelligente Auswahl

### Warum ist die Wiederzulassung in weniger als 24 Stunden in Kombination mit Intelligent Selection nicht möglich?

Wir lassen nicht zu, dass Kampagnen mit intelligenter Auswahl in einem zu kurzen Zeitfenster wieder wählbar sind, da dies die Integrität der Kontrollvariante beeinträchtigen würde. Indem wir eine Lücke von 24 Stunden schaffen, stellen wir sicher, dass der Algorithmus mit einem statistisch gültigen Datensatz arbeiten kann.

Normalerweise führen Kampagnen mit Wiederwahlmöglichkeit dazu, dass Nutzer:innen dieselbe Variante erneut eingeben müssen, die sie zuvor erhalten haben. Bei der Intelligenten Auswahl kann Braze nicht garantieren, dass ein Benutzer dieselbe Kampagnenvariante erhält, da sich die Variantenverteilung aufgrund des Aspekts der optimalen Zuweisung für diese Funktion verschoben hätte. Wäre es zulässig, dass die Nutzerin oder der Nutzer erneut eintritt, bevor die intelligente Auswahl die Performance der Variante überprüft, könnten die Daten aufgrund der Nutzer:innen, die erneut eintreten, verzerrt sein.

Zum Beispiel, wenn eine Kampagne diese Varianten verwendet:

- Variante A: 20%
- Variante B: 20%
- Kontrolle: 60%

Dann könnte die Variantenverteilung für die zweite Runde wie folgt aussehen:

- Variante A: 15%
- Variante B: 25%
- Kontrolle: 60%

### Warum zeigen meine Intelligent Selection-Varianten in der Anfangsphase meiner Kampagne gleiche Sendungen an?

Die intelligente Auswahl weist Varianten für den Versand auf der Grundlage des aktuellen Status der Konversion der Kampagne zu. Es bestimmt die endgültigen Variantenzuweisungen erst nach einer Trainingsperiode, in der die Sendungen gleichmäßig auf die Varianten verteilt werden. Wenn Sie nicht möchten, dass die Intelligente Auswahl in den frühen Phasen Ihrer Kampagne gleichmäßig sendet, verwenden Sie feste Varianten für einen traditionellen A/B-Test.

### Wird die Intelligente Auswahl aufhören zu optimieren, ohne einen klaren Gewinner zu ermitteln?

Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95%iger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % der aktuellen Rate verbessern wird.

### Warum kann ich die intelligente Auswahl in meinem Canvas oder meiner Kampagne nicht aktivieren (ausgegraut)?

Die intelligente Auswahl ist nicht verfügbar, wenn:

- Sie haben keine Konversionsereignisse zu Ihrer Kampagne oder Ihrem Canvas hinzugefügt
- Sie erstellen eine Kampagne, die nur einmal versendet wird
- Sie haben die Wiederholbarkeit mit einem Zeitfenster von weniger als 24 Stunden aktiviert
- Ihr Canvas besteht aus einer einzigen Variante, der keine weiteren Varianten oder Kontrollgruppen hinzugefügt wurden.
- Ihr Canvas besteht aus einer einzigen Kontrollgruppe, der keine Varianten hinzugefügt wurden

---

## Intelligentes Timing

### Allgemein

#### Was sagt Intelligentes Timing voraus?

Intelligentes Timing konzentriert sich auf die Prognose, wann ein Nutzer Ihre Nachrichten am ehesten öffnet oder klickt, um sicherzustellen, dass Ihre Nachrichten die Nutzer:innen zum optimalen Zeitpunkt erreichen.

#### Wird das intelligente Timing für jeden Wochentag separat berechnet?

Nein, Intelligentes Timing ist nicht an bestimmte Tage gebunden. Stattdessen personalisiert es die Sendezeiten auf der Grundlage des eindeutigen Engagements jedes Nutzers und des von Ihnen verwendeten Kanals, wie E-Mail oder Push-Benachrichtigungen. So können Sie sicherstellen, dass Ihre Nachrichten die Nutzer:innen dann erreichen, wenn sie am empfänglichsten sind.

### Berechnungen

#### Welche Daten werden verwendet, um die optimale Zeit für jeden Nutzer:innen zu berechnen?

Um die optimale Zeit zu berechnen, verwenden Sie Intelligentes Timing:

1. Analysiert die Interaktionsdaten für jeden Nutzer:innen, die vom Braze SDK aufgezeichnet wurden. Dies beinhaltet:
  - Zeiten der Sitzung
  - Push direkt öffnet
  - Push beeinflusst Öffnungen
  - E-Mail Klicks
  - Öffnungen von E-Mails (ohne Öffnungen durch den Computer)
2. Gruppiert diese Ereignisse nach Zeit und identifiziert die optimale Sendezeit für jeden Nutzer:innen.

#### Werden die Öffnungen der Maschinen bei der Berechnung der optimalen Zeit berücksichtigt?

Nein, [Öffnungen der Maschine]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens) sind von den Berechnungen für die optimale Zeit ausgeschlossen. Das bedeutet, dass die Sendezeiten ausschließlich auf dem echten Engagement der Nutzer:innen beruhen, was eine genauere Zeitplanung für Ihre Kampagnen ermöglicht.

#### Wie genau ist der optimale Zeitpunkt?

Intelligentes Timing plant Nachrichten während der "engagiertesten Stunde" jedes Nutzers, basierend auf dem Beginn der Sitzung und der Öffnung von Nachrichten. Innerhalb dieser Stunde wird der Zeitpunkt der Nachrichten auf die nächsten fünf Minuten gerundet. Wenn beispielsweise die optimale Zeit eines Nutzers:innen mit 16:58 Uhr berechnet wird, wird die Nachricht für 17:00 Uhr geplant. Es kann zu leichten Verzögerungen bei der Zustellung kommen, da das System in Stoßzeiten aktiv ist.

#### Wie sehen die Fallback-Berechnungen aus, wenn nicht genügend Daten vorhanden sind?

Wenn es weniger als fünf relevante Ereignisse für einen Nutzer:innen gibt, verwendet Intelligentes Timing die [Ausweichzeit][1] in Ihren Nachrichteneinstellungen. 

### Management von Kampagnen

#### Wie weit im Voraus sollte ich eine Intelligent Timing Kampagne starten, um sie erfolgreich an alle Nutzer:innen in allen Zeitzonen zu bringen?

Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit, eine der ersten Zeitzonen der Welt. An einem einzigen Tag erstreckt er sich über etwa 48 Stunden. Zum Beispiel hat jemand, dessen optimale Zeit 12:01 Uhr ist und der in Australien lebt, seine optimale Zeit bereits überschritten, und es ist "zu spät", um ihm zu senden. Aus diesen Gründen müssen Sie einen Zeitplan von 48 Stunden vorbringen, um Ihre App erfolgreich an alle Nutzer weltweit zuzustellen.

#### Warum werden in meiner Intelligent Timing-Kampagne nur wenige oder gar keine Sendungen angezeigt?

Braze benötigt eine ausreichende Anzahl von Datenpunkten, um eine gute Schätzung vornehmen zu können. Wenn die Sitzungsdaten nicht ausreichen oder die anvisierten Benutzer nur wenige oder gar keine E-Mail-Klicks oder -Öffnungen aufweisen (z. B. neue Benutzer), kann Intelligent Timing die beliebteste Stunde des Arbeitsbereichs an diesem Wochentag als Standard festlegen. Wenn es nicht genügend Informationen über den Workspace gibt, greifen wir auf die Standardzeit von 17 Uhr zurück. Sie können auch eine bestimmte [Ausweichzeit]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) festlegen.

#### Warum wird meine Intelligent Timing-Kampagne nach dem geplanten Datum gesendet?

Ihre Kampagne mit intelligentem Timing versendet möglicherweise über das geplante Datum hinaus, weil Sie A/B-Tests nutzen. Kampagnen, die A/B-Tests verwenden, können die Gewinner-Variante automatisch versenden, nachdem der A/B-Test beendet ist, wodurch sich die Dauer des Kampagnenversands verlängert. Standardmäßig werden Intelligent Timing-Kampagnen so geplant, dass die Gewinner-Variante am nächsten Tag an die verbleibenden Nutzer versendet wird, aber Sie können dieses Versanddatum ändern.

Wir empfehlen Ihnen, bei intelligenten Timing-Kampagnen mehr Zeit für den Abschluss des A/B-Tests einzuplanen und die Gewinnervariante für zwei Tage statt für einen Tag zu versenden. 

### Technische Überlegungen

#### Wann prüft Braze die Zulassungskriterien für Segmente und Zielgruppenfilter?

Braze führt zwei Prüfungen durch, wenn eine Kampagne gestartet wird:

1. **Erste Überprüfung:** Um Mitternacht in der ersten Zeitzone am Tag des Versands.
2. **Prüfung des Zeitplans:** Kurz vor dem Senden zu der für den Nutzer:innen ausgewählten Zeit Intelligent Timing.

Seien Sie vorsichtig, wenn Sie auf der Grundlage anderer Kampagnensendungen filtern, um das Targeting von nicht geeigneten Segmenten zu vermeiden. Wenn Sie z.B. zwei Kampagnen am selben Tag zu unterschiedlichen Zeiten versenden und einen Filter hinzufügen, der es Nutzern:innen nur erlaubt, die zweite Kampagne zu erhalten, wenn sie die erste erhalten haben, werden die Nutzer:innen die zweite Kampagne nicht erhalten. Das liegt daran, dass niemand berechtigt war, als die Kampagne ins Leben gerufen und die Segmente gebildet wurden.

#### Kann ich Ruhezeiten in meiner Intelligent Timing-Kampagne verwenden?

Ruhezeiten können in einer Kampagne verwendet werden, die Intelligentes Timing einsetzt. Der Algorithmus des intelligenten Timings vermeidet Ruhezeiten, so dass die Nachricht trotzdem an alle in Frage kommenden Nutzer:innen gesendet wird. Wir empfehlen jedoch, die Ruhezeiten zu deaktivieren, es sei denn, es gibt Richtlinien, Compliance- oder andere rechtliche Gründe dafür, wann Nachrichten gesendet werden können und wann nicht.

#### Was passiert, wenn die optimale Zeit für einen Nutzer:innen innerhalb der Ruhezeiten liegt? 

Wenn die ermittelte optimale Zeit in die Ruhezeiten fällt, findet Braze den nächstgelegenen Rand der Ruhezeiten und plant die Nachricht für die nächste zulässige Stunde vor oder nach den Ruhezeiten. Die Nachricht wird in die Warteschlange gestellt, um an der nächstgelegenen Grenze der Ruhezeiten in Bezug auf die optimale Zeit gesendet zu werden.

#### Kann ich Intelligent Timing und Ratenbegrenzung verwenden?

Rate-Limiting kann bei einer Kampagne verwendet werden, die Intelligent Timing einsetzt. Rate-Limiting bedeutet jedoch, dass einige Nutzer:innen ihre Nachrichten zu einem suboptimalen Zeitpunkt erhalten, insbesondere wenn eine große Anzahl von Nutzer:innen im Verhältnis zur Rate-Limiting-Größe aufgrund unzureichender Daten auf den Zeitplan für den Fallback-Zeitpunkt gesetzt wird. 

Wir empfehlen die Verwendung von Rate-Limits bei einer Intelligent Timing Kampagne nur dann, wenn es technische Anforderungen gibt, die mit Rate-Limits erfüllt werden müssen.

#### Kann ich Intelligent Timing während der IP-Erwärmung verwenden?

Braze rät davon ab, Intelligent Timing zu verwenden, wenn Nutzer:innen zum ersten Mal IP-Warming betreiben, da einige seiner Verhaltensweisen zu Schwierigkeiten beim Erreichen des täglichen Volumens führen können. Das liegt daran, dass Intelligent Timing die Kampagnensegmente doppelt auswertet. Einmal bei der Erstellung der Kampagne und ein zweites Mal vor dem Versand an die Nutzer, um zu überprüfen, ob sie noch in diesem Segment sein sollten.

Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzer:innen-Obergrenze herankommen können.

#### Wie wird die Zeit der beliebtesten App ermittelt?

Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für den Workspace (in Ortszeit) bestimmt. Diese Metrik finden Sie im Dashboard bei der Vorschau der Zeiten für eine Kampagne, die in Rot angezeigt wird.

#### Berücksichtigt Intelligentes Timing die Öffnungen maschinelle Öffnungen?

Ja, maschinelle Öffnungen werden von Intelligent Timing herausgefiltert, so dass sie die Ausgabe nicht beeinflussen.

#### Wie kann ich sicherstellen, dass Intelligent Timing so gut wie möglich funktioniert?

Intelligentes Timing verwendet den individuellen Verlauf des Engagements jedes Nutzers:innen bei Nachrichten, unabhängig davon, zu welchen Zeiten sie diese erhalten haben. Bevor Sie intelligentes Timing verwenden, vergewissern Sie sich, dass Sie den Nutzer:innen Nachrichten zu verschiedenen Tageszeiten geschickt haben. Auf diese Weise können Sie "ausprobieren", wann der beste Zeitpunkt für die einzelnen Nutzer:innen ist. Eine unzureichende Auswahl verschiedener Tageszeiten kann dazu führen, dass Intelligent Timing eine suboptimale Sendezeit für eine:n Nutzer:in auswählt.


[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing#fallback-time
