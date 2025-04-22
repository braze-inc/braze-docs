{% alert important %}
As of iOS 14, geofences do not work reliably for users who choose to only give their approximate location permission.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %} Additionally, you'll need to [set up silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

## Setting up geofences

### Step 1: Enable location services

Braze location services [must be enabled](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) through the SDK. They are not enabled by default.

### Step 2: Enable geofences

Enable geofences by setting `location.geofencesEnabled` to `true` on the `configuration` object that initializes the[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) instance. For other `location` configuration options, see [Braze Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).
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

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

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

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Configuring geofences for background reporting

By default, geofences are only monitored if your app is in the foreground, or it has `Always` authorization (which monitors all application states).

However, you can choose to monitor geofence events when your app is in the background or when it has the [`When In Use` authorization](#step-5) by adding the `Background Mode -> Location updates` capability to your Xcode project and enabling `allowBackgroundGeofenceUpdates`. This let's Braze extend your app's "in use" status by continuously monitoring location updates.

`allowBackgroundGeofenceUpdates` only works when your app is in the background. When it re-opens, it's existing background processes are paused, so foreground processes can be prioritized instead.

{% alert important %}
To prevent battery drain and rate limiting, be sure to configure `distanceFilter` to a value that meets your app's specific needs. Setting `distanceFilter` to a higher value prevents your app from requesting your user's location too frequently.
{% endalert %}

### Step 3: Verify background push

Braze syncs geofences to devices using background push notifications. Follow the [ignoring silent push]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) article to ensure that your application does not take any unwanted actions upon receiving Braze geofence sync notifications.

### Step 4: Update your `Info.plist`

Add the key `NSLocationAlwaysAndWhenInUseUsageDescription` or `NSLocationWhenInUseUsageDescription` to your `info.plist` with a `String` value that has a description of why your application needs to track location.

This description will be shown when the system location prompt requests authorization and should clearly explain the benefits of location tracking to your users.

{% alert note %}
Apple has deprecated `NSLocationAlwaysUsageDescription`. For more information, see [Apple's developer documentation](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Step 5: Request authorization {#step-5}

When requesting authorization from a user, you can request `When In Use` or `Always` authorization.

{% tabs local %}
{% tab When In Use %}
To request `When In Use` authorization, use the `requestWhenInUseAuthorization()` method:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
By default, `requestAlwaysAuthorization()` only grants your app `When In Use` authorization and will re-prompt your user for `Always` authorization after some time has passed. However, you can choose to immediately prompt your user by first calling `requestWhenInUseAuthorization()`, then calling `requestAlwaysAuthorization()` after receiving your initial `When In Use` authorization.

{% alert important %}
You can only immediately prompt for `Always` authorization a single time.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 6: Configure the dashboard

iOS only allows up to 20 geofences to be stored for a given app. With geofences enabled, Braze will use up some of these 20 available slots. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual apps on the dashboard. For our location services to work correctly, check that your app is not using all available geofence spots.

There are two ways to enable geofences for a particular app: from the **Locations** page or from the **Manage Settings** page.

{% tabs local %}
{% tab Locations %}
Enable geofences on the **Locations** page of the dashboard.

1. Go to **Audience** > **Locations**.
2. The number of apps in your workspace that currently have geofences enabled is displayed beneath the map, for example: **0 of 1 Apps with Geofences enabled**. Click this text.
3. Select the app to enable geofences. Click **Done.**
![The geofence options on the Braze locations page.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})
{% endtab %}

{% tab App Settings %}
Enable geofences from your app's settings.

1. Go to **Settings** > **App Settings**.
2. Select the app for which you wish to enable geofences.
3. Select the **Geofences Enabled** checkbox. Click **Save.**

![The geofence checkbox located on the Braze settings pages.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})
{% endtab %}
{% endtabs %}

## Disabling automatic geofence requests

### Step 1: Set `automaticGeofenceRequests` to `false`

You can disable automatic geofence requests in your `configuration` object passed to [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Set `automaticGeofenceRequests` to `false`. For example:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Step 2: Manually request geofences

When the Braze SDK requests geofences to monitor from the backend, it reports the user's current location and receives geofences that are determined to be optimally relevant based on the location reported. There is a rate limit of one geofence refresh per session.

To control the location that the SDK reports for the purposes of receiving the most relevant geofences, you can manually request geofences by providing the latitude and longitude of a location. It is recommended to disable automatic geofence requests when using this method. To do so, use the following code:

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
