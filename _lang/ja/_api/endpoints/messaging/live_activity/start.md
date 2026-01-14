---
nav_title: "POST:ライブ活動を開始する"
article_title: "POST:ライブアクティビティを開始"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「ライブアクティビティを開始」エンドポイントの詳細について説明します。"

---
{% api %}
# ライブアクティビティを開始
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> このエンドポイントを使用して、iOSアプリに表示される[Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)をリモートで開始します。このエンドポイントは追加のセットアップが必要です。

ライブアクティビティを作成した後、任意のセグメントのアクティビティをリモートで開始するためにPOSTリクエストを送信できます。詳細については、Appleのライブアクティビティについては、[ActivityKitプッシュ通知でライブアクティビティを開始および更新する](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)を参照してください。

`content-available` が設定されていない場合、デフォルトのAppleプッシュ通知サービス（APN）の優先順位は10である。`content-available` が設定されている場合、この優先順位は5となる。詳しくは[Apple push objectを]({{site.baseurl}}/api/objects_filters/messaging/apple_object)参照のこと。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、次の手順を完了する必要があります:

- `messages.live_activity.start` の権限を持つ API キーを生成します。
- 「[ライブアクティビティを作成]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity)」Braze SWIFT SDK を使用します。

{% multi_lang_include api/payload_size_alert.md %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## リクエストパラメーター

| パラメーター | required | データ型| 説明  |
|-----------|----------|----------|--------------|
| `app_id` | 必須 | 文字列 | アプリ[API 識別子]({{site.baseurl}}/api/identifier_types/#the-app-identifier)は[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得されました。  |
| `activity_id` | 必須 | 文字列  | カスタム文字列を`activity_id`として定義します。この ID を使用して、ライブアクティビティに更新または終了イベントを送信します。  |
| `activity_attributes_type`  | 必須 | 文字列 | アプリ内の`liveActivities.registerPushToStart`で定義するアクティビティ属性タイプ。  |
| `activity_attributes` | 必須 | オブジェクト  | アクティビティタイプの静的属性値（スポーツチームの名前など、変更されないもの）。 |
| `content_state` | 必須 | オブジェクト  | ライブアクティビティを作成する際に`ContentState`パラメータを定義します。このオブジェクトを使用して、`ContentState`の更新された値を渡します。<br><br>このリクエストの形式は、最初に定義した形状に一致している必要があります。 |
| `dismissal_date` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | このパラメーターは、ユーザーのUIからライブアクティビティを削除する時間を定義します。 |
| `stale_date` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | このパラメーターは、ライブアクティビティのコンテンツがユーザーの UI で古いものとしてマークされたときに、システムに通知します。 |
| `notification` | 必須 | オブジェクト | プッシュ通知を定義する[`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)オブジェクトを含めます。このプッシュ通知の動作は、ユーザーがアクティブか、プロキシデバイスを使用しているかに依存する。 {::nomarkdown}<ul><li>もし  <code>notification</code> 含まれており、更新が配信されたときにユーザーがiPhoneでアクティブである場合、更新されたライブアクティビティUIがスライドダウンしてプッシュ通知のように表示されます。</li><li>もし  <code>notification</code> が含まれており、ユーザーがiPhoneでアクティブでない場合、ロック画面に更新されたライブアクティビティUIを表示するために画面が点灯します。</li><li>この  <code>notification alert</code> は、標準のプッシュ通知として表示されません。さらに、ユーザーがApple Watchのようなプロキシデバイスを持っている場合、 <code>alert</code> そこに表示されます。</li></ul>{:/} |
| `external_user_ids` | `segment_id`または`audience`が提供されている場合は任意 | 文字列の配列 | [外部ユーザーID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)を参照してください。最大50の外部ユーザーID。  |
| `segment_id `  | `external_user_ids`または`audience`が提供されている場合は任意 | 文字列    | [セグメント識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `custom_audience` | `external_user_ids`または`segment_id`が提供されている場合は任意 | 接続されたオーディエンスオブジェクト  | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "dismissal_date": "2024-01-22T00:00:00+0000",
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'
```

## 応答

このエンドポイントには2つのステータスコード応答があります: `201` と `4XX`。

### 成功応答の例

リクエストが正しくフォーマットされ、当社がそのリクエストを受け取った場合、`201` ステータスコードが返されます。ステータスコード `201` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコードの`4XX`クラスはクライアントエラーを示します。エラーに関する詳細は、[APIエラーと応答の記事]({{site.baseurl}}/api/errors/)を参照してください。

ステータスコード `400` は、次の応答本文を返す可能性があります。

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
