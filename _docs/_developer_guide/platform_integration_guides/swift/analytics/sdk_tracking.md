---
nav_title: iOS SDK Tracking
article_title: SDK Tracking for iOS
platform: Swift
page_order: 8
description: "This article shows how to manage tracking data collection for the Swift SDK."

---

# Disabling iOS SDK tracking

> To comply with data privacy regulations, data tracking activity on the iOS SDK can be stopped entirely by setting the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property on the Braze instance to `false`.

When set to `false`, the Braze SDK ignores any call to the public API. The SDK also cancels all in-flight actions (network requests, event processing, etc.). If you wish to resume data collection, you can set the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) property to `true`.

Additionally, you can use the method [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) to fully clear locally stored SDK data on the device.

Unless a user uninstalls all apps from a vendor on a given device, the next time the Braze SDK runs after calling `wipeData()` will result in our server re-identifying that user via their device identifier. In order to fully remove all user data, you should combine a call to `wipeData()` with a request to delete data on the server via the Braze [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

# Declaring Data for Tracking Purposes

In iOS 17, Apple introduced new data tracking policies and enforcement mechanisms via [privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests). Using privacy manifests, app developers and SDK providers can declare domains intended for collecting data used in third-party advertising. If an end user does not accept [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) permissions, Apple will block any connections to the domains listed in the privacy manifest. To understand what circumstances require tracking permissions, refer to Apple's page on [User privacy and data user](https://developer.apple.com/app-store/user-privacy-and-data-use/).

Braze offers granular controls within the Swift SDK to declare and manage your data collection practices. If you intend to collect user data for third-party advertising, refer to the [integration tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking) to set up your app for compliance. However, if you do not intend to collect user data for such purposes, there are no action items needed from your end.

For the full list of data types that can be configured for tracking, refer to the tracking properties [here](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty).
