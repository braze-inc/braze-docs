---
nav_title: Heap
article_title: Heap
description: "このリファレンス記事では、Braze と Heap の統合について詳しく説明します。Heap はデジタルインサイトプラットフォームであり、Heap データを Braze にインポートしたり、ユーザーコホートを作成したり、Braze データを Heap にエクスポートしてセグメントを作成したりできます。"
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> [Heap](https://heap.io/) はデジタルインサイトプラットフォームであり、デジタルエクスペリエンスにおいてビジネスに最も大きく影響する機会に集中して取り組むことができるようにし、フリクションを解消し、顧客を楽しませ、収益創出を加速させます。

Braze と Heap の統合により、[Heap データをBraze にインポート](#data-import-integration)し、ユーザーコホートを作成し、[Braze データを Heap にエクスポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/)してセグメントを作成することができます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Heap アカウント | このパートナーシップを利用するには、[Heap](https://heap.io/about)アカウントが必要です。 |
| Braze データインポートキー | これは、Braze ダッシュボードの [**パートナー連携**] > [**テクノロジーパートナー**] からキャプチャされます。その後 [**Heap**] を選択します。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| Braze Currents | BrazeからHeapにデータをエクスポートするには、アカウントで[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を有効にする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース
- 放棄されたファネルを再度利用するユーザーを再エンゲージする:ユーザーが購入またはサブスクリプションのファネルを放棄したときに、再エンゲージメントメッセージングをトリガーします。
- 試用体験をパーソナライズする：トライアル体験における摩擦点を特定し、トライアル中にユーザーを再エンゲージするための適切なタイミングでリマインダーを送信し、価値を見出す手助けをします。
- 発表とオファーに対するエンゲージメントを高める：プロモーション、アップデート、および新しいサービス発表のターゲットを、関連性のあるオーディエンスに設定します。

## データインポート統合

Heap と Braze の統合を使用して、Heap で定義されたコホートを Braze に自動的に同期します。

### ステップ1:Braze データインポートキーを取得する

Brazeで [**パートナー連携**] >[**テクノロジーパートナー**] に移動し、[**Heap**] を選択します。 

このページでは、データインポートキーとRESTエンドポイントを見つけることができます。統合の設定を完了するため、これらの両方の値をメモして Heap アカウントマネージャーに提出します。

![][3]{: style="max-width:90%;"}

### ステップ2:Brazeでインポートされたユーザーをセグメント化する

Braze で [**セグメント**] に移動し、Heap コホートセグメントに名前を付け、フィルターとして [**セグメントコホート**] を選択します。ここから、どの Heap コホートを含めるかを選択できます。Heap のコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成するときにこのセグメントをオーディエンスフィルターとして選択できます。

![Braze セグメントビルダーで、ユーザー属性フィルター「Heap cohort」が「次を含む」と「Heap Test Cohort」に設定されている。][2]{: style="max-width:90%;"}

### この統合を使う

Heap セグメントを使用するには、Braze キャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択します。

![Braze キャンペーンビルダーのターゲティングステップで、[セグメントを基準にユーザーをターゲットに設定] フィルターが「Heap cohort」に設定されている。][4]{: style="max-width:90%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

## 統合の詳細

エクスポートされたデータのペイロードの構造は、カスタム HTTP コネクターのペイロード構造と同じです。これは、[カスタム HTTP コネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
