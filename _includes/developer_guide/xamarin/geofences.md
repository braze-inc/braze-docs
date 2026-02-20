{% multi_lang_include developer_guide/prerequisites/xamarin.md %} Additionally, you'll need to [set up silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Prerequisites

This is the minimum SDK versions needed to start using geofences:

{% sdk_min_versions xamarin:9.0.0 %}

## Setting up geofences {#setting-up-geofences}

### Step 1: Enable in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Next, follow the platform-specific instructions below for either Android or iOS:

{% tabs %}
{% tab Android %}

### Step 2: Add dependencies

Add the following NuGet package reference to your project:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Step 3: Update your AndroidManifest.xml

Add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
The background location access permission is required for geofences to work while the app is in the background on Android 10+ devices.
{% endalert %}

### Step 4: Configure Braze location collection

Ensure that location collection is enabled in your Braze configuration. If you want to enable geofences without automatic location collection, set the following in your `Braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Step 5: Request location permissions at runtime

You must request location permissions from the user before registering geofences. In your C# code, use the following pattern:

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

After permissions are granted, initialize Braze location collection:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Step 6: Manually request geofence updates (optional)

To manually request geofences for a specific location:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Geofences can only be requested once per session, either automatically by the SDK or manually with this method.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Step 2: Add dependencies

Add the following NuGet package reference to your project:

- `Braze.iOS.BrazeLocation`

### Step 3: Configure location usage in Info.plist

Add a usage description string for location services in your `Info.plist`:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple has deprecated `NSLocationAlwaysUsageDescription`. Use the keys above for iOS 14+.
{% endalert %}

### Step 4: Enable geofences in your Braze configuration

In your app startup code (e.g., `App.xaml.cs`), configure Braze with geofences enabled:

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### Step 5: Enable background location updates (optional)

To monitor geofences in the background, enable the **Location updates** background mode by adding the following configuration to your `Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Then, in your Braze configuration, set:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Set `DistanceFilter` to a value that meets your app's needs to avoid battery drain.
{% endalert %}

### Step 6: Request location authorization

Request either `When In Use` or `Always` authorization from the user:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Without `Always` authorization, iOS restricts location services from running while the app is not in use. This is enforced by the operating system and cannot be bypassed by the Braze SDK.
{% endalert %}
{% endtab %}
{% endtabs %}
