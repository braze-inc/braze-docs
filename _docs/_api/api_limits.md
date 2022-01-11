---
nav_title: Rate Limits
article_title: API Rate Limits
page_order: 4.5
description: "This reference article covers API rate limits for the Braze API infrastructure."
page_type: reference

---

# API rate limits

The Braze API infrastructure is designed to handle high volumes of data across our customer base. To ensure responsible user of the API, we enforce API rate limits per app group. A rate limit is the the number of requests the API can receive in a given time period. If too many requests are sent in a given time frame, you may see error responses with a status code of `429`, which indicates the rate limit has been hit.

{% alert warning %}
API rate limits and their values (limited or unlimited) are subject to change depending on the proper usage of our system. We encourage sensible limits when making an API call to prevent damage or misuse.
{% endalert %}

## Rate limits by request type

The following table lists specific API rate limits for different request types. All other requests not listed in this table have a default rate limit of 250,000 requests per hour.

| Request Type | Default API Rate Limit |
| --- | --- |
| [`/users/track`][10] | **Requests:** 50,000 requests per minute. This limit can be increased upon request. Reach out to your Customer Success Manager for more information.<br><br>**Batching:** 75 events, 75 purchases, and 75 attributes per API request. See [Batching User Track requests](#batch-user-track) below for more. |
| [`/users/export/ids`][11] | 2,500 requests per minute. |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/identify`][14] | 20,000 requests per minute, shared between the endpoints. |
| [`/events/list`][15] | 1,000 requests per hour, shared with the `/purchases/product_list` endpoint. |
| [`/purchases/product_list`][16] | 1,000 requests per hour, shared with the `/events/list` endpoint. |
| [`/messages/send`][17] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/campaigns/trigger/send`][17.1] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/canvas/trigger/send`][17.2] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/sends/id/create`][18] | 100 requests per day. |
| [`/subscription/status/set`][19] | 5000 requests per minute. |
{: .reset-td-br-1 .reset-td-br-2}

## Batching API requests

Braze's APIs are built to support batching. With batching, Braze can take in as much data as possible in a single API call so that you don’t need to make a lot of API calls. It's more efficient for Braze to process data in batches than to process data one call at a time. For example, handling 1,000 batched API calls requires less resources than handling 75,000 individual calls. Batching is extremely important for any application that may require more than 75,000 calls per hour.

{% alert note %}
REST API rate limit increases are considered based on need for customers who are making use of the API batching capabilities.
{% endalert %}

### Batching User Track requests {#batch-user-track}

Each `/users/track` request can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each (max of 225 individual users). Each update can also belong to the same user for a maximum of 225 updates to a single user in a request.

Requests made to this endpoint will generally begin processing in this order: 

1. Attributes
2. Events
3. Purchases

### Batching Messaging endpoint requests

A single request to the [Messaging endpoints][1] can reach any one of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- An ad-hoc audience segment of any size, defined in the request as a [Connected Audience][2] object

## Monitoring your rate limits

Every single API request sent to Braze returns the following information in the response headers:

Header Name             | Description
----------------------- | -----------------------
`X-RateLimit-Limit`     | The maximum number of requests that you can make in a specified interval (your rate limit).
`X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window.
`X-RateLimit-Reset`     | The time at which the current rate limit window resets in UTC epoch seconds.
{: .reset-td-br-1 .reset-td-br-2}

This information is intentionally included in the header of the response to the API request rather than the Braze dashboard. This allows your system to better react in real time as you're interacting with our API. For example, if the `X-RateLimit-Remaining` value drops below a certain threshold, you might want to slow sending to ensure all transactional emails go out. Or, if it reaches zero, you might want to pause all sending until the time specified in `X-RateLimit-Reset` elapses.

If you have questions about API limits please contact your Customer Success Manager or open a [support ticket][support].

### Optimal delay between endpoints

> We recommend that you allow for a 5-minute delay between subsequent calls to minimize the probability of error.

Understanding the optimal delay between endpoints is crucial when making consecutive calls to the Braze API. Problems arise when endpoints depend on the successful processing of other endpoints, and if called too soon, could raise errors. For example, if you're assigning users an alias via our `/user/alias/new` endpoint, and then hitting that alias to send a custom event via our `/users/track` endpoint, how long should you wait?

Under normal conditions, the time for our data eventual consistency to occur is 10–100ms (1/10 of a second). However, there can be some cases where it takes longer for that consistency to occur. Therefore, we recommend that you allow for a 5-minute delay between making subsequent calls to minimize the probability of error.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/

[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
