# Disabling SDK Tracking

> This article shows how to disable data collection for your Android or FireOS application.

In order to comply with data privacy regulations, data tracking activity on the Android SDK can be stopped entirely using the method [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). This method will cause all network connections to be canceled, and the Braze SDK will not pass any data to Braze servers. If you wish to resume data collection at a later point in time, you can use the [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) method in the future to resume data collection.

Additionally, you can use the method [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) to fully clear all client-side data stored on the device.

