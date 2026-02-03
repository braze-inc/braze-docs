---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Datenverwaltung einsetzen können."
alias: /creating-agents/
---

# Angepasste Agenten erstellen

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Daten-Management einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Braze-Agenten befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

- Zugriff auf die **Agentenkonsole** in Ihrem Workspace. Wenden Sie sich an Ihre Braze-Administratoren, wenn Sie diese Option nicht sehen.  
- Berechtigung zum Erstellen und Bearbeiten angepasster KI-Agenten. 
- Eine Idee, was Sie mit dem Agenten bezwecken möchten. Braze Agents können die folgenden Aktionen unterstützen:  
   - **Messaging:** Generieren Sie Betreffzeilen, Überschriften, produktinterne Texte oder andere Inhalte.  
   - **Entscheidungsfindung:** Leiten Sie Nutzer:innen in Canvas auf der Grundlage von Verhalten, Vorlieben oder angepassten Attributen weiter.  
   - **Datenverwaltung:** Berechnen Sie Werte, reichern Sie Katalogeinträge an oder aktualisieren Sie Profilfelder.  

## Funktionsweise

Wenn Sie einen Agenten erstellen, definieren Sie seinen Zweck und setzen Leitplanken für sein Verhalten. Nach der Inbetriebnahme kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu erstellen, Entscheidungen in Echtzeit zu treffen oder Katalogfelder zu aktualisieren. Sie können einen Agenten jederzeit über das Dashboard pausieren oder aktualisieren.

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, wie Sie angepasste Agenten nutzen können.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Umgang mit Kunden:in | Geben Sie das Feedback der Nutzer:innen an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Nachrichten zu erstellen. Für hochwertige Nutzer:innen könnte der Agent die Antwort eskalieren oder Vergünstigungen anbieten. |
| Inhalte lokalisieren | Übersetzen Sie den Katalogtext für globale Kampagnen in eine andere Sprache, oder passen Sie Ton und Länge für regionalspezifische Kanäle an. Übersetzen Sie zum Beispiel "Classic Clubmaster Sonnenbrille" ins Spanische als "Gafas de sol Classic Clubmaster" oder kürzen Sie Beschreibungen für SMS Kampagnen. |
| Fassen Sie Bewertungen oder Feedback zusammen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, indem Sie z.B. Stimmungswerte wie Positiv, Neutral oder Negativ vergeben oder eine kurze Textzusammenfassung wie "Die meisten Kund:in erwähnen die gute Passform, bemängeln aber den langsamen Versand." erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einen Agenten erstellen

Um Ihren angepassten Agenten zu erstellen:  

