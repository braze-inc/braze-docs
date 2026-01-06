---
nav_title: "GET: List users' subscription group status"
article_title: "GET: List User's Subscription Group Status"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List user's subscription group status Braze endpoint."

---
{% api %}
# List user's subscription group status
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Use this endpoint to get the subscription state of a user in a subscription group.

These groups will be available on the **Subscription Group** page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

If you want to see examples or test this endpoint for **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

If you want to see examples or test this endpoint for **SMS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

If you want to see examples or test this endpoint for **WhatsApp Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `subscription.status.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Required | String | The `id` of your subscription group. |
| `external_id`  |  Required* | String | The `external_id` of the user (must include at least one and at most 50 `external_ids`). <br><br>When both an `external_id` and `email`/`phone` are submitted, only the `external_id`(s) provided will be applied to the result query. |
| `email` | Required* | String | The email address of the user. It can be passed as an array of strings with a maximum of 50.<br><br> Submitting both an email address and phone number (with no `external_id`) will result in an error. |
| `phone` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone number of the user. If email is not included, you must include at least one phone number (with a maximum of 50).<br><br> Submitting both an email address and phone number (with no `external_id`) will result in an error. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

*One of `external_id` or `email` or `phone` is required for each user.

- For SMS and WhatsApp subscription groups, either `external_id` or `phone` is required.  When both are submitted, only the `external_id` is used for querying and the phone number is applied to that user.
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
{% tab SMS and WhatsApp %}
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

All successful responses will return `Subscribed`, `Unsubscribed`, or `Unknown` depending on status and user history with the subscription group.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert note %}
When a user unsubscribes globally, they are unsubscribed from each subscription group. This endpoint returns the last subscription status for each subscription group. This is expected behavior because if the user decides to globally resubscribe, Braze reverts each subscription status.
{% endalert %}

{% endapi %}
