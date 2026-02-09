---
nav_title: Disable iOS SDK tracking
article_title: Disable SDK Tracking for iOS
platform: iOS
page_order: 8
description: "This article shows how to disable data collection for your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Disable data collection for iOS

To comply with data privacy regulations, data tracking activity on the iOS SDK can be stopped entirely using the [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733) method. This method will cause all network connections to be canceled, and the Braze SDK will not pass any data to our servers. If you wish to resume data collection later, you can use the [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) method in the future to resume data collection.

Additionally, you can use the method [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) to fully clear all client-side data stored on the device.

Unless a user uninstalls all apps from a vendor on a given device, the next Braze SDK and app runs after calling `wipeDataAndDisableForAppRun()` will result in our server re-identifying that user via their device identifier (IDFV). In order to fully remove all user data, you should combine a call to `wipeDataAndDisableForAppRun` with a request to delete data on the server via the Braze [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint).

## iOS SDK v5.7.0+
For devices using iOS SDK v5.7.0 and above, when [disabling IDFV collection]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfv-collection---swift/), calling [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) will not result in our server re-identifying that user via their device identifier (IDFV).