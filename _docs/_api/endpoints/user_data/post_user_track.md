---
nav_title: "POST: Track users"
article_title: "POST: Track Users"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Track user Braze endpoint."

---
{% api %}
# Track users
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track
{% endapimethod %}

> Use this endpoint to record custom events and purchases and update user profile attributes.

{% alert note %}
Braze processes the data passed through API at face value, and customers should only pass deltas (changing data) to minimize unnecessary data point logging. To read more, refer to [Data points]({{site.baseurl}}/user_guide/data/data_points/). 
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.track` permission.

Customers using the API for server-to-server calls may need to allowlist `rest.iad-01.braze.com` if they're behind a firewall.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Request parameters

{% alert important %}
For each request component listed in the following table, one of `external_id`, `user_alias`, `braze_id`, `email`, or `phone` is required.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array of attributes objects | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array of event objects | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array of purchase objects | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example requests

### Update a user profile by email address

You can update a user profile by email address using the `/users/track` endpoint. 

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Update a user profile by phone number

You can update a user profile by phone number using the `/users/track` endpoint. This endpoint only works if you include a valid phone number.

{% alert important %}
If you include a request with both `email` and `phone`, Braze will use the email as the identifier.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Set subscription groups

This example shows how to create a user and set their subscription group within the user attributes object. 

Updating the subscription status with this endpoint will update the user specified by their `external_id` (such as User1) and update the subscription status of any users with the same email as that user (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### Example request to create an alias-only user

You can use the `/users/track` endpoint to create a new alias-only user by setting the `_update_existing_only` key with a value of `false` in the body of the request. If this value is omitted, the alias-only user profile will not be created. Using an alias-only user guarantees that one profile with that alias will exist. This is especially helpful when building a new integration as it prevents the creation of duplicate user profiles.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Responses

When using any of the aforementioned API requests, you should receive one of the following three general responses: a [successful message](#successful-message), a [successful message with non-fatal errors](#successful-message-with-non-fatal-errors), or a [message with fatal errors](#message-with-fatal-errors).

### Successful message

Successful messages will be met with the following response:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Successful message with non-fatal errors

If your message is successful but has non-fatal errors, such as one invalid event object out of a long list of events, then you will receive the following response:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

For success messages, any data not affected by an error in the `errors` array will still be processed. 

### Message with fatal errors

If your message has a fatal error, you will receive the following response:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

If you receive the error "provided external_id is blacklisted and disallowed", your request may have included a "dummy user." For more information, refer to [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Frequently asked questions

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### What happens when multiple profiles with the same email address are found?
If the `external_id` exists, the most recently updated profile with an external ID will be prioritized for updates. If the `external_id` doesn't exist, the most recently updated profile will be prioritized for updates.

### What happens if no profile with the email address currently exists?
A new profile will be created, and an email-only user will be created. An alias will not be created. The email field will be set to test@braze.com, as noted in the example request for updating a user profile by email address.

### How do you use `/users/track` to import legacy user data?
You may submit data through the Braze API for a user who has not yet used your mobile app to generate a user profile. If the user subsequently uses the application all information following their identification using the SDK will be merged with the existing user profile you created using the API call. Any user behavior recorded anonymously by the SDK before identification will be lost upon merging with the existing API-generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded using the User API who have not yet engaged with the app, add the `Session Count > 0` filter.

### How does `/users/track` handle duplicate events?

Each event object in the events array represents a single occurrence of a custom event by a user at a designated time. This means each event ingested into Braze has its own event ID, so "duplicate" events are treated as separate, unique events.

### How does `/users/track` handle invalid nested custom attributes?

When a nested custom attribute contains any invalid values (such as invalid time formats or null values), all nested custom attribute updates in the request will be dropped from processing. This applies to all nested structures within that specific attribute. To ensure successful processing, verify that all values within nested custom attributes are valid before sending.

## Monthly Active Users CY 24-25
For customers who have purchased Monthly Active Users - CY 24-25, Braze manages different rate limits on its `/users/track` endpoint:
- Hourly rate limits are set according to the expected data ingestion activity on your account, which may correspond to the number of monthly active users you have purchased, industry, seasonality, or other factors.
- In addition to the hourly limit, Braze enforces a burst limit on the number of requests that can be sent every three seconds.
- Each request may batch up to 50 updates combined across attribute, event, or purchase objects.

Current limits based on expected ingestion can be found in the dashboard under **Settings** > **APIs and Identifiers** > **API Usage Dashboard**. We may modify rate limits to protect system stability or allow for increased data throughput on your account. Please contact Braze Support or your customer success manager for questions or concerns regarding hourly or per-second request limit and the needs of your business.



{% endapi %}
