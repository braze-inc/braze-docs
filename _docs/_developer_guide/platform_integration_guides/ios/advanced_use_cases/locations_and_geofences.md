---
nav_title: Locations & Geofences Integration for iOS
platform: iOS
page_order: 6
search_rank: 5
---
## Locations & Geofences

Geofences are only available in select Braze packages. For access please create a support ticket or speak with your Braze Customer Success Manager. Learn more in [Docs]({{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences).

To support geofences for iOS:

1. Your integration must support background push notifications.

2. Braze Geofences must be enabled through the SDK either implicitly by enabling location collection or explicitly by enabling geofence collection. They are not enabled by default.

### Step 1: Enable Background Push

To fully utilize our geofence syncing strategy you must have [Background Push][6] enabled in addition to completing the standard push integration.

### Step 2: Enable Geofences

By default, geofences are enabled based on whether automatic location collection is enabled. You can enable geofences using the `Info.plist` file. Add the `Appboy` dictionary to your `Info.plist` file. Inside the `Appboy` dictionary, add the `EnableGeofences` boolean subentry and set the value to `YES`.

 You can also enable geofences at app startup time via the [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4] method. In the `appboyOptions` dictionary, set `ABKEnableGeofencesKey` to `YES`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].locationManager logSingleLocation];
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.locationManager.logSingleLocation()
Appboy.startWithApiKey("YOUR-API-KEY",
inApplication:application,
withLaunchOptions:launchOptions,
withAppboyOptions:[ ABKEnableGeofencesKey : true ]])
```

{% endtab %}
{% endtabs %}


### Step 3: Check for Braze Background Push

Braze syncs geofences to devices using background push notifications. Follow the instructions [here][7] to ensure that your application does not take any unwanted actions upon receiving Braze's geofence sync notifications.

### Step 4: Add NSLocationAlwaysUsageDescription to your Info.plist

Add the key `NSLocationAlwaysUsageDescription` and `NSLocationAlwaysAndWhenInUseUsageDescription` to your `info.plist` with a `String` value that has a description of why your application needs to track location. Both keys are required by iOS 11.
This description will be shown when the system location prompt requests authorization and should clearly explain the benefits of location tracking to your users.

### Step 5: Request authorization from the user

The Braze iOS SDK can automatically request authorization from the user at app start if configured in our dashboard.

Otherwise, you can request authorization yourself and our SDK will wait until it has permission to start registering geofences.

### Step 6: Enable Geofences on the Dashboard

iOS only allows up to 20 geofences to be stored for a given app. Braze's Locations product will use up some of these 20 available geofence slots. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual Apps on the Dashboard.

For Braze's Locations product to work correctly, you should also ensure that your App is not using all available geofence spots.

##### Enable geofences from the Locations page:

![Appboy Developer Console]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

##### Enable geofences from the App Settings page:

![Appboy Developer Console]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

[4]: #customizing-appboy-on-startup
[6]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#ignoring-brazes-internal-push-notifications
[9]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
