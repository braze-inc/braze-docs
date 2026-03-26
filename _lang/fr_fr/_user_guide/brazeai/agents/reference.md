---
nav_title: Article de référence
article_title: Référence des agents
description: "Retrouvez les détails clés sur les agents de Braze."
page_order: 3
---

# Référence des agents

> Lorsque vous créez des agents personnalisés, reportez-vous à cet article pour en savoir plus sur les paramètres clés, tels que les instructions et les schémas de sortie. Pour une introduction, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Modèles

Lorsque vous configurez un agent, vous pouvez choisir le modèle qu'il utilise pour générer des réponses. Deux possibilités s'offrent à vous : utiliser un modèle fourni par Braze ou apporter votre propre clé API.

{% alert important %}
Le modèle **Auto** fourni par Braze est optimisé pour les modèles dont les capacités de raisonnement sont suffisantes pour effectuer des tâches telles que la recherche dans un catalogue et la vérification d'appartenance à un segment. Si vous utilisez d'autres modèles, nous vous recommandons de les tester pour confirmer qu'ils sont adaptés à votre cas d'utilisation. Vous devrez peut-être ajuster vos [instructions](#writing-instructions) pour fournir différents niveaux de détails ou de raisonnement étape par étape selon la vitesse et les capacités du modèle choisi.
{% endalert %}

### Option 1 : Utiliser un modèle fourni par Braze

C'est l'option la plus simple : aucune configuration supplémentaire n'est nécessaire. Braze donne accès directement à des grands modèles de langage (LLM). Pour utiliser cette option, sélectionnez **Auto**, qui s'appuie sur les modèles Gemini.

{% alert important %}
Si vous ne voyez pas **Braze Auto** dans le menu déroulant **Modèle** lors de la création d'un agent, contactez votre Customer Success Manager pour savoir comment devenir éligible à l'utilisation du modèle Braze Auto.
{% endalert %}

### Option 2 : Apporter votre propre clé API

Cette option vous permet de connecter votre compte Braze à des fournisseurs tels qu'OpenAI, Anthropic ou Google Gemini. Si vous apportez votre propre clé API d'un fournisseur de LLM, les coûts liés aux jetons sont facturés directement par votre fournisseur, et non par Braze.

Nous vous recommandons de tester régulièrement les modèles les plus récents, car les anciens modèles peuvent être abandonnés ou rendus obsolètes au bout de quelques mois.

Pour configurer cette option :

1. Allez dans **Intégrations partenaires** > **Partenaires technologiques** et trouvez votre fournisseur.
2. Saisissez votre clé API fournie par le fournisseur.
3. Sélectionnez **Enregistrer**.

Vous pouvez ensuite retourner à votre agent et sélectionner votre modèle.

Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants secondaires de Braze, conformément aux conditions de l'addendum relatif au traitement des données (DPA) conclu entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.

#### Niveaux de réflexion

Certains fournisseurs de LLM vous permettent d'ajuster le niveau de réflexion d'un modèle sélectionné. Les niveaux de réflexion définissent l'étendue du raisonnement que le modèle effectue avant de répondre, allant de réponses rapides et directes à des chaînes de raisonnement plus longues. Cela affecte la qualité des réponses, la latence et la consommation de jetons.

| Niveau | Quand l'utiliser |
|--------|-----------------|
| **Minimal** | Tâches simples et bien définies (comme la recherche dans un catalogue ou la classification directe). Réponses les plus rapides et coût le plus bas. |
| **Faible** | Tâches qui bénéficient d'un peu plus de raisonnement sans nécessiter d'analyse approfondie. |
| **Moyen** | Tâches à plusieurs étapes ou nuancées (comme l'analyse de plusieurs entrées pour recommander une action). |
| **Élevé** | Raisonnement complexe, cas particuliers, ou situations où le modèle doit réfléchir aux étapes avant de répondre. |

Nous vous recommandons de commencer par **Minimal** et de tester les réponses de votre agent. Vous pouvez ensuite passer au niveau **Faible** ou **Moyen** si l'agent a du mal à fournir des réponses précises. Dans de rares cas, un niveau **Élevé** peut être nécessaire, mais sachez que ce niveau peut entraîner des coûts de jetons élevés, des temps de réponse plus longs ou un risque accru d'erreurs de délai d'attente. Si votre agent peine à concilier un raisonnement à plusieurs étapes avec des temps de réponse raisonnables, envisagez de diviser votre cas d'utilisation en plusieurs agents capables de collaborer dans un Canvas ou un catalogue.

Braze utilise les mêmes plages d'adresses IP pour les appels LLM sortants que pour le contenu connecté. Ces plages sont répertoriées dans la [liste d'autorisation IP du contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#connected-content-ip-allowlisting). Si votre fournisseur prend en charge la liste d'autorisation IP, vous pouvez restreindre la clé à ces plages afin que seul Braze puisse l'utiliser.

{% alert important %}
Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants secondaires de Braze, conformément aux conditions de l'addendum relatif au traitement des données (DPA) conclu entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.  
{% endalert %}

## Rédaction des instructions

Les instructions sont les règles ou directives que vous donnez à l'agent (prompt système). Elles définissent le comportement de l'agent à chaque exécution. Les instructions système peuvent contenir jusqu'à 25 Ko.

Voici quelques bonnes pratiques générales pour vous aider à démarrer avec la rédaction de prompts :

1. Commencez par la fin. Énoncez d'abord l'objectif.
2. Donnez au modèle un rôle ou un personnage (« Vous êtes un ... »).
3. Définissez clairement le contexte et les contraintes (audience, longueur, ton, format).
4. Demandez une structure (« Retournez du JSON/une liste à puces/un tableau... »).
5. Montrez plutôt que de décrire. Incluez quelques exemples de qualité.
6. Décomposez les tâches complexes en étapes ordonnées (« Étape 1... Étape 2... »).
7. Encouragez le raisonnement (« Réfléchissez en interne aux différentes étapes, puis donnez une réponse finale concise » ou « expliquez brièvement votre décision »).
8. Testez, inspectez et itérez. De petits ajustements peuvent produire des gains de qualité importants.
9. Traitez les cas particuliers, ajoutez des garde-fous et des instructions de refus.
10. Mesurez et documentez ce qui fonctionne en interne pour faciliter la réutilisation et la montée en charge.

### Utilisation de Liquid

Inclure du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) dans les instructions de votre agent permet d'ajouter une couche supplémentaire de personnalisation à ses réponses. Vous pouvez spécifier la variable Liquid exacte que l'agent reçoit et l'intégrer dans le contexte de votre prompt. Par exemple, au lieu d'écrire explicitement « prénom », vous pouvez utiliser l'extrait de code Liquid {% raw %}`{{${first_name}}}`{% endraw %} :

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Dans la section **Journaux** de la **Console de l'agent**, vous pouvez examiner les détails des entrées et sorties de l'agent pour comprendre quelle valeur est rendue par Liquid.

![Détails d'un agent qui utilise Liquid dans ses instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Exemples d'agents Canvas

Imaginons que vous faites partie d'une marque de voyage, UponVoyage, et que vos objectifs sont d'analyser les retours clients, de rédiger des messages personnalisés et de déterminer le taux de conversion de vos utilisateurs abonnés gratuits. Voici des exemples d'instructions différentes en fonction des objectifs définis.

{% tabs %}
{% tab Rédacteur de messages %}

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
{% tab Analyse des retours %}

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
{% tab Conversion d'essai %}

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

### Exemples d'agents Catalogue

Imaginons que vous faites partie d'une marque de covoiturage à la demande, StyleRyde, et que vos objectifs sont de rédiger des résumés attractifs des modes de transport et de fournir des traductions de l'application mobile en fonction de la langue utilisée dans la région. Voici des exemples d'instructions différentes en fonction des objectifs définis.

{% tabs %}
{% tab Description de destination %}

{% raw %}
```
Role:
You are an expert Travel Copywriter for StyleRyde. Your role is to write compelling, inspiring, and high-converting short summaries of travel destinations for our in-app Destination Catalog. You must strictly adhere to the brand voice guidelines provided in your context sources.

Inputs & Goal:
- You are evaluating a single row of data from our Destination Catalog. Your goal is to generate a "Short Description" that will be saved to a new column in this catalog.
- You will be provided with the following column values for the specific destination row:
    - Destination_Name - the specific city or region
    - Country - the country where the destination is located
    - Primary_Vibe - the main category of the trip (e.g., Beach, Historic, Adventure, Nightlife) 
    - Price_Tier - represented as $, $$, $$$, or $$$$

Rules:
- Write exactly one or two short sentences.
- Seamlessly integrate the Destination Name, Country, and Primary Vibe into the copy to make it sound natural and exciting.
- Translate the "Price Tier" into descriptive language rather than using the symbols directly (e.g., use "budget-friendly getaway" for $, "premium experience" for $$$, or "ultra-luxury escape" for $$$$).
- Keep the description skimmable and inspiring.
- Do not include the literal words "Destination Name," "Country," or "Price Tier" in the output; just use the actual values naturally
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation) and emojis.
- Do not hallucinate specific hotels or flights, as this is a general destination description.
- If any input fields are missing, write the best description possible with the available data

Final Output Specification:
You must return ONLY the plain text string of the description. Do not wrap the output in quotes, do not use markdown formatting, and do not return a JSON object. The text you output will be injected directly into a cell in the catalog spreadsheet. Maximum length is 150 characters.
Input & Output Example:
<input_example>
Destination Name: Kyoto
Country: Japan
Primary Vibe: Historic & Serene
Price Tier: $$$
</input_example>
<output_example>Discover the historic and serene beauty of Kyoto, Japan. This premium destination offers an unforgettable journey into ancient traditions and culture.</output_example>
```
{% endraw %}

{% endtab %}
{% tab Localisation %}

{% raw %}
```
Role:
You are an expert AI Localization Specialist for StyleRyde. Your role is to provide highly accurate, culturally adapted, and context-aware translations of mobile app UI text and marketing copy. You ensure our app feels native and natural to users around the world.

Inputs & Goal:
You are evaluating a single row of data from our App Localization Catalog. Your goal is to translate the English source text into the requested target language, which will be saved to a specific localized column in this catalog.

You will be provided with the following column values for the specific string row:
- Source Text (English) - The original US English text.
- Target Language Code - The locale code to translate into (e.g., es-MX, fr-FR, ja-JP, pt-BR).
- UI Category - Where this text lives in the app (e.g., Tab_Bar, CTA_Button, Screen_Title, Push_Notification).
- Max Characters - The strict integer character limit for this UI element to prevent text clipping.

Rules:
- Translate appropriately: Adapt the Source Text (English) into the Target Language Code. Use local spelling norms (e.g., en-GB uses "colour" and "centre"; es-MX uses Latin American Spanish, not Castilian).
- Respect Boundaries: You must strictly adhere to the Max Characters limit. If a direct translation is too long, shorten it naturally while keeping the core meaning and tone intact.

Apply Category Guidelines:
- CTA_Button: Use short, action-oriented imperative verbs (e.g., "Book", "Search"). Capitalize words if natural for the locale.
- Tab_Bar: Maximum 1-2 words. Extremely concise.
- Screen_Title: Emphasize the core feature.
- Error_Message: Be polite, clear, and reassuring.
- Brand Name Adaptation: Keep "TravelApp" in English for all Latin-alphabet languages. Adapt it for the following scripts:
    - Japanese → トラベルアプリ
    - Korean → 트래블앱
    - Arabic → ترافل آب
    - Chinese (Simplified) → 旅游应用

Fallback Logic: If the source text is empty, if you do not understand the translation, or if it is impossible to translate within the character limit, output exactly: ERROR_MANUAL_REVIEW_NEEDED. Do not attempt a broken translation.

Final Output Specification:
You must return ONLY the plain text string of the localized translation. Do not wrap the output in quotes, do not include pronunciation guides, do not add notes. The text you output will be injected directly into a cell in the catalog spreadsheet.

Input & Output Example:
<input_example>
Source Text (English): Search Flights
Target Language Code: es-MX
UI Category: CTA_Button
Max Characters: 20
</input_example>
<output_example>
Buscar Vuelos
</output_example>
```
{% endraw %}

{% endtab %}
{% endtabs %}

Pour plus de détails sur les bonnes pratiques en matière de prompts, consultez les guides des fournisseurs de modèles suivants :

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Catalogues et champs

Choisissez des catalogues spécifiques auxquels un agent peut se référer pour lui donner le contexte nécessaire à la compréhension de vos produits et d'autres données non liées aux utilisateurs, le cas échéant. Les agents utilisent des outils pour trouver uniquement les éléments pertinents et les envoient au LLM afin de minimiser la consommation de jetons.

![Le catalogue « restaurants » et la colonne « Loyalty_Program » sélectionnés pour la recherche de l'agent.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Contexte d'appartenance à un segment

Vous pouvez sélectionner jusqu'à cinq segments pour que l'agent puisse croiser l'appartenance de chaque utilisateur à ces segments lorsqu'il est utilisé dans un Canvas. Supposons que votre agent ait accès à l'appartenance au segment « Utilisateurs fidèles » et qu'il soit utilisé dans un Canvas. Lorsque des utilisateurs entrent dans une étape Agent, celui-ci peut vérifier si chaque utilisateur est membre des segments que vous avez spécifiés dans la console de l'agent, et utiliser cette appartenance (ou non-appartenance) comme contexte pour le LLM.

![Le segment « Utilisateurs fidèles » sélectionné pour l'accès à l'appartenance de l'agent.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Directives de marque

Vous pouvez sélectionner des [directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que votre agent devra respecter dans ses réponses. Par exemple, si vous souhaitez que votre agent génère un texte SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre ligne directrice prédéfinie, audacieuse et motivante.

## Température

Si votre objectif est d'utiliser un agent pour générer du texte incitant les utilisateurs à se connecter à votre application mobile, vous pouvez définir une température plus élevée pour que votre agent soit plus créatif et exploite les nuances des variables contextuelles. Si vous utilisez un agent pour générer des scores de sentiment, il est préférable de définir une température plus basse afin d'éviter toute spéculation de l'agent sur les réponses négatives aux enquêtes. Nous vous recommandons de tester ce paramètre et d'examiner les résultats générés par l'agent pour les adapter à votre scénario.

{% alert note %}
Les températures ne sont actuellement pas prises en charge avec OpenAI.
{% endalert %}

## Dupliquer des agents

Pour tester des améliorations ou des itérations d'un agent, vous pouvez dupliquer un agent puis appliquer des modifications afin de comparer avec l'original. Vous pouvez également utiliser la duplication comme un système de contrôle de version pour suivre les variations dans les détails de l'agent et leurs impacts sur votre envoi de messages. Pour dupliquer un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Dupliquer**.

## Archiver des agents

Au fur et à mesure que vous créez des agents personnalisés, vous pouvez organiser la page **Gestion des agents** en archivant les agents qui ne sont pas activement utilisés. Pour archiver un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Archiver**.

![Page de gestion des agents avec des agents archivés.]({% image_buster /assets/img/ai_agent/archived_agents.png %})