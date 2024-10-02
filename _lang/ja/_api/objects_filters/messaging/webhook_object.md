---
nav_title: "ウェブフック・オブジェクト"
article_title: ウェブフック・メッセージング・オブジェクト
page_order: 13
page_type: reference
channel: 
  - webhook
description: "このリファレンス記事では、BrazeのWebhookオブジェクトについて概説している。"

---

# ウェブフック・オブジェクト

> `webhook` オブジェクトを使うと、[メッセージング・エンドポイント]({{site.baseurl}}/api/endpoints/messaging)経由でウェブフック・メッセージを変更したり作成したりできる。

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

ベストプラクティスとして、Braze は、送信者やサーバーが時間とともに変更される可能性があるため、一貫性のある予測可能な動作を確保するために、`request_headers` フィールドに `Content-Type` の明示的な値を提供することを推奨します。`Content-Type` ヘッダーに値が指定されなければ、リクエストボディから推測されます。
