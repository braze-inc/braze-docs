---
nav_title: "API Key Overview"
page_order: 2.1

description: "This reference article covers the concept of API keys, what they are used for, and how they are used." 
page_type: reference
tool: 
  - dashboard
  - docs
platform: 
  - API
---

# API Key Overview

>  This reference article covers the two main types of keys you will see at Braze, the REST API Key or APP Group Key, referred to as the `api_key`, and the App Identifier Key, known as the `app_id`, as well as what these keys are are, how they are used at Braze, their permissions and how to keep them secure. 

In addition to these keys, there also exists Identifier Keys that can be used to reference specific things like templates, canvases, campaigns, content cards, and segments from the API. Information on those API identifier types/keys can be found [here][2].

## What is a REST API Key/App Group REST API Key?

A REST Application Programming Interface key (API key) is a unique code that is passed into an API to authenticate the API call and identify the calling application or user. API access is done using HTTPS web requests to your company's rest API endpoint. We use API keys at Braze in tandem with our SDK to make sure everything is running smoothly on both your and our end. 

The `api_key` included in each request acts as an authentication key that allows your server code to utilize our REST APIs. REST APIs are used to track users, send messages, export user data, and more.  When you create a new REST API Key, you will need to give it access to specific endpoints. [endpoints listed here] By assigning specific permissions to an API Key, you can limit exactly which calls an API Key can authenticate.




App Groups are used all the time at Braze, they are designed to house versions of the same application across multiple platforms. Many clients also use app groups to contain free and premium versions of their applications on the same platform. As you may notice, these App groups are also making use of the REST API. 

Within your company, each app group will have a unique set of REST API Keys. These keys are similar to our standard API keys, except they are linked to an app group that you or your company has made. 

These app group keys can be found within the Braze dashboard by navigating to the Developer Console section for each app group. To use the REST API for any given App Group, you must create keys and give them permissions.

### Where can I find it?

Your API keys can always be found in the Braze Dashboard in the "Developer Console" under "App Settings". This new page will list all of your available REST API Keys as well as give you options to create new API keys. 

## API Key Permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls.

{% tabs %}
{% tab User Data %}

| Permission | Description  |
|---|---|---|
| `users.track` | Record user attributes, custom events, and purchases  |
| `users.delete` | Delete any user. |
| `users.alias.new` | Create a new alias for an existing user.  |
| `users.identify` | Query for user profile information by user ID.  |
| `users.export.ids` | The language the browser is set to use.  |
| `users.export.segment` | Query for user profile information by Segment. |

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

{% endtab %}
{% tab Messages %}

| Name | Description |
|---|---|---|
| `messages.send` | Send an immediate, ad-hoc message to specific users. |
| `messages.schedule.create` | Schedule a message to be sent at a specific time. |
| `messages.schedule.update` | Update a scheduled message. |
| `messages.schedule.delete` | Delete a scheduled message. |
| `messages.schedule_broadcasts` | Query all scheduled broadcast messages. |

{% endtab %}
{% tab Campaigns %}

| Name | Description |
|---|---|---|
| `campaigns.trigger.send` | Trigger the sending of an existing Campaign. |
| `campaigns.trigger.schedule.create` | Schedule a future send of a Campaign with API-triggered delivery. |
| `campaigns.trigger.schedule.update` | Update a Campaign scheduled with API-triggered delivery. |
| `campaigns.trigger.schedule.delete` | Delete a Campaign scheduled with API-triggered delivery |
| `campaigns.list` | Query for a list of Campaigns. |
| `campaigns.data_series` | Query for Campaign analytics over a time range. |
| `campaigns.details` | Query for details of a specific Campaign. |
| `sends.data_series` | Query for message send analytics over a time range. |
| `sends.id.create` | Create Send ID for message blast tracking. |

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

{% endtab %}
{% tab Segments %}

| Name | Description |
|---|---|---|
| `segments.list` | Query for a list of Segments. |
| `segments.data_series` | Query for Segment analytics over a time range. |
| `segments.details` | Query for details of a specific Segment. |

{% endtab %}
{% tab Purchases %}

| Name | Description |
|---|---|---|
| `purchases.product_list` | Query for a list of products purchased in your app. |
| `purchases.revenue_series` | Query for total money spent per day in your app over a time range. |
| `purchases.quantity_series` | Query for the total number of purchases per day in your app over a time range. |

{% endtab %}
{% tab Events %}

| Name | Description |
|---|---|---|
| `events.list` | Query for a list of Custom Events. |
| `events.data_series` | Query occurrences of a Custom Event over a time range. |

{% endtab %}
{% tab News Feed %}

| Name | Description |
|---|---|---|
| `feed.list` | Query for a list of News Feed cards. |
| `feed.data_series` | Query for News Feed analytics over a time range. |
| `feed.details` | Query for details of a specific News Feed. |

{% endtab %}
{% tab Sessions %}

| Name | Description |
|---|---|---|
| `sessions.data_series` | Query for sessions per day over a time range. |

{% endtab %}
{% tab KPIs %}

