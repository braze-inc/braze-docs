---
nav_title: エージェントの設計
article_title: エージェントの設計
page_order: 3
description: "AI意思決定サービスチームと共に、Decisioning Studioプロエージェントの設計方法を学ぶ。対象オーディエンスの定義、成功指標、およびディメンションを含む。"
---

# エージェントの設計

> エージェント設定の第一ステップは、AI意思決定サービスチームと協力してエージェントを設計することだ。この記事では、主要な設計上の決定事項と、オーディエンスを定義する方法について説明する。

意思決定エージェントに関する基礎概念（成功指標、次元、アクションバンク、制約など）については、『[意思決定エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)』を参照のこと。

## 主要な設計上の決定事項

AI意思決定サービスチームと協力して、以下の決定を行うことになる：

| 決定 | 説明 | 例 |
|----------|-------------|----------|
| **成功指標** | カスタマーエンゲージメントをパーソナライズする際、エージェントは何を最大化するのか？ | 収益、生涯価値、ARPU、コンバージョン、リテンション |
| **オーディエンス** | Decisioning Studioのエージェントは、誰に対してカスタマーエンゲージメントの決定を行うのか？ | すべての顧客、ロイヤルティ会員、リスクのあるサブスクライバー |
| **実験グループ** | Decisioning Studioの無作為化比較試験はどのように設計すべきか？ | Decisioning Studio、ランダムコントロール、通常業務、ホールドアウト |
| **ディメンション** | エージェントはどの決定をパーソナライズすべきか？ | 時間帯、件名、頻度、オファー、チャネル |
| **options** | エージェントにはどんな選択肢があるのか？ | 特定のテンプレート、オファー、時間枠 |
| **制約** | エージェントが*決して*下すべきでない決定とは何か？ | 地理的制限、予算制限、適格性ルール |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

これらの決定のそれぞれが、エージェントがどれだけ追加的な向上を生み出せるか、そしてどれだけ速く実現できるかに影響を及ぼす。当社のAI意思決定サービスチームは、貴社のビジネスルールを全て遵守しつつ、最大の価値を生み出すエージェントを設計するため、貴社と協力する。

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## オーディエンスを定義する

ユースケースのオーディエンスは通常、カスタマーエンゲージメントプラットフォーム（BrazeやSalesforce Marketing Cloudなど）で定義され、その後Decisioning Studioエージェントに送信される。その後、エージェントは顧客を治療群に分け、無作為化比較試験を実施する。

### 治療群

| グループ | 説明 |
|-------|-------------|
| **Decisioning Studio** | AIによって最適化された推薦を受け取る顧客 |
| **ランダムコントロール** | ランダムに選択されたオプションを受け取る顧客（ベースライン比較） |
| **従来通りの業務（任意）** | 現在のマーケティング・ジャーニーを受け取る顧客（既存のパフォーマンスとの比較用） |
| **保留（任意）** | 連絡を受け取らない顧客（キャンペーン全体の効果を測定するため） |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### オーディエンスを設定する

{% tabs %}
{% tab Braze %}

**Brazeでオーディエンスを設定する：**

1. ターゲットにしたいオーディエンス向けのセグメントを作成する。
2. セグメントIDをAI意思決定サービスチームに提供せよ。

{% alert note %}
Brazeでは、複数のセグメントを取り込み、それらを組み合わせてオーディエンスを作成できる。Decisioning Studioは、通常業務比較キャンペーンのセグメントを取り込むことができる。これらのパターンはすべて許容される。
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Salesforce Marketing Cloudでオーディエンスを設定する：**

1. オーディエンス向けにSFMCデータ拡張機能を設定し、データ拡張IDを提供する
2. Decisioning Studioが要求する適切な権限で、API統合用のSFMCインストール済みパッケージを設定する。
3. このデータ拡張機能は毎日更新されるようにする。Decisioning Studioは利用可能な最新の増分データを取得するからだ。

拡張機能IDとAPI キーをBrazeサービスチームに提供せよ。彼らは顧客データの取り込みにおける次のステップを支援する。

{% endtab %}
{% tab Klaviyo %}

**Klaviyoでオーディエンスを定義する：**

1. オーディエンスセグメントを作成する
2. プライベートAPI キーを生成し、これをBraze AI Decisioningチームに提供する。
3. セグメントIDとAPI キーをBrazeサービスチームに提供せよ

これらのステップの詳細については、[Klaviyoのドキュメント](https://help.klaviyo.com/hc/en-us/articles/115005237908)を参照せよ。

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

もしオーディエンスが現在Braze、SFMC、またはKlaviyoに保存されていない場合、次に取るべき最善のステップは、BrazeがコントロールするGoogle Cloud Servicesのバケットへ直接オートメーションでエクスポートを設定することだ。

これが可能かどうかを判断するには、使用しているマーテクプラットフォームのドキュメントを参照せよ。例えば、mParticleは[Google Cloud Storageとのネイティブ統合](https://www.mparticle.com/integration/google-cloud-storage/)を提供している。その場合、オーディエンスデータをエクスポートするためのGCSバケットを提供できる。

以下に類似のページがある：
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [アドビ エクスペリエンス プラットフォーム](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## プロ向け機能

Decisioning Studio ProはAI意思決定の全機能を提供する：

| 能力 | 詳細 |
|------------|---------|
| **いかなる成功指標も** | 収益、コンバージョン、ARPU、生涯価値、あるいはあらゆるビジネスKPIを最適化する |
| **無限の次元** | オファー、チャネル、タイミング、頻度、クリエイティブなど、あらゆる要素でパーソナライゼーションを行う |
| **任意のCEP** | Braze、SFMC、Klaviyoとのネイティブ連携に加え、あらゆるプラットフォーム向けのカスタム連携 |
| **AI意思決定サービス** | Brazeのデータサイエンスチームによる専任サポート |
| **高度な実験計画法** | 完全にカスタマイズ可能な治療群と保留群 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## ベストプラクティス

Decisioning Studioエージェント設計におけるベストプラクティスをいくつか挙げる：

1. **データの豊かさを最大限に高める**：エージェントが顧客について持っている情報が多ければ多いほど、彼らのパフォーマンスは向上する。
2. **アクションを多様化する**：エージェントが取れるアクションの選択肢が多様であればあるほど、各ユーザーに対してパーソナライズされた戦略を適用できる。
3. **制約を最小限に抑える**。エージェントに対する制約は少ないほど良い。制約は、ビジネスルールを尊重しつつ、可能な限りエージェント主導の実験を自由にするように設計すべきだ。

## 次のステップ

主要な設計上の決定がなされ次第、ローンチに進むことができる。

- [エージェントを起動せよ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)