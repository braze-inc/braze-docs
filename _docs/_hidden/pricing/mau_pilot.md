---
nav_title: MAU Pilot
permalink: "/mau_pilot/"
hidden: true
noindex: true
hide_toc: true
---

# Monthly Active Users - Pilot

Braze’s Monthly Active Users Pilot offers all of the same functionality as Braze, with some changes to the limits imposed on data ingestion. 

- Rate limits are enforced on Braze’s `/users/track` endpoint, and these limits are dependent on the number of MAU purchased. Rate limits may be increased by adding on one or more additional API Boosts.   
- Data Points, which are commonly referenced in Braze docs and enablement materials, are not limited for customers on the Monthly Active Users Pilot.
- All other rate limits documented in the Braze dashboard or documentation apply to your usage of Braze.

{% alert note %}
The applicable rate limit for `/users/track` endpoints is reflected on your order form, and in the Braze dashboard under Settings > APIs and Identifiers > API limits
{% endalert %}

## `/users/track` limits

### Request throughput 

Two limits apply to `/users/track` - a steady-state limit on requests per hour, and a burst limit on requests per second. Specific limits applicable to your company depend on contracted MAU and API Boost, and can be found under Settings > APIs and Identifiers > API limits. 

### Batching
Each request to `/users/track` may update up to 50 users in total across attributes, events, and purchases. If a request contains too many users, Braze will respond with a `400` error. 

### Response headers
Non-rate limited requests (all responses other than `429`) will include the following headers with details on the steady (hourly) rate limit remaining in the current period. These headers can be used to make sure you are sending requests at an appropriate rate:
- `X-RateLimit-Limit`: The maximum number of requests that you can make in a specified interval (your rate limit). This is the steady state limit reflected in the Braze dashboard   
- `X-RateLimit-Remaining`: The number of requests remaining in the current rate limit window   
- `X-RateLimit-Reset`: The time at which the current rate limit window resets in UTC epoch seconds   

Rate limited requests will receive a `429` response, and contain an HTTP header indicating when you should retry the request. 

- `X-RateLimit-RetryAfter`: number of seconds you should wait until making additional requests

### API Usage

All other information in the documentation for `/users/track` applies to companies in the Monthly Active Users Pilot. See these [docs]({{site.baseurl}}/docs/api/endpoints/user_data/post_user_track) for more details on expected request body format and responses, and other guidance on usage of these endpoints. 


If any functionality above is updated, this will be reflected in this article and noted in our [release notes]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).
