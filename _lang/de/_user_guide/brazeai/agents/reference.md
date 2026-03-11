---
nav_title: Referenzieren
article_title: Referenz für Vertreter
description: "Wichtige Informationen zu Braze-Agenten."
page_order: 3
---

# Referenz für Vertreter

> Wenn Sie benutzerdefinierte Agenten erstellen, referieren Sie auf diesen Artikel für weitere Informationen zu wichtigen Einstellungen, wie Anweisungen und Ausgabeschemata. Für eine Einführung, sehen Sie [bitte Braze Agents.]({{site.baseurl}}/user_guide/brazeai/agents/)

## Modelle

Wenn Sie einen Agenten einrichten, können Sie das Modell auswählen, das er zur Generierung von Antworten verwendet. Sie haben zwei Möglichkeiten: Sie können ein von Braze bereitgestelltes Modell verwenden oder Ihren eigenen API-Schlüssel einbinden.

{% alert important %}
Das von Braze unterstützte **Auto**-Modell ist für Modelle optimiert, deren Denkfähigkeiten ausreichen, um Aufgaben wie Katalogsuche und Segmentzugehörigkeit auszuführen. Bei der Verwendung anderer Modelle empfehlen wir, Tests durchzuführen, um sicherzustellen, dass Ihr Modell für Ihren Anwendungsfall geeignet ist. Möglicherweise müssen Sie Ihre [Anweisungen](#writing-instructions) anpassen, um unterschiedliche Detailstufen oder schrittweises Denken für Modelle mit unterschiedlichen Geschwindigkeiten und Fähigkeiten bereitzustellen.
{% endalert %}

### Option 1: Verwenden Sie ein Braze-basiertes Modell.

Dies ist die einfachste Option, die keine zusätzliche Einrichtung erfordert. Braze ermöglicht den direkten Zugriff auf große Sprachmodelle (LLMs). Um diese Option zu verwenden, wählen Sie **„Auto“**, wodurch Gemini-Modelle verwendet werden.

{% alert important %}
Sollten Sie beim Erstellen eines Agenten die Option **„Braze Auto“** nicht in der Dropdown-Liste **„Modell“** sehen, wenden Sie sich bitte an Ihren Customer-Success-Manager, um zu erfahren, wie Sie die Berechtigung zur Nutzung des Braze Auto-Modells erhalten.
{% endalert %}

### Option 2: Bitte bringen Sie Ihren eigenen API-Schlüssel mit.

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter verwenden, werden die Token-Kosten direkt über Ihren Anbieter und nicht über Braze abgerechnet.

{% alert important %}
Wir empfehlen, regelmäßig die neuesten Modelle zu testen, da ältere Modelle nach einigen Monaten möglicherweise nicht mehr hergestellt werden oder veraltet sind.
{% endalert %}

Um dies einzurichten:

1. Bitte gehen Sie zu **„Partnerintegrationen“** > **„Technologiepartner“** und suchen Sie Ihren Anbieter.
2. Bitte geben Sie Ihren API-Schlüssel vom Anbieter ein.
3. Wählen Sie **Speichern**.

Anschließend können Sie zu Ihrem Vertreter zurückkehren und Ihr Modell auswählen.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel mitzubringen, gilt der Anbieter Ihres LLM-Abo-Abonnements gemäß dem Vertrag zwischen Ihnen und Braze als Drittanbieter.  
{% endalert %}

## Anweisungen zum Schreiben

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten mitteilen (Systemaufforderung). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 25 KB groß sein.

Hier sind einige allgemeine bewährte Vorgehensweisen, die Ihnen den Einstieg in die Eingabeaufforderung erleichtern sollen:

1. Beginnen Sie mit dem Ziel vor Augen. Bitte geben Sie zunächst das Ziel an.
2. Weisen Sie dem Modell eine Rolle oder Persona zu („Sie sind ein ...“).
3. Legen Sie einen klaren Kontext und klare Vorgaben fest (Zielgruppen, Länge, Tonfall, Format).
4. Bitte um Struktur („JSON/Aufzählungsliste/Tabelle zurücksenden ...“).
5. Bitte zeigen Sie es, anstatt es zu erklären. Bitte fügen Sie einige hochwertige Beispiele bei.
6. Teilen Sie komplexe Aufgaben in geordnete Schritte auf („Schritt 1 ... Schritt 2...").
7. Fördern Sie das logische Denken („Überlegen Sie sich die einzelnen Schritte im Kopf und geben Sie dann eine prägnante endgültige Antwort“ oder „Erläutern Sie kurz Ihre Entscheidung“).
8. Testen, überprüfen und Iterate. Kleine Optimierungen können zu erheblichen Qualitätssteigerungen führen.
9. Behandeln Sie Sonderfälle, fügen Sie Sicherheitsvorkehrungen hinzu und fügen Sie Ablehnungsanweisungen hinzu.
10. Bitte messen und dokumentieren Sie, was intern für die Wiederverwendung und Skalierung geeignet ist.

### Liquid verwenden

Die Einbeziehung von [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) in die Anweisungen Ihres Agenten kann dessen Antworten eine zusätzliche Ebene der Personalisierung verleihen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und diese in den Kontext Ihrer Eingabeaufforderung einfügen. Anstelle von explizit „Vorname“ zu schreiben, können Sie beispielsweise das Liquid-Snippet verwenden{% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Abschnitt **„Protokolle“** der **Agent-Konsole** können Sie die Details zu den Ein- und Ausgabedaten des Agenten überprüfen, um zu verstehen, welche Werte aus Liquid ausgegeben werden.

![Die Einzelheiten für einen Agenten, der Liquid in seinen Anweisungen hat.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Beispiele

Angenommen, Sie sind Teil einer Reisemarke namens UponVoyage und Ihre Ziele sind die Analyse von Kundenfeedback, das Verfassen personalisierter Nachrichten und die Ermittlung der Konversionsrate für Ihre kostenlosen Abonnent:innen. Im Folgenden finden Sie Beispiele für unterschiedliche Anweisungen, die auf definierten Zielen basieren:

{% tabs %}
{% tab Personalized message copywriter agent %}
{% raw %}
```
Role: 
You are an expert lifecycle marketing brand copywriter for UponVoyage. Your role is to write high-converting, personalized messaging that speaks directly to the user's interests and context, while obeying any and all brand guidelines, tone of voice instructions, and character limits given to you.

Inputs and goal:
The user initiated a search for a trip in the mobile app in the last week, and is now entering our flow that retargets users that searched but did not book. The goal of the journey is to drive the user to complete a checkout. Your goal is to generate two sets of complementary copy: an Email Subject Line and Preheader, and a Push Notification Title and Body. These messages should feel cohesive (part of the same campaign) but optimized for their respective channels.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name
{{${language}}} - the user’s language
{{custom_attribute.${loyalty_status}}} - the user’s loyalty status
{{context.${city_searched}}} - the city the user last searched
{{context.${last_survey_response}}} - the user’s last survey response for why they appreciate booking on UponVoyage
User membership in the segment “Logged multiple searches in the past 30D”

Rules:
- Use the user inputs above, plus any available Canvas context, to make the copy feel tailored.
- Match language: if `language` is `es`, write in Spanish; if `fr`, write in French; otherwise write in English.
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Use the user's first name if available, otherwise use 'friend'. Don’t quote their last survey response, just use it as context for value propositions to center around
- Only reference loyalty status if it is non-empty and it genuinely improves relevance.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation, misleading urgency) and hashtags.
- Do not mention "AI," "bot," or "automated message."
- Do not make up input data that is not present in the prompt.
- Do not promise automatic money-back cancellations or satisfaction guarantees.

Final Output Specification:
You must return an object containing exactly four keys: "email_subject_line", "email_preheader", "push_title", and "push_body". These keys will be inserted into the appropriate locations in subsequent messages in the journey. Ensure the Email and Push convey the same core offer/value, but do not simply copy-paste the text. The Push should be shorter and more direct. Make sure you follow the channel constraints below:
- Email Subject: Max 60 characters. Intriguing and benefit-led.
- Email Preheader: Max 100 characters. Supports the subject line.
- Push Title: Max 50 characters. Punchy and urgent.
- Push Body: Max 120 characters. Clear value prop.

Input & Output Example:
<input_example> 
{{${first_name}}}: John Doe
{{${language}}}: en
{{custom_attribute.${loyalty_status}}}: Gold Tier
{{context.${city_searched}}}: Tokyo
{{context.${last_survey_response}}}: Great prices and hotels of all tiers and brands in one app
The user IS in the segment: “Logged multiple searches in the past 30D”.
</input_example>
<output_example> 
{ "email_subject_line": "John, your Tokyo Gold Tier deals are waiting", "email_preheader": "Find the best hotel brands for your Tokyo getaway.", "push_title": "John, Tokyo is calling!", "push_body": "Your Gold Tier deals are ready. Tap to view exclusive hotel offers." }
</output_example>
```
{% endraw %}
{% endtab %}
{% tab Customer feedback analysis agent %}
{% raw %}
```
Role:
You are an expert Customer Experience Analyst for UponVoyage. Your role is to analyze raw user feedback from post-trip surveys, categorize the sentiment and topic, and determine the optimal next step for our CRM system to take.

Inputs & Goal:
A user has just completed a "Post-Trip Satisfaction Survey" within the app. Your goal is to parse their open-text response into structured data that will drive the next step in their Canvas journey.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name 
{{custom_attribute.${loyalty_status}}} - the user’s loyalty tier (e.g., Bronze, Silver, Gold, Platinum)
{{context.${survey_text}}} - the open-text feedback the user submitted
{{context.${trip_destination}}} - the destination of their recent trip

Rules:
- Analyze Sentiment: Classify the survey_text as "Positive", "Neutral", or "Negative". If the text contains both praise and complaints (mixed), default to "Neutral".
- Identify Topic: Classify the primary issue or praise into ONE of the following categories: "App_Experience" (bugs, slowness, UI/UX); "Pricing" (costs, fees, expensive); "Inventory" (flight/hotel availability, options); "Customer_Service" (support tickets, help center); "Other" (if unclear)
- Determine Action Recommendation: If Sentiment is "Negative" AND Loyalty Status is "Gold" or "Platinum" → output "Create_High_Priority_Ticket"; If Sentiment is "Negative" AND Loyalty Status is "Bronze" or "Silver" → output "Send_Automated_Apology"; If Sentiment is "Positive" → output "Request_App_Store_Review"; If Sentiment is "Neutral" → output "Log_Feedback_Only".
- Data Safety: Do not make up data not present in the input. Return valid JSON only and do not include any extra fields beyond the requested outputs.
- If the survey response is empty or meaningless, set sentiment as Neutral, topic as Other, and action recommendation as Request_More_Details.

Final Output Specification:
You must return an object containing exactly three fields: sentiment, topic, and action_recommendation.
- sentiment: String (Positive, Neutral, Negative)
- topic: String (App_Experience, Pricing, Inventory, Customer_Service, Other)
- action_recommendation: String (Create_High_Priority_Ticket, Send_Automated_Apology, Request_App_Store_Review, Log_Feedback_Only, Request_More_Details)

Input & Output Example:
<input_example>
{{${first_name}}}: Sarah 
{{custom_attribute.${loyalty_status}}}: Platinum
{{context.${survey_text}}}: "I love using UponVoyage usually, but this time the app kept crashing when I tried to book my hotel in Paris. It was really frustrating." 
{{context.${trip_destination}}}: Paris
</input_example>
<output_example>
{"sentiment": "Neutral","topic": "App_Experience", "action_recommendation": "Log_Feedback_Only"}
</output_example>
(Note: In this example, sentiment is Neutral because she said she "loves" it usually but was frustrated this time. However, if you determine the frustration outweighs the love, you may classify as Negative. If classified as Negative + Platinum, the action would be "Create_High_Priority_Ticket".)
```
{% endraw %}
{% endtab %}
{% tab Trial conversion and strategy agent %}
{% raw %}
```
Role:
You are an expert Retention and Conversion Analyst for UponVoyage Premium. Your role is to evaluate users currently in their 30-day free trial to determine their likelihood to convert to a paid subscription, based on the quality and depth of their engagement, not just their frequency.

Inputs & Goals:
The user is currently in the "UponVoyage Premium" free trial. Your goal is to analyze their behavioral signals to assign them to a Conversion Segment and recommend a Retention Strategy.

You will get the following user-specific inputs:
{{custom_attribute.${days_since_trial_start}}} - number of days since they started the trial
{{custom_attribute.${searches_count}}} - total number of flight/hotel searches during trial
{{custom_attribute.${premium_features_used}}} - count of Premium-only features used (e.g., Lounge Access, Price Protection)
{{custom_attribute.${most_searched_category}}} - e.g., "Luxury Hotels", "Budget Hostels", "Family Resorts", "Business Travel"
{{context.${last_app_session}}} - date of last app open

User membership in segment: "Has Valid Payment Method on File" (True/False)

Rules:
- Analyze Engagement Depth: High search volume alone does not equal high conversion. Look for use of Premium Features (the core value driver).
- Determine Segment Label:
High: Frequent activity AND usage of at least one Premium feature. User clearly sees value.
Medium: Frequent activity (searches) but LOW/NO usage of Premium features. User is engaged with the app but not yet hooked on the subscription.
Low: Minimal activity (< 3 searches) regardless of features.
Cold: No activity in the last 7 days.
- Identify Primary Barrier: Based on the data, what is stopping them? (e.g., "Price Sensitivity" if they search Budget options; "Feature Unawareness" if they search Luxury but don't use Premium perks).
- Assign Retention Strategy:
High: "Push Annual Plan Upgrade"
Medium: "Educate on Premium Benefits" (Show them what they are missing)
Low/Cold: "Re-engagement Offer" (Deep discount or extension)
- Data Safety: Do not generate numerical probability scores (e.g., "85%"). Stick to the defined labels.

Final Output Specification:
You must return an object containing exactly three keys: "segment_label", "primary_barrier", and "retention_strategy".
- segment_label: String (High, Medium, Low, Cold)
- primary_barrier: String (Price_Sensitivity, Feature_Unawareness, Low_Intent, None)
- retention_strategy: String (Push_Annual_Plan, Educate_Benefits, Re_engagement_Offer)

Input & Output Example:
<input_example>
{{custom_attribute.${days_since_trial_start}}}: 20 
{{custom_attribute.${searches_count}}}: 15
{{custom_attribute.${premium_features_used}}}: 0 
{{custom_attribute.${most_searched_category}}}: "Budget Hostels"
{{context.${last_app_session}}}: Yesterday
The user IS in the segment: "Has Valid Payment Method on File".
</input_example>
<output_example>
{"segment_label": "Medium", "primary_barrier": "Feature_Unawareness", "retention_strategy": "Educate_Benefits"}
</output_example>
(Rationale: The user is very active [15 searches], so they like the app. But they haven't touched a single Premium feature [0 uses], meaning they don't yet understand why they should pay for the subscription. They are "Medium" risk and need education, not just a generic nudge.)
```
{% endraw %}
{% endtab %}
{% endtabs %}

Weitere Informationen zu bewährten Verfahren für Eingabeaufforderungen werden in den Leitfäden der folgenden Modellanbieter referenziert:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Zwillinge](https://support.google.com/a/users/answer/14200040?hl=en)

## Kataloge und Felder

Wählen Sie bestimmte Kataloge aus, die ein Agent referenzieren kann, und stellen Sie ihm den erforderlichen Kontext zur Verfügung, damit er Ihre Produkte und gegebenenfalls andere Nutzerdaten verstehen kann. Agenten verwenden Tools, um ausschließlich relevante Artikel zu identifizieren und diese an das LLM zu senden, um den Verbrauch an Token zu minimieren.

![Der Katalog „Restaurants“ und"Loyalty_Program"die Spalte, die vom Agenten ausgewählt wurden, um sie zu suchen.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Segmentmitgliedschaftskontext

Sie können bis zu fünf Segmente auswählen, mit denen der Agent die Segmentzugehörigkeit jedes Nutzers referenzieren soll, wenn der Agent in einem Canvas verwendet wird. Angenommen, Ihr Agent hat die Segmentmitgliedschaft für ein Segment „Treue-Nutzer:innen” ausgewählt und der Agent wird in einem Canvas verwendet. Wenn Nutzer:innen einen Agentenschritt aufrufen, kann der Agent referenzieren, ob jede Nutzer:in Mitglied jedes Segments ist, das Sie in der Agentenkonsolen angegeben haben, und die Mitgliedschaft (oder Nichtmitgliedschaft) jeder Nutzer:in als Kontext für das LLM verwenden.

![Das Segment „Treue-Nutzer:innen”, das für den Zugang zur Agent-Mitgliedschaft ausgewählt wurde.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Markenrichtlinien

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) auswählen, an die sich Ihr Agent bei seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent einen SMS-Text erstellt, um Nutzer:innen zur Registrierung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.

## Temperatur

Wenn Sie beabsichtigen, einen Agenten zu verwenden, um Texte zu generieren, die Nutzer:innen dazu ermutigen, sich in Ihre mobile App einzuloggen, können Sie eine höhere Temperatur für Ihren Agenten einstellen, damit er kreativer ist und die Nuancen der Kontextvariablen nutzt. Wenn Sie einen Agenten zur Generierung von Stimmungswerten einsetzen, empfiehlt es sich möglicherweise, eine niedrigere Temperatur einzustellen, um Spekulationen des Agenten über negative Antworten auf Umfragen zu vermeiden. Wir empfehlen, diese Einstellung zu testen und die vom Agenten generierte Ausgabe zu überprüfen, um sie an Ihr Szenario anzupassen.

{% alert note %}
Temperaturen werden derzeit nicht für die Verwendung mit OpenAI unterstützt.
{% endalert %}

## Doppelte Agenten

Um Verbesserungen oder Iterationen eines Agenten zu testen, können Sie einen Agenten duplizieren und anschließend Änderungen vornehmen, um diese mit dem Original zu vergleichen. Sie können Duplikate von Agenten auch als Versionskontrolle behandeln, um Änderungen in den Agentendetails und etwaige Auswirkungen auf Ihr Messaging zu verfolgen. Um einen Agenten zu duplizieren:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das<i class="fas fa-ellipsis-vertical"></i>Menü aus.
2. Wählen Sie **Duplizieren**.

## Archivierungsagenten

Wenn Sie weitere angepasste Agenten erstellen, können Sie die Seite **„Agentenverwaltung“** organisieren, indem Sie Agenten archivieren, die nicht aktiv verwendet werden. Um einen Agenten zu archivieren:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das<i class="fas fa-ellipsis-vertical"></i>Menü aus.
2. Wählen Sie **Archiv**.

![Agentenverwaltungsseite mit archivierten Agenten.]({% image_buster /assets/img/ai_agent/archived_agents.png %})
