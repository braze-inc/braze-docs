---
nav_title: Referência
article_title: Referência para agentes
description: "Detalhes de referência sobre os Agentes Braze."
page_order: 3
---

# Referência para agentes

> Ao criar agentes personalizados, consulte este artigo para mais informações sobre configurações importantes, como instruções e esquemas de saída. Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Modelos

Quando você configura um agente, pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo alimentado pelo Braze ou trazer sua própria chave de API.

{% alert important %}
O modelo **Auto** alimentado pelo Braze é otimizado para modelos cujas capacidades de raciocínio são suficientes para realizar tarefas como busca em catálogo e associação a segmentos. Ao usar outros modelos, recomendamos testar para confirmar se seu modelo funciona bem para seu caso de uso. Você pode precisar ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhe ou raciocínio passo a passo para modelos com diferentes velocidades e capacidades.
{% endalert %}

### Opção 1: Use um modelo alimentado pelo Braze

Esta é a opção mais simples, sem configuração extra necessária. O Braze fornece acesso a grandes modelos de linguagem (LLMs) diretamente. Para usar esta opção, selecione **Auto**, que utiliza modelos Gemini.

{% alert important %}
Se você não vê **Braze Auto** como uma opção no menu suspenso **Modelo** ao criar um agente, entre em contato com seu gerente de sucesso do cliente para saber como se tornar elegível para usar o modelo Braze Auto.
{% endalert %}

### Opção 2: Traga sua própria chave de API

Com esta opção, você pode conectar sua conta Braze com provedores como OpenAI, Anthropic ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos de token são cobrados diretamente através do seu provedor, não através do Braze.

{% alert important %}
Recomendamos testar rotineiramente os modelos mais recentes, pois modelos legados podem ser descontinuados ou depreciados após alguns meses.
{% endalert %}

Para configurar isso:

1. Acessar **Integrações de Parceiros** > **Parceiros de Tecnologia** e encontrar seu provedor.
2. Insira sua chave de API do provedor.
3. Selecione **Salvar**.

Em seguida, você pode voltar para seu agente e selecionar seu modelo.

{% alert important %}
Quando você usa um LLM fornecido pela Braze, os provedores de tal modelo atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre você e a Braze. Se você optar por trazer sua própria chave de API, o provedor da sua assinatura de LLM é considerado um Provedor de Terceiros sob o contrato entre você e a Braze.  
{% endalert %}

## Escrevendo instruções

Instruções são as regras ou diretrizes que você dá ao agente (prompt do sistema). Elas definem como o agente deve se comportar cada vez que é executado. Instruções do sistema podem ter até 25 KB.

Aqui estão algumas melhores práticas gerais para você começar a criar prompts:

1. Comece com o fim em mente. Declare o objetivo primeiro.
2. Dê ao modelo um papel ou persona ("Você é um ...").
3. Defina um contexto e restrições claros (público, comprimento, tom, formato).
4. Peça por estrutura ("Retorne JSON/lista com marcadores/tabela...").
5. Mostre, não conte. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1..."). Etapa 2...".
7. Incentive o raciocínio ("Pense nas etapas internamente, depois forneça uma resposta final concisa," ou "explique brevemente sua decisão").
8. Pilote, inspecione e itere. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione barreiras de proteção e instruções de recusa.
10. Meça e documente o que funciona internamente para reutilização e escalabilidade.

### Usando Liquid

Incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) nas instruções do seu agente pode adicionar uma camada extra de personalização na sua resposta. Você pode especificar a variável Liquid exata que o agente recebe e pode incluí-la no contexto do seu prompt. Por exemplo, em vez de escrever explicitamente "primeiro nome", você pode usar o trecho Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Na seção **Logs** do **Console do Agente**, você pode revisar os detalhes da entrada e saída do agente para entender qual valor é renderizado a partir do Liquid.

![Os detalhes de um agente que tem Liquid em suas instruções.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Exemplos

Vamos supor que você faz parte de uma marca de viagens, UponVoyage, e seus objetivos são analisar o feedback dos clientes, escrever mensagens personalizadas e determinar a taxa de conversão para seus assinantes gratuitos. Aqui estão exemplos de diferentes instruções com base em objetivos definidos:

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

Para mais detalhes sobre as melhores práticas de prompting, consulte guias dos seguintes provedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Catálogos e campos

Escolha catálogos específicos para um agente referenciar e dar ao seu agente o contexto que ele precisa para entender seus produtos e outros dados não relacionados ao usuário quando relevante. Os agentes usam ferramentas para encontrar apenas os itens relevantes e enviá-los ao LLM para minimizar o uso de tokens.

![O catálogo "restaurantes" e "Loyalty_Program" a coluna selecionada para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Contexto de associação de segmento

Você pode selecionar até cinco segmentos para o agente cruzar a associação de segmento de cada usuário quando o agente é usado em um Canvas. Vamos supor que seu agente tenha a associação de segmento selecionada para um segmento de "Usuários de Fidelidade", e o agente é usado em um Canvas. Quando os usuários entram em uma etapa do Agente, o agente pode cruzar se cada usuário é membro de cada segmento que você especificou no console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O segmento "Usuários de Fidelidade" selecionado para acesso de membros agentes.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Diretrizes da marca

Você pode selecionar [diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para o seu agente seguir em suas respostas. Por exemplo, se você quiser que seu agente gere cópias de SMS para incentivar os usuários a se inscreverem em uma associação de academia, você pode usar este campo para referenciar sua diretriz motivacional em negrito pré-definida.

## Temperatura

Se o seu objetivo é usar um agente para gerar cópias que incentivem os usuários a fazer login no seu app móvel, você pode definir uma temperatura mais alta para que seu agente seja mais criativo e use as nuances das variáveis de contexto. Se você estiver usando um agente para gerar pontuações de sentimento, pode ser ideal definir uma temperatura mais baixa para evitar qualquer especulação do agente sobre respostas negativas de pesquisas. Recomendamos testar essa configuração e revisar a saída gerada pelo agente para se adequar ao seu cenário.

{% alert note %}
Temperaturas não são atualmente suportadas para uso com OpenAI.
{% endalert %}

## Agentes duplicados

Para testar melhorias ou iterações de um agente, você pode duplicar um agente e, em seguida, aplicar alterações para comparar com o original. Você também pode tratar a duplicação de agentes como controle de versão para rastrear variações nos detalhes do agente e quaisquer impactos na sua mensagem. Para duplicar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Duplicar**.

## Arquivar agentes

À medida que você cria mais agentes personalizados, pode organizar a página **Gerenciamento de Agentes** arquivando agentes que não estão sendo usados ativamente. Para arquivar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Arquivo**.

![Página de Gerenciamento de Agentes com agentes arquivados.]({% image_buster /assets/img/ai_agent/archived_agents.png %})
