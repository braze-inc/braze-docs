---
nav_title: "POST: Track Users"
article_title: "POST: Track Users"
hidden: true
permalink: /post_user_track_synchronous/
layout: api_page
page_type: reference
description: "This article outlines details about the synchronous Track user Braze endpoint."

---
{% api %}
# Track users (synchronous)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track/sync
{% endapimethod %}

> Use this endpoint to record custom events and purchases and update user profile attributes synchronously. This endpoint functions similarly to the [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track), which updates user profiles asynchronously.

{% alert important %}
This endpoint is currently in beta. Contact your Braze account manager for 
{% endalert %}

## Synchronous and asynchronous API calls

In an asynchronous call, the API will return a 201 status code indicating that your request was successfully received, understood, and accepted. However, this does not mean that your request has been fully completed.

In a synchronous call, the API will return a 201 status code indicating that your request was successfully received, understood, accepted, and completed. The call response will show you select user profile fields as a result of that operation.

This endpoint has a lower rate limit than the POST: Track Users endpoint (see rate limits below). Each /users/sync/track request can contain only 1 event object, 1 attribute object, OR 1 purchase object. 

As such, this endpoint should be reserved for user profile updates where a synchronous call is needed. For a healthy implementation, we recommend using both /users/track/sync and /users/track together.

For example, if you're sending consecutive requests for the same user over a short period of time, race conditions are possible with the asynchronous /users/track endpoint, but with the /users/track/sync endpoint you can send those requests in sequence, each after receiving a `2XX` response.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.track.sync` permission.

Customers using the API for server-to-server calls may need to allowlist `rest.iad-01.braze.com` if they're behind a firewall.

## Rate limit

We apply a base speed limit of 500 requests per minute to this endpoint for all customers. Each `/users/sync/track/` request can contain up to 1 event object, 1 attribute object, or 1 purchase object. Each object (event, attribute, and purchase arrays) can update one user each.

Reach out to your customer success manager if you need your limit increased.


## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Request parameters

{% alert important %}
For each request component listed in the following table, one of `external_id`, `user_alias`, `braze_id`, `email`, or `phone` is required.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | One attributes object | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | One event object | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | One purchase object | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Responses

When using any of the aforementioned API requests, you should receive one of the following two general responses: a successful message or a message with fatal errors.

### Successful message

Successful messages will be met with the following response, which includes information about the user profile data that was updated.

```javascript
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
}
```


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
}'
```

### Update a user profile by phone number

You can update a user profile by phone number using the `/users/track` endpoint. This endpoint only works if you include a valid phone number.

{% alert important %}
If you include a request with both email and phone, Braze will use the email as the identifier.
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

## Frequently asked questions

### In what instances should I use the asynchronous or synchronous endpoint?

For most profile updates, `/users/track` endpoint will work best because of its higher rate limit and flexibility to let you batch requests. However, the `/users/track/sync` endpoint is useful if you are experiencing race conditions due to rapid, consecutive requests for the same user.

### Does response time differ compared to the `/users/track` endpoint?

With a synchronous call, the API waits until the request is completed to return a response. As a result, synchronous requests will take longer on average than asynchronous requests to /users/track. For the majority of requests, expect a response in seconds.

### Can you send multiple requests to this endpoint at the same time?

Yes, as long as the requests are for different users, or each request updates different attributes, events, purchases for one user.

If you are sending multiple requests for 1 user, for the same attribute, event, or purchase, it is recommended that you wait for a successful response between each request. This will prevent race conditions from occurring.

### Why does my response list a different custom attribute value than my original request?

It’s possible that although your request is completed, it still did not update. This can happen when your custom attribute update exceeds the max number of characters, exceeds array limits, or if the user does not exist in Braze and you have _update_existing_only = true.

In these cases, treat the response as an indication that your request, while completed, your desired update has not been made. Troubleshoot with the reasons why this may happen from above.

{% endapi %}