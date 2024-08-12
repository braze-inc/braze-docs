---
nav_title: "削除：メールアドレスまたは電話番号によるサブスクリプション状態の削除"
article_title: "削除：メールアドレスまたは電話番号によるサブスクリプション状態の削除"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "この記事では、メールアドレスまたは電話番号によるサブスクリプションの削除状態Brazeエンドポイントの詳細について説明します。"

---

{% api %}
# メールアドレスまたは電話番号でサブスクリプションの状態を削除する
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> このエンドポイントを使用して、メール アドレスまたは電話番号に基づいてサブスクリプション状態の値を削除します。

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --- | --- | --- | --- |
| `email` |はい |文字列 |ユーザーのメールアドレス (少なくとも 1 つのアドレスと最大 50 のアドレスを含める必要があります)。|
| `phone` |はい |文字列 |ユーザーの電話番号 (少なくとも 1 つの電話番号と最大 50 の電話番号を含める必要があります)。これは E.164 形式で提供することをお勧めします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例

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