---
nav_title: Agenten
article_title: Braze-Agenten
page_order: 0.5
description: "Braze Agents können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, so dass Sie personalisiertere Kundenerlebnisse zustellen können."
---

# Braze-Agenten

> Braze-Agenten sind KI-gestützte Helfer, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, so dass Sie personalisiertere Kundenerlebnisse zustellen können.

{% alert important %}
Braze-Agenten befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Warum Braze-Agenten verwenden?

Braze Agents helfen Ihrem Team, intelligentere, personalisierte Erlebnisse zuzustellen - ohne zusätzliche Arbeit. Sie agieren als intelligente Assistenten, die nicht nur auf Aufforderungen reagieren, sondern den Kontext verstehen, Entscheidungen treffen und auf ein Ziel hinarbeiten.

In der Praxis können Agenten automatisch Nachrichten - wie Betreffzeilen oder produktinterne Texte - erstellen, so dass jeder Kunde eine auf ihn zugeschnittene Kommunikation erhält. Sie können sich auch in Echtzeit anpassen und Menschen auf der Grundlage von Vorlieben, Verhaltensweisen oder anderen Daten durch verschiedene Canvas-Pfade leiten.

Über Messaging hinaus können Agenten Ihre Kataloge anreichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten frisch und dynamisch halten. Indem sie sich wiederholende oder komplexe Aufgaben übernehmen, geben sie Ihrem Team den nötigen Freiraum, um sich auf Strategie und Kreativität zu konzentrieren, statt auf die manuelle Einrichtung. Braze-Agenten agieren eher als Mitarbeiter denn als Hintergrundprozesse - sie helfen Ihnen, Probleme zu lösen und in großem Umfang Wirkung zu erzielen.

### Wann Sie Braze-Agenten im Vergleich zu anderen BrazeAI Features verwenden sollten

Verwenden Sie Agenten für die Personalisierung von Inhalten anhand des spezifischen Kontexts eines Nutzers:innen. Wenn ein Agent z.B. weiß, dass ein Nutzer:innen am liebsten Schokolade isst und Gummibärchen als Topping bevorzugt, kann er für diesen Nutzer:innen beim Durchlaufen des Canvas Push-Kopien erstellen, die genau diese Kombination enthalten.

Der Agent lernt jedoch nicht durch Versuch und Irrtum, und er hat keine Idee von einem ultimativen Marketing-Ziel, das er messen und maximieren will. Selbst wenn Sie ihm sagen, dass es generell Texte schreiben soll, die zu Konversionen führen, hat es keinen Mechanismus, um die Auswirkungen seiner agenturischen Schreibarbeit auf die Konversion zu überwachen und diese Daten wieder in zukünftige agenturische Aufrufe zu integrieren. Sie können sich das als "Vibe"-Entscheidungen vorstellen, nicht als KI-Entscheidungen, die auf Belohnungen basieren.

Im Gegensatz dazu sind andere BrazeAI-Tools darauf ausgelegt, die von ihnen gemessenen Metriken zu maximieren. Agenten sind zum Beispiel sehr gut darin, qualitativ einzuschätzen, wie die Eigenschaften eines Nutzers:innen die Wahrscheinlichkeit oder Neigung beeinflussen, ein bestimmtes Ereignis durchzuführen oder ein bestimmtes Produkt zu mögen. Da der Agent jedoch nicht durch Versuch und Irrtum lernt, hat er keine Idee, wie er seine Genauigkeit bei der Vorhersage von Wahrscheinlichkeiten messen und das Signal im Laufe der Zeit verbessern kann. Die Predictive Suite übertrifft also den Agentenschritt, wenn man die Genauigkeit der Prognosen und die Verbesserungen im Laufe der Zeit beurteilt.

## Features

Features für Braze-Agenten umfassen:

- **Flexible Einrichtung:** Verwenden Sie eine von Braze bereitgestellte LLM oder verbinden Sie Ihren eigenen Modellanbieter (wie OpenAI, Anthropic, Google Gemini oder AWS Bedrock).
- **Nahtlose Integration:** Setzen Sie Agenten direkt in Canvas-Schritten oder Katalogfeldern ein.
- **Tools zum Testen und Protokollieren:** Machen Sie eine Vorschau auf die Ausgabe Ihres Agenten, indem Sie ihn vor dem Start mit Beispieleingaben testen. Zeigen Sie die Protokolle für jede Ausführung des Agenten an, einschließlich der Eingaben und Ausgaben für diese Ausführung.
- **Kontrolle der Verwendung:** Tägliche Limits helfen bei der Verwaltung von Performance und Kosten.

