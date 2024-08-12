---
nav_title: "ポスト:識別子によるユーザプロファイルのエクスポート"
article_title: "ポスト:識別子によるユーザプロファイルのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、識別子Braze エンドポイントによるエクスポートユーザの詳細について説明します。"

---
{% api %}
# 識別子によるユーザープロファイルのエクスポート
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> このエンドポイントを使用して、ユーザー識別子を指定して、任意のユーザープロファイルからデータをエクスポートします。 

1 つのリクエストには、最大 50 個の `external_ids` または `user_aliases` を含めることができます。`device_id` または`email_address` を指定する場合は、リクエストごとにどちらか一方の識別子を含めることができます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.export.ids` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export. Defaults to all if not provided
}
```

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|-----|-----|-----|-----|
|`external_ids` | オプション| 文字列の配列| エクスポートするユーザの外部識別子。|
|`user_aliases` | オプション| ユーザーエイリアスオブジェクトの配列| [エクスポートするユーザーのユーザーエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object/)。|
|`device_id` | オプション| 文字列| デバイス識別子。`getDeviceId` などのさまざまなSDK メソッドによって返されます。|
|`braze_id` | オプション| 文字列| 特定のユーザのBraze識別子。|
|`email_address` | オプション| 文字列| ユーザーのメールアドレス|
|`phone` | オプション| [E.164](https://en.wikipedia.org/wiki/E.164) 形式| ユーザの電話番号|
|`fields_to_export` | オプション| 文字列の配列| エクスポートするユーザデータフィールドの名前。指定されていない場合は、デフォルトでall になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## エクスポートするフィールド

以下は、有効な`fields_to_export`のリストです。返されるデータを最小限に抑えるために`fields_to_export` を使用すると、このAPI エンドポイントの応答時間を短縮できます。

| エクスポートするフィールド| データ型| 説明|
|---|---|---|
| `apps` | Array | このユーザーがセッションをログに記録したアプリケーション。以下のフィールドが含まれます。<br><br>-`name`: アプリ名<br>- `platform`: iOS、Android、Web などのアプリプラットフォーム<br>- `version`:アプリのバージョン番号または名前 <br>- `sessions`: このアプリのセッションの合計数<br>- `first_used`:最初のセッションの日付<br>- `last_used`:最後のセッションの日付<br><br>すべてのフィールドは文字列です。|
| `attributed_campaign` | String | [属性積分]({{site.baseurl}}/partners/message_orchestration/attribution)からのデータ(設定されている場合)。特定の広告キャンペーンのID。|
| `attributed_source` | String | [属性積分]({{site.baseurl}}/partners/message_orchestration/attribution)からのデータ(設定されている場合)。広告が掲載されたプラットフォームの識別子。|
| `attributed_adgroup` | String | [属性積分]({{site.baseurl}}/partners/message_orchestration/attribution)からのデータ(設定されている場合)。campaign の下のオプションのサブグループの識別子。|
| `attributed_ad` | String | [属性積分]({{site.baseurl}}/partners/message_orchestration/attribution)からのデータ(設定されている場合)。campaign およびad group の下にあるオプションのサブグループのID。|
| `braze_id` | String | このユーザに対してBraze によって設定されるデバイス固有の一意のユーザ識別子。|
| `country` | String | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard を使用するユーザーの国|
| `created_at` | String | ユーザープロファイルが作成された日時(ISO 8601 形式)。|
| `custom_attributes` | Object | このユーザーのカスタム属性キーと値のペア。|
| `custom_events` | Array | 過去90 日間にこのユーザに起因するカスタムイベント。|
| `devices` | Array | ユーザーのデバイスに関する情報。プラットフォームに応じて、次の情報が含まれます。<br><br>`model`デバイスのモデル名<br>`os`デバイスのオペレーティングシステム<br>`carrier`デバイスのサービスキャリア(利用可能な場合)<br>- `idfv`: (iOS) Brazeデバイス識別子、ベンダーのアップル識別子(存在する場合)<br>- `idfa`: (iOS) Advertising の識別子(存在する場合)<br>`device_id`(Android) Brazeデバイス識別子<br>`google_ad_id`(Android) Google Play Advertising Identifier(存在する場合)<br>`roku_ad_id`(六)六広告識別子<br>`ad_tracking_enabled`デバイスで広告追跡が有効になっている場合、true またはfalse | を指定できます。
| `dob` | String | ユーザの生年月日`YYYY-MM-DD`.|
| `email` | 文字列| ユーザーの電子メールアドレス|
| `external_id` | 文字列| 識別されたユーザの一意のユーザ識別子。|
| `first_name` | String | ユーザーのファーストネーム|
| `gender` | String | ユーザーの性別。可能な値は次のとおりです。<br><br>-`M`: 男性<br>-`F`: 女性<br>-`O`: その他<br>-`N`: 該当なし<br>-`P`: 言いたくない<br>-`nil`: 不明 |
| `home_city` | String | ユーザのホームシティ。|
| `language` | String | ISO-639-1 規格のユーザー言語|
| `last_coordinates` | 浮動小数点の配列| ユーザの最新のデバイスの場所。`[longitude, latitude]` としてフォーマットされます。|
| `last_name` | String | ユーザの姓|
| `phone` | 文字列| E.164 形式のユーザの電話番号|
| `purchases` | Array | このユーザが過去90 日間に行った購入。|
| `push_tokens` | Array | アプリの通知の送信先を指定する一意の匿名識別子。|
| `random_bucket` | Integer | User's [乱数バケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)、ランダムユーザの均一に分散されたセグメントを作成するために使用されます。|
| `time_zone` | String | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。|
| `total_revenue` | Float | このユーザに帰属する総収益。総収益は、ユーザーが受領したキャンペーンおよびキャンバスの変換ウィンドウで行った購入に基づいて計算されます。|
| `uninstalled_at` | Timestamp | ユーザーがアプリをアンインストールする日時。アプリがアンインストールされていない場合は省略。|
| `user_aliases` | Object | [`alias_name` および`alias_label` (存在する場合) を含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

`/users/export/ids` エンドポイントは、受信したすべてのキャンペーンやキャンバス、実行されたすべてのカスタムイベント、作成されたすべての購入、すべてのカスタム属性などのデータを含む、このユーザのユーザプロファイル全体をまとめることに注意してください。その結果、このエンドポイントは他のREST API エンドポイントよりも低速になります。

要求されたデータによっては、このAPI エンドポイントは、1 分あたり2500 件のリクエストのレート制限により、ニーズを満たすのに十分でない場合があります。このエンドポイントを定期的に使用してユーザをエクスポートすることを想定している場合は、セグメント別にユーザをエクスポートすることを検討してください。セグメントは非同期であり、データプルが大きくなるように最適化されています。

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

このエンドポイント経由でアクセス可能なデータの例については、次の例を参照してください。

### サンプルユーザーエクスポートファイルの出力

ユーザエクスポートオブジェクト(可能な限り最小のデータを含みます。フィールドがオブジェクトから欠落している場合は、null、false、または空であると見なされます):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" : 
         {
           "opened_email" : (bool),
           "opened_push" : (bool),
           "clicked_email" : (bool),
           "clicked_triggered_in_app_message" : (bool)
          },
          "converted" : (bool),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, bool) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (bool),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes": 
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged": 
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted": 
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
