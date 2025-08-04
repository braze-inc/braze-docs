
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the `/scim/v2/Users/` GET, DELETE, and POST endpoints as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the `/scim/v2/Users/` PUT, GET, DELETE, and POST endpoints as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the `/scim/v2/Users/` PUT, GET, and POST endpoints as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the `/scim/v2/Users/` PUT, GET, and DELETE endpoints as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the `/scim/v2/Users/` PUT, GET, DELETE, and POST endpoints as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
We apply a rate limit of 1,000 requests per minute to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Starting on October 28th, 2024, we apply a base speed limit of 3,000 requests per three seconds to this endpoint for all customers. Each `/users/track` request can contain up to 75 event objects, 75 attribute objects, and 75 purchase objects. Each object (event, attribute, and purchase arrays) can update one user each. In total, this means a maximum of 225 users can be updated in a single call. In addition, a single user profile can be updated by multiple objects.

Different limits apply to customers who have purchased **Monthly Active Users - CY 24-25**. For details on these limits, see [Monthly Active Users - CY 24-25 limits]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25).

See our page on [API rate limits]({{site.baseurl}}/api/api_limits/) for details, and reach out to your customer success manager if you need your limit increased.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
If you onboarded with Braze on or after August 22, 2024, this endpoint has a rate limit of 250 requests per minute, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

You can also increase this endpoint's rate limit to 40 requests per second by meeting the following requirements:

- Your workspace has the default rate limit (250 requests per minute) enabled. Contact your Braze account manager for further assistance with removing any pre-existing rate limit you may have.
- Your request includes the `fields_to_export` parameter to list out all the fields you want to receive.

{% alert important %}
If you include `canvases_received` or `campaigns_received` in the `fields_to_export` parameter, your request will be ineligible for the faster rate limit. We recommend only including these in your request if you have a specific use case for them.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/alias/new`, `/users/identify`, `/users/merge`, and `/users/alias/update` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete`, `/users/identify`, `/users/merge`, and `/users/alias/update` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete`, `/users/alias/new`, `/users/identify`, and `/users/merge` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete`, `/users/alias/new`, `/users/merge`, and `/users/alias/update` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete`, `/users/alias/new`, `/users/identify`, and `/users/alias/update` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/events`, `/events/list`, and `/purchases/product_list` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "events" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/custom_attributes`, `/events/list`, and `/purchases/product_list` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/custom_attributes`, `/events`, and `/purchases/product_list` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/custom_attributes`, `/events`, and `/events/list` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
When specifying a segment or Connected Audience in your request, we apply a rate limit of 250 requests per minute to this endpoint. Otherwise, if specifying an `external_id`, this endpoint has a default rate limit of 250,000 requests per hour shared between `/messages/send`, `/campaigns/trigger/send`, and `/canvas/trigger/send`, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
Braze Transactional Emails are not subject to a rate limit. Depending on your chosen package, a set number of transactional emails is covered per hour by SLA. Requests that exceed that rate will still send, but are not covered by SLA. 99.9% of emails will send in less than one minute.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
The daily maximum number of custom send identifiers that can be created via this endpoint is 100 for a given workspace. Each `send_id` and `campaign_id` combination that you create will count toward your daily limit. The response headers for any valid request include the current rate limit status, see [API rate limits]({{site.baseurl}}/api/api_limits/) for details.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
This endpoint has a rate limit of 5,000 requests per minute shared across the `/subscription/status/set` and `/v2/subscription/status/set` endpoint as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
This endpoint has a rate limit of 50 requests per minute.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
This endpoint has a rate limit of 20 requests per minute.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
This endpoint has a rate limit of 100 requests per minute.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze endpoints support [batching API requests]({{site.baseurl}}/api/api_limits/#batching-api-requests). A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- An audience segment of any size, defined in the request as a [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/) object

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze endpoints support [batching API requests]({{site.baseurl}}/api/api_limits/#batching-api-requests). A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- An audience segment of any size, defined in the request as a [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/) object

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

This endpoint has a rate limit of 250,000 requests per minute.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze endpoints support [batching API requests]({{site.baseurl}}/api/api_limits/#batching-api-requests). A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific `external_ids`
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- An audience segment of any size, defined in the request as a [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience/) object

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

This endpoint has a shared rate limit of 16,000 requests per minute between all asynchronous catalog item endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog item endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

This endpoint has a shared rate limit of 50 requests per minute between all asynchronous catalog fields and selections endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

This endpoint has a rate limit of 50,000 requests per minute.

{% endif %}

