---
nav_title: "SMSオブジェクト"
article_title: SMSメッセージング・オブジェクト
page_order: 10
page_type: reference
channel: SMS
description: "この参考記事では、Braze SMS オブジェクトのさまざまなコンポーネントについて説明します。"

---
# SMSオブジェクト

> `sms` オブジェクトを使用すると、[メッセージングエンドポイント[]({{site.baseurl}}/api/endpoints/messaging)を通じて SMS メッセージを変更または作成できます。

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
  - ワークスペースに設定されたアプリからの有効な`app_id` は、ユーザーが特定のアプリをプロファイルに登録しているかどうかに関係なく、ワークスペース内のすべてのユーザーに対して機能する。