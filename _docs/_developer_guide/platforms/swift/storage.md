---
nav_title: Storage
article_title: Storage for iOS
platform: Swift
page_order: 8.9
page_type: reference
description: "This reference article describes the device-level properties captured by the Braze iOS Swift SDK."
---

# Storage

> This article describes the different device-level properties captured when using the Braze iOS Swift SDK.

## Device properties

By default, Braze will collect the following [device-level properties](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) to allow device, language, and time zone-based message personalization:

* Device Carrier (see note on the [`CTCarrier` deprecation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
* Device Locale
* Device Model
* Device OS Version
* Push Authorization Status
* Push Display Options
* Push Enabled
* Device Resolution
* Device Time Zone

{% alert note %}
The Braze SDK does not collect IDFA automatically. Apps may optionally pass IDFA to Braze by implementing the methods directly below. Apps must obtain explicit opt-in to tracking by the end user through the App Tracking Transparency framework before passing IDFA to Braze.

1. To set the advertising tracking state, use [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. To set the identifier for advertiser (IDFA), use [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

Configurable device fields are defined in the [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) enum. To disable or specify the device field you'd like to allowlist, add the fields to the [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) property of the `configuration` object.

For example, to specify time zone and locale collection to be allowlisted, set:

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, local time zone delivery will not function without the time zone.

To read more about the automatically collected device properties, visit our [SDK data collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

