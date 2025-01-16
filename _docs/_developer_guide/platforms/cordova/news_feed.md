---
page_order: 4
nav_title: News Feed
description: "Learn how to set up News Feed for the Braze Android SDK."
platform: 
  - Cordova
  - Android
  - FireOS
channel:
  - news feed
---

# News Feed

> Learn how to set up News Feed for the Braze Cordova SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Setting up News Feed

See the [Android]({{site.baseurl}}/developer_guide/platforms/android/news_feed/) and [iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/news_feed/integration/) integration instructions for information on how to integrate the News Feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal News Feed without further integration.

The Braze Cordova SDK has several methods to get the number of read or unread News Feed cards for different categories. Check out a [sample project implementation](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) for an example.
