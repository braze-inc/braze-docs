---
nav_title: Storage
article_title: Storage for iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze iOS SDK."

---

# Storage

this article describes the different device-level properties captured when using the braze ios sdk.

## Device properties

By default, Braze will collect the following [device-level properties](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) to allow device, language, and time zone-based message personalization:

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

Configurable device fields are defined in the [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179) enum. To disable or specify the device field you'd like to allowlist, assign the bitwise `OR` of desired fields to [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) in the `appboyOptions` of `startWithApiKey:inApplication:withAppboyOptions:`.

For example, to specify time zone and locale collection to be allowlisted, set:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, without the time zone, local time zone delivery will not function.

To read more about the automatically collected device properties, visit our [SDK Data Collection Options]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) article. 
