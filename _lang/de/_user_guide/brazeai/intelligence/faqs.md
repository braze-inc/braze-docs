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

## Intelligentes Timing

### Sagt Intelligent Timing voraus, wann ein Benutzer am ehesten konvertiert, oder nur, wann er am ehesten öffnet oder klickt?

Intelligentes Timing sagt voraus, wann ein Benutzer am ehesten öffnet oder klickt.

### Wie wird die Zeit der beliebtesten App ermittelt?

Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für den Workspace (in Ortszeit) bestimmt. Diese Metrik finden Sie im Dashboard bei der Vorschau der Zeiten für eine Kampagne, die in Rot angezeigt wird.

### Berücksichtigt Intelligentes Timing die Öffnungen maschinelle Öffnungen?

Ja, maschinelle Öffnungen werden von Intelligent Timing herausgefiltert, so dass sie die Ausgabe nicht beeinflussen.

### Wie kann ich sicherstellen, dass Intelligent Timing so gut wie möglich funktioniert?

Intelligentes Timing nutzt den individuellen Verlauf des Engagements jeder Nutzerin und jedes Nutzers bei Nachrichten, unabhängig davon, zu welchem Zeitpunkt sie diese erhalten haben. Bevor Sie intelligentes Timing verwenden, vergewissern Sie sich, dass Sie den Nutzer:innen Nachrichten zu verschiedenen Tageszeiten geschickt haben. Auf diese Weise können Sie "ausprobieren", wann der beste Zeitpunkt für die einzelnen Nutzer:innen ist. Eine unzureichende Auswahl verschiedener Tageszeiten kann dazu führen, dass Intelligent Timing eine suboptimale Sendezeit für eine:n Nutzer:in auswählt. 

### Wie weit im Voraus sollte ich eine Intelligent Timing Kampagne starten, um sie erfolgreich an alle Nutzer:innen in allen Zeitzonen zu bringen?

Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit, eine der ersten Zeitzonen der Welt. An einem einzigen Tag erstreckt er sich über etwa 48 Stunden. Zum Beispiel hat jemand, dessen optimale Zeit 12:01 Uhr ist und der in Australien lebt, seine optimale Zeit bereits überschritten, und es ist "zu spät", um ihm zu senden. Aus diesen Gründen müssen Sie 48 Stunden im Voraus einplanen, um sicherzustellen, dass jeder auf der Welt, der Ihre App nutzt, sie erfolgreich zugestellt bekommt.

### Warum werden in meiner Intelligent Timing-Kampagne nur wenige oder gar keine Sendungen angezeigt?

Braze benötigt eine ausreichende Anzahl von Datenpunkten, um eine gute Schätzung vornehmen zu können. Wenn die Sitzungsdaten nicht ausreichen oder die anvisierten Benutzer nur wenige oder gar keine E-Mail-Klicks oder -Öffnungen aufweisen (z. B. neue Benutzer), kann Intelligent Timing die beliebteste Stunde des Arbeitsbereichs an diesem Wochentag als Standard festlegen. Wenn es nicht genügend Informationen über den Workspace gibt, greifen wir auf die Standardzeit von 17 Uhr zurück. Sie können auch eine bestimmte [Ausweichzeit]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) festlegen.

### Warum wird meine Intelligent Timing-Kampagne nach dem geplanten Datum gesendet?

Ihre Kampagne mit intelligentem Timing versendet möglicherweise über das geplante Datum hinaus, weil Sie A/B-Tests nutzen. Kampagnen, die A/B-Tests verwenden, können die Gewinner-Variante automatisch versenden, nachdem der A/B-Test beendet ist, wodurch sich die Dauer des Kampagnenversands verlängert. Standardmäßig werden Intelligent Timing-Kampagnen so geplant, dass die Gewinner-Variante am nächsten Tag an die verbleibenden Nutzer versendet wird, aber Sie können dieses Versanddatum ändern.

Wir empfehlen Ihnen, bei intelligenten Timing-Kampagnen mehr Zeit für den Abschluss des A/B-Tests einzuplanen und die Gewinnervariante für zwei Tage statt für einen Tag zu versenden. 

### Wann prüft Braze die Zulassungskriterien für Segmente und Zielgruppenfilter?

Braze führt zwei Prüfungen durch, wenn eine Kampagne gestartet wird:

1. Sobald die erste Zeitzone identifiziert ist, beginnt der Prozess der Nutzerwarteschlangenbildung, und
2. Zum geplanten Zeitpunkt, um zu sehen, ob die Nutzer:innen noch berechtigt sind, die Kampagne zu erhalten.

Seien Sie vorsichtig, wenn Sie Kampagnen erstellen, die die Aussendungen anderer Kampagnen filtern. Wenn Sie z.B. zwei Kampagnen am selben Tag zu unterschiedlichen Zeiten versenden und einen Filter hinzufügen, der es Nutzern nur erlaubt, die zweite Kampagne zu erhalten, wenn sie die erste erhalten haben, werden die Nutzer die zweite Kampagne nicht erhalten. Das liegt daran, dass niemand berechtigt war, als die Kampagne ins Leben gerufen und die Segmente gebildet wurden.

### Kann ich Ruhezeiten in meiner Intelligent Timing-Kampagne verwenden?

Wir raten davon ab, intelligentes Timing und Ruhezeiten gleichzeitig für Ihre Kampagne oder Ihren Canvas zu verwenden, da dies kontraproduktiv ist. Quiet Hours basieren auf Top-Down-Annahmen über das Nutzerverhalten, während Intelligent Timing auf der Aktivität der Nutzer basiert.

### Kann ich Intelligent Timing und Ratenbegrenzung verwenden?

Braze empfiehlt die Verwendung von Intelligent Timing und Ratenbegrenzung nicht, da es keine Garantie dafür gibt, wann die Nachricht zugestellt wird.

### Kann ich Intelligent Timing während der IP-Erwärmung verwenden?

Braze rät davon ab, Intelligent Timing zu verwenden, wenn Nutzer:innen zum ersten Mal IP-Warming betreiben, da einige seiner Verhaltensweisen zu Schwierigkeiten beim Erreichen des täglichen Volumens führen können. Das liegt daran, dass Intelligent Timing die Kampagnensegmente doppelt auswertet. Einmal bei der Erstellung der Kampagne und ein zweites Mal vor dem Versand an die Nutzer, um zu überprüfen, ob sie noch in diesem Segment sein sollten. 

Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzerobergrenze herankommen können.
