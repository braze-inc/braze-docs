---
nav_title: Heap
article_title:Heap
description:「この参考記事では、BrazeとデジタルインサイトプラットフォームであるHeapの統合について詳しく説明しています。これにより、ヒープデータをBrazeにインポートしたり、ユーザーコホートを作成したり、BrazeデータをHeapにエクスポートしてセグメントを作成したりできます。「
alias: /partners/heap/
page_type: partner
search_tag:Partner

---

# Heap

> [デジタルインサイトプラットフォームであるHeapは](https://heap.io/)、ビジネスに最も影響を与えるデジタルエクスペリエンススの機会に焦点を当て、摩擦を排除し、顧客を喜ばせ、収益を加速させます。

Braze と Heap の統合により、[Heap データを Braze にインポートしたり](#data-import-integration)、ユーザーコホートを作成したり、[Braze データを Heap にエクスポートしてセグメントを作成したりできます]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/)。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ヒープアカウント | このパートナーシップを利用するには、[ヒープアカウントが必要です](https://heap.io/about)。 |
| Braze データインポートキー | **これは Braze ダッシュボードの \[**パートナーインテグレーション] > \[**テクノロジーパートナー****] からキャプチャし、\[ヒープ] を選択できます。** |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| Braze Currents | Braze から Heap にデータをエクスポートするには、アカウントで [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を有効にする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース
- ファネルを放棄したユーザーを再エンゲージする:ユーザーが購入またはサブスクリプションファネルを放棄したときに、エンゲージメントメッセージングトリガーします。
- トライアル体験をカスタマイズ:トライアル体験における摩擦点を特定し、適切なタイミングでリマインダーを送信して、トライアル中にユーザーに再度働きかけ、価値を引き出せるようにします。
- お知らせやオファーへのエンゲージメントを高めましょう。関連するオーディエンスに向けたプロモーション、アップデート、新サービスの告知を行います。

## データインポート統合

Heap to Braze インテグレーションを使用すると、Heap で定義されたコホートを Braze に自動的に同期できます。

### ステップ1:Braze データインポートキーを取得

**Braze で、\[**パートナー統合**] > \[**テクノロジーパートナー**] に移動し、\[ヒープ] を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

このページでは、データインポートキーと REST エンドポイント。これら両方の値を書き留めておき、Heap アカウントマネージャーに伝えてインテグレーション設定を完了してください。

![][3]{: style="max-width:90%;"}

### ステップ2:Braze にインポートされたユーザーをセグメント化

Braze で \[Segment] に移動し、**ヒープコホートセグメントに名前を付け**、フィルターとして \[**ヒープコホート**] を選択します。ここから、どのヒープコホートを含めるかを選択できます。ヒープコホートSegment を作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。

![Braze Segment ビルダーでは、ユーザー属性フィルター「ヒープコホート」が「含む」と「ヒープテストコホート」に設定されています。][2]{: style="max-width:90%;"}

### このインテグレーションを使用する

ヒープSegment を使用するには、Braze キャンペーンまたは Canvas を作成し、そのSegment をターゲットオーディエンスとして選択します。

![Braze キャンペーンビルダーのターゲティングステップでは、「Segment 別にユーザーをターゲットにする」フィルターが「ヒープコホート」に設定されています。][4]{: style="max-width:90%;"}

## インテグレーション詳細

エクスポートされたデータのペイロード構造は、カスタム HTTP コネクタのペイロード構造と同じです。カスタム HTTP [コネクタのサンプルリポジトリで確認できます](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
