---
nav_title: Agenten
article_title: Braze-Agenten
page_order: 0.5
description: "Braze Agents können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, so dass Sie personalisiertere Kundenerlebnisse zustellen können."
---

# Braze-Agenten

> Braze-Agenten sind KI-gestützte Helfer, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, so dass Sie personalisiertere Kundenerlebnisse zustellen können.

{% alert important %}
Braze Agents befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Warum Braze-Agenten verwenden?

Braze Agents helfen Ihrem Team, intelligentere, personalisierte Erlebnisse zuzustellen - ohne zusätzliche Arbeit. Sie agieren als intelligente Assistenten, die nicht nur auf Aufforderungen reagieren, sondern den Kontext verstehen, Entscheidungen treffen und auf ein Ziel hinarbeiten.

In der Praxis können Agenten automatisch Nachrichten - wie Betreffzeilen oder produktinterne Texte - erstellen, so dass jeder Kunde eine auf ihn zugeschnittene Kommunikation erhält. Sie können sich auch in Echtzeit anpassen und Menschen auf der Grundlage von Vorlieben, Verhaltensweisen oder anderen Daten durch verschiedene Canvas-Pfade leiten.

Über Messaging hinaus können Agenten Ihre Kataloge anreichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten frisch und dynamisch halten. Indem sie sich wiederholende oder komplexe Aufgaben übernehmen, geben sie Ihrem Team den nötigen Freiraum, um sich auf Strategie und Kreativität zu konzentrieren, statt auf die manuelle Einrichtung. Braze-Agenten agieren eher wie Mitarbeiter als wie Hintergrundprozesse - sie helfen Ihnen, Probleme zu lösen und in großem Umfang Wirkung zu erzielen.

## Features

Features für Braze Agents umfassen:

- **Flexible Einrichtung:** Verwenden Sie eine von Braze bereitgestellte LLM oder verbinden Sie Ihren eigenen Modellanbieter (wie OpenAI, Anthropic, Google Gemini oder AWS Bedrock).
- **Nahtlose Integration:** Setzen Sie Agenten direkt in Canvas-Schritten oder Katalogfeldern ein.
- **Tools zum Testen und Protokollieren:** Machen Sie eine Vorschau auf die Ausgabe Ihres Agenten, indem Sie ihn vor dem Start mit Beispieleingaben testen. Zeigen Sie die Protokolle für jede Ausführung des Agenten an, einschließlich der Eingaben und Ausgaben für diese Ausführung.
- **Kontrolle der Verwendung:** Eingebaute Aufruf- und Größenbeschränkungen helfen, Performance und Kosten zu verwalten.

## Über Braze Agents

Agenten werden mit Anweisungen (System-Prompts) konfiguriert, die festlegen, wie sie sich verhalten. Wenn ein Agent ausgeführt wird, verwendet er Ihre Anweisungen zusammen mit den von Ihnen übermittelten Daten, um eine Antwort zu erzeugen. 

### Wichtige Konzepte

| Term | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | Das "Gehirn" des Agenten, in diesem Fall ein großes Sprachmodell (LLM). Es interpretiert Eingaben, erzeugt Antworten und führt Schlussfolgerungen aus. Ein stärkeres Modell (trainiert auf mehr relevanten Daten) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemaufforderung). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Wirkstoff zuverlässiger und berechenbarer. |
| Kontext | Daten, die zur Laufzeit an den Agenten übergeben werden, unabhängig davon, wo er eingesetzt wird, z.B. Felder des Nutzerprofils oder Katalogzeilen. Diese Eingabe liefert die Informationen, die der Agent zur Erzeugung von Ausgaben verwendet. |
| [Variable ausgeben]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Arbeitsabläufe zu steuern. Ausgabevariablen können ein String, eine Zahl oder ein boolescher Datentyp sein.  |
| Anrufung | Eine einzige Ausführung des Agenten. Dies wird auf Ihr Tages- und Gesamtlimit angerechnet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

Agenten bearbeiten Anfragen mit etwa 1.000 Aufrufen pro Minute. Jeder Workspace kann bis zu 1.000 Agenten unterstützen. Wenn dieses Limit erreicht ist, müssen Sie einen bestehenden Agenten entfernen, bevor Sie einen neuen erstellen können. 

Zusätzlich während der Beta-Phase:

- Der Aufruf ist auf 50.000 Durchläufe pro Tag und 500.000 Durchläufe insgesamt begrenzt.
- Jeder Lauf muss innerhalb von 30 Sekunden abgeschlossen sein. Nach 30 Sekunden wird der Agent eine Null-Antwort zurückgeben, wenn er verwendet wird.
- Die Eingabedaten sind auf 10 KB pro Anfrage begrenzt. Längere Eingaben werden abgeschnitten.
- Bei Katalogen aktualisieren die agenturischen Felder nur die ersten 10.000 Zeilen.

## Nächste Schritte

Jetzt, da Sie die Braze-Agenten kennen, sind Sie bereit für die nächsten Schritte:

- [Anpassen von Agenten]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
