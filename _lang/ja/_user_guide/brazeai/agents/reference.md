---
nav_title: リファレンス
article_title: エージェントのリファレンス
description: "Braze エージェントの主要な詳細について説明します。"
page_order: 3
---

# エージェントのリファレンス

> カスタムエージェントを作成する際、インストラクションや出力スキーマなどの主要な設定の詳細については、この記事を参照してください。概要については、[Braze エージェント]({{site.baseurl}}/user_guide/brazeai/agents/)を参照してください。

## モデル

エージェントを設定するときに、レスポンスの生成に使用するモデルを選択できます。Braze パワードモデルの使用と、独自の API キーの持ち込みの2つのオプションがあります。

{% alert important %}
Braze パワードの **Auto** モデルは、カタログ検索やセグメントメンバーシップなどのタスクを実行するのに十分な思考能力を持つモデルに最適化されています。他のモデルを使用する場合は、ご利用のユースケースに適しているかどうかをテストで確認することをお勧めします。速度や能力が異なるモデルに対して、さまざまなレベルの詳細やステップバイステップの思考を与えるために、[インストラクション](#writing-instructions)を調整する必要がある場合があります。
{% endalert %}

### オプション 1: Braze パワードモデルを使用する

これは最もシンプルなオプションで、追加のセットアップは不要です。Braze は大規模言語モデル（LLM）への直接アクセスを提供します。このオプションを使用するには、Gemini モデルを使用する **Auto** を選択します。

{% alert important %}
エージェント作成時に**モデル**ドロップダウンに **Braze Auto** が表示されない場合は、カスタマーサクセスマネージャーに連絡して、Braze Auto モデルの使用資格を取得する方法をご確認ください。
{% endalert %}

### オプション 2: 独自の API キーを持ち込む

このオプションでは、OpenAI、Anthropic、Google Gemini などのプロバイダーに Braze アカウントを接続できます。LLM プロバイダーから独自の API キーを持ち込む場合、トークンコストは Braze ではなくプロバイダーを通じて直接請求されます。

レガシーモデルは数か月後に廃止または非推奨になる可能性があるため、最新のモデルを定期的にテストすることをお勧めします。

設定方法:

1. **パートナー連携** > **テクノロジーパートナー**に移動し、プロバイダーを見つけます。
2. プロバイダーから取得した API キーを入力します。
3. **保存**を選択します。

その後、エージェントに戻ってモデルを選択できます。

Braze 提供の LLM を使用する場合、そのモデルのプロバイダーは、お客様と Braze 間のデータ処理補遺（DPA）の条件に従い、Braze のサブプロセッサーとして機能します。独自の API キーを持ち込むことを選択した場合、LLM サブスクリプションのプロバイダーは、お客様と Braze 間の契約に基づくサードパーティプロバイダーと見なされます。

#### 思考レベル

一部の LLM プロバイダーでは、選択したモデルの思考レベルを調整できます。思考レベルは、モデルが回答する前に使用する思考の範囲を定義します。素早く直接的なレスポンスから、より長い推論の連鎖まで対応します。これはレスポンスの品質、レイテンシー、トークン使用量に影響します。

| レベル | 使用するタイミング |
|-------|-------------|
| **Minimal** | シンプルで明確に定義されたタスク（カタログ検索、単純な分類など）。最速のレスポンスで最低コストです。 |
| **Low** | もう少し推論が必要だが、深い分析は不要なタスク。 |
| **Medium** | 複数ステップまたはニュアンスのあるタスク（複数の入力を分析してアクションを推奨するなど）。 |
| **High** | 複雑な推論、エッジケース、またはモデルにステップを踏んで回答させたい場合。 |

まず **Minimal** から始めて、エージェントのレスポンスをテストすることをお勧めします。エージェントが正確な回答を提供するのに苦労している場合は、思考レベルを **Low** または **Medium** に調整できます。まれに **High** の思考レベルが必要になることがありますが、このレベルを使用するとトークンコストが高くなり、レスポンス時間が長くなったり、タイムアウトエラーのリスクが高くなったりする可能性があります。エージェントが複数ステップの推論と妥当なレスポンス時間のバランスに苦労している場合は、ユースケースを複数のエージェントに分割し、Canvas やカタログで連携させることを検討してください。

Braze は、コネクテッドコンテンツと同じ IP 範囲をアウトバウンド LLM コールに使用します。範囲は[コネクテッドコンテンツ IP 許可リスト]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#connected-content-ip-allowlisting)に記載されています。プロバイダーが IP 許可リストをサポートしている場合、Braze のみがキーを使用できるようにこれらの範囲に制限できます。

{% alert important %}
Braze 提供の LLM を使用する場合、そのモデルのプロバイダーは、お客様と Braze 間のデータ処理補遺（DPA）の条件に従い、Braze のサブプロセッサーとして機能します。独自の API キーを持ち込むことを選択した場合、LLM サブスクリプションのプロバイダーは、お客様と Braze 間の契約に基づくサードパーティプロバイダーと見なされます。  
{% endalert %}

## インストラクションの記述

インストラクションは、エージェントに与えるルールまたはガイドライン（システムプロンプト）です。エージェントが実行されるたびにどのように動作するかを定義します。システムインストラクションは最大 25 KB です。

プロンプト作成を始めるための一般的なベストプラクティスを以下に示します。

1. ゴールを念頭に置いて始めましょう。まず目標を述べます。
2. モデルにロールまたはペルソナを与えます（「You are a ...」）。
3. 明確なコンテキストと制約を設定します（オーディエンス、長さ、トーン、フォーマット）。
4. 構造を求めます（「Return JSON/bullet list/table...」）。
5. 説明するのではなく、示しましょう。質の高い例をいくつか含めます。
6. 複雑なタスクを順序付けられたステップに分割します（「ステップ 1... ステップ 2...」）。
7. 推論を促します（「内部的にステップを考え、簡潔な最終回答を提供してください」または「判断を簡潔に説明してください」）。
8. パイロット、検査、反復を行います。小さな調整が大きな品質向上につながります。
9. エッジケースを処理し、ガードレールを追加し、拒否のインストラクションを追加します。
10. 再利用とスケーリングのために、うまくいったことを測定し文書化します。

### Liquid の使用

エージェントのインストラクションに [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) を含めると、レスポンスにパーソナライゼーションのレイヤーを追加できます。エージェントが取得する正確な Liquid 変数を指定し、プロンプトのコンテキストに含めることができます。たとえば、「名」を明示的に記述する代わりに、Liquid スニペット {% raw %}`{{${first_name}}}`{% endraw %} を使用できます。

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**エージェントコンソール**の**ログ**セクションで、エージェントの入出力の詳細を確認し、Liquid からどのような値がレンダリングされるかを理解できます。

![インストラクションに Liquid を含むエージェントの詳細。]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Canvas エージェントの例

旅行ブランド UponVoyage の一員であるとしましょう。目標は、顧客フィードバックの分析、パーソナライズされたメッセージの作成、無料サブスクライバーのコンバージョン率の判定です。以下は、定義された目標に基づくさまざまなインストラクションの例です。

{% tabs %}
{% tab メッセージコピーライター %}

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
{% tab フィードバック分析 %}

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
{% tab トライアルコンバージョン %}

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

### カタログエージェントの例

オンデマンドのライドシェアブランド StyleRyde の一員であるとしましょう。目標は、移動手段のマーケティング向けサマリーの作成と、地域で使用されている言語に基づくモバイルアプリの翻訳の提供です。以下は、定義された目標に基づくさまざまなインストラクションの例です。

{% tabs %}
{% tab 目的地の説明 %}

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
{% tab ローカライゼーション %}

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

プロンプトのベストプラクティスの詳細については、以下のモデルプロバイダーのガイドを参照してください。

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## カタログとフィールド

エージェントが参照する特定のカタログを選択し、製品やその他の関連する非ユーザーデータを理解するために必要なコンテキストをエージェントに提供します。エージェントはツールを使用して関連するアイテムのみを検索し、トークン使用量を最小限に抑えるためにそれらのみを LLM に送信します。

![エージェントが検索するために選択された「restaurants」カタログと「Loyalty_Program」列。]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## セグメントメンバーシップのコンテキスト

エージェントが Canvas で使用されている場合に、各ユーザーのセグメントメンバーシップを相互参照するためのセグメントを最大5つまで選択できます。たとえば、エージェントが「Loyalty Users」セグメントのセグメントメンバーシップを選択しており、そのエージェントが Canvas で使用されているとします。ユーザーがエージェントステップに入ると、エージェントは各ユーザーがエージェントコンソールで指定した各セグメントのメンバーであるかどうかを相互参照し、各ユーザーのメンバーシップ（または非メンバーシップ）を LLM のコンテキストとして使用できます。

![エージェントメンバーシップアクセス用に選択された「Loyalty Users」セグメント。]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## ブランドガイドライン

エージェントがレスポンスで遵守する[ブランドガイドライン]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)を選択できます。たとえば、エージェントがジムのメンバーシップへの登録を促す SMS コピーを生成する場合、このフィールドを使用して、事前定義された大胆でモチベーショナルなガイドラインを参照できます。

