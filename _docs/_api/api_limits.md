---
nav_title: Rate Limits
article_title: API Rate Limits
page_order: 4.5
description: "This reference article covers API rate limits for the Braze API infrastructure."
page_type: reference

---

# API rate limits

> The Braze API infrastructure is designed to handle high volumes of data across our customer base. To this end, we enforce API rate limits per app group. 

A rate limit is the number of requests the API can receive in a given time period. Many load-based denial-of-service incidents in large systems are unintentional—caused by errors in software or configurations—not malicious attacks. Rate limits ensure that such errors don't deprive our customers of Braze API resources. If too many requests are sent in a given time frame, you may see error responses with a status code of `429`, which indicates the rate limit has been hit.

{% alert warning %}
API rate limits are subject to change depending on the proper usage of our system. We encourage sensible limits when making an API call to prevent damage or misuse.
{% endalert %}

## Rate limits by request type

The following table lists the default API rate limits for different request types. All other requests not listed in this table have a default rate limit of 250,000 requests per hour. 

These default limits can be increased upon request. Reach out to your customer success manager for more information.

| Request Type | Default API Rate Limit |
| --- | --- |
| [`/users/track`][10] | **Requests:** 50,000 requests per minute.<br><br>**Batching:** 75 events, 75 purchases, and 75 attributes per API request. See [Batching User Track requests](#batch-user-track) for more. |
| [`/users/export/ids`][11] | 2,500 requests per minute. |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44] | 20,000 requests per minute, shared between the endpoints. |
| [`/users/external_id/rename`][20] | 1,000 requests per minute. |
| [`/users/external_id/remove`][21] | 1,000 requests per minute. |
| [`/events/list`][15] | 1,000 requests per hour, shared with the `/purchases/product_list` endpoint. |
| [`/purchases/product_list`][16] | 1,000 requests per hour, shared with the `/events/list` endpoint. |
| [`/messages/send`][17] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/campaigns/trigger/send`][17.1] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/canvas/trigger/send`][17.2] | 250 requests per minute when specifying a segment or Connected Audience. Otherwise, 250,000 requests per hour. |
| [`/sends/id/create`][18] | 100 requests per day. |
| [`/subscription/status/set`][19] | 5,000 requests per minute. |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28] | 1,000 requests per minute, per app group. |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30] | 10 requests per minute, per app group. |
| [`DELETE: /catalogs/{catalog_name}`][31]<br>[`GET: /catalogs`][32]<br>[`POST: /catalogs`][33] | 5 requests per minute shared between the endpoints. |
| [`DELETE: /catalogs/{catalog_name}/items`][34]<br>[`PATCH: /catalogs/{catalog_name}/items`][35]<br>[`POST: /catalogs/{catalog_name}/items`][36] | 100 requests per minute shared between the endpoints. |
| [`DELETE: /catalogs/{catalog_name}/items/{item_id}`][37]<br>[`GET: /catalogs/{catalog_name}/items/{item_id}`][38]<br>[`GET: /catalogs/{catalog_name}/items`][39]<br>[`PATCH: /catalogs/{catalog_name}/items/{item_id}`][40]<br>[`POST: /catalogs/{catalog_name}/items/{item_id}`][41] | 50 requests per minute shared between the endpoints. |
| [`GET: /scim/v2/Users/YOUR_ID_HERE`][22]<br>[`GET: /scim/v2/Users?filter=userName eq "user@test.com"`][43]<br>[`PUT: /scim/v2/Users/YOUR_ID_HERE`][25]<br>[`DELETE: /scim/v2/Users/YOUR_ID_HERE`][24]<br>[`POST: /scim/v2/Users/`][23] | 5,000 requests per day, per company, shared between the endpoints. |
{: .reset-td-br-1 .reset-td-br-2}

## Batching API requests

Braze's APIs are built to support batching. With batching, Braze can take in as much data as possible in a single API call so that you don't need to make a lot of API calls. It's more efficient for Braze to process data in batches than to process data one call at a time. For example, handling 1,000 batched API calls requires less resources than handling 75,000 individual calls. Batching is extremely important for any application that may require more than 75,000 calls per hour.

{% alert note %}
REST API rate limit increases are considered based on need for customers who are making use of the API batching capabilities.
{% endalert %}

### Batching User Track requests {#batch-user-track}

Each `/users/track` request can contain up to 75 event objects, 75 attribute objects, and 75 purchase objects. Each object (event, attribute, and purchase arrays) can update one user each. In total, this means a max of 225 users can be updated in a single call. In addition, a single user profile can be updated by multiple objects.

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

If you have questions about API limits, contact your customer success manager or open a [support ticket][support].

### Optimal delay between endpoints

{% alert note %}
We recommend that you allow for a 5-minute delay between consecutive endpoint calls to minimize errors.
{% endalert %}

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
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
