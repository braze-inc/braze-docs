---
nav_title: Subscription Group REST APIs
page_order: 3.2
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

```json
GET https://YOUR_REST_API_URL/subscription/user/status
Content-Type: application/json
{
   "api_key": (required, string) your App Group REST API Key,
   "external_id": (required, string) the external_id of the user,
   "email_address": (required, string) the email address of the user (must include at least one address and at most 50 addresses)
   "limit": (optional, integer) limit on the maximum number of results returned. Default (and max) limit is 100
   "offset": (optional, integer) offset of returned result list. Default offset is 0. For example, if there are 230 users that matches API query, limit is set to 50, and offset is 0, the first 50 users will be returned in response. If offset is changed to 50, the next 50 users will be returned.
 }
```

{% alert tip %}
If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
{% endalert %}


## Getting the Subscription Status

Use the endpoints below to get the subscription state of a user in a subscription group. These groups will be available on the __Subscription Group__ page. The response from this endpoint will include a 0 (subscribed), 1 (unsubscribed), or null value for the specific subscription group requested in the API call.  This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/subscription/status/get`
US-02 | `https://rest.iad-02.braze.com/subscription/status/get`
US-03 | `https://rest.iad-03.braze.com/subscription/status/get`
US-04 | `https://rest.iad-04.braze.com/subscription/status/get`
US-06 | `https://rest.iad-06.braze.com/subscription/status/get`
EU-01 | `https://rest.fra-01.braze.eu/subscription/status/get`

```json
GET https://YOUR_REST_API_URL/subscription/status/get
Content-Type: application/json
{
   "api_key": (required, string) your App Group REST API Key,
   "subscription_group_id": (required, string) the id of your subscription group,
   "external_id": (required*, string) the external_id of the user,
   "email_address": (required*, string) the email address of the user
   //one of eternal_id or email_address is required
   //can be passed as an array of string with a max of 100
 }
```

_Example of API call request based on email_address (shown broken out for documentation purposes only)_

```json
GET https://YOUR_REST_API_URL/subscription/status/get?
api_key=12345&
subscription_group_id=111-222-333&
email=bob%40bigburgers.com
```

 _Example Response_

```json
Response: (status 200)
{
  "status": {
    "bob@bigburgers.com": "unsubscribed"
  },
  "message": "success"
}
```

_Example of API call request based on external_id (shown broken out for documentation purposes only)_

```json
Request:
GET https://YOUR_REST_API_URL/subscription/status/get?
api_key=12345&
subscription_group_id=111-222-333&
external_id=external-user-id-bob&
external_id=external-user-id-john
```

```json
Response: (status 200)
{
  "status": {
    "external-user-id-bob": "subscribed",
    "external-user-id-john": "unknown"
  },
  "message": "success"
}
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
   "subscription_group_state": (required, string) available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group),
   "external_id": (required*, string) the external_id of the user,
   "email_address": (required*, string) the email address of the user
   //one of eternal_id or email_address is required
   //can be passed as an array of string with a max of 100
 }
```

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
    "email": "john@braze.com"
  }
```

```json
Response: (status 201)
{
    "message": "success"
}
```


[support]: {{ site.baseurl }}/support_contact/
