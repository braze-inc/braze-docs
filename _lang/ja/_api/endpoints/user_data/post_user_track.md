---
nav_title: "POST:ユーザーを追跡"
article_title: "POST:ユーザーを追跡する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ユーザーを追跡」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを追跡
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}。
/users/track
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を更新します。

{% alert note %}
BrazeはAPIを通して渡されたデータを額面通りに処理し、顧客は不要なデータポイントのロギングを最小限にするために、デルタ（変化するデータ）のみを渡すべきである。続きを読むには、[データポイント]({{site.baseurl}}/user_guide/data/data_points/)を参照してください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.track` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

サーバー間の呼び出しに API を使用する顧客がファイアウォールの内側にいる場合には、`rest.iad-01.braze.com` を許可リストに登録する必要が生じることがあります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users track' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### リクエストパラメーター

{% alert important %}
以下の表に列挙されている各リクエストコンポーネントに対して、`external_id` 、`user_alias` 、`braze_id` 、`email` 、`phone` のいずれかを含める必要がある。
{% endalert %}

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | 属性オブジェクトの配列 | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください |
| `events` | オプション | イベントオブジェクトの配列 | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | オプション | 購入オブジェクトの配列 | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

### メールアドレスでユーザープロファイルを更新

`/users/track` エンドポイントを使用して、メールアドレスでユーザープロファイルを更新できます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### 電話番号でユーザープロファイルを更新する

電話番号を使用して`/users/track`エンドポイントでユーザープロファイルを更新できます。このエンドポイントは、有効な電話番号を含めた場合にのみ機能します。

{% alert important %}
`email` と`phone` の両方をリクエストに含めると、Brazeはメールを識別子として使用する。
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### サブスクリプショングループを設定する

この例では、ユーザーを作成し、ユーザー属性オブジェクト内にサブスクリプショングループを設定する方法を示します。

このエンドポイントを使用してサブスクリプションステータスを更新すると、`external_id` で指定されたユーザー (User1 など) が更新され、そのユーザー (User1) と同じメールアドレスを持つすべてのユーザーのサブスクリプションステータスも更新されます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### エイリアスのみのユーザーを作成するリクエスト例

リクエストの本文に`_update_existing_only`キーを`false`の値で設定することにより、新しいエイリアス専用ユーザーを作成するために`/users/track`エンドポイントを使用できます。この値を省略すると、Brazeはエイリアスのみのユーザープロファイルを作成しない。エイリアスのみのユーザーを使用すると、そのエイリアスを持つ1つのプロファイルが存在することが保証されます。これは、Brazeが重複したユーザープロファイルを作成するのを防ぐため、新しい統合を構築するときに特に役立つ。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## 回答

これらのAPIリクエストのいずれかを使用する場合、次の3つの一般的な応答のいずれかを受け取るはずです: [成功メッセージ](#successful-message)、[非致命的なエラーを含む成功メッセージ](#successful-message-with-non-fatal-errors)、または[致命的なエラーを含むメッセージ](#message-with-fatal-errors)。

### 成功のメッセージ

メッセージングに成功すると、次のようなレスポンシブが返ってくる：

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### 非致命的なエラーがある成功メッセージ

メッセージが成功しているが、長いイベントリストの中に1つの無効なイベントオブジェクトが含まれているなどの致命的でないエラーがある場合、次の応答が返されます:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

成功メッセージの場合、Brazeは`errors` 配列のエラーに影響されないデータを処理する。

### 致命的なエラーを含むメッセージ

メッセージに致命的なエラーがある場合、次の応答が返されます:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### 致命的なエラー応答コード

リクエストが致命的なエラーに遭遇した場合にBrazeが返すステータスコードと関連するエラーメッセージについては、[致命的エラー& レスポンスを]({{site.baseurl}}/api/errors/#fatal-errors)参照のこと。

providedexternal_id is blacklisted and disallowed "というエラーが表示された場合、リクエストに "ダミーユーザー "が含まれている可能性がある。詳細については、「[スパムのブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)」を参照してください。

## よくある質問

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 同じメールアドレスを持つ複数のプロファイルが見つかった場合はどうなりますか？
`external_id` が存在する場合、Brazeは外部IDを持つ最も最近更新されたプロファイルを優先して更新する。`external_id` が存在しない場合、Brazeは最近更新されたプロファイルを優先して更新する。

### メールアドレスのプロファイルが存在しない場合はどうなりますか？
Brazeは新しいプロファイルとEメールのみのユーザーを作成し、Eメールアドレスによるユーザープロファイルの更新リクエスト例で述べたように、Eメールフィールドをtest@braze.com に設定する。Brazeはエイリアスを作らない。

### どのようにして`/users/track`を使用してレガシーユーザーデータをインポートしますか？
まだモバイルアプリを使用していないユーザーのユーザープロファイルを生成するために、Braze APIを通じてデータを送信することができます。ユーザーがその後アプリケーションを使用する場合、SDKを使用した識別に続くすべての情報は、APIコールを使用して作成した既存のユーザープロファイルにマージされる。識別前にSDKによって匿名で記録されたユーザー行動は、既存のAPI生成ユーザープロファイルと統合された時点で失われる。

セグメンテーションツールは、アプリとのエンゲージメントの有無にかかわらず、これらのユーザーを含む。ユーザー API 経由でアップロードされたものの、アプリをまだ使用していないユーザーを除外する場合は、`Session Count > 0` フィルターを追加します。

### `/users/track`は重複イベントをどのように処理しますか？

イベント配列内の各イベントオブジェクトは、指定された時間にユーザーによるカスタムイベントの単一の発生を表します。これは、Brazeに取り込まれる各イベントに独自のイベントIDがあることを意味し、「重複」イベントは別々のユニークなイベントとして扱われるということです。

### `/users/track` は無効な階層化カスタム属性をどのように処理しますか？

ネストされたカスタム属性に無効な値(無効な時間形式やNULL値など)が含まれる場合、Brazeはリクエスト内のすべてのネストされたカスタム属性の更新を処理から除外する。これは、その特定の属性内のすべての階層化構造に適用されます。処理を成功させるには、階層化カスタム属性内のすべての値が有効であることを確認してから送信してください。

## CY24-25の月間アクティブユーザー数、ユニバーサルMAU、Web MAU、モバイルMAU  
月間アクティブユーザー数CY 24-25、ユニバーサルMAU、Web MAU、またはモバイルMAUを購入した顧客については、Brazeは`/users/track` エンドポイントで異なるレート制限を管理している：
- 1時間あたりのレート制限は、アカウントで予想されるデータ取り込みアクティビティに応じて設定されます。このアクティビティは、購入した月間アクティブユーザー数、業界、季節、またはその他の要因に対応する場合があります。
- 1 時間ごとの制限に加えて、Braze は 3 秒ごとに送信できるリクエストの数にバースト制限を適用します。
- 各リクエストは、アトリビューション、イベント、購入オブジェクトを合わせて、最大75の更新をバッチすることができる。

予想される取り込みに基づく現在の制限は、ダッシュボードの [**設定**] > [**API と識別子**] > [**API 使用状況ダッシュボード**] にあります。システムの安定性を保護するためにレート制限を変更したり、アカウントのデータスループットを向上させる場合があります。毎時または毎秒のリクエスト制限とビジネスのニーズに関する質問や懸念については、Braze Supportまたはカスタマーサクセスマネージャーにお問い合わせください。

### 月間アクティブユーザー数（CY24-25）、ユニバーサルMAU、Web MAU、モバイルMAUのレート制限ヘッダー

レート制限のない(`429` などの)すべてのレスポンスは、クライアントに時間ごとのレート制限ウィンドウの状態を示す以下のHTTPレスポンスヘッダーを含む。リクエストレートを管理するために、これらのヘッダーを使用することをお勧めする：

| ヘッダー名             | 説明                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 期間ごとに許可されるリクエスト数                                              |
| `X-RateLimit-Remaining` | ウィンドウ内に残っているおおよそのリクエスト数                                |
| `X-RateLimit-Reset`     | 現在のウィンドウがリセットされるまでの残り秒数                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

HTTP`429` エラーが発生した場合、`RateLimit-Limit` 、`RateLimit-Remaining` 、`RateLimit-Reset` ヘッダーは返されないことに注意。エラーが発生すると、これらのヘッダーは`X-Ratelimit-Retry-After` 、 リクエストを開始できるまでの秒数を示す整数を返すヘッダーで置き換えられる。

{% endapi %}
