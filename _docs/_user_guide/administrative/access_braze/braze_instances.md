---
nav_title: Braze Instances
page_order: 0
---

# Braze Instances

_This is the URL Braze Users need to log into Braze, access the API, and integrate your SDK_

Braze manages a number of different instances for our dashboard, SDK, and REST Endpoints. When your account is provisioned, you will log into the corresponding URL below. You should bookmark your URL to make sure you are always logging into the right one.

|Instance|URL|REST Endpoint|SDK Endpoint|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `https://sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `https://sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `https://sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `https://sdk.iad-04.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `https://sdk.iad-06.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `https://sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `https://sdk.fra-01.braze.eu` |

{% alert important %}
When integrating your SDK, use the "SDK Endpoint", not the "REST Endpoint".

When using endpoints for API calls, use the "REST Enpoint".
{% endalert %}
