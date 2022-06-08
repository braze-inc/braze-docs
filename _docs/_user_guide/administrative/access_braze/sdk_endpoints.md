---
nav_title: SDK Endpoints
article_title: SDK Endpoints
page_order: 1
page_type: reference
description: "This reference article covers Braze's SDK Endpoints and their use."

---

# SDK endpoints

## What is an SDK?

A Software Development Kit (SDK) is a set of tools that can be used to develop software applications targeting a specific platform. The Braze SDK makes it possible to track your users' engagement with your app or site and allows the sending of targeted campaigns. Learn more about the Braze SDK in our Braze Learning course, [Braze 101][85].

## Braze SDK endpoints

|Instance | SDK Endpoint
|---|---|
|US-01 | sdk.iad-01.braze.com |
|US-02 | sdk.iad-02.braze.com |
|US-03 | sdk.iad-03.braze.com |
|US-04 | sdk.iad-04.braze.com |
|US-05 | sdk.iad-05.braze.com |
|US-06 | sdk.iad-06.braze.com |
|US-08 | sdk.iad-08.braze.com |
|EU-01 | sdk.fra-01.braze.eu |
|EU-02 | sdk.fra-02.braze.eu |
{: .reset-td-br-1 .reset-td-br-2}

When using endpoints for SDK integration, use the **SDK Endpoint** listed on this page, not the [REST endpoint][2] used for API calls.

{% alert note %}
To configure the Braze Web SDK to use the appropriate endpoint for your integration, you must use the `baseUrl` option when initializing the function and include the SDK endpoint here. For example `braze.initialize('YOUR-API-KEY-HERE', {baseUrl: 'sdk.iad-03.braze.com'})`
<br><br>For more information, check out our [initial setup guide][1].
{% endalert %}

## SDK file sizes

| Platform | Approximate SDK Size |
|---|---|
| Android | 800 KB |
| iOS | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web | 36KB (core), 50KB (core + UI) |
{: .reset-td-br-1 .reset-td-br-2}

[85]: https://learning.braze.com/braze-101
[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[2]: {{site.baseurl}}/api/basics/#endpoints
