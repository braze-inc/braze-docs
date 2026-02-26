{% alert important %}
Geofences are supported on **Android only** in the React Native SDK. The `requestGeofences` and `requestLocationInitialization` methods are no-ops on iOS.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Additionally, you'll need to [set up silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) for geofence sync.

## Setting up geofences {#setting-up-geofences}

### Step 1: Enable in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Step 2: Complete native Android setup

Because the React Native SDK uses the native Braze Android SDK under the hood, complete the native Android geofence setup for your project:

1. **Update `build.gradle`** – Add `android-sdk-location` and Google Play Services location. See [Android geofences – Step 2]({{site.baseurl}}/developer_guide/geofences/?sdktab=android#setting-up-geofences).
2. **Update the manifest** – Add location permissions and the Braze boot receiver. See [Android geofences – Step 3]({{site.baseurl}}/developer_guide/geofences/?sdktab=android#setting-up-geofences).
3. **Enable Braze location collection** – Update your `braze.xml` file. See [Android geofences – Step 4]({{site.baseurl}}/developer_guide/geofences/?sdktab=android#setting-up-geofences).

### Step 3: Request geofences from JavaScript

After the user grants location permissions, call `requestLocationInitialization()` to initialize Braze location features and request geofences from Braze servers:

```javascript
import Braze from '@braze/react-native-sdk';

// Call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Step 4: Manually request geofences (optional)

By default, Braze automatically retrieves the device's location and requests geofences. To manually provide a GPS coordinate instead:

1. **Disable automatic geofence requests** – Set `com_braze_automatic_geofence_requests_enabled` to `false` in your `braze.xml`.
2. **Call `requestGeofences`** with the desired latitude and longitude:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Geofences can only be requested once per session, either automatically by the SDK or manually with this method.
{% endalert %}
