---
nav_title: "POST:Segmentによるユーザープロファイルのエクスポート"
article_title: "POST:セグメント別ユーザープロファイルのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「セグメントごとにユーザーをエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# Segmentによるユーザープロファイルのエクスポート
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> このエンドポイントを使用して、Segment内のすべてのユーザーs をエクスポートします。

{% alert important %}
このエンドポイントを使用する場合は、次の点に注意してください。<br><br>1\.このAPI リクエストの`fields_to_export` フィールドは**required** です。<br>2\.`custom_events`、`purchases`、`campaigns_received`、`canvases_received` のフィールドには、過去 90 日間のデータのみが含まれます。
{% endalert %}

ユーザーデータは、新しい行で区切られたユーザーのJSONオブジェクトの複数のファイルとしてエクスポートされます(1行に1つのJSONオブジェクトなど)。データは自動的に生成されたURLか、この統合がすでに設定されている場合はS3バケットにエクスポートされる。エクスポートに成功すると、圧縮アーカイブZIPまたはGZIPファイルを含む.txtファイルを受け取る。エクスポートに失敗すると、メールで通知が届く。

企業は、このエンドポイントを使用するセグメントごとに、特定の時刻に最大 1 つのエクスポートを実行できます。エクスポートが完了するのを待ってから、再試行してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`users.export.segment`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースの応答の詳細

[S3][1]、[Azure][2]、[Google Cloud Storageの][3]認証情報をBrazeに追加している場合、各ファイルは`segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` のようなキーフォーマットのZIPファイルとしてバケットにアップロードされる。Azure を使用している場合は、Braze の Azure パートナーの概要ページで、[**これをデフォルトのデータエクスポート先にする**] チェックボックスがオンになっていることを確認します。通常、Brazeは処理を最適化するため、ユーザー5,000人につき1ファイルを作成する。大きなワークスペース内で小さなセグメントをエクスポートすると、複数のファイルが生成される場合があります。その後、ファイルを抽出し、必要に応じてすべての`json` ファイルを1 つのファイルに連結できます。`gzip` の`output_format` を指定した場合、ファイルの拡張子は`.zip` ではなく`.gz` となる。

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

このエンドポイントを使用してエクスポートに独自のバケットポリシーを適用する場合は、独自の S3 または Azure 資格情報を設定することを強くお勧めします。クラウドストレージの認証情報がない場合は、リクエストへの応答で、すべてのユーザーファイルを含む ZIP ファイルをダウンロードできる URL が提供されます。URLが有効な場所になるのは、エクスポートの準備が整ってからである。

クラウドストレージ認証情報s を提供しない場合は、このエンドポイントからエクスポートできるデータ量に制限があることに注意してください。エクスポートするフィールドやユーザーの個数によっては、大きすぎるとファイル転送が失敗することがあります。ベストプラクティスは、`fields_to_export` を使用してエクスポートするフィールドを指定し、転送のサイズを低く保つために必要なフィールドs のみを指定することです。ファイルを生成するエラーを取得する場合は、乱数バケット番号に基づいてユーザー群をより多くのSegments に分割することを検討します(たとえば、乱数バケット番号が1000 未満、または1000 から2000 の間のSegmentを作成します)。

どちらのシナリオでも、オプションで`callback_endpoint` を指定して、エクスポートの準備が整ったときに通知することができます。`callback_endpoint` が提供された場合、Brazeはダウンロードの準備ができ次第、提供されたアドレスにポストリクエストを行う。投稿本文は "success":trueとなっている。S3認証情報をBrazeに追加していない場合、投稿本文にはさらに、ダウンロードURLを値とするアトリビューション`url` 。

ユーザー群が大きければ大きいほど、輸出に要する時間は長くなる。例えば、2,000 万人のユーザーを持つアプリの場合、1 時間以上かかることもあります。

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## リクエストパラメーター

