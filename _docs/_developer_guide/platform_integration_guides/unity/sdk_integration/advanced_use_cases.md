---
nav_title: Advanced Implementation
article_title: Advanced SDK Implementation
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "This reference article covers advanced SDK implementation for the Unity platform."
---

# Advanced implementation

> This reference article covers advanced SDK implementation for the Unity platform.

## Customizing the Unity package

You can choose to customize and export the Braze Unity package using the provided scripts.

1. Clone the [Braze Unity SDK GitHub project](https://github.com/appboy/appboy-unity-sdk):

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. From the `braze-unity-sdk/scripts` directory, run `./generate_package.sh` to export the Unity packages. Unity should be open while running `generate_package.sh`.
3. The packages will be exported to `braze-unity-sdk/unity-package/`.
4. In the Unity Editor, import the desired package into your Unity project by navigating to **Assets** > **Import Package** > **Custom Package**.
5. (optional) Deselect any files you do not wish to import.

You can customize the exported Unity package by editing both `generate_package.sh` and the export script located at `Assets/Editor/Build.cs`.

## Prime 31 compatibility

To use the Braze Unity plugin with Prime31 plugins, edit your project's `AndroidManifest.xml` to use the Prime31 compatible Activity classes. Change all references of
`com.braze.unity.BrazeUnityPlayerActivity` to `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Amazon ADM push

Braze supports integrating [Amazon ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) into Unity apps. If you want to integrate Amazon ADM push, create a file called `api_key.txt` containing your ADM API key and place it in the `Plugins/Android/assets/` folder.  For more information on integrating Amazon ADM with Braze, visit our [ADM push integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Android SDK advanced implementation options {#android-sdk-advanced}

### Enabling verbose logging in the Unity editor
To enable verbose logging in the Unity Editor, do the following:

1. Open the Braze Configuration Settings by navigating to **Braze** > **Braze Configuration**.
2. Click the **Show Braze Android Settings** dropdown.
3. In the **SDK Log Level** field, input the value "0".

### Extending Braze Unity player (Android) {#extending-braze-unity-player}

The example `AndroidManifest.xml` file provided has one Activity class registered, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). This class is integrated with the Braze SDK and extends `UnityPlayerActivity` with session handling, in-app message registration, push notification analytics logging, and more. See [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) for more information on extending the `UnityPlayerActivity` class.

If you are creating your own custom `UnityPlayerActivity` in a library or plugin project, you will need to extend our `BrazeUnityPlayerActivity` to integrate your custom functionality with Braze. Before beginning work on extending `BrazeUnityPlayerActivity`, follow our instructions for integrating Braze into your Unity project.
1. Add the Braze Android SDK as a dependency to your library or plugin project as described in the [Braze Android SDK integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Integrate our Unity `.aar`, which contains our Unity-specific functionality, to your Android library project you are building for Unity. The `appboy-unity.aar` is available from our [public repo](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). After our Unity library is successfully integrated, modify your `UnityPlayerActivity` to extend `BrazeUnityPlayerActivity`.
3. Export your library or plugin project and drop it into `/<your-project>/Assets/Plugins/Android` as normal. Do not include any Braze source code in your library or plugin as they will already be present in `/<your-project>/Assets/Plugins/Android`.
4. Edit your `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` to specify your `BrazeUnityPlayerActivity` subclass as the main activity.

You should now be able to package an `.apk` from the Unity IDE that is fully integrated with Braze and contains your custom `UnityPlayerActivity` functionality.

## iOS SDK advanced implementation options {#ios-sdk-advanced}

### Enabling verbose logging in the Unity editor
To enable verbose logging in the Unity Editor, do the following:

1. Open the Braze Configuration Settings by navigating to **Braze** > **Braze Configuration**.
2. Click the **Show Braze iOS Settings** dropdown.
3. In the **SDK Log Level** field, input the value "0".

### Extending the SDK (iOS)

To extend the SDK's behaviors, fork the [Braze Unity SDK GitHub project](https://github.com/appboy/appboy-unity-sdk) and make your required changes.

To publish your modified code as a Unity package, see our [Advanced use cases]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/).

### Transitioning from manual to automated integration (iOS)

To take advantage of the automated iOS integration offered in the Braze Unity SDK, follow these steps on transitioning from a manual to an automated integration.

1. Remove all Braze-related code from your Xcode project's `UnityAppController` subclass.
2. Remove Braze iOS libraries from your Unity or Xcode project (such as `Appboy_iOS_SDK.framework` and `SDWebImage.framework`) and [import the Braze Unity package](#step-1-importing-the-braze-unity-package) into your Unity project.
3. Follow the integration instructions on [setting your API key through Unity](#step-2-setting-your-api-key).

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
