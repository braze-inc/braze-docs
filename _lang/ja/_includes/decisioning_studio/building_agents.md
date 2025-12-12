# エージェントの構築

> BrazeAI Decisioning Studio™ のエージェントを構築する方法を学習することで、パーソナライズされた実験を自動化し、手動で AB テストを行うことなく、コンバージョン、リテンション、収益などの成果を最適化することができます。

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## エージェントについて

AI 意思決定エージェントは、BrazeAI™ 意思決定エンジンのカスタム設定であり、特定のビジネス目標を達成するためにカスタマイズされます。

例えば、初回販売後のフォローアップコンバージョンを増やすために、リピート購入エージェントを構築することができます。Braze でオーディエンスやメッセージを定義すると、意思決定エージェントが毎日実験を行い、顧客ごとに商品のオファー、メッセージのタイミング、頻度などのさまざまな組み合わせを自動的にテストします。時間の経過とともに、BrazeAI™ は何が最も効果的かを学習し、再購入率を最大化するために Braze を通じてパーソナライズされた送信を調整します。

優れたエージェントを構築するには、次を行います。

- 収益、コンバージョン、ARPU など、最適化する BrazeAI™ の成功指標を選択する。
- オファー、件名、クリエイティブ、チャネル、送信時間など、テストするディメンションを定義する。
- メールと SMS、1 日および 1 週あたりの頻度など、ディメンションごとにオプションを選択する。

![紹介メール用の Decisioning Studio エージェントのサンプル図。]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## サンプルエージェント

BrazeAI Decisioning Studio™ で構築できるエージェントの例をいくつかご紹介します。AI の意思決定エージェントは、顧客とのやり取りから学習し、そのインサイトを翌日のアクションに活かします。

{% multi_lang_include decisioning_studio/sample_agents.md %}

## エージェントの構築

### 前提条件

エージェントを構築する前に、[ BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration) を統合する必要があります。

### ステップ 1: AI エキスパートサービスへの連絡

AI エキスパートサービスチームが協力して、意思決定エージェントの調査、設計、構築を行います。ご連絡がまだの場合は、[問い合わせ](https://www.braze.com/get-started/)ページからご連絡ください。

以下のステップを一緒に実行して、適切なカスタムエージェントを構築します。

### ステップ 2: エージェントの設計

AI エキスパートサービスチームと一緒に以下を定義します。

- ターゲットオーディエンス 
- 最適化するビジネス指標 
- BrazeAI™ 意思決定エージェントのアクション 
- エージェントがビジネス成果を牽引するために活用するファーストパティ顧客データ 

設計を準備することで、チームはあなたと協力し、追加の統合要件を特定し、完成させることができます。

### ステップ 3: 配信プラットフォームの設定

次に、AI エキスパートサービスチームがマーケティングオートメーションプラットフォームの設定をお手伝いします。Decisioning Studio は Braze に最適ですが、他のさまざまなプラットフォームがサポートされています。追加のリソースについては、AI エキスパートサービスチームにお問い合わせください。

{% tabs local %}
{% tab Braze %}
Braze の設定方法:

1. [キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)または[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule)を作成します。BrazeAI Decisioning Studio™ では、この配信方式を使用して、1:1 でパーソナライズされたアクティベーションイベントを、定義したオーディエンスのユーザーに送信します。
2. BrazeAI™ を専用のコントロールグループにするために、Braze[ コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)は含めないでください。
3. お使いのディメンションに応じて、クリエイティブコンテンツで Liquid タグを設定し、メッセージングに BrazeAI™ のレコメンデーションをダイナミックに入力できます。BrazeAI™ は、Braze API を使用して、テンプレートで Liquid タグに顧客固有のコンテンツを渡します。
{% endtab %}
{% endtabs %}

### ステップ 4: 起動と監視

エージェントを起動した後、AI エキスパートサービスチームは、合意された設計に合わせて監視および調整を続けます。また、必要に応じて、エージェントの調整、拡張、修正を行うこともできます。
