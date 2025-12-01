---
nav_title: Rate limits
article_title: API Rate Limits
page_order: 4.5
description: "This reference article covers API rate limits for the Braze API infrastructure."
page_type: reference

---

# Rate limits

> The Braze API infrastructure is designed to handle high volumes of data across our customer base. To this end, we enforce API rate limits per workspace.

A rate limit is the number of requests the API can receive in a given time period. Many load-based denial-of-service incidents in large systems are unintentional—caused by errors in software or configurations—not malicious attacks. Rate limits check that such errors don't deprive our customers of Braze API resources. If too many requests are sent in a given time frame, you may see error responses with a status code of `429`, which indicates the rate limit has been hit.

{% alert warning %}
API rate limits are subject to change depending on the proper usage of our system. We encourage sensible limits when making an API call to prevent damage or misuse.
{% endalert %}

## Rate limits by request type

Refer to the following for the default API rate limits of different request types. These default limits can be increased upon request. Contact your customer success manager for more information.

### Requests with different rate limits

| Request Type                                                                                                                                                                                                                                           | Default API Rate Limit                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **Requests:** 3,000 requests per three seconds.<br><br>**Batching:** 75 events, 75 purchases, and 75 attributes per API request. See [Batching User Track requests](#batch-user-track) for more.<br><br>**Limits for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU :** see [guidance on limits here]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **If you onboarded on or after August 22, 2024:** 250 requests per minute. <br><br> **If you onboarded before August 22, 2024:** 2,500 requests per minute.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 20,000 requests per minute, shared between the endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1,000 requests per hour, shared with the `/purchases/product_list` endpoint.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1,000 requests per hour, shared with the `/events/list` endpoint.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 50,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | 250 requests per minute for broadcast calls (when only specifying a segment or Connected Audience). Otherwise, 250,000 requests per hour is shared between all endpoints that don't have their own rate limit.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 100 requests per day.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 5,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 10 requests per minute.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 50 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 16,000 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 50 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 requests per minute shared between the endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 5,000 requests per day, per company, shared between the endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 50 requests per minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 20 requests per minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 100 requests per minute.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Requests with shared rate limits

The following requests have a rate limit of 250,000 requests per hour, shared between them.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

## Batching API requests

Braze APIs are built to support batching. With batching, Braze can take in as much data as possible in a single API call so that you don't need to make a lot of API calls. It's more efficient for Braze to process data in batches than to process data one call at a time. For example, handling 1,000 batched API calls requires less resources than handling 75,000 individual calls. Batching is extremely important for any application that may require more than 75,000 calls per hour.

{% alert note %}
REST API rate limit increases are considered based on need for customers who are making use of the API batching capabilities.
{% endalert %}

### Batching requests for Track users endpoint {#batch-user-track}

Each `/users/track` request can contain up to 75 event objects, 75 attribute objects, and 75 purchase objects. Each object (event, attribute, and purchase arrays) can update one user each. In total, this means up to 225 users can be updated in a single call. In addition, a single user profile can be updated by multiple objects.

Requests made to this endpoint will generally begin processing in this order:

1. Attributes
2. Events
3. Purchases

### Batching Messaging endpoint requests

A single request to the [Messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) can reach any one of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- Users who match additional audience filters of any size, defined in the request as a [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/) object

### Example batch request

The following example uses `external_id` to make one API call for email and SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Monitoring your rate limits

Every single API request sent to Braze returns the following information in the response headers:

| Header Name             | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | The maximum number of requests that you can make in a specified interval (your rate limit). |
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window.                          |
| `X-RateLimit-Reset`     | The time at which the current rate limit window resets in UTC epoch seconds.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

This information is intentionally included in the header of the response to the API request rather than the Braze dashboard. This allows your system to better react in real time as you're interacting with our API. For example, if the `X-RateLimit-Remaining` value drops below a certain threshold, you might want to slow sending to make sure all transactional emails go out. Or, if it reaches zero, you might want to pause all sending until the time specified in `X-RateLimit-Reset` elapses.

{% alert note %}
HTTP headers will be returned in all lowercase characters. This behavior aligns with the HTTP/2 protocol that mandates all header field names must be lowercase. This differs from HTTP/1.X where header names were case-insensitive but were commonly written in various capitalizations.
{% endalert %}

If you have questions about API limits, contact your customer success manager or open a [support ticket]({{site.baseurl}}/braze_support/).

{% alert tip %}
You can use the [API usage dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) to view and compare incoming traffic against your rate limits.
{% endalert %}

### Optimal delay between endpoints

{% alert note %}
We recommend that you allow for a 5-minute delay between consecutive endpoint calls to minimize errors.
{% endalert %}

Understanding the optimal delay between endpoints is crucial when making consecutive calls to the Braze API. Problems arise when endpoints depend on the successful processing of other endpoints, and if called too soon, could raise errors. For example, if you're assigning users an alias through our `/user/alias/new` endpoint, and then hitting that alias to send a custom event through our `/users/track` endpoint, how long should you wait?

Under normal conditions, the time for our data eventual consistency to occur is 10–100ms (1/10 of a second). However, there can be some cases where it takes longer for that consistency to occur, so we recommend that you allow for a 5-minute delay between making subsequent calls to minimize the probability of error.

