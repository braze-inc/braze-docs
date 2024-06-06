---
nav_title: "ポスト:グローバルコントロールグループによるユーザープロファイルのエクスポート"
article_title: "ポスト:グローバルコントロールグループによるユーザープロファイルのエクスポート"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、グローバルコントロールグループのBrazeエンドポイントのユーザーのエクスポートに関する詳細について説明します。"

---
{% api %}
# グローバルコントロールグループによるユーザープロファイルのエクスポート
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> このエンドポイントを使用して、グローバルコントロールグループ内のすべてのユーザーをエクスポートします。 

ユーザーデータは、改行で区切られたユーザー JSON オブジェクトの複数のファイルとしてエクスポートされます (1 行に 1 つの JSON オブジェクトなど)。ファイルが生成されるたびに、グローバルコントロールグループのすべてのユーザーが含まれます。Brazeは、グローバルコントロールグループにユーザーが追加されたり削除されたりした履歴を保存しません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.export.global_control_group`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースの回答詳細

[[S3またはAzureの認証情報をBrazeに追加した場合][2]][1]、`segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`各ファイルは次のようなキー形式のZIPファイルとしてバケットにアップロードされます。Azure を使用している場合は、Braze の Azure **パートナー概要ページの [これをデフォルトのデータエクスポート先にする**] チェックボックスがオンになっていることを確認してください。通常、処理を最適化するために、ユーザー5,000人につき1つのファイルを作成します。大きなワークスペース内の小さなセグメントをエクスポートすると、複数のファイルが作成されることがあります。その後、必要に応じてファイルを抽出し、`json`すべてのファイルを 1 つのファイルに連結できます。`output_format`of を指定すると`gzip`、`.gz`ファイル拡張子はの代わりになります`.zip`。

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

このエンドポイントを使用するときは、独自のS3またはAzure認証情報を設定して、エクスポートに独自のバケットポリシーを適用することを強くお勧めします。クラウドストレージの認証情報を入力していない場合は、リクエストへの応答に、すべてのユーザーファイルを含むZIPをダウンロードできるURLが表示されます。この URL は、エクスポートの準備ができて初めて有効な場所になります。 

クラウドストレージの認証情報を指定しない場合、このエンドポイントからエクスポートできるデータ量に制限があることに注意してください。エクスポートするフィールドとユーザー数によっては、サイズが大きすぎるとファイル転送が失敗する場合があります。転送のサイズを小さくするために、`fields_to_export`エクスポートするフィールドを指定し、必要なフィールドのみを指定するのがベストプラクティスです。ファイルの生成でエラーが発生した場合は、ランダムなバケット番号に基づいてユーザーベースをさらにセグメントに分割することを検討してください (たとえば、ランダムバケット番号が 1,000 未満、または 1,000 ～ 2,000 のセグメントを作成します)。

どちらのシナリオでも、`callback_endpoint`オプションでエクスポートの準備が整ったときに通知するように指定できます。`callback_endpoint`が提供されている場合、ダウンロードの準備が整い次第、提供されたアドレスへの投稿リクエストを行います。投稿の本文は「成功」: true になります。クラウドストレージの認証情報をBrazeに追加していない場合、`url`投稿の本文にはダウンロードURLを値とする属性が追加されます。

ユーザーベースが大きくなると、エクスポート時間が長くなります。たとえば、ユーザー数が 2,000 万人のアプリの場合、1 時間以上かかる場合があります。

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
個々のカスタム属性はエクスポートできません。ただし、fields\_to\_export 配列 (たとえば) に custom\_attributes を含めることで、すべてのカスタム属性をエクスポートできます。`['first_name', 'email', 'custom_attributes']`
{% endalert %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --- | ----------- | --------- | ------- |
| `callback_endpoint` | オプション | 文字列 | エクスポートが可能になったときにダウンロード URL を投稿するエンドポイント。|
| `fields_to_export` | 必須* | 文字列の配列 | エクスポートするユーザーデータフィールドの名前。カスタム属性もエクスポートできます。<br><br>\* 2021 年 4 月以降、新規アカウントではエクスポートする特定のフィールドを指定する必要があります。|
| `output_format` | オプション | 文字列 | 独自の S3 バケットを使用する場合、`zip`ファイル形式をまたはとして指定できます`gzip`。デフォルトは ZIP ファイル形式です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
  "output_format" : "zip"
}'
```

## エクスポートするフィールド

以下は有効なリストです`fields_to_export`。`fields_to_export`を使用して返されるデータを最小限に抑えることで、この API エンドポイントの応答時間を改善できます。

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
| `purchase` s | 配列 | このユーザーが過去90日間に購入したもの。|
| `random_bucket` | Integer | [ユーザーのランダムなバケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。ランダムなユーザーのセグメントを均一に分散させるために使用されます。|
| `time_zone` | 文字列 | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。|
| `total_revenue` | Float | このユーザーに帰属する総収益。総収益は、ユーザーが受け取ったキャンペーンやキャンバスのコンバージョン期間中に行った購入に基づいて計算されます。|
| `uninstalled_at` | タイムスタンプ | ユーザーがアプリをアンインストールした日付と時刻。アプリがアンインストールされていない場合は省略されます。|
| `user_aliases` | オブジェクト | [`alias_name`およびを含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)（`alias_label`存在する場合）。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URL が公開されると、その有効期間は数時間です。そのため、Braze には独自の S3 認証情報を追加することを強くお勧めします。

### ユーザー・エクスポート・ファイル出力の例

ユーザーエクスポートオブジェクト (可能な限り少ないデータを含めます。オブジェクトにフィールドがない場合は、null、false、または空とみなす必要があります):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at" : (string),
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
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (string),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
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
}
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/

{% endapi %}
