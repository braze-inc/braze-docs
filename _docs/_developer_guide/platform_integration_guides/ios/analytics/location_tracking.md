---
nav_title: Location Tracking
platform: iOS
page_order: 6
search_rank: 5
---
## Location Tracking

By default, Braze enables location tracking after the host application has gained permission from the user. Provided that users have opted into location tracking, Braze will log a single location for each user on session start.

### Requesting Location Tracking Permissions
The `allowRequestWhenInUseLocationPermission` method gives Braze permission to request WhenInUse authorization on your behalf the next time the application attempts to collect location in the foreground:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].locationManager allowRequestWhenInUseLocationPermission];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance().locationManager.allowRequestWhenInUseLocationPermission()
```

{% endtab %}
{% endtabs %}

### Logging A Single Location
To log a single location using Braze's location manager, use the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].locationManager logSingleLocation];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance().locationManager.logSingleLocation()
```

{% endtab %}
{% endtabs %}

### Disabling Automatic Location Tracking
Starting with Braze iOS SDK `v3.14.1`, you can disable automatic location tracking using the `Info.plist` file. Add the `Appboy` dictionary to your `Info.plist` file. Inside the `Appboy` dictionary, add the `DisableAutomaticLocation` boolean subentry and set the value to `YES`.

 In versions prior to `v3.14.1`, you can disable automatic location tracking at app startup time via the [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4] method. In the `appboyOptions` dictionary, set `ABKDisableAutomaticLocationCollectionKey` to `YES`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.startWithApiKey("YOUR-API-KEY",
inApplication:application,
withLaunchOptions:launchOptions,
withAppboyOptions:[ ABKDisableAutomaticLocationCollectionKey : true ]])
```

{% endtab %}
{% endtabs %}

### Manually Enabling iOS Location Targeting

If you wish to use your own `CLLocationManager` instead of Braze's provided location manager, you can follow the steps below to manually enable location targeting in your iOS application. Once location tracking is enabled, you can use Braze's methods to manually pass location tracking information along to Braze.

#### Setting Up Location Tracking

1. Click on the target for your project (using the left-side navigation), and select the “Build Phases” tab.
2. Click the button under “Link Binary With Libraries”
3. In the menu, select `CoreLocation.framework`
4. Mark this library as required using the pull-down menu next to `CoreLocation.framework`
5. Add `NSLocationWhenInUserUsageDescription` and/or `NSLocationAlwaysUsageDescription` as keys to your plist.
  - The value should be a string, which will be displayed when the system asking permission from your users.
6. See the following sample code to authorize `CLLocationManager` so Braze can collect location from your app:

```objc
@property (retain, nonatomic) CLLocationManager *locationManager;

- (void)startLocationUpdates {
  // Create the location manager if this object does not
  // already have one.
  if (self.locationManager == nil) {
    CLLocationManager \*locationManager = [[CLLocationManager alloc] init];
    self.locationManager = locationManager;
    [locationManager release];
  }

  self.locationManager.delegate = self;
  self.locationManager.desiredAccuracy = kCLLocationAccuracyBest;

  // Set a movement threshold for new events.
  self.locationManager.distanceFilter = 500; // meters

  if ([self.locationManager respondsToSelector:@selector(requestWhenInUseAuthorization)]) {
    [self.locationManager requestWhenInUseAuthorization];
  }
  /* When you want to request authorization even when the app is in the background, use requestAlwaysAuthorization.
   if ([self.locationManager respondsToSelector:@selector(requestAlwaysAuthorization)]) {
    [self.locationManager requestAlwaysAuthorization];
  } \*/
  [self.locationManager startUpdatingLocation];
}

#pragma location manager delegate method
- (void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation {
  // test that the horizontal accuracy does not indicate an invalid measurement
  if (newLocation.horizontalAccuracy < 0) return;
  // test the age of the location measurement to determine if the measurement is cached
  // in most cases you will not want to rely on cached measurements
  NSTimeInterval locationAge = -[newLocation.timestamp timeIntervalSinceNow];
  if (locationAge > 5.0) return;
}

- (void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error {
  // The location "unknown" error simply means the manager is currently unable to get the location.
  if ([error code] != kCLErrorLocationUnknown) {
    [self stopUpdatingLocation];
  }
}

- (void)stopUpdatingLocation {
  [self.locationManager stopUpdatingLocation];
  self.locationManager.delegate = nil;
}
```

For additional details please see this [helpful blog post][2].

#### Passing Location Data to Braze

The following two methods can be used to set the last known location for the user. Keep in mind that these methods are intended for use only where Braze's automatic location tracking has been disabled (i.e., `ABKDisableAutomaticLocationCollectionKey` has been set to `YES`).

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

For more information, see [`ABKUser.h`][5].

##### Implementation Examples

[`AppDelegate.m`][1] in the Stopwatch sample application shows how to authorize Braze to request location authorization on your behalf, and [`MiscViewController.m`][3] gives an example of logging location data.

### Not Compiling Location Request Authorization Code {#not-compiling-location-services-code}

If you don't use location services in your application, you can opt to instruct Braze not to compile location request authorization code in order to comply with recent Apple Store review policies. This flag removes all references to methods that request location-related authorization from the end user.

To do this, open your application main target's `Build Settings` in Xcode and add the `ABK_DISABLE_LOCATION_SERVICES=1` Preprocessor Macro to all relevant configurations.

![Disable Location][6]

If you have a Cocoapods integration, select the `Appboy-iOS-SDK` target from your Pods project in Xcode, open the `Build Settings` tab, and add the `ABK_DISABLE_LOCATION_SERVICES=1` Preprocessor Macro to all relevant configurations.

![Disable Location][7]

This feature is not available for Carthage integration yet.

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[2]: http://nevan.net/2014/09/core-location-manager-changes-in-ios-8/
[3]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/MiscViewController.m
[4]: #customizing-appboy-on-startup
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKUser.h
[6]: {% image_buster /assets/img_archive/ios_disable_location_01.png %}
[7]: {% image_buster /assets/img_archive/ios_disable_location_02.png %}
