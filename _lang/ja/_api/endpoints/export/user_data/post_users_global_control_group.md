---
nav_title: "POST:世界コントロールグループ別輸出ユーザープロファイル"
article_title: "POST:グローバルコントロールグループ別にユーザープロファイルをエクスポートする"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「グローバルコントロールグループでのユーザーのエキスポート」Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# グローバルコントロールグループ別にユーザープロファイルをエクスポートする
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> このエンドポイントを使用して、グローバルコントロールグループ内のすべてのユーザーをエクスポートする。

ユーザーデータは、新しい行で区切られたユーザーのJSONオブジェクトの複数のファイルとしてエクスポートされます(1行に1つのJSONオブジェクトなど)。ファイルが生成されるたびに、グローバルコントロールグループの全ユーザーが含まれます。Brazeは、ユーザーがいつグローバルコントロールグループに追加され、削除されたかの履歴を保存しない。

グローバルコントロールグループのSegment 識別子を確認するには、[API 識別子タイプ]({{site.baseurl}}/api/identifier_types/?tab=segments#segment-identifier)を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`users.export.global_control_group`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースの応答の詳細

[S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3)または[Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/)認証情報sを、それぞれの**Technology Partners**ページからBrazeするように追加した場合、それぞれのファイルは`segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`のような鍵形式でZIPファイルとしてバケットにアップロードされます。Azure を使用している場合は、Braze の Azure パートナーの概要ページで、[**これをデフォルトのデータエクスポート先にする**] チェックボックスがオンになっていることを確認します。

一般的に、5000 ユーザー s ごとに1 つのファイルを作成し、プロセッシングを最適化します。大きなワークスペース内で小さなセグメントをエクスポートすると、複数のファイルが生成される場合があります。その後、ファイルを抽出し、必要に応じてすべての`json` ファイルを1 つのファイルに連結できます。`output_format` の`gzip` を指定すると、ファイル拡張子は`.zip` ではなく`.gz` になります。

{% details Export pathing breakdown for ZIP %}
**ZIP 形式:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**ZIP の例:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| プロパティ                        | 詳細                                                                              | 例に示す                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | バケット名に基づいて修正されました。                                                     | `braze.docs.bucket`                    |
| `segment-export`                | 固定。                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | エクスポートリクエストに含まれます。                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | コールバックが正常に受信された日付。                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | リクエスト時にBrazeによって生成されるランダムUUID。                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | UTC でエクスポートが要求された Unix 時間 (2017-01-01:00:00:00Z からの秒数)。 | `1556044807`                           |
| `filename`                      | ファイルごとにランダム。                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

このエンドポイントを使用してエクスポートで独自のバケットポリシーを適用する場合は、独自のS3 またはAzure 認証情報s を設定することを強くお勧めします(**Partner Integrations** > **Technology Partners** > partner page)。

![Azure のテクノロジーパートナーページ。Amazon S3 のタブ付き。]({% image_buster /assets/img/technology_partners_page.png %})

クラウドストレージの認証情報が提供されていない場合、リクエストに対するレスポンスは、すべてのユーザーファイルを含むZIPをダウンロードできるURLを提供する。URL は、エクスポートの準備ができた後でのみ有効な場所になります。

クラウドストレージの認証情報を提供しない場合、このエンドポイントからエクスポートできるデータ量には制限があることに注意しよう。エクスポートするフィールドやユーザーの個数によっては、大きすぎるとファイル転送が失敗することがあります。ベストプラクティスは、`fields_to_export` を使ってエクスポートするフィールドを指定し、転送サイズを低く抑えるために必要なフィールドだけを指定することである。ファイルの生成でエラーが発生する場合は、ランダムなバケツ番号に基づいてユーザーベースをより多くのセグメントに分割することを検討する（たとえば、ランダムなバケツ番号が1,000未満または1,000～2,000のセグメントを作成する）。

どちらのシナリオでも、オプションで`callback_endpoint` を指定して、エクスポートの準備が整ったときに通知することができます。`callback_endpoint` が指定されている場合、ダウン読み込むの準備ができたときに、指定された住所に投稿リクエストを行います。投稿の本文は`"success":true` です。クラウドストレージ認証情報s をBraze に追加していない場合、投稿の本文には属性`url` が追加され、ダウン読み込むのURL が値になります。

ユーザー群s を大きくすると、エクスポート時間が長くなります。例えば、2,000 万人のユーザーを持つアプリの場合、1 時間以上かかることもあります。

## 要求本文:

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
個々のカスタム属性をエクスポートすることはできない。ただし、fields_to_export 配列にcustom_attributes を含めることで、すべてのカスタム属性s をエクスポートできます(たとえば、`['first_name', 'email', 'custom_attributes']`)。
{% endalert %}

## リクエストパラメーター

| パラメーター           | required  | データ型        | 説明                                                                                                                                                    |
| ------------------- | --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | オプション  | 文字列           | エクスポートが利用可能になった場合に、ダウンロード URL を投稿するエンドポイント。                                                                                               |
| `fields_to_export`  | 必須* | 文字列の配列 | エクスポートするユーザー・データ・フィールドの名前。カスタム属性をエクスポートすることもできる。<br><br>\*2021 年 4 月以降、新しいアカウントでは、エクスポートする特定のフィールドを指定する必要があります。 |
| `output_format`     | オプション  | 文字列           | 独自のS3バケットを使用する場合、ファイル形式を`zip` または`gzip` に指定できる。デフォルトはZIPファイル形式である。                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
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

以下は、有効な`fields_to_export`のリストです。`fields_to_export` を使用して返されるデータを最小限に抑えると、このAPI エンドポイントのレスポンスタイムが向上します。

| エクスポートするフィールド       | データタイプ       | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | 配列           | このユーザーがセッションを記録したアプリケーション。これには次のフィールドが含まれます。<br><br>-`name`: アプリ名<br>- `platform`: アプリ プラットフォーム(iOS、Android、またはWeb など)<br>- `version`:アプリのバージョン番号または名前 <br>-`sessions`: このアプリの総セッション数<br>-`first_used`: 初回セッションの日付<br>-`last_used`: 最終セッションの日付<br><br>すべてのフィールドsはストリングです。                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。特定の広告キャンペーンのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。広告が表示されたプラットフォームのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。キャンペーン の下のオプションのサブグループのID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | 文字列          | [アトリビューション積分]({{site.baseurl}}/partners/message_orchestration/)からのデーター(設定されている場合)。キャンペーンと広告グループの下にある任意のサブグループの識別子。                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
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
| `purchase`s           | 配列           | このユーザーは過去90日間に購入しました。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `random_bucket`       | 整数         | ユーザーの[乱数バケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。乱数ユーザーsの一様分布Segmentsを作成するために使用されます。                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | 文字列          | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | フロート           | このユーザーに帰属する総収益。総収益は、受領したキャンペーンおよびキャンバスのコンバージョン期間中に行われたユーザーの購入に基づいて計算されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | タイムスタンプ       | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | オブジェクト          | [`alias_name` および`alias_label` を含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) (存在する場合)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 応答

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that is used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URL が使用可能になった後、数時間しか有効になりません。そのため、独自のS3 認証情報をBraze に追加することを強くお勧めします。

### サンプルユーザーのエクスポートファイルアウトプット

ユーザエクスポートオブジェクト(可能な限り最小のデータを含みます。フィールドがオブジェクトから欠落している場合は、ヌルまたは空であると見なされます):

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

{% endapi %}
