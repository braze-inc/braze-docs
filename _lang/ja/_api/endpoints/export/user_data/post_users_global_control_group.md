---
nav_title: "POST:グローバルコントロールグループ別にユーザープロファイルをエクスポートする"
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

ユーザーデータは、改行で区切られたユーザーJSONオブジェクトの複数のファイルとしてエクスポートされる（1行に1つのJSONオブジェクトなど）。ファイルが生成されるたびに、グローバルコントロールグループの全ユーザーが含まれます。Brazeは、ユーザーがいつグローバルコントロールグループに追加され、削除されたかの履歴を保存しない。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.export.global_control_group` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## クレデンシャルに基づくレスポンスの詳細

[S3][1] または [Azure][2] の認証情報を Braze に追加している場合、各ファイルは `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` のようなキー形式の ZIP ファイルとしてバケットにアップロードされます。Azure を使用している場合は、Braze の Azure パートナーの概要ページで、\[**これをデフォルトのデータエクスポート先にする**] チェックボックスがオンになっていることを確認します。通常、処理を最適化するため、5,000人のユーザーにつき1ファイルを作成します。大きなワークスペース内で小さなセグメントをエクスポートすると、複数のファイルが生成される場合があります。その後、必要に応じてファイルを抽出し、すべての `json` ファイルを1つのファイルに連結できます。`output_format` に `gzip` を指定すると、ファイル拡張子は `.zip` ではなく `.gz` になります。

{% details ZIP のエクスポートパスの内訳 %}
**ZIP 形式：**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**ZIP の例：**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| プロパティ | 詳細 | 例では次のように示されています。 |
|---|---|
| `bucket-name` | バケット名に基づいて修正されます。 | `braze.docs.bucket` |
| `segment-export` | 修正済み。 | `segment-export` |
| `SEGMENT_ID` | 輸出要求に含まれる。 | `abc56c0c-rd4a-pb0a-870pdf4db07q` |
| `YYYY-MM-dd` | コールバックが正常に受信された日付。 | `2019-04-25` |
| `RANDOM_UUID` | リクエスト時にBrazeが生成したランダムなUUID。 | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | UTC でエクスポートがリクエストされた Unix 時間 (2017-01-01:00:00:00Z からの秒数)。 | `1556044807` |
| `filename` | ファイルごとにランダムです。 | `114f0226319130e1a4770f2602b5639a` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% enddetails %}

このエンドポイントを使用する際には、エクスポートに独自のバケットポリシーを適用するために、独自のS3またはAzure認証情報を設定することを強く推奨する。クラウドストレージの認証情報が提供されていない場合、リクエストに対するレスポンスは、すべてのユーザーファイルを含むZIPをダウンロードできるURLを提供する。URLが有効な場所になるのは、エクスポートの準備が整ってからだ。 

クラウドストレージの認証情報を提供しない場合、このエンドポイントからエクスポートできるデータ量には制限があることに注意しよう。エクスポートするフィールドやユーザー数によっては、ファイル転送が大きすぎると失敗することがある。ベストプラクティスは、`fields_to_export` を使ってエクスポートするフィールドを指定し、転送サイズを低く抑えるために必要なフィールドだけを指定することである。ファイルの生成でエラーが発生する場合は、ランダムなバケツ番号に基づいてユーザーベースをより多くのセグメントに分割することを検討する（たとえば、ランダムなバケツ番号が1,000未満または1,000～2,000のセグメントを作成する）。

いずれのシナリオでも、エクスポートが準備できた際に通知を受けとれるように、オプションで `callback_endpoint` を指定できます。`callback_endpoint` が提供された場合、ダウンロードの準備ができ次第、提供されたアドレスに郵送依頼を行う。投稿本文は "success":trueとなる。クラウドストレージの認証情報をBrazeに追加していない場合、投稿本文にはさらに、ダウンロードURLを値として持つ属性`url` 。

ユーザー数が多いほど、エクスポートにかかる時間は長くなる。例えば、2000万人のユーザーを持つアプリの場合、1時間以上かかることもあります。

## Request body

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
個々のカスタム属性をエクスポートすることはできない。しかし、fields_to_export配列にcustom_attributesを含めることで、すべてのカスタム属性をエクスポートすることができる（例えば、`['first_name', 'email', 'custom_attributes']` ）。
{% endalert %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --- | ----------- | --------- | ------- |
|`callback_endpoint` | オプション | string | エクスポートが利用可能になったときにダウンロードURLを掲載するエンドポイント。 |
|`fields_to_export` | 必須 | 文字列の配列 | エクスポートするユーザー・データ・フィールドの名前。カスタム属性をエクスポートすることもできる。<br><br>\*2021年4月以降、新しいアカウントでは、エクスポートする特定のフィールドを指定する必要があります。 |
|`output_format` | オプション | string | 独自のS3バケットを使用する場合、ファイル形式を`zip` または`gzip` に指定できる。デフォルトはZIPファイル形式である。 |
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

以下は有効な`fields_to_export` のリストである。`fields_to_export` を使用して戻されるデータを最小化すると、この API エンドポイントの応答時間を短縮できます。

| エクスポートするフィールド | データタイプ | 説明 |
|---|---|---|
| `apps` | 配列 | このユーザーがセッションを記録したアプリケーション。これには次のフィールドが含まれます。<br><br>-`name`: アプリ名<br>-`platform`: iOS、Android、Webなどのアプリプラットフォーム<br>-`version`: アプリのバージョン番号または名前 <br>-`sessions`: このアプリの総セッション数<br>-`first_used`: 初回セッションの日付<br>-`last_used`: 最終セッションの日付<br><br>すべてのフィールドは文字列である。 |
| `attributed_campaign` | string | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution)のデータ (設定されている場合)。特定の広告キャンペーンの識別子。 |
| `attributed_source` | string | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution)のデータ (設定されている場合)。広告が掲載されたプラットフォームの識別子。 |
| `attributed_adgroup` | string | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution)のデータ (設定されている場合)。キャンペーン以下の任意のサブグループの識別子。 |
| `attributed_ad` | string | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution)のデータ (設定されている場合)。キャンペーンと広告グループの下にあるオプションのサブグループの識別子。 |
| `braze_id` | string | このユーザーに対してBrazeが設定したデバイス固有の一意のユーザー識別子。 |
| `country` | string | [ISO3166-1アルファ2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)標準を使用したユーザーの国。 |
| `created_at` | string | ユーザープロファイルが作成された日時 (ISO 8601形式)。 |
| `custom_attributes` | オブジェクト | このユーザーのカスタム属性のキーと値のペア。 |
| `custom_events` | 配列 | 過去90日間にこのユーザーに起因するカスタムイベント。 |
| `devices` | 配列 | ユーザーのデバイスに関する情報であり、プラットフォームによって以下のものが含まれる：<br><br>-`model` ：デバイスのモデル名<br>- `os`:デバイスのオペレーティング・システム<br>- `carrier`:端末のサービス・キャリア（利用可能な場合<br>-`idfv`: (iOS) Braze デバイス識別子、Apple Identifier for Vendor (存在する場合)<br>-`idfa`: (iOS) 広告の識別子（存在する場合<br>- `device_id`:(Android) Braze デバイス識別子<br>- `google_ad_id`:(Android) Google Play Advertising Identifier（存在する場合<br>- `roku_ad_id`:(Roku） Roku 広告識別子<br>-`ad_tracking_enabled` ：広告トラッキングがデバイス上で有効になっている場合、trueまたはfalseを指定する。 |
| `dob` | string | `YYYY-MM-DD` 形式のユーザーの生年月日。 |
| `email` | string | ユーザーのEメールアドレス。 |
| `external_id` | string | 識別されたユーザーに対する一意のユーザー識別子。 |
| `first_name` | string | ユーザーの名。 |
| `gender` | string | ユーザーの性別。可能な値は以下の通りである：<br><br>-`M`: 男性<br>-`F`: 女性<br>-`O`: その他<br>-`N`: 該当なし<br>-`P`: 言いたくない<br>-`nil`: 不明 |
| `home_city` | string | ユーザーの出身地。 |
| `language` | string | ISO-639-1標準のユーザー言語。 |
| `last_coordinates` | 浮動小数点数の配列 | ユーザーの最新のデバイスの場所、(`[longitude, latitude]` の形式)。 |
| `last_name` | string | ユーザーの姓。 |
| `phone` | string | E.164 形式のユーザーの電話番号。 |
| `purchase`s | 配列 | このユーザーが過去90日間に購入したもの。 |
| `random_bucket` | 整数 | ユーザーの[ランダムなバケット番号で]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)、一様に分布したランダムユーザーのセグメントを作成するために使用される。 |
| `time_zone` | string | IANAタイムゾーンデータベースと同じフォーマットによるユーザーのタイムゾーン。 |
| `total_revenue` | フロート | このユーザーに帰属する総収入。総収益は、ユーザーが受け取ったキャンペーンとキャンバスのコンバージョン期間中に行った購入に応じて計算されます。 |
| `uninstalled_at` | タイムスタンプ | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略する。 |
| `user_aliases` | オブジェクト | 存在すれば、`alias_name` と`alias_label` を含む[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)。 |
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

URLは公開後、数時間のみ有効である。そのため、Brazeに独自のS3認証情報を追加することを強く推奨する。

### ユーザー・エクスポート・ファイルの出力例

ユーザー・エクスポート・オブジェクト（可能な限り最小限のデータを含める。オブジェクトにフィールドがない場合は、null、false、または空であると仮定する）：

{% tabs %}
{% tab すべての分野 %}

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
{% tab サンプル出力 %}

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
