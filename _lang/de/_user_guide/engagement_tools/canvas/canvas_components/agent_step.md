---
nav_title: Agent
article_title: Agentenschritt
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie den Agent-Schritt in Canvas verwenden, um Inhalte zu generieren oder intelligente Entscheidungen in Echtzeit zu treffen."
tool: Canvas
toc_headers: h2
---

# Agent Schritt  

> Mit dem Agent-Schritt können Sie KI-gestützte Entscheidungsfindung und Inhaltserstellung direkt in Ihren Canvas-Workflow integrieren. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Ein Agent-Schritt in einer Canvas-Nutzer:innen-Reise.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Funktionsweise

Wenn ein Nutzer:innen in einem Canvas einen Agenten-Schritt erreicht, sendet Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an den von Ihnen gewählten Agenten. Der Agent verarbeitet dann die Eingabe anhand seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariablen gespeichert, die Sie in dem Schritt definiert haben.

Sie können diese Variable dann auf zwei Arten verwenden:

- **Entscheidungsfindung:** Leiten Sie Nutzer:innen je nach der Antwort des Agenten auf verschiedene Canvas-Pfade weiter. Ein Lead Scoring Agent könnte zum Beispiel eine Zahl zwischen 1 und 10 zurückgeben. Anhand dieser Punktzahl können Sie entscheiden, ob Sie das Messaging mit einem Nutzer:innen fortsetzen oder ihn von der Reise ausschließen.
- **Personalisierung:** Fügen Sie die Antwort des Agenten direkt in eine Nachricht ein. Ein Agent könnte zum Beispiel das Feedback eines Kunden analysieren und eine einfühlsame E-Mail erstellen, die den Kommentar des Kunden referenziert und eine Lösung vorschlägt.

## Schritt zum Erstellen eines Agenten

### Schritt 1: Einen Schritt hinzufügen

Ziehen Sie die **Agentenkomponente** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> plus Button am unteren Rand eines Schritts und wählen Sie **Agent**.  

### Schritt 2: Wählen Sie Ihren Agenten aus  

Wählen Sie den Agenten aus, der die Daten in diesem Schritt verarbeiten soll. Wählen Sie einen vorhandenen Agenten aus oder erstellen Sie direkt in diesem Schritt einen neuen Agenten. Eine Anleitung zur Einrichtung finden Sie unter [Anpassen von Agenten]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Schritt 3: Definieren Sie die Ausgabevariable

Die Ausgaben der Agenten werden als "Ausgabevariablen" bezeichnet und in einer [Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) gespeichert, um den Zugriff zu erleichtern. Um die Ausgabevariable zu definieren:

1. Geben Sie der Variable einen Namen.
2. Wählen Sie einen Datentyp aus. 

Die Ausgaben der Agenten können als Strings, Zahlen, Boolesche Werte oder Objekte gespeichert werden. Dadurch sind sie sowohl für die Personalisierung von Texten als auch für die bedingte Logik in Ihrem Canvas flexibel. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Häufige Verwendungen |
| --- | --- |
| String | Personalisierung von Nachrichten (Betreffzeilen, Texte, Antworten) |
| Zahl | Scoring, Schwellenwerte, Routing in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolesch | Ja/Nein Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objekt | Nutzen Sie einen oder mehrere der oben genannten Datentypen mit einem einzigen LLM-Aufruf in einer prognostischen Datenstruktur |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn sie definiert ist, können Sie eine Ausgabevariable im gesamten Canvas verwenden, indem Sie die gleiche Template-Syntax wie bei einer Kontextvariablen verwenden. Verwenden Sie entweder den Filter für **kontextvariable** Segmente oder das Template für Agentenantworten direkt mit Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Um eine bestimmte Eigenschaft einer Objektausgabevariablen zu verwenden, greifen Sie mit Liquid in Punktschreibweise auf diese Eigenschaft zu: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agentenschritt für Body HTML Writer mit Ausgabe eines Objektdatentyps für die Variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

Verwenden Sie die oben gezeigten Liquid-Syntaxmuster, um in zukünftigen Canvas-Schritten bestimmte Felder aus der Agentenausgabe zu referenzieren.

### Schritt 4: Entscheiden Sie, welchen Kontext Sie dem Agenten bieten möchten  

Sie müssen entscheiden, welche Daten der Agent zur Laufzeit erhalten soll. Die folgenden Optionen sind verfügbar:  

