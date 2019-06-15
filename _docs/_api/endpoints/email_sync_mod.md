---
nav_title: Email Sync
page_order: 3
search_rank: 2
---
# Email Sync

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database.

## API Specification

All API requests are made over HTTPS. Below are the paths for each email sync endpoint:

| URL | HTTP Verb | Functionality |
| ---------------------| --------------- | --------------- |
| /email/unsubscribes | GET | Retrieving Objects|
| /email/status | POST | Creating Objects |
| /email/bounce/remove | POST | Removing Objects |
| /email/spam/remove | POST | Removing Objects |

Your Endpoint will correspond to your Braze Instance.

Instance  | REST Endpoint
-----------|-----------------------------------------
US-01 | `https://rest.iad-01.braze.com/email/`
US-02 | `https://rest.iad-02.braze.com/email/`
US-03 | `https://rest.iad-03.braze.com/email/`
US-04 | `https://rest.iad-04.braze.com/email/`
US-06 | `https://rest.iad-06.braze.com/email/`
EU-01 | `https://rest.fra-01.braze.eu/email/`

## Querying Unsubscribed Emails

```yaml
GET https://YOUR_REST_API_URL/email/unsubscribes
Content-Type: application/json

endpoint: unsubscribed emails
endpoint_url: /email/unsubscribes
method: get
description: get emails that have unsubscribed during the time period from `start_date` to `end_date`.
parameters: api_key(string), start_date(string), end_date(string), limit(integer), offset(integer), sort_direction(string), email(string)
request_body_example: 
response_body_parameters:
link_to_swagger: 'https://www.braze.com/docs/api/interactive/#/Email%20Sync/QueryingAllEmailUnsubscribesExample'
errors: 401
glossary_tags: email,user_data,get_method
```


emails that have unsubscribed during the time period from "start_date" to "end_date".

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- | --------------- | --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `sort_direction` | No | String | Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. |
| `email` | No * | String | If provided, we will return whether or not the user has unsubscribed |

\* You must provide either an `email` or a `start_date`, and an `end_date`.

>  If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

#### Sample response

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

## Querying Hard Bounced Emails

```yaml
GET https://YOUR_REST_API_URL/email/hard_bounces
Content-Type: application/json

endpoint: query hard bounced emails
endpoint_url: /email/hard_bounces
method: get
description: remove email addresses from the hard bounce list maintained by Braze and your email provider.
response_details: providing an email, or `start_date` and `end_date`, should respond with a list of invalid emails.
query_parameters: api_key(string), start_date(string), end_date(string), limit(integer), offset(integer), email(string)
query_example: 
response_body_parameters:
link_to_swagger:
errors:
glossary_tags: email, get_method

```

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- | --------------- | --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve hard bounces, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `email` | No * | String | If provided, we will return whether or not the user has hard bounced |

\* You must provide either an `email` or a `start_date`, and an `end_date`.

>  If your date range has more than `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

#### Sample response

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

## Changing Email Subscription Status

```yaml
POST https://YOUR_REST_API_URL/email/status
Content-Type: application/json

endpoint: email subscription status
endpoint_url: /email/status
method: post
description: user email subscription status can be updated and retrieved via Braze using a RESTful API
response_details: use to change user email subscription state.
query_parameters: api_key(required,string),email(string or array),subscription_state(string)
query_example: {
  "api_key": "123a45b6-cd78-9e01-g234-hi56j7k8l9m0",
  "email": [
    "name@email.com"
  ],
  "subscription_state": "Either “subscribed”, “unsubscribed”, or “opted_in”."
}
response_body_parameters: 
link_to_swagger: 'https://www.braze.com/docs/api/interactive/#/Email%20Sync/ChangingEmailSubscriptionStatusExample'
errors: 401
glossary_tags: email, post_method
```



This endpoint allows you to set the email subscription state for your users. Users can be "opted_in", "unsubscribed", or "subscribed" (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.


| Parameter | Required | Data Type | Description |
| ---------------------| --------------- | --------------- | --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
| `subscription_state` | Yes | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |

## Removing Hard Bounces

```yaml
POST https://YOUR_REST_API_URL/email/bounce/remove
Content-Type: application/json

endpoint: remove hard bounces
endpoint_url: /email/bounce/remove
method: post
description: use to remove email addresses from your Braze bounce list and your email provider.
response_details: success message when a given email is successfully removed from bounce list.
query_parameters: api_key(sring), email(string)
query_example:
response_body_parameters:
link_to_swagger: 'https://www.braze.com/docs/api/interactive/#/operations/Email%20Sync/RemovingHardBouncedEmailExample'
errors: 401
glossary_tags: email 
```

This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- | --------------- | --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |

## Removing Spam

This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.

```yaml
POST https://YOUR_REST_API_URL/email/spam/remove
Content-Type: application/json

endpoint: remove spam
endpoint_url: /email/spam/remove
method: post
description: use to remove spam email addresses from your Braze spam list and your email provider.
response_details: success message when a given spam email is successfully removed from list.
query_parameters: api_key(string), email(string)
query_example:
response_body_parameters: 
link_to_swagger: 'https://www.braze.com/docs/api/interactive/#/operations/Email%20Sync/RemovingSpamListEmailExample'
errors: 401
glossary_tags: email

```

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- | --------------- | --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |

### Example Unsubscribe CURL

The following example CURL demonstrates how to unsubscribe a user from receiving email via the Braze APIs:

```
curl -X POST -H "Content-Type: application/json" -d '{"api_key":"YOUR_APP_GROUP_REST_API_KEY","email":"EMAIL_TO_UNSUBSCRIBE","subscription_state":"unsubscribed"}' https://rest.iad-01.braze.com/email/status
```

[1]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[4]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
