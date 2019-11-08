---
nav_title: Android SDK Integration
page_order: 0
search_rank: 5
platform: Android
---
# Initial SDK Setup

Installing the Braze SDK will provide you with basic analytics functionality as well as working in-app messages with which you can engage your users.

## Android SDK Integration

### Step 1: Integrate the Braze Library
The Braze Android SDK can optionally be integrated without UI components. However, Content Cards, News Feed, and In-App Messaging will be rendered inoperable unless you pass the custom data to a UI solely of your design. Additionally, push notifications will not work because our push handling code is in the UI library. Please note that these UI elements are open source and [fully customizable][1]. We strongly recommend integration of these features. Please refer to [Braze Docs][2] for the benefits of using the Braze Content Cards, News Feed, and In-App Message UI.

#### Basic Integration
In order to access Braze's messaging features, you must integrate the UI library. Please see the following directions to integrate the UI library depending on your IDE:

#### Using Android Studio

##### Add Our Repository

In your top-level project `build.gradle`, add the following as repositories under `allprojects` -> `repositories`.

For example:

```gradle
allprojects {
  repositories {
    google()
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

Alternatively, you may install the `android-sdk-ui` as an AAR file to your local maven repository. See the [SDK Readme][37] for details.

> See the [Android Support Library Setup instructions][65] for more information on the google maven repository.

##### Add Braze Dependency

Add the `android-sdk-ui` dependency to your app's `build.gradle`. For example:

```gradle
dependencies {
  implementation "com.appboy:android-sdk-ui:+"
}
```

The below example shows where to place the dependency line in your `build.gradle`. Note that the version used in the example below uses an old version. Please visit [Braze Android SDK Releases][60] for the most up to date version of the Braze Android SDK.

![MavenScreen2][32]

##### Perform Gradle Sync

Be sure to perform a Gradle Sync to build your project and incorporate the dependency additions noted above.

![GradleSync][38]

### Step 2: Configure the Braze SDK in appboy.xml
Now that the libraries have been integrated, you have to create an `appboy.xml` file in your project's `res/values` folder. If you have a custom endpoint or are on a [specific data cluster][66], you need specify the [endpoint][67] in your `appboy.xml` file as well. The contents of that file should resemble the following code snippet:

>  Be sure to substitute the API key found within the App Settings page of the Braze dashboard for `REPLACE_WITH_YOUR_API_KEY`. To find out your specific cluster or custom endpoint, please ask your Customer Success Manager or [open a support ticket][68].

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_API_KEY</string>
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

**Implementation Example**

See the [`appboy.xml`][6] in the Droidboy sample app for an implementation example.

### Step 3: Add Required Permissions to Android Manifest
Now that you've added your API key, you need to add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

>  With the release of Android M, Android switched from an install-time to a runtime permissions model. However, both of these permissions are normal permissions and are granted automatically if listed in the app manifest. For more information, visit Android's [permission documentation][46].

**Implementation Example**

See the [`AndroidManifest.xml`][69] in the Droidboy sample app for an implementation example.

### Step 4: Tracking User Sessions in Android

#### Activity Lifecycle Callback Integration (API 14+)

Calls to `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`][64], and `InAppMessageManager` registration are optionally handled automatically. See the [HelloBraze sample application][62] for a full example.

##### Instructions
Add the following code to the `onCreate()` method of your Application class:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new AppboyLifecycleCallbackListener(sessionHandlingEnabled, inAppMessagingRegistrationEnabled));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(AppboyLifecycleCallbackListener(sessionHandlingEnabled, inAppMessagingRegistrationEnabled))
  }
}
```

{% endtab %}
{% endtabs %}

The first argument instructs the listener to handle `openSession()` and `closeSession()` calls.
The second argument instructs the listener to handle `registerInAppMessageManager()` and `unregisterInAppMessageManager()` calls.

See the [javadoc][63] for more information. Please note that any non-standard manual session integration is not fully supported.

### Step 5: Custom Endpoint Setup {#step-5-optional-custom-endpoint-setup}

Your Braze representative should have already advised you of the [correct endpoint]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

To update the default endpoint in your integration of the Braze SDKs please add the following code to your `appboy.xml`:

```xml
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
```

The SDK Endpoint configuration via `appboy.xml` is available starting with __Braze Android SDK v2.1.1__.

### Step 6: Enable Location Tracking

If you would like to enable Braze location collection, update your `appboy.xml` file to include `com_appboy_enable_location_collection` and ensure its value is set to true.

```xml
<bool name="com_appboy_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0 Braze location collection is disabled by default.
{% endalert %}

### SDK Integration Complete

Braze will now be able to collect [specified data from your application]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/overview/) and your basic integration should be complete.

Please see the following sections in order to enable [custom event tracking]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events), [push messaging]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/), the [news feed]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/news_feed/overview/) and the [complete suite]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) of Braze features.

{% alert important %}
Our Unity SDK integration for Android requires [the same support library version as the base Android SDK](https://github.com/Appboy/appboy-android-sdk#version-support).
{% endalert %}

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/news_feed/customization/#news-feed-customization
[2]: {{ site.baseurl }}/user_guide/introduction/
[3]: https://developer.android.com/studio/build/build-variants.html
[4]: https://raw.github.com/appboy/appboy-android-sdk/master/android-sdk-ui/libs/appboy.jar
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values/appboy.xml
[7]: http://developer.android.com/reference/android/app/Activity.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[16]: {% image_buster /assets/img_archive/file_import.png %}
[17]: {% image_buster /assets/img_archive/android_import.png %}
[18]: {% image_buster /assets/img_archive/click_browse.png %}
[19]: {% image_buster /assets/img_archive/select_project_android.png %}
[20]: {% image_buster /assets/img_archive/import_android_ui.png %}
[21]: {% image_buster /assets/img_archive/reference_project.png %}
[22]: {% image_buster /assets/img_archive/click_properties.png %}
[23]: {% image_buster /assets/img_archive/NewBuildPath.png %}
[32]: {% image_buster /assets/img_archive/androidstudio2.png %}
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/README.md
[38]: {% image_buster /assets/img_archive/androidstudio3.png %}
[42]: https://developers.google.com/android/guides/setup
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/hello-appboy/build.gradle#L4
[46]: https://developer.android.com/training/permissions/index.html
[47]: https://android.googlesource.com/platform/sdk/+/master/files/proguard-android.txt
[50]: https://developer.android.com/tools/help/proguard.html
[51]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[52]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#step-4-tracking-user-sessions-in-android
[53]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[54]: https://developer.android.com/reference/android/util/Log.html
[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#error-logging
[57]: {% image_buster /assets/img_archive/android_device_data.png %}
[59]: https://github.com/Appboy/appboy-android-sdk
[60]: https://github.com/Appboy/appboy-android-sdk/releases
[61]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[62]: https://github.com/Appboy/appboy-android-sdk/blob/master/hello-appboy/src/main/java/com/appboy/helloworld/HelloAppboyApplication.java
[63]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/AppboyLifecycleCallbackListener.html#AppboyLifecycleCallbackListener-boolean-boolean-
[64]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[65]: https://developer.android.com/topic/libraries/support-library/setup.html#add-library
[66]: {{ site.baseurl }}/developer_guide/eu01_us3_sdk_implementation_differences/overview/
[67]: {{ site.baseurl }}/developer_guide/eu01_us3_sdk_implementation_differences/overview/#sdk-implementation
[68]: {{ site.baseurl }}/support_contact/
[69]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/AndroidManifest.xml
