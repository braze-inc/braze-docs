---
nav_title: "POST:識別子によるユーザープロファイルのエクスポート"
article_title: "POST:識別子によるユーザプロファイルのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「識別子ごとにユーザーをエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 識別子によるユーザープロファイルのエクスポート
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> このエンドポイントを使用して、ユーザー識別子を指定して任意のユーザープロファイルからデータをエクスポートします。

1 つのリクエストには、最大 50 個の `external_ids` または `user_aliases` を含めることができます。`device_id` 、`email_address` 、`phone` のいずれかを指定したい場合は、リクエストごとにこれらの識別子を1つだけ含めることができる。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`users.export.ids`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Request body

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
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
2024年8月22日以降に Braze にオンボーディングした顧客については、リクエストパラメータ`fields_to_export` が必要です。
{% endalert %}

## リクエストパラメーター

| パラメーター          | required | データ型                                                     | 説明                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | オプション | 文字列の配列                                              | エクスポートするユーザーの外部識別子s。                                              |
| `user_aliases`     | オプション | ユーザー別名オブジェクトの配列                                    | エクスポートするユーザーの[ユーザーエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object/)。 |
| `device_id`        | オプション | 文字列                                                        | `getDeviceId` などのさまざまな SDK メソッドによって返されるデバイス識別子。                 |
| `braze_id`         | オプション | 文字列                                                        | 特定のユーザーのBraze 識別子。                                                      |
| `email_address`    | オプション | 文字列                                                        | ユーザーのメールアドレス。                                                                       |
| `phone`            | オプション | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号。                                                                        |
| `fields_to_export` | オプション* | 文字列の配列                                              | エクスポートするユーザーデータ フィールドの名前。<br><br>\*このフィールドは、毎秒40リクエストという高速レート制限を使用するために必要である。省略された場合、250リクエスト/分のデフォルトレート制限が代わりに使われる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*2024年8月22日以降にBrazeにオンボーディングした顧客が対象。

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

以下は、有効な`fields_to_export`のリストです。`fields_to_export` を使用して返されるデータを最小限に抑えると、このAPI エンドポイントのレスポンスタイムが向上します。

| エクスポートするフィールド       | データタイプ       | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | 配列           | このユーザーがセッションを記録したアプリケーション。これには次のフィールドが含まれます。<br><br>-`name`: アプリ名<br>- `platform`: アプリ プラットフォーム(iOS、Android、またはWeb など)<br>- `version`:アプリのバージョン番号または名前 <br>-`sessions`: このアプリの総セッション数<br>-`first_used`: 初回セッションの日付<br>-`last_used`: 最終セッションの日付<br><br>すべてのフィールドsはストリングです。                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。特定の広告キャンペーンのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。広告が表示されたプラットフォームのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。キャンペーン の下のオプションのサブグループのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。キャンペーンと広告グループの下にある任意のサブグループの識別子。                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | string          | ユーザーのプッシュ通知の購読ステータス。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | string          | ユーザーのメールサブスクリプションステータス。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | 文字列          | このユーザーにBrazeで設定されたデバイス固有の一意のユーザー 識別子。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | 文字列          | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 標準を使用するユーザーの国。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | 文字列          | ユーザープロファイルが作成された日時 (ISO 8601形式)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | オブジェクト          | このユーザーのカスタム属性キーと値のペア。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | 配列           | 過去 90 日間にこのユーザーに帰属するカスタム イベント。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | 配列           | ユーザーのデバイスに関する情報。プラットフォームに応じて、次の情報が含まれます。<br><br>- `model`:デバイスのモデル名<br>- `os`:装置のオペレーティングシステム<br>- `carrier`:デバイスのサービスキャリア (利用可能な場合)<br>- `idfv`: (iOS) Braze デバイス識別子、ベンダーの Apple 識別子 (存在する場合)<br>- `idfa`: (iOS) Advertising の識別子(存在する場合)<br>- `device_id`:(Android)Braze機器識別子<br>- `google_ad_id`:(Android)グーグルプレイ広告識別子(存在する場合)<br>- `roku_ad_id`:(Roku） Roku 広告識別子<br>- `ad_tracking_enabled`:デバイスで広告"トラッキングが有効になっている場合、真または偽になることがあります |
| `dob`                 | 文字列          | `YYYY-MM-DD` 形式のユーザーの生年月日。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | 文字列          | ユーザーのメールアドレス。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | 文字列          | 識別されたユーザー固有のユーザー識別子。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | 文字列          | ユーザーの名。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | 文字列          | ユーザーの性別。可能な値は次のとおりです。<br><br>-`M`: 男性<br>-`F`: 女性<br>-`O`: その他<br>-`N`: 該当なし<br>-`P`: 言いたくない<br>- `nil`:不明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | 文字列          | ユーザーの所在地。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | 文字列          | ISO-639-1 規格のユーザー言語。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | 浮動小数点の配列 | `[longitude, latitude]` としてフォーマットされたユーザーの最新のデバイスの場所。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | 文字列          | ユーザの姓。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | 文字列          | E.164 形式のユーザーの電話番号。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | 配列           | このユーザーは過去90日間に購入しました。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | 配列           | アプリの通知の送信先を指定する一意の匿名識別子。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | 整数         | ユーザーの[乱数バケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。乱数ユーザーsの一様分布Segmentsを作成するために使用されます。                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | 文字列          | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | フロート           | このユーザーに帰属する総収益。総収益は、受領したキャンペーンおよびキャンバスのコンバージョン期間中に行われたユーザーの購入に基づいて計算されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | タイムスタンプ       | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | オブジェクト          | [`alias_name` および`alias_label` を含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) (存在する場合)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

`/users/export/ids` エンドポイントは、受信したすべてのキャンペーンやキャンバス、実行されたすべてのカスタムイベント、作成されたすべての購入、すべてのカスタム属性などのデータを含む、このユーザーのユーザープロファイル全体をまとめることに注意してください。このため、このエンドポイントは他の REST API エンドポイントよりも低速になります。

要求されたデータによっては、この API エンドポイントでは1分あたり 250 件のリクエストのレート制限があるため、ニーズを満たすには不十分な場合があります。このエンドポイントを定期的に使用してユーザーをエクスポートすることを想定している場合は、代わりに、非同期で大規模なデータプルに最適化されているセグメント別にユーザーをエクスポートすることを検討してください。

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

このエンドポイントからアクセスできるデータの例については、次の例を参照してください。

### サンプルユーザーのエクスポートファイルアウトプット

ユーザーエクスポートオブジェクト (できるだけ少ないデータを含めます。オブジェクトにフィールドがない場合は、null または空であると見なされます):

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
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
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
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
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
        "in_control": (boolean),
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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
