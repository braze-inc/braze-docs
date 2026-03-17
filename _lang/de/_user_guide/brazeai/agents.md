---
nav_title: Agentenkonsole
article_title: Braze-Agenten
page_order: 1
description: "Braze Agents können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können."
---

# Braze-Agenten in der Agent-Konsole

> Braze Agents sind KI-gestützte Assistenten, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können.

{% alert important %}
Für den Zugriff auf und die Nutzung von Braze Agents sind Nachrichtenguthaben erforderlich. Sollten Sie derzeit nicht über Nachrichtenguthaben verfügen und Braze Agents nutzen möchten, wenden Sie sich bitte an Ihren Account Manager, um die nächsten Schritte zu besprechen.
{% endalert %}

## Warum sollten Sie Braze Agents einsetzen?

Braze Agents unterstützen Ihr Team dabei, intelligentere und personalisierte Erlebnisse zu bieten – ohne zusätzlichen Arbeitsaufwand. Sie agieren als autonome Agenten, die nicht nur auf Eingaben reagieren, sondern auch den Kontext verstehen, Entscheidungen treffen und Maßnahmen ergreifen, um ein Ziel zu erreichen.

In der Praxis können Agenten automatisch Nachrichtentexte erstellen, wie Betreffzeilen oder Produkttexte, sodass jede Kund:in eine auf sie angepasste Kommunikation erhält. Sie können sich auch in Realtime anpassen und Personen basierend auf Präferenzen, Verhaltensweisen oder anderen Daten über verschiedene Canvas-Pfade leiten.

Über das Messaging hinaus können Agenten Ihre Kataloge bereichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten aktuell und dynamisch halten. Durch die Übernahme repetitiver oder komplexer Aufgaben ermöglichen sie Ihrem Team, sich auf Strategie und Kreativität zu konzentrieren, anstatt sich mit manuellen Setup-Aufgaben zu befassen. Braze-Agenten agieren eher als Kooperationspartner denn als Hintergrundprozesse – sie unterstützen Sie bei der Lösung von Problemen und erzielen eine große Wirkung.

### Wann sollten Braze-Agenten im Vergleich zu anderen BrazeAI-Features eingesetzt werden?

Verwenden Sie Agenten, um Inhalte anhand des spezifischen Kontexts einer Nutzer:in in Echtzeit zu personalisieren. Wenn ein Agent beispielsweise weiß, dass die bevorzugte Eissorte einer bestimmten Nutzer:in Schokolade ist und seine bevorzugte Garnierung Gummibärchen sind, kann er eine Push-Nachricht erstellen, die speziell auf diese Kombination für diese Nutzer:in zugeschnitten ist, wenn diese den Canvas durchläuft.

Der Agent lernt jedoch nicht durch Versuch und Irrtum und hat keine Idee von einem endgültigen Ziel des Marketings, das er messen und maximieren möchte. Selbst wenn Sie das System anweisen, generell Texte zu verfassen, die zu Konversionen führen, verfügt es über keinen Mechanismus, um die Auswirkungen seines agentenbasierten Schreibens auf die Konversion zu überwachen und diese Daten in zukünftige agentenbasierte Aufrufe zu integrieren. Man kann sich dies als eine „Stimmungs“-Entscheidung vorstellen, nicht als eine belohnungsbasierte KI-Entscheidung.

Im Gegensatz dazu sind andere BrazeAI-Tools darauf ausgelegt, die von ihnen gemessenen Metriken zu maximieren. Beispielsweise sind Agenten sehr gut darin, qualitativ zu beurteilen, inwiefern die Eigenschaften einer Nutzer:in dessen Wahrscheinlichkeit oder Neigung beeinflussen, eine bestimmte Handlung auszuführen oder ein bestimmtes Produkt zu mögen. Da der Agent jedoch nicht durch Versuch und Irrtum lernt, hat er keine Idee, wie er seine Genauigkeit bei der Vorhersage von Wahrscheinlichkeiten messen und das Signal im Laufe der Zeit verbessern kann. Daher übertrifft die Verwendung von Predictive Suite den Agent-Schritt, wenn man die Genauigkeit der Prognosen und die Verbesserungen im Laufe der Zeit betrachtet.

## Features

Zu den Features für Braze-Agenten gehören:

