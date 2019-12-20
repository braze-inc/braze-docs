---
nav_title: Subscription Groups
page_order: 3
---

# Subscription Group REST APIs

Use the Subscription Group REST APIs to programmatically manage the subscription groups that you have stored on the Braze dashboard, on the Subscription Group page.

## Get Users' Subscription Groups

Use the endpoints below to list and get the subscription groups of a certain user.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/subscription/user/status`
US-02 | `https://rest.iad-02.braze.com/subscription/user/status`
US-03 | `https://rest.iad-03.braze.com/subscription/user/status`
US-04 | `https://rest.iad-04.braze.com/subscription/user/status`
US-06 | `https://rest.iad-06.braze.com/subscription/user/status`
EU-01 | `https://rest.fra-01.braze.eu/subscription/user/status`

### Request Parameters

```
GET https://YOUR_REST_API_URL/subscription/user/status
```

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

## Getting the Subscription Status

Use the endpoints below to get the subscription state of a user in a subscription group. These groups will be available on the __Subscription Group__ page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call.  This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/subscription/status/get`
US-02 | `https://rest.iad-02.braze.com/subscription/status/get`
US-03 | `https://rest.iad-03.braze.com/subscription/status/get`
US-04 | `https://rest.iad-04.braze.com/subscription/status/get`
US-06 | `https://rest.iad-06.braze.com/subscription/status/get`
EU-01 | `https://rest.fra-01.braze.eu/subscription/status/get`

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `subscription_group_id`  | Yes | String | The `id` of your subscription group. |
| `external_id`  |  Yes* | String | The `external_id` of the user (must include at least one and at most 50 `external_ids`). |
| `email` | Yes* | String | The email address of the user. It can be passed as an array of string with a max of 50. |
| `phone` | No* | String | The phone number of the user. You must include _at least one_ phone number (if email is not included) and _at most 50 phone numbers_. The recommendation is to provide this in the `E.164 format`.|

_* Generally, either `external_id` or `email` is required. <br>  But, for SMS subscription groups, either `external_id` or `phone` is required. <br>  Must include `phone` or `email` value, but not both._

### Example Request

```
https://rest.iad-03.braze.com/subscription/user/status?api_key=23abc-def5-3729-owod-23f9f3j30&email=example%2B1%40braze.com
```

## Updating a Subscription State

Use the endpoints below to update the subscription state of a user on the Braze dashboard. You can access a subscription groups `subscription_group_id` by navigating to it on the Subscription Group page.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/subscription/status/set`
US-02 | `https://rest.iad-02.braze.com/subscription/status/set`
US-03 | `https://rest.iad-03.braze.com/subscription/status/set`
US-04 | `https://rest.iad-04.braze.com/subscription/status/set`
US-06 | `https://rest.iad-06.braze.com/subscription/status/set`
EU-01 | `https://rest.fra-01.braze.eu/subscription/status/set`

```json
POST https://YOUR_REST_API_URL/subscription/status/set
Content-Type: application/json
{
   "api_key": (required, string) your App Group REST API Key,
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group),
   "external_id": (required*, string) the external_id of the user,
   "email": (required*, string) the email address of the user
   //one of eternal_id or email is required
   //can be passed as an array of string with a max of 50
   //endpoint only accepts email or phone value, not both
   "phone": (optional, string in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers).
 }
```
> Only `external_id` or `phone` is accepted for SMS subscription groups


_Example of API call_

```json
POST https://YOUR_REST_API_URL/subscription/status/set
Content-Type: application/json
{
  Request:
  POST https://YOUR_REST_API_URL/subscription/status/set
  Body:
  {
    "api_key": "12345",
    "subscription_group_id": "111-222-333",
    "subscription_state": "unsubscribed",
    //endpoint only accepts email or phone value, not both
    "email": "john@braze.com",
    - or -
    "phone": "+14152342671"
  }
```

```json
Response: (status 201)
{
    "message": "success"
}
```
{% alert important %}
The endpoint only accepts the `email` or `phone` value, not both. If given both, you will receive this response: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

[support]: {{ site.baseurl }}/support_contact/
