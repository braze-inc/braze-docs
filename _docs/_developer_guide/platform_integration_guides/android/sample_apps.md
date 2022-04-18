---
nav_title: Sample Apps
article_title: Sample Apps for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 10
description: "This article covers Android sample apps."

---

# Sample apps

Braze's SDKs each come with a sample application within the repository for your convenience. Each of these apps is fully buildable so you can test Braze features alongside implementing them within your own applications. Testing behavior within your own application versus expected behavior and code paths within the sample applications is an excellent way to debug any problems you may run into.

## Building the Droidboy test application
Braze's test application within the [Android SDK GitHub repository][3] is called Droidboy. Follow these instructions to build a fully functional copy of it alongside your project.

1. Create a new [app group][25] and note the Braze API identifier key.<br><br>
2. Copy your FCM sender ID and Braze API identifier key into the appropriate places within `/droidboy/res/values/braze.xml` (in between the tags for the strings named `com_braze_push_fcm_sender_id` and `com_braze_api_key`, respectively).<br><br>
3. Copy your FCM server key and server ID into your app group settings under **Manage Settings**.<br><br>
4. To assemble the Droidboy APK, run `./gradlew assemble` within the SDK directory. Use `gradlew.bat` on Windows.<br><br>
5. To automatically install the Droidboy APK on a test device, run `./gradlew installDebug` within the SDK directory:

## Building the Hello Braze test application
The Hello Braze test application shows a minimal use case of the Braze SDK and additionally shows how to easily integrate the Braze SDK into a Gradle project.

1. Copy your API identifier key from the **Manage Settings** page into your `braze.xml` file in the `res/values` folder.
![][34]<br><br>
2. To install the sample app to a device or emulator, run the following command within the SDK directory:
```
./gradlew installDebug
```
If you don't have your `ANDROID_HOME` variable properly set or don't have a `local.properties` folder with a valid `sdk.dir` folder, this plugin will also install the base SDK for you. See the [plugin repo][27] for more information.

For more information on the Android SDK build system, see the [Github Repository README][26].

[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/README.md
[27]: https://github.com/JakeWharton/sdk-manager-plugin
[3]: https://github.com/appboy/appboy-android-sdk "Appboy Android GitHub Repository"
[34]: {% image_buster /assets/img_archive/hello_appboy.png %}
