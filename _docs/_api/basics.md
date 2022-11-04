---
nav_title: "API Overview"
article_title: API Overview
page_order: 2.1
description: "This reference article covers the API basics including what a REST API is, the terminology, and an overview of API keys."
page_type: reference
alias: /api/api_key/
---

# API overview

> This reference article covers the API basics including common terminology and an overview of REST API keys, permissions, and how keep them secure. 

## API definitions

The following lists an overview of terms you may see in the Braze REST API documentation.

### Endpoints

Braze manages a number of different instances for our dashboard and REST Endpoints. When your account is provisioned you will log in to one of the following URLs. Use the correct REST endpoint based on which instance you are provisioned to. If you are unsure, open a [support ticket][support] or use the following table to match the URL of the dashboard you use to the correct REST Endpoint.

{% alert important %}
When using endpoints for API calls, use the "REST Endpoint".

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

### API limits

For most APIs, Braze has a default rate limit of 250,000 requests per hour. However, certain request types have their own rate limit applied to better handle high volumes of data across our customer base. For details, refer to [API rate limits]({{site.baseurl}}/api/api_limits/)

### User IDs 

- **External user ID**: The `external_id` serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze SDK in order to avoid creating multiple profiles for the same user.
- **Braze user ID**: `braze_id` serves as a unique user identifier that is set by Braze. This identifier can be used to delete users through the REST API in addition to external_ids.

For more information, refer to the following article based on your platform: [iOS][9], [Android][10], and [Web][13].

## REST API key

A REST Application Programming Interface key (REST API key) is a unique code that is passed into an API to authenticate the API call and identify the calling application or user. API access is done using HTTPS web requests to your company's REST API endpoint. We use REST API keys at Braze in tandem with our App Identifier keys to track, access, send, export, and analyze data to help make sure everything is running smoothly on both your and our end. 

App Groups and API Keys go hand in hand at Braze. App Groups are designed to house versions of the same application across multiple platforms. Many customers also use app groups to contain free and premium versions of their applications on the same platform. As you may notice, these app groups are also making use of the REST API and have their own REST API keys. These keys can be individually scoped to include access to specific endpoints on the API. Each call to the API must include a key with access to the endpoint hit.

We refer to both the REST API key and App Group API key as the `api_key`. The `api_key` is included in each request as a request header and acts as an authentication key that allows you to utilize our REST APIs. These REST APIs are used to track users, send messages, export user data, and more. When you create a new REST API key, you will need to give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

![REST API keys panel on the API Settings tab of the Developer Console.][27]

{% alert tip %}
In addition to REST API keys, there also exists a type of key called Identifier keys that can be used to reference specific things like apps, templates, Canvases, campaigns, Content Cards, and segments from the API. For more information, refer to [API Identifier types]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### REST API key permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls.

{% tabs %}
{% tab User Data %}

| Permission | Description  |
|---|---|---|
| `users.track` | Record user attributes, custom events, and purchases  |
| `users.delete` | Delete any user. |
| `users.alias.new` | Create a new alias for an existing user.  |
| `users.identify` | Query for user profile information by user ID.  |
| `users.export.ids` | Query for user profile information by identifier e.g., device_id, email_address, external_id.  |
| `users.export.segment` | Query for user profile information by Segment. |
| `users.external_ids.rename` | Rename a user's existing external ID. |
| `users.external_ids.remove` | Remove a user's deprecated external ID. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Email %}

| Name | Description |
|---|---|---|
| `email.unsubscribe` | Query for unsubscribed email addresses.  |
| `email.status` | Change email address status. |
| `email.hard_bounces` | Query for hard bounced email addresses. |
| `email.bounce.remove` | Remove email addresses from your hard bounce list. |
| `email.spam.remove` | Remove email addresses from your spam list. |
| `email.blacklist` | Blacklist email addresses. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Messages %}

| Name | Description |
|---|---|---|
| `messages.send` | Send an immediate, ad-hoc message to specific users. |
| `messages.schedule.create` | Schedule a message to be sent at a specific time. |
| `messages.schedule.update` | Update a scheduled message. |
| `messages.schedule.delete` | Delete a scheduled message. |
| `messages.schedule_broadcasts` | Query all scheduled broadcast messages. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Campaigns %}

| Name | Description |
|---|---|---|
| `campaigns.trigger.send` | Trigger the sending of an existing campaign. |
| `campaigns.trigger.schedule.create` | Schedule a future send of a campaign with API-triggered delivery. |
| `campaigns.trigger.schedule.update` | Update a campaign scheduled with API-triggered delivery. |
| `campaigns.trigger.schedule.delete` | Delete a campaign scheduled with API-triggered delivery |
| `campaigns.list` | Query for a list of campaigns. |
| `campaigns.data_series` | Query for campaign analytics over a time range. |
| `campaigns.details` | Query for details of a specific campaign. |
| `sends.data_series` | Query for message send analytics over a time range. |
| `sends.id.create` | Create Send ID for message blast tracking. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| Name | Description |
|---|---|---|
| `canvas.trigger.send` | Trigger the sending of an existing Canvas. |
| `canvas.trigger.schedule.create` | Schedule a future send of a Canvas with API-triggered delivery. |
| `canvas.trigger.schedule.update` | Update a Canvas scheduled with API-triggered delivery. |
| `canvas.trigger.schedule.delete` | Delete a Canvas scheduled with API-triggered delivery. |
| `canvas.list` | Query for a list of Canvases. |
| `canvas.data_series` | Query for Canvas analytics over a time range. |
| `canvas.details` | Query for details of a specific Canvas. |
| `canvas.data_summary` | Query for rollups of Canvas analytics over a time range. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Segments %}

