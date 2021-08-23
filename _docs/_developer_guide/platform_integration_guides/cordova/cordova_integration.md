---
nav_title: Cordova Integration
article_title: Cordova Integration
platform: Cordova
page_order: 1
page_type: reference
description: "This article covers initial SDK setup steps for Android and FireOS apps running on Cordova."

---

# Cordova Integration

## Setting a Custom API Endpoint

A custom API endpoint can be configured via the `config.xml`. For example, to use the EU endpoint, see the following:

{% tabs %}
{% tab Android %}

```
<platform name="android">
    ...
    <preference name="com.appboy.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% tab iOS %}

```
<platform name="ios">
    ...
    <preference name="com.appboy.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Push Notifications

If you use the Cordova SDK default setup you won't have to make any new changes client-side. For modified integrations, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/) or [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) integration instructions.

## In-App Messaging
{% tabs %}
{% tab Android %}
By default the Cordova SDK supports in-app messages with no changes. See [the Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) or the [sample Android application](https://github.com/Appboy/appboy-android-sdk ) for implementation samples.
{% endtab %}
{% tab iOS %}
By default the Cordova SDK supports in-app messages with no changes. See [the iOS integration instructions]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) or the [sample iOS application](https://github.com/Appboy/appboy-ios-sdk) for implementation samples.
{% endtab %}
{% endtabs %}

## Analytics

### Setting User IDs

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) integration instructions for an in depth discussion of when to set and change a user ID.

```javascript
AppboyPlugin.changeUser("YOUR_USER_ID");
```

### Logging Custom Events

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) integration instructions for in depth discussion of event tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Setting Custom Attributes

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) integration instructions for in depth discussion of attribute tracking best practices and interfaces.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Logging Purchases

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) integration instructions for in depth discussion of revenue tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("testPurchaseWithNullCurrency", 10, null, 5, properties);
```

## News Feed

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/) integration instructions for information on how to integrate the News Feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal News Feed without further integration.

The Braze Cordova SDK has several methods to get the number of read/unread News Feed cards for different categories. See our [sample project implementation](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) for an example.

You can look at the sample [Android](https://github.com/Appboy/appboy-android-sdk) or [iOS](https://github.com/Appboy/appboy-ios-sdk) application and sample Cordova Android](https://github.com/Appboy/appboy-android-sdk) or [iOS](https://github.com/Appboy/appboy-ios-sdk) application implementation samples.
