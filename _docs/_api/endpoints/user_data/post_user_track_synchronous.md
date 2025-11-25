---
nav_title: "POST: Track users (synchronous)"
article_title: "POST: Track Users (Synchronous)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "This article outlines details about the synchronous Track user Braze endpoint."

---
{% api %}
# Track users (synchronous)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Use this endpoint to record custom events and purchases and update user profile attributes synchronously. This endpoint functions similarly to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track), which updates user profiles asynchronously.

{% alert important %}
This endpoint is currently in beta. Contact your Braze account manager if you’re interested in participating in this beta.
{% endalert %}

## Synchronous and asynchronous API calls

In an asynchronous call, the API will return the status code `201`, indicating that your request was successfully received, understood, and accepted. However, this does not mean that your request has been fully completed.

In a synchronous call, the API will return a status code `201`, indicating that your request was successfully received, understood, accepted, and completed. The call response will show select user profile fields as a result of the operation.

This endpoint has a lower rate limit than the `/users/track` endpoint (see [rate limit](#rate-limit) below). Each `/users/track/sync` request can contain only  one event object, one attribute object, **or** one purchase object. This endpoint should be reserved for user profile updates where a synchronous call is needed. For a healthy implementation, we recommend using `/users/track/sync` and `/users/track` together.

For example, if you're sending consecutive requests for the same user over a short period of time, race conditions are possible with the asynchronous `/users/track` endpoint, but with the `/users/track/sync` endpoint you can send those requests in sequence, each after receiving a `2XX` response.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.track.sync` permission.

Customers using the API for server-to-server calls may need to allowlist `rest.iad-01.braze.com` if they're behind a firewall.

## Rate limit

We apply a base speed limit of 500 requests per minute to this endpoint for all customers. Each `/users/track/sync` request can contain up to one event object, one attribute object, or one purchase object. Each object (event, attribute, and purchase arrays) can update one user each.

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
For each request component listed in the following table, you must include one of `external_id`, `user_alias`, `braze_id`, `email`, or `phone`.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | One attributes object | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | One event object | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | One purchase object | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Responses

When using this endpoint's [request parameters](#request-parameters), you should receive one of the following responses: a successful message or a message with fatal errors.

### Successful message

Successful messages return the following response, which includes information about the user profile data that Braze updated.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### Message with fatal errors

If your message has a fatal error, you'll receive the following response:

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

## Example requests and responses

### Update a custom attribute by external ID

#### Request

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Response

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Update a custom event by email

#### Request

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### Response

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### Update a purchase event by user alias

#### Request

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Response

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## Frequently asked questions

### Should I use the asynchronous or synchronous endpoint?

For most profile updates, the `/users/track` endpoint will work best because of its higher rate limit and flexibility to let you batch requests. However, the `/users/track/sync` endpoint is useful if you're experiencing race conditions due to rapid, consecutive requests for the same user.

### Does the response time differ from the `/users/track` endpoint?

With a synchronous call, the API waits until Braze completes the request to return a response. As a result, synchronous requests take longer on average than asynchronous requests to `/users/track`. For the majority of requests, you can expect a response within seconds.

### Can I send multiple requests at the same time?

Yes, as long as the requests are for different users, or each request updates different attributes, events, purchases for one user.

If you're sending multiple requests for a user, for the same attribute, event, or purchase, Braze recommends waiting for a successful response between each request to prevent race conditions from occurring.

### Why doesn't the response value match the one in my original request?

Although your request is completed, it's possible your custom attribute value didn't update. This can happen when your custom attribute update exceeds the maximum number of characters, exceeds array limits, or if the user does not exist in Braze and you have `_update_existing_only = true`.

In these cases, treat the response as an indication that your request, while completed, your desired update has not been made. Troubleshoot with the reasons why this may happen from above.

{% endapi %}
