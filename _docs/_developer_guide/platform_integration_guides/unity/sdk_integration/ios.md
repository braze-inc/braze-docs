---
nav_title: iOS
article_title: SDK iOS Integration for Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "This reference article covers the iOS SDK integration for the Unity platform."
search_rank: .9
---

# SDK iOS integration

> This reference article covers the iOS SDK integration for the Unity platform. Follow these guide to get Braze running in your Unity application. 

If you are transitioning from a manual integration, read the instructions on [Transitioning to an automated integration](#transitioning-from-manual-to-automated-integration-ios).

## Step 1: Choose your Braze Unity package

The Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bundles native bindings for the Android and iOS platforms, along with a C# interface.

The Braze Unity package is available for download on the [Braze Unity releases page](https://github.com/Appboy/appboy-unity-sdk/releases) with two integration options:

1. `Appboy.unitypackage` only
  - This package bundles the Braze Android and iOS SDKs without any additional dependencies. With this integration method, there will not be proper functionality of Braze in-app messaging, and Content Cards features on iOS. If you intend on utilizing full Braze functionality without custom code, use the option below instead.
  - To use this integration option, ensure that the box next to `Import SDWebImage dependency` is *unchecked* in the Unity UI under "Braze Configuration".
2. `Appboy.unitypackage` with `SDWebImage`
  - This integration option bundles the Braze Android and iOS SDKs and the [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependency for the iOS SDK, which is required for the proper functionality of Braze in-app messaging, and Content Cards features on iOS. The `SDWebImage` framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
  - To automatically import `SDWebImage`, be sure to *check* the box next to `Import SDWebImage dependency` in the Unity UI under "Braze Configuration".

**iOS**: To see if you require the [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependency for your iOS project, visit the [iOS in-app message documentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: As of Unity 2.6.0, the bundled Braze Android SDK artifact requires [AndroidX](https://developer.android.com/jetpack/androidx) dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage`.

## Step 2: Import the package

In the Unity Editor, import the package into your Unity project by navigating to **Assets > Import Package > Custom Package**. Next, click **Import**.

Alternatively, follow the [Unity asset package import](https://docs.unity3d.com/Manual/AssetPackages.html) instructions for a more detailed guide on importing custom Unity packages. 

{% alert note %}
If you only wish to import the iOS or Android plugin, deselect the `Plugins/Android` or `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}

## Step 3: Set your API key

Braze provides a native Unity solution for automating the Unity iOS integration. This solution modifies the built Xcode project using Unity's [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) and subclasses the `UnityAppController` using the `IMPL_APP_CONTROLLER_SUBCLASS` macro.

1. In the Unity Editor, open the Braze Configuration Settings by navigating to **Braze > Braze Configuration**.
2. Check the **Automate Unity iOS Integration** box.
3. In the **Braze API Key** field, input your application's API key found in **Manage Settings**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

If your application is already using another `UnityAppController` subclass, you will need to merge your subclass implementation with `AppboyAppDelegate.mm`.

## Basic SDK integration complete

Braze should now be collecting data from your application, and your basic integration should be complete. For more information on integrating push, check out the following articles: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/), and [Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

To learn about advanced SDK integration options, check out [Advanced Implementation]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced).

[5]: #transitioning-from-manual-to-automated-integration-ios
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[54]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/
