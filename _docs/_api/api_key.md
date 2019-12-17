---
nav_title: "API Key Overview"
page_order: 5

description: "This reference article covers the concept of API keys, what they are used for, and how they are used, as well as as a look at various types of IDs and their purposes." 
page_type: reference
tool: 
  - dashboard
  - docs
platform: 
  - API
---

#API Key Overview

>  This reference article covers what API keys are, what they are used for, their permissions and how to keep these keys secure. It also touches on what campaign IDs, canvas IDs, and template IDs are, how they are used, and how you can use them too within the Braze Dashboard. 

## What is an API Key?

An application programming interface key (API key) is a unique code that is passed into an API to authenticate the API call and identify the calling application or user. API access is done using HTTPS web requests to your company's rest API endpoint. We use API keys at Braze in tandem with our SDK to make sure everything is running smoothly on both your and our end. 

The `api_key` included in each request acts as an authentication key that allows your server code to utilize our REST APIs. REST APIs are used to track users, send messages, export user data, and more.  When you create a new REST API Key, you will need to give it access to specific endpoints. [endpoints listed here] By assigning specific permissions to an API Key, you can limit exactly which calls an API Key can authenticate.

## What is an App Group Key?

Often used at Braze is the functionality of App Groups, App groups are designed to house versions of the same application across multiple platforms. Many clients also use app groups to contain free and premium versions of their applications on the same platform. As you may notice, these App groups are also making use of the REST API. 

Within your company, each app group will have a unique set of REST API Keys. These keys are similar to our standard API keys, except they are linked to an app group that you or your company has made. 

These app group keys can be found within the Braze dashboard by navigating to the Developer Console section for each app group. To use the REST API for any given App Group, you must create keys and give them permissions.

### API Key Permissions

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

### API Key Security

Security is of the utmost importance at Braze. Given that REST API Keys allow access to potentially sensitive REST API endpoints, please ensure they are stored and used securely. 

(?) We strongly encourage you to keep your API keys within your company.

A good security practice is to assign a user only as much access as is necessary to complete his or her job: this principle can also be applied to API Keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account.

(?)For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

### Multiple API keys:

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

## API key vs. APP Identifier

###The App Identifier (previously called the API key):

The app_id is an identifier that designates which app within the app group you are interacting with
The key value can be found in the developer console or manage appgroup (iosClient, subkey, app)

App_id is a parameter associating activity with a specific app in your app group. Ie you will have an app_id for your iOS app, an app_id for your android app and an app_id for your web integration.

If you want to send push to a set of device tokens (instead of users), you need to indicate on behalf of which specific app you are messaging. In that case, you will provide the appropriate App Identifier in a Tokens Object. It can be found in the Developer Console section of the Braze dashboard under the `API settings` tab.

(?) This field is necessary for SDK integrations to work.

###The API Key:

The API key is an identifier that designates which app group you are interacting with
The key value can be found on the developer console. (client production, master, appgroup)

______________________

### App Identifier vs REST API key
The ‘App Identifier’ is the App API Key found in the `Manage App Group` or `Developer Console` page on the Braze Dashboard. This field is necessary for SDK integrations to work. 
The ‘REST API Key’ is the dashboard Rest API Key for making API calls. Make sure the key has permission to access `users/track` endpoint.


Within API
App Identifier is a legacy field specific to a specific platform like iOS or Android.
If you are not on one of these channels/platofrm, you can put in anything and it will work. 

App Group: Manage App Group > App Settings
    The `api_key` indicates the app title with which the data in this request is associated and authenticates the requester as someone who is allowed to send messages to the app. It must be included with every request. It can be found in the Developer Console section of the Braze dashboard.
____________________________________________________________
 (?) How to get the API Key in technology partners?
    In your Braze account, navigate to "Technology Partners" , then "Attribution" and find the API key and REST Endpoint in the AppsFlyer section. The API key and the REST Endpoint are used in the next step when setting up a postback in Appsflyer's dashboard.

