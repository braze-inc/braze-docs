---
nav_title: "POST: User Track"
article_title: "POST: User Track"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the User Track Braze endpoint."
---

{% api %}
# User track
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

Use this endpoint to record custom events, purchases, and update user profile attributes.

User Track has a base speed limit of 50,000 requests per minute for all customers. Each request can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each (max of 225 individual users). Each update can also belong to the same user for a max of 225 updates to a single user in a request. Please see our page on API limits for details, and reach out to your Customer Success Manager if you need your limit increased.

{% alert note %}
Braze processes the data passed via API at face value and customers should only pass deltas (changing data) to minimize unnecessary data point consumption. To read more, check out our data point [documentation]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#data-points).
{% endalert %}


{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optional, array of attributes object),
   "events" : (optional, array of event object),
   "purchases" : (optional, array of purchase object),
}
```

Customers using the API for server-to-server calls may need to whitelist `rest.iad-01.braze.com` if they're behind a firewall.

### Request parameters

| Parameter    | Required | Data Type                   | Description                                                                                |
| ------------ | -------- | --------------------------- | ------------------------------------------------------------------------------------------ |
| `attributes` | Optional | Array of attributes objects | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events`     | Optional | Array of event objects      | See [events object]({{site.baseurl}}/api/objects_filters/event_object/)                    |
| `purchases`  | Optional | Array of purchase objects   | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/)              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
For each of the request components listed above, one of `external_id`, `user_alias`, or `braze_id` is required.
{% endalert %}

{% alert note %}
- When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to `false`.
- Updating the subscription status with this endpoint will not only update the user-specified by their `external_id` (e.g User1), but it will also update the subscription status of any users with the same email as that user (User1).
{% endalert %}

## Example request body for event tracking

```json
{
  "events": [
    {
      "external_id": "string",
      "name": "string",
      "time": "string"
    }
  ]
}
```

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
  {
    "external_id":"user_identifier",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ],
    "events": [
    {
      "external_id": "user_identifier",
      "app_id" : "app_identifier",
      "name": "watched_trailer",
      "time": "2013-07-16T19:20:30+1:00"
    }  
   ],
  "purchases": [
     {
      "external_id": "user_identifier",
      "app_id": "app_identifier",
      "product_id": "product_name",
      "currency": "USD",
      "price": 12.12,
      "quantity": 6,
      "time": "2017-05-12T18:47:12Z",
      "properties": {
         "integer_property": 3,
         "string_property": "Russell",
         "date_property": "2014-02-02T00:00:00Z"
       } 
     }
  ]
}'
```

## Responses

Upon using any of the aforementioned API requests you should receive one of the following three general responses:

### Successful message

Successful messages will be met with the following response:

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Successful message with non-fatal errors

If your message is successful but has non-fatal errors such as one invalid Event Object out of a long list of events you will receive the following response:

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

### Message with fatal errors

In the case of a success, any data that was not affected by an error in the _errors_ array will still be processed. If your message has a fatal error you will receive the following response:

```json
{
  "message" : <fatal error message>,
  "errors" : [
    {
      <fatal error message>
    }
  ]
}
```

### Fatal error response codes

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code         | Reason / Cause                                                    |
| ------------------ | ----------------------------------------------------------------- |
| `400 Bad Request`  | Bad Syntax.                                                       |
| `401 Unauthorized` | Unknown or missing REST API Key.                                  |
| `404 Not Found`    | Unknown REST API Key (if provided).                               |
| `429 Rate Limited` | Over rate limit.                                                  |
| `5XX`              | Internal server error, you should retry with exponential backoff. |
{: .reset-td-br-1 .reset-td-br-2}

If you receive the error "provided external_id is blacklisted and disallowed", your request may have included a "dummy user". For more information, refer to [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Importing legacy user data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API-generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API who have not yet engaged with the app you should add the filter -- `Session Count > 0`.

## Making bulk updates

If you have a use case where you need to make batch updates to the `users/track` endpoint, we recommend adding the bulk update header so that Braze can properly identify, observe, and route your request.

Refer to the following sample request with the `X-Braze-Bulk` header:

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'X-Braze-Bulk: true' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{ "attributes": [ ], "events": [ ], "purchases": [ ], "partner": "PARTNER-NAME-HERE" }'
```

{% alert warning %}
When the `X-Braze-Bulk` header is present with any value, Braze will consider the request a bulk request. Please set the value to `true`. Currently, setting the value to `false` does not disable the header—it will still be treated as if it were true.
{% endalert %}

### Use cases

Some use cases in which you might use the bulk update header include:

- A daily job where multiple users' custom attributes are updated via the `/users/track` endpoint.
- An ad-hoc user data backfill script which updates user information via the `/users/track` endpoint.

{% endapi %}
