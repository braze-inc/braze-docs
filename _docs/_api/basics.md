---
nav_title: Overview
article_title: API Overview
page_order: 0
description: "This reference article covers the API basics including what a REST API is, the terminology, a brief overview of API keys, and API limits."
page_type: reference

---
# API overview

> Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This reference article covers what a REST API is, the terminology, a brief overview of API keys, and API limits.

## What is a REST API?

A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints which perform various actions and/or return various data.

{% alert note %}
Customers using Braze's EU database should use the `https://rest.fra-01.braze.eu/` endpoint. This endpoint will be used when configuring the Braze [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#compile-time-endpoint-configuration-recommended), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml), and [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) SDKs.
{% endalert %}

## API definitions

Below is some terminology that you may see in the Braze REST API documentation and what it means.

### Endpoints

Braze manages a number of different instances for our dashboard and REST Endpoints. When your account is provisioned you will log in to one of the corresponding URLs below. Use the correct REST Endpoint based on which instance you are provisioned to. If you are unsure, open a [support ticket][support] or use the table below to match the URL of the dashboard you use to the correct REST Endpoint.

{% alert important %}
When using endpoints for API calls, use the "REST Endpoint" located below.

For SDK integration, use the ["SDK Endpoint"]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), not the "REST Endpoint".
{% endalert %}

|Instance|URL|REST Endpoint|SDK Endpoint|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Company secret explanation

The `company_secret` was formerly included with all API requests but has been deprecated as of October 2014. This field will be ignored for all future API requests to ensure backward compatibility.

### App group REST API keys

{% alert note %}
For a deeper dive on the different kinds of API Keys here at Braze, check out our dedicated <a href="{{site.baseurl}}/api/api_key/">API Keys</a> and <a href="{{site.baseurl}}/api/identifier_types/">API Identifier Types</a> reference articles.

{% endalert %}

The `api_key` included in each request acts as an authentication key that allows your server code to utilize our REST APIs. Within your company, each app group will have a unique set of REST API Keys. They can be found within the Braze dashboard by navigating to the Developer Console section for each app group. To use the REST API for any given App Group, you must create keys and give them permissions.

![REST API Keys][27]

#### API key permissions

API Keys are used to authenticate an API call. When you create a new REST API Key, you need to give it access to specific endpoints. By assigning specific permissions to an API Key, you can limit exactly which calls an API Key can authenticate.

A good security practice is to assign a user only as much access as is necessary to complete their job: this principle can also be applied to API Keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account.

![REST API Key Permissions][25]

{% alert warning %}
Given that REST API Keys allow access to potentially sensitive REST API endpoints, ensure they are stored and used securely. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.
{% endalert %}

If accidental exposure of a key occurs, it can be deleted from the [Developer Console][8]. For help with this process, please open a [support ticket][support].

#### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets which are allowed to make REST API requests for a given REST API Key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the **Whitelist IPs** section when creating a new REST API Key: 

![API IP Whitelisting][26]

If you don’t specify any, requests can be sent from any IP address.

{% alert tip %}
Making a Braze-to-Braze webhook and using allowlisting? Check out our list of [IPs to whitelist]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

#### Creating and managing REST API keys

![Create New API Key][28]{: style="max-width:20%;float:right;margin-left:15px;"}

To create a new REST API Key, visit the [Developer Console][8] on your Braze dashboard. This page displays your existing API Keys. To create a new key, click **Create New API Key**.

You can then to do the following:

- Give your new key a name for identification at a glance
- Select which permissions you would like to be associated with your new key
- Specify allowlisted IP addresses and subnets for the new key

Existing REST API Keys can be Viewed or Deleted by clicking the gear icon and selecting the corresponding option.

![API Key Options][29]

{% alert important %}
Keep in mind that once you create a new API Key, you cannot edit the scope of permissions or the allowlisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. Once you've completed your implementation, go ahead and delete the old key.
{% endalert %}

### External user ID explanation

The `external_id` serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze SDK in order to avoid creating multiple profiles for the same user.

### Braze user ID explanation

The `braze_id` serves as a unique user identifier that is set by Braze. This identifier can be used to delete users through the REST API in addition to external_ids.

#### More resources

For more information, refer to the following article based on your platform:

- [Setting User IDs - iOS][9]
- [Setting User IDs - Android][10]
- [Setting User IDs - Windows Universal][13]

## API limits

For most APIs, Braze has a default rate limit of 250,000 requests per hour. However, certain request types have their own rate limit applied to better handle high volumes of data across our customer base. For details, refer to [API rate limits]({{site.baseurl}}/api/api_limits/).

## Additional resources

### Ruby client library (MVP)

If you're implementing Braze using Ruby, you can use our [Ruby client library](https://github.com/braze-inc/braze-api-client-ruby) (MVP) to reduce your data import time.

A client library is a collection of code specific to one programming language—in this case, Ruby—that makes it easier to use an API. Because different languages make and process HTTP requests differently, a client library codifies requests as if they were native functionalities of a language. Additionally, they match the data types used in that language.

The Ruby client library supports the [User Endpoints]({{site.baseurl}}/api/endpoints/#user-data).

{% alert note %}
Want to help us make this library better? Send us feedback at [smb-product@braze.com](mailto:smb-product@braze.com) and let us know why the client library is or isn't helpful so that we can add to it over time.
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[8]: https://dashboard-01.braze.com/app_settings/developer_console/ "Developer Console"
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#setting-user-ids
[support]: {{site.baseurl}}/braze_support/
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
