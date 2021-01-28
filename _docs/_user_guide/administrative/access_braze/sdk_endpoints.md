---
nav_title: SDK Endpoints
page_order: 1
---

# SDK Endpoints

## What is an SDK?

A Software Development Kit (SDK) is a set of tools that can be used to develop software applications targeting a specific platform. The Braze SDK makes it possible to track your users' engagement with your app or site and allows the sending of targeted campaigns. Learn more about the Braze SDK in our LAB course, [Braze 101][85].

# Braze SDK Endpoints

|Instance | SDK Endpoint
|---|---|
|US-01 | sdk.iad-01.braze.com |
|US-02 | sdk.iad-02.braze.com |
|US-03 | sdk.iad-03.braze.com |
|US-04 | sdk.iad-04.braze.com |
|US-06 | sdk.iad-06.braze.com |
|EU-01 | sdk.fra-01.braze.eu |
{: .reset-td-br-1 .reset-td-br-2}

When using endpoints for SDK integration, use the __SDK Endpoint__ listed on this page, __not__ the [Rest Endpoint]({{site.baseurl}}/api/basics/#endpoints) used for API calls.

{% alert note %}
To configure the Braze Web SDK to use the appropriate endpoint for your integration, you must use the `baseUrl` option when initializing the function and include the SDK endpoint here. For example `appboy.initialize('YOUR-API-KEY-HERE', {baseUrl: 'sdk.iad-03.braze.com'})`
<br>For more information check out our <a href="https://github.com/Appboy/appboy-web-sdk#getting-started">Github Web SDK documentation</a>.
{% endalert %}

## Software Development Kit (SDK) File Sizes

| Platform | Approximate SDK Size |
|---|---|
| Android | 800 KB |
| iOS | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web | 35kb (core), 50kb (core + UI) |
{: .reset-td-br-1 .reset-td-br-2}

[85]: https://lab.braze.com/braze-101
