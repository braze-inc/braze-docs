---
nav_title: "GET: 이메일 주소 또는 전화번호로 구독 상태 나열하기"
article_title: "GET: 이메일 주소 또는 전화번호로 구독 상태 나열하기"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "이 문서에서는 이메일 주소 또는 전화번호가 있는 목록 구독 상태의 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 이메일 주소 또는 전화번호로 구독 상태를 나열합니다.
{% apimethod get %}
/users/subscription
{% endapimethod %}

> 이 엔드포인트를 사용하여 이메일 주소 또는 전화번호를 기준으로 구독 상태 값을 반환합니다.

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `email` | 예 | 문자열 | 사용자의 이메일 주소(최소 1개, 최대 50개의 주소를 포함해야 함). |
| `phone` | 예 | 문자열 | 사용자의 전화번호(최소 1개에서 최대 50개의 전화번호를 포함해야 함). E.164 형식으로 제공하는 것이 좋습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답

항목은 내림차순으로 나열됩니다.

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
