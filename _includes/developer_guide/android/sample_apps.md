# Sample apps

> Braze SDKs each come with a sample application within the repository for your convenience. Each of these apps is fully buildable so you can test Braze features alongside implementing them within your own applications. 

Testing behavior within your own application versus expected behavior and code paths within the sample applications is an excellent way to debug any problems you may run into.

## Building the Droidboy test application
Our test application within the [Android SDK GitHub repository](https://github.com/braze-inc/braze-android-sdk) is called Droidboy. Follow these instructions to build a fully functional copy of it alongside your project.

1. Create a new [workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) and note the Braze API identifier key.<br><br>
2. Copy your FCM sender ID and Braze API identifier key into the appropriate places within `/droidboy/res/values/braze.xml` (in between the tags for the strings named `com_braze_push_fcm_sender_id` and `com_braze_api_key`, respectively).<br><br>
3. Copy your FCM server key and server ID into your workspace settings under **Manage Settings**.<br><br>
4. To assemble the Droidboy APK, run `./gradlew assemble` within the SDK directory. Use `gradlew.bat` on Windows.<br><br>
5. To automatically install the Droidboy APK on a test device, run `./gradlew installDebug` within the SDK directory:

## Building the Hello Braze test application
The Hello Braze test application shows a minimal use case of the Braze SDK and additionally shows how to easily integrate the Braze SDK into a Gradle project.

1. Copy your API identifier key from the **Manage Settings** page into your `braze.xml` file in the `res/values` folder.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. To install the sample app to a device or emulator, run the following command within the SDK directory:
```
./gradlew installDebug
```
If you don't have your `ANDROID_HOME` variable properly set or don't have a `local.properties` folder with a valid `sdk.dir` folder, this plugin will also install the base SDK for you. See the [plugin repository](https://github.com/JakeWharton/sdk-manager-plugin) for more information.

For more information on the Android SDK build system, see the [GitHub Repository README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).

