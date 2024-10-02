---
nav_title: "Kindle およびFireOS プッシュオブジェクト"
article_title: Kindle およびFireOS プッシュメッセージングオブジェクト
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "このリファレンス記事では、Braze Kindle と FireOS プッシュオブジェクトのさまざまなコンポーネントについて説明します。"

---

# Kindle およびFireOS プッシュオブジェクト

> `kindle_push` オブジェクトを使用すると、[ メッセージング エンドポイント s]({{site.baseurl}}/api/endpoints/messaging) でKindle およびFire OS プッシュ通知を変更または作成できます。

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

`priority` パラメータは、`-2` から `2` までの値を受け入れます。ここで、`-2` は最低の優先度を表し、`2` は最高の優先度を表します。`0` はデフォルト値です。その整数範囲外に送信された値は、デフォルトで `0` に設定されます。
