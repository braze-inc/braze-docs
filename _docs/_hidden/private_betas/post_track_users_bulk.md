---
nav_title: "POST: Track Users (Bulk)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "This article outlines details about the Track users (bulk) endpoint."
---

{% api %}
# Track users (bulk)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track/bulk
{% endapimethod %}

> Use this endpoint to record custom events and purchases and update user profile attributes in bulk.

{% alert important %}
This endpoint is currently in beta. Contact your Braze account manager if you're interested in participating in the beta.
{% endalert %}

## When to use this endpoint

Similar to the [POST: Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), you can use this endpoint to update user profiles. However, this endpoint is better suited for making bulk updates:

- **Larger requests:** This endpoint allows for 10,000 users per request, meaning that you have to make fewer requests to achieve your bulk update needs.
- **Prioritization:** During peak traffic conditions, requests from `/users/track` will be prioritized over requests from `/users/track/bulk`. Using both endpoints provides you with more control over data ingestion.

Note that user updates to this endpoint will not trigger any action-based campaigns or action-based Canvases, trigger any exception events, or track towards conversion metrics. User updates to this endpoint are available for segmentation and personalization.

Consider using this endpoint when you're backfilling many user profiles during onboarding or syncing large amounts of user profiles as part of a daily sync.

## Prerequisites

To use this endpoint, you’ll need an API key with the `users.track.bulk` permission.

If you're using the API for server-to-server calls, you may need to allowlist the endpoint (for example, `rest.iad-01.braze.com`) if you're behind a firewall. Refer to the [endpoints per instance]({{site.baseurl}}/api/basics#endpoints) for more information.

## Rate limit

We apply a base speed limit of 5 requests per second to this endpoint for all customers.

Each `/users/sync/bulk` request has a payload limit of 4&nbsp;MB, and may contain up to 10,000 event, attribute, or purchase objects.

Each object (event, attribute, and purchase arrays) can update one user each, meaning up to 10,000 different users can be updated in a single request. A single user profile can be updated with up to 100 objects in a single request.

{% alert note %}
If you need your rate limit increased, reach out to your customer success manager.
{% endalert %}


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

### Bulk update 10,000 user profiles in one request

You can update up to 10,000 user profiles. Here’s a truncated example where the request consists of 10,000 attribute objects:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Here’s an example where the request consists of both attribute and event objects:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
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
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

## Responses

### Successful messages

Successful messages will be met with the following response:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Successful message with non-fatal errors

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

#### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, refer to [Fatal errors and responses]({{site.baseurl}}/api/errors/#fatal-errors).

If you receive the error `provided external_id is blacklisted and disallowed`, your request may have included a “dummy user.” For more information, refer to [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Frequently asked questions

### Should I use this endpoint or regular `/users/track`?

We recommend using both.

For large user profile backfills and syncs where triggering for action-based campaigns and Canvases, conversion tracking, and exception events are not needed, use `/users/track/bulk`. 

For real-time use cases, use the `/users/track` endpoint.

### What identifiers can I use in /users/track/bulk?

One of `external_id`, `braze_id`, `user_alias`, `email`, or `phone` is required. For more examples, refer to our documentation for [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [events object]({{site.baseurl}}/api/objects_filters/event_object/), or [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/). 

### Can I include attributes, events, and purchases in 1 request?

Yes. You cam construct your request with any amount of attributes, events, and purchase objects up to 10,000 objects per request.


{% endapi %}
