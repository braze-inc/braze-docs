---
nav_title: Content Optimizer
article_title: Content Optimizer
alias: "/content_optimizer/"
description: "Content Optimizer ist ein Agent, der Ihnen hilft, den Inhalt von Nachrichten in großem Umfang zu testen und zu optimieren, indem er KI einsetzt, um automatisch große Mengen von Inhaltsvarianten zu generieren und zu bewerten."
page_type: reference
page_order: 4
---

# Content Optimizer

> Content Optimizer ist ein Agent, der Ihnen hilft, den Inhalt von Nachrichten in großem Umfang zu testen und zu optimieren, indem er KI einsetzt, um automatisch große Mengen von Inhaltsvarianten zu generieren und zu bewerten.

{% alert important %}
Content Optimizer befindet sich derzeit im Beta-Stadium und ist nur für Nachrichten per E-Mail verfügbar. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Über Content Optimizer

Content Optimizer ist ein Agent, der in einem Canvas-Schritt ausgeführt wird. Es hilft Ihnen, zu testende Nachrichtenkomponenten zu definieren, Varianten mit Hilfe von generativer KI oder manueller Eingabe zu generieren und automatisch zu optimieren, welche Inhaltskombinationen an Nutzer:innen gesendet werden. Dieses Feature hilft Ihnen dabei:

- Optimieren Sie Betreffzeilen, Überschriften, Inhalte oder primäre CTAs für E-Mails.
- Verbessern Sie kontinuierlich die Performance von Nachrichten, ohne manuelle A/B-Tests durchführen zu müssen.
- Testen Sie schnell eine große Anzahl von Varianten und nutzen Sie KI für die Ideenfindung.
- Schalten Sie automatisch leistungsschwache Inhalte aus und vergrößern Sie die Gewinner.

Lernen Sie, wie Sie einen [Content Optimizer Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/) erstellen.

## Anwendungsfälle

### E-Mail

| Anwendungsfall Optimierung | Ziel | Beschreibung |
| --- | --- | --- |
| Variationen der Betreffzeile | Öffnungsrate erhöhen | Testen Sie Tonfall, Dringlichkeit, Personalisierung und die Verwendung von Emojis. |
| Kopfzeilen Messaging Stile | Engagement fördern | Vergleichen Sie emotionales, wertorientiertes und klares Messaging in der Kopfzeile. | 
| Format des Inhalts | Verbessern Sie Lesbarkeit und Engagement | Testen Sie Storytelling versus Feature-Listen, Aufzählungszeichen versus Absätze und die Länge des Inhalts. |
| CTA-Kopie & Ton | Click-throughs erhöhen | Vergleichen Sie handlungsorientierte, nutzenorientierte und in der ersten Person formulierte CTAs. |
| Thematische Inhaltskombinationen | Entdecken Sie leistungsstarke Kombinationen | Kombinieren Sie die Komponenten Betreff, Text und CTA, um die beste Gesamtkombination zu finden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Funktionsweise

