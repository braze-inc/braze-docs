---
nav_title: Disabling Android SDK Tracking
article_title: Disabling Data Collection for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "This article shows how to disable data collection for your Android or FireOS application."

---

# Disabling data collection for Android and FireOS

In order to comply with data privacy regulations, data tracking activity on the Android SDK can be stopped entirely using the method [`disableSDK()`][1]. This method will cause all network connections to be canceled, and the Braze SDK will not pass any data to Braze's servers. If you wish to resume data collection at a later point in time, you can use the [`enableSDK()`][2] method in the future to resume data collection.

Additionally, you can use the method [`wipeData()`][3] to fully clear all client-side data stored on the device.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html