- **Flexible Einrichtung:** Verwenden Sie ein von Braze bereitgestelltes LLM oder verbinden Sie Ihre eigenen [KI-Modellanbieter]({{site.baseurl}}/partners/ai_model_providers) (wie OpenAI, Anthropic oder Google Gemini).
- **Nahtlose Integration:** Agenten können direkt in Canvas-Schritten oder Katalogfeldern eingesetzt werden.
- **Test- und Protokollierungstools:** Bitte erhalten Sie eine Vorschau auf die Ausgabe Ihres Agenten vor dem Start, indem Sie ihn mit Beispiel-Eingaben testen. Zeigen Sie die Protokolle für jeden Ausführungsvorgang des Agenten an, einschließlich der Ein- und Ausgaben für diesen Vorgang.
- **Nutzungskontrollen:** Tägliche Limits unterstützen bei der Verwaltung von Performance und Kosten.

## Über Braze-Agenten

Agenten werden mit Anweisungen (Systemaufforderungen) konfiguriert, die ihr Verhalten definieren. Wenn ein Agent ausgeführt wird, verwendet er Ihre Anweisungen zusammen mit den von Ihnen übermittelten Daten, um eine Antwort zu generieren.

### Wichtige Konzepte

| Term | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | Das „Gehirn“ des Agenten, in diesem Fall ein großes Sprachmodell (LLM). Es interpretiert Eingaben, generiert Antworten und führt Schlussfolgerungen durch. Ein leistungsfähigeres Modell (das auf relevanteren Daten trainiert wurde) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten mitteilen (Systemaufforderung). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Agenten zuverlässiger und berechenbarer. |
| Kontext | Daten, die während der Laufzeit an den Agenten übermittelt werden, unabhängig davon, wo dieser eingesetzt wird, wie beispielsweise Felder des Nutzerprofils oder Katalogzeilen. Diese Eingabe liefert die Informationen, die der Agent zur Generierung von Ausgaben verwendet. |
| [Ausgangsvariable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Workflow-Pfade zu steuern. Ausgabevariablen können vom Datentyp String, Zahl oder Boolesche Variable sein.  |
| [Ausführung](#limitations) | Ein einzelner Durchlauf des Agenten. Dies wird auf Ihre täglichen Limits angerechnet. |
| [Ausgabeformat]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | Die vordefinierte Struktur der Daten der Antwort des Agenten. |
| [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) | Der Grad der Abweichung für die Leistung des Agenten. Dies bestimmt, wie präzise oder kreativ Ihr Agent sein kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

Es gelten die folgenden Einschränkungen:

- Jeder Agent verfügt über ein Standard-Tägliches Ausführungslimit von 250.000 Ausführungen, das auf maximal 1.000.000 Ausführungen pro Tag erhöht werden kann. Bitte wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie daran interessiert sind, dieses Limit zu erhöhen.
- Standardmäßig muss jeder Durchlauf innerhalb von 15 Sekunden abgeschlossen sein. Nach 15 Sekunden sendet der Agent eine`null`Antwort zurück, wo sie verwendet wird.
    - Sollten Ihre Agenten regelmäßig eine Zeitüberschreitung haben, wenden Sie sich bitte an Ihren Braze-Account Manager, um dieses Limit zu erhöhen.
- Die Daten zur Eingabe sind auf 25 KB pro Anfrage begrenzt. Längere Eingaben werden gekürzt.

## Wie werden meine Daten verwendet und an die von Braze bereitgestellten LLMs übermittelt?

Um KI-Ergebnisse über die Braze AI-Features zu generieren, die Braze als Nutzung der von Braze bereitgestellten LLMs identifiziert („Ergebnisse“), übermittelt Braze Ihre Systemaufforderung oder gegebenenfalls andere Eingaben („Eingaben“) an das von Braze bereitgestellte LLM. Die an das von Braze bereitgestellte LLM gesendeten Daten werden nicht zum Trainieren oder Verbessern des von Braze bereitgestellten LLM verwendet. Zwischen Ihnen und Braze ist der Output Ihre geistige Eigenschaft. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Ausgaben. Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich Output.

Das von Braze bereitgestellte LLM für Braze-Agenten, das einen Bezeichner „Auto“ hat, nutzt Google Gemini-Modelle. Google speichert die über Braze übermittelten Eingaben und Ausgaben für einen Zeitraum von 55 Tagen. Nach Ablauf dieser Frist werden die Daten gelöscht.

## Nächste Schritte

Nachdem Sie nun über Braze Agents informiert sind, können Sie mit den nächsten Schritten fortfahren:

- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
