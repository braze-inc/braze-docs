---
nav_title: "KindleとFireOSのプッシュオブジェクト"
article_title: KindleとFireOSのプッシュ・メッセージング・オブジェクト
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "このリファレンス記事では、Braze KindleおよびFireOSのプッシュオブジェクトのさまざまなコンポーネントについて説明します。"

---

# KindleとFireOSのプッシュオブジェクト

> `kindle_push` オブジェクトを使用すると、当社の[メッセージングエンドポイントを介して]({{site.baseurl}}/api/endpoints/messaging) Kindle と FireOS のプッシュ通知を変更または作成できます。

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "priority": (optional, integer) the notification priority value,
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI
}
```

`priority` パラメータは、`-2` から`2` までの値を受け付ける。ここで、`-2` は最低優先度、`2` は最高優先度を表す。`0` はデフォルト値。この整数範囲外の値が送信された場合、デフォルトは`0` になります。
