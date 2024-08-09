---
nav_title: Other Integrations
article_title: Other integrations
page_order: 6
---

# Other integrations

> These are the other integrations supported in the Cordova Braze SDK.

{% multi_lang_include cordova/prerequisites.md %}

## In-app messaging

By default the Cordova SDK supports in-app messages with no changes. See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) or [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) integration examples for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) or the sample [Android](https://github.com/braze-inc/braze-android-sdk) or [iOS](https://github.com/braze-inc/braze-swift-sdk) application for implementation samples.

### GIF Support

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## News Feed

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

See the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) integration instructions for information on how to integrate the News Feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal News Feed without further integration.

The Braze Cordova SDK has several methods to get the number of read or unread News Feed cards for different categories. Check out a [sample project implementation](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) for an example.