1. Gehen Sie im Braze-Dashboard zu **Agentenkonsole** > **Agent Management**.  
2. Wählen Sie **Agent erstellen**.  
3. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team seinen Zweck versteht.
4. Wählen Sie das [Modell](#models), das Ihr Agent verwenden wird.  

![Schnittstelle der Agentenkonsole zur Erstellung eines angepassten Agenten in Braze. Der Bildschirm enthält Felder zur Eingabe des Agentennamens und der Beschreibung sowie zum Auswählen eines Modells.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Geben Sie dem Agenten Anweisungen. Lesen Sie dazu die [Anleitung zum Schreiben](#writing-instructions).
6\. [Testen Sie die](#testing-your-agent) Ausgabe des [Agenten](#testing-your-agent) und passen Sie die Anweisungen nach Bedarf an.
7\. Wenn Sie bereit sind, wählen Sie **Agent erstellen**, um den Agenten zu aktivieren. 

Ihr Agent ist jetzt einsatzbereit! Einzelheiten finden Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Modelle

Wenn Sie einen Agenten einrichten, können Sie das Modell wählen, das er zur Erzeugung von Antworten verwendet. Sie haben zwei Möglichkeiten: Sie können ein von Braze betriebenes Modell verwenden oder Ihren eigenen API-Schlüssel mitbringen.

{% alert important %}
Bei der Verwendung des von Braze betriebenen **Automodells** haben wir uns für Modelle entschieden, deren Denkvermögen ausreicht, um Aufgaben wie die Katalogsuche und die Segmentierung der Nutzer:innen zu erfüllen. Wenn Sie andere Modelle verwenden, empfehlen wir Ihnen zu testen, ob Ihr Modell für Ihren Anwendungsfall geeignet ist. Möglicherweise müssen Sie Ihre [Anleitungen](#writing-instructions) anpassen, um Modelle mit unterschiedlichen Geschwindigkeiten und Fähigkeiten unterschiedlich detailliert oder schrittweise anzuleiten.
{% endalert %}

### Option 1: Verwenden Sie ein Modell mit Braze-Antrieb

Dies ist die einfachste Option, für die keine zusätzlichen Einstellungen erforderlich sind. Braze bietet direkten Zugriff auf große Sprachmodelle (LLM). Um diese Option zu verwenden, wählen Sie **Auto**, das Gemini-Modelle verwendet.

### Option 2: Bringen Sie Ihren eigenen API-Schlüssel mit

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic, AWS Bedrock oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter mitbringen, werden die Token-Kosten direkt über Ihren Anbieter abgerechnet, nicht über Braze.

{% alert important %}
Wir empfehlen, routinemäßig die neuesten Modelle zu testen, da ältere Modelle möglicherweise nach einigen Monaten eingestellt werden oder veraltet sind.
{% endalert %}

So richten Sie dies ein:

1. Gehen Sie zu **Partnerintegrationen** > **Technologiepartner** und finden Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel des Anbieters ein.
3. Wählen Sie **Speichern**.

Dann können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, handeln die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze und unterliegen den Bedingungen des Zusatzes zur Datenverarbeitung (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel mitzubringen, wird der Anbieter Ihres LLM-Abos im Rahmen des Vertrags zwischen Ihnen und Braze als Drittanbieter betrachtet.  
{% endalert %}

## Anweisungen schreiben

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemabfrage). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 25 KB groß sein.

Hier sind einige allgemeine Best Practices, die Ihnen den Einstieg in das Prompting erleichtern:

1. Beginnen Sie mit dem Ziel vor Augen. Geben Sie zuerst das Ziel an.
2. Geben Sie dem Modell eine Rolle oder Persona ("Sie sind ein ...").
3. Legen Sie einen klaren Kontext und Einschränkungen fest (Zielgruppe, Länge, Ton, Format).
4. Fragen Sie nach der Struktur ("Geben Sie JSON/Bullet-Liste/Tabelle...").
5. Zeigen, nicht erzählen. Fügen Sie ein paar hochwertige Beispiele hinzu.
6. Unterteilen Sie komplexe Aufgaben in geordnete Schritte ("Schritt 1... Schritt 2...").
7. Ermutigen Sie zum Nachdenken ("Erst laut denken, dann antworten").
8. Pilotieren, prüfen und iterieren Sie. Kleine Optimierungen können zu großen Qualitätssteigerungen führen.
9. Kümmern Sie sich um die Randfälle, fügen Sie Leitplanken ein und fügen Sie Anweisungen zur Ablehnung hinzu.
10. Messen und dokumentieren Sie, was intern zur Wiederverwendung und Skalierung funktioniert.

Wir empfehlen auch einen Standard als Auffangantwort, wenn der Agent eine Antwort erhält, die nicht geparst werden kann. Diese Fehlerbehandlung ermöglicht es dem Agenten, Sie über eine unbekannte Ergebnisvariable zu informieren. Anstatt den Agenten beispielsweise nur nach "positiven" oder "negativen" Stimmungswerten zu fragen, bitten Sie ihn, "unsicher" zurückzugeben, wenn er sich nicht entscheiden kann.

### Einfache Eingabeaufforderung

Diese Beispiel-Eingabeaufforderung nimmt eine Umfrage als Input und gibt eine einfache Stimmungsanalyse aus:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Komplexe Eingabeaufforderung 

In diesem Beispiel wird eine Umfrage eines Nutzers:innen in ein einziges Sentiment-Label eingeordnet. Das Ergebnis kann dann verwendet werden, um Nutzer:innen auf verschiedene Canvas-Pfade zu leiten (z.B. positives oder negatives Feedback) oder die Stimmung als angepasstes Attribut in ihrem Profil für zukünftiges Targeting zu speichern.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}

Weitere Einzelheiten zu den besten Praktiken für Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropisch](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Zwillinge](https://support.google.com/a/users/answer/14200040?hl=en)

### Ausgabeformat

Verwenden Sie das Feld **Ausgabeformat**, um die Ausgabe des Agenten zu organisieren und zu definieren, indem Sie Felder manuell strukturieren oder JSON verwenden. 

- **Felder:** Ein Code-freier Weg, um eine Agentenausgabe zu erzwingen, die Sie konsistent verwenden können. 
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können.

#### Felder

Nehmen wir an, Sie möchten die Antworten auf eine einfache Umfrage formatieren, um festzustellen, wie wahrscheinlich es ist, dass die Befragten die neueste Eissorte Ihres Restaurants weiterempfehlen. Sie können die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert
| --- | --- |
| **likelihood_score** | Zahl |
| **Erklärung** | Text |
| **confidence_score** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agentenkonsole mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Vertrauenswert.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### JSON-Schema

Nehmen wir an, Sie möchten das Feedback der Nutzer:innen zu ihrem letzten Restaurantbesuch in Ihrer Restaurantkette sammeln. Sie könnten **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Sentiment-Variable und eine Argumentationsvariable enthält.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

Wenn Sie versuchen, einen Agenten mit einer JSON-Ausgabe in einem Katalog zu verwenden, wird er nicht Ihrem Schema folgen. Verwenden Sie stattdessen die [definierten Ausgabefelder](#fields).

{% alert important %}
Die Ausgabeformate werden derzeit von Claude KI nicht unterstützt. Wenn Sie einen Anthropic-Schlüssel verwenden, empfehlen wir, die Struktur manuell in die Eingabeaufforderung des Agenten einzufügen.
{% endalert %}

## Optionale Einstellungen

### Markenrichtlinien

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) auswählen, an die sich Ihr Agent bei seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Registrierung für eine Mitgliedschaft im Fitnessstudio zu ermutigen, können Sie in diesem Feld Ihre vordefinierte fettgedruckte, motivierende Richtlinie referenzieren.

### Kataloge

Wählen Sie spezifische Kataloge aus, auf die ein Agent referenzieren kann, und geben Sie Ihrem Agenten den Kontext, den er braucht, um Ihre Produkte und andere Nutzer:innen-Daten zu verstehen, wenn diese relevant sind.

![Der Katalog "Restaurants" und die Spalte "Loyalty_Program" wurden für die Suche des Agenten ausgewählt.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### Kontext der Segmentzugehörigkeit

Sie können bis zu drei Segmente auswählen, mit denen der Agent die Segmentzugehörigkeit jedes Nutzers:innen referenziert, wenn der Agent in einem Canvas verwendet wird. Nehmen wir an, Ihr Agent hat die Segmentzugehörigkeit für ein Segment "Treue Nutzer:innen" ausgewählt und der Agent wird in einem Canvas verwendet. Wenn Nutzer:innen einen Schritt des Agenten betreten, kann der Agent referenzieren, ob die einzelnen Nutzer:innen Mitglieder der einzelnen Segmente sind, die Sie in der Agentenkonsole angegeben haben, und die Mitgliedschaft (oder Nicht-Mitgliedschaft) der einzelnen Nutzer:innen als Kontext für die LLM verwenden.

![Das Segment "Nutzer:innen der Treue" wurde für den Zugriff auf die Agentenmitgliedschaft ausgewählt.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### Temperatur

Wenn Ihr Ziel darin besteht, mit Hilfe eines Agenten Texte zu erstellen, die Nutzer:innen dazu bewegen, sich in Ihre mobile App einzuloggen, können Sie eine höhere Temperatur für Ihren Agenten einstellen, um kreativer zu sein und die Nuancen der Kontextvariablen zu nutzen. Wenn Sie einen Agenten verwenden, um Stimmungswerte zu generieren, ist es vielleicht ideal, eine niedrigere Temperatur einzustellen, um zu vermeiden, dass der Agent auf negative Umfragen spekuliert. Wir empfehlen Ihnen, diese Einstellung zu testen und die vom Agenten generierte Ausgabe auf Ihr Szenario hin zu überprüfen.

{% alert note %}
Temperaturen werden derzeit nicht für die Verwendung mit OpenAI unterstützt.
{% endalert %}

## Ihren Agenten testen

Das **Live-Vorschau-Fenster** ist eine Instanz des Agenten, die in der Konfigurationsumgebung als Panel nebeneinander angezeigt wird. Damit können Sie den Agenten testen, während Sie ihn erstellen oder Updates vornehmen, um ihn ähnlich wie die Nutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass sich das System so verhält, wie Sie es erwarten, und gibt Ihnen die Möglichkeit zur Feinabstimmung, bevor es live geht.

![Agenten-Konsole mit dem Live-Vorschau-Fenster zum Testen eines angepassten Agenten. Die Schnittstelle zeigt ein Beispieleingabefeld mit beispielhaften Kundendaten, einen Button Test ausführen und einen Antwortbereich, in dem die Ausgabe des Agenten erscheint.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. In das Feld **Beispieleingaben** können Sie Beispieldaten oder Kunden:in eingeben - alles, was reale Szenarien widerspiegelt, die Ihr Agent bearbeiten wird. 
2. Wählen Sie **Test ausführen**. Der Agent wird auf der Grundlage Ihrer Konfiguration ausgeführt und zeigt seine Antwort an. Testläufe werden auf Ihr tägliches Ausführungslimit angerechnet.

Prüfen Sie die Ausgabe mit einem kritischen Auge. Überlegen Sie sich die folgenden Fragen:

- Ist der Text markengerecht? 
- Leitet die Entscheidungslogik die Kund:in wie vorgesehen weiter? 
- Sind die berechneten Werte korrekt? 

Wenn Sie das Gefühl haben, dass etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie einige verschiedene Eingaben durch, um zu sehen, wie sich der Agent an verschiedene Szenarien anpasst, insbesondere an Grenzfälle wie keine Daten oder ungültige Antworten.

### Überwachen Sie Ihren Agenten

Im Tab **Protokolle** Ihres Agenten können Sie die tatsächlichen Agentenaufrufe überwachen, die in Ihren Canvase und Katalogen erfolgen. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Misserfolg) oder dem Standort des Anrufers filtern.

![Protokolle für einen Agenten Random Sport Assignment, die enthalten, wann und wo der Agent aufgerufen wurde.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

Wählen Sie **Ansicht** für einen bestimmten Agentenaufruf, um die Eingabe, die Ausgabe und die Nutzer:innen zu sehen.

![Protokolle für einen Agenten Ort Trends und Empfehlung Buchen. Das Panel "Details" zeigt die Eingabeaufforderung, die Ausgabeantwort und die zugehörige Nutzer:in an.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
