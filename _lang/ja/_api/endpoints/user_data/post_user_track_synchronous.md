---
nav_title: "POST:ユーザーを追跡する（同期）"
article_title: "POST:ユーザーを追跡する（同期）"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "この記事では、「ユーザー同期追跡」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを追跡する（同期）
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints %}
/ユーザー/トラッキング/同期
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を同期的に更新します。このエンドポイントは、ユーザープロファイルを非同期に更新する [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)と同様に機能します。

{% alert important %}
このエンドポイントは現在ベータ版である。このベータ版への参加に興味がある場合は、Brazeのアカウントマネージャーに連絡すること。
{% endalert %}

## 同期APIコールと非同期APIコール

非同期呼び出しでは、APIはステータスコード`201` を返し、リクエストが正常に受信、理解、受諾されたことを示す。ただし、これは、リクエストが完全に完了したわけではありません。

同期呼び出しでは、APIはステータスコード`201` を返し、リクエストの受信、理解、受諾、完了に成功したことを示す。コールレスポンスは、操作の結果として、選択されたユーザープロファイル フィールドを示す。

このエンドポイントは、`/users/track` エンドポイントよりも低いレート制限を持っている（下記の[レート制限を](#rate-limit)参照）。各 `/users/track/sync` リクエストには、1つのイベントオブジェクト、1つの属性オブジェクト、**また**は1つの購入オブジェクトのみを含めることができます。このエンドポイントは、同期呼び出しが必要なユーザープロファイルの更新用に予約する必要があります。健全な実装のためには、`/users/track/sync` と`/users/track` を併用することをお勧めします。

例えば、同じユーザーに対して短時間に連続してリクエストを送信する場合、非同期の `/users/track` エンドポイントでは競合が発生する可能性がありますが、`/users/track/sync` エンドポイントでは、`2XX` レスポンスを受信した後に、それらのリクエストをそれぞれ順番に送信することができます。

## 前提条件

このエンドポイントを使用するには、`users.track.sync` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

サーバー間の呼び出しに API を使用する顧客がファイアウォールの内側にいる場合には、`rest.iad-01.braze.com` を許可リストに登録する必要が生じることがあります。

## レート制限

すべての顧客に対して、このエンドポイントに対して1分あたり500リクエストの基本スピード制限を適用します。各 `/users/track/sync` リクエストには、最大1つのイベントオブジェクト、1つの属性オブジェクト、または1つの購入オブジェクトを含めることができます。それぞれのオブジェクト (イベント、属性、および購入配列) は、それぞれ1つのユーザーを更新できます。

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### リクエストパラメーター

{% alert important %}
以下の表に列挙されている各リクエストコンポーネントに対して、`external_id` 、`user_alias` 、`braze_id` 、`email` 、`phone` のいずれかを含める必要がある。
{% endalert %}

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | つの属性オブジェクト | 「[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)」を参照 |
| `events` | オプション | イベントオブジェクト | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | オプション | 1つの購入オブジェクト | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 応答

このエンドポイントの[リクエスト・パラメーターを](#request-parameters)使用すると、次のいずれかのレスポンスを受け取るはずである：成功したメッセージ、または致命的なエラーを含むメッセージ。

### 成功のメッセージ

メッセージに成功すると、Brazeが更新したユーザープロファイル・データに関する情報を含む以下のレスポンシブが返される。

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### 致命的なエラーを含むメッセージ

メッセージに致命的なエラーがあった場合、次のような応答が返ってくる：

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

## リクエストとレスポンスの例

### 外部IDでカスタム属性を更新する

#### リクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### 応答

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Eメールでカスタムイベントを更新する

#### リクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### 応答

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### ユーザーエイリアスで購入イベントを更新する

#### リクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### 応答

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## よくある質問

### 非同期エンドポイントと同期エンドポイントのどちらを使うべきか？

ほとんどのプロファイル更新では、`/users/track` のエンドポイントが、レート制限が高く、リクエストをバッチ処理できる柔軟性があるため、最適である。ただし、`/users/track/sync` エンドポイントは、同じユーザーに対する短時間の連続するリクエストによって競合が発生している場合に便利です。

### レスポンスタイムは`/users/track` エンドポイントと異なるか？

同期呼び出しでは、APIはBrazeがリクエストを完了するまで待ってレスポンスを返す。その結果、同期リクエストは、非同期リクエストよりも平均して、`/users/track` 。大半のリクエストでは、数秒以内にレスポンスが返ってきます。

### 複数のリクエストを同時に送信できますか？

リクエストが異なるユーザーに対するものであるか、各リクエストが1人のユーザーに対して異なるアトリビュート、イベント、購入を更新する限りは、そうだ。

ユーザーに対して、同じ属性、イベント、または購入のために複数のリクエストを送信する場合、Brazeは、レースコンディションの発生を防ぐために、各リクエストの間に成功した応答を待つことを推奨する。

### なぜレスポンスの値が元のリクエストの値と一致しないのか？

リクエストは完了したが、カスタム属性の値が更新されなかった可能性がある。これは、カスタム属性の更新が最大文字数を超えている場合、配列の制限を超えている場合、またはユーザーが Braze に存在せず `_update_existing_only = true` がある場合に発生する可能性があります。

このような場合、リクエストは完了したものの、希望する更新が行われなかったことを示しているものとして応答を処理します。このような現象が起こる理由を、上記から考えてトラブルシューティングを行う。

{% endapi %}