## 温度

エージェントを使用してモバイルアプリへのログインを促すコピーを生成する場合、エージェントの温度を高く設定することで、よりクリエイティブにコンテキスト変数のニュアンスを活用できます。センチメントスコアの生成にエージェントを使用している場合は、ネガティブなアンケートレスポンスに対するエージェントの推測を避けるために、低い温度に設定するのが理想的です。この設定をテストし、シナリオに合わせてエージェントの生成出力を確認することをお勧めします。

{% alert note %}
現在、OpenAI での使用では温度はサポートされていません。
{% endalert %}

## エージェントの複製

エージェントの改善や反復をテストするには、エージェントを複製してから変更を適用し、オリジナルと比較できます。また、エージェントの複製をバージョン管理として扱い、エージェントの詳細の変化やメッセージングへの影響を追跡することもできます。エージェントを複製するには:

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical"></i> メニューを選択します。
2. **複製**を選択します。

## エージェントのアーカイブ

カスタムエージェントをさらに作成すると、アクティブに使用されていないエージェントをアーカイブすることで**エージェント管理**ページを整理できます。エージェントをアーカイブするには:

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical"></i> メニューを選択します。
2. **アーカイブ**を選択します。

![アーカイブされたエージェントを含むエージェント管理ページ。]({% image_buster /assets/img/ai_agent/archived_agents.png %})