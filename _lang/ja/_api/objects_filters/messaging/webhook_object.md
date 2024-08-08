---
nav_title: "ウェブフックオブジェクト"
article_title: Webhook メッセージングオブジェクト
page_order: 13
page_type: reference
channel: 
  - webhook
description: "この参考記事では、Braze Webhook オブジェクトの概要を説明しています。"

---

# ウェブフックオブジェクト

> `webhook`このオブジェクトを使用すると、[メッセージングエンドポイントを介してWebhookメッセージを変更または作成できます]({{site.baseurl}}/api/endpoints/messaging)。

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

送信者とサーバーは時間とともに変化する可能性があるため、Braze はベストプラクティスとして `Content-Type` in the `request_headers` field に明示的な値を指定することを推奨しています。一貫性のある予測可能な動作を実現するためです。`Content-Type`ヘッダーに値が指定されていない場合は、リクエスト本文から値が推測されます。