## Über Braze Agents

Agenten werden mit Anweisungen (Systemprompts) konfiguriert, die festlegen, wie sie sich verhalten. Wenn ein Agent ausgeführt wird, verwendet er Ihre Anweisungen zusammen mit den von Ihnen übermittelten Daten, um eine Antwort zu erzeugen. 

### Wichtige Konzepte

| Term | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | Das "Gehirn" des Agenten, in diesem Fall ein großes Sprachmodell (LLM). Es interpretiert Eingaben, erzeugt Antworten und führt Schlussfolgerungen aus. Ein stärkeres Modell (trainiert auf mehr relevanten Daten) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemaufforderung). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Wirkstoff zuverlässiger und berechenbarer. |
| Kontext | Daten, die zur Laufzeit an den Agenten übergeben werden, unabhängig davon, wo er eingesetzt wird, z.B. Felder des Nutzerprofils oder Katalogzeilen. Diese Eingabe liefert die Informationen, die der Agent zur Erzeugung von Ausgaben verwendet. |
| [Variable ausgeben]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Arbeitsabläufe zu steuern. Ausgabevariablen können ein String, eine Zahl oder ein boolescher Datentyp sein.  |
| [Ausführung](#limitations) | Eine einzige Ausführung des Agenten. Dies wird auf Ihr Tageslimit angerechnet. |
| [Ausgabeformat]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) | Die vordefinierte Datenstruktur der Antwort des Agenten. |
| [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) | Der Grad der Abweichung für den Output des Agenten. Dies bestimmt, wie präzise oder kreativ Ihr Agent sein kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

Während der Beta-Phase gelten die folgenden Einschränkungen:

- Jeder Agent verfügt standardmäßig über ein tägliches Ausführungslimit von 50.000 Läufen, das auf ein Maximum von 100.000 Läufen pro Tag erhöht werden kann.
- Standardmäßig muss jeder Lauf innerhalb von 15 Sekunden abgeschlossen sein. Nach 15 Sekunden sendet der Agent eine Antwort `null` zurück, in der er verwendet wird. 
    - Wenn Ihre Agenten ständig Zeitüberschreitungen haben, wenden Sie sich an Ihren Braze-Konto Manager:in, um dieses Limit zu erhöhen.
- Die Eingabedaten sind auf 25 KB pro Anfrage begrenzt. Längere Eingaben werden abgeschnitten.

## Nächste Schritte

Jetzt, da Sie die Braze-Agenten kennen, sind Sie bereit für die nächsten Schritte:

- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

## Modell-Provider als Unterauftragsverarbeiter oder Drittanbieter

Wenn der Kunde eine Integration mit den von Braze über die Serviceleistungen; Dienste bereitgestellten Modellen ("von Braze bereitgestellte LLM") verwendet, handeln die Anbieter dieser von Braze bereitgestellten LLMs als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen dem Kunden und Braze. 

Wenn der Kunde seinen eigenen API-Schlüssel zur Integration in die Braze AI-Funktionalität mitbringt, wird der Anbieter des eigenen LLM-Abos des Kunden als Drittanbieter betrachtet, wie im Vertrag zwischen dem Kunden und Braze definiert. 

### Wie werden meine Daten verwendet und an die von Braze zur Verfügung gestellten LLMs gesendet?

Um die KI-Ausgabe durch die Braze AI-Features zu erzeugen, die Braze als die von Braze bereitgestellten LLMs nutzend identifiziert ("Ausgabe"), sendet Braze Ihre Systemaufforderung oder ggf. andere Eingaben ("Eingabe") an die von Braze bereitgestellten LLMs. Daten, die an das entsprechende von Braze bereitgestellte LLM gesendet werden, werden nicht verwendet, um das von Braze bereitgestellte LLM zu trainieren oder zu verbessern. Zwischen Ihnen und Braze ist der Output Ihre geistige Eigenschaft. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Ausgaben. Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich Output.

Das von Braze zur Verfügung gestellte LLM für Braze-Agenten, das als "Auto" bezeichnet wird, verwendet Google Gemini-Modelle. Google speichert die über Braze übermittelten Inputs und Outputs 55 Tage lang, danach werden die Daten gelöscht.
