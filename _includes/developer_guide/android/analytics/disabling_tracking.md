## Disabling data tracking

To disable data-tracking activity on the Android SDK, use the method [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). This will cause all network connections to be canceled, meaning the Braze SDK will no longer pass any data to Braze servers.

## Wiping previously-stored data

You can use the method [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) to fully clear all client-side data stored on the device.

## Resuming data tracking

To resume data collection, you can use the [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) method. Keep in mind, this will not restore any previously wiped data.
