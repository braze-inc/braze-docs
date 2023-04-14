---
nav_title: Storage
article_title: Storage for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 9
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze Android SDK."

---

# Storage

> This article describes the different device-level properties captured when using the Braze Android SDK.

## Device properties

By default, Braze will collect the following [device-level properties][1] to allow device, language, and time zone-based message personalization:

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` and `TIMEZONE` aren't collected if they are `null` or blank. `GOOGLE_ADVERTISING_ID` is not collected automatically by the SDK and must be passed in via `com.appboy.IAppboy.setGoogleAdvertisingId`.
{% endalert %}

You can disable or specify the properties you wish to collect by setting them using [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`][2] and [`BrazeConfig.Builder.setDeviceObjectAllowlist()`][3].

The following example showcases allowlisting the device object to only include the Android OS version and device locale in the device object:
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, local time zone delivery will not function without the time zone.

Visit our [SDK Data Collection]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) article to read more about the automatically collected device properties.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html
