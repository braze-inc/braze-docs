---
nav_title: "ポスト:セグメント別にユーザープロファイルをエクスポート"
article_title: "ポスト:セグメント別にユーザープロファイルをエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、セグメント別にユーザーをエクスポートする Braze エンドポイントの詳細について説明します。"

---
{% api %}
# セグメント別にユーザープロファイルをエクスポート
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> このエンドポイントを使用して、セグメント内のすべてのユーザーをエクスポートします。 

{% alert important %}
2021 年 12 月から、この API について以下が変更されました。<br><br>1\.この API `fields_to_export` **リクエストのフィールドは必須です**。すべてのフィールドをデフォルトにするオプションは削除されました。<br>2\.`custom_events`、、`purchases`、のフィールドには`campaigns_received`、過去 90 `canvases_received` 日間のデータのみが含まれます。
{% endalert %}

ユーザーデータは、改行で区切られたユーザー JSON オブジェクトの複数のファイルとしてエクスポートされます (1 行に 1 つの JSON オブジェクトなど)。データは自動的に生成されたURLにエクスポートされるか、この統合がすでに設定されている場合はS3バケットにエクスポートされます。

企業がこのエンドポイントを使用して一度に実行できるエクスポートは、セグメントごとに最大 1 回であることに注意してください。エクスポートが完了するのを待ってから、やり直してください。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.export.segment`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースの回答詳細

[S3][1]、[Azure][2]、または [Google クラウドストレージの認証情報を][3] Braze に追加した場合、`segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`各ファイルは次のようなキー形式の ZIP ファイルとしてバケットにアップロードされます。Azure を使用している場合は、Braze の Azure **パートナー概要ページの [これをデフォルトのデータエクスポート先にする**] チェックボックスがオンになっていることを確認してください。通常、処理を最適化するために、ユーザー5,000人につき1つのファイルを作成します。大きなワークスペース内の小さなセグメントをエクスポートすると、複数のファイルが作成されることがあります。その後、必要に応じてファイルを抽出し、`json`すべてのファイルを 1 つのファイルに連結できます。`output_format`of を指定すると`gzip`、`.gz`ファイル拡張子はの代わりになります`.zip`。

{% details Export pathing breakdown for ZIP %}
**ZIP フォーマット:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**郵便番号の例:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| プロパティ | 詳細 | 例では次のようになります。
|---|---|
| `bucket-name` | バケット名に基づいて修正されました。| `braze.docs.bucket` |
| `segment-export` | 修正されました。`segment-export`
| `SEGMENT_ID` | エクスポートリクエストに含まれています。| `abc56c0c-rd4a-pb0a-870pdf4db07q` |
`YYYY-MM-dd`| | 成功したコールバックを受信した日付 | | `2019-04-25`
| `RANDOM_UUID` | リクエスト時に Braze によって生成されたランダムな UUID。| | `d9696570-dfb7-45ae-baa2-25e302r2da27`
| `TIMESTAMP_WHEN_EXPORT_STARTED` | UTC でエクスポートがリクエストされた Unix 時間 (2017 年から 01:00:00:00 Z までの秒数)。| `1556044807`
| `filename` | ファイルごとにランダム。| `114f0226319130e1a4770f2602b5639a` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% enddetails %}

このエンドポイントを使用するときは、独自のS3またはAzure認証情報を設定して、エクスポートに独自のバケットポリシーを適用することを強くお勧めします。クラウドストレージの認証情報がない場合は、リクエストへの応答に、すべてのユーザーファイルを含むZIPファイルをダウンロードできるURLが表示されます。この URL は、エクスポートの準備ができて初めて有効な場所になります。 

クラウドストレージの認証情報を提供しない場合、このエンドポイントからエクスポートできるデータ量に制限があることに注意してください。エクスポートするフィールドとユーザー数によっては、サイズが大きすぎるとファイル転送が失敗する場合があります。ベストプラクティスは、`fields_to_export`どのフィールドを使用してエクスポートするかを指定し、転送のサイズを小さく抑えるために必要なフィールドのみを指定することです。ファイルの生成でエラーが発生した場合は、ランダムなバケット番号に基づいてユーザーベースをさらにセグメントに分割することを検討してください (たとえば、ランダムなバケット番号が 1,000 未満、または 1,000 ～ 2,000 のセグメントを作成します)。

どちらのシナリオでも、`callback_endpoint`オプションでエクスポートの準備が整ったときに通知するように指定できます。`callback_endpoint`が提供されている場合、ダウンロードの準備が整い次第、提供されたアドレスへの投稿リクエストを行います。投稿の本文は「成功」: true になります。BrazeにS3認証情報を追加していない場合、`url`投稿の本文にはダウンロードURLを値とする属性が追加されます。

ユーザーベースが大きくなると、エクスポート時間が長くなります。たとえば、ユーザー数が 2,000 万人のアプリの場合、1 時間以上かかる場合があります。

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. *Beginning April 2021, new accounts must specify specific fields to export.
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `segment_id` | 必須 | 文字列 | エクスポートするセグメントの識別子。[セグメント識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。<br><br>`segment_id`特定のセグメントのは、Braze アカウントの [API キーページから確認するか]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)、[セグメントリストエンドポイントを使用できます]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)。|
| `callback_endpoint` | オプション | 文字列 | エクスポートが可能になったときにダウンロード URL を投稿するエンドポイント。|
| `fields_to_export` | 必須* | 文字列の配列 | エクスポートするユーザーデータフィールドの名前。`custom_attributes`このパラメータに含めることで、すべてのカスタムアトリビュートをエクスポートすることもできます。<br><br>\* 2021 年 4 月以降、新規アカウントではエクスポートする特定のフィールドを指定する必要があります。|
| `custom_attributes_to_export` | オプション | 文字列の配列 | エクスポートする特定のカスタム属性の名前。最大 500 のカスタム属性をエクスポートできます。ダッシュボードでカスタム属性を作成して管理するには、**[データ設定] > [****カスタム属性**] に移動します。|
| `output_format` | オプション | 文字列 | ファイルの出力形式。`zip`デフォルトはファイルフォーマットです。独自の S3 バケットを使用している場合は、`zip`またはを指定できます`gzip`。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`fields_to_export`をパラメータに含めると`custom_attributes`、何が入っているかに関係なく、すべてのカスタムアトリビュートがエクスポートされます`custom_attributes_to_export`。特定の属性をエクスポートすることが目的の場合は、`custom_attributes``fields_to_export`パラメータに含めないでください。代わりに、`custom_attributes_to_export`パラメーターを使用してください。
{% endalert %}

## すべてのカスタム属性をエクスポートするリクエストの例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## 特定のカスタム属性をエクスポートするリクエストの例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
}'
```

