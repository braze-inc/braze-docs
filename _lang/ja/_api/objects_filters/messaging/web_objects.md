---
nav_title: "Web オブジェクト"
article_title: Web メッセージングオブジェクト
page_order: 12
page_type: reference
channel: push
platform: Web
description: "この参考記事では、Braze で使用されるさまざまな Web オブジェクトを一覧表示して説明しています。"

---
# Web プッシュオブジェクト

> `web_push`このオブジェクトを使用すると、[メッセージングエンドポイントを介してWebプッシュおよびWebプッシュアラートコンテンツに関連する情報を定義またはリクエストできます]({{site.baseurl}}/api/endpoints/messaging)。

## Web プッシュオブジェクト

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "custom_uri": (optional, string) a web URL,
   "image_url": (optional, string) URL for image to show,
   "large_image_url": (optional, string) URL for large image, supported on Chrome Windows/Android,
   "require_interaction": (optional, boolean) whether to require the user to dismiss the notification, supported on Mac Chrome,
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
   "buttons" : (optional, array of Web Push Action Button Objects) push action buttons to display
}
```

の値は、画像がホストされている場所にリンクする URL `image_url` でなければなりません。画像は 1:1 のアスペクト比にトリミングする必要があります。

## Web プッシュアクションボタンオブジェクト

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```
