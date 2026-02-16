---
nav_title: エージェントの設計
article_title: エージェントの設計
page_order: 3
description: "オーディエンス定義、サクセスメトリクス、ディメンションなど、AI デシジョンサービスチームを使用してデシジョンスタジオプロエージェントをデザインする方法について説明します。"
---

# エージェントの設計

> エージェント設定の最初のステップは、AI デシジョンサービスチームと連携してエージェントをデザインします。ここでは、主要なデザイン決定とオーディエンスの定義方法について説明します。

サクセスメトリック、ディメンション、アクションバンク、およびコンストレーニングts など、デシジョンエージェントに関する基本的な概念については、[デシジョンエージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)を参照してください。

## 重要な設計決定

AI Decisioning Services チームでは、以下の決定を行います。

| 決定 | 説明 | 例 |
|----------|-------------|----------|
| **成功メトリック** | カスタマーエンゲージメントをパーソナライズする場合、エージェントはどのようなものを最大化しますか? | 収益、生涯価値、ARPU、コンバージョン s、リテンション |
| **オーディエンス** | デシジョンスタジオエージェントは誰に対してカスタマーエンゲージメント決定を行いますか? | すべての顧客s、ロイヤルティメンバ、リスクのあるサブスクライバーs |
| **実験群** | デシジョン・スタジオの無作為化コントロール主導試験はどのように構成されるべきか? | 決定スタジオ、ランダム制御、BAU、ホールドアウト |
| **ディメンション** | エージェントはどのような決定をパーソナライズすべきか? | 時刻、件名、頻度、オファー、チャネル |
| **options** | エージェントはどのようなオプションを使用する必要がありますか? | 具体的なテンプレート、オファー、タイムウィンドウ |
| **制約** | エージェント*never*は、どのような決定を行うべきか? | 地理的な制約、予算の制限、適格性のルール |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

これらの決定のそれぞれは、エージェントがどれだけの増分上昇を生み出すことができるか、そしてどれくらいの速さで生み出すことができるか、という意味合いを持つ。私たちのAI Decisioning Servicesチームは、あなたと協力して、あなたのビジネスルールのすべてを尊重しながら最大の価値を生み出すエージェントを設計します。

![プロダイアグラムの決定]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## オーディエンスの定義

ユースケースオーディエンスs は通常、カスタマーエンゲージメントプラットフォーム(Braze やSalesforce Marketing Cloud など) で定義され、Decisioning Studio エージェントに送信されます。その後、無作為化コントロール主導試験を実施するために、顧客sを治療群に分ける。

### 投与群

| グループ | 説明 |
|-------|-------------|
| **決定スタジオ** | AIに最適化された推奨を受け取った顧客 |
| **ランダム制御** | 無作為に選択したオプション(ベースライン比較)を受ける顧客 |
| **通常のビジネス(オプション)** | 現行のマーケティング行程を受け取った顧客(現行パフォーマンスとの比較用) |
| **ホールドアウト(オプション)** | 通信を受けていない顧客(総合的なキャンペーン影響を測定するため) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### オーディエンスの設定

{% tabs %}
{% tab Braze %}

**Braze でのオーディエンスの設定:**

1. 対象とするオーディエンスのSegmentを作成します。
2. AI Decisioning Services チームにセグメントID を提供します。

{% alert note %}
Brazeのために、多重Segmentsを取り込み、それらを組み合わせてオーディエンスを作成することができます。デシジョンスタジオは、Business-as-Usual比較キャンペーンのSegmentを取り込むことができます。これらのパターンはすべて許容される。
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Salesforce Marketing Cloud でのオーディエンスの設定:**

1. オーディエンスのSFMCデータ拡張を設定し、データ拡張IDを指定します
2. Decisioning Studioで必要とされるアプリの適切な権限を使用したAPIインテグレーションのためのSFMCインストールパッケージの設定
3. デシジョンスタジオが利用可能な最新の増分データからプルするため、このデータ拡張が毎日更新されることを確認します

Braze サービスチームに拡張ID とAPI キーを提供します。今後のステップでは、顧客データの摂取を支援する。

{% endtab %}
{% tab Klaviyo %}

**Klaviyoでオーディエンスを定義します。**

1. オーディエンス Segmentの作成
2. 非公開API キーを生成し、これをBraze AI 決定チームに提供します
3. Segment番号とAPI キーをBraze部門に提供する

これらのステップの取得方法の詳細については、[Klaviyo ドキュメント](https://help.klaviyo.com/hc/en-us/articles/115005237908)を参照してください。

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

オーディエンスが現在 Braze、SFMC、または Klaviyo に保存されていない場合、次に最適なステップは、Braze-コントロール先の Google Cloud Services バケットへの自動エクスポートを設定することです。

これが実行可能かどうかを判断するには、マーテックプラットフォームのドキュメントを参照してください。たとえば、mParticle は、[Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/) とのネイティブ統合を提供します。この場合、オーディエンスデータをエクスポートするGCS バケットを提供できます。

次のようなページがあります。
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience プラットフォーム](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Pro機能

Studio Pro を決定すると、AI の決定機能を最大限に活用できます。

| 能力 | 詳細 |
|------------|---------|
| **任意の成功メトリック** | 収益、コンバージョン、ARPU、生涯価値、または事業のKPIの最適化 |
| **無制限寸法** | オファー、チャネル、時期、頻度、クリエイティブ、その他にまたがってカスタマイズ |
| **任意のCEP** | Braze、SFMC、Klaviyo、および任意のプラットフォームのカスタムインテグレーションとのネイティブインテグレーション |
| **AIデシジョンサービス** | Brazeのデータサイエンスチームによる熱心な支援 |
| **先進実験設計** | 完全にカスタマイズ可能な治療グループとホールドアウト |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## ベストプラクティス

Decisioning Studio エージェントを設計するためのベストプラクティス:

1. **データの豊富さを最大化します**:エージェントが顧客s について持っている情報量が多いほど、エージェントのパフォーマンスは向上します。
2. **アクションの分散 s**:エージェントが使用できるアクションの集合が多様であればあるほど、ユーザーごとに戦略をパーソナライズできるようになります。
3. **cons トレーニングを最小化ts**:代理店のトレーニングが少ないほど、より良い結果が得られます。Cons トレーニング tは、できるだけエージェント主導の実験を解放しながら、ビジネスルールを尊重するように設計する必要があります。

## 次のステップ

重要な設計上の決定が下されたら、次の手順に進みます。

- [エージェントを起動する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)