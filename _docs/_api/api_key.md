---
nav_title: "API Key Overview"
article_title: REST API Key Overview
page_order: 2.1
description: "This reference article covers the concept of API keys, what they are used for, and how they are used." 
page_type: reference

---

# REST API Key Overview

>  This reference article covers two of the three main types of keys you will see at Braze, the REST API Key or App Group API Key, referred to as the `api_key`, and the App Identifier Key, known as the `app_id`, as well as what these keys are, how they are used at Braze, their permissions and how to keep them secure. 

In addition to these keys, there also exists a third type of key called Identifier Keys that can be used to reference specific things like templates, Canvases, campaigns, Content Cards, and segments from the API. Information on those API Identifier types/keys can be found [here][2].

## What is a REST API Key/App Group API Key?

A REST Application Programming Interface key (REST API key) is a unique code that is passed into an API to authenticate the API call and identify the calling application or user. API access is done using HTTPS web requests to your company's REST API endpoint. We use REST API keys at Braze in tandem with our App Identifier keys to track, access, send, export, and analyze data to help make sure everything is running smoothly on both your and our end. 

App Groups and API Keys go hand in hand at Braze. App Groups are designed to house versions of the same application across multiple platforms. Many clients also use app groups to contain free and premium versions of their applications on the same platform. As you may notice, these app groups are also making use of the REST API and have their own REST API keys. These keys can be individually scoped to include access to specific endpoints on the API. Each call to the API must include a key with access to the endpoint hit.

We refer to both the REST API Key and App Group API Key as the `api_key`. The `api_key` is included in each request as a request header and acts as an authentication key that allows you to utilize our REST APIs. These REST APIs are used to track users, send messages, export user data, and more.  When you create a new REST API Key, you will need to give it access to specific endpoints. By assigning specific permissions to an API Key, you can limit exactly which calls an API Key can authenticate.

### Where can I find it?

Your API keys can always be found in the Braze dashboard in the **Developer Console** under **Settings**. At the top of this new page, you will find the **REST API Keys** section. Here you can view all of your available REST API/App Group API Keys, and create new API keys.

### How can I use it?

Prior to April 2020, API keys would be included as a part of the API request body or within the request URL as a parameter. Braze now has updated the way in which we read API keys. API keys are now set with the HTTP Authorization request header, making your API keys more secure.

While the old way of passing API keys continues to work, after a period of time this will be permenatly removed so we urge users to update API calls accordingly. 

{% alert important %}
__Looking for the `api_key` parameter in your Braze endpoints?__<br>
As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see YOUR-REST-API-KEY within each endpoint Example Requests.
<br><br>
Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

### REST API Key Permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls.

{% tabs %}
{% tab User Data %}

| Permission | Description  |
|---|---|---|
| `users.track` | Record user attributes, custom events, and purchases  |
| `users.delete` | Delete any user. |
| `users.alias.new` | Create a new alias for an existing user.  |
| `users.identify` | Query for user profile information by user ID.  |
| `users.export.ids` | Query for user profile information by identifier e.g. device_id, email_address, external_id.  |
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
| `templates.email.create` | Create a new email template on the Dashboard. |
| `templates.email.update` | Update an email template stored on the Dashboard. |
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
| `content_blocks.create` | Create a new Content Block on the Dashboard. |
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

Please check [Braze documentation][5] site or our [Braze Postman documentation][6] for a full description of these API endpoints.

{% alert important %}
Once you create a new API Key, you cannot edit the scope of permissions or the whitelisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. Once you’ve completed your implementation, go ahead and delete the old key.
{% endalert %}

## The App Identifier API Key

The App Identifier API Key or `app_id` is a parameter associating activity with a specific app in your app group. It designates which app within the app group you are interacting with. For example, you will find that you will have an `app_id` for your iOS app, an `app_id` for your android app, and an `app_id` for your web integration. At Braze, you might find that you have multiple apps for the same platform across the various platform types that Braze supports.

App identifiers at Braze are used when integrating the SDK and are also used to reference a specific app in REST API calls. With the `app_id` you can do many things like pull data for a custom event that occurred for a particular app, retrieve uninstall stats, new user stats, DAU stats, and session start stats for a particular app.

Sometimes, you may find you are prompted for an `app_id` but you are not working with an app, because it is a legacy field specific to a specific platform, you can “omit” this field by including any string of characters as a placeholder for this required parameter.

### Where can I find it?
There are two ways to locate your `app_id`:

1. You can find this `app_id` or application identifier in the **Developer Console** under **Settings**. On this new page, under **Identification**, you will be able to see every `app_id` that exists for your apps.

2. Go to **Manage Settings** under **Settings**. From this new page, in the **Settings** tab, midway through the page you will find an "API key for __APP NAME__ on __PLATFORM__" (e.g "API Key for Ice Cream on iOS). This API key is your Application Identifier.

### Multiple App Identifier API keys

During SDK set up, the most common use case for multiple App Identifier API keys is separating those keys for debug and release build variants.
To easily switch between multiple App Identifier API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant][3]. A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types][8] and no product flavors.
For each relevant build variant, create a new `braze.xml` for it in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```
When the build variant is compiled, it will use the new API key.

## REST API Key Security

Security is of the utmost importance at Braze. Given that REST API Keys allow access to potentially sensitive REST API endpoints, please secure these keys and only share them with trusted partners. They should never be publicly exposed. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

A good security practice is to assign a user only as much access as is necessary to complete their job: this principle can also be applied to API Keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account. 

With App identifiers, the `app_id` is assigned by Braze and permissions cannot be assigned or revoked. Because of the nature of the relationship between `app_id` and the SDK, keeping this identifier secure is __crucial__ in the security of your application.


[2]: {{site.baseurl}}/api/identifier_types/
[3]: https://developer.android.com/studio/build/build-variants.html
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
