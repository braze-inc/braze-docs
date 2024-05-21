---
nav_title: テスト
article_title: iOS のプッシュ通知テスト
platform: iOS
page_order: 29
description: "この参照記事では、iOS プッシュ通知のコマンドラインプッシュテストについて説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# {#push-testing} のテスト

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURL と [メッセージング API][29] を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

必須フィールド

- `YOUR-API-KEY-HERE` - [**設定**] > [**API キー**] で利用できます。キーが `/messages/send` REST API エンドポイントを介してメッセージを送信することを許可されていることを確認します。 
- `EXTERNAL_USER_ID` - [**ユーザーの検索**] ページで使用できます。
- `REST_API_ENDPOINT_URL` - Braze [インスタンス]({{site.baseurl}}) /api/basics/#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on. にリストされています

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- [**API キー**] は [**開発者コンソール**] > [**API 設定**] にあります。<br>\- [**ユーザー検索**]は、[**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

省略可能なフィールド:
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```
[29]: {{site.baseurl}}/api/endpoints/messaging/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
