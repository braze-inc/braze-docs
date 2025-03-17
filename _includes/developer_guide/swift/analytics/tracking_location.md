## Logging the current location

### Step 1: Configure your project

{% alert important %}
When using Braze location features, your application is responsible for requesting authorization for using location services. Be sure to review [Apple Developer: Requesting authorization to user location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

To enable location tracking, open your Xcode project and select your app. In the **General** tab, add the `BrazeLocation` module.

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
{% tab objective-c %}

In your `AppDelegate.m` file, import the `BrazeLocation` module at the top of the file. Add a `BrazeLocationProvider` instance to the Braze configuration, making sure all changes to the configuration are done prior to calling `Braze(configuration:)`. See `BRZConfigurationLocation` for the available configurations.

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

### Step 2: Log the user's location

Next, log the user's last-known location to Braze. The following examples assume you’ve assigned the Braze instance as a variable in your `AppDelegate`.

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
{% tab objective-c %}

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

{% alert tip %}
For more information, see [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).
{% endalert %}
