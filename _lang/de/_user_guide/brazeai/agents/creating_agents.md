---
nav_title: Agenten erstellen
article_title: Anpassen von Agenten
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Datenverwaltung einsetzen können."
alias: /creating-agents/
---

# Anpassen von Agenten

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Daten-Management einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Braze Agents befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
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

## Einen Agenten erstellen

Um Ihren angepassten Agenten zu erstellen:  

1. Gehen Sie im Braze-Dashboard zu **Agentenkonsole** > **Agent Management**.  
2. Wählen Sie **Agent erstellen**.  
3. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team seinen Zweck versteht.  
4. Wählen Sie das [Modell](#models), das Ihr Agent verwenden wird.  

![Schnittstelle der Agentenkonsole zur Erstellung eines angepassten Agenten in Braze. Der Bildschirm enthält Felder zur Eingabe des Agentennamens und der Beschreibung sowie zum Auswählen eines Modells.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. Geben Sie dem Agenten Anweisungen. Lesen Sie dazu die [Anleitung zum Schreiben](#writing-instructions).
6. [Testen Sie die](#testing-your-agent) Ausgabe des [Agenten](#testing-your-agent) und passen Sie die Anweisungen nach Bedarf an.
7. Wenn Sie bereit sind, wählen Sie **Agent erstellen**, um den Agenten zu aktivieren. 

## Nächster Schritt

Ihr Agent ist jetzt einsatzbereit! Weitere Informationen finden Sie unter [Einsetzen von Agenten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Referenzieren

### Modelle

Wenn Sie einen Agenten einrichten, wählen Sie das Modell aus, das er zur Generierung von Antworten verwendet. Sie haben zwei Möglichkeiten:

#### Option 1: Verwenden Sie ein Modell mit Braze-Antrieb

Dies ist die einfachste Option, für die keine zusätzlichen Einstellungen erforderlich sind. Braze bietet direkten Zugriff auf große Sprachmodelle (LLM). Um diese Option zu verwenden, wählen Sie **Auto**.

{% alert note %}
Wenn Sie den leistungsstarken LLM verwenden, entstehen Ihnen während der Beta-Phase keine Kosten. Der Aufruf ist auf 50.000 Durchläufe pro Tag und 500.000 Durchläufe insgesamt begrenzt. Siehe [Einschränkungen]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) für Details.
{% endalert %}

#### Option 2: Bringen Sie Ihren eigenen API-Schlüssel mit

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic, AWS Bedrock oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter mitbringen, werden die Kosten direkt über Ihren Anbieter abgerechnet, nicht über Braze.

So richten Sie dies ein:
1. Gehen Sie zu **Partnerintegrationen** > **Technologiepartner** und finden Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel des Anbieters ein.
3. Wählen Sie **Speichern**.

Dann können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

### Anweisungen schreiben

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemabfrage). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 10 KB groß sein.

{% tabs %}
{% tab Best practices %}

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

Weitere Einzelheiten zu den besten Praktiken für Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropisch](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Zwillinge](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

Diese Beispiel-Eingabeaufforderung nimmt eine Umfrage als Input und gibt eine einfache Stimmungsanalyse aus:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

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
{% enddetails %}

{% endtab %}
{% endtabs %}


#### Testen Sie Ihren Agenten  

Das **Live-Vorschau-Fenster** ist eine Instanz des Agenten, die in der Konfigurationsumgebung als Panel nebeneinander angezeigt wird. Damit können Sie den Agenten testen, während Sie ihn erstellen oder Updates vornehmen, um ihn ähnlich wie die Nutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass sich das System so verhält, wie Sie es erwarten, und gibt Ihnen die Möglichkeit, Feinabstimmungen vorzunehmen, bevor es live geht.

![Agentenkonsole mit dem Live-Vorschaufenster zum Testen eines angepassten Agenten. Die Schnittstelle zeigt ein Beispieleingabefeld mit beispielhaften Kundendaten, einen Button Test ausführen und einen Antwortbereich, in dem die Ausgabe des Agenten erscheint.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. In das Feld **Beispieleingaben** können Sie Beispieldaten oder Kunden:in eingeben - alles, was reale Szenarien widerspiegelt, die Ihr Agent bearbeiten wird. 
2. Wählen Sie **Test ausführen**. Der Agent wird auf der Grundlage Ihrer Konfiguration ausgeführt und zeigt seine Antwort an. Testläufe werden auf Ihr Tages- und Gesamtaufruflimit angerechnet.

Prüfen Sie die Ausgabe mit einem kritischen Auge. Überlegen Sie sich die folgenden Fragen:

- Ist der Text markengerecht? 
- Leitet die Entscheidungslogik die Kund:in wie vorgesehen weiter? 
- Sind die berechneten Werte korrekt? 

Wenn Sie das Gefühl haben, dass etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie einige verschiedene Eingaben durch, um zu sehen, wie sich der Agent an verschiedene Szenarien anpasst, insbesondere an Grenzfälle wie keine Daten oder ungültige Antworten.

