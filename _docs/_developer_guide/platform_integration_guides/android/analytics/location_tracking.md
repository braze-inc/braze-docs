---
nav_title: Location Tracking
article_title: Location Tracking for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "This article shows how to configure location tracking for your Android application."
Tool:
  - Location

---

# Location tracking for Android and FireOS

Add at least one of the following permissions to your `AndroidManifest.xml` file to declare your app's intent to collect location data:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` includes GPS data in reporting user location while `ACCESS_COARSE_LOCATION` includes data from the most battery-efficient non-GPS provider available (e.g., the network). Coarse location will likely be sufficient for most location data use-cases; however, under the runtime permissions model, receiving location permission from the user implicitly authorizes the collection of fine location data. Take a look at [Location Strategies][1] from Android Developers to read more about the differences between these location permissions and how you should utilize them.

{% alert important %}
With the release of Android M, Android switched from an install-time to a runtime permissions model. To enable location tracking on devices running Android M or later, the app must explicitly receive permission to use the location from the user (Braze will not do this). Once location permissions are obtained, Braze will automatically begin tracking location on the next session start if location collection is enabled in `braze.xml`. Devices running earlier versions of Android only require location permissions to be declared in the `AndroidManifest.xml`. For more information, visit Android's [permission documentation](https://developer.android.com/training/permissions/index.html).
{% endalert %}

## Disabling automatic location tracking

To disable automatic location tracking, set `com_braze_enable_location_collection` to false in `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

Then you can manually log single location data points via the [`setLastKnownLocation()`][4] method on `BrazeUser` like this:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
```

{% endtab %}
{% endtabs %}

[1]: https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html
