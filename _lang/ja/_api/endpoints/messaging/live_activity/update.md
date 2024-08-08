---
nav_title: "ポスト:ライブアクティビティを更新"
article_title: "ポスト:ライブアクティビティを更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、ライブアクティビティの更新エンドポイントの詳細について説明します。"

---
{% api %}
# ライブアクティビティを更新
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> このエンドポイントを使用して、iOS [アプリに表示されるライブアクティビティを更新および終了します]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/)。このエンドポイントには追加の設定が必要です。

ライブアクティビティを登録したら、JSON ペイロードを渡して Apple プッシュ通知サービス (APN) を更新できます。詳細については、[プッシュ通知ペイロードによるライブアクティビティの更新に関するAppleのドキュメントを参照してください](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、以下を完了する必要があります。

- `messages.live_activity.update`権限を使用して API キーを生成します。
- Braze Swift SDK を使用して、[[リモートまたはローカルでライブアクティビティを登録します]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=local#step-2-start-the-activity)]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=remote#step-2-start-the-activity)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `app_id` | 必須 | 文字列 | [API [キーページから取得したアプリ API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 識別子]({{site.baseurl}}/api/identifier_types/#the-app-identifier)。|
| `activity_id` | 必須 | 文字列 | を使用してライブアクティビティを登録する場合[`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class)、`pushTokenTag`パラメータを使用してアクティビティのプッシュトークンにカスタム文字列という名前を付けます。<br><br>`activity_id`このカスタム文字列に設定して、更新するライブアクティビティを定義します。|
| `content_state` | 必須 | オブジェクト | `ContentState` ライブアクティビティを作成するときにパラメーターを定義します。`ContentState`このオブジェクトを使用する際に、更新された値を渡してください。<br><br>このリクエストの形式は、最初に定義した形状と一致する必要があります。|
| `end_activity` | オプション | Boolean | `true` もし、このリクエストはライブアクティビティを終了します。|
| `dismissal_date` | オプション | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | このパラメータは、ライブアクティビティをユーザーのUIから削除する時間を定義します。`end_activity`この時間が過去のものであれば`true`、ライブアクティビティはすぐに削除されます。<br><br> `false`または省略した場合、`end_activity`このパラメーターはライブアクティビティのみを更新します。|
| `stale_date` | オプション | 日時 <br>（[ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)）| このパラメータは、ライブアクティビティのコンテンツがユーザーのUIで古くなっているとマークされたときにシステムに通知します。|
| `notification` | オプション | オブジェクト | [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)プッシュ通知を定義するオブジェクトを含めます。このプッシュ通知のこの動作は、ユーザーがアクティブか、ユーザーがプロキシデバイスを使用しているかによって異なります。 {::nomarkdown}<ul><li><code>通知が含まれていて</code>、アップデートが配信されたときにユーザーが iPhone でアクティブになっている場合、更新された Live Activity UI が下にスライドしてプッシュ通知のように表示されます。</li><li><code>通知が含まれていてユーザーがiPhoneでアクティブでない場合</code>、画面が点灯し、ロック画面に更新されたLive Activity UIが表示されます。</li><li><code>通知アラートは標準のプッシュ通知としては表示されません</code>。さらに、ユーザーがApple Watchなどのプロキシデバイスを持っている場合は、<code>そこにアラートが表示されます</code>。</li></ul>{:/}
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

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

このエンドポイントには、`201`との 2 つのステータスコード応答があります`4XX`。

### 成功レスポンスの例

リクエストが正しくフォーマットされ、リクエストを受け取った場合は、`201`ステータスコードが返されます。`201`ステータスコードは次のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンスの例

`4XX`ステータスコードのクラスはクライアントエラーを示します。[発生する可能性のあるエラーの詳細については、API エラーとレスポンスの記事を参照してください]({{site.baseurl}}/api/errors/)。

`400`ステータスコードは次のレスポンスボディを返す可能性があります。 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
