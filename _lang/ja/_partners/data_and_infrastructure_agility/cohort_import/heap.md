---
nav_title: Heap
article_title: Heap
description: "このリファレンス記事では、BrazeとデジタルインサイトプラットフォームであるHeapとの統合について詳述しています。これにより、HeapデータをBrazeにインポートし、ユーザーコホートを作成することができるほか、BrazeデータをHeapにエクスポートしてセグメントを作成することもできます。"
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> [Heap](https://heap.io/)、デジタルインサイトプラットフォームは、ビジネスに最も影響を与えるデジタルエクスペリエンスの機会に焦点を当て、摩擦を排除し、顧客を喜ばせ、収益を加速させます。

BrazeとHeapの統合により、[HeapデータをBrazeにインポート](#data-import-integration)し、ユーザーコホートを作成することや、[BrazeデータをHeapにエクスポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/)してセグメントを作成することができます。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| ヒープアカウント | このパートナーシップを利用するには、[Heap](https://heap.io/about)アカウントが必要です。 |
| Braze データインポートキー | これは、**パートナー統合** > **テクノロジーパートナー** からBrazeダッシュボードにキャプチャして、**Heap** を選択できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。あなたのエンドポイントは、インスタンスのBraze URLに依存します。 |
| Braze Currents | BrazeからHeapにデータをエクスポートするには、アカウントで[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を有効にする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース
- 放棄されたファネルを再度利用するユーザーを再エンゲージする:ユーザーが購入またはサブスクリプションのファネルを放棄したときに、再エンゲージメントメッセージングをトリガーします。
- 試用体験をパーソナライズする：トライアル体験における摩擦点を特定し、トライアル中にユーザーを再エンゲージするための適切なタイミングでリマインダーを送信し、価値を見出す手助けをします。
- 発表とオファーに対するエンゲージメントを高める：ターゲットプロモーション、更新、および新しいサービスの発表を関連するオーディエンスに向けて行います。

## データインポート統合

HeapとBrazeの統合を使用して、Heapで定義されたコホートをBrazeに自動的に同期します。

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**パートナー統合** > **テクノロジーパートナー** に移動し、**Heap** を選択します。 

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

このページでは、データインポートキーとRESTエンドポイントを見つけることができます。これらの値の両方に注意し、それらをHeapのアカウントマネージャーに提供して、統合の設定を完了してください。

![][3]{: style="max-width:90%;"}

### ステップ2:Brazeでインポートされたユーザーをセグメント化する

Brazeで、**Segment**に移動し、HeapコホートSegmentに名前を付け、フィルターとして**Heapコホート**を選択します。ここから、含めたいHeapコホートを選択できます。HeapのコホートSegmentが作成された後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![BrazeのSegmentビルダーでは、ユーザー属性フィルター「Heapコホート」が「含む」と「Heapテストコホート」に設定されています。][2]{: style="max-width:90%;"}

### この統合を使用する

Heap Segment を使用するには、Braze キャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択します。

![Brazeのキャンペーンビルダーのターゲティングステップで、「セグメントによるターゲットユーザー」フィルターが「Heapコホート」に設定されています。][4]{: style="max-width:90%;"}

## 統合の詳細

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクタのペイロード構造と同じであり、[カスタムHTTPコネクタの例のリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
