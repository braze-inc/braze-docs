---
nav_title: Locations & Geofences
article_title: Locations & Geofences for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "This reference article covers how to implement locations and geofences in your Android or FireOS application."
Tool:
  - Location

---

# Locations and geofences

[Geofences]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/) are only available in select Braze packages. For access, create a [support ticket][support] or speak with your Braze customer success manager.

To support geofences for Android:

1. Your integration must support background push notifications.
2. Braze geofences or location collection must be enabled.

## Step 1: Update build.gradle

Add `android-sdk-location` to your app-level `build.gradle`. Also, add the Google Play Services [location package][3] using the Google Play Services [setup guide][10]:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## Step 2: Update the manifest

Add boot, fine location, and background location permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
The background location access permission was added in Android 10 and is required for Geofences to work while the app is backgrounded for all Android 10+ devices.
{% endalert %}

Add the Braze boot receiver to the `application` element of your `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

{% alert note %}
If you are using a version of the Android SDK less than `2.3.0`, the following manifest declaration is also required:

```
<service android:name="com.appboy.services.AppboyGeofenceService"/>
```
{% endalert %}

## Step 3: Enable Braze location collection

If you have not yet enabled Braze location collection, update your `braze.xml` file to include `com_braze_enable_location_collection` and ensure its value is set to `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0, Braze location collection is disabled by default.
{% endalert %}

Braze geofences are enabled if Braze location collection is enabled. If you would like to opt-out of our default location collection but still want to use geofences, it can be enabled selectively by setting the value of key `com_braze_geofences_enabled` to `true` in `braze.xml`, independently of the value of `com_braze_enable_location_collection`:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## Step 4: Obtain location permissions from the end user

For Android M and higher versions, you must request location permissions from the end user before gathering location information or registering geofences.

Add the following call to notify Braze when a user grants the location permission to your app:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

This will cause the SDK to request geofences from Braze's servers and initialize geofence tracking.

See [`RuntimePermissionUtils.java`][4] in our sample application for an example implementation.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY_PERMISSION_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.");
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
          Braze.getInstance(context).requestLocationInitialization();
        } else {
          Log.i(TAG, "Required location permissions NOT granted.");
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  fun handleOnRequestPermissionsResult(context: Context, requestCode: Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false
      }
    }
    return true
  }
}
```

{% endtab %}
{% endtabs %}

Using the preceding sample code is done via:

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

## Step 5: Enable geofences on the dashboard

Android only allows up to 100 geofences to be stored for a given app. Braze's locations product will use up to 20 geofence slots if available. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual apps on the dashboard.

For Braze's locations product to work correctly, you should also ensure that your app is not using all available geofence spots.

### Enable geofences from the locations page

![The geofence options on the Braze locations page.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Enable geofences from the settings page

![The geofence checkbox located on the Braze settings pages.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## Step 6: Manually request geofence updates (optional)

By default, Braze automatically retrieves the device's location and requests geofences based on that collected location. However, you can manually provide a GPS coordinate that will be used to retrieve proximal Braze Geofences instead. To manually request Braze Geofences, you must disable automatic Braze Geofence requests and provide a GPS coordinate for requests.

#### Part 1: Disable automatic geofence requests

Automatic Braze Geofence requests can be disabled in your `braze.xml` file by setting `com_braze_automatic_geofence_requests_enabled` to `false`:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

This can additionally be done at runtime via:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### Part 2: Manually request Braze geofence with GPS coordinate

Braze Geofences are manually requested via the [`requestGeofences()`][11] method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Braze Geofences can only be requested once per session, either automatically by the SDK or manually with this method.
{% endalert %}

## Push to sync

Note that Braze syncs geofences to devices using background push. In most cases, this will involve no code changes, as this feature requires no further integration on the part of the app.

However, note that if your application is stopped, receiving a background push will launch it in the background and its `Application.onCreate()` method will be called. If you have a custom `Application.onCreate()` implementation, you should defer automatic server calls and any other actions you would not want to be triggered by background push.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://github.com/Appboy/appboy-android-sdk/blob/91622eb6cd4bba2e625cc22f00ca38e6136a0596/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.java
[10]: https://developers.google.com/android/guides/setup
[11]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html
[support]: {{site.baseurl}}/braze_support/
