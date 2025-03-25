## Logging the current location

Even if continuous tracking is disabled, you can manually log the user's current location using the [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) method.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

## Continuously tracking the location

{% alert important %}
[Starting with Android Marshmallow](https://developer.android.com/training/permissions/index.html), you must prompt your users to explicitly opt-in to location tracking. Once they do, Braze can start tracking their location at the beginning of the next session. This is unlike earlier versions of Android, where only declaring location permissions in your `AndroidManifest.xml` was required.
{% endalert %}

To continuously track a user's location, you'll need to declare your app's intent to collect location data by adding at least one of the following permissions to your `AndroidManifest.xml` file.

|Permission|Description|
|---|---|
| `ACCESS_COARSE_LOCATION` | Uses the most battery-efficient, non-GPS provider (such as a home network). Typically, this is sufficient for most location-data needs. Under the runtime permissions model, granting location permission implicitly authorizes the collection of fine location data. |
| `ACCESS_FINE_LOCATION`   | Includes GPS data for more precise location. Under the runtime permissions model, granting location permission also covers fine location access. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Your `AndroidManifest.xml` should be similar to the following:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Disabling continuous tracking

You can disable continuous tracking at compile time or runtime.

{% tabs local %}
{% tab compile time %}

To disable continuous location tracking at compile time, set `com_braze_enable_location_collection` to `false` in `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

To selectively disable continuous location tracking at runtime, use [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
