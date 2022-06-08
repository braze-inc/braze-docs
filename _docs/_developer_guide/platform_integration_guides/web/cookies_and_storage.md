---
nav_title: Cookies and Storage
article_title: Cookies and Storage for Web
platform: Web
page_order: 15
page_type: reference
description: "This reference article describes the different cookies used by the Braze Web SDK."

---

# Cookies and storage

This article describes the different cookies used by the Braze Web SDK.

Before reading on, note that the Braze Web SDK will not store any data in the browser (cookies or otherwise) until your website [initializes][5] the SDK.

Additionally, these values are subject to change and should not be accessed directly through your integration. Instead, see our [Javascript documentation][1] for our public API interfaces.

{% include archive/web-v4-rename.md %}

## Cookies {#cookies}

This section provides information on how cookies in the Braze Web SDK can be set and managed. The Braze Web SDK is built to provide you with maximum flexibility, legal compliance, and messaging relevance.

When Braze creates cookies, they are stored with a one-year expiration that automatically renews on new sessions.

### Disabling cookies {#disable-cookies}

To disable all cookies, use the [`noCookies`][6] option when initializing the Web SDK. 
Disabling cookies will prevent you from associating anonymous users who navigate across sub-domains and will result in a new user on each subdomain.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

To stop Braze tracking in general, or to clear all stored browser data, see the [`disableSDK`][3] and [`wipeData`][4] SDK methods, respectively. These two methods can be useful should a user revoke consent or you want to stop all Braze functionality after the SDK has already been initialized.

### List of cookies

|Cookie|Description|Size|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Used to determine whether the currently logged-in user has changed and to associate events with the current user.|Based on the size of the value passed to `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Out-of-the-box randomly generated string used to determine whether the user is starting a new or existing session to sync messages and calculate session analytics.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|Out-of-the-box randomly generated string used to identify anonymous users, and to differentiate users' devices and enables device-based messaging.|~200 bytes|
|`ab.optOut`|Used to store a user's opt-out preference when `disableSDK` is called|~40 bytes|
|`ab._gd`|Temporarily created (and then deleted) to determine the root-level cookie domain, which allows the SDK to work properly across sub-domains.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Device properties

By default, Braze will collect the following device-level properties to allow device, language, and time zone based message personalization:

* BROWSER
* BROWSER_VERSION
* LANGUAGE
* OS
* RESOLUTION
* TIME_ZONE
* USER_AGENT

You can disable or specify the properties you wish to collect by setting the `devicePropertyAllowlist` initialization option to a list of [`DeviceProperties`][2]. 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

By default, all fields are enabled. Note that without some properties, not all features will function properly. For instance, local time zone delivery will not function without the time zone.

To read more about the automatically collected device properties, visit [SDK data collection options]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata
[5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[6]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions
