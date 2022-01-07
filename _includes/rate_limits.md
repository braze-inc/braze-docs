
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
We apply a base speed limit of 50,000 requests per minute to this endpoint for all customers. Each request to the `/users/track` endpoint can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each for a max of 225 individual users. Each update can also belong to the same user for a max of 225 updates to a single user in a request.

See our page on [API rate limits]({{site.baseurl}}/api/api_limits/) for details, and reach out to your Customer Success Manager if you need your limit increased.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
For customers who onboarded with Braze on or after August 16, 2021, we apply a rate limit of 2,500 requests per minute to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
For customers who onboarded with Braze on or after September 16, 2021, we apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/alias/new` and `/users/identify` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
For customers who onboarded with Braze on or after September 16, 2021, we apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete` and `/users/identify` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
For customers who onboarded with Braze on or after September 16, 2021, we apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the `/users/delete` and `/users/alias/new` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
For customers who onboarded with Braze on or after September 16, 2021, we apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/purchases/product_list` endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
For customers who onboarded with Braze on or after September 16, 2021, we apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the `/events/list` endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
When specifying a segment or Connected Audience in your request, we apply a rate limit of 250 requests per minute to this endpoint. Otherwise, if specifying an `external_id`, this endpoint has a default rate limit of 250,000 requests per hour, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send -->

{% elsif include.endpoint == "transactional email" %}
Transactional emails are not subject to a rate limit. Depending on your chosen package, a set number of transactional email are covered per hour by SLA. Requests that exceed that rate will still send, but are not covered by SLA. 99.9% of emails will send in less than one minute.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
The daily maximum number of custom send identifiers that can be created via this endpoint is 100 for a given app group. Each `send_id` and `campaign_id` combination that you create will count towards your daily limit. The response headers for any valid request include the current rate limit status, see [API rate limits]({{site.baseurl}}/api/api_limits/) for details.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze endpoints support [batching API requests]({{site.baseurl}}/api/api_limits/#batching-api-requests). A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- An ad-hoc audience segment of any size, defined in the request as a [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/) object

{% endif %}