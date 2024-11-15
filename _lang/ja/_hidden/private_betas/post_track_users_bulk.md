---
nav_title: "POST:ユーザーをトラッキング(一括)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "この記事では、Track users (bulk) エンドポイントの詳細について概説する。"
---

{% api %}
# ユーザーをトラッキング(一括)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントや購入を記録し、ユーザープロファイル属性を一括更新する。

{% alert important %}
このエンドポイントは現在ベータ版である。ベータ版への参加に興味がある場合は、Brazeのアカウント・マネージャーに連絡を。
{% endalert %}

## このエンドポイントを使用する場合

[POSTに似ている：Track users エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites) 、このエンドポイントを使用してユーザープロファイルを更新できる。しかし、このエンドポイントは一括更新に適している：

- **もっと大きなリクエストもある：**このエンドポイントでは、1回のリクエストで10,000ユーザーを受け入れることができるため、一括更新のニーズを達成するために少ないリクエスト数で済むことになる。
- **優先順位をつける：**トラフィックのピーク時には、`/users/track` からのリクエストは、`/users/track/bulk` からのリクエストよりも優先される。両方のエンドポイントを使用することで、データの取り込みをよりコントロールすることができる。

このエンドポイントへのユーザー更新は、アクションベースのキャンペーンやアクションベースのキャンバスのトリガーにはならず、例外イベントのトリガーにもならず、コンバージョンメトリクスのトラッキングにもならないことに注意すること。このエンドポイントへのユーザー更新は、セグメンテーションとパーソナライゼーションのために利用できる。

オンボーディング中に多くのユーザープロファイルをバックフィルする場合や、デイリーシンクの一環として大量のユーザープロファイルを同期する場合に、このエンドポイントを使用することを検討する。

## 前提条件

このエンドポイントを使用するには、`users.track.bulk` 権限を持つ API キーが必要だ。

サーバー間通話にAPIを使用している場合、ファイアウォールの内側にいる場合は、エンドポイント（例えば、`rest.iad-01.braze.com` ）をallowlistする必要があるかもしれない。詳細は[インスタンスごとのエンド]({{site.baseurl}}/api/basics#endpoints)ポイントを参照のこと。

## レート制限

このエンドポイントには、すべての顧客に対して、毎秒5リクエストの基本速度制限が適用される。

各`/users/sync/bulk` リクエストのペイロードの上限は4MBで、最大10,000のイベント、アトリビューション、または購入オブジェクトを含むことができる。

各オブジェクト（イベント、アトリビューション、購入アレイ）は、それぞれ1人のユーザーを更新することができる。つまり、1回のリクエストで最大10,000人の異なるユーザーを更新することができる。ひとつのユーザープロファイルは、1回のリクエストで最大100オブジェクトまで更新できる。

{% alert note %}
レート制限の引き上げが必要な場合は、カスタマー・サクセス・マネージャーに連絡すること。
{% endalert %}


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
次のテーブルに記載されている各リクエストコンポーネントには、`external_id`、`user_alias`、`braze_id`、`email`、または `phone` のいずれかが必要です。
{% endalert %}

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | 属性オブジェクトの配列 | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください |
| `events` | オプション | イベントオブジェクトの配列 | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | オプション | 購入オブジェクトの配列 | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

### 1回のリクエストで10,000ユーザープロファイルを一括更新

ユーザープロファイルは最大10,000まで更新できる。リクエストは10,000の属性オブジェクトで構成されている：

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

以下は、リクエストが属性オブジェクトとイベントオブジェクトの両方で構成されている例である：

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
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
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

## 回答

### 成功したメッセージ

成功したメッセージには次の応答が返されます:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### 非致命的なエラーがある成功メッセージ

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

#### 致命的なエラー応答コード

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラーと]({{site.baseurl}}/api/errors/#fatal-errors)レスポンスを参照のこと。

`provided external_id is blacklisted and disallowed` というエラーが表示された場合、リクエストに "ダミーユーザー "が含まれている可能性がある。詳細については、「[スパムのブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)」を参照してください。

## よくある質問

### このエンドポイントを使うべきか、それとも通常の`/users/track` を使うべきか？

両方使うことをお勧めする。

アクションベースのキャンペーンやキャンバス、コンバージョントラッキング、例外イベントのトリガーが不要な大規模なユーザープロファイルのバックフィルや同期には、`/users/track/bulk` を使用する。 

リアルタイムのユースケースでは、`/users/track` エンドポイントを使用する。

### で使用できる識別子は？users/track/bulk?

`external_id` 、`braze_id` 、`user_alias` 、`email` 、`phone` のいずれかが必要である。詳しい例については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)、[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)、[購入オブジェクトの]({{site.baseurl}}/api/objects_filters/purchase_object/)ドキュメントを参照されたい。 

### 属性、イベント、購入を1つのリクエストに含めることはできるか？

はい。アトリビューション、イベント、購入オブジェクトは、リクエストごとに最大10,000オブジェクトまで、いくらでもリクエストを作成することができる。


{% endapi %}