| パラメーター                     | required  | データ型        | 説明                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id`                  | 必須  | 文字列           | エクスポートするSegmentのID。[セグメント識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br>特定のSegmentの`segment_id` は、Braze アカウントの[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから見つけることができます。または、[ Segment一覧エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) を使用することもできます。 |
| `callback_endpoint`           | オプション  | 文字列           | エクスポートが利用可能になった場合に、ダウンロード URL を投稿するエンドポイント。                                                                                                                                                                                                                                                                                                                                             |
| `fields_to_export`            | 必須* | 文字列の配列 | エクスポートするユーザーデータ フィールドの名前。また、このパラメータに`custom_attributes` を含めることで、すべてのカスタム属性s をエクスポートすることもできます。<br><br>\*2021 年 4 月以降、新しいアカウントでは、エクスポートする特定のフィールドを指定する必要があります。                                                                                                                                                                                        |
| `custom_attributes_to_export` | オプション  | 文字列の配列 | エクスポートする特定のカスタム属性の名前。最大500 個のカスタム属性をエクスポートできます。ダッシュボードでカスタム属性の作成および管理を行うには、[**データ設定**] > [**カスタム属性**] に移動します。                                                                                                                                                                                                          |
| `output_format`               | オプション  | 文字列           | ファイルの出力形式。デフォルトは `zip` ファイル形式です。独自のS3 バケットを使用している場合は、`zip` または`gzip` を指定できます。                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`fields_to_export` パラメーターに `custom_attributes` が含まれている場合、`custom_attributes_to_export` の内容に関係なく、すべてのカスタム属性がエクスポートされます。特定の属性をエクスポートすることが目的の場合は、`custom_attributes` を `fields_to_export` パラメーターに含めないでください。代わりに、`custom_attributes_to_export` パラメータを使用します。
{% endalert %}

## すべてのカスタム属性をエクスポートするサンプルリクエスト
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

## 具体的なカスタム属性をエクスポートするリクエスト例
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

以下は、有効な`fields_to_export`のリストです。`fields_to_export` を使用して返されるデータを最小限に抑えると、このAPI エンドポイントのレスポンスタイムを改善できます。

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
| `push_tokens`         | 配列           | ユーザーのプッシュトークンについての説明。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `random_bucket`       | 整数         | ユーザーの[乱数バケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。乱数ユーザーsの一様分布Segmentsを作成するために使用されます。                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | 文字列          | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | フロート           | このユーザーに帰属する総収益。総収益は、受領したキャンペーンおよびキャンバスのコンバージョン期間中に行われたユーザーの購入に基づいて計算されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | タイムスタンプ       | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | オブジェクト          | [`alias_name` および`alias_label` を含むユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) (存在する場合)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 重要なお知らせ

- `custom_events` 、`purchases` 、`campaigns_received` 、`canvases_received` のフィールドには、過去90日間のデータのみが含まれている。
- `custom_events` と`purchases` の両方に、`first` と`count` のフィールドs が含まれています。これらのフィールドはいずれも、過去90日間のデータに限定されず、すべての時間の情報を反映している。例えば、特定のユーザーが90日前に初めてそのイベントを行った場合、これは`first` フィールドに正確に反映され、`count` フィールドは過去90日以前に発生したイベントも考慮する。
- 企業がエンドポイント レベルで実行できる同時セグメント エクスポートの数は 100 に制限されています。この制限を超える試みはエラーとなる。
- 最初のエクスポート・ジョブがまだ実行されている間に、セグメンテーションを2回目にエクスポートしようとすると、429エラーが発生する。

## 応答

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that is used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URLは公開後、数時間のみ有効である。そのため、独自のS3 認証情報をBraze に追加することを強くお勧めします。

APIレスポンスに`object_prefix` 、データをダウンロードするURLが表示されない場合、このエンドポイントにAmazon S3バケットがすでに設定されていることを意味する。このエンドポイントを使用してエクスポートされたデータは、S3バケットに直接送られる。

## サンプルユーザーのエクスポートファイルアウトプット

ユーザーエクスポートオブジェクト（Brazeは可能な限り最小限のデータを含む-オブジェクトにフィールドがない場合、そのフィールドはNULLまたは空であると仮定する）：

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

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}
