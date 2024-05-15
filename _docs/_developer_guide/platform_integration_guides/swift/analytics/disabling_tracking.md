---
nav_title: Disabling iOS SDK Tracking
article_title: Disabling SDK Tracking for iOS
platform: Swift
page_order: 8
description: "This article shows how to disable data collection for the Swift SDK."

---

# Disabling iOS SDK tracking

> To comply with data privacy regulations, data tracking activity on the iOS SDK can be stopped entirely by setting the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property to `false` on your Braze instance. 

When `enabled` is set to `false`, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc. To resume data collection, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) to `true`.

You can also use the [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) method to fully clear locally-stored SDK data on a user's device.

Keep in mind, if you're using Swift SDK version 5.7.0 and earlier, or `useUUIDAsDeviceId` is set to `false`, your Identifier for Vendors (IDFV) will be used as the device ID instead, meaning additonal steps are required to fully clear locally-stored SDK data. In both cases, after calling `wipeData()`, Braze will continue to re-identify that user using your IDFV. To completely clear their user data from Braze, simultaneously call `wipeData()` while making a post request to [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

Starting with version 7.0.0, the Braze Swift SDK randomly generates a UUID for device IDs instead. Similarly, calling `wipeData()` also randomly generates a new device ID.
