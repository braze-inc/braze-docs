---
nav_title: "GET: List User's Subscription Groups"
page_order: 4

layout: api_page

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

If you want to see examples or test this endpoint for __SMS Subscription Groups__:

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Subscription%20Groups/GetUsersSubscriptionGroups {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}


## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `external_id`  | Yes | String | The external_id of the user (must include at least one and at most 50 `external_ids`). |
| `email`  |  Yes* | String | The email address of the user, can be passed as an array of strings (must include at least one address and at most 50 addresses). |
| `phone` | Yes* | String | The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format. |
| `limit` | No | Integer | The limit on the maximum number of results returned. Default (and max) limit is 100. |
| `offset`  |  No | Integer | Number of templates to skip before returning the rest of the templates that fit the search criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
{% endalert %}

### Example Request
`https://rest.iad-03.braze.com/subscription/user/status?external_id=12345&email=foo@bar.com&limit=100&offset=1`

### Example Request for multiple users
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`

### Example Request for SMS
```
curl --location --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id=123456789&limit=100&offset=0&phone=+11112223334' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

### Example Request for Email
```
curl --location --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id=123456789&email=foo@bar.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

{% endapi %}
