---
nav_title: FAQ
article_title: FAQs zu multivariaten und A/B-Tests
page_order: 21
page_type: reference
toc_headers: h2
description: "Dieser Artikel behandelt FAQs für multivariate und A/B-Tests mit Braze."
---

# FAQs zu multivariaten und A/B-Tests

## Grundlagen des Testens

### Was ist der Unterschied zwischen A/B-Tests und multivariaten Tests?

#### A/B-Tests

Bei A/B-Tests experimentiert der Marketer mit einer einzelnen Variable innerhalb der Kampagne (z. B. E-Mail-Betreffzeilen oder Versandzeitpunkt von Nachrichten). Dabei wird eine Teilmenge der Zielgruppe nach dem Zufallsprinzip in zwei oder mehr Gruppen aufgeteilt, jeder Gruppe wird eine andere Variante präsentiert, und es wird beobachtet, welche Variante die höchste Konversionsrate aufweist. In der Regel wird die beste Performance-Variante anschließend an die restliche Zielgruppe gesendet.

#### Mehrvariantentests 

Multivariate Tests sind eine Erweiterung von A/B-Tests, die es dem Marketer erlauben, mehrere Variablen gleichzeitig zu testen, um die effektivste Kombination zu ermitteln. Sie könnten zum Beispiel die Betreffzeile Ihrer Nachricht, das Bild, das Ihren Text begleitet, und die Farbe des CTA-Buttons testen. Diese Art von Tests erlaubt es Ihnen, mehr Variablen und Variationskombinationen innerhalb eines einzigen Experiments zu untersuchen und schneller und umfassendere Insights zu erhalten als A/B-Tests. Das Testen mehrerer Variablen und Kombinationen innerhalb eines einzigen Experiments erfordert jedoch eine größere Zielgruppe, um statistische Signifikanz zu erzielen.

### Wie werden die Ergebnisse von A/B-Tests berechnet?

Braze testet alle Varianten gegeneinander mit Pearson's Chi-Quadrat-Tests, die messen, ob eine Variante statistisch gesehen alle anderen bei einem Signifikanzniveau von p < 0,05 übertrifft, oder was wir als 95%ige Signifikanz bezeichnen. Für alle Varianten, die diese Signifikanzschwelle überschreiten, wird die Variante mit der besten Performance als "Gewinner" ermittelt.

Dies ist ein anderer Test als der Konfidenzwert, der nur die Leistung einer Variante im Vergleich zur Kontrolle mit einem numerischen Wert zwischen 0 und 100% beschreibt. Konkret bedeutet dies, dass wir darauf vertrauen, dass der standardisierte Unterschied in der Konversionsrate zwischen der Variante und der Kontrolle signifikant größer als der Zufall ist.

### Warum ist die Verteilung der Varianten nicht gleichmäßig?

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Tests durchführen und abschließen

### Wann ist der erste Test beendet?

Wenn Sie die Gewinnvariante für Einzelversandkampagnen verwenden, ist der Test beendet, wenn der Sendezeitpunkt der Gewinnvariante erreicht ist. Braze stuft eine Variante als Gewinner ein, wenn sie mit statistisch signifikantem Abstand die höchste Konversionsrate aufweist.

Bei wiederkehrenden, aktionsbasierten und API-getriggerten Kampagnen können Sie die intelligente Auswahl nutzen, um die Performance-Daten jeder Variante kontinuierlich zu tracken und den Kampagnen-Traffic kontinuierlich in Richtung der leistungsstärksten Varianten zu optimieren. Bei der intelligenten Auswahl wird nicht explizit eine Versuchsgruppe definiert, in der Nutzer:innen zufällige Varianten erhalten, sondern der Braze-Algorithmus verfeinert kontinuierlich seine Schätzung der leistungsstärksten Variante, was eine schnellere Auswahl der leistungsstärksten Variante zulässig macht.

### Wie behandelt Braze Nutzer:innen, die eine Variante einer Nachricht in einer wiederkehrenden Kampagne oder einem Canvas-Eingang erhalten haben? 

