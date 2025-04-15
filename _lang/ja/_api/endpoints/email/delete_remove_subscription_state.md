---
nav_title: "DELETE:メールアドレスまたは電話番号でサブスクリプション状態を削除"
article_title: "DELETE:メールアドレスまたは電話番号でサブスクリプション状態を削除"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "この記事では、メールアドレスまたは電話番号のBrazeエンドポイントによるサブスクリプション状態の削除についての詳細を説明します。"

---

{% api %}
# メールアドレスまたは電話番号でサブスクリプション状態を削除
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> このエンドポイントを使用して、メールアドレスまたは電話番号に基づいてサブスクリプション状態の値を削除します。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --- | --- | --- | --- |
| `email` | はい | 文字列 | ユーザーのメールアドレス （最低1個、最大50個のアドレスを含むこと）。 |
| `phone` | はい | 文字列 | ユーザーの電話番号 （最低1個、最大50個の電話番号を含むこと）。これは、E.164 形式で指定することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

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
