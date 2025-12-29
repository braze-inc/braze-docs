---
nav_title: Tealium for Currents
article_title: Tealium for Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "この参考記事では、Braze Currentsと、マーケティング・スタックのソース間で情報を収集し、ルーティングする顧客データ・プラットフォームであるTealiumとのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium for Currents

> [Tealium](https://www.tealium.com) は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォームです。

BrazeとTealiumの統合により、2つのシステム間の情報の流れをシームレスにコントロールすることができる。Currents では、データを Tealium に接続し、グローススタック全体で実用的なデータにすることもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealium EventStream or Tealium AudienceStream | このパートナーシップを活用するには、[Tealium アカウント](https://my.tealiumiq.com/)が必要です。 |
| Currents | Tealium にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
| Tealium URL | これは、Tealium のダッシュボードに移動し、取り込み URL をコピーすることで取得できます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Tealium内にBraze用のデータソースを作成する。

データソースを作成する手順は、[Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/) サイトにあります。完了すると、Tealium からデータソース URL が提供されます。この URL をコピーして、次のステップで使用します。

### ステップ2:Current を作成する

Braze で **[Currents] > [+ Currents を作成] > [Tealium のエクスポート]** に移動します。統合名、連絡先メール、および Tealium URL を指定します。次に、利用可能なイベントのリストから追跡するイベントを選択します。最後に [**Currents を起動**] をクリックします。

Tealium に送信されるすべてのイベントには、ユーザーの `external_user_id` が含まれます。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータをTealiumに送信しない。

{% alert important %}
Tealium URL を最新の状態に保つことが重要です。コネクタのURLが正しくない場合、Brazeはイベントを送信できない。これが**5 日** 以上続く場合、コネクタのイベントはドロップされ、データは永続的に失われます。
{% endalert %}

## 統合の詳細

Braze では、「[Currents イベント用語集]({{site.baseurl}}/user_guide/data/braze_currents/)」にリストされているすべてのデータ ([メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)イベントおよび[顧客行動]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)イベントのすべてのプロパティを含む) を Tealium にエクスポートできます。

エクスポートされたデータのペイロードの構造は、カスタム HTTP コネクターのペイロード構造と同じです。これは、[カスタム HTTP コネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。
