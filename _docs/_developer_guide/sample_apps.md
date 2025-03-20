---
nav_title: Sample Apps
article_title: Sample apps for the Braze SDK
platform: 
  - Android
  - FireOS
  - Swift
page_order: 98.0
description: "This reference article covers how to use Android sample apps."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
toc_headers: h2
---

# Sample apps for the Braze SDK

> Each Braze SDK repository includes fully-buildable sample applications you can use to test Braze features or implement alongside your own applications.

## List of sample apps

| Platform          | Repository                                                                 |
| ----------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [GitHub repository](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [GitHub repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [GitHub repository](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [GitHub repository](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [GitHub repository](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [GitHub repository](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | [GitHub repository](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [GitHub repository](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| Unreal Engine SDK | [GitHub repository](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| Xamarin SDK       | [GitHub repository](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Building a sample app

{% alert note %}
At this time, not all SDK sample apps are documented. However, we plan to add more overtime.
{% endalert %}

{% tabs %}
{% tab android %}
### Building "Droidboy"

Our test application within the [Android SDK GitHub repository](https://github.com/braze-inc/braze-android-sdk "Braze Android GitHub Repository") is called Droidboy. Follow these instructions to build a fully functional copy of it alongside your project.

1. Create a new [workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) and note the Braze API identifier key.<br><br>
2. Copy your FCM sender ID and Braze API identifier key into the appropriate places within `/droidboy/res/values/braze.xml` (in between the tags for the strings named `com_braze_push_fcm_sender_id` and `com_braze_api_key`, respectively).<br><br>
3. Copy your FCM server key and server ID into your workspace settings under **Manage Settings**.<br><br>
4. To assemble the Droidboy APK, run `./gradlew assemble` within the SDK directory. Use `gradlew.bat` on Windows.<br><br>
5. To automatically install the Droidboy APK on a test device, run `./gradlew installDebug` within the SDK directory:

### Building "Hello Braze"

The Hello Braze test application shows a minimal use case of the Braze SDK and additionally shows how to easily integrate the Braze SDK into a Gradle project.

1. Copy your API identifier key from the **Manage Settings** page into your `braze.xml` file in the `res/values` folder.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. To install the sample app to a device or emulator, run the following command within the SDK directory:
```
./gradlew installDebug
```
If you don't have your `ANDROID_HOME` variable properly set or don't have a `local.properties` folder with a valid `sdk.dir` folder, this plugin will also install the base SDK for you. See the [plugin repository](https://github.com/JakeWharton/sdk-manager-plugin) for more information.

For more information on the Android SDK build system, see the [GitHub Repository README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Building Swift test apps

Follow these instructions to build and run our test applications.

1. Create a new [workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) and note the app identifier API key and endpoint.
2. Based on your integration method (Swift Package Manager, CocoaPods, Manual), select the appropriate `xcodeproj` file to open.
3. Place your API key and your endpoint within the appropriate field in the `Credentials` file.
{% endtab %}
{% endtabs %}
