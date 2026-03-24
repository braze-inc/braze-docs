---
nav_title: Content Optimizer
article_title: Content Optimizer
alias: "/content_optimizer/"
description: "Der Content Optimizer ist ein Tool, das Ihnen dabei unterstützt, Nachrichteninhalte in großem Umfang zu testen und zu optimieren. Dabei wird KI eingesetzt, um automatisch große Mengen an Varianten zu generieren und zu bewerten."
page_type: reference
page_order: 3
---

# Content Optimizer

> Der Content Optimizer ist ein Tool, das Ihnen dabei unterstützt, Nachrichteninhalte in großem Umfang zu testen und zu optimieren. Dabei wird KI eingesetzt, um automatisch große Mengen an Varianten zu generieren und zu bewerten.

{% alert important %}
Der Content Optimizer befindet sich derzeit in der Beta-Phase und ist ausschließlich für E-Mail-Nachrichten verfügbar. Für Unterstützung beim Einstieg wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endalert %}

## Über den Content Optimizer

Der Content Optimizer ist ein Agent, der in einem Canvas-Schritt ausgeführt wird. Es unterstützt Sie dabei, zu testende Nachrichtenkomponenten zu definieren, Varianten mithilfe generativer KI oder manueller Eingaben zu generieren und automatisch zu optimieren, welche Inhaltskombinationen an die Nutzer:innen gesendet werden. Dieses Feature unterstützt Sie dabei:

- Optimieren Sie Betreffzeilen, Kopfzeilen, Textinhalte oder primäre CTA für E-Mails.
- Verbessern Sie kontinuierlich die Performance der Nachrichten, ohne manuelle A/B-Tests durchführen zu müssen.
- Testen Sie große Mengen an Inhaltsvarianten zügig und nutzen Sie dabei KI zur Ideenfindung.
- Leistungsschwache Inhalte sollten automatisch ausgemustert und erfolgreiche Inhalte ausgebaut werden.

Erfahren Sie, wie Sie einen [Schritt für den Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/) erstellen.

## Anwendungsfälle

### E-Mail

| Anwendungsfall Optimierung | Ziel | Beschreibung |
| --- | --- | --- |
| Variationen der Betreffzeile | Erhöhen Sie die Öffnungsrate | Testton, Dringlichkeit, Personalisierung und Verwendung von Emojis. |
| Stile für Kopfzeilen-Nachrichten | Steigern Sie das Engagement | Vergleichen Sie emotionale, werteorientierte und klare Nachrichten in der Kopfzeile des Textes. | 
| Format des Textinhalts | Verbessern Sie die Lesbarkeit und das Engagement | Bitte vergleichen Sie Storytelling mit Feature-Listen, Aufzählungspunkte mit Absätzen und die Länge der Inhalte. |
| CTA-Text& | Steigern Sie die Click-throughs | Vergleichen Sie handlungsorientierte, vorteilsorientierte und in der ersten Person formulierte CTA-Formulierungen. |
| Thematische Inhaltskombinationen | Entdecken Sie Kombinationen mit hoher Performance | Kombinieren Sie Themen, Text und CTA-Komponenten, um die beste Gesamtkombination zu finden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Funktionsweise

Der Content Optimizer verwendet einen nicht-kontextuellen [Multi-Armed-Bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit)-Algorithmus, um leistungsstarken Varianten mehr Sendungen zuzuweisen und die Zuweisung an leistungsschwache Varianten zu reduzieren. Im Laufe der Zeit führt dies zu einer kontinuierlichen Verbesserung Ihrer Nachrichteninhalte bei minimalem manuellem Aufwand.

Der proprietäre Bandit-Optimierungsalgorithmus von Braze wurde speziell für die kombinatorische Natur des Content Optimizer-Schritts entwickelt. Da jede Nachricht aus mehreren Komponenten besteht, lernt der Algorithmus gleichzeitig über die Performance jeder einzelnen Komponente (wie Betreffzeile, Textkörper, CTA) sowie über deren Wechselwirkungen, wenn sie zu einer Nachricht kombiniert werden. Konkret bedeutet dies, dass bei der Übermittlung einer bestimmten Kombination alle Kombinationen, die dieselben Komponenten aufweisen, von den Daten dieser Übermittlung profitieren. Dadurch kann der Bandit im Vergleich zu einem Standard-Bandit-Algorithmus mit derselben Datenmenge wesentlich schneller lernen.

