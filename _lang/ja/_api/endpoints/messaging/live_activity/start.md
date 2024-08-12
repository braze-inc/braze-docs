---
nav_title: "ポスト:ライブアクティビティの開始"
article_title: "ポスト:ライブアクティビティの開始"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、Start Live Activity エンドポイントの詳細について説明します。"

---
{% api %}
# ライブアクティビティの開始
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> このエンドポイントを使用して、iOS アプリに表示される [ライブ アクティビティ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) をリモートで開始します。このエンドポイントには追加の設定が必要です。

ライブアクティビティを作成したら、POST 要求を行って、特定のセグメントのアクティビティをリモートで開始できます。Apple のライブアクティビティの詳細については、「 [ActivityKit プッシュ通知を使用したライブアクティビティの開始と更新](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)」を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、次の作業を完了する必要があります。

- 権限を持つ `messages.live_activity.start` APIキーを生成します。
- Braze Swift SDKを使用して[ライブアクティビティを作成します]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-1-create-a-live-activity)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (i.e. the sports team names which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## 要求パラメーター

|パラメータ |必須項目 |データ型 |形容                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------- | -------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|`app_id` |必須項目 |文字列 |[[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)] ページから取得したアプリの [API 識別子]({{site.baseurl}}/api/identifier_types/#the-app-identifier)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `activity_id`       |必須項目 |文字列 |カスタム文字列 `activity_id`を .この ID は、ライブ アクティビティに更新イベントまたは終了イベントを送信するときに使用します。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `activity_attributes_type`       |必須項目 |文字列 |アプリで定義する `liveActivities.registerPushToStart` アクティビティ属性の種類                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `activity_attributes`       |必須項目 |オブジェクト |アクティビティタイプの静的属性値(つまり、変更されないスポーツチーム名)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `content_state`     |必須項目 |オブジェクト |パラメーターは `ContentState` 、ライブアクティビティを作成するときに定義します。このオブジェクトを使用するために `ContentState` 更新された値を渡します。<br><br>この要求の形式は、最初に定義した形状と一致する必要があります。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `dismissal_date` |オプション |日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) |このパラメーターは、ユーザーの UI からライブアクティビティを削除する時間を定義します。|
| `stale_date` |オプション |日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) |このパラメーターは、ライブ アクティビティ コンテンツがユーザーの UI で古くなったとマークされたときにシステムに通知します。|
| `notification`      |必須項目 |オブジェクト | [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) プッシュ通知を定義するオブジェクトを含めます。このプッシュ通知の動作は、ユーザーがアクティブかどうか、またはユーザーがプロキシデバイスを使用しているかどうかによって異なります。 {::nomarkdown}<ul><li><code>通知</code>が含まれていて、更新プログラムが配信されたときにユーザーが iPhone でアクティブになっている場合、更新されたライブ アクティビティ UI は下にスライドし、プッシュ通知のように表示されます。</li><li><code>通知</code>が含まれていて、ユーザーが iPhone でアクティブになっていない場合、画面が点灯し、更新されたライブ アクティビティ UI がロック画面に表示されます。</li><li><code>通知アラート</code>は、標準のプッシュ通知として表示されません。さらに、ユーザーがApple Watchなどのプロキシデバイスを持っている場合は、 <code>そこにアラート</code> が表示されます。</li></ul>{:/}
|`external_user_ids` |省略可能 (または `audience` が指定されている場合) `segment_id` |文字列の配列 |[外部ユーザー ID (external user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) を参照。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|`segment_id ` |省略可能 (または `audience` が指定されている場合) `external_user_ids` |文字列 |[セグメント ID (segment identifier]({{site.baseurl}}/api/identifier_types/)) を参照。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|`custom_audience` |省略可能 (または `segment_id` が指定されている場合) `external_user_ids` |接続されたオーディエンスオブジェクト |[「接続されたオーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)」を参照してください。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求の例

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

このエンドポイント `201` には、と `4XX`の 2 つの状態コード応答があります。

### 成功応答の例

`201`要求が正しく書式設定され、要求を受け取った場合は、状態コードが返されます。状態コード `201` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例

状態コードのクラスは `4XX` 、クライアント エラーを示します。発生する可能性のあるエラーの詳細については、 [API のエラーと応答に関する記事]({{site.baseurl}}/api/errors/) を参照してください。

状態コード `400` は、次の応答本文を返す可能性があります。 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
