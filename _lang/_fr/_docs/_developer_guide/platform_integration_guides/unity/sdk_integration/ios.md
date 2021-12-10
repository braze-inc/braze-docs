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

Follow the below instructions to get Braze running in your Unity application. If you are transitioning from a manual integration, please read the instructions on [Transitioning From a Manual to an Automated Integration][5].

## Step 1: Choose your Braze Unity package

The Braze [`.unitypackage`][41] bundles native bindings for the Android and iOS platforms, along with a C# interface.

There are several Braze Unity packages available for download at [Braze Unity Releases Page][42]:

* `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs as well as the [SDWebImage][unity-1] dependency for the iOS SDK, which is required for proper functionality of Braze's In-App Messaging, and Content Cards features on iOS. The [SDWebImage][unity-1] framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.<br>
* `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage][unity-1] framework not being present. This package is useful if you do not want the [SDWebImage][unity-1] framework present in your iOS app. <br><br>

> iOS: To see if you require the [SDWebImage][unity-1] dependency for your iOS project, please visit the \[iOS In-App Message Documentation\]\[unity-4\].<br><br>Android: As of Unity 2.6.0, the bundled Braze Android SDK artifact requires  [AndroidX][unity-3] dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage` above.

## Step 2: Import the package

1. In the Unity Editor, import the package into your Unity project by navigating to `Assets > Import Package > Custom Package`.
2. Click __Import__.

Alternatively, follow the Unity instructions for [Importing Asset packages][41] for a more detailed guide on importing custom Unity packages.

{% alert note %}
If you only wish to import the iOS/Android plugin, deselect the `Plugins/Android`/`Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}

## Step 3b: Set your API key

Braze provides a native Unity solution for automating the Unity iOS integration. This solution modifies the built Xcode project using Unity's [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)) and subclasses the UnityAppController using the `IMPL_APP_CONTROLLER_SUBCLASS` macro.

1. In the Unity Editor, open the Braze Configuration Settings by navigating to Braze > Braze Configuration.
2. Check the "Automate Unity iOS Integration" box.
3. In the "Braze API Key" field, input your application's API key from the [Settings](https://dashboard-01.braze.com/app_settings/app_settings) page in the Braze dashboard. Your Braze Configuration settings should look like this:

![Braze Config Editor]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

> If your application is already using another `UnityAppController` subclass, you will need to merge your subclass implementation with `AppboyAppDelegate.mm`.

## Basic SDK integration complete

Braze should now be collecting data from your application and your basic integration should be complete.

- __Push__: See the [Android][53] or [iOS][50] push documentation for information on integrating push.
- __In-App Messages__: See the [In-App Message documentation][34] for information on integrating in-app messages.
- __Content Cards__: See the [Content Cards documentation][40] for information on integrating Content Cards.
- __News Feed__: See the [News Feed documentation][35] for information on integrating the News Feed.

## Extending the SDK (iOS)

To extend the SDK's behaviors, fork our [Braze Unity SDK Github project](https://github.com/appboy/appboy-unity-sdk) and make your required changes.

To publish your modified code as a Unity package, see [Advanced Use Cases]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Advanced_Use_Cases/advanced_use_cases).

## Transitioning from manual to automated integration (iOS)

To take advantage of the automated iOS integration offered in the Braze Unity SDK, follow these steps on transitioning from a manual to an automated integration.

1. Remove all Braze-related code from your Xcode project's `UnityAppController` subclass.
2. Remove Braze's iOS libraries from your Unity or Xcode project (i.e., `Appboy_iOS_SDK.framework` and `SDWebImage.framework`) and [import the Braze Unity package](#step-1-importing-the-braze-unity-package) into your Unity project.
3. Follow the integration instructions on [setting your API key through Unity](#step-2-setting-your-api-key).
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-3]: https://developer.android.com/jetpack/androidx