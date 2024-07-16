---
nav_title: Tealium for Currents
article_title:カレント用Tealium
page_order:3
alias: /partners/tealium_for_currents/
description:"この参考記事では、Braze Currentsと、マーケティングスタック内のソース間で情報を収集・ルーティングする顧客データプラットフォームであるTealiumとのパートナーシップについて概説している。"
page_type: partner
tool:Currents
search_tag:Partner

---

# Tealium for Currents

> [Tealiumは](https://www.tealium.com)顧客データプラットフォームであり、複数のデータソースから情報を収集し、マーケティングスタックのさまざまな場所にルーティングする。

BrazeとTealiumの統合により、2つのシステム間の情報の流れをシームレスにコントロールすることができる。Currentsを使えば、データをTealiumに接続して、成長スタック全体でアクション可能にすることもできる。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealium EventStream or Tealium AudienceStream | このパートナーシップを利用するには、[Tealiumアカウントが](https://my.tealiumiq.com/)必要である。 |
| Currents | データをTealiumにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
| Tealium URL | これらは、Tealiumダッシュボードに移動し、インジェストURLをコピーすることで取得できる。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Tealium内にBrazeのデータソースを作成する。

データソースの作成方法は、[Tealiumの](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/)サイトに掲載されている。完了すると、TealiumはコピーするデータソースURLを提供するので、次のステップでそれを使用する。

### ステップ2:カレントを作成する

Brazeで、**Currents > + Create Currents > Tealium Exportに**移動する。統合名、連絡先メール、Tealium URLを記入する。次に、利用可能なイベントのリストから追跡したいものを選択する。最後に、**Launch Currentsを**クリックする。

Tealiumに送信されるすべてのイベントには、ユーザーの`external_user_id` 。現時点では、Brazeは、`external_user_id` を設定していないユーザーのイベントデータをTealiumに送信しない。

{% alert important %}
's important to keep your Tealium URL up to date. If your connector'のURLが正しくない場合、Brazeはイベントを送信できない。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

## 統合の詳細

Brazeは、[Currentsイベント用語集に]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)記載されているすべてのデータ（[メッセージエンゲージメントイベントと]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) [顧客行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)イベントの両方のすべてのプロパティを含む）のTealiumへのエクスポートをサポートしています。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じで、[カスタムHTTPコネクターのサンプルリポジトリで](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)見ることができる。