Content Optimizer verwendet einen nicht-kontextuellen [, mehrarmigen Bandit-Algorithmus](https://en.wikipedia.org/wiki/Multi-armed_bandit), um leistungsstarken Varianten mehr Sends zuzuweisen und die Zuweisung für leistungsschwache Varianten zu reduzieren. Im Laufe der Zeit führt dies zu einer kontinuierlichen Verbesserung des Inhalts Ihrer Nachrichten bei minimalem manuellem Aufwand.

Wenn der Schritt zum ersten Mal gestartet wird, sendet Content Optimizer nach dem Zufallsprinzip Varianten, um erste Performance-Daten zu sammeln. Nach dieser anfänglichen Erkundungsphase beginnt der Algorithmus, den Datenverkehr auf leistungsstärkere Inhaltskombinationen zu verlagern und die Zuteilung an leistungsschwächere Optionen schrittweise zu reduzieren. Während der Erkundungsphase wird der Verkehr im Allgemeinen auf die verfügbaren Varianten verteilt, damit der Algorithmus aus deren relativer Performance lernen kann.

Content Optimizer ähnelt dem Messaging-Schritt in Canvas, mit Features wie Ruhezeiten, [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) und Ereignisprotokollierung. Sie können einen Schritt zur Inhaltsoptimierung konfigurieren, indem Sie eine Basisnachricht erstellen und festlegen, welche Inhaltskomponenten (wie Betreffzeile, Textkörper oder Call-to-Action) optimiert werden sollen. Varianten für jede Komponente können mit KI generiert oder manuell eingegeben werden, und Liquid-Tags müssen der Basisnachricht hinzugefügt werden, um die Komponenten dem Inhalt der Nachricht zuzuordnen.

Jeder Nutzer:innen erhält eine Nachricht pro Eingang in den Content Optimizer Schritt. Wiederholte Eingänge werden wie neue Eingänge behandelt, ohne Erinnerung an frühere Varianten.

Die besten Ergebnisse erzielen Sie, wenn Sie den Content Optimizer in Canvase verwenden, in denen die Nutzer:innen den Schritt nach und nach eingeben, z. B. in wiederkehrenden oder ständig aktiven Canvase mit gleichbleibendem Tagesvolumen. Wenn alle Nutzer:innen den Schritt auf einmal eingeben, hat der Agent keine Zeit, aus den ersten Ergebnissen zu lernen. Der Schritt wird sich eher wie ein statischer A/B-Test verhalten als eine Live-Optimierungsmaschine.

Das bedeutet, dass Sie Content Optimizer auch in einmalig gesendeten oder kurzfristigen Canvase verwenden können, allerdings nur, wenn die Nutzer:innen den Schritt über einen längeren Zeitraum betreten (z.B. durch einen Verzögerungsschritt, einen geplanten Eingang oder einen API-getriggerten Ablauf). Stellen Sie sicher, dass der Schritt genügend Traffic und Zeit hat, um Performance-Unterschiede zu beobachten, bevor die meisten Nutzer:innen erreicht werden.


### Wichtige Konzepte

| Term                    | Beschreibung |
|-------------------------|-------------|
| Basisnachricht   | Die Hauptvorlage für Nachrichten, aus der Varianten erstellt werden, einschließlich aller Sendeeinstellungen. |
| Inhaltliche Komponenten  | Elemente innerhalb einer Nachricht (z.B. Betreffzeile oder primärer CTA), die getestet und optimiert werden können. Marketer müssen den entsprechenden Liquid-Tag in die Nachricht einfügen, in der die Komponente erscheinen soll. |
| Content-Varianten    | Die verschiedenen Werte, die eine Inhaltskomponente annehmen kann. |
| Inhaltliche Kombinationen| Eindeutige Nachrichten, die durch das Mischen und Anpassen von Inhaltsvarianten erstellt werden. |
| Event-Optimierung       | Legt fest, wie Content Optimizer die Performance auswertet und den Traffic im Laufe der Zeit den Inhaltskombinationen zuordnet, z. B. Klicks oder Öffnungen für E-Mails. Gilt für alle Inhaltskomponenten in einem Schritt. Content Optimizer lernt kontinuierlich aus diesem Ereignis und verlagert die Zustellung automatisch in Richtung leistungsfähigerer Inhaltskombinationen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

- Content Optimizer befindet sich derzeit im Beta-Stadium und ist nur für Nachrichten per E-Mail verfügbar.
- Der Agent kann bis zu 125 Kombinationen pro Schritt erzeugen:
   - Bis zu 3 Komponenten pro Schritt
   - Bis zu 5 Varianten für jede Komponente
- Pro Nutzer:innen wird nur eine Nachricht pro Eingang gesendet. Es gibt keine Erinnerung an frühere Sendungen für erneute Eingänge.
- Marketer müssen Liquid-Tags für jede Komponente manuell in den Nachrichten-Editor einfügen, wo die definierten Varianten der Inhaltskomponente dargestellt werden sollen.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Nächste Schritte

- Kontaktieren Sie Ihren Customer-Success-Manager:in, um an der Beta-Phase teilzunehmen oder Unterstützung beim Onboarding zu erhalten.
- Lernen Sie, wie Sie einen [Content Optimizer Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/) erstellen.
