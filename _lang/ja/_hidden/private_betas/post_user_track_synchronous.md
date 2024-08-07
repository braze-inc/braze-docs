---
nav_title: "ポストだ：ユーザーを追跡する（同期）"
article_title: "ポストだ：ユーザーを追跡する（同期）"
hidden: true
permalink: /post_user_track_synchronous/
layout: api_page
page_type: reference
description: "この記事では、同期TrackユーザーBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# ユーザーを追跡する（同期）
APIMETHOD POST CORE_ENDPOINT| {% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> このエンドポイントを使用して、カスタム・イベントや購入を記録し、ユーザー・プロファイル属性を同期的に更新する。このエンドポイントは、非同期でユーザープロファイルを更新する[`/users/track` エンド]({{site.baseurl}}/api/endpoints/user_data/post_user_track)ポイントと同様の機能を持つ。

{% alert important %}
このエンドポイントは現在ベータ版である。このベータ版への参加に興味がある場合は、Brazeのアカウントマネージャーに連絡すること。
{% endalert %}

## 同期APIコールと非同期APIコール

非同期呼び出しでは、APIはステータスコード`201` を返し、リクエストが正常に受信、理解、受け入れられたことを示す。しかし、これはあなたの要請が完全に完了したことを意味するものではない。

同期呼び出しでは、APIはステータスコード`201` を返し、リクエストが正常に受信され、理解され、受け入れられ、完了したことを示す。コールレスポンスには、操作の結果として、選択されたユーザープロファイルの フィールドが表示される。

このエンドポイントは、`/users/track` エンドポイントよりも低いレート制限を持っている（下記の[レート制限を](#rate-limit)参照）。各`/users/track/sync` リクエストは、1つのイベント・オブジェクト、1つのアトリビュート・オブジェ クト**、または**1つの購買オブジェクトのみを含むことができる。このエンドポイントは、同期呼び出しが必要なユーザープロファイル更新のために予約されるべきである。健全な導入のためには、`/users/track/sync` と`/users/track` を併用することをお勧めする。

例えば、同じユーザーに対して短時間に連続してリクエストを送信する場合、非同期の`/users/track` エンドポイントではレースコンディションが発生する可能性があるが、`/users/track/sync` エンドポイントでは、`2XX` レスポンスを受信した後に、それらのリクエストを順番に送信することができる。

## 前提条件

このエンドポイントを使うには、`users.track.sync` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/api_key/)必要だ。

サーバー間通話にAPIを使用している顧客は、ファイアウォールの内側にいる場合、`rest.iad-01.braze.com` 。

## レート制限

このエンドポイントには、すべての顧客に対して、1分あたり500リクエストという基本速度制限が適用される。`/users/track/sync` 各リクエストは、最大1つのイベントオブジェクト、1つのアトリビュートオブジェクト、または1つの購買オブジェクトを含むことができる。各オブジェクト（イベント、アトリビュート、購入アレイ）は、それぞれ1人のユーザーを更新することができる。

## Request body

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
以下の表に列挙されている各リクエストコンポーネントには、`external_id` 、`user_alias` 、`braze_id` 、`email` 、`phone` のいずれかが必要である。
{% endalert %}

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | つの属性オブジェクト | [ユーザー属性オブジェクトを]({{site.baseurl}}/api/objects_filters/user_attributes_object/)参照のこと[。]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | オプション | イベントオブジェクト | [イベント・オブジェクトを]({{site.baseurl}}/api/objects_filters/event_object/)見る |
| `purchases` | オプション | 購入対象は1つ | [購入対象を]({{site.baseurl}}/api/objects_filters/purchase_object/)見る |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 回答

このエンドポイントの[リクエスト・パラメーターを](#request-parameters)使用すると、次のいずれかのレスポンスを受け取るはずである：成功したメッセージ、または致命的なエラーを含むメッセージ。

### 成功のメッセージ

成功したメッセージは、更新されたユーザー・プロファイル・データに関する情報を含む、以下のレスポンスを返す。

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
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

ほとんどのプロファイル更新には、`/users/track` エンドポイントが最も適している。しかし、`/users/track/sync` エンドポイントは、同じユーザーに対する連続したリクエストが急激に発生し、レースコンディションが発生している場合に便利である。

### レスポンスタイムは`/users/track` エンドポイントと異なるか？

同期呼び出しでは、APIはリクエストが完了するまで応答を返すのを待つ。その結果、同期リクエストは、非同期リクエストよりも平均して`/users/track` に時間がかかる。リクエストの大半は、数秒以内に返信される。

### 複数のリクエストを同時に送ることは可能か？

リクエストが異なるユーザーに対するものであるか、各リクエストが1人のユーザーに対して異なるアトリビュート、イベント、購入を更新する限りは、そうだ。

ユーザーに対して、同じ属性、イベント、または購入のために複数のリクエストを送信する場合、Brazeは、レースコンディションの発生を防ぐために、各リクエストの間に成功した応答を待つことを推奨する。

### なぜレスポンスの値が元のリクエストの値と一致しないのか？

リクエストは完了したが、カスタム属性の値が更新されなかった可能性がある。これは、カスタム属性の更新が最大文字数を超える場合、配列の制限を超える場合、またはユーザーがBrazeに存在せず、`_update_existing_only = true` 。

このような場合、リクエストは完了したものの、希望する更新が行われなかったことを示す応答として扱う。このような現象が起こる理由を、上記から考えてトラブルシューティングを行う。

{% endapi %}
