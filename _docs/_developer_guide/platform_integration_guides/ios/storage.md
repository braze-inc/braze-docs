---
nav_title: Storage
platform: iOS
page_order: 15
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze iOS SDK."

---

# Storage

This article describes the different cookies used by the Braze iOS SDK.

## Device Properties

By default, Braze will collect the following [device-level properties](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) to allow device, language, and timezone based message personalization:

* Device Resolution
* Device Carrier
* Device Locale
* Device Model
* Device OS Version
* IDFV
* IDFA
* Push Enabled
* Device Time Zone
* Push Auth Status
* Ad Tracking Enabled

You can disable or speicfy the properties you wish to collect by setting the 

Configurable device fields are defined in the `ABKDeviceOptions` enum. To specify whitelisted device fields, assign the bitwise `OR` of desired fields to `ABKDeviceWhitelistKey` in the `appboyOptions` of `startWithApiKey:inApplication:withAppboyOptions:`.

For example, to specify timezone and locale collection, to be whitelisted set:
```
appboyOptions[ABKDeviceWhitelistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, without the time zone, local timezone delivery will not function.

To read more about the automatically collected device properties, visit our [SDK Data Collection Options](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) article. 
