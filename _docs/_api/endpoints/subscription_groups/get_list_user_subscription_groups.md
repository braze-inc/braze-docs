---
nav_title: "GET: List User's Subscription Groups"
page_order: 4

layout: api_page2

page_type: reference
platform: API
channel:
  - Email
  - SMS
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the List User's Subscription Groups Braze endpoint."
---

{% api %}

# Get Users' Subscription Groups

{% apimethod get %}
/subscription/user/status
{% endapimethod %}

Use the endpoints below to list and get the subscription groups of a certain user.

If you want to see examples or test this endpoint for __Email Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionGroups {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

<br>

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionGroups {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}


## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `external_id`  | Yes | String | The external_id of the user (must include at least one and at most 50 `external_ids`). |
| `email`  |  Yes | String | The email address of the user (must include at least one address and at most 50 addresses). |
| `limit` | No | Integer | The limit on the maximum number of results returned. Default (and max) limit is 100. |
| `offset`  |  No | Integer | Number of templates to skip before returning the rest of the templates that fit the search criteria. |

{% alert tip %}
If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
{% endalert %}

### Example Request

```
https://rest.iad-03.braze.com/subscription/user/status?api_key=23abc-def5-3729-owod-23f9f3j30&email=example%2B1%40braze.com&subscription_group_id=14386d4a-60dd-42e2-9c94-5f2423b91d9f
```
{% endapi %}
