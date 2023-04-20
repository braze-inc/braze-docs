---
nav_title: Location Tracking
article_title: Location Tracking for iOS
platform: Swift
page_order: 6
description: "This article shows how to configure location tracking for your iOS application."
Tool:
  - Location

---

# Location tracking for iOS

By default, Braze disables location tracking. We enable location tracking after the host application has opted into location tracking and gained permission from the user. Provided users have opted into location tracking, Braze will log a single location for each user on session start.

## Enabling automatic location tracking

Go over [Requesting Authorization for Location Services](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) and make sure to configure your application purpose strings. When using Braze location features, your application is responsible for requesting authorization for using location services. 

To enable location tracking, add the `BrazeLocation` module in the **General** tab of your application configuration page.

{% tabs %}
{% tab swift %}

In your `AppDelegate.swift` file, import the `BrazeLocation` module at the top of the file. Add a `BrazeLocationProvider` instance to the Braze configuration, making sure all changes to the configuration are done prior to calling `Braze(configuration:)`. See `Braze.Configuration.Location` for the available configurations.

```swift
import UIKit
import BrazeKit
import BrazeLocation

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    configuration.logger.level = .info
    configuration.location.brazeLocationProvider = BrazeLocationProvider()
    configuration.location.automaticLocationCollection = true
    configuration.location.geofencesEnabled = true
    configuration.location.automaticGeofenceRequests = true
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    return true
  }

}

```

{% endtab %}
{% tab OBJECTIVE-C %}

In your `AppDelegate.m` file, import the `BrazeLocation` module at the top of the file. Add a `BrazeLocationProvider` instance to the Braze configuration, making sure all changes to the configuration are done prior to calling Braze(configuration:). See `BRZConfigurationLocation` for the available configurations.

```objc
#import "AppDelegate.h"

@import BrazeKit;
@import BrazeLocation;

@implementation AppDelegate

#pragma mark - Lifecycle

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
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

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}

@end
```

{% endtab %}
{% endtabs %}

### Passing location data to Braze

The following methods can be used to manually set the last known location for the user. These examples assume you’ve assigned the Braze instance as a variable in the AppDelegate.



{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude)
```

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude,
                                             altitude:altitude,
                                             horizontalAccuracy:horizontalAccuracy,
                                             verticalAccuracy:verticalAccuracy)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy];

```

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy
                                                altitude:altitude
                                        verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% endtabs %}

Refer to [`Braze.User.swift`][5] for more information.

[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/
