---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "このリファレンス記事では、Braze と Radar のパートナーシップについて説明します。Radar は、位置情報コンテキストとトラッキングを iOS アプリと Android アプリに追加するためのジオフェンシングプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) は、業界をリードするジオフェンシングおよび位置情報追跡プラットフォームです。Radar プラットフォームには3つの主力商品があります。[Geofences](https://radar.io/product/geofencing)、[Trip Tracking](https://radar.io/product/trip-tracking)、および [Geo APIs](https://radar.io/product/api)。Braze の業界屈指のエンゲージメントプラットフォームと Radar の業界をリードするジオフェンシング機能を組み合わせることで、ロケーションベースの幅広い商品/サービスエクスペリエンスを通じて収益とロイヤルティを向上させることができます。これには、集荷と配送の追跡、ロケーショントリガー通知、コンテキストパーソナライゼーション、ロケーション検証、ストアロケーター、住所オートコンプリートなどが含まれます。

_この統合は Radar によって管理されます。_

## 統合について

BrazeとRadarの統合により、高度なロケーションベースのキャンペーン トリガーと、豊富なファーストパーティロケーションデータを使用したユーザープロファイルエンリッチメントにアクセスできます。Radar のジオフェンスまたは移動追跡イベントが生成されると、カスタムイベントとユーザー属性がリアルタイムで Braze に送信されます。これらの事象および属性sは、次いで、位置に基づくキャンペーンsをトリガーし、ラストマイルのピックアップおよび配送オペレーションを駆動し、フリートおよび配送物流を監視し、または位置パターンに基づいてユーザー Segmentsを構築するために使用することができる。 

さらに、Radar Geo API を活用して、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)を介してマーケティングキャンペーンを強化・パーソナライズできます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Radar アカウント | このパートナーシップを活用するには、Radar アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| アプリ識別子 | [アプリ識別子]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)は、Braze ダッシュボードの [**設定**] > [**API キー**] で確認できます。 |
| iOS API キー<br>Android API キー | これらのAPI キーsは、**設定**>**アプリ設定**のBraze ダッシュボード内にあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

Braze SDK と Radar SDK 間でデータをマッピングするには、両方のシステムで同じユーザー ID またはユーザーエイリアスを設定する必要があります。これは、Braze SDK の`changeUser()` メソッドと、Radar SDK の`setUserId()` メソッドを使用して実行できます。

統合を有効にするには:

1. Radar の [[Integrations](https://radar.com/documentation/integrations)] ページで Braze を見つけます。
1. **Enabled**を**Yes**に設定します。
3. アプリ 識別子とAPI キーs に貼り付けます。

{% alert note %}
試験環境とライブ環境に別々のAPI キーs を設定できます。
{% endalert %}

{:start="4"}
4\.Braze エンドポイントを選択します。
5. イベントまたはイベント属性フィルタリングを入力して、関連データのみがエンゲージメントマーケティングのために Braze に送信されるようにします。Radar イベントが生成されるたびに、Radar からカスタムイベントとユーザー属性が Braze に送信されます。iOS デバイスからのイベントは iOS API キーを使用して送信され、Android デバイスからのイベントおよびユーザー属性は Android API キーを使用して送信されます。

{% alert note %}
デフォルトでは、ログインユーザーの Radar `userId` は Braze の `external_id` にマッピングされます。ただし、ログアウトしたユーザーを追跡すること、Radar の `metadata.brazeAlias` または `metadata.brazeExternalId` を設定してカスタムマッピングを指定することはできます。`metadata.brazeAlias` を設定した場合は、Braze でラベル `radarAlias` を使用して一致エイリアスを追加する必要もあります。
{% endalert %}

## イベントベースおよび属性ベースのユースケース

カスタムイベントとユーザー属性を使用して、ロケーションベースのセグメントを作成し、ロケーションベースのキャンペーンをトリガーすることができます。

### カーブサイドピックアップの店舗到着通知のトリガ 

ユーザーがカーブサイドピックアップのために店舗に到着したときに、到着の手順を案内するプッシュ通知を送信します。

![「arrived_at_trip_destination」カスタムイベントが発生し、「trip_metadata"equals "curbside」が「curbside」の場合にキャンペーンが配信されることを示すアクションベースの配信キャンペーン。]({% image_buster /assets/img_archive/radar-campaign.png %})

### 最近の来店者のオーディエンスセグメントを作成する

たとえば、購買の有無にかかわらず、過去7日間にあなたの店舗を訪問したユーザーを対象にします。

![「radar_geofence_tags」に値 my_store が含まれており、「radar_updated_at」が過去7日以内のセグメント。]({% image_buster /assets/img_archive/radar-segment.png %})

## コネクテッドコンテンツ

次の例は、デジタルオファーを使用して近くにいるユーザーを店舗に引き付けるプロモーションを実行する方法を示しています。 

![「New In Store Deals, Walmart and target near you」というコネクテッドコンテンツプッシュメッセージが表示された Android の画像。]{% image_buster /assets/img/radar_example.png %}{: style="float:right;max-width:30%;border:0;"}

開始するには、リクエスト URL 内で使用するために、Radar が公開可能な API キーを手元に用意しておく必要があります。

次に、`connected_content` タグ内で、[ Search Places API](https://radar.io/documentation/api#search-places) へのGET リクエストを行います。Search Places API は、[Radar Places](https://radar.io/documentation/places) (場所の位置情報、チェーン、カテゴリを収録しており、全世界の包括的なビューを提供する:データベース) に基づいて付近の位置情報を返します。

以下のコード スニペットは、API 呼び出しからJSON オブジェクトとしてRadarが返す例です。

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

コネクテッドコンテンツのターゲットを絞りパーソナライズされた Braze メッセージを作成するには、Braze の `most_recent_location` 属性を API リクエスト URL の`near` パラメーターの入力として使用できます。`most_recent_location` 属性は、Radar イベント統合から収集されるか、または Braze SDK を介して直接収集されます。

次の例題では、Radarチェーンフィルターのing はTarget とWalmart のロケーションではアプリになり、近くのロケーションの検索範囲は2km に設定されています。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

`connect_content` タグからわかるように、JSON オブジェクトはURL の後に`:save nearbyplaces` を追加することで、ローカル変数`nearbyplaces` に保存されます。
出力内容をテストするには、{% raw %}`{{nearbyplaces.places}}`{% endraw%} を参照します。

ユースケースをまとめると、キャンペーンのシンタックスがどのように見えるかがわかります。以下のコードは、`nearbyplaces.places` オブジェクトを反復処理し、一意の値を抽出し、それらの値を可読可能な区切り文字で連結してメッセージにします。

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
接続コンテンツで活用できるすべてのRadar API の[Radar ドキュメント](https://radar.io/documentation/api) を参照してください。
{% endalert %}


