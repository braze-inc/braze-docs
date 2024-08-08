---
nav_title: "アンドロイドオブジェクト"
article_title: Android メッセージングオブジェクト
page_order: 0
page_type: reference
channel: push
platform: Android
description: "この参考記事では、Braze で使用されるさまざまな Android オブジェクトを一覧表示して説明しています。"

---
# アンドロイドオブジェクト

> `android_push`このオブジェクトを使用すると、[メッセージングエンドポイントを介して]({{site.baseurl}}/api/endpoints/messaging) Android Push および Android Push Alert コンテンツに関連する情報を定義またはリクエストできます。

##  アンドロイドプッシュオブジェクト

`messages`ターゲットとするユーザーに Android デバイスでプッシュを受信させるには、Android プッシュオブジェクトを含める必要があります。`alert``extra`文字列とオブジェクトの合計バイト数は 4,000 バイトを超えないようにしてください。Google で許可されているメッセージサイズを超えると、Messaging API はエラーを返します。

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android Push Action Button Objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed via Conversation Push.
}
```

`appboy_image_url``extra`オブジェクト内のキーを指定することで、「全体像」通知を送信できます。の値は、画像がホストされている場所にリンクする URL `appboy_image_url` でなければなりません。画像は 2:1 のアスペクト比にトリミングし、600 x 300 ピクセル以上にする必要があります。通知に使用される画像は、Jelly Bean (Android 4.1) 以降を搭載しているデバイスのみに表示されます。

#### その他のパラメーターの詳細

| パラメーター | 詳細 |
| --------- | ------- |
| `priority` | `-2` このパラメータはからまでの値を受け入れます。ここで`2``-2`、「MIN」`2` 優先度を表し、「MAX」を表します。`0`は「デフォルト」値です。<br> <br> その整数の範囲外に送信された値は、デフォルトで 0 になります。使用する優先度レベルの詳細については、[Android 通知の優先度に関するセクションをご覧ください][29]。|
| `collapse_key` | FCM が同時に保存できる折りたたみキーは、1 つのデバイスにつき 4 つまでです。4 つ以上の折りたたみキーを使用する場合、FCM はどのキーが保持されるかを保証しません。Braze はキャンペーンではこれらのうちの 1 つをデフォルトで使用するため、Android メッセージに追加する折りたたみキーは 3 つまでしか追加しないようにしてください。|
| `push_icon_image_url` | 大きいアイコンパラメータの値は、画像がホストされている場所にリンクするURLでなければなりません。<br> <br> 画像は 1:1 のアスペクト比にトリミングし、少なくとも 40x40 にする必要があります。|
| `notification_channel` | これが指定されていない場合、Braze [はダッシュボードフォールバックチャネル][45] ID を使用して通知ペイロードを送信しようとします。詳細については、「[通知チャネル][44]」および「[統合中に通知チャネルを定義する手順][43]」を参照してください。|
| `send_to_sync` | `send_to_sync` メッセージについて詳しくは、[Android のサイレント通知をご覧ください][28]。|
{: .reset-td-br-1 .reset-td-br-2}

## Android プッシュアクションボタンオブジェクト

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android 会話プッシュオブジェクト {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

このメッセージの概念は、[Android の「ユーザーと会話][46]」プッシュドキュメントの概念に対応しています。

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android 会話プッシュメッセージオブジェクト

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Android 会話プッシュユーザーオブジェクト

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[44]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/
[43]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels
[45]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[46]: https://developer.android.com/guide/topics/ui/conversations
