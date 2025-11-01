---
nav_title: "POST:ライブ活動を更新する"
article_title: "POST:ライブアクティビティを更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、ライブ・アクティビティを更新するエンドポイントについての詳細を概説する。"

---
{% api %}
# ライブアクティビティを更新
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> このエンドポイントを使用して、iOSアプリが表示する[ライブ・アクティビティを]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)更新・終了する。このエンドポイントは追加のセットアップが必要です。

ライブ・アクティビティを登録した後、アップル・プッシュ・ノーティフィケーション・サービス（APN）をアップデートするためにJSONペイロードを渡すことができる。詳しくは、[プッシュ通知ペイロードを使ったライブアクティビティの更新](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications)に関する Apple のドキュメントを参照してください。

`content-available` が設定されていない場合、デフォルトのAppleプッシュ通知サービス（APN）の優先順位は10である。`content-available` が設定されている場合、この優先順位は5となる。詳しくは[Apple push objectを]({{site.baseurl}}/api/objects_filters/messaging/apple_object)参照のこと。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、次の手順を完了する必要があります:

- `messages.live_activity.update` の権限を持つ API キーを生成します。
- Braze Swift SDK を使用して、[リモート]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=remote&sdktab=swift)または[ローカル]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift)でライブアクティビティを登録する。

{% multi_lang_include api/payload_size_alert.md %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `app_id` | 必須 | 文字列 | アプリ[API 識別子]({{site.baseurl}}/api/identifier_types/#the-app-identifier)は[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得されました。  |
| `activity_id` | 必須 | 文字列 | [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class) を使用してライブアクティビティを登録する場合は、`pushTokenTag` パラメーターを使用して、アクティビティのプッシュトークンにカスタム文字列を名前として付けます。<br><br>`activity_id` をこのカスタム文字列に設定して、更新するライブアクティビティを定義します。 |
| `content_state` | 必須 | オブジェクト | ライブアクティビティを作成する際に`ContentState`パラメータを定義します。このオブジェクトを使用して、`ContentState`の更新された値を渡します。<br><br>このリクエストの形式は、最初に定義した形状に一致している必要があります。 |
| `end_activity` | オプション | ブール値 | `true` の場合、このリクエストはライブアクティビティを終了します。 |
| `dismissal_date` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | このパラメーターは、ユーザーのUIからライブアクティビティを削除する時間を定義します。この時間が過去のもので、`end_activity` が `true` の場合、ライブアクティビティは直ちに削除されます。<br><br> `end_activity` が`false` であるか、省略された場合、このパラメーターはライブアクティビティのみを更新します。|
| `stale_date` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | このパラメーターは、ライブアクティビティのコンテンツがユーザーの UI で古いものとしてマークされたときに、システムに通知します。 |
| `notification` | オプション | オブジェクト | プッシュ通知を定義する[`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)オブジェクトを含めます。このプッシュ通知の動作は、ユーザーがアクティブか、プロキシデバイスを使用しているかに依存する。 {::nomarkdown}<ul><li><code>通知が</code>含まれていて、更新が配信されたときにユーザーがiPhoneでアクティブになっていれば、更新されたライブ・アクティビティのUIがプッシュ通知のようにスライドして表示される。</li><li><code>通知が</code>含まれ、ユーザーがiPhoneでアクティブでない場合、画面が点灯し、ロック画面に更新されたライブ・アクティビティUIが表示される。</li><li><code>通知アラートは</code>標準的なプッシュ通知としては表示されない。さらに、ユーザーがアップルウォッチのようなプロキシデバイスを持っている場合、<code>アラートは</code>そこに表示される。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
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
