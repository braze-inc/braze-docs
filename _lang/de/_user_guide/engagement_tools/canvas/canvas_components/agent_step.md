---
nav_title: Agent
article_title: Agentenschritt
alias: /agent_step/
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die Verwendung des Agent-Schritts in Canvas, um Inhalte zu generieren oder intelligente Entscheidungen in Echtzeit zu treffen."
tool: Canvas
toc_headers: h2
---

# Agentenschritt  

> Mit dem Schritt „Agent" können Sie KI-gestützte Entscheidungsfindung und Inhaltserstellung direkt in Ihren Canvas-Workflow integrieren. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Ein Agentenschritt in einer Canvas-User-Journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Funktionsweise

Wenn eine Nutzer:in einen Agentenschritt in einem Canvas erreicht, übermittelt Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an den von Ihnen ausgewählten Agenten. Der Agent verarbeitet dann die Eingabe anhand seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariablen gespeichert, die Sie in diesem Schritt definiert haben.

Sie können diese Variable dann auf drei Arten verwenden:

- **Entscheidungsfindung:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agenten auf unterschiedliche Canvas-Pfade weiter. Beispielsweise könnte ein Lead-Scoring-Agent eine Zahl zwischen 1 und 10 zurückgeben. Anhand dieser Punktzahl können Sie entscheiden, ob Sie einer Nutzer:in weiterhin Nachrichten senden oder sie aus der Journey entfernen möchten.
- **Personalisierung:** Fügen Sie die Antwort des Agenten direkt in eine Nachricht ein. Beispielsweise könnte ein Agent Kundenfeedback analysieren und eine einfühlsame Folge-E-Mail verfassen, die den Kommentar der Kund:in referenziert und eine Lösung vorschlägt.
- **Verarbeitung von Nutzerdaten:** Analysieren und standardisieren Sie Ihre Nutzerdaten und speichern Sie diese anschließend im Nutzerprofil oder senden Sie sie mithilfe eines Webhooks. Beispielsweise könnte ein Agent eine Stimmungsbewertung oder eine Produkt-Affinitätszuordnung zurückgeben. Sie können diese Daten in einem Nutzerprofil für die zukünftige Verwendung speichern.

## Voraussetzung

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables), um relevanten Kontext zu erfassen und eine Variable auszugeben, die im Canvas genutzt werden kann.

## Erstellen eines Agentenschritts

### 1. Schritt: Einen Schritt hinzufügen

Ziehen Sie die Komponente **„Agent"** aus der Seitenleiste per Drag-and-Drop oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und dann **Agent** aus.  

### 2. Schritt: Ihren Agenten auswählen  

Wählen Sie den Agenten aus, der die Daten in diesem Schritt verarbeiten soll. Wählen Sie einen vorhandenen Agenten aus. Anleitungen zur Einrichtung finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### 3. Schritt: Legen Sie die Ausgabe Ihres Agenten fest {#define-the-output-variable}

Agentenausgaben werden als „Ausgabevariablen" bezeichnet und zur leichteren Zugänglichkeit in einer [Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) gespeichert. Um die Ausgabevariable zu definieren, vergeben Sie einen Namen für die Variable.

