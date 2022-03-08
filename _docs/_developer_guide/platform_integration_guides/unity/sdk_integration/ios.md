---
nav_title: iOS
article_title: SDK iOS Integration for Unity
platform: 
  - Unity
  - iOS
page_order: 0
description: "This reference article covers the iOS SDK integration for the Unity platform."

---

# SDK iOS integration

Follow the below instructions to get Braze running in your Unity application. If you are transitioning from a manual integration, read the instructions on [Transitioning to an automated integration][5].

## Step 1: Choose your Braze Unity package

The Braze [`.unitypackage`][41] bundles native bindings for the Android and iOS platforms, along with a C# interface.

There are several Braze Unity packages available for download on the [Braze Unity releases page][42]:
- `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs and the [SDWebImage][unity-1] dependency for the iOS SDK, which is required for the proper functionality of Braze's In-App Messaging, and Content Cards features on iOS. The SDWebImage framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
- `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage][unity-1] framework is not present. This package is useful if you do not want the SDWebImage framework present in your iOS app.

**iOS**: To see if you require the [SDWebImage][unity-1] dependency for your iOS project, visit the [iOS in-app message documentation][unity-4].<br>
**Android**: As of Unity 2.6.0, the bundled Braze Android SDK artifact requires  [AndroidX][unity-3] dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage` above.

## Step 2: Import the package

In the Unity Editor, import the package into your Unity project by navigating to **Assets > Import Package > Custom Package**. Next, click **Import**.

Alternatively, follow the [Unity asset package import][41] instructions for a more detailed guide on importing custom Unity packages. 

{% alert note %}
If you only wish to import the iOS or Android plugin, deselect the `Plugins/Android` or `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}

## Step 3: Set your API key

Braze provides a native Unity solution for automating the Unity iOS integration. This solution modifies the built Xcode project using Unity's [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) and subclasses the `UnityAppController` using the `IMPL_APP_CONTROLLER_SUBCLASS` macro.

1. In the Unity Editor, open the Braze Configuration Settings by navigating to **Braze > Braze Configuration**.
2. Check the **Automate Unity iOS Integration** box.
3. In the "Braze API Key" field, input your application's API key found in **Manage Settings**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

If your application is already using another `UnityAppController` subclass, you will need to merge your subclass implementation with `AppboyAppDelegate.mm`.

## Basic SDK integration complete

Braze should now be collecting data from your application, and your basic integration should be complete. Check out the following articles for more information on integrating push ([Android][53] and [iOS][50]), [in-app messages][34], [Content Cards][40], and [News Feed][35].

## Additional advanced implementation options

### Extending the SDK (iOS)

To extend the SDK's behaviors, fork the [Braze Unity SDK Github project](https://github.com/appboy/appboy-unity-sdk) and make your required changes.

To publish your modified code as a Unity package, see our [Advanced use cases]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Advanced_Use_Cases/advanced_use_cases).

### Transitioning from manual to automated integration (iOS)

To take advantage of the automated iOS integration offered in the Braze Unity SDK, follow these steps on transitioning from a manual to an automated integration.

1. Remove all Braze-related code from your Xcode project's `UnityAppController` subclass.
2. Remove Braze's iOS libraries from your Unity or Xcode project (i.e., `Appboy_iOS_SDK.framework` and `SDWebImage.framework`) and [import the Braze Unity package](#step-1-importing-the-braze-unity-package) into your Unity project.
3. Follow the integration instructions on [setting your API key through Unity](#step-2-setting-your-api-key).

[5]: #transitioning-from-manual-to-automated-integration-ios
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/
