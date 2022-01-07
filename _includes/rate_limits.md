
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/users/track-->

{% if include.endpoint == "/users/track" %}
We apply a base speed limit of 50,000 requests per minute to this endpoint for all customers. Each request to the `/users/track` endpoint can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each for a max of 225 individual users. Each update can also belong to the same user for a max of 225 updates to a single user in a request. 

See our page on [API rate limits]({{site.baseurl}}api/api_limits/) for details, and reach out to your Customer Success Manager if you need your limit increased.
{% endif %}

<!---/users/export/ids-->

{% if include.endpoint == "/users/export/ids %}
We apply a rate limit of 2,500 requests per minute to this endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)
{% endif %}

<!---/users/delete-->

{% if include.endpoint = "/users/delete %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint, shared with the `/users/alias/new` and `/users/identify` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/users/alias/new-->

{% if include.endpoint = "/users/alias/new %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint, shared with the `/users/delete` and `/users/identify` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/users/identify-->

{% if include.endpoint = "/users/identify %}
We apply a shared rate limit of 20,000 requests per minute to this endpoint, shared with the `/users/alias/new` and `/users/delete` endpoints, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/events/list-->

{% if include.endpoint == "/events/list" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint, shared with the `/purchases/product_list` endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/purchases/product_list-->

{% if include.endpoint == "/purchases/product_list" %}
We apply a shared rate limit of 1,000 requests per hour to this endpoint, shared with the `/events/list` endpoint, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/).
{% endif %}

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% if include.endpoint == "send endpoints" %}
When specifying a segment or Connected Audience in your request, we apply a rate limit of 250 requests per minute to this endpoint. Otherwise, if specifying an `external_id`, this endpoint has a default rate limit of 250,000 requests per hour.
{% endif %}

<!---/sends/id/create-->

{% if include.endpoint == "/sends/id/create" %}
The daily maximum number of custom send identifiers that can be created via this endpoint is 100 for a given app group. Each `send_id` and `campaign_id` combination that you create will count towards your daily limit. The response headers for any valid request include the current rate limit status, see [API rate limits]({{site.baseurl}}/api/api_limits/) for details.
{% endif %}