---
nav_title: "ポスト:ユーザーを追跡"
article_title: "ポスト:ユーザーを追跡"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Track user Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを追跡
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベント、購入の記録、ユーザープロファイル属性の更新を行います。

{% alert note %}
BrazeはAPI経由で渡されたデータを額面通りに処理し、お客様は不要なデータポイントの消費を最小限に抑えるため、デルタ（変化するデータ）のみを渡す必要があります。詳しくは[データ]({{site.baseurl}}/user_guide/data_and_analytics/data_points/)ポイントを参照。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.track` パーミッションを持つ[API キーが]({{site.baseurl}}/api/api_key/)必要です。

サーバー間通話にAPIを使用している顧客がファイアウォールの内側にいる場合、`rest.iad-01.braze.com` 。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users track' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes" : (optional, array of attributes object),
  "events" : (optional, array of event object),
  "purchases" : (optional, array of purchase object),
}
```

### リクエストパラメータ

{% alert important %}
以下の表に列挙されている各リクエストコンポーネントに対して、`external_id` 、`user_alias` 、`braze_id` 、`email` のいずれかが必要である。
{% endalert %}

| パラメータ｜必須｜データ型｜説明
| --------- | ---------| --------- | ----------- |
|`attributes` ｜任意｜属性オブジェクトの配列｜[ユーザー属性オブジェクトを]({{site.baseurl}}/api/objects_filters/user_attributes_object/)参照。
|`events` ｜任意｜イベント・オブジェクトの配列｜[イベント・オブジェクトを]({{site.baseurl}}/api/objects_filters/event_object/)参照。
|`purchases` ｜オプション｜購入オブジェクトの配列｜[購入オブジェクトを]({{site.baseurl}}/api/objects_filters/purchase_object/)参照
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

### メールアドレスによるユーザープロファイルの更新リクエスト例

`/users/track` エンドポイントを使用すると、電子メール・アドレスによってユーザー・プロファイルを更新できます。 

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
            "integer_attribute": 25,
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

### 電話番号によるユーザープロファイルの更新リクエスト例

`/users/track` エンドポイントを使用して、電話番号別にユーザープロファイルを更新できます。このエンドポイントは、有効な電話番号が含まれている場合にのみ機能します。

{% alert important %}
Eメールと電話の両方をリクエストに含める場合、BrazeはEメールを識別子として使用します。
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
### 購読グループを設定するリクエスト例

この例では、ユーザを作成し、ユーザ属性オブジェクト内でサブスクリプショングループを設定する方法を示します。 

このエンドポイントで購読ステータスを更新すると、`external_id` で指定されたユーザー（User1 など）が更新され、そのユーザー（User1）と同じ電子メールを持つすべてのユーザーの購読ステータスが更新されます。

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
    "subscription_groups" : [{
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

### エイリアス専用ユーザーの作成リクエスト例

`/users/track` エンドポイントを使用して、リクエスト本文に`_update_existing_only` キーを`false` という値で設定することで、新しいエイリアスのみのユーザーを作成することができる。この値が省略された場合、エイリアスのみのユーザー・プロファイルは作成されません。エイリアスのみのユーザーを使用すると、そのエイリアスを持つプロファイルが1つ存在することが保証されます。これは、重複したユーザープロファイルの作成を防ぐため、新しい統合を構築する際に特に役立ちます。

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

前述のAPIリクエストのいずれかを使用すると、次の3つの一般的な応答のいずれかを受け取るはずです：[成功したメッセージ](#successful-message)、[致命的でないエラーを伴う成功したメッセージ](#successful-message-with-non-fatal-errors)、[致命的なエラーを伴うメッセージ](#message-with-fatal-errors)。

### 成功メッセージ

成功したメッセージには次のような返答がある：

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### 致命的でないエラーを含む成功メッセージ

メッセージは成功したが、致命的でないエラー、例えば、長いイベント・リストの中に無効なイベント・オブジェクトが1つでもあった場合、以下のようなレスポンスが返ってくる：

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

成功メッセージの場合、`errors` の配列でエラーの影響を受けなかったデータはそのまま処理される。 

### 致命的なエラーを含むメッセージ

メッセージに致命的なエラーがある場合、次のような応答が返されます：

```json
{
  "message" : <fatal error message>,
  "errors" : [
    {
      <fatal error message>
    }
  ]
}
```

### 致命的なエラー・レスポンス・コード

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラーと]({{site.baseurl}}/api/errors/#fatal-errors)応答を参照してください。

provided external\_id is blacklisted and disallowed "というエラーが表示された場合、リクエストに "ダミー・ユーザー "が含まれている可能性があります。 詳細については、[スパムブロックを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)参照してください。 

## よくある質問

### 同じメールアドレスを持つ複数のプロフィールが見つかった場合はどうなりますか？
`external_id` が存在する場合、外部 ID を持つ最近更新されたプロファイルが優先的に更新されます。`external_id` が存在しない場合は、最近更新されたプロフィールが優先的に更新されます。

### メールアドレスを持つプロフィールが現在存在しない場合はどうなりますか？
新しいプロフィールが作成され、Eメールのみのユーザーが作成されます。エイリアスは作成されない。メールアドレスによるユーザープロファイルの更新のリクエスト例にあるように、Eメールフィールドはtest@braze.com。

### `/users/track` 、レガシーユーザーデータをどのようにインポートしますか？
ユーザーは、ユーザープロファイルを生成するために、まだモバイルアプリを使用していないユーザーのデータをBraze APIを通じて送信することができます。ユーザーがその後アプリケーションを使用する場合、SDKを介した識別に続くすべての情報は、APIコールを介して作成された既存のユーザープロファイルにマージされます。識別前にSDKによって匿名で記録されたユーザーの行動は、既存のAPI生成ユーザープロファイルと統合された時点で失われます。

セグメンテーションツールは、アプリに関与したかどうかに関係なく、これらのユーザーを含む。ユーザーAPI経由でアップロードされたユーザーのうち、まだアプリとエンゲージしていないユーザーを除外したい場合は、`Session Count > 0` というフィルターを追加するだけです。

### `/users/track` 、重複イベントはどのように処理されるのか？

events配列の各eventオブジェクトは、指定された時間にユーザーによってカスタムイベントが1回発生したことを表す。つまり、Brazeに取り込まれる各イベントは、それぞれ独自のイベントIDを持つため、「重複する」イベントは、個別のユニークなイベントとして扱われます。

{% endapi %}
