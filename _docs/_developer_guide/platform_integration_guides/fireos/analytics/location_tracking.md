---
nav_title: Location Tracking
platform: FireOS
page_order: 6
search_rank: 4
---
## Location Tracking

Add at least one of the following the following permission to your `AndroidManifest.xml` file to declare your app's intent to collect location data:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
Or:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

{% alert important %}
With the release of Android M, Android switched from an install-time to a runtime permissions model. To enable location tracking on devices running M and above, the app must explicitly receive permission to use location from the user (Braze will not do this). Once location permissions are obtained, Braze will automatically begin tracking location on the next session start, if location collection is enabled in `appboy.xml`. Devices running earlier versions of Android only require location permissions to be declared in the `AndroidManifest.xml`. For more information, visit Android's [permission documentation](https://developer.android.com/training/permissions/index.html).
{% endalert %}

`ACCESS_FINE_LOCATION` includes GPS data in reporting user location while `ACCESS_COARSE_LOCATION` includes data from the most battery-efficient non-GPS provider available (e.g. the network). Coarse location location will likely be sufficient for the majority of location data use-cases; however, under the runtime permissions model, receiving location permission from the user implicitly authorizes the collection of fine location data. You can read more about the differences between these location permissions and how you ought to utilize them [here][1].

### Disabling Automatic Location Tracking

To disable automatic location tracking, set `com_appboy_enable_location_collection` to false in `appboy.xml`:

```xml
<bool name="com_appboy_enable_location_collection">false</bool>
```

Then you can manually log single location data points via the setLastKnownLocation() method on `AppboyUser` like this:

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
```

See [here][3] for an implementation example of the above in our Droidboy sample app and [here in our Javadocs][4] for more information on the `setLastKnownLocation` method.

[1]: http://developer.android.com/guide/topics/location/strategies.html
[3]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/PreferencesActivity.java#L146
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/AppboyUser.html#setLastKnownLocation-double-double-java.lang.Double-java.lang.Double-
