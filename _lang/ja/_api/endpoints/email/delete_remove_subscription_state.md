---
nav_title: "削除メールアドレスまたは電話番号によるサブスクリプション状態の削除"
article_title: "削除メールアドレスまたは電話番号によるサブスクリプション状態の削除"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "この記事では、Braze エンドポイントで電子メール アドレスまたは電話番号によるサブスクリプション状態の削除について詳しく説明します。"

---

{% api %}
# メールアドレスまたは電話番号でサブスクリプション状態を削除する
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> このエンドポイントを使用して、電子メール アドレスまたは電話番号に基づいてサブスクリプション状態の値を削除します。

## リクエストパラメータ

| パラメータ | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `email`| はい | 文字列 | ユーザーの電子メール アドレス (少なくとも 1 つ、最大 50 個のアドレスを含める必要があります)。 |
| `phone`| はい | 文字列 | ユーザーの電話番号 (少なくとも 1 つ、最大 50 個の電話番号を含める必要があります)。E.164 形式で提供することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## 応答

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}