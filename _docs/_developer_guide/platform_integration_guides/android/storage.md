---
nav_title: Storage
platform: iOS
page_order: 15
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze Android SDK."

---

# Storage

This article describes the different cookies used by the Braze Android SDK.

## Device Properties

By default, Braze will collect the following device-level properties to allow device, language, and timezone based message personalization:

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

Added the ability to optionally whitelist keys in the device object. See `AppboyConfig.Builder.setDeviceObjectWhitelistEnabled()` and `AppboyConfig.Builder.setDeviceObjectWhitelist()` for more information.

The following example showcases whitelisting the device object to only include the Android OS version and device locale in the device object:
```
  new AppboyConfig.Builder()
      .setDeviceObjectWhitelistEnabled(true)
      .setDeviceObjectWhitelist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));

```
By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, without the time zone, local timezone delivery will not function.

To read more about the automatically collected device properties, visit our [SDK Data Collection Options](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) article. 
