---
nav_title: テスト
article_title: FireOS のテスト
platform: FireOS
page_order: 19
page_type: reference
description: "このリファレンス記事では、FireOS のアプリ内メッセージやプッシュ通知をコマンドラインからテストする方法を紹介します。"
channel: 
- push

---

# テスト

> このリファレンス記事では、FireOS のアプリ内メッセージやプッシュ通知をコマンドラインからテストする方法を紹介します。

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、cURL と[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

必須フィールド

- `YOUR-API-KEY-HERE` - [**設定**] > [**API キー**] で利用できます。キーが `/messages/send` REST API エンドポイントを介してメッセージを送信することを許可されていることを確認します。 
- `EXTERNAL_USER_ID` - [**ユーザーの検索**] ページで使用できます。
- `REST_API_ENDPOINT_URL` - Braze [インスタンス]({{site.baseurl}}/api/basics/#endpoints.にリストされています。ワークスペースがある Braze インスタンスに対応するエンドポイントを使用してください。

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
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```

