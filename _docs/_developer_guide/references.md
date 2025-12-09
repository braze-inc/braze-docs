---
nav_title: References & sample apps
article_title: Braze SDK references, repositories, and sample apps
page_order: 5.5
description: "This is a list of reference documentation, GitHub repositories, and sample apps belonging to each Braze SDK."
toc_headers: h2
---

# References, repositories, and sample apps

> This is a list of reference documentation, GitHub repositories, and sample apps belonging to each Braze SDK. An SDK's reference documentation details its available classes, types, functions, and variables. While the GitHub repository provides insight into that SDK's function and attribute declarations, code changes, and versioning. Each repository also includes fully-buildable sample applications you can use to test Braze features or implement alongside your own applications.

## List of resources

{% alert note %}
Currently, some SDKs do not have dedicated reference documentation&#8212;but we're actively working on it.
{% endalert %}

| Platform          | Reference                                                                                                                                    | Repository                                                                 | Sample app                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [Reference documentation](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHub repository](https://github.com/braze-inc/braze-android-sdk)      | [Sample app](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [Reference documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHub repository](https://github.com/braze-inc/braze-swift-sdk)            | [Sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [Reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHub repository](https://github.com/braze-inc/braze-web-sdk)              | [Sample app](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [Declaration File](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHub repository](https://github.com/braze-inc/braze-cordova-sdk)      | [Sample app](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [Reference documentation](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHub repository](https://github.com/braze-inc/braze-flutter-sdk)      | [Sample app](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Declaration File](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [GitHub repository](https://github.com/braze-inc/braze-react-native-sdk) | [Sample app](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | N/A                                                                                                                                                         | [GitHub repository](https://github.com/braze-inc/braze-roku-sdk)            | [Sample app](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [Declaration file](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHub repository](https://github.com/braze-inc/braze-unity-sdk)          | [Sample app](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| Unreal Engine SDK | N/A                                                                                                                                                         | [GitHub repository](https://github.com/braze-inc/braze-unreal-sdk)        | [Sample app](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK (formerly Xamarin)      | N/A                                                                                                                                                         | [GitHub repository](https://github.com/braze-inc/braze-xamarin-sdk)      | [Sample app](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Building a sample app

{% tabs %}
{% tab android %}
### Building "Droidboy"

Our test application within the [Android SDK GitHub repository](https://github.com/braze-inc/braze-android-sdk) is called Droidboy. Follow these instructions to build a fully functional copy of it alongside your project.

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

{% alert note %}
While performing QA on your SDK integration, use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to get troubleshoot issues without turning on verbose logging for your app.
{% endalert %}
