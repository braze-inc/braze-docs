* `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs as well as the [SDWebImage][unity-1] dependency for the iOS SDK, which is required for proper functionality of Braze's In-App Messaging, and Content Cards features on iOS. The [SDWebImage][unity-1] framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.

* `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage][unity-1] framework not being present. This package is useful if you do not want the [SDWebImage][unity-1] framework present in your iOS app.

> To see if you require the [SDWebImage][unity-1] dependency for your iOS project, please visit the [iOS In-App Message Documentation][unity-4].

> As of Unity 2.6.0, the bundled Braze Android SDK artifact requires  [AndroidX][unity-3] dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage` above.

[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/