Nutzer:innen werden nach dem Zufallsprinzip einer bestimmten Variante zugewiesen, bevor sie die Kampagne zum ersten Mal erhalten. Jedes Mal, wenn die Kampagne empfangen wird (oder der Nutzer:in eine Canvas-Variante einsteigt), erhält er dieselbe Variante, es sei denn, die prozentualen Anteile der Variante werden geändert. Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt. Nutzer:innen bleiben in diesen Varianten, bis die Prozentsätze wieder geändert werden. Nutzer:in werden nur für die Varianten weitergegeben, die bearbeitet wurden.

Nehmen wir zum Beispiel an, wir haben eine Kampagne oder ein Canvas mit drei Varianten. Wenn nur Variante A und Variante B geändert oder aktualisiert werden, werden die Nutzer:innen der Variante C nicht umverteilt, da der prozentuale Anteil der Variante C nicht geändert wurde. Kontrollgruppen bleiben konsistent, wenn der Prozentsatz der Varianten unverändert bleibt. Nutzer:innen, die bereits Nachrichten erhalten haben, können bei einem späteren Versand nicht mehr in die Kontrollgruppe eintreten. Auch kann kein Nutzer:innen in der Kontrollgruppe jemals eine Nachricht erhalten.

#### Was ist mit Experiment-Pfaden?

Das gilt auch, weil die Canvas-Pfade, die auf ein Experiment folgen, ebenfalls Varianten sind.

#### Kann ich die Nutzer:innen in Kampagnen und Canvase umverteilen?

Die einzige Möglichkeit, Nutzer:innen in Canvase umzuverteilen, ist die Verwendung von [Randomized Paths in Experiment-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution). Dadurch werden die Pfadzuweisungen immer zufällig verteilt, wenn Nutzer:innen den Canvas erneut betreten. Dies ist jedoch kein Standardexperiment und könnte die Ergebnisse des Experiments verfälschen, da die Kontrollgruppe mit Nutzer:innen der Behandlung kontaminiert werden kann.

## Vertrauen und Voreingenommenheit

### Nimmt das Vertrauen mit der Zeit zu?

Das Vertrauen nimmt mit der Zeit zu, wenn alles andere konstant bleibt. Konstant halten bedeutet, dass es keine anderen Marketing-Faktoren gibt, die die Varianten beeinflussen könnten, wie z.B. Variante A, die über einen Rabatt von 25% spricht, der in der Mitte des Tests endet.

Konfidenz ist ein Maß dafür, wie sicher Braze ist, dass sich die Variante von der Kontrolle unterscheidet. Je mehr Nachrichten versendet werden, desto größer ist die statistische Aussagekraft des Tests, was die Wahrscheinlichkeit erhöht, dass die gemessenen Unterschiede in der Performance nicht auf Zufall beruhen. Im Allgemeinen erhöht ein größerer Stichprobenumfang unser Vertrauen in die Identifizierung kleinerer Unterschiede in der Performance zwischen Varianten und Kontrolle.

### Kann die Zuweisung von Kontroll- und Testgruppen zu Verzerrungen beim Testen führen?

Es gibt keine praktische Möglichkeit, dass die Attribute oder Verhaltensweisen eines Nutzers vor der Erstellung einer bestimmten Kampagne oder eines Canvas systematisch zwischen Varianten und Kontrolle variieren. 

Um Nutzer:innen den Messaging-Varianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zuzuordnen, verknüpfen wir zunächst ihre zufällig generierte Nutzer:innen-ID mit der zufällig generierten Kampagne oder Canvas-ID. Als nächstes wenden wir einen sha256 Hash-Algorithmus an, teilen das Ergebnis durch 100 und behalten den Rest (auch bekannt als Modulus mit 100). Schließlich ordnen wir die Nutzer:innen in Slices ein, die den prozentualen Zuweisungen für die im Dashboard gewählten Varianten (und die optionale Kontrolle) entsprechen.

### Warum kann ich Rate-Limiting nicht mit einer Kontrollgruppe verwenden?

Braze unterstützt derzeit kein Rate-Limiting mit A/B-Tests, die eine Kontrollgruppe haben. Dies liegt daran, dass Rate-Limiting für die Kontrollgruppe nicht in der gleichen Weise gilt wie für die Varianten, wodurch eine Verzerrung entsteht. Verwenden Sie stattdessen die [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), die den Prozentsatz der Nutzer:innen, die jede Variante erhalten, auf der Grundlage von Analytics und der Performance der Kampagne automatisch anpasst.
