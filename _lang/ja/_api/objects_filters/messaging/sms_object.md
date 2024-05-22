---
nav_title: "SMSオブジェクト"
article_title: SMSメッセージング・オブジェクト
page_order: 10
page_type: reference
channel: SMS
description: "この参考記事では、Braze SMSオブジェクトのさまざまなコンポーネントについて説明しています。"

---
# SMSオブジェクト

> `sms` オブジェクトを使用すると、当社の[メッセージングエンドポイントを介して]({{site.baseurl}}/api/endpoints/messaging) SMS メッセージを変更または作成できます。

```json
{
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message.    
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)