## エクスポートするフィールド

以下は有効なリストです`fields_to_export`。`fields_to_export`を使用して返されるデータを最小限に抑えると、この API エンドポイントの応答時間を短縮できます。

| エクスポートするフィールド | データ型 | 説明 |
|---|---|---|
| `apps` | Array | このユーザーがセッションをログに記録したアプリ。これには次のフィールドが含まれます。<br><br>-`name`: アプリ名<br>-`platform`: iOS、Android、ウェブなどのアプリプラットフォーム<br>-`version`: アプリのバージョン番号または名前 <br>-`sessions`: このアプリの合計セッション数<br>-`first_used`: 最初のセッションの日付<br>-`last_used`: 最終セッションの日付<br><br>すべてのフィールドは文字列です。|
| `attributed_campaign` | 文字列 | [アトリビューション統合からのデータ]({{site.baseurl}}/partners/message_orchestration/attribution)（設定されている場合）特定の広告キャンペーンの識別子。|
| `attributed_source` | 文字列 | [アトリビューション統合からのデータ]({{site.baseurl}}/partners/message_orchestration/attribution)（設定されている場合）広告が掲載されたプラットフォームの識別子。|
| `attributed_adgroup` | 文字列 | [アトリビューション統合からのデータ]({{site.baseurl}}/partners/message_orchestration/attribution)（設定されている場合）キャンペーンの下にあるオプションのサブグループの識別子。|
| `attributed_ad` | 文字列 | [アトリビューション統合からのデータ]({{site.baseurl}}/partners/message_orchestration/attribution)（設定されている場合）キャンペーンと広告グループの下にあるオプションのサブグループの識別子。|
| `braze_id` | 文字列 | Braze がこのユーザーに設定したデバイス固有のユーザー識別子。|
| `country` | 文字列 | [ISO 3166-1アルファ2標準を使用するユーザーの国](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)。|
| `created_at` | 文字列 | ユーザープロファイルが作成された日付と時刻（ISO 8601形式）。|
| `custom_attributes` | オブジェクト | このユーザーのカスタム属性キーと値のペア。| |
| `custom_events` | 配列 | 過去 90 日間にこのユーザーに発生したカスタムイベント。|
| `devices` | Array | ユーザーのデバイスに関する情報。プラットフォームによっては以下が含まれる場合があります。<br><br>`model`デバイスのモデル名<br>`os`デバイスのオペレーティングシステム<br>`carrier`デバイスのサービスキャリア (利用可能な場合)<br>-`idfv`: (iOS) Braze デバイス識別子、ベンダー用の Apple 識別子 (存在する場合)<br>-`idfa`: (iOS) 広告の識別子 (存在する場合)<br>`device_id`(アンドロイド) Braze デバイス識別子<br>`google_ad_id`(Android) Google Play 広告識別子 (存在する場合)<br>`roku_ad_id`(ロク) ロク広告識別子<br>`ad_tracking_enabled`デバイスで広告トラッキングが有効になっている場合は、true または false を指定できます。|
| `dob` | 文字列 | 形式でのユーザーの生年月日`YYYY-MM-DD`。|
| `email` | 文字列 | ユーザーのメールアドレス。|
| `external_id` | 文字列 | 識別されたユーザーの一意のユーザー識別子。|
| `first_name` | 文字列 | ユーザーの名。|
| `gender` | 文字列 | ユーザーの性別。指定できる値は次のとおりです。<br><br>-`M`: 男性<br>-`F`: 女性<br>-`O`: その他<br>-`N`: 該当なし<br>-`P`: 言いたくない<br>-`nil`: 不明 |
| `home_city` | 文字列 | ユーザーの出身地。|
| `language` | 文字列 | ISO-639-1 標準におけるユーザーの言語。|
| `last_coordinates` | 浮動小数点数の配列 | ユーザーの最新のデバイス位置をとしてフォーマットします。`[longitude, latitude]`|
| `last_name` | 文字列 | ユーザーの姓。|
| `phone` | 文字列 | E.164形式のユーザーの電話番号。|
| `purchases` | 配列 | このユーザーが過去 90 日間に購入したもの。|
| `push_tokens` | 配列 | ユーザーのプッシュトークンに関する情報。|
| `random_bucket` | Integer | [ユーザーのランダムなバケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。ランダムなユーザーのセグメントを均一に分散させるために使用されます。|
| `time_zone` | 文字列 | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。|
| `total_revenue` | Float | このユーザーに帰属する総収益。総収益は、ユーザーが受け取ったキャンペーンやキャンバスのコンバージョン期間中に行った購入に基づいて計算されます。|
| `uninstalled_at` | タイムスタンプ | ユーザーがアプリをアンインストールした日付と時刻。アプリがアンインストールされていない場合は省略されます。|
| `user_aliases` | オブジェクト | [`alias_name`およびを含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)（`alias_label`存在する場合）。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 重要な注意事項

- `custom_events`、、`purchases``campaigns_received`、`canvases_received`のフィールドには、過去 90 日間のデータのみが含まれます。
- `custom_events``purchases``first`とには両方におよびのフィールドが含まれます`count`。これらのフィールドは両方とも過去の情報を反映し、過去 90 日間のデータだけに限定されません。たとえば、特定のユーザーが90日前に初めてイベントを行った場合、これはフィールドに正確に反映され、`first``count`フィールドには過去90日より前に発生したイベントも考慮されます。
- 企業がエンドポイントレベルで実行できるセグメントの同時エクスポート数は 100 に制限されています。この制限を超える試行はエラーになります。
- 最初のエクスポートジョブの実行中にセグメントをもう一度エクスポートしようとすると、429 エラーが発生します。

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URL が公開されると、その有効期間は数時間です。そのため、Braze には独自の S3 認証情報を追加することを強くお勧めします。

## ユーザー・エクスポート・ファイル出力の例

ユーザーエクスポートオブジェクト (可能な限り少ないデータを含めます。オブジェクトにフィールドがない場合は、null、false、または空とみなす必要があります):

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
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}
