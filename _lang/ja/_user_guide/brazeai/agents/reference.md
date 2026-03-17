---
nav_title: 参考
article_title: エージェント sのリファレンス
description: "Braze Agent のリファレンスキーについて説明します。"
page_order: 3
---

# エージェント sのリファレンス

> カスタムエージェントs を作成する際、手順や出力スキーマなどのキー設定の詳細については、この記事を参照してください。概要については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/)を参照してください。

## モデル

エージェントを設定するときに、レスポンスを生成するために使用するモデルを選択できます。Brazeパワーモデルの使用と、独自のAPI キーの持ち込みの2つの選択肢があります。

{% alert important %}
Braze-powered **Auto**モデルは、カタログ検索やセグメントメンバーシップなどの作業を実行するのに充分な思考能力を持つモデルに最適化されています。他の機種をご使用の際は、ご使用のユースケースに合った機種であることを確認するためのテストをお勧めします。さまざまなスピードと能力を持つ機種に、さまざまな細部やステップ的な思考を与えるために、[命令](#writing-instructions)を調整する必要があるかもしれません。
{% endalert %}

### オプション 1: Braze駆動の機種を使用する

これは最も単純なオプションで、追加のセットアップは必要ありません。Braze は、ラージ・ランゲージ・モデル(LLM) を直接的に利用できます。このオプションを使用するには、Gemini モデルを使用する**Auto** を選択します。

{% alert important %}
** Braze Auto** が、エージェントの作成時に **Model** ドロップダウンに表示されない場合は、顧客 のサクセスマネージャーに連絡して、Braze Auto モデルの使用資格を取得してください。
{% endalert %}

### オプション 2: 自分のAPI キーを持ってくる

この機能を使用すると、OpenAI、Anthropic、Google Gemini などのプロバイダーにBraze アカウントを接続できます。LLMプロバイダーから独自のAPI キーを取得した場合、トークン費用はBrazeではなくプロバイダーを通じて直接請求されます。

{% alert important %}
レガシーモデルは数カ月後に廃止または廃止される可能性があるため、最新のモデルを定期的にテストすることをお勧めします。
{% endalert %}

これを設定するには:

1. **Partner Integrations**> **Technology Partners**に移動し、プロバイダを見つけます。
2. プロバイダーからAPI キーを入力します。
3. [**保存**] を選択します。

その後、エージェントに戻り、機種を選択できます。

{% alert important %}
Braze提供のLLMを使用する場合、そのようなモデルのプロバイダーは、お客様とBrazeの間のデータプロセッシングアドオンダム(DPA)の条件に従い、Brazeサブプロセッサとして機能します。独自のAPI キーを取得することを選択した場合、LLM サブスクリプションのプロバイダーは、お客様とBraze 間の契約に基づくサードパーティプロバイダーと見なされます。  
{% endalert %}

## 命令の記述

指示は、エージェントに指定する規則または指針です(システムプロンプト)。これらは、エージェントが実行されるたびにどのように動作するかを定義します。システム命令は最大25KB です。

プロンプトを開始するための一般的なベストプラクティスを次に示します。

1. 最後を念頭に置いて始めましょう。まず目標を述べよ。
2. モデルにロールまたはペルソナを指定します("You are ...")。
3. クリアコンテキストとコンストレーニングts(オーディエンス、長さ、トーン、形式)を設定します。
4. 構造を確認します("JSON/箇条書きリスト/table...")。
5. 見せろ、言わないで。質の高い例をいくつか挙げてください。
6. 複雑な作業を順序付けられたステップに分割(" ステップ 1...)ステップ2...")
7. 推論を促す("ステップで考えてみよう s 内部 ly、簡潔な最終回答"または"判断とクォートを簡単に説明する;)。
8. パイロット、検査、および反復。微調整は、大きな品質向上につながります。
9. エッジケースの取り扱い、ガードレールの追加、拒否指示の追加。
10. 再利用と拡大・縮小のために内部機能するものを測定し、文書化する。

### Liquid の使用

エージェントの指示に[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) を含めると、レスポンスに追加のパーソナライゼーションレイヤーを追加できます。エージェントが取得するリキッド変数を指定し、プロンプトのコンテキストに含めることができます。たとえば、"名" を明示的に記述する代わりに、Liquid スニペット{% raw %}`{{${first_name}}}`{% endraw %} を使用できます。

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**Logs**セクションの**エージェントコンソール**では、エージェントの入出力の詳細を確認して、リキッドからどのような値が表示されるかを理解することができます。

![指示にリキッドが含まれているエージェントの詳細。]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### 例

旅行ブランド、UponVoyageの一部であるとしよう。目標は、顧客 フィードバックを分析し、パーソナライズされたを書き、自由サブスクライバーsのコンバージョン率を決定することである。次に、定義された目標に基づいたさまざまな命令の例を示します。

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

ベストプラクティスのプロンプトの詳細については、次のモデルプロバイダのガイドを参照してください。

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ジェミニ](https://support.google.com/a/users/answer/14200040?hl=en)

## カタログおよびフィールド

エージェントの具体的なカタログsを選んで、あなたの商品や、関連する場合には他の非ユーザーデータを理解するために必要な文脈をあなたのエージェントに伝えましょう。エージェントはツールを使用して関連項目のみを検索し、トークンの使用を最小限に抑えるためにLLM に送信します。

!["restaurants" カタログ および"Loyalty_Program" 列が、検索するエージェントに対して選択されます。]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## セグメント・メンバーシップのコンテキスト

セグメントは、エージェントがキャンバスで使用されているときに、それぞれのユーザーのセグメントメンバーシップを相互参照するために、最大5 つまで選択できます。たとえば、あなたのエージェントが、"Loyalty Users" セグメントに対して選択されたセグメントメンバーシップを持っており、そのエージェントがキャンバスで使用されているとします。ユーザー s がエージェント ステップを入力すると、各ユーザーがエージェントコンソールで指定した各セグメントのメンバであり、LLM のコンテキストとして各ユーザーのメンバシップ(または非メンバシップ) を使用する場合、エージェントは相互参照できます。

!["Loyalty Users"エージェントメンバーシップアクセス用に選択されたセグメント。]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## ブランド・ガイドライン

エージェントが対応に従うように、[ブランドガイドライン]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)を選択できます。たとえば、エージェントがSMSコピーを生成して、ユーザーがジムのメンバーシップに登録することを奨励する場合、このフィールドを使用して、事前定義された大胆なモチベーションガイドラインを参照できます。

## 温度

エージェントを使用してコピーを生成し、ユーザーが携帯アプリにログインできるようにするには、エージェントをよりクリエイティブに設定し、コンテキスト変数のニュアンスを使用します。センチメントスコアを生成するためにエージェントを使用している場合は、低温に設定することがアイデアな場合があります。これは、負の調査レスポンスに対するエージェントの推測を回避するためです。この設定をテストし、シナリオに合わせてエージェントで生成されたアウトプットを確認することをお勧めします。

{% alert note %}
OpenAI で使用するための温度は現在サポートされていません。
{% endalert %}

## 重複エージェント

エージェントの改良や反復を検証するには、エージェントを複製し、ly の変更をアプリして元のものと比較します。また、複製エージェントをバージョンコントロールとして扱って、エージェントの細部の変化やメッセージングへの影響を追跡することもできます。エージェントを複製するには

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical"></i>を選択します。
2. [**複製**] を選択します。

## エージェントのアーカイブ

カスタムエージェントs をさらに作成すると、アクティブに使用されていないエージェントをアーカイブすることで、** エージェント管理** ページを編成できます。エージェントをアーカイブするには

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical"></i>を選択します。
2. [**アーカイブ**] を選択します。

![アーカイブされたエージェントを含むエージェントマネジメントページ。]({% image_buster /assets/img/ai_agent/archived_agents.png %})