| Name | Description |
|---|---|---|
| `kpi.mau.data_series` | Query for total unique active users over a 30-day rolling window over a time range. |
| `kpi.dau.data_series` |  Query for unique active users per day over a time range. |
| `kpi.new_users.data_series` | Query for new users per day over a time range. |
| `kpi.uninstalls.data_series` | Query for app uninstalls per day over a time range. |

{% endtab %}
{% tab Templates %}

| Name | Description |
|---|---|---|
| `templates.email.create` | Create a new email template on the Dashboard. |
| `templates.email.update` | Update an email template stored on the Dashboard. |
| `templates.email.info` | Query for information of a specific template. |
| `templates.email.list` | Query for a list of email templates. |

{% endtab %}
{% tab SSO %}

| Name | Description |
|---|---|---|
| `sso.saml.login` |  Setup identity provider-initiated login. Read our documentation for more info. |

{% endtab %}
{% tab Content Blocks %}

| Name | Description |
|---|---|---|
| `canvas.trigger.send` | Trigger the sending of an existing Canvas. |
| `canvas.trigger.schedule.create` | Schedule a future send of a Canvas with API-triggered delivery. |
| `canvas.trigger.schedule.update` | Update a Canvas scheduled with API-triggered delivery. |
| `canvas.trigger.schedule.delete` | Delete a Canvas scheduled with API-triggered delivery. |
| `canvas.list` | Query for a list of Canvases. |
| `canvas.data_series` | Query for Canvas analytics over a time range. |
| `canvas.details` | Query for details of a specific Canvas. |
| `canvs.data_summary` | Query for rollups of Canvas analytics over a time range. |

{% endtab %}
{% tab Subscription %}

| Name | Description |
|---|---|---|
| `subscription.status.set` | Set subscription group status. |
| `subscription.status.get` | Get subscription group status. |
| `subscription.groups.get` | Get status of subscription groups that specific users are explicitly subscribed/unsubscribed to. |

{% endtab %}
{% endtabs %}

Please check [Braze documentation][5] site or our [Braze Postman documentation][6] for a full description of these API endpoints.

{% alert note %}
Keep in mind that once you create a new API Key, you cannot edit the scope of permissions or the whitelisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. Once you’ve completed your implementation, go ahead and delete the old key.
{% endalert %}

## API Key Security

Security is of the utmost importance at Braze. Given that REST API Keys allow access to potentially sensitive REST API endpoints, please ensure they are stored and used securely. 

A good security practice is to assign a user only as much access as is necessary to complete his or her job: this principle can also be applied to API Keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account.

For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

## API key vs. APP Identifier

### The App Identifier:

The `app_id` or App Identifier is a parameter associating activity with a specific app in your app group. It designates which app within the app group you are interacting with. You will find that you will have an app_id for your iOS app, an app_id for your android app, and an app_id for your web integration. 

(?) If you want to send push to a set of device tokens (instead of users), you need to indicate on behalf of which specific app you are messaging. In that case, you will provide the appropriate App Identifier in a Tokens Object. It can be found in the Developer Console section of the Braze dashboard. This field is necessary for SDK integrations to work.
- How to do this? - 

If you are prompted for an `app_id` but you are not working with an app, because it is a legacy field specific to a specific platform, you are able to omit completely or randomly include a string of characters in that field. 

### Where can I find it?
There are two ways to locate your `app_id`:

1. You can find this `app_id` or application identifier by opening up the Braze Dashboard, and open "Developer Console" under "App Settings". On this new page, you can see your API key identifiers, and below them, you will be able to see every `app_id` for all your apps.

2. From the Braze Dashboard, open up "Manage App Group" under "App Settings". From this new page, in the "App Settings" tab, midway through the page you will find an "API key for __APP NAME__ on __PLATFORM__" (e.g "API Key for Ice Cream on iOS) This API key is your Application Identifier.


## Multiple API keys

During SDK set up, The most common use case for multiple API keys is separating API keys for debug and release build variants.
To easily switch between multiple API keys in your builds, we recommend creating a separate `appboy.xml` file for each relevant [build variant][3]. A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types][8] and no product flavors.
For each relevant build variant, create a new `appboy.xml` for it in `src/<build variant name>/res/values/`:
When the build variant is compiled, it will use the new API key.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```
When the build variant is compiled, it will use the new API key.

### App Identifier vs. REST API key

The ‘App Identifier’ is the App API Key found in the `Manage App Group` or `Developer Console` page on the Braze Dashboard. This field is necessary for SDK integrations to work. 
The ‘REST API Key’ is the dashboard Rest API Key for making API calls. Make sure the key has permission to access `users/track` endpoint.

[2]: https://www.braze.com/docs/api/identifier_types/
[3]: https://developer.android.com/studio/build/build-variants.html
[4]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[5]: http://localhost:4000/docs/api/endpoints/email_sync/#api-specification
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro

BAD_PLACE
### The API Key

The `api_key` indicates the app title with which the data in this request is associated and authenticates the requester as someone who is allowed to send messages to the app. It must be included with every request. It can be found in the Developer Console section of the Braze dashboard.