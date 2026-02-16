---
nav_title: Referenzieren
article_title: Agenten referenzieren
description: "Referenzieren Sie wichtige Details über Braze-Agenten."
page_order: 3
---

# Agenten referenzieren

> Wenn Sie angepasste Agenten erstellen, finden Sie in diesem Artikel weitere Informationen zu den wichtigsten Einstellungen, wie Anweisungen und Ausgabeschemata. Eine Einführung finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/).

{% alert important %}
Braze-Agenten befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Modelle

Wenn Sie einen Agenten einrichten, können Sie das Modell auswählen, das er zur Erzeugung von Antworten verwendet. Sie haben zwei Möglichkeiten: Sie können ein von Braze betriebenes Modell verwenden oder Ihren eigenen API-Schlüssel mitbringen.

{% alert important %}
Das von Braze betriebene **Automodell** ist für Modelle optimiert, deren Denkvermögen ausreicht, um Aufgaben wie Katalogsuche und Segmentierung der Nutzer:innen zu erfüllen. Wenn Sie andere Modelle verwenden, empfehlen wir Ihnen zu testen, ob Ihr Modell für Ihren Anwendungsfall geeignet ist. Möglicherweise müssen Sie Ihre [Anleitungen](#writing-instructions) anpassen, um Modelle mit unterschiedlichen Geschwindigkeiten und Fähigkeiten unterschiedlich detailliert oder schrittweise anzuleiten.
{% endalert %}

### Option 1: Verwenden Sie ein Modell mit Braze-Antrieb

Dies ist die einfachste Option, für die keine zusätzlichen Einstellungen erforderlich sind. Braze bietet direkten Zugriff auf große Sprachmodelle (LLM). Um diese Option zu verwenden, wählen Sie **Auto**, das Gemini-Modelle verwendet.

### Option 2: Bringen Sie Ihren eigenen API-Schlüssel mit

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic, AWS Bedrock oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter mitbringen, werden die Token-Kosten direkt über Ihren Anbieter und nicht über Braze abgerechnet.

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

Hier finden Sie einige allgemeine Best Practices, die Ihnen den Einstieg in das Prompting erleichtern:

1. Beginnen Sie mit dem Ziel vor Augen. Geben Sie zuerst das Ziel an.
2. Geben Sie dem Modell eine Rolle oder Persona ("Sie sind ein ...").
3. Legen Sie einen klaren Kontext und Einschränkungen fest (Zielgruppe, Länge, Ton, Format).
4. Fragen Sie nach der Struktur ("Geben Sie JSON/Bullet-Liste/Tabelle...").
5. Zeigen, nicht erzählen. Fügen Sie ein paar hochwertige Beispiele hinzu.
6. Unterteilen Sie komplexe Aufgaben in geordnete Schritte ("Schritt 1... Schritt 2...").
7. Ermutigen Sie zur Argumentation ("Denken Sie die Schritte intern durch und geben Sie dann eine prägnante endgültige Antwort" oder "Begründen Sie kurz Ihre Entscheidung").
8. Pilotieren, prüfen und iterieren Sie. Kleine Optimierungen können zu großen Qualitätssteigerungen führen.
9. Kümmern Sie sich um die Randfälle, fügen Sie Leitplanken ein und fügen Sie Anweisungen zur Ablehnung hinzu.
10. Messen und dokumentieren Sie, was intern zur Wiederverwendung und Skalierung funktioniert.

Wir empfehlen auch einen Standard als Auffangantwort, wenn der Agent eine Antwort erhält, die nicht geparst werden kann. Diese Fehlerbehandlung ermöglicht es dem Agenten, Sie über eine unbekannte Ergebnisvariable zu informieren. Anstatt den Agenten beispielsweise nur nach "positiven" oder "negativen" Stimmungswerten zu fragen, bitten Sie ihn, "unsicher" zurückzugeben, wenn er sich nicht entscheiden kann.

### Einfache Eingabeaufforderung

Diese Beispiel-Eingabeaufforderung nimmt eine Umfrage als Input und gibt eine einfache Stimmungsanalyse aus:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
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

### Liquid verwenden

Wenn Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) in die Anweisungen Ihres Agenten einbeziehen, können Sie eine zusätzliche Ebene der Personalisierung seiner Antwort hinzufügen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und sie in den Kontext Ihrer Eingabeaufforderung einbeziehen. Anstatt beispielsweise explizit "Vorname" zu schreiben, können Sie das Liquid Snippet {% raw %}`{{${first_name}}}`{% endraw %} verwenden:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Bereich **Protokolle** der **Agentenkonsole** können Sie die Details zu den Ein- und Ausgaben des Agenten einsehen, um zu verstehen, welcher Wert vom Liquid wiedergegeben wird.

![Die Angaben zu einem Mittel, das Liquid in seinen Anweisungen hat.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## Kataloge und Felder

Wählen Sie spezifische Kataloge aus, auf die ein Agent referenzieren kann, und geben Sie Ihrem Agenten den Kontext, den er braucht, um Ihre Produkte und andere Nutzer:innen-Daten zu verstehen, wenn diese relevant sind. Agenten verwenden Tools, um nur die relevanten Artikel zu finden und diese an den LLM zu senden, um die Verwendung von Token zu minimieren.

![Der Katalog "Restaurants" und die Spalte "Loyalty_Program" wurden für die Suche des Agenten ausgewählt.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## Kontext der Segmentzugehörigkeit

Sie können bis zu drei Segmente auswählen, mit denen der Agent die Segmentzugehörigkeit jedes Nutzers:innen referenziert, wenn der Agent in einem Canvas verwendet wird. Nehmen wir an, Ihr Agent hat die Segmentzugehörigkeit für ein Segment "Treue Nutzer:innen" ausgewählt und der Agent wird in einem Canvas verwendet. Wenn Nutzer:innen einen Schritt des Agenten betreten, kann der Agent referenzieren, ob die einzelnen Nutzer:innen Mitglieder der einzelnen Segmente sind, die Sie in der Agentenkonsole angegeben haben, und die Mitgliedschaft (oder Nicht-Mitgliedschaft) der einzelnen Nutzer:innen als Kontext für die LLM verwenden.

![Das Segment "Nutzer:innen der Treue" wurde für den Zugriff auf die Agentenmitgliedschaft ausgewählt.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## Markenrichtlinien

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) auswählen, an die sich Ihr Agent bei seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Registrierung für eine Mitgliedschaft im Fitnessstudio zu ermutigen, können Sie in diesem Feld Ihre vordefinierte fettgedruckte, motivierende Richtlinie referenzieren.

## Temperatur

Wenn Ihr Ziel darin besteht, mit Hilfe eines Agenten Texte zu erstellen, die Nutzer:innen dazu bewegen, sich in Ihre mobile App einzuloggen, können Sie eine höhere Temperatur für Ihren Agenten einstellen, um kreativer zu sein und die Nuancen der Kontextvariablen zu nutzen. Wenn Sie einen Agenten verwenden, um Stimmungswerte zu generieren, ist es vielleicht ideal, eine niedrigere Temperatur einzustellen, um zu vermeiden, dass der Agent auf negative Umfragen spekuliert. Wir empfehlen Ihnen, diese Einstellung zu testen und die vom Agenten generierte Ausgabe auf Ihr Szenario abzustimmen.

{% alert note %}
Temperaturen werden derzeit nicht für die Verwendung mit OpenAI unterstützt.
{% endalert %}