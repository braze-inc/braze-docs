---
nav_title: Braze Instances
article_title: Braze Instances
page_order: 0
page_type: reference
description: "This reference article lists the dashboard URLs and endpoints for available Braze instances."

---

# Braze Instances

_This is the URL Braze Users need to log into Braze, access the API, and integrate your SDK_

Braze manages a number of different instances for our dashboard, SDK, and REST Endpoints, which we call "clusters." Your Braze onboarding manager will let you know which cluster you're on.

Logging in at [dashboard.braze.com](https://dashboard.braze.com) will automatically send you to the right cluster address.

|Instance|URL|REST Endpoint|SDK Endpoint|
|---|---|---|
|US-01| https://dashboard-01.braze.com | https://rest.iad-01.braze.com | https://sdk.iad-01.braze.com |
|US-02| https://dashboard-02.braze.com | https://rest.iad-02.braze.com | https://sdk.iad-02.braze.com |
|US-03| https://dashboard-03.braze.com | https://rest.iad-03.braze.com | https://sdk.iad-03.braze.com |
|US-04| https://dashboard-04.braze.com | https://rest.iad-04.braze.com | https://sdk.iad-04.braze.com |
|US-05| https://dashboard-05.braze.com | https://rest.iad-05.braze.com | https://sdk.iad-05.braze.com |
|US-06| https://dashboard-06.braze.com | https://rest.iad-06.braze.com | https://sdk.iad-06.braze.com |
|US-08| https://dashboard-08.braze.com | https://rest.iad-08.braze.com | https://sdk.iad-08.braze.com |
|EU-01| https://dashboard-01.braze.eu | https://rest.fra-01.braze.eu | https://sdk.fra-01.braze.eu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
When integrating your SDK, use the "SDK Endpoint". When making calls to our REST API, use the "REST Endpoint".
{% endalert %}
