---
nav_title: Agent
article_title: Agentenschritt
alias: /agent_step/
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die Verwendung des Agent-Schritts in Canvas, um Inhalte zu generieren oder intelligente Entscheidungen in Realtime zu treffen."
tool: Canvas
toc_headers: h2
---

# Agentenschritt  

> Mit dem Schritt „Agent“ können Sie KI-gestützte Entscheidungsfindung und Inhaltserstellung direkt in Ihren Canvas-Workflow integrieren. Für weitere allgemeine Informationen, siehe [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Ein Agentenschritt in einer Canvas-Benutzerreise.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Funktionsweise

Wenn ein Nutzer einen Agentenschritt in einem Braze-Canvas erreicht, übermittelt Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an den von Ihnen ausgewählten Agenten. Der Agent verarbeitet dann die Eingabe anhand seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariablen gespeichert, die Sie in diesem Schritt definiert haben.

Sie können diese Variable dann auf drei Arten verwenden:

- **Entscheidungsfindung:** Leiten Sie die Nutzer:innen basierend auf der Antwort des Agenten auf unterschiedliche Canvas-Pfade weiter. Beispielsweise könnte ein Lead-Scoring-Agent eine Zahl zwischen 1 und 10 zurückgeben. Anhand dieser Punktzahl können Sie entscheiden, ob Sie einer Nutzer:in weiterhin Nachrichten per Messaging senden oder sie aus der Customer Journey entfernen möchten.
- **Personalisierung:** Fügen Sie die Antwort des Mitarbeiters direkt in eine Nachricht ein. Beispielsweise könnte ein Mitarbeiter Kundenfeedback analysieren und eine einfühlsame Folge-E-Mail verfassen, die den Kommentar der Kund:in referenziert und eine Lösung vorschlägt.
- **Verarbeitung von Nutzerdaten:** Analysieren und standardisieren Sie Ihre Nutzerdaten, speichern Sie diese anschließend im Nutzerprofil oder senden Sie sie mithilfe eines Webhooks. Beispielsweise könnte ein Agent eine Stimmungsbewertung oder eine Affinitätszuordnung für Produkte zurückgeben. Sie können diese Daten in einem Nutzerprofil für die zukünftige Verwendung speichern.

## Voraussetzung

Agent-Schritte verwenden [Canvas-Kontextvariablen,]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) um relevanten Kontext zu erfassen und eine Variable auszugeben, die in Canvas genutzt werden kann.

## Erstellen eines Agentenschritts

### Schritt 1: Einen Schritt hinzufügen

Ziehen Sie die Komponente **„Agent”** aus der Seitenleiste per Drag-and-Drop oder wählen Sie **„Agent”** über den Button<i class="fas fa-plus-circle"></i> „Plus” am unteren Rand eines Schritts aus.  

### Schritt 2: Ihren Agenten auswählen  

Wählen Sie den Agenten aus, der die Daten in diesem Schritt verarbeiten soll. Bitte wählen Sie einen vorhandenen Agenten aus. Anleitungen zur Einrichtung finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Schritt 3: Legen Sie die Ausgabe Ihres Agenten fest. {#define-the-output-variable}

Agentenausgaben werden als „Ausgabevariablen“ bezeichnet und zur leichteren Zugänglichkeit in einer [Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) gespeichert. Um die Ausgabevariable zu definieren, benennen Sie die Variable bitte.

Bitte beachten Sie, dass der Datentyp der Ausgabevariablen über die [Agent-Konsole]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt wird. Agentenausgaben können als Strings, Zahlen, Boolesche Werte oder Objekte gespeichert werden. Dadurch sind sie sowohl für die Text-Personalisierung als auch für die bedingte Logik in Ihrem Canvas flexibel einsetzbar. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Häufige Verwendungszwecke |
| --- | --- |
| String | Personalisierung von Nachrichten (Betreffzeilen, Text, Antworten) |
| Zahl | Bewertung, Schwellenwerte, Weiterleitung in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolesch | Ja/Nein-Branchen in [Decision-Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objekt | Nutzen Sie einen oder mehrere der oben genannten Datentypen mit einem einzigen LLM-Aufruf in einer vorhersehbaren Datenstruktur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können eine Ausgabevariable im gesamten Canvas verwenden, indem Sie dieselbe Syntax des Templates wie bei einer Kontextvariablen verwenden. Bitte verwenden Sie entweder den Segment-Filter **„Kontextvariable“** oder erstellen Sie die Antworten des Agenten direkt mit Liquid:{% raw %}`{{context.${response_variable_name}}}` {% endraw %} .

Um eine bestimmte Eigenschaft aus einer Objekt-Ausgabevariablen zu verwenden, nutzen Sie die Punktnotation, um mit Liquid auf diese Eigenschaft zuzugreifen: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agentenschritt für Body HTML Writer mit einer Datenausgabe für die Variable/assets/img/ai_agent/test_agent_step.pngimage_buster"agent_output".]({%%}){: style="max-width:80%;"}

### Schritt 4: Fügen Sie gegebenenfalls zusätzlichen Kontext hinzu (optional)

Sie können zusätzliche Kontextwerte für den Agentenschritt hinzufügen, die von diesem bei seiner Ausführung referenziert werden können. Sie können alle Liquid-Templates eingeben, die Sie normalerweise in einem Canvas verwenden würden.

{% alert note %}
Bitte beachten Sie, dass der Agent bereits automatisch den im Abschnitt **„Anweisungen“** konfigurierten Kontext erhält. Liquid-Variablen, die dort bereits konfiguriert wurden, müssen hier nicht erneut eingegeben werden.
{% endalert %}

![Die Möglichkeit, einem Agentenschritt mithilfe von Liquid zusätzlichen Kontext hinzuzufügen.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Schritt 5: Bitte überprüfen Sie den Agenten.

Nachdem Sie Ihren Agentenschritt eingerichtet haben, können Sie die Ausgabe dieses Schritts testen und in der Vorschau anzeigen.

![Vorschau der Agentenausgabe als zufälliger Nutzer:in.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Fehlerbehandlung  

- Wenn das verbundene Modell einen Fehler bei den Rate-Limits zurückgibt, wiederholt Braze den Versuch bis zu fünf Mal mit exponentiellem Backoff.  
- Sollte der Agent aus einem anderen Grund fehlschlagen (z. B. aufgrund eines Zeitüberschreitungsfehlers oder eines ungültigen API-Schlüssels), wird die Ausgabevariable auf gesetzt`null`.
    - Wenn ein Agent sein tägliches Aufruflimit erreicht, wird die Ausgabevariable auf gesetzt`null`. Wenn Sie die Ausgabe eines Agenten in einem Schritt für Nachrichten verwenden, sollten Sie die Verwendung von [Standard-Liquid-Werten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values) in Betracht ziehen.
- Antworten werden für identische Eingaben zwischengespeichert und können für wiederholte identische Aufrufe innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, werden weiterhin zur Gesamtzahl und zu den täglichen Aufrufen gezählt.

## Analytics  

Bitte referieren Sie auf die folgenden Metriken, um die Performance Ihrer Agentenschritte zu verfolgen:  

| Metrisch | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Fälle, in denen Nutzer:innen den Agentenschritt aufgerufen haben. |
| _Fortgefahren mit nächstem Schritt_ | Die Anzahl der Nutzer:innen, die nach Durchlaufen des Agentenschritts zum nächsten Schritt im Ablauf übergegangen sind. |
| _Canvas wurde verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas nach Durchlaufen des Agent-Schritts verlassen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Wann sollte ich einen Agentenschritt verwenden?

Im Allgemeinen empfehlen wir die Verwendung eines Agent-Schritts, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen möchten und dieses eine Canvas-Kontextvariable auf intelligente Weise in einem für Menschen unmöglichen Umfang zuweisen soll.

Angenommen, Sie senden eine personalisierte Nachricht, um einem Nutzer:in, der zuvor Schokolade und Erdbeere bestellt hat, eine neue Eissorte zu empfehlen. Hier ist der Unterschied zwischen der Verwendung eines Agent-Schritts und KI-Artikelempfehlungen:

- **Agentenschritt:** Verwendet LLMs, um auf der Grundlage der Anweisungen und Kontextdatenpunkte, die dem Agenten zur Verfügung gestellt werden, eine qualitative Entscheidung darüber zu treffen, was der Nutzer:in möglicherweise wünscht. In diesem Beispiel könnte ein Agent-Schritt eine neue Geschmacksrichtung empfehlen, basierend auf der Möglichkeit, dass die Nutzer:innen verschiedene Geschmacksrichtungen ausprobieren möchten.
- **KI-Artikelempfehlungen:** Verwendet Modelle des maschinellen Lernens, um auf Grundlage früherer Benutzeraktivitäten, wie beispielsweise Käufe, die Produkte vorherzusagen, die ein Benutzer am ehesten wünschen könnte. In diesem Beispiel würden KI-Artikelempfehlungen eine Geschmacksrichtung (Vanille) vorschlagen, basierend auf den beiden vorherigen Bestellungen des Nutzers (Schokolade und Erdbeere) und einem Vergleich dieser Bestellungen mit dem Verhalten anderer Nutzer:innen in Ihrem Workspace.

### Wie verwenden Agent-Schritte Daten?

Ein Agentenschritt analysiert die Daten zum Kontext, für deren Verwendung der Agent konfiguriert ist, sowie alle zusätzlichen Kontexte, die [dem Agenten zur Verfügung gestellt](#step-4-add-any-additional-context-optional) werden.

## Ähnliche Artikel  

- [Übersicht über Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referenz für Vertreter]({{site.baseurl}}/user_guide/brazeai/agents/reference/)  