---
nav_title: "GET: List subscription state with email address or phone number"
article_title: "GET: List Subscription State with Email Address or Phone Number"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "This article outlines the details about the List subscription state with an email address or phone number Braze endpoint."

---
{% api %}
# List subscription state with an email address or phone number
{% apimethod get %}
/users/subscription
{% endapimethod %}

> Use this endpoint to return the subscription state value based on an email address or phone number.

## Request parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `email` | Yes | String | The email address of the user (must include at least one address and at most 50 addresses). |
| `phone` | Yes | String | The phone number of the user (must include at least one phone number and at most 50 phone numbers). We recommend providing this in E.164 format. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

Entries are listed in descending order.

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
