---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "このリファレンス記事では、位置情報と\"トラッキングをiOSとAndroid アプリsに追加するために、ジオフェンシングプラットフォームであるBrazeとRadarの提携について概説します。"
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) は、先頭のジオフェンシングと位置"トラッキング プラットフォームです。Radar プラットフォームには3つの主力商品があります。[Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking), and [Geo APIs](https://radar.io/product/api).Brazeの業界をリードするエンゲージメント プラットフォームとRadarの業界をリードするジオフェンシング機能を組み合わせることで、ロケーションベースの幅広い商品・サービス体験を通じて収益とロイヤルティを牽引することができます。これには、集配"トラッキング、場所-トリガーの通知s、文脈に応じた or 状況に即した パーソナライゼーション、場所の確認、店舗のロケーター、住所の自動完了などが含まれます。

BrazeとRadarの統合により、高度なロケーションベースのキャンペーン トリガーと、豊富なファーストパーティロケーションデータを使用したユーザープロファイルエンリッチメントにアクセスできます。Radar ジオフェンスまたはトリップ"トラッキングが生成されると、カスタムイベントs およびユーザー 属性s がリアルタイムでBrazeに送信されます。これらの事象および属性sは、次いで、位置に基づくキャンペーンsをトリガーし、ラストマイルのピックアップおよび配送オペレーションを駆動し、フリートおよび配送物流を監視し、または位置パターンに基づいてユーザー Segmentsを構築するために使用することができる。 

さらに、Radar Geo API を活用して、[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) を通じてマーケティング キャンペーンを強化またはパーソナライズできます。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Radar勘定 | この提携の前進タグeを考慮するには、Radarな考慮が必要である。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| アプリ識別子 | [アプリ 識別子]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) は、**設定**> **API Keys** のBraze ダッシュボード内にあります。 |
| iOS API キー<br>Android API キー | これらのAPI キーsは、**設定**>**アプリ設定**のBraze ダッシュボード内にあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

Braze とRadar SDK s の間でデータマッピングを行うには、両方のシステムで同じユーザー ID s またはユーザー別名を設定する必要があります。これは、Braze SDKの`changeUser()` メソッドとRadar SDKの`setUserId()` メソッドを使用して実行できます。

統合を有効にするには:

1. [Integrations](https://radar.com/documentation/integrations) ページのRadarで、Braze を見つけます。
1. **Enabled**を**Yes**に設定します。
3. アプリ 識別子とAPI キーs に貼り付けます。

{% alert note %}
試験環境とライブ環境に別々のAPI キーs を設定できます。
{% endalert %}

{:start="4"}
4\.Braze エンドポイントを選択します。
5. イベントまたはイベント属性 フィルターを入力して、関連するデータのみがエンゲージメント マーケティングのためにBraze に送信されるようにします。Radar事象が発生するたびに、Radarはカスタムイベントsとユーザー 属性sをBrazeに送信する。iOS デバイスからのイベントはiOS API キー s を使用して送信され、Android デバイスからのイベントおよびユーザー 属性 s はAndroid API キー s を使用して送信されます。

{% alert note %}
デフォルトでは、Radar`userId` は、ログインしているユーザーs のBraze`external_id` にマップされます。ただし、ログアウトしたユーザーs を追跡したり、設定 Radar`metadata.brazeAlias` または`metadata.brazeExternalId` でカスタムm アプリ ings を指定したりできます。`metadata.brazeAlias` を設定した場合は、ラベル`radarAlias` のBrazeにも一致する別名を追加する必要があります。
{% endalert %}

## イベントベースおよび属性ベースのユースケース

カスタムイベント s およびユーザー 属性 s を使用して、ロケーションベースのSegments またはトリガーのロケーションベースのキャンペーンs を構築できます。

### カーブサイドピックアップの店舗到着通知のトリガ 

カーブサイドピックアップのためにあなたのお店に到着した時、到着指示のあるプッシュ通知をユーザーに送ってください。

!["arrived_at_trip_送信先"カスタムイベントが発生し、"trip_metadata"equals "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})が発生したときにキャンペーンが配信されることを示すアクションベースの配信キャンペーン

### 最近の来店者オーディエンス Segmentの構築

たとえば、購買の有無にかかわらず、過去7日間にあなたの店舗を訪問したユーザーを対象にします。

!["radar_ジオフェンス_タグ s" value my_store と"radar_更新 d_at" が7 日前より少ないSegment。]({% image_buster /assets/img_archive/radar-segment.png %})

## コネクテッドコンテンツ

次に、ディジタルオファーで近くのユーザー s 店内をドライブするプロモーションを実行する例を示します。 

!["New In Store Deals, Walmart, target near you"を表示するConnected ContentプッシュメッセージのAndroid "画像。][1]{: style="float:right;max-width:30%;border:0;"}

開始するには、リクエストURL 内で使用するために、Radarの公開可能なAPI キーを手元に用意する必要があります。

次に、`connected_content` タグ内で、[ Search Places API](https://radar.io/documentation/api#search-places) へのGET リクエストを行います。検索では、[ Radar Places](https://radar.io/documentation/places): ワールドの包括的なビューを提供するプレイス、チェーン、およびカテゴリのロケーションのデータベースに基づいて、API が近くのロケーションを返します。

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

Connected Content ターゲットおよびパーソナライズされた Braze メッセージを作成するには、Braze`most_recent_location` 属性をAPI リクエストのURL の`near` パラメータの入力として活用できます。`most_recent_location` 属性は、RadarイベントインテグレーションまたはBraze SDKを介して収集されます。

次の例題では、Radarチェーンフィルターのing はTarget とWalmart のロケーションではアプリになり、近くのロケーションの検索範囲は2km に設定されています。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

`connect_content` タグからわかるように、JSON オブジェクトはURL の後に`:save nearbyplaces` を追加することで、ローカル変数`nearbyplaces` に保存されます。
出力内容をテストするには、{% raw %}`{{nearbyplaces.places}}`{% endraw%} を参照します。

ユースケースをまとめると、キャンペーンのシンタックスがどのように見えるかがわかります。以下のコードは、`nearbyplaces.places` オブジェクトを反復処理し、一意の値を抽出し、メッセージの適切な人間が読める区切り文字で連結します。

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

[1]: {% image_buster /assets/img/radar_example.png %}