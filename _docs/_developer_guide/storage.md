---
nav_title: Storage
article_title: Storage for iOS
page_order: 3.60
page_type: reference
description: "Learn about the different device-level properties that are stored by the Braze SDK."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Storage

> Learn about the different device-level properties that are stored by the Braze SDK.

## Device properties

By default, Braze will collect the following device-level properties to allow device, language, and time zone-based message personalization:

{% tabs %}
{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}

{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` and `TIMEZONE` aren't collected if they are `null` or blank. `GOOGLE_ADVERTISING_ID` is not collected automatically by the SDK and must be passed in via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Device Carrier (see note on the [`CTCarrier` deprecation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Device Locale
- Device Model
- Device OS Version
- Push Authorization Status
- Push Display Options
- Push Enabled
- Device Resolution
- Device Time Zone

{% alert note %}
The Braze SDK does not collect IDFA automatically. Apps may optionally pass IDFA to Braze by implementing the methods directly below. Apps must obtain explicit opt-in to tracking by the end user through the App Tracking Transparency framework before passing IDFA to Braze.

1. To set the advertising tracking state, use [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. To set the identifier for advertiser (IDFA), use [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}
{% endtabs %}

By default, all properties are enabled. However, you can choose to enable or disable them manually. Keep in mind, some Braze SDK features require specific properties (such as local time zone delivery and time zone), so be sure to test your configuration before releasing to production.

{% tabs %}
{% tab web %}
For example, you can specify the device language to be allowlisted. For more information, see refer to the `devicePropertyAllowlist` option for [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}

{% tab android %}
For example, you can specify the Android OS version and device locale to be allowlisted. For more information, see the [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) and [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) methods. 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
For example, you can specify time zone and locale collection to be allowlisted. For more information, see the [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) property of the `configuration` object.

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
To learn more about automatically-collected device properties, see [SDK Data Collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Storing cookies (web only) {#cookies}

After [initializing the Web Braze SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) it'll create and store cookies with a 400-day expiration that automatically renews on new sessions.

The following cookies are stored:

|Cookie|Description|Size|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Used to determine whether the currently logged-in user has changed and to associate events with the current user.|Based on the size of the value passed to `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Randomly-generated string used to determine whether the user is starting a new or existing session to sync messages and calculate session analytics.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|Randomly-generated string used to identify anonymous users, and to differentiate users' devices and enables device-based messaging.|~200 bytes|
|`ab.optOut`|Used to store a user's opt-out preference when `disableSDK` is called|~40 bytes|
|`ab._gd`|Temporarily created (and then deleted) to determine the root-level cookie domain, which allows the SDK to work properly across sub-domains.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Disabling cookies {#disable-cookies}

To disable all cookies, use the [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) option when initializing the Web SDK. This will prevent you from associating anonymous users who navigate across sub-domains and will result in a new user on each subdomain.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

To stop Braze tracking in general, or to clear all stored browser data, see the [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) and [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) SDK methods, respectively. These two methods can be useful should a user revoke consent or you want to stop all Braze functionality after the SDK has already been initialized.
