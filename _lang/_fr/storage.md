---
nav_title: Storage
article_title: Storage for Android/FireOS
platform:
  - Android
  - FireOS
page_order: 9
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze Android SDK."
---

# Storage

This article describes the different device-level properties captured when using the Braze Android SDK.

## Device properties

By default, Braze will collect the following [device-level properties](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/enums/DeviceKey.html) to allow device, language, and time zone-based message personalization:

* AD_TRACKING_ENABLED
* ANDROID_VERSION
* CARRIER
* GOOGLE_ADVERTISING_ID
* IS_BACKGROUND_RESTRICTED
* LOCALE
* MODEL
* NOTIFICIATION_ENABLED
* RESOLUTION
* TIMEZONE

You can disable or specify the properties you wish to collect by setting them using [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDeviceObjectAllowlistEnabled-boolean-) and [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDeviceObjectAllowlist-java.util.EnumSet-).

The following example showcases allowlisting the device object to only include the Android OS version and device locale in the device object:
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, without the time zone, local time zone delivery will not function.

To read more about the automatically collected device properties, visit our [SDK Data Collection Options]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) article. 
