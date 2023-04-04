---
nav_title: "POST: Track User"
article_title: "POST: Track User"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the User Track Braze endpoint."

---
{% api %}
# Track users
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track
{% endapimethod %}

Use this endpoint to record custom events, purchases, and update user profile attributes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

{% alert note %}
Braze processes the data passed via API at face value and customers should only pass deltas (changing data) to minimize unnecessary data point consumption. To read more, refer to [Data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#data-points). 
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users track' %}

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

{% alert important %}
For each of the request components listed in the following table, one of `external_id`, `user_alias`, or `braze_id` is required.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array of attributes objects | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array of event objects | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array of purchase objects | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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

## Example request for updating a user profile by email address

{% alert important %}
Updating a user profile by email address with this endpoint is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

Using the `/users/track` endpoint, you can update a user profile by email address. You'll need to generate an API key with `users.track` permissions to use this endpoint.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
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
}`
```

### Frequently asked questions

#### What happens when multiple profiles with the same email address are found?
If the `external_id` exists, the most recently updated profile with an external ID will be prioritized for updates. If the `external_id` doesn't exist, the most recently updated profile will be prioritized for updates.

#### What happens if no profile with the email address currently exists?
A new profile will be created and an email-only user will be created.  There will be no alias created. The email field will be set to test@braze.com as noted in the example request for updating a user profile by email address.

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user_identifier",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user_identifier",
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
            "external_id": "user_identifier",
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
}`
```

## Example request to set subscription groups

This example shows how you can create a user and set their subscription group within the user attributes object. 

Updating the subscription status with this endpoint will both update the user specified by their `external_id` (such as User1) and update the subscription status of any users with the same email as that user (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups" : [{
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

## Responses

When using any of the aforementioned API requests, you should receive one of the following three general responses:

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

If your message is successful but has non-fatal errors, such as one invalid event object out of a long list of events, then you will receive the following response:

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

For success messages, any data that was not affected by an error in the `errors` array will still be processed. 

### Message with fatal errors

If your message has a fatal error, you will receive the following response:

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

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

If you receive the error "provided external_id is blacklisted and disallowed", your request may have included a "dummy user". For more information, refer to [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Creating an alias-only user profile

You can use the `/users/track` endpoint to create a new alias-only user by setting the `_update_existing_only` key with a value of `false` in the body of the request. If this value is omitted, the alias-only user profile will not be created. Using an alias-only user guarantees that one profile with that alias will exist. This is especially helpful when building a new integration as it prevents the creation of duplicate user profiles.

### Example request to create an alias-only user
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
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
}
```

## Importing legacy user data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API-generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API who have not yet engaged with the app, simply add the filter: `Session Count > 0`.

## Making bulk updates

If you have a use case where you need to make batch updates to the `users/track` endpoint, we recommend adding the bulk update header so that Braze can properly identify, observe, and route your request.

Refer to the following sample request with the `X-Braze-Bulk` header:

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'X-Braze-Bulk: true' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{ "attributes": [ ], "events": [ ], "purchases": [ ] }'
```

{% alert warning %}
When the `X-Braze-Bulk` header is present with any value, Braze will consider the request a bulk request. Set the value to `true`. Currently, setting the value to `false` does not disable the header—it will still be treated as if it were true.
{% endalert %}

### Use cases

Consider the following use cases where you may use the bulk update header:

- A daily job where multiple users' custom attributes are updated via the `/users/track` endpoint.
- An ad-hoc user data backfill script which updates user information via the `/users/track` endpoint.

{% endapi %}
