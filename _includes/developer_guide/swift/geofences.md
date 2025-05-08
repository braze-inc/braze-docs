{% alert important %}
As of iOS 14, geofences do not work reliably for users who choose to only give their approximate location permission.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Setting up geofences {#setting-up-geofences}

### Step 1: Configure the Braze dashboard

There are two ways to enable geofences for a particular app: from the **Locations** page or from the **App Settings** page.

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

### Step 2: Enable your app's location services

Braze location services must be enabled in your app. They are not enabled by default.

Follow the steps below to enable location services in your app. Optionally reference [this tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) for more information.

#### Add the `BrazeLocation` module

In the `General` tab of your `Application` configuration page, under `Frameworks, Libraries, and Embedded Content`, add the `BrazeLocation` module.

![Add the BrazeLocation module in your Xcode project]({% image_buster /assets/img_archive/add-brazeLocation-module-xcode.png %})

#### Update your `Info.plist`

Add the key `NSLocationAlwaysAndWhenInUseUsageDescription` or `NSLocationWhenInUseUsageDescription` to your `Info.plist` with a `String` value that describes why your application needs to track location.

This description will be shown when the system location prompt requests authorization and should clearly explain the benefits of location tracking to your users.

{% alert note %}
Apple has deprecated `NSLocationAlwaysUsageDescription`. For more information, see [Apple's developer documentation](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Step 3: Enable geofences in your code

In your app's code, enable geofences by setting `location.geofencesEnabled` to `true` on the `configuration` object that initializes the [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) instance. For other `location` configuration options, see our [Braze Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).
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

// Additional configuration customization...

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

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Step 3.1 (Optional) Enable background reporting

By default, geofences are only monitored if your app is in the foreground, or if it has `Always` authorization (which monitors all application states).

However, you can choose to monitor geofence events when your app is in the background or if [`When In Use` authorization](#swift_request-authorization) is active. To do this, add the `Background Mode -> Location updates` capability to your Xcode project.

![In Xcode, Background Mode > Location Updates]({% image_buster /assets/img_archive/xcode-background-modes-location-updates.png %})

Then, enable `allowBackgroundGeofenceUpdates` to let Braze extend your app's "When In Use" status by continuously monitoring location updates. This setting only works when your app is in the background. When the app re-opens, the existing background processes are paused and foreground processes are prioritized instead.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
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

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
To prevent battery drain and rate limiting, configure `distanceFilter` to a value that meets your app's specific needs. Setting `distanceFilter` to a higher value prevents your app from requesting your user's location too frequently.
{% endalert %}

### Step 4: Request authorization {#request-authorization}

When requesting authorization from a user, request either `When In Use` or `Always` authorization.

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
By default, `requestAlwaysAuthorization()` only grants your app `When In Use` authorization and will re-prompt your user for `Always` authorization after some time has passed.

However, you can choose to immediately prompt your user by first calling `requestWhenInUseAuthorization()` and then calling `requestAlwaysAuthorization()` after receiving your initial `When In Use` authorization.

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

### Step 5: Verify background push

Braze syncs geofences to devices using background push notifications. Follow these instructions to [set up silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) so that geofence updates from the server are properly handled.

{% alert note %}
To ensure that your application does not take any unwanted actions upon receiving Braze geofence sync notifications, follow the [ignoring silent push]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) article.
{% endalert %}

## Manually request geofences {#manually-request-geofences}

When the Braze SDK requests geofences from the backend, it reports the user's current location and receives geofences that are determined to be optimally relevant based on the location reported.

To control the location that the SDK reports for the purposes of receiving the most relevant geofences, you can manually request geofences by providing the desired coordinates.

### Step 1: Set `automaticGeofenceRequests` to `false`

You can disable automatic geofence requests in your `configuration` object passed to [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Set `automaticGeofenceRequests` to `false`.

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

### Step 2: Call `requestGeofences` manually

In your code, request geofences with the appropriate latitude and longitude.

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

## Frequently Asked Questions (FAQ) {#faq}

#### Why am I not receiving geofences on my device?

To confirm whether or not geofences are being received on your device, first use the [SDK Debugger tool]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) to check SDK's logs. You will then be able to see if geofences are successfully being received from the server and if there are any notable errors.

Below are other possible reasons geofences may not be received on your device:

##### iOS operating system limitations

The iOS operating system only allows up to 20 geofences to be stored for a given app. With geofences enabled, Braze will use up some of these 20 available slots.

To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual apps on the dashboard. For our location services to work correctly, check that your app is not using all available geofence spots.

##### Rate limiting

Braze has a limit of 1 geofence refresh per session to avoid unnecessary requests.

#### How does it work if I am using both Braze and non-Braze geofence features?

As mentioned above, iOS allows a single app to store a maximum of 20 geofences. This storage is shared by both Braze and non-Braze geofences and is managed by [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

For instance, if your app contains 20 non-Braze geofences, there would be no storage to track any Braze geofences (or vise versa). In order to receive new geofences, you will need to use [Apple's location APIs](https://developer.apple.com/documentation/corelocation) to stop monitoring some of the existing geofences on the device.

#### Can the Geofences feature be used while a device is offline?

A device needs to be connected to the internet only when a refresh occurs. Once it has successfully received geofences from the server, it is possible to log a geofence entry or exit even if the device is offline. This is because a device's location operates separately from its internet connectivity.

For example, say a device successfully received and registered geofences on session start and goes offline. If it then enters one of those registered geofences, it can trigger a Braze campaign.

#### Why are geofences not monitored when my app is backgrounded/terminated?

Without `Always` authorization, Apple restricts location services from running while an app is not in use. This is enforced by the operating system and is outside the control of the Braze SDK. While Braze offers separate configurations to run services while the app is in the background, there is no way to circumvent these restrictions for apps that are terminated without receiving explicit authorization from the user.