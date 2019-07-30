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

2. Braze location collection must be enabled.

>  On iOS, we are not strictly enforcing the Braze request processing policy for geofences. When geofences are enabled, the requests will automatically be sent up even if the processing policy is manual processing.

### Step 1: Enable Background Push

To fully utilize our geofence syncing strategy you must have [Background Push][6] enabled in addition to completing the standard push integration.

### Step 2: Check for Braze Background Push

Braze syncs geofences to devices using background push notifications. Follow the instructions [here][7] to ensure that your application does not take any unwanted actions upon receiving Braze's geofence sync notifications.

### Step 3: Add NSLocationAlwaysUsageDescription to your Info.plist

Add the key `NSLocationAlwaysUsageDescription` and `NSLocationAlwaysAndWhenInUseUsageDescription` to your `info.plist` with a `String` value that has a description of why your application needs to track location. Both keys are required by iOS 11.
This description will be shown when the system location prompt requests authorization and should clearly explain the benefits of location tracking to your users.

### Step 4: Request authorization from the user

The Braze iOS SDK can automatically request authorization from the user at app start if configured in our dashboard.

Otherwise, you can request authorization yourself and our SDK will wait until it has permission to start registering geofences.

### Step 5: Enable Geofences on the Dashboard

iOS only allows up to 20 geofences to be stored for a given app. Braze's Locations product will use up some of these 20 available geofence slots. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual Apps on the Dashboard.

For Braze's Locations product to work correctly, you should also ensure that your App is not using all available geofence spots.

##### Enable geofences from the Locations page:

![Appboy Developer Console]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

##### Enable geofences from the App Settings page:

![Appboy Developer Console]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

[6]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#ignoring-brazes-internal-push-notifications
[9]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