- **Alle Canvas-Kontexte einbeziehen:** Übergeben Sie alle verfügbaren Canvas-Kontextvariablen (z.B. [Eingangs-Eigenschaften von Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) an den Agent-Schritt. Sie können Context-Schritte vor den Agentenschritten verwenden, um dem Context weitere Daten vorzuschalten.
- **Liefern Sie Werte:** Übergeben Sie nur ausgewählte Eigenschaften, wie z.B. den Vornamen oder die Lieblingsfarbe eines Nutzers:innen. Wählen Sie diese Option, um dem Agenten nur Zugriff auf die Werte zu geben, die Sie hier zuweisen. Geben Sie für jeden **Schlüssel** den [Liquid-Tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) ein, der das spezifische Feld des Nutzerprofils oder die Kontextvariable definiert.  

{% alert note %}
Braze gibt die ersten 10 KB des Inhalts an den Agenten weiter. Die Angabe von Werten, deren Gesamtwert 10 KB übersteigt, führt zu einer Abschneidung.
{% endalert %}

### Schritt 5: Testen Sie den Agenten

Nachdem Sie Ihren Agent-Schritt eingerichtet haben, können Sie die Ausgabe dieses Schritts testen und eine Vorschau anzeigen.

## Fehlerbehandlung  

- Wenn das verbundene Modell einen Rate-Limits-Fehler meldet, versucht Braze es bis zu fünf Mal mit exponentiellem Backoff.  
- Wenn der Agent aus einem anderen Grund fehlschlägt (z.B. ungültiger API-Schlüssel), wird die Ausgabevariable auf `null` gesetzt.
    - Wenn ein Agent sein tägliches Aufruflimit erreicht, wird die Ausgangsvariable auf `null` gesetzt. Wenn Sie die Ausgabe eines Agenten in einem Nachrichtenschritt verwenden, sollten Sie die Abbruchlogik von Liquid nutzen.
- Antworten werden für identische Eingaben zwischengespeichert und können für wiederholte identische Aufrufe innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, zählen trotzdem für die Gesamtzahl und die täglichen Aufrufe.

## Analytics  

Anhand der folgenden Metriken können Sie das Tracking der Performance Ihrer Agentenschritte verfolgen:  

| Metrisch | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Nutzer:innen, die den Schritt Agent eingegeben haben. |
| _Fortgefahren mit nächstem Schritt_ | Die Anzahl der Nutzer:innen, die nach dem Schritt Agent zum nächsten Schritt im Ablauf übergegangen sind. |
| _Canvas wurde verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas verlassen haben, nachdem sie den Agenten-Schritt durchlaufen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Wann sollte ich einen Agentenschritt verwenden?

Im Allgemeinen empfehlen wir die Verwendung eines Agenten-Schrittes, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen und dieses auf intelligente Weise Canvas-Kontextvariablen zuweisen möchten, und zwar in einem Umfang, der für Menschen unmöglich ist.

Nehmen wir an, Sie senden eine personalisierte Nachricht, um einem Nutzer:innen, der zuvor Schokolade und Erdbeere bestellt hat, eine neue Eissorte zu empfehlen. Hier ist der Unterschied zwischen der Verwendung eines Agentenschritts und KI-Artikel-Empfehlungen:

- **Schritt des Agenten:** Verwendet LLMs, um eine qualitative Entscheidung darüber zu treffen, was der Nutzer:in auf der Grundlage der Anweisungen und der Datenpunkte aus dem Kontext, die dem Agenten gegeben wurden, wünschen könnte. In diesem Beispiel könnte ein Agent eine neue Geschmacksrichtung empfehlen, wenn der Nutzer:innen verschiedene Geschmacksrichtungen ausprobieren möchte.
- **KI Artikel Empfehlungen:** Nutzt Modelle des maschinellen Lernens, um auf der Grundlage vergangener Nutzer:innen-Events, wie z.B. Käufen, die Produkte zu prognostizieren, die ein Nutzer mit hoher Wahrscheinlichkeit haben möchte. In diesem Beispiel würden die KI-Empfehlungen für Artikel eine Geschmacksrichtung (Vanille) vorschlagen, die auf den beiden vorangegangenen Bestellungen des Nutzers (Schokolade und Erdbeere) und dem Verhalten der anderen Nutzer:innen in Ihrem Workspace basiert.

### Wann sollte ich ein Standardausgabeformat für einen Agenten verwenden?

Wir empfehlen die Verwendung des Ausgabeformats, wenn Sie möchten, dass der Agent eine Datenstruktur mit mehreren strukturiert definierten Werten zurückgibt und nicht nur einen einzigen Wert ausgibt. Dies lässt zu, dass die Ausgabe besser als konsistente Kontextvariable formatiert wird.

Sie können zum Beispiel in einem Agenten ein Ausgabeformat verwenden, das auf der Grundlage eines von einem Nutzer:innen eingereichten Formulars eine Beispiel-Reiseroute erstellen soll. Über das Ausgabeformat können Sie festlegen, dass jede Agentenantwort mit Werten für `tripStartDate`, `tripEndDate` und `destination` zurückkommen soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und in einen Schritt der Nachricht zur Personalisierung mit Liquid eingefügt werden.

### Wie verwenden die Agentenschritte Eingabedaten?

Agentenschritte verwenden spezifische Kontextdaten, die [dem Agenten zur Verfügung gestellt](#step-4-decide-what-context-to-provide-the-agent) werden. 

Sie haben die Wahl, entweder den gesamten Canvas-Kontext als Kontext an den Agenten zu übergeben oder bestimmte Werte mithilfe von Liquid-Tags in den Kontext dieses Agenten-Schritts zu übertragen. Sie können Connected-Content auch als Eingabewert in einem Agent-Schritt verwenden.

## Ähnliche Artikel  

- [Braze Agents Übersicht]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  