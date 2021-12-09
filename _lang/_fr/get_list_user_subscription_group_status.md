---
nav_title: "GET: List Users' Subscription Group Status"
article_title: "GET: List User's Subscription Group Status"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List Users' Subscription Group Status Braze endpoint."
---

{% api %}
# Get users' subscription group status
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

Use the endpoints below to get the subscription state of a user in a subscription group. These groups will be available on the __Subscription Group__ page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

If you want to see examples or test this endpoint for __Email Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Request parameters

| Parameter               | Required  | Data Type                                                     | Description                                                                                                                                                                                                                                        |
| ----------------------- | --------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subscription_group_id` | Required  | String                                                        | The `id` of your subscription group.                                                                                                                                                                                                               |
| `external_id`           | Required* | String                                                        | The `external_id` of the user (must include at least one and at most 50 `external_ids`). <br><br>When both an `external_id` and `email`/`phone` are submitted, only the `external_id`(s) provided will be applied to the result query. |
| `email`                 | Required* | String                                                        | The email address of the user. It can be passed as an array of strings with a max of 50. Submitting both an email address and phone number (with no `external_id`) will result in an error.                                                        |
| `phone`                 | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone number of the user. If email is not included, you must include at least one phone number (with a max of 50). <br><br> Submitting both an email address and phone number (with no `external_id`) will result in an error.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

*One of `external_id` or `email` or `phone` is required for each user.

- For SMS subscription groups, either `external_id` or `phone` is required.  When both are submitted, only the `external_id` is used for querying and the phone number is applied to that user.
- For email subscription groups, either `external_id` or `email` is required.  When both are submitted, only the `external_id` is used for the query and the email address is applied to that user.

## Example request

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Response

All successful responses will return `subscribed`, `unsubscribed`, or `unknown` depending on status and user history with the subscription group.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
