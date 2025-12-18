---
nav_title: "GET: List users subscription groups"
article_title: "GET: List User's Subscription Groups"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the List user's subscription groups Braze endpoint."

---
{% api %}
# List user's subscription groups
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Use this endpoint to list and get the subscription groups with the history of a certain user.

If you want to see examples or test this endpoint for **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

If you want to see examples or test this endpoint for **SMS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

If you want to see examples or test this endpoint for **WhatsApp Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `subscription.groups.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `external_id`  | Required | String | The `external_id` of the user (must include at least one and at most 50 `external_ids`). |
| `email`  |  Required* | String | The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). |
| `phone` | Required* | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | The phone number of the user. Must include at least one phone number (with a maximum of 50). |
| `limit` | Optional | Integer | The limit on the maximum number of results returned. Default (and maximum) `limit` is 100. |
| `offset`  |  Optional | Integer | Number of templates to skip before returning the rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
If there are multiple users (multiple `external_ids`) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
{% endalert %}

## Example request

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Example response

Only subscription groups that have had a subscription status update in a user's history will be included in a successful response. This means that newly created subscription groups will not be listed.

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}