| Name | Description |
|---|---|---|
| `segments.list` | Query for a list of Segments. |
| `segments.data_series` | Query for Segment analytics over a time range. |
| `segments.details` | Query for details of a specific Segment. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Purchases %}

| Name | Description |
|---|---|---|
| `purchases.product_list` | Query for a list of products purchased in your app. |
| `purchases.revenue_series` | Query for total money spent per day in your app over a time range. |
| `purchases.quantity_series` | Query for the total number of purchases per day in your app over a time range. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Events %}

| Name | Description |
|---|---|---|
| `events.list` | Query for a list of custom events. |
| `events.data_series` | Query occurrences of a custom event over a time range. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab News Feed %}

| Name | Description |
|---|---|---|
| `feed.list` | Query for a list of News Feed cards. |
| `feed.data_series` | Query for News Feed analytics over a time range. |
| `feed.details` | Query for details of a specific News Feed. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Sessions %}

| Name | Description |
|---|---|---|
| `sessions.data_series` | Query for sessions per day over a time range. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab KPIs %}

| Name | Description |
|---|---|---|
| `kpi.mau.data_series` | Query for total unique active users over a 30-day rolling window over a time range. |
| `kpi.dau.data_series` |  Query for unique active users per day over a time range. |
| `kpi.new_users.data_series` | Query for new users per day over a time range. |
| `kpi.uninstalls.data_series` | Query for app uninstalls per day over a time range. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Templates %}

| Name | Description |
|---|---|---|
| `templates.email.create` | Create a new email template on the dashboard. |
| `templates.email.update` | Update an email template stored on the dashboard. |
| `templates.email.info` | Query for information of a specific template. |
| `templates.email.list` | Query for a list of email templates. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab SSO %}

| Name | Description |
|---|---|---|
| `sso.saml.login` |  Setup identity provider-initiated login. Read our documentation for more info. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Content Blocks %}

| Name | Description |
|---|---|---|
| `content_blocks.info` | Query for information of a specific template. |
| `content_blocks.list` | Query for a list of Content Blocks. |
| `content_blocks.create` | Create a new Content Block on the dashboard. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Subscription %}

| Name | Description |
|---|---|---|
| `subscription.status.set` | Set subscription group status. |
| `subscription.status.get` | Get subscription group status. |
| `subscription.groups.get` | Get status of subscription groups that specific users are explicitly subscribed/unsubscribed to. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Creating and managing REST API keys

![][28]{: style="max-width:20%;float:right;margin-left:15px;"}

To create a new REST API key, visit the **Developer Console** on your Braze dashboard. This page displays your existing API keys. To create a new key, click **Create New API Key**.

You can then to do the following:

- Give your new key a name for identification at a glance
- Select which permissions you would like to be associated with your new key
- Specify allowlisted IP addresses and subnets for the new key

Existing REST API keys can be viewed or deleted by clicking settings <i class="fas fa-gear"></i> and selecting the corresponding option.

![][29]

{% alert important %}
Keep in mind that once you create a new API key, you cannot edit the scope of permissions or the allowlisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. Once you've completed your implementation, go ahead and delete the old key.
{% endalert %}

## REST API key security

API keys are used to authenticate an API call. When you create a new REST API key, you need to give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

Given that REST API keys allow access to potentially sensitive REST API endpoints, secure these keys and only share them with trusted partners. They should never be publicly exposed. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

A good security practice is to assign a user only as much access as is necessary to complete their job: this principle can also be applied to API keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account. 

![API key permissions available when creating an API key.][25]

{% alert warning %}
Given that REST API keys allow access to potentially sensitive REST API endpoints, ensure they are stored and used securely. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.
{% endalert %}

If accidental exposure of a key occurs, it can be deleted from the Developer Console. For help with this process, open a [support ticket][support].

### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets which are allowed to make REST API requests for a given REST API key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the **Whitelist IPs** section when creating a new REST API key: 

![Option to whitelist IPs when creating an API key][26]

If you don’t specify any, requests can be sent from any IP address.

{% alert tip %}
Making a Braze-to-Braze webhook and using allowlisting? Check out our list of [IPs to whitelist]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Additional resources

### Ruby client library

If you're implementing Braze using Ruby, you can use our [Ruby client library](https://github.com/braze-inc/braze-api-client-ruby) to reduce your data import time. A client library is a collection of code specific to one programming language—in this case, Ruby—that makes it easier to use an API.

The Ruby client library supports the [User Endpoints]({{site.baseurl}}/api/endpoints/#user-data).

{% alert note %}
This client library is currently in beta. Want to help us make this library better? Send us feedback at [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[support]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
