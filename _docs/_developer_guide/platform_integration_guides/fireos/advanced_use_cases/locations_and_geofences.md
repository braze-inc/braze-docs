---
nav_title: Locations & Geofences Integration for Android
platform: FireOS
page_order: 6

---

## Locations & Geofences

Geofences are only available in select Braze packages. For access please create a support ticket or speak with your Braze Customer Success Manager. Learn more in [Braze Docs]({{site.baseurl}}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences).

To support geofences for Android:

1. Your integration must support background push notifications.

2. Braze geofences or location collection must be enabled.

### Step 1: Update build.gradle

Add the [Google Play Services Location package][3] to your app level `build.gradle` using the [Google Play Services setup guide][10]:

```groovy
dependencies {
  compile "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### Step 2: Update the Manifest

Add fine location permissions and boot permissions to your `AndroidManifest.xml`:

```
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
```

Add the Braze boot receiver to the `application` element of your `AndroidManifest.xml`:

```
<receiver android:name="com.appboy.AppboyBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

{% alert note %}
If you are using a version of the Android SDK less than `2.3.0`, the following manifest
declaration is also required:

```
<service android:name="com.appboy.services.AppboyGeofenceService"/>
```
{% endalert %}

### Step 3: Enable Braze Location Collection

If you have not yet enabled Braze location collection, update your `braze.xml` file to include `com_appboy_enable_location_collection` and ensure its value is set to `true`.

```xml
<bool name="com_appboy_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0 Braze location collection is disabled by default.
{% endalert %}

Braze geofences are enabled if Braze location collection is enabled. If you would like to opt-out of our default location collection but still want to use geofences, it can be enabled selectively by setting the value of key `com_appboy_geofences_enabled` to `true` in `braze.xml`, independently of the value of `com_appboy_enable_location_collection`. 

```xml
<bool name="com_appboy_geofences_enabled">true</bool>
```

### Step 4: Obtain Location Permissions from the End User

For Android M and higher versions, you must request location permissions from the end user before gathering location information or registering geofences.

Add the following call to notify Braze when a user grants the location permission to your app:

```
Braze.getInstance(context).requestLocationInitialization();
```

This will cause the SDK to request geofences from Braze's servers and initialize geofence tracking.

See [`RuntimePermissionUtils.java`][4] in our sample application for an example implementation.

### Step 5: Enable Geofences on the Dashboard

Android only allows up to 100 geofences to be stored for a given app. Braze's Locations product will use up to 20 of these geofence slots if available. To prevent accidental or unwanted disruption to other geofence-related functionality in your app, location geofences must be enabled for individual Apps on the Dashboard.

For Braze's Locations product to work correctly, you should also ensure that your App is not using all available geofence spots.

##### Enable geofences from the Locations page:

![Braze Developer Console]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

##### Enable geofences from the App Settings page:

![Braze Developer Console]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})


### Note about Push to Sync

Note that Braze syncs geofences to devices using background push. In most cases, this will involve no code changes, as this feature requires no further integration on the part of the app.

However, note that if your application is stopped, receiving a background push will launch it in the background and its `Application.onCreate()` method will be called. If you have a custom `Application.onCreate()` implementation, you should defer automatic server calls and any other actions you would not want to be triggered by background push.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://github.com/Appboy/appboy-android-sdk/blob/91622eb6cd4bba2e625cc22f00ca38e6136a0596/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.java
[10]: https://developers.google.com/android/guides/setup
