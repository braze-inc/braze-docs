---
nav_title: API and SDK Endpoints
article_title: API and SDK Endpoints
page_order: 1
page_type: reference
description: "This reference article lists the dashboard URLs, API endpoints, and SDK endpoints for available Braze instances."

---

# API and SDK endpoints

> Your Braze instance determines the URL required to log into Braze, access the API, and integrate your SDK. Learn more about the Braze SDK in our Braze Learning course, [Braze 101][1].

Braze manages a number of different instances for our dashboard, SDK, and REST endpoints, which we call "clusters." Your Braze onboarding manager will let you know which cluster you're on.

Logging in at [dashboard.braze.com](https://dashboard.braze.com) will automatically send you to the right cluster address.

|Instance|URL|REST Endpoint|SDK Endpoint|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
When integrating your SDK, use the SDK endpoint. When making calls to our REST API, use the REST endpoint.
{% endalert %}

For details about accessing the API, see the [API overview article][2]. 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/