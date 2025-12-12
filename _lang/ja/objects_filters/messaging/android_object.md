---
nav_title: "Androidオブジェクト"
article_title: Android メッセージングオブジェクト
page_order: 0
page_type: reference
channel: push
platform: Android
description: "このリファレンス記事では、Brazeで使用されているさまざまなAndroidオブジェクトをリストアップし、説明している。"

---
# Androidオブジェクト

> `android_push` オブジェクトを使用すると、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を介して Android プッシュおよび Android プッシュアラートコンテンツに関連する情報を定義またはリクエストできます。

## Android プッシュオブジェクト

ターゲットにしたユーザーが Android デバイスでプッシュを受信できるようにするには、`messages` に Android プッシュオブジェクトを含める必要があります。`alert` 文字列と `extra` オブジェクトの合計バイト数は4,000を超えないようにしてください。メッセージングAPIは、Googleが許容するメッセージサイズを超えるとエラーを返す。

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "android_priority": (optional, string) the FCM sender priority,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to false,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android push action button objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed through Conversation Push
}
```

`extra` オブジェクトにキー `appboy_image_url` を指定すると、「Big Picture」通知を送信できます。`appboy_image_url` の値は、画像がホストされている場所にリンクする URL である必要があります。画像は縦横比2:1にトリミングし、600×300px以上であること。

### 追加パラメータの詳細

| パラメータ | 詳細 |
| --------- | ------- |
| `priority` | このパラメーターには `-2` から `2` までの値を指定できます。`-2` は「MIN」優先度を表し、`2` は「MAX」を表します。`0` は「デフォルト」値です。<br> <br> その範囲外の値が送信された場合、デフォルトは0となる。どの優先度を使うかについては、[Android の通知優先度]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority)を参照してください。 |
| `android_priority` | このパラメーターは、FCM 送信者の優先順位を指定するために、`normal` または `high` のいずれかの値を受け入れます。デフォルトでは、メッセージは[プッシュ設定]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns)ページで構成されたデフォルトの FCM 優先度で送信されます。<br><br> 値の違いが配信に与える影響の詳細については、[Android メッセージの優先度](https://firebase.google.com/docs/cloud-messaging/android/message-priority)を参照してください。 |
| `collapse_key` | FCM で同時に保存できるのは、1つのデバイスにつき最大4つの折りたたみキーのみです。4つを超える折りたたみキーを使用する場合、FCM でどの折りたたみキーが保持されるかについては保証されません。Braze はデフォルトでこれらのうちの1つをキャンペーンに使用するため、Android メッセージ用に指定する追加の折りたたみキーは3つまでにしてください。 |
| `push_icon_image_url` | large icon パラメーターの値は、画像がホストされている場所にリンクする URL である必要があります。<br> <br> イメージは1:1のアスペクト比にトリミングする必要があり、40x40以上にする必要があります。 |
| `notification_channel` | これが指定されない場合、Brazeは[ダッシュボードのフォールバック]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel)チャンネルIDで通知ペイロードを送信しようとする。詳細については、「[通知チャネル]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/)」を参照し、統合中に「[通知チャネルを定義する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)」ステップを参照してください。 |
| `send_to_sync` | `send_to_sync` メッセージの詳細については、[Android のサイレント通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Android プッシュアクションボタンオブジェクト

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android会話プッシュ・オブジェクト {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

このメッセージのコンセプトは、[Android People and Conversations](https://developer.android.com/guide/topics/ui/conversations) のプッシュドキュメントのコンセプトと同じです。

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android会話プッシュメッセージオブジェクト

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### アンドロイド会話プッシュ人物オブジェクト

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

