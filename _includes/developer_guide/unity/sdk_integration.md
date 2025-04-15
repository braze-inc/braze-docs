## About the Unity Braze SDK

For a full list of types, functions, variables, and more, see [Unity Declaration File](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). Additionally, if you've already integrated Unity manually for iOS, you can [switch to an automated integration](#unity_automated-integration) instead.

## Integrating the Unity SDK

### Prerequisites

Before you start, verify your environment is supported by the [latest Braze Unity SDK version](https://github.com/braze-inc/braze-unity-sdk/releases).

### Step 1: Choose your Braze Unity package

{% tabs %}
{% tab Android %}
The Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bundles native bindings for the Android and iOS platforms, along with a C# interface.

There are several Braze Unity packages available for download on the [Braze Unity releases page](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs and the [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependency for the iOS SDK, which is required for the proper functionality of Braze in-app messaging, and Content Cards features on iOS. The SDWebImage framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
- `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage](https://github.com/SDWebImage/SDWebImage) framework is not present. This package is useful if you do not want the SDWebImage framework present in your iOS app.

{% alert note %}
As of Unity 2.6.0, the bundled Braze Android SDK artifact requires  [AndroidX](https://developer.android.com/jetpack/androidx) dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage`.
{% endalert %}
{% endtab %}

{% tab Swift %}
The Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bundles native bindings for the Android and iOS platforms, along with a C# interface.

The Braze Unity package is available for download on the [Braze Unity releases page](https://github.com/Appboy/appboy-unity-sdk/releases) with two integration options:

1. `Appboy.unitypackage` only
  - This package bundles the Braze Android and iOS SDKs without any additional dependencies. With this integration method, there will not be proper functionality of Braze in-app messaging, and Content Cards features on iOS. If you intend on utilizing full Braze functionality without custom code, use the option below instead.
  - To use this integration option, ensure that the box next to `Import SDWebImage dependency` is *unchecked* in the Unity UI under "Braze Configuration".
2. `Appboy.unitypackage` with `SDWebImage`
  - This integration option bundles the Braze Android and iOS SDKs and the [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependency for the iOS SDK, which is required for the proper functionality of Braze in-app messaging, and Content Cards features on iOS. The `SDWebImage` framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
  - To automatically import `SDWebImage`, be sure to *check* the box next to `Import SDWebImage dependency` in the Unity UI under "Braze Configuration".

{% alert note %}
To see if you require the [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependency for your iOS project, visit the [iOS in-app message documentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Step 2: Import the package

{% tabs %}
{% tab Android %}
In the Unity Editor, import the package into your Unity project by navigating to **Assets > Import Package > Custom Package**. Next, click **Import**.

Alternatively, follow the [Unity asset package import](https://docs.unity3d.com/Manual/AssetPackages.html) instructions for a more detailed guide on importing custom Unity packages. 

{% alert note %}
If you only wish to import the iOS or Android plugin, deselect the `Plugins/Android` or `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}
{% endtab %}

{% tab Swift %}
In the Unity Editor, import the package into your Unity project by navigating to **Assets > Import Package > Custom Package**. Next, click **Import**.

Alternatively, follow the [Unity asset package import](https://docs.unity3d.com/Manual/AssetPackages.html) instructions for a more detailed guide on importing custom Unity packages. 

{% alert note %}
If you only wish to import the iOS or Android plugin, deselect the `Plugins/Android` or `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}
{% endtab %}
{% endtabs %}

### Step 3: Configure the SDK

{% tabs %}
{% tab Android %}
#### Step 3.1: Configure `AndroidManifest.xml`

To fullo [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) to function. If your app does not have an `AndroidManifest.xml`, you can use the following as a template. Otherwise, if you already have an `AndroidManifest.xml`, ensure that any of the following missing sections are added to your existing `AndroidManifest.xml`.

1. Go to the `Assets/Plugins/Android/` directory and open your `AndroidManifest.xml` file. This is the [default location in the Unity editor](https://docs.unity3d.com/Manual/android-manifest.html).
2. In your `AndroidManifest.xml`, add the required permissions and activities from in the following template.
3. When you're finished, your `AndroidManifest.xml` should only contain a single Activity with `"android.intent.category.LAUNCHER"` present.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
All Activity classes registered in your `AndroidManifest.xml` file should be fully integrated with the Braze Android SDK, otherwise your analytics won't be collected. If you add your own Activity class, be sure you [extend the Braze Unity player](#unity_extend-unity-player) so you can prevent this.
{% endalert %}

#### Step 3.2: Update `AndroidManifest.xml` with your package name

To find your package name, click **File > Build Settings > Player Settings > Android Tab**.

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

In your `AndroidManifest.xml`, all instances of `REPLACE_WITH_YOUR_PACKAGE_NAME` should be replaced with your `Package Name` from the previous step.

#### Step 3.3: Add gradle dependencies

To add gradle dependencies to your Unity project, first enable ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) in your Publishing Settings. This will create a template gradle file that your project will use. A gradle file handles setting dependencies and other build-time project settings. For more information, check out the Braze Unity sample app's [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

The following dependencies are required:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

You may also set these dependencies using the [External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver).

#### Step 3.4: Automate the Unity Android integration

Braze provides a native Unity solution for automating the Unity Android integration. 

1. In the Unity Editor, open the Braze Configuration Settings by navigating to **Braze > Braze Configuration**.
2. Check the **Automate Unity Android Integration** box.
3. In the **Braze API Key** field, input your application's API key found in **Manage Settings** from the Braze dashboard.

{% alert note %}
This automatic integration should not be used with a manually created `braze.xml` file since the configuration values may conflict during project building. If you require a manual `braze.xml`, disable the automatic integration.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Step 3.1: Set your API key

Braze provides a native Unity solution for automating the Unity iOS integration. This solution modifies the built Xcode project using Unity's [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) and subclasses the `UnityAppController` using the `IMPL_APP_CONTROLLER_SUBCLASS` macro.

1. In the Unity Editor, open the Braze Configuration Settings by navigating to **Braze > Braze Configuration**.
2. Check the **Automate Unity iOS Integration** box.
3. In the **Braze API Key** field, input your application's API key found in **Manage Settings**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

If your application is already using another `UnityAppController` subclass, you will need to merge your subclass implementation with `AppboyAppDelegate.mm`.
{% endtab %}
{% endtabs %}

## Customizing the Unity package

### Step 1: Clone the repository

In your terminal, clone the [Braze Unity SDK GitHub repository](https://github.com/braze-inc/braze-unity-sdk), then navigate to that folder:

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Step 2: Export package from repository

First, launch Unity and keep it running in the background. Then, in the repository root, run the following command to export the package to `braze-unity-sdk/unity-package/`.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit	
```
{% endtab %}
{% endtabs %}

{% alert tip %}
If you experience any issues after running these commands, refer to [Unity: Command Line Arguments](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Step 3: Import package into Unity

1. In Unity, import the desired package into your Unity project by navigating to **Assets** > **Import Package** > **Custom Package**.
2. If there's any files you don't want want to import, deselect them now.
3. Customize the exported Unity package located in `Assets/Editor/Build.cs`.

## Switch to an automated integration (Swift only) {#automated-integration}

To take advantage of the automated iOS integration offered in the Braze Unity SDK, follow these steps on transitioning from a manual to an automated integration.

1. Remove all Braze-related code from your Xcode project's `UnityAppController` subclass.
2. Remove Braze iOS libraries from your Unity or Xcode project (such as `Appboy_iOS_SDK.framework` and `SDWebImage.framework`).
3. Import the Braze Unity package into your project again. For a full walkthrough, see [Step 2: Import the package](#unity_step-2-import-the-package).
4. Set your API key again. For a full walkthrough, see [Step 3.1: Set your API key](#unity_step-31-set-your-api-key).

## Optional configurations

### Verbose logging

To enable verbose logging in the Unity Editor, do the following:

1. Open the Braze Configuration Settings by navigating to **Braze** > **Braze Configuration**.
2. Click the **Show Braze Android Settings** dropdown.
3. In the **SDK Log Level** field, input the value "0".

### Prime 31 compatibility

To use the Braze Unity plugin with Prime31 plugins, edit your project's `AndroidManifest.xml` to use the Prime31 compatible Activity classes. Change all references of
`com.braze.unity.BrazeUnityPlayerActivity` to `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Amazon Device Messaging (ADM)

Braze supports integrating [ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) into Unity apps. If you want to integrate ADM push, create a file called `api_key.txt` containing your ADM API key and place it in the `Plugins/Android/assets/` folder.  For more information on integrating ADM with Braze, visit our [ADM push integration instructions]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity).

### Extending the Braze Unity player (Android only) {#extend-unity-player}

The example `AndroidManifest.xml` file provided has one Activity class registered, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). This class is integrated with the Braze SDK and extends `UnityPlayerActivity` with session handling, in-app message registration, push notification analytics logging, and more. See [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) for more information on extending the `UnityPlayerActivity` class.

If you are creating your own custom `UnityPlayerActivity` in a library or plugin project, you will need to extend our `BrazeUnityPlayerActivity` to integrate your custom functionality with Braze. Before beginning work on extending `BrazeUnityPlayerActivity`, follow our instructions for integrating Braze into your Unity project.

1. Add the Braze Android SDK as a dependency to your library or plugin project as described in the [Braze Android SDK integration instructions]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
2. Integrate our Unity `.aar`, which contains our Unity-specific functionality, to your Android library project you are building for Unity. The `appboy-unity.aar` is available from our [public repo](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). After our Unity library is successfully integrated, modify your `UnityPlayerActivity` to extend `BrazeUnityPlayerActivity`.
3. Export your library or plugin project and drop it into `/<your-project>/Assets/Plugins/Android` as normal. Do not include any Braze source code in your library or plugin as they will already be present in `/<your-project>/Assets/Plugins/Android`.
4. Edit your `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` to specify your `BrazeUnityPlayerActivity` subclass as the main activity.

You should now be able to package an `.apk` from the Unity IDE that is fully integrated with Braze and contains your custom `UnityPlayerActivity` functionality.

## Troubleshooting

### Error: "File could not be read"

Errors resembling the following may be safely ignored. Apple software uses a proprietary PNG extension called CgBI, which Unity does not recognize. These errors will not affect your iOS build or the proper display of the associated images in the Braze bundle.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
