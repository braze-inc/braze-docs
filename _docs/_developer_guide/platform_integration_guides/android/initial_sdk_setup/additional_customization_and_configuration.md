---
nav_title: Additional Customization & Configuration
page_order: 3
search_rank: 5
platform: Android
---

# Additional Customization and Configuration

## Using Proguard with Braze
[Proguard][50] configuration is automatically included with your Braze integration.

Client apps that Proguard Braze code must store release mapping files for Braze to interpret stack traces. If you would like to continue to keep all Braze code, add the following to your Proguard configuration:

```
-keep class bo.app.** { *; }
-keep class com.appboy.** { *; }
```

If you are integrating Baidu Cloud Push with Braze, add:

```
-dontwarn com.baidu.**
-keep class com.baidu.** { *; }
```

## Braze Log Level

The default Log Level for the Braze Android SDK is `INFO`. This level includes push payload logs and basic Braze server communication logs.

To change the Braze Log Level, call `AppboyLogger.setLogLevel()` with one of the [`android.util.Log`][54] priority constants or `AppboyLogger.SUPPRESS`. For example:

{% tabs %}
{% tab JAVA %}

```java
// Change log level to VERBOSE
AppboyLogger.setLogLevel(Log.VERBOSE);

// Suppress logs
AppboyLogger.setLogLevel(AppboyLogger.SUPPRESS);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Change log level to VERBOSE
AppboyLogger.setLogLevel(Log.VERBOSE)

// Suppress logs
AppboyLogger.setLogLevel(AppboyLogger.SUPPRESS)
```

{% endtab %}
{% endtabs %}

### Verbose Logging

When debugging Braze behavior, set the Log level to `Verbose` before your first call to Braze, preferably in your `Application.onCreate()`. This Log level contains every log made by the Braze SDK. This is only intended to be used in development environments and should not be set in a released application.

>  If the Braze API Key from the "App Settings" page is not present in `appboy.xml` then an error message is logged to the Android logcat.

>  If required permissions `ACCESS_NETWORK_STATE` and `INTERNET` are not declared in the manifest, an error message is logged to the Android logcat.

## Multiple API Keys

The most common usecase for multiple API keys is separating API keys for debug and release build variants.

To easily switch between multiple API keys in your builds, we recommend creating a separate `appboy.xml` file for each relevant [build variant][3]. A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types][8] and no product flavors.

For each relevant build variant, create a new `appboy.xml` for it in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

When the build variant is compiled, it will use the new API key.

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/news_feed/#news-feed-customization
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
[22]: {% image_buster /assets/img_archive/click_properties.png %}
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
[58]: {% image_buster /assets/img_archive/activity_lifecycle_callback_integration.png %}
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
