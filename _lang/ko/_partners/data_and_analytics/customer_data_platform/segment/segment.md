---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "This reference article outlines the partnership between Braze and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) is a customer data platform that helps you collect, clean, and activate your customer data. 

The Braze and Segment integration allows you to track your users and route data to various user analytics providers. Segment allows you to:

- Sync [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage/) to Braze for use in Braze campaign and Canvas segmentation.
- [Import data across the two platforms](#integration-options). We offer a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for syncing your data to the Braze REST APIs
- [Connect data to Segment through Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/). 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment account | A [Segment account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Installed source and Segment source [libraries](https://segment.com/docs/sources/) | The origin of any data sent into Segment, such as mobile apps, websites, or backend servers.<br><br>You must install the libraries into your app, site, or server before being able to set up a successful `Source > Destination` flow. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate Braze and Segment, you must set [Braze as a destination](#connection-settings) in accordance with [your chosen integration type](#integration-options) (connection mode). If you're a new-to-Braze customer, you can relay historical data to Braze using [Segment replays](#segment-replays). Next, you must set up [mappings](#methods) and [test your integration](#step-4-test-your-integration) to ensure smooth data flow between Braze and Segment.

### Step 1: Create a Braze destination {#connection-settings}

After successfully setting up your sources, you'll need to configure Braze as a [destination](https://segment.com/docs/destinations/) for each source (iOS, Android, web, etc.). You'll have many options to customize the data flow between Braze and Segment using the connection settings.

### Step 2: Choose destination framework and connection type {#integration-options}

In Segment, navigate to **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![The source setup page. This page includes settings to set the destination framework as either "actions" or "classic" and set the connection mode as either "cloud mode" or "device mode".]({% image_buster /assets/img/segment/setup.png %})

You can integrate Segment's web source (Analytics.js) and native client-side libraries with Braze using either a side-by-side (device-mode) integration or a server-to-server (cloud-mode) integration.

Your choice of connection mode will be determined by the type of Source the destination is configured for.

| Integration | Details |
| ----------- | ------- |
| [Side-by-side<br>(device-mode)](#side-by-side-sdk-integration) |Uses Segment's SDK to translate events into Braze native calls, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration.<br><br>Note that Segment does not support all Braze methods (for example, Content Cards). To use a Braze method that isn't mapped through a corresponding mapping, you will have to invoke the method by adding native Braze code to your codebase. |
| [Server-to-server<br>(cloud-mode)](#server-to-server-integration) | Forwards data from Segment to Braze REST API endpoints.<br><br>Does not support Braze UI features such as in-app messaging, Content Cards, or push notifications. There also exists automatically captured data, such as device-level fields, that are unavailable through this method.<br><br>Consider a side-by-side integration if you wish to use these features.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Visit [Segment](https://segment.com/docs/destinations/#connection-modes) to learn more about the two integration options (connection modes), including the benefits of each.
{% endalert %}

#### Side-by-side SDK integration

Also called device-mode, this integration maps Segment's SDK and [methods](#methods) to the Braze SDK, allowing access to all the features our SDK provides, such as push, in-app messaging, and other methods native to Braze. 

{% alert note %}
When using Segment's device-mode, you do not need to integrate the Braze SDK directly. When adding Braze as a device-mode destination for Segment, the Segment SDK will initialize the Braze SDK and call the relevant mapped Braze methods.
{% endalert %}

When using a device-mode connection, similar to integrating the Braze SDK natively, the Braze SDK will assign a `device_id` and a backend identifier, `braze_id`, to every user. This allows Braze to capture anonymous activity from the device by matching those identifiers instead of `userId`. 

{% tabs local %}
{% tab Android %}

{% alert important %}
The source code for the Android device mode integration is maintained by Braze and is updated regularly to reflect new Braze SDK releases.

<br>
The Braze SDK you use will depend on which Segment SDK you use:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferred | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

To set up Braze as a device-mode destination for your Android source, choose **Actions** as the **Destination framework**, then select **Save**. 

To complete the side-by-side integration, refer to Segment's detailed instructions for adding the Braze destination dependency to your [Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) app.

The source code for the [Android device mode](https://github.com/braze-inc/braze-segment-kotlin) integration is maintained by Braze and is updated regularly to reflect new Braze SDK releases.

{% endtab %}
{% tab iOS %}

{% alert important %}
The source code for the iOS device mode integration is maintained by Braze and is updated regularly to reflect new Braze SDK releases.

<br>
The Braze SDK you use will depend on which Segment SDK you use:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferred | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

To set up Braze as a device-mode destination for your iOS source, choose **Actions** as the **Destination framework**, then select **Save**. 

To complete the side-by-side integration, refer to Segment's detailed instructions for adding the Braze Segment pod to your [iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) app.

The source code for the [iOS device mode](https://github.com/braze-inc/braze-segment-swift) integration is maintained by Braze and is updated regularly to reflect new Braze SDK releases.

{% endtab %}
{% tab Web or JavaScript %}

Segment's Braze Web Mode (Actions) framework is recommended for setting up Braze as a device-mode destination for your web source. 

In Segment, select **Actions** as your destination framework and **Device Mode** as your connection mode.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
The source code for the [React Native Braze plugin](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) is maintained by Segment and is updated regularly to reflect new Braze SDK releases.

When connecting a React Native Segment Source to Braze, you must set up a source and destination per operating system. For example, setting up an iOS destination and an Android destination. 

Within your app codebase, conditionally initialize the Segment SDK by device type, using the respective source write key associated with each app.

When a push token is registered from a device and sent to Braze, it is associated with the app identifier used when initializing the SDK. The device-type conditional initialization helps confirm that any push tokens sent to Braze are associated with the relevant app.

{% alert important %}
If the React Native app initializes Braze with the same Braze app identifier for all devices, then all React Native users will be considered Android or iOS users in Braze, and all push tokens will be associated with that operating system.
{% endalert %}

To set up Braze as a device-mode destination for each source, choose **Actions** as the **Destination framework**, then select **Save**.

{% endtab %}
{% endtabs %}

#### Server-to-server integration

Also called cloud-mode, this integration forwards data from Segment to the Braze REST APIs. Use Segment's [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) framework to set up a cloud-mode destination for any of your sources. 

Unlike the side-by-side integration, the server-to-server integration does not support Braze UI features, such as in-app messaging, Content Cards, or automatic push token registration. There also exists [automatically captured]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) data (such as anonymous users and device-level fields) that are not available through cloud-mode.

If you wish to use this data and these features, consider using the side-by-side (device-mode) SDK integration.

The source code for the [Braze Cloud Mode (Actions) destination](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) is maintained by Segment.

### Step 3: Settings

Define the settings for your destination. Not at all settings will apply to all destination types.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Setting | Description |
| ------- | ----------- |
| App identifier | The app identifier used to reference the specific app. This can be found in the Braze dashboard under **Manage Settings** | 
| Custom API endpoint<br>(SDK endpoint) | Your Braze SDK endpoint that corresponds to your instance (such as `sdk.iad-01.braze.com`) | 
| Endpoint region | Your Braze instance (such as US 01, US 02, EU 01, etc.) | 
| Enable automatic in-app message registration | Disable this if you want to manually register in-app messages. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Web Device-Mode %}

| Setting | Description |
| ------- | ----------- |
| App identifier | The app identifier used to reference the specific app. This can be found in the Braze dashboard under **Manage Settings** | 
| Custom API endpoint<br>(SDK endpoint) | Your Braze SDK endpoint that corresponds to your instance (such as `sdk.iad-01.braze.com`) | 
| Safari website push ID | If you support Safari push, you must specify this option with the website push ID that you provided to Apple when creating your Safari push certificate (starts with `web`, for example, `web.com.example.domain`). |
| Braze Web SDK version | The version of the Braze Web SDK you would like to use |
| Automatically send in-app messages | By default, all in-app messages a user is eligible for are automatically delivered to the user. Disable this if you would like to manually display in-app messages. |
| Do not load font awesome | Braze uses Font Awesome for in-app message icons. By default, Braze will automatically load FontAwesome from the FontAwesome CDN. To disable this behavior (for example, because your site uses a customized version of FontAwesome), set this option to `TRUE`. Note that if you do this, you are responsible for ensuring that FontAwesome is loaded on your site - otherwise, in-app messages may not render correctly. |
| Enable HTML in-app messages | Enabling this option will allow Braze dashboard users to use HTML in-app messages. | 
| Open in-app messages in a new tab | By default, links from in-app message clicks load in the current tab or a new tab as specified in the dashboard on a message-by-message basis. Set this option to `TRUE` to force all links from in-app message clicks open in a new tab or window. |
| In-app message z index | Provide a value for this option to override the Braze default z-indexes. | 
| Require explicit in-app message dismissal | By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. Set this option to true to prevent this behavior and require an explicit button click to dismiss messages. |
| Minimum interval between trigger actions in seconds | Defaults to 30.<br>By default, a trigger action will only fire if at least 30 seconds have elapsed since the last trigger action. Provide a value for this configuration option to override that default with a value of your own. We do not recommend making this value any smaller than 10 to avoid spamming the user with notifications.|
| Service worker location | By default, when registering users for web push notifications, Braze will look for the required service worker file in the root directory of your web server at `/service-worker.js`. If you want to host your service worker at a different path on that server, provide a value for this option that is the absolute path to the file. (for example, `/mycustompath/my-worker.js`). Note that setting a value here limits the scope of push notifications on your site. For instance, in the above example, because the service worker file is located within the `/mycustompath/` directory, `requestPushPermission` may only be called from web pages that start with `http://yoursite.com/mycustompath/`. |
| Disable push token maintenance | By default, users who have already granted web push permission will sync their push token with the Braze backend automatically on new sessions to ensure deliverability. To disable this behavior, set this option to `FALSE`. |
| Manage service worker externally | If you have your own service worker that you register and control the lifecycle of, set this option to `TRUE`, and the Braze SDK will not register or unregister a service worker. If you set this option to `TRUE`, for push to function correctly, you must register the service worker yourself before calling `requestPushPermission` and ensure that it contains the Braze service worker code, either with `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` or by including the content of that file directly. When this option is `TRUE`, the `serviceWorkerLocation` option is irrelevant and is ignored. |
| Content security nonce | If you provide a value for this option, the Braze SDK will add the nonce to any `<script>` and `<style>` elements created by the SDK. This permits the Braze SDK to work with your website's content security policy. In addition to setting this nonce, you may also need to allow FontAwesome to load, which you can do by adding `use.fontawesome.com` to your Content Security Policy allowlist or by using the `doNotLoadFontAwesome` option and loading it manually. |
| Allow crawler activity | By default, the Braze Web SDK ignores activity from known spiders or web crawlers, such as Google, based on the user agent string. This saves data points, makes analytics more accurate, and may improve page rank. However, if you want Braze to log activity from these crawlers instead, you may set this option to `TRUE`. |
| Enable logging | Set to `TRUE` to enable logging by default. Note that this will cause Braze to log to the JavaScript console, which is visible to all users. Before you release your page to production, you should remove this or provide an alternate logger with `setLogger`. |
| Allow user-supplied JavaScript | By default, the Braze Web SDK does not allow user-supplied JavaScript click actions, as it allows Braze dashboard users to run JavaScript on your site. To indicate that you trust the Braze dashboard users to write non-malicious JavaScript click actions, set this property to `TRUE`. If `enableHtmlInAppMessages` is `TRUE`, this option will also be set to `TRUE`. |
| App version| If you provide a value for this option, user events sent to Braze will be associated with the given version, which can be used for user segmentation. |
| Session timeout in seconds | Defaults to 30.<br>By default, sessions time out after 30 minutes of inactivity. Provide a value for this configuration option to override that default with a value of your own. | 
| Device property allowlist | By default, the Braze SDK automatically detects and collects all device properties in `DeviceProperties`. To override this behavior, provide an array of `DeviceProperties`. Note that without some properties, not all features will function properly. For instance, local time zone delivery will not function without the time zone. |
| Localization | By default, any SDK-generated user-visible messages will be displayed in the user's browser language. Provide a value for this option to override that behavior and force a specific language. The value for this option should be an ISO 639-1 language code. |
| No cookies | By default, the Braze SDK will store small amounts of data (user ids, session ids) in cookies. This is done to allow Braze to recognize users and sessions across different subdomains of your site. If this presents a problem for you, pass `TRUE` for this option to disable cookie storage and rely entirely on HTML 5 localStorage to identify users and sessions. |
| Track all pages | **Classic Destination Web Device-Mode (maintenance) Only**<br><br>Segment recommends migrating to the Web Actions framework destination where this setting can be [enabled through mappings](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>This will send all [page calls](https://segment.com/docs/spec/page/) to Braze as a "Loaded/Viewed a Page" event. |
| Track only named pages | **Classic Destination Web Device-Mode (maintenance) Only**<br><br>Segment recommends migrating to the Web Actions framework destination where this setting can be [enabled through mappings](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>This will send only page calls to Braze with a name associated with them. |
| Log purchase when revenue is present | **Classic Destination Web Device-Mode (maintenance) Only**<br><br>Segment recommends migrating to the Web Actions framework destination where this setting can be [enabled through mappings](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>When this option is enabled, all Track calls with the revenue property will trigger a purchase event. | 
| Only track known users | **Classic Destination Web Device-Mode (maintenance) Only**<br><br>Segment recommends migrating to the Web Actions Framework destination where this setting can be enabled through mappings.<br><br>If enabled, this new setting delays calling of `window.appboy.initialize` until there is a valid `userId`. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Cloud-Mode %}

| Setting | Description |
| ------- | ----------- |
| App identifier | The app identifier used to reference the specific app. This can be found in the Braze dashboard under **Manage Settings** | 
| REST API key | This can be found in your Braze dashboard under **Settings** > **API Keys**. | 
| Custom REST API endpoint | Your Braze REST endpoint that corresponds to your instance (such as rest.iad-01.braze.com). | 
| Update existing users only | **Classic Destination Cloud-Mode (Maintenance) Only**<br><br>Segment recommends migrating to the Cloud Actions Framework destination where this setting can be [enabled through mappings](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determines whether to update existing users only. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Step 4: Map methods {#methods}

Braze supports the [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/), and [Track](https://segment.com/docs/spec/track/) Segment methods. The types of identifiers used within these methods will depend on whether the data is being sent through a server-to-server (cloud-mode) or side-by-side (device-mode) integration. In the Braze Web Mode Actions and Cloud Mode Actions destinations, you can also choose to set up a mapping for a [Segment alias call](https://segment.com/docs/connections/spec/alias/). 

{% alert note %}
Although user aliases are supported as an identifier in the Braze Cloud Mode (Actions) destination, it should be noted that Segment's alias call is not directly related to Braze user aliases.
{% endalert %}

| Identifier type | Supported destination |
| --------------- | --------------------- |
| `userId` (`external_id`) | All |
| Anonymous user | Device mode destinations |
| User alias | Cloud mode destinations |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The Cloud Mode (Actions) Destination offers a [Create Alias action](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) that can be used to create an alias-only user or add an alias to an existing `external_id` profile. The [Identify User action](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) can be used alongside the Create Alias action to merge an alias-only user with an `external_id` after one becomes available for the user. 

It is also possible to engineer a workaround and use `braze_id` to send anonymous user data in cloud-mode. This requires manually including the user's `braze_id` in all your Segment API calls. You can learn more about how to set up this workaround in [Segment's documentation](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Destinations data sent to Braze can be batched within Cloud Mode Actions. Batch sizes are capped at 75 events, and these batches will accumulate over a 30-second period before being flushed. Request batching is done per-action. For example, Identify Calls (attributes) will be batched in a request and Track Calls (custom events) will be batched in a second request. Braze recommends enabling this feature as it will reduce the number of requests being sent from Segment to Braze. In turn, this will reduce the risk of the destination hitting Braze rate limits and retrying requests. 

You can turn on batching for an action by navigating to your Braze Destination > **Mappings**. From there, click the 3-dot icon to the right of the mapping and select **Edit Mapping**. Scroll to the bottom of the **Select mappings** section and make sure that **Batch Data to Braze** is set to **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

The [Identify](https://segment.com/docs/spec/identify/) call lets you tie a user to their actions and record attributes about them. 

Certain Segment special traits map to standard attribute profile fields in Braze:

| Special Segment traits | Braze standard attributes |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Other reserved Braze profile fields such as `email_subscribe` and `push_subscribe` can be sent by using the Braze naming convention for these fields and passing them as traits within an identify call.

##### Adding a user to a subscription group

You can also subscribe or unsubscribe a user from a given subscription group using the following fields in the traits parameter.

Use the reserved Braze profile field called `braze_subscription_groups`, which can be associated with an array of objects. Each object in the array should have two reserved keys:

1. `subscription_group_state`: Indicates whether the user is `"subscribed"` or `"unsubscribed"` to a specific subscription group.
2. `subscription_group_id`: Represents the unique ID of the subscription group. You can find this ID in the Braze dashboard under **Subscription Group Management**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Custom attributes

All other traits will be recorded as [custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

| Segment method | Braze method | Example |
|---|---|---|
| Identify with user ID | Set external ID | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify with reserved traits | Set user attributes | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify with custom traits | Set custom attributes | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify with user ID and traits | Segment: Set External ID and Attribute | Combine preceding methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In the [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) and [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) destinations, the above mappings can be set using the Update User Profile Action.

{% alert important %}
When passing user attribute data, check that you only pass values for attributes that have changed since the last update. This will ensure you do not unnecessarily consume data points toward your allotment. For client-side sources, use Segment's open-source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) tool to optimize your integration and limit data point usage by debouncing duplicate `identify()` calls from Segment. 

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

When you track an event, we will record that event as a [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) using the name provided. 

Metadata sent within the properties object of the track call will be logged in Braze as the custom event properties for the associated event. All [custom event property data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) are supported.

In the [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) and [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) destinations, the above mappings can be set using the Track Event Action.

| Segment method | Braze method | Example |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Logged as a [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [Track with properties](https://segment.com/docs/spec/track/) | Logged as [Event Property]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track with product](https://segment.com/docs/spec/track/) | Logged as a [Purchase Event]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### Order completed {#order-completed}

When you track an event with the name `Order Completed` using the format described in Segment's [eCommerce API](https://segment.com/docs/spec/ecommerce/v2/), we will record the products you've listed as [purchases]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

In the [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) and [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) destinations, the default mapping can be customized through the Track Purchase Action.

{% endtab %}

{% tab Page %}
#### Page {#page}

The [Page](https://segment.com/docs/spec/page/) call lets you record whenever a user sees a page of your website, along with any optional properties about the page.

This event type can be used as a trigger in the Web Mode Actions and Cloud Actions destinations to log a custom event to Braze.
{% endtab %}

{% endtabs %}

### Step 5: Test your integration

When using the side-by-side (device-mode) integration, your [overview]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/) metrics (lifetime sessions, MAU, DAU, stickiness, daily sessions, and daily sessions per MAU) can be used to ensure that Braze is receiving data from Segment.

You can view your data in the [custom events]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data) or [revenue]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) pages, or by [creating a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment). The dashboard's **Custom Events** page lets you view custom event counts over time. Note that you will not be able to use [formulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula) that include MAU and DAU statistics when using a server-to-server (cloud mode) integration.

If you're sending purchase data to Braze (see order completed in the **Track** tab of [Step 3](#methods)), the [revenue]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) page allows you to view data on revenue or purchases over specific periods or your app's total revenue.

[Creating a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) allows you to filter your users based on the custom event and attribute data.

{% alert important %}
If you use a server-to-server integration (cloud-mode), filters related to automatically collected session data (such as "first used app" and "last used app") will not work. Use a side-by-side integration (device-mode) if you want to use these in your Segment and Braze integration.
{% endalert %}

## User deletion and suppression 

If you need to delete or suppress users, note that [Segment's user delete feature](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **is** mapped to the Braze [`/users/delete` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). Note that verification of these deletions could take up to 30 days.

You must ensure that you select a common user identifier between Braze and Segment (as in `external_id`). After you've initiated a deletion request with Segment, you can view the status within the deletion requests tab in your Segment dashboard.

## Segment replays

Segment provides a service to clients to "replay" all historical data to a new technology partner. New Braze customers who want to import all relevant historical data can do so through Segment. Talk to your Segment rep if this is something you are interested in.

Segment will connect to our [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to import user data into Braze on your behalf.

{% alert important %}
All identifiers supported in the Cloud Mode Actions destination are supported as part of Segment Replays.
{% endalert %}

## Best practices

{% details Review use cases to avoid data overages. %}

Segment **does not** limit the number of data elements clients send to them. Segment allows you to send all or decide which events you will send to Braze. Rather than sending all of your events using Segment, we suggest you review use cases with your marketing and editorial teams to determine which events you will send to Braze to avoid data overages.

{% enddetails %}

{% details Understand the difference between the custom API endpoint and the custom REST API endpoint in the Mobile Device Mode destination settings. %}

| Braze terminology | Segment equivalent |
| ----------------- | ------------------ |
| Braze SDK endpoint | Custom API endpoint |
| Braze REST endpoint | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Your Braze API endpoint (called the "Custom API Endpoint" in Segment) is the SDK endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Your Braze REST API endpoint (called the "Custom REST API Endpoint" in Segment) is the REST API endpoint (for example, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Ensure your custom API endpoint is correctly input into the mobile device mode destination settings. %}

| Braze terminology | Segment equivalent |
| ----------------- | ------------------ |
| Braze SDK endpoint | Custom API endpoint |
| Braze REST endpoint | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The proper format must be followed to ensure that you input your Braze SDK endpoint correctly. Your Braze SDK endpoint must not include `https://` (for example, `sdk.iad-03.braze.com`), or else the Braze integration will break. This is required because Segment automatically prepends your endpoint with `https://`, resulting in Braze initializing with an invalid endpoint `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Data mapping nuances. %}

Scenarios where data will not pass as expected:

1. Nested custom attributes
  - Although [nested custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) can technically be sent to Braze through Segment, the **entire payload** will be sent each time. This will incur [data points]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) per key passed in the nested object each time the payload is sent.<br><br> To spend only a subset of data points when the payload sends, you can use the custom [destination functions](https://segment.com/docs/connections/functions/destination-functions/) feature owned by Segment. This feature in the Segment platform allows you to customize how data is sent to downstream destinations.

  {% alert note %}
  Custom destination functions are controlled within Segment, and Braze has limited insight into functions that have been configured externally.
  {% endalert %}

{: start="2"}
2\. Passing anonymous data server-to-server.
  - Customers may use Segment's server-to-server libraries to funnel anonymous data to other systems. See the map methods section to learn more about sending users without an `external_id` to Braze via a server-to-server (cloud-mode) integration.

{% enddetails %}

{% details Customization of Braze initialization. %}

There are several different ways that Braze can be customized: push, in-app messages, Content Cards, and initialization. With a side-by-side integration, you can still customize push, in-app messages, and Content Cards as you would with a direct Braze integration.

However, customizing when the Braze SDK is integrated or specifying initialization configurations may be difficult and sometimes not possible. This is because Segment will initialize the Braze SDK for you when the Segment initialization occurs.

{% enddetails %}

{% details Sending deltas to Braze. %}

When passing user attribute data, check that you only pass values for attributes that have changed since the last update. This will ensure you do not unnecessarily consume data points toward your allotment. For client-side sources, use Segment's open-source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) tool to optimize your integration and limit Data Point usage by debouncing duplicate `identify()` calls from Segment. 

{% enddetails %}


