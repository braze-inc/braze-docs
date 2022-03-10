---
nav_title: Cordova Integration
article_title: Cordova Integration
platform: 
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "This article covers initial SDK setup steps for Android and FireOS apps running on Cordova."

---

# Cordova integration

## Setting a custom API endpoint

A custom API endpoint can be configured via the `config.xml`. For example, to use the EU endpoint, see the following:

#### Android
```
<platform name="android">
    ...
    <preference name="com.appboy.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
#### iOS
```
<platform name="ios">
    ...
    <preference name="com.appboy.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```

## Push notifications

If you use the Cordova SDK default setup you won't have to make any new changes client-side. For modified integrations, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/) or [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) integration instructions.

## In-app messaging

By default the Cordova SDK supports in-app messages with no changes. See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) or [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) integration examples for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) or the sample [Android](https://github.com/Appboy/appboy-android-sdk) or [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) application for implementation samples.

## Analytics

### Setting user IDs

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) integration instructions for an in-depth discussion of when to set and change a user ID.

```javascript
AppboyPlugin.changeUser("YOUR_USER_ID");
```

### Logging custom events

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) integration instructions for in-depth discussion of event tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Setting custom attributes

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) integration instructions for in-depth discussion of attribute tracking best practices and interfaces.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Logging purchases

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) integration instructions for in-depth discussion of revenue tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("testPurchaseWithNullCurrency", 10, null, 5, properties);
```

## News Feed

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed) and [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/) integration instructions for information on how to integrate the News Feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal News Feed without further integration. 

The Braze Cordova SDK has several methods to get the number of read or unread News Feed cards for different categories. Check out a [sample project implementation](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) for an example.
