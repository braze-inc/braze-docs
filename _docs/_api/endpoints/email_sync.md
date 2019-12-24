---
nav_title: Email Lists & Addresses
page_order: 0
layout: api_page
excerpt_separator: ""
---

{% api %}

## Retrieve List of or Query Email Unsubscribes

{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

{% apitags %}
Get,Email Lists & Addresses,Subscriptions
{% endapitags %}

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/QueryingAllEmailUnsubscribesExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

### Query Parameters

You must provide an `end_date`, as well as either an `email` or a `start_date` .

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `sort_direction` | No | String | Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. |
| `email` | No * | String | If provided, we will return whether or not the user has unsubscribed |

>  If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

#### Sample Response

Entries are listed in descending order.

```json
{
  "emails": [
    {
      "email": "foo@braze.com",
      "unsubscribed_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "bar@braze.com",
      "unsubscribed_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "baz@braze.com",
      "unsubscribed_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```

{% endapi %}

{% api %}

## Querying Hard Bounced Emails

{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

{% apitags %}
Get,Email Lists & Addresses,Bounces
{% endapitags %}

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS.

{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

### Query Parameters

You must provide an `end_date`, as well as either an `email` or a `start_date` .

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve hard bounces, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `email` | No * | String | If provided, we will return whether or not the user has hard bounced |

>  If your date range has more than `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

#### Sample Response

Entries are listed in descending order.

```json
{
  "emails": [
    {
      "email": "foo@braze.com",
      "hard_bounced_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "bar@braze.com",
      "hard_bounced_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "baz@braze.com",
      "hard_bounced_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```

{% endapi %}


{% api %}

## Change User's Email Subscription Status

{% apimethod post %}
/email/status
{% endapimethod %}

{% apitags %}
Post,Email Lists & Addresses,Subscriptions
{% endapitags %}

This endpoint allows you to set the email subscription state for your users. Users can be `opted_in`, `unsubscribed`, or `subscribed` (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.

`Content-Type: application/json`

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/ChangingEmailSubscriptionStatusExample {% endapiref %}
{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

### Request Body

```json
{
  "api_key": "{{api_key}}",
  "email": "example@123.com",
  "subscription_state": "subscribed"
}
```

#### Parameters

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | See App Group REST API Key in Parameter Definitions. |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
| `subscription_state` | Yes | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |

{% endapi %}

{% api %}

## Remove Hard Bounces

{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

{% apitags %}
Post,Email Lists & Addresses,Bounces
{% endapitags %}

This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

`Content-Type: application/json`

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingHardBouncedEmailExample {% endapiref %}
{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

### Request Body

```json
{
  "api_key": "{{api_key}}",
  "email": "example@123.com"
}
```

#### Parameters

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |

{% endapi %}

{% api %}

## Remove Spam

{% apimethod post %}
/email/spam/remove
{% endapimethod %}

{% apitags %}
Post,Email Lists & Addresses,Spam
{% endapitags %}

This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.

`Content-Type: application/json`

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingSpamListEmailExample {% endapiref %}
{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

### Request Body

```json
{
  "api_key": "{{api_key}}",
  "email": "example@123.com"
}
```

#### Parameters

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | See App Group REST API Key in Parameter Definitions. |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |

### Example Unsubscribe CURL

The following example CURL demonstrates how to unsubscribe a user from receiving email via the Braze APIs:

```
curl -X POST -H "Content-Type: application/json" -d '{"api_key":"YOUR_APP_GROUP_REST_API_KEY","email":"EMAIL_TO_UNSUBSCRIBE","subscription_state":"unsubscribed"}' https://rest.iad-01.braze.com/email/status
```
{% endapi %}

[1]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[4]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
