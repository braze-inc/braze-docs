---
nav_title: Radar
article_title:Radar
alias: /partners/radar/
description:「この参考記事では、BrazeとジオフェンシングプラットフォームであるRadarが提携して、iOSアプリとAndroidアプリに位置情報コンテキストとトラッキング, 追跡を追加する方法について概説しています。「
page_type: partner
search_tag:Partner

---

# Radar

> [Radar](https://www.onradar.com/) は、主要なジオフェンシングおよび位置トラッキング, 追跡プラットフォームです。Radar プラットフォームには次の 3 つのコア製品があります。[ジオフェンス](https://radar.io/product/geofencing)、[トリップトラッキング](https://radar.io/product/trip-tracking)、[Geo API](https://radar.io/product/api)'s industry-leading engagement platform and Radar'業界をリードするBrazeのジオフェンシング機能を組み合わせることで、ロケーションベースの幅広い製品やサービス体験を通じて収益とロイヤルティを高めることができます。これらには、集荷と配達のトラッキング, 追跡、ロケーショントリガー通知、文脈に応じた or 状況に即したパーソナライゼーション、ロケーション検証、店舗検索、住所のオートコンプリートなどが含まれます。

BrazeとRadarの統合により、高度なロケーションベースのキャンペーンントリガーや、豊富なファーストパーティロケーションデータによるユーザープロファイルエンリッチメントが可能になります。Radar ジオフェンスまたはトリップトラッキング, 追跡イベントが生成されると、カスタムイベントとユーザー属性がリアルタイムで Braze に送信されます。その後、これらのイベントと属性を使用して、ロケーションベースのキャンペーンの開始、ラストマイル集配業務の強化、車両と配送ロジスティクスの監視、ロケーションパターンに基づいたユーザーセグメントの構築を行うことができます。 

[さらに、Radar Geo APIを活用して、コネクテッドコンテンツを通じてマーケティングキャンペーンを充実させたり、パーソナライズしたりできます。]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Radar アカウント | このパートナーシップを利用するには、Radar アカウントが必要です。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| アプリ識別子 | [アプリ識別子]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)は、Braze ダッシュボードの **\[設定] > \[**API キー**]** から確認できます。 |
| iOS API キー<br>Android API キー | これらの API キーは、Braze ダッシュボードの **\[設定] > \[アプリ設定****]** にあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

Braze SDK と Radar SDK 間でデータをマッピングするには、両方のシステムで同じユーザー ID またはユーザーエイリアスを設定する必要があります。これは、Braze SDK `changeUser()` のメソッドとRadar SDK `setUserId()` のメソッドを使用して実行できます。

統合を有効にするには:

1. [インテグレーションページのRadar](https://radar.com/documentation/integrations) で Braze を探します。
1. \[**有効]** を \[**はい]** に設定します。
3. アプリ識別子と API キーを貼り付けます。

{% alert note %}
テスト環境とライブ環境に別々の API キーを設定できます。
{% endalert %}

{:start="4"}
4\.Braze エンドポイントを選択します。
5. イベントまたはイベント属性フィルタリングを入力して、関連するデータのみがエンゲージメントマーケティング用に Braze に送信されるようにします。Radar イベントが生成されるたびに、Radar はカスタムイベントとユーザー属性をBrazeに送信します。iOS デバイスからのイベントは iOS API キーを使用して送信され、Android デバイスからのイベントとユーザー属性は Android API キーを使用して送信されます。

{% alert note %}
デフォルト、ログインしているユーザーのRadar は Braze `userId` `external_id` にマップされます。ただし、Radar または設定することで、ログアウトしたユーザーを追跡したり、`metadata.brazeAlias`カスタムマッピングを指定したりできます`metadata.brazeExternalId`。設定した場合は`metadata.brazeAlias`、`radarAlias`対応するエイリアスをラベル付きの Braze にも追加する必要があります。
{% endalert %}

## イベントベースと属性ベースのユースケース

カスタムイベントとユーザー属性を使用して、ロケーションベースのセグメントを構築したり、ロケーションベースのキャンペーンをトリガーしたりできます。

### カーブサイドピックアップの店舗到着通知をトリガーする 

カーブサイドピックアップのために店舗に到着したユーザーに、到着手順を記載したプッシュ通知を送信します。

![An action-based delivery campaign showing that the campaign will be delivered when the "arrived_at_trip_destination" custom event occurs, and the "trip_metadata" equals "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})

### 最近の来店者のオーディエンスSegment を構築

たとえば、購入の有無にかかわらず、過去7日以内にストアを訪れたすべてのユーザーをターゲットにします。

![A segment where "radar_geofence_tags" includes value my_store and "radar_updated_at" was less than 7 days ago.]({% image_buster /assets/img_archive/radar-segment.png %})

## コネクテッドコンテンツ

次の例は、デジタルオファーで近くのユーザーを店舗に誘導するプロモーションを実行する方法を示しています。 

![「新しい店舗内セール、ウォルマート、お近くのターゲット」を表示するコネクテッドコンテンツプッシュメッセージのAndroid画像, 写真。][1]{: style="float:right;max-width:30%;border:0;"}

開始するには、リクエストURL内で使用するためのRadar公開可能なAPI キーを手元に用意する必要があります。

次に、`connected_content`タグ内で、[Search Places API](https://radar.io/documentation/api#search-places) に GET リクエストを行います。Search Places APIは、Radar [プレイスに基づいて近くの場所を返します。レーダープレイスは](https://radar.io/documentation/places)、世界の包括的なビューを提供する場所、チェーン、カテゴリの位置のデータベースです。

次のコードスニペットは、Radar が API 呼び出しから JSON オブジェクトとして返す内容の例です。

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

接続コンテンツをターゲットにしてパーソナライズされた Braze メッセージを作成するには、Braze `most_recent_location` 属性を API リクエストの URL `near` のパラメータの入力として活用できます。`most_recent_location`属性はRadar イベントインテグレーションを介して収集されるか、Braze SDKから直接収集されます。

次の例では、Radar チェーンフィルタリングが Target と Walmart のロケーションに適用され、近くのロケーションの検索半径が 2 km に設定されています。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

`connect_content`タグからわかるように、JSON オブジェクトは URL `nearbyplaces` `:save nearbyplaces` の後に追加することでローカル変数に格納されます。
{% raw %}`{{nearbyplaces.places}}`{% endraw%}参照することで、出力がどうあるべきかをテストできます。

ユースケースをまとめると、キャンペーン構文は次のようになります。次のコードでは、`nearbyplaces.places`オブジェクトを繰り返し処理して一意の値を抽出し、その値を人間が読める適切な区切り文字でメッセージ用に連結します。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
コネクテッドコンテンツで利用できるすべての Radar API については、Radar [のドキュメントをご覧ください](https://radar.io/documentation/api)。
{% endalert %}

[1]: {% image_buster /assets/img/radar_example.png %}