---
nav_title: "GET：Eメールアドレスまたは電話番号付きリスト購読州"
article_title: "GET：Eメールアドレスまたは電話番号付きリスト購読州"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "この記事では、電子メールアドレスまたは電話番号を持つBrazeエンドポイントのリスト購読状態に関する詳細について概説します。"

---
{% api %}
# 電子メールアドレスまたは電話番号で購読状態をリストする
{% apimethod get %}
/users/subscription
{% endapimethod %}

> このエンドポイントを使用して、電子メールアドレスまたは電話番号に基づいてサブスクリプション状態の値を返します。

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| --- | --- | --- | --- |
|`email` ｜はい｜文字列｜ユーザーの電子メールアドレス（少なくとも1つ、最大50のアドレスを含める必要があります）。|
|`phone` ｜はい｜文字列｜ユーザーの電話番号（少なくとも1つ、最大50の電話番号を含める必要があります）。E.164形式で提供することを推奨する。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 応答

エントリーは降順で表示される。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example@braze.com",
      "email_subscribe": {
        "email_subscription_event_date": "2019-11-20T19:58:04.825Z",
        "email_subscription_state": "Subscribed"
      },
      "subscription_group": [
        {
          "subscription_group_id": "5f5536d2a76e0f4e323a1234",
          "subscription_group_event_date": "2021-03-11T21:29:22.347Z",
          "subscription_group_state": "Unsubscribed"
        }
      ],
      "hard_bounced_at": null,
      "spam_at": null
    }
  ],
	"phone": [{
		"phone": "+12123355555",
		"subscription_group": [{
			"subscription_group_id": "3f5536d2a76e0f4e323a5555",
			"subscription_group_state": "Subsscribed",
			"subscription_group_event_date": "2021-03-11T21:29:22.347Z"
		}]
	}],
	"message": "success"
}
```

{% endapi %}