Bei der ersten Ausführung des Schritts sendet der Content Optimizer zufällig Varianten, um erste Daten zur Performance zu erfassen. Nach dieser anfänglichen Erkundungsphase beginnt der Algorithmus, den Datenverkehr auf Inhalte mit höherer Performance umzuleiten und die Zuweisung an Optionen mit geringer Performance schrittweise zu reduzieren. Während der Erkundungsphase wird der Datenverkehr in der Regel auf die verfügbaren Varianten verteilt, damit der Algorithmus aus deren relativer Performance lernen kann.

Der Content Optimizer ähnelt dem Schritt „Nachricht“ in Canvas und verfügt über Features wie Ruhezeiten, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) und Ereignisprotokollierung. Sie können einen Content Optimizer-Schritt konfigurieren, indem Sie eine Basenachricht erstellen und festlegen, welche Inhaltskomponenten (wie Betreffzeile, Textkörper oder Call-to-Action) optimiert werden sollen. Varianten für jede Komponente können mit KI generiert oder manuell eingegeben werden. Liquid-Tags müssen zur Basenachricht hinzugefügt werden, um Komponenten in den Meldungsinhalt abzubilden.

Jeder Nutzer:in erhält eine Nachricht pro Eintrag im Schritt „Content Optimizer“. Wiederholungen werden als neu behandelt, ohne dass frühere Varianten berücksichtigt werden.

Um optimale Ergebnisse zu erzielen, verwenden Sie den Content Optimizer in Canvases, in denen Nutzer:innen den Schritt schrittweise über einen längeren Zeitraum hinweg ausführen, beispielsweise in wiederkehrenden oder ständig aktiven Canvases mit einem konstanten täglichen Volumen. Sollten alle Nutzer:innen gleichzeitig den Schritt ausführen, hat der Agent keine Zeit, aus den ersten Ergebnissen zu lernen. Dieser Schritt wird eher wie ein statischer A/B-Test als wie eine Live-Optimierungs-Engine funktionieren.

Dies bedeutet, dass Sie den Content Optimizer weiterhin in einmalig versendeten oder kurzfristigen Canvases verwenden können, jedoch nur, wenn die Nutzer:innen den Schritt über einen längeren Zeitraum hinweg ausführen (z. B. durch einen Verzögerungsschritt, einen Zeitplan für den Eintritt oder einen API-ausgelösten Ablauf). Stellen Sie sicher, dass der Schritt ausreichend Traffic und Zeit bietet, um Performance-Unterschiede zu beobachten, bevor die meisten Nutzer:innen erreicht werden.

### Wichtige Konzepte

| Term                    | Beschreibung |
|-------------------------|-------------|
| Basisnachricht   | Das Haupt-Template für Nachrichten, auf dem die Varianten basieren, einschließlich aller Sendeeinstellungen. |
| Inhaltskomponenten  | Elemente innerhalb einer Nachricht (z. B. Betreffzeile oder primäre CTA), die getestet und optimiert werden können. Marketer müssen den entsprechenden Liquid-Tag an der Stelle in die Nachricht einfügen, an der die Komponente erscheinen soll. |
| Content-Varianten    | Die verschiedenen Werte, die eine Inhaltskomponente annehmen kann. |
| Inhaltskombinationen| Eindeutige Nachrichten, die durch die Kombination verschiedener Inhaltsvarianten erstellt werden. |
| Event-Optimierung       | Legt fest, wie der Content Optimizer die Performance bewertet und den Traffic im Laufe der Zeit auf Content-Kombinationen verteilt, beispielsweise Klicks oder Öffnungen für E-Mails. Gilt für alle Inhaltskomponenten in einem Schritt. Der Content Optimizer lernt kontinuierlich aus diesem Ereignis und verschiebt die Zustellung automatisch hin zu leistungsstärkeren Inhaltskombinationen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

- Der Content Optimizer befindet sich derzeit in der Beta-Phase und ist ausschließlich für E-Mail-Nachrichten verfügbar.
- Der Agent kann bis zu 125 Kombinationen pro Schritt generieren:
   - Bis zu 3 Komponenten pro Schritt
   - Bis zu 5 Varianten für jede Komponente
- Pro Nutzer:in und Eintrag wird nur eine Nachricht versendet. Es gibt keine Speicherung früherer Sendungen für erneute Eingaben.
- Marketer müssen Liquid-Tags manuell für jede Komponente im Nachrichten-Editor einfügen, wo die definierten Inhaltskomponentenvarianten gerendert werden sollen.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Nächste Schritte

- Bitte wenden Sie sich an Ihren Customer-Success-Manager, um an der Beta-Phase teilzunehmen oder Unterstützung beim Onboarding zu erhalten.
- Erfahren Sie, wie Sie einen [Schritt für den Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/) erstellen.
