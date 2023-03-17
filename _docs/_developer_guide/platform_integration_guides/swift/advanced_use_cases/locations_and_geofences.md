---
nav_title: Locations & Geofences
article_title: Location & Geofences for iOS
platform: Swift
page_order: 6
description: "This reference article covers how to implement locations and geofences in your iOS application."
Tool:
  - Location

---

# Locations and geofences

Geofences are only available in select Braze packages. For access, create a [support ticket][support] or speak with your Braze customer success manager.

To support geofences for iOS:

1. Your integration must support background push notifications.
2. Braze Geofences [must be enabled][1] through the SDK explicitly by enabling geofence collection. They are not enabled by default.

{% alert important %}
As of iOS 14, Geofences do not work reliably for users who choose to give their approximate location permission.
{% endalert %}

## Step 1: Enable background push

To fully utilize our geofence syncing strategy, you must have [background push][6] enabled in addition to completing the standard push integration.

## Step 2: Enable geofences

Enable geofences by setting `location.geofencesEnabled` to `true` on the `configuration` object that initializes the[`Braze`][1] instance.
{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

## Step 3: Check for Braze background push

Braze syncs geofences to devices using background push notifications. Follow the [iOS customization][7] article to ensure that your application does not take any unwanted actions upon receiving Braze's geofence sync notifications.

## Step 4: Add NSLocationAlwaysUsageDescription to your Info.plist

Add the key `NSLocationAlwaysUsageDescription` and `NSLocationAlwaysAndWhenInUseUsageDescription` to your `info.plist` with a `String` value that has a description of why your application needs to track location. Both keys are required by iOS 11 or later.
This description will be shown when the system location prompt requests authorization and should clearly explain the benefits of location tracking to your users.

## Step 5: Request authorization from the user

The Geofences feature is only functional while `Always` location authorization is granted.

To request for `Always` location authorization, use the following code:

{% tabs %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% endtabs %}

## Step 6: Enable geofences on the dashboard

iOS only allows up to 20 geofences to be stored for a given app. Braze's locations product will use up some of these 20 available geofence slots. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual apps on the dashboard.

For Braze's Locations product to work correctly, you should also ensure that your app is not using all available geofence spots.

### Enable geofences from the locations page:

![The geofence options on the Braze locations page.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Enable geofences from the settings page:

![The geofence checkbox located on the Braze settings pages.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Disabling automatic geofence requests

You can disable automatic geofence requests in your `configuration` object passed to [`init(configuration)`][4]. Set `automaticGeofenceRequests` to `false`. For example:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.automaticGeofencesRequest = false;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

If you choose to use this option, you will need to manually request geofences for the feature to work.

## Manually requesting geofences

When the Braze SDK requests geofences to monitor from the backend, it reports the user's current location and receives geofences that are determined to be optimally relevant based on the location reported. There is a rate limit of one geofence refresh per session.

To control the location that the SDK reports for the purposes of receiving the most relevant geofences, starting in iOS SDK version 3.21.3, you can manually request geofences by providing the latitude and longitude of a location. It is recommended to disable automatic geofence requests when using this method. To do so, use the following code:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

[1]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/
[6]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/
[support]: {{site.baseurl}}/braze_support/
