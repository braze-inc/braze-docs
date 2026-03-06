---
nav_title: API and SDK endpoints
article_title: API and SDK Endpoints
page_order: 5
page_type: reference
description: "Look up the correct dashboard URL, REST API endpoint, and SDK endpoint for your Braze instance."

---

# API and SDK endpoints

> Look up the correct dashboard URL, REST API endpoint, and SDK endpoint for your Braze instance. You need these URLs to log in, make API calls, and integrate the SDK.

Braze manages a number of different instances for our dashboard, SDK, and REST endpoints, which we call "clusters." Your Braze onboarding manager will let you know which cluster you're on. To learn more about the Braze SDK, check out the [Braze 101](https://learning.braze.com/braze-101) Braze Learning course.

Logging in at [dashboard.braze.com](https://dashboard.braze.com) will automatically send you to the right cluster address.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
When integrating your SDK, use the SDK endpoint. When making calls to our REST API, use the REST endpoint.
{% endalert %}

For details about accessing the API, see our [API overview article]({{site.baseurl}}/api/basics/). 
