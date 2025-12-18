---
nav_title: Agent
article_title: Agentenschritt
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie den Agent-Schritt in Canvas verwenden, um Inhalte zu generieren oder intelligente Entscheidungen in Echtzeit zu treffen."
tool: Canvas
---

# Agentenschritt  

> Mit dem Agent-Schritt können Sie KI-gestützte Entscheidungsfindung und Inhaltserstellung direkt in Ihren Canvas-Workflow integrieren. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Ein Agent-Schritt in einer Canvas Nutzer:innen-Reise.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

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

Die Ausgaben der Agenten werden als "Ausgabevariablen" bezeichnet und in einer [Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) gespeichert, um den Zugriff zu erleichtern. So definieren Sie die Ausgabevariable:

1. Geben Sie der Variable einen Namen.
2. Wählen Sie einen Datentyp aus. 

Die Ausgaben der Agenten können als Strings, Zahlen oder Boolesche Werte gespeichert werden. Dadurch sind sie sowohl für die Personalisierung von Texten als auch für die bedingte Logik in Ihrem Canvas flexibel. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Häufige Verwendungen |
| --- | --- |
| String | Personalisierung von Nachrichten (Betreffzeilen, Texte, Antworten) |
| Zahl | Scoring, Schwellenwerte, Routing in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolesch | Ja/Nein Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn sie definiert ist, können Sie eine Ausgabevariable im gesamten Canvas verwenden, indem Sie die gleiche Template-Syntax wie bei einer Kontextvariablen verwenden. Verwenden Sie entweder den Filter für **kontextvariable** Segmente oder das Template für Agentenantworten direkt mit Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

### Schritt 4: Entscheiden Sie, welchen Kontext Sie dem Agenten bieten möchten  

Sie müssen entscheiden, welche Daten der Agent zur Laufzeit erhalten soll. Die folgenden Optionen sind verfügbar:  

- **Alle Canvas-Kontexte einbeziehen:** Übergeben Sie alle verfügbaren Canvas-Kontextvariablen (wie z.B. [Eingangs-Eigenschaften von Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) und jeden anderen Kontext, der ihm über Kontext-Schritte zugewiesen wurde.  
- **Liefern Sie Werte:** Übergeben Sie nur ausgewählte Eigenschaften, wie z.B. den Vornamen oder die Lieblingsfarbe eines Nutzers:innen. Wählen Sie diese Option, um dem Agenten nur Zugriff auf die Werte zu geben, die Sie hier zuweisen. Geben Sie für jeden **Schlüssel** den [Liquid-Tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) ein, der das spezifische Feld des Nutzerprofils oder die Kontextvariable definiert.  

{% alert note %}
Braze gibt nur die ersten 10 KB des Inhalts an den Agenten weiter. Die Angabe von Werten, deren Gesamtwert mehr als 10 KB beträgt, führt zu einer Abschneidung. Um Kosten zu sparen, verwenden Braze-Agenten in Canvas kurzlebige Caches für LLM-Antworten auf identische Eingaben. Die Einbeziehung aller Canvas-Kontexte erhöht die Wahrscheinlichkeit, dass zwischengespeicherte Ergebnisse nicht verwendet werden können, was Ihre LLM-Kosten erhöhen könnte.
{% endalert %}

## Fehlerbehandlung  

- Wenn das verbundene Modell einen Rate-Limits-Fehler meldet, versucht Braze es bis zu fünf Mal mit exponentiellem Backoff.  
- Wenn der Agent aus einem anderen Grund fehlschlägt (z.B. ungültiger API-Schlüssel), wird die Ausgabevariable auf `null` gesetzt.  
- Antworten werden für identische Eingaben zwischengespeichert, um wiederholte Aufrufe zu vermeiden.  

## Analytics  

Anhand der folgenden Metriken können Sie das Tracking der Performance Ihrer Agentenschritte verfolgen:  

| Metrisch | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Nutzer:innen, die den Schritt Agent eingegeben haben. |
| _Fortgefahren mit nächstem Schritt_ | Die Anzahl der Nutzer:innen, die nach dem Schritt Agent zum nächsten Schritt im Ablauf übergegangen sind. |
| _Canvas wurde verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas verlassen haben, nachdem sie den Agenten-Schritt durchlaufen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ähnliche Artikel  

- [Braze Agents Übersicht]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Anpassen von Agenten]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Einsatz von Agenten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  