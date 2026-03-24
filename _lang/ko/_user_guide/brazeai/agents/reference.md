---
nav_title: 참조
article_title: 에이전트에 대한 참조
description: "Braze 에이전트에 대한 주요 세부정보를 참조합니다."
page_order: 3
---

# 에이전트에 대한 참조

> 커스텀 에이전트를 생성할 때 지침 및 출력 스키마와 같은 주요 설정에 대한 자세한 내용은 이 문서를 참조하세요. 소개는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)를 참조하세요.

## 모델

에이전트를 설정할 때 응답을 생성하는 데 사용할 모델을 선택할 수 있습니다. 두 가지 옵션이 있습니다: Braze 기반 모델을 사용하거나 자체 API 키를 가져오는 것입니다.

{% alert important %}
Braze 기반 **Auto** 모델은 카탈로그 검색 및 세그먼트 멤버십과 같은 작업을 수행하기에 충분한 사고 능력을 갖춘 모델에 최적화되어 있습니다. 다른 모델을 사용할 때는 해당 모델이 사용 사례에 잘 작동하는지 테스트하는 것이 좋습니다. 다양한 속도와 기능을 가진 모델에 대해 다른 수준의 세부정보 또는 단계별 사고를 제공하기 위해 [지침](#writing-instructions)을 조정해야 할 수도 있습니다.
{% endalert %}

### 옵션 1: Braze 기반 모델 사용

이것은 추가 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대형 언어 모델(LLM)에 직접 액세스를 제공합니다. 이 옵션을 사용하려면 Gemini 모델을 사용하는 **Auto**를 선택하세요.

{% alert important %}
에이전트를 생성할 때 **모델** 드롭다운에서 **Braze Auto**가 옵션으로 표시되지 않으면, 고객 성공 매니저에게 문의하여 Braze Auto 모델을 사용할 수 있는 자격을 얻는 방법을 알아보세요.
{% endalert %}

### 옵션 2: 자체 API 키 가져오기

이 옵션을 사용하면 OpenAI, Anthropic 또는 Google Gemini와 같은 제공업체와 Braze 계정을 연결할 수 있습니다. LLM 제공업체로부터 자체 API 키를 가져오면 토큰 비용이 Braze가 아닌 제공업체를 통해 직접 청구됩니다.

레거시 모델은 몇 개월 후에 중단되거나 사용 중지될 수 있으므로 최신 모델을 정기적으로 테스트하는 것이 좋습니다.

설정 방법:

1. **파트너 통합** > **기술 파트너**로 이동하여 제공업체를 찾으세요.
2. 제공업체에서 받은 API 키를 입력하세요.
3. **저장**을 선택하세요.

그런 다음 에이전트로 돌아가 모델을 선택할 수 있습니다.

Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.

#### 사고 수준

일부 LLM 제공업체에서는 선택한 모델의 사고 수준을 조정할 수 있습니다. 사고 수준은 모델이 답변하기 전에 사용하는 사고의 범위를 정의합니다—빠르고 직접적인 응답부터 더 긴 추론 체인까지 다양합니다. 이는 응답 품질, 지연 시간 및 토큰 사용량에 영향을 미칩니다.

| 수준 | 사용 시기 |
|-------|-------------|
| **최소** | 간단하고 명확하게 정의된 작업(예: 카탈로그 조회, 간단한 분류). 가장 빠른 응답과 가장 낮은 비용. |
| **낮음** | 약간 더 많은 추론이 도움이 되지만 깊은 분석이 필요하지 않은 작업. |
| **중간** | 다단계 또는 미묘한 작업(예: 여러 입력을 분석하여 동작을 추천). |
| **높음** | 복잡한 추론, 엣지 케이스, 또는 모델이 답변하기 전에 단계를 거쳐야 할 때. |

**최소**로 시작하여 에이전트의 응답을 테스트하는 것을 권장합니다. 에이전트가 정확한 답변을 제공하는 데 어려움을 겪는 경우 사고 수준을 **낮음** 또는 **중간**으로 조정할 수 있습니다. 드문 경우에 **높음** 사고 수준이 필요할 수 있지만, 이 수준을 사용하면 높은 토큰 비용과 더 긴 응답 시간 또는 타임아웃 오류의 위험이 높아질 수 있습니다. 에이전트가 다단계 추론과 합리적인 응답 시간 사이에서 균형을 맞추는 데 어려움을 겪는 경우, 사용 사례를 Canvas 또는 카탈로그에서 함께 작동할 수 있는 둘 이상의 에이전트로 분리하는 것을 고려하세요.

Braze는 연결된 콘텐츠와 동일한 IP 범위를 아웃바운드 LLM 호출에 사용합니다. 해당 범위는 [연결된 콘텐츠 IP 허용 목록]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#connected-content-ip-allowlisting)에 나열되어 있습니다. 제공업체가 IP 허용 목록을 지원하는 경우, Braze만 사용할 수 있도록 키를 해당 범위로 제한할 수 있습니다.

{% alert important %}
Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.  
{% endalert %}

## 지침 작성

지침은 에이전트(시스템 프롬프트)에게 주는 규칙 또는 가이드라인입니다. 에이전트가 실행될 때마다 어떻게 행동해야 하는지를 정의합니다. 시스템 지침은 최대 25KB까지 가능합니다.

프롬프트를 시작하는 데 도움이 되는 일반적인 모범 사례는 다음과 같습니다:

1. 결과를 염두에 두고 시작하세요. 목표를 먼저 명시하세요.
2. 모델에 역할이나 페르소나를 부여하세요 ("당신은 ...입니다").
3. 명확한 컨텍스트와 제약 조건을 설정하세요 (오디언스, 길이, 톤, 형식).
4. 구조를 요청하세요 ("JSON/글머리 목록/표로 반환...").
5. 말하지 말고 보여주세요. 몇 가지 고품질 예제를 포함하세요.
6. 복잡한 작업을 순서가 있는 단계로 나누세요 ("1단계... 2단계...").
7. 추론을 장려하세요 ("단계를 내부적으로 생각한 다음 간결한 최종 답변을 제공하세요," 또는 "결정을 간략하게 설명하세요").
8. 파일럿, 검사 및 반복하세요. 작은 조정이 큰 품질 향상으로 이어질 수 있습니다.
9. 엣지 케이스를 처리하고, 가드레일을 추가하고, 거부 지침을 추가하세요.
10. 내부에서 효과가 있는 것을 측정하고 문서화하여 재사용 및 확장할 수 있도록 하세요.

### Liquid 사용

에이전트의 지침에 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)을 포함하면 응답에 추가적인 개인화 레이어를 더할 수 있습니다. 에이전트가 받는 정확한 Liquid 변수를 지정할 수 있으며, 이를 프롬프트의 컨텍스트에 포함할 수 있습니다. 예를 들어, "이름"을 명시적으로 작성하는 대신 Liquid 스니펫 {% raw %}`{{${first_name}}}`{% endraw %}을 사용할 수 있습니다:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**에이전트 콘솔**의 **로그** 섹션에서 에이전트의 입력 및 출력 세부정보를 검토하여 Liquid에서 렌더링된 값을 확인할 수 있습니다.

![지침에 Liquid가 포함된 에이전트의 세부정보.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Canvas 에이전트 예시

여행 브랜드인 UponVoyage의 일원이라고 가정해 보겠습니다. 고객 피드백을 분석하고, 개인화된 메시지를 작성하고, 무료 가입자의 전환율을 결정하는 것이 목표입니다. 정의된 목표에 따른 다양한 지침 예시는 다음과 같습니다.

{% tabs %}
{% tab 메시지 카피라이터 %}

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
{% tab 피드백 분석 %}

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
{% tab 체험판 전환 %}

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

### 카탈로그 에이전트 예시

온디맨드 라이드셰어링 브랜드인 StyleRyde의 일원이라고 가정해 보겠습니다. 이동 수단에 대한 마케팅용 요약을 작성하고, 해당 지역에서 사용되는 언어에 따라 모바일 앱의 번역을 제공하는 것이 목표입니다. 정의된 목표에 따른 다양한 지침 예시는 다음과 같습니다.

{% tabs %}
{% tab 목적지 설명 %}

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
{% tab 현지화 %}

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

프롬프트 모범 사례에 대한 자세한 내용은 다음 모델 제공업체의 가이드를 참조하세요:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## 카탈로그 및 필드

에이전트가 참조할 특정 카탈로그를 선택하고, 관련이 있을 때 제품 및 기타 비사용자 데이터를 이해하는 데 필요한 컨텍스트를 에이전트에 제공하세요. 에이전트는 도구를 사용하여 관련 항목만 찾고, 이를 LLM에 보내 토큰 사용을 최소화합니다.

![에이전트가 검색할 "restaurants" 카탈로그 및 "Loyalty_Program" 열이 선택되었습니다.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## 세그먼트 멤버십 컨텍스트

에이전트가 Canvas에서 사용될 때 각 사용자의 세그먼트 멤버십을 교차 참조하기 위해 최대 5개의 세그먼트를 선택할 수 있습니다. 에이전트에 "로열티 사용자" 세그먼트에 대한 세그먼트 멤버십이 선택되어 있고, 에이전트가 Canvas에서 사용된다고 가정해 보겠습니다. 사용자가 에이전트 단계에 들어가면, 에이전트는 에이전트 콘솔에서 지정한 각 세그먼트에 각 사용자가 멤버인지 교차 참조할 수 있으며, 각 사용자의 멤버십(또는 비멤버십)을 LLM의 컨텍스트로 사용할 수 있습니다.

![에이전트 멤버십 접근을 위해 선택된 "로열티 사용자" 세그먼트.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## 브랜드 가이드라인

에이전트가 응답에서 준수해야 할 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)을 선택할 수 있습니다. 예를 들어, 에이전트가 사용자에게 체육관 멤버십 가입을 유도하는 SMS 카피를 생성하도록 하려면, 이 필드를 사용하여 미리 정의된 대담하고 동기 부여가 되는 가이드라인을 참조할 수 있습니다.

## 온도

사용자가 모바일 앱에 로그인하도록 유도하는 카피를 생성하기 위해 에이전트를 사용하려는 경우, 에이전트가 더 창의적이고 컨텍스트 변수의 뉘앙스를 활용할 수 있도록 더 높은 온도를 설정할 수 있습니다. 에이전트를 사용하여 감정 점수를 생성하는 경우, 부정적인 설문조사 응답에 대한 에이전트의 추측을 피하기 위해 더 낮은 온도를 설정하는 것이 이상적일 수 있습니다. 이 설정을 테스트하고 에이전트가 생성한 출력을 검토하여 시나리오에 맞게 조정하는 것을 권장합니다.

{% alert note %}
온도는 현재 OpenAI와 함께 사용이 지원되지 않습니다.
{% endalert %}

## 에이전트 복제

에이전트의 개선 사항이나 반복을 테스트하기 위해, 에이전트를 복제한 다음 변경 사항을 적용하여 원본과 비교할 수 있습니다. 에이전트 복제를 에이전트 세부정보의 변화를 추적하고 메시징에 미치는 영향을 확인하는 버전 관리로 활용할 수도 있습니다. 에이전트를 복제하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **복제**를 선택합니다.

## 에이전트 아카이브

더 많은 커스텀 에이전트를 생성함에 따라, 활발히 사용되지 않는 에이전트를 아카이브하여 **에이전트 관리** 페이지를 정리할 수 있습니다. 에이전트를 아카이브하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **아카이브**를 선택합니다.

![아카이브된 에이전트가 있는 에이전트 관리 페이지.]({% image_buster /assets/img/ai_agent/archived_agents.png %})