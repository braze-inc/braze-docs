{% alert note %}
For optimal performance on Android 12, we recommend upgrading to [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) as soon as possible. For more information, see our [Android 12 upgrade guide]({{site.baseurl}}/android_12/).
{% endalert %}

## Step 1: Integrate the UI library (optional)

To use push notifications, in-app messaging, and Content Cards, you must integrate the Braze UI library. Although skipping this step is possible, it is not recommended.

### Step 1.2: Add Braze dependency

In your Android Studio project, add the `android-sdk-ui` dependency to your app's `build.gradle`. If you're using any location or Braze Geofence functionality, also include `android-sdk-location` in your app's `build.gradle`.

{% alert important %}
If you're using a non-native Android SDK (for example, Flutter, Cordova, Unity, etc.), that SDK already has the `android-sdk-ui` dependency for the correct version of the Android SDK. Do not update that version manually.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

The following example shows where to place the dependency line in your `build.gradle`. Note that the version used in the example uses an old version. Visit [Braze Android SDK releases](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) for the most up-to-date version of the Braze Android SDK.

![Android studio displaying the "build.gradle". In this screenshot, the dependency code is added to the bottom of the file.]({% image_buster /assets/img_archive/androidstudio2.png %})

### Step 1.2: Perform Gradle sync

Be sure to perform a Gradle sync to build your project and incorporate the [dependency additions](#add-braze-dependency).

![Android studio displaying a banner and button at the top of the application that says, "Gradle files have changed since last project sync. A project sync may be necessary for the IDE to work properly. Sync Now."]({% image_buster /assets/img_archive/androidstudio3.png %})

## Step 2: Configure the Braze SDK in braze.xml

{% alert note %}
As of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For more details, refer to our <a href="{{site.baseurl}}/api/basics/#endpoints">list of available endpoints</a>.
{% endalert %}

Next, create a `braze.xml` file in your project's `res/values` folder. If you are on a specific data cluster or have a pre-existing custom endpoint, you need to specify the endpoint in your `braze.xml` file as well. 

The contents of that file should resemble the following code snippet. Make sure to substitute `YOUR_APP_IDENTIFIER_API_KEY` with the identifier found in the **Manage Settings** page of the Braze dashboard. Log in at [dashboard.braze.com](https://dashboard.braze.com) to find your [cluster address]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Step 3: Add required permissions to AndroidManifest.xml

Next, add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
With the release of Android M, Android switched from an install-time to a runtime permissions model. However, both of these permissions are normal permissions and are granted automatically if listed in the app manifest. For more information, visit Android's [permission documentation](https://developer.android.com/training/permissions/index.html).
{% endalert %}

## Step 4: Enable user session tracking

Calls to `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html), and `InAppMessageManager` registration are optionally handled automatically.

To register activity lifecycle callbacks, add the following code to the `onCreate()` method of your `Application` class:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

{% endtab %}
{% endtabs %}

See our SDK reference documentation for more information on the parameters available for [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Step 5: Enable location tracking

To enable Braze location collection, update your `braze.xml` file to include `com_braze_enable_location_collection` and ensure its value is set to `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0, Braze location collection is disabled by default.
{% endalert %}
