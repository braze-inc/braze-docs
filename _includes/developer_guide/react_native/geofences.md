{% alert important %}
Geofences are supported on **both iOS and Android** in the React Native SDK. The `requestLocationInitialization` method is Android-only and is not required for iOS. The `requestGeofences` method is available on both platforms. By default, the SDK can automatically request and monitor geofences when location is available; you can rely on this automatic configuration or call `requestGeofences` to request manually.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} On Android, you'll need to [set up silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) for geofence sync.

## Setting up geofences {#setting-up-geofences}

### Step 1: Enable in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Step 2: Complete native Android setup

Because the React Native SDK uses the native Braze Android SDK, complete the native Android geofence setup for your project. The iOS equivalent of these steps is covered in the native Swift SDK geofences guide ([steps 2.2 to 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)); step 2.1 (Add the BrazeLocation module) is not required for React Native because BrazeLocation is already included implicitly with the Braze React Native SDK.

1. **Update `build.gradle`** – Add `android-sdk-location` and Google Play Services location. See [Android geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Update the manifest** – Add location permissions and the Braze boot receiver. See [Android geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Enable Braze location collection** – Update your `braze.xml` file. See [Android geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Step 3: Complete native iOS setup

Because the React Native SDK uses the native Braze iOS SDK, complete the native iOS geofence setup for your project by following the native Swift SDK instructions starting from step 2.2: update your `Info.plist` with location usage descriptions (step 2.2), and enable geofences in your Braze configuration including `automaticGeofenceRequests = true` (step 3); optionally enable background reporting (step 3.1). Step 2.1 (Add the BrazeLocation module) is not required—BrazeLocation is already included implicitly with the Braze React Native SDK. See [iOS geofences, steps 2.2 to 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Step 4: Request geofences from JavaScript

**On Android:** After the user grants location permissions, call `requestLocationInitialization()` to initialize Braze location features and request geofences from Braze servers. This method is not supported on iOS and is not required for iOS.

**On iOS:** The equivalent is to enable the `automaticGeofenceRequests` configuration in your native Swift or Objective-C Braze configuration (see Step 3). With that enabled, the SDK automatically requests and monitors geofences when location is available; no JavaScript call equivalent to `requestLocationInitialization` is required.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Step 5: Manually request geofences (optional)

On both iOS and Android, you can manually request a geofence update for a specific GPS coordinate using `requestGeofences`. By default, Braze automatically retrieves the device's location and requests geofences. To manually provide a coordinate instead:

1. **Disable automatic geofence requests** – On Android, set `com_braze_automatic_geofence_requests_enabled` to `false` in your `braze.xml`. On iOS, set `automaticGeofenceRequests` to `false` in your Braze configuration.
2. **Call `requestGeofences`** with the desired latitude and longitude:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Geofences can only be requested once per session, either automatically by the SDK or manually with this method.
{% endalert %}
