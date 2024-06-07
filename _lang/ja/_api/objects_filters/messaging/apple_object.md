---
nav_title: "アップルオブジェクト"
article_title: Apple メッセージングオブジェクト
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "この参考記事では、Braze で使われているさまざまな Apple オブジェクトを一覧表示して説明しています。"

---

# アップルプッシュオブジェクト

> `apple_push`このオブジェクトを使用すると、Apple Push および Apple Push Alert [コンテンツに関連する情報をメッセージングエンドポイント経由で定義またはリクエストできます]({{site.baseurl}}/api/endpoints/messaging)。

## アップルプッシュオブジェクト

```json
{
   "badge": (optional, int) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") specifies the interruption level passed (iOS 15+),
   "relevance_score": (optional, float) specifies the relevance score between 0.0 and 1.0 used for grouping notification summaries (iOS 15+),
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device after you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple Push Action Button Objects) push action buttons to display
}
```

ターゲットとするユーザーに `messages` iOS デバイスでプッシュを受信させるには、Apple Push オブジェクトを含める必要があります。`alert`文字列、`extra`オブジェクト、およびその他のオプションパラメータの合計バイト数は、1912 を超えないようにしてください。Appleが許可するメッセージサイズを超えると、Messaging APIはエラーを返します。`ab``aps``extra`キーを含むメッセージやオブジェクトに含まれるメッセージは拒否されます。

{% alert note %}
Apple Push オブジェクトを Live Activities ペイロードの一部として送信する場合は、`sound``alert`必ずオブジェクトに文字列を含めてください。
{% endalert %}

### Apple プッシュアラートオブジェクト

ほとんどの場合、`alert``apple_push`オブジェクト内の文字列として指定できます。

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button's title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key,
   "sound": (optional, string) the location of a custom notification sound within the app (live activities only),
}
```

## Apple プッシュアクションボタンオブジェクト

iOS プッシュアクションボタンを使用するには、Apple Push `category` オブジェクトにフィールドを含める必要があります。`category`フィールドを含めると、関連するすべてのプッシュアクションボタンが表示されます。ボタンの個々のクリックアクションを追加で定義する場合のみ、`buttons`フィールドを含めてください。Braze SDK には、次の表に示すように、使用できるデフォルトのプッシュアクションボタンのセットが用意されています。アプリに登録されている独自のボタンを使用することもできます。

### Braze デフォルトボタン用の Apple プッシュアクションボタンオブジェクト

| カテゴリ識別子 | ボタンテキスト | ボタンアクション識別子 | 許可されるアクション |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | 同意する | `ab_pb_accept` |  OPEN\_APP, URI, or DEEP\_LINK |
| `ab_cat_accept_decline` | 拒否 | `ab_pb_decline` | 閉じる |
| `ab_cat_yes_no` | はい | `ab_pb_yes` | OPEN\_APP, URI, or DEEP\_LINK |
| `ab_cat_yes_no` | いいえ | `ab_pb_no` | 閉じる |
| `ab_cat_confirm_cancel` | 確認 | `ab_pb_confirm` | OPEN\_APP, URI, or DEEP\_LINK |
| `ab_cat_confirm_cancel` | キャンセル | `ab_pb_cancel` | 閉じる |
| `ab_cat_more` | 詳細 | `ab_pb_more` | OPEN\_APP, URI, or DEEP\_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### アプリで定義されたカテゴリのAppleプッシュアクションボタンオブジェクト

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```
