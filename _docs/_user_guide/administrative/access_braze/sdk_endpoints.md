---
nav_title: API and SDK endpoints
article_title: API and SDK Endpoints
page_order: 1
page_type: reference
description: "This reference article lists the dashboard URLs, API endpoints, and SDK endpoints for available Braze instances."

---

# API and SDK endpoints

> Your Braze instance determines the URL required to log into Braze, access the API, and integrate your SDK. Learn more about the Braze SDK in our Braze Learning course, [Braze 101](https://learning.braze.com/braze-101).

Braze manages a number of different instances for our dashboard, SDK, and REST endpoints, which we call "clusters." Your Braze onboarding manager will let you know which cluster you're on.

Logging in at [dashboard.braze.com](https://dashboard.braze.com) will automatically send you to the right cluster address.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
When integrating your SDK, use the SDK endpoint. When making calls to our REST API, use the REST endpoint.
{% endalert %}

For details about accessing the API, see our [API overview article]({{site.baseurl}}/api/basics/). 