On that page, search for Braze and click on Braze's logo to open up a configuration window.
Under "Integration Parameters" select "enable".
Copy the Braze API key (obtained in the prior step) into the "API_key" field.
Copy the Braze Rest Endpoint URL (obtained in the prior step) into the "REST_endpoint" field.
Click "Save & Close".

# Template IDs, Canvas IDs and Campaign IDs

The following identifiers can be used to acess your teample, canvas or campaign from Braze's external API

##Template IDs

A Template ID, or Template API Identifier is a key generated by Braze for a given template within the Dashboard. Template IDs are unique for each template and can be used to reference templates throughout the platform. 

Templates are great for if your company contracts out your HTML designs for campaigns. Once the templates have been built, you now have a template that is not specific to a campaign, but can be applied to a series of campaigns like a newsletter.

### Where can I find it?
You can find your Template ID by going to the Dashboard, opening up "Templates & Media" under "Engagement" and selecting a pre-existing template. If the template you want does not exist yet, create one and save it. At the bottom of the individual template page, you will be able to find your Template API Identifier.

[Picture]

### What can it be used for?

At Braze, we have a seperate endpoint for [templates][7]. 
Using the Template ID, we can over API...
- Update templates over API
- Grab information on a specific template

## Canvas IDs

A Canvas ID, or Canvas API Identifier is a key generated by Braze for a given campaign within the Dashboard. Canvas IDs are unique to each canvas

### Where can I find it?
You can find your Canvas ID by going to the Dashboard, opening up "Canvas" under "Engagement" and selecting a pre-existing Canvas. If the Canvas you want does not exist yet, create one and save it. At the bottom of the individual Canvas page, you will find a "Analyze Variants" button, upon clicking it, a window will apear with the Canvas API Identifier located at the bottom. 

Note that if you have a Canvas that has variants, there exists an overall Canvas ID as well as individual varient Canvas IDs nested under the main campaign. 

[Picture]

### What can it be used for?
- Track analytics on a specific message
- Grab high level agregate stats on Canvas performance
- Grab details on a specific Canvas
- In currents
- With API trigger delivery in order to collect statistics for transactional messages

## Campaign IDs

A Campaign ID, or Campaign API Identifier is a key generated by Braze for a given campaign within the Dashboard. Campaign IDs are unique to each campaign. 

### Where can I find it?
You can find your Campaign ID by going to the Dashboard, opening up "Campaigns" under "Engagement" and selecting a pre-existing Campaign. If the Canvas you want does not exist yet, create one and save it. At the bottom of the individual campaign page, you will be able to find your Campaign API Identifier.

Note that if you have a Campaign that has variants, there exists an overall Campaign ID as well as individual varient Campaign IDs nested under the main campaign. 

[Picture]

### What can it be used for?
- Track analytics on a specific message
- Grab high level agregate stats on Campaign performance
- Grab details on a specific Campaign
- With API trigger delivery in order to collect statistics for transactional messages

## Segment IDs

A Campaign ID, or Campaign API Identifier is a key generated by Braze for a given campaign within the Dashboard. Campaign IDs are unique to each campaign. 

### Where can I find it?
You can find your Campaign ID by going to the Dashboard, opening up "Campaigns" under "Engagement" and selecting a pre-existing Campaign. If the Canvas you want does not exist yet, create one and save it. At the bottom of the individual campaign page, you will be able to find your Campaign API Identifier.

Note that if you have a Campaign that has variants, there exists an overall Campaign ID as well as individual varient Campaign IDs nested under the main campaign. 

[Picture]

### What can it be used for?
- Track analytics on a specific message
- Grab high level agregate stats on Campaign performance
- Grab details on a specific Campaign
- With API trigger delivery in order to collect statistics for transactional messages

[3]: https://developer.android.com/studio/build/build-variants.html
[4]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[5]: http://localhost:4000/docs/api/endpoints/email_sync/#api-specification
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[7]: https://www.braze.com/docs/api/endpoints/email_templates/