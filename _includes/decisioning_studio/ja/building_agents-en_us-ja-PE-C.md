# 建築代理店

> BrazeAI Decisioning Studio™のエージェントを構築する方法について説明します。これにより、パーソナライズされたの実験を自動化し、手動のA/Bテストなしでコンバージョン、リテンション、収益などの結果を最適化できます。

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## エージェントについて

AI デシジョンエージェントは、BrazeAI™デシジョンエンジンのカスタム設定であり、特定の事業目標に合わせてカスタマイズされます。

たとえば、最初のセール後のフォローアップコンバージョンsを増やすために、リピート購入エージェントを構築できます。オーディエンスとメッセージはBrazeで定義しますが、デシジョンエージェントは毎日の実験を実行し、顧客ごとにさまざまな組み合わせの製品オファー、メッセージタイミング、および頻度を自動的にテストします。やがて、BrazeAI™はパーソナライズされたがBrazeを通して送る最も効果的なことを学び、自社株買いの比率を最大化するように調整します。

優れたエージェントを構築するには、次のようにします。

- BrazeAI™の成功基準を選択して、収益、コンバージョンs、ARPUなどに最適化します。
- オファー、件名、クリエイティブ、チャネル、送信時刻など、テストするディメンションを定義します。
- メールとSMS、または毎日と毎週の頻度など、ディメンションごとに選択します。

\![紹介メール用の決断スタジオエージェントのサンプルダイアグラム。]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## 試薬

BrazeAI Decisioning Studio™でビルドできるエージェントのサンプルを以下に示します。あなたのAIデシジョンエージェントは、すべての顧客のアクションから学び、翌日のアクションまで、それらのインサイトをアプリします。

{% multi_lang_include decisioning_studio/sample_agents.md %}

## エージェントの構築

### 前提条件

エージェントを構築するには、[ BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration) を統合する必要があります。

### ステップ 1: AIエキスパートサービスに問い合わせる

AI Expert Services チームは、あなたと密接に連携して、あなたのデシジョンエージェントの範囲、設計、構築を行います。まだの場合は、[リーチアウト](https://www.braze.com/get-started/) を開始してください。

以下のステップを一緒に実行して、適切なカスタムエージェントを構築します。

### ステップ2: エージェントの設計

AI Expert Services チームとともに、以下を定義します。

- 標的オーディエンス、 
- 最適化するビジネスメトリック。 
- BrazeAI™デシジョンエージェントのアクションs、および 
- 代理店が事業成果を牽引するために活用すべき第一者顧客データ。 

設計を手元に置くことで、チームはあなたと協力して、追加の統合要件を特定し、完成させることができます。

### ステップ 3: 配信プラットフォームの設定

次に、AIエキスパートサービスチームがマーケティング オートメーション プラットフォームの設定を手伝います。デシジョンスタジオはBrazeに最適ですが、他のさまざまなプラットフォームがサポートされています。追加のリソースについては、AI エキスパートサービスチームにお問い合わせください。

{% tabs local %}
{% tab Braze %}
Brazeを設定するには:

1. [キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)または[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule)を作成します。BrazeAI Decisioning Studio™では、この配信方式を使用して、1:1 パーソナライズされたアクティベーションイベントを定義したオーディエンスのユーザーs に送信します。
2. Braze[コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)を含めないでください。そのため、代わりにBrazeAI™を専用コントロールグループにすることができます。
3. お使いのディメンションに応じて、クリエイティブコンテンツの「リキッドタグ」を設定し、メッセージングにBrazeAI™の推奨事項をダイナミックな入力できます。BrazeAI™は、Braze API を使用して、テンプレートs のリキッドタグs に顧客固有のコンテンツを渡します。
{% endtab %}
{% endtabs %}

### ステップ 4: 起動と監視

エージェントを起動した後、AI Expert Services チームは、合意された設計に合わせて監視およびチューニングを続けます。また、必要に応じて、エージェントの調整、拡張、または変更を行うこともできます。