Beachten Sie, dass der Datentyp der Ausgabevariablen über die [Agent-Konsole]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt wird. Agentenausgaben können als Strings, Zahlen, Boolesche Werte oder Objekte gespeichert werden. Dadurch sind sie sowohl für die Text-Personalisierung als auch für bedingte Logik in Ihrem Canvas flexibel einsetzbar. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Häufige Verwendungszwecke |
| --- | --- |
| String | Personalisierung von Nachrichten (Betreffzeilen, Text, Antworten) |
| Zahl | Bewertung, Schwellenwerte, Weiterleitung in [Zielgruppenpfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolescher Wert | Ja/Nein-Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objekt | Nutzen Sie einen oder mehrere der oben genannten Datentypen mit einem einzigen LLM-Aufruf in einer vorhersehbaren Datenstruktur |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können eine Ausgabevariable im gesamten Canvas verwenden, indem Sie dieselbe Template-Syntax wie bei einer Kontextvariablen nutzen. Verwenden Sie entweder den Segment-Filter **„Kontextvariable"** oder fügen Sie die Antworten des Agenten direkt mit Liquid ein: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Um eine bestimmte Eigenschaft aus einer Objekt-Ausgabevariablen zu verwenden, nutzen Sie die Punktnotation, um mit Liquid auf diese Eigenschaft zuzugreifen: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agentenschritt für Body HTML Writer mit einem Objekt-Datentyp als Ausgabe für die Variable „agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### 4. Schritt: Zusätzlichen Kontext hinzufügen (optional)

Sie können zusätzliche Kontextwerte für den Agentenschritt hinzufügen, auf die dieser bei seiner Ausführung zugreifen kann. Sie können alle Liquid-Template-Werte eingeben, die Sie normalerweise in einem Canvas verwenden würden.

{% alert note %}
Beachten Sie, dass der Agent bereits automatisch den im Abschnitt **„Anweisungen"** konfigurierten Kontext erhält. Liquid-Variablen, die dort bereits konfiguriert wurden, müssen hier nicht erneut eingegeben werden.
{% endalert %}

![Die Möglichkeit, einem Agentenschritt mithilfe von Liquid zusätzlichen Kontext hinzuzufügen.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### 5. Schritt: Den Agenten testen

Nachdem Sie Ihren Agentenschritt eingerichtet haben, können Sie die Ausgabe dieses Schritts testen und in der Vorschau anzeigen.

![Vorschau der Agentenausgabe als zufällige Nutzer:in.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Fehlerbehandlung  

- Wenn das verbundene Modell einen Rate-Limit-Fehler zurückgibt, wiederholt Braze den Versuch bis zu fünf Mal mit exponentiellem Backoff.  
- Sollte der Agent aus einem anderen Grund fehlschlagen (z. B. aufgrund eines Zeitüberschreitungsfehlers oder eines ungültigen API-Schlüssels), wird die Ausgabevariable auf `null` gesetzt.
    - Wenn ein Agent sein tägliches Aufruflimit erreicht, wird die Ausgabevariable auf `null` gesetzt. 
- Verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values), um Fehler abzufangen. Beispielsweise können Sie im Modal **„Personalisierung hinzufügen"** einen Standard-Liquid-Wert eingeben, wie {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} oder {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Antworten werden für identische Eingaben zwischengespeichert und können für wiederholte identische Aufrufe innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, werden weiterhin zur Gesamtzahl und zu den täglichen Aufrufen gezählt.
- Agentenschritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Wenn Sie Nutzer:innen sehen, die in diesem Schritt noch ausstehend sind, überprüfen Sie Ihre Logs, um sicherzustellen, dass Aufrufe stattfinden.

## Analytics  

Verwenden Sie die folgenden Metriken, um die Performance Ihrer Agentenschritte zu verfolgen:  

| Metrik | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Fälle, in denen Nutzer:innen den Agentenschritt aufgerufen haben. |
| _Zum nächsten Schritt fortgefahren_ | Die Anzahl der Nutzer:innen, die nach Durchlaufen des Agentenschritts zum nächsten Schritt im Ablauf übergegangen sind. |
| _Canvas verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas nach Durchlaufen des Agentenschritts verlassen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Wann sollte ich einen Agentenschritt verwenden?

Im Allgemeinen empfehlen wir die Verwendung eines Agentenschritts, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen möchten und dieses eine Canvas-Kontextvariable auf intelligente Weise in einem für Menschen unmöglichen Umfang zuweisen soll.

Angenommen, Sie senden eine personalisierte Nachricht, um einer Nutzer:in, die zuvor Schokolade und Erdbeere bestellt hat, eine neue Eissorte zu empfehlen. Hier ist der Unterschied zwischen der Verwendung eines Agentenschritts und KI-Artikelempfehlungen:

- **Agentenschritt:** Verwendet LLMs, um auf der Grundlage der Anweisungen und Kontextdatenpunkte, die dem Agenten zur Verfügung gestellt werden, eine qualitative Entscheidung darüber zu treffen, was die Nutzer:in möglicherweise wünscht. In diesem Beispiel könnte ein Agentenschritt eine neue Geschmacksrichtung empfehlen, basierend auf der Möglichkeit, dass die Nutzer:in verschiedene Geschmacksrichtungen ausprobieren möchte.
- **KI-Artikelempfehlungen:** Verwendet Modelle des maschinellen Lernens, um auf Grundlage früherer Nutzeraktivitäten wie beispielsweise Käufe die Produkte vorherzusagen, die eine Nutzer:in am ehesten wünschen könnte. In diesem Beispiel würden KI-Artikelempfehlungen eine Geschmacksrichtung (Vanille) vorschlagen, basierend auf den beiden vorherigen Bestellungen der Nutzer:in (Schokolade und Erdbeere) und einem Vergleich dieser Bestellungen mit dem Verhalten anderer Nutzer:innen in Ihrem Workspace.

### Wie verwenden Agentenschritte Eingabedaten?

Ein Agentenschritt analysiert die Kontextdaten, für deren Verwendung der Agent konfiguriert ist, sowie alle zusätzlichen Kontexte, die [dem Agenten zur Verfügung gestellt](#step-4-add-any-additional-context-optional) werden.

## Verwandte Artikel  

- [Übersicht über Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referenz für Agenten]({{site.baseurl}}/user_guide/brazeai/agents/reference/)