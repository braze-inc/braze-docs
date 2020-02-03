* `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs as well as the [SDWebImage][unity-1] dependency for the iOS SDK, which is required for proper functionality of Braze's In-App Messaging, News Feed, and Content Cards features on iOS. The [SDWebImage][unity-1] framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality and are not using [androidX][unity-3] dependencies, download and import this package.

* `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage][unity-1] framework not being present. This package is useful if you do not want the [SDWebImage][unity-1] framework present in your iOS app.

* `Appboy-jetified.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the Braze Android artifacts being transformed via jetifier to support [androidX][unity-3]. This package is particularly useful if using the latest [`firebase messaging unity`][unity-2] versions. The [SDWebImage][unity-1] framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality and are using [androidX][unity-3] dependencies, download and import this package.

* `Appboy-jetified-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the Braze Android artifacts being transformed via jetifier to support [androidX][unity-3] and the [SDWebImage][unity-1]] framework not being present. This package is particularly useful if using the latest [`firebase messaging unity`][unity-2] versions and you do not want the [SDWebImage][unity-1] framework present in your iOS app.

> To see if you require the [SDWebImage][unity-1] dependency for your iOS project, please see the [iOS In-App Message Documentation][unity-4].

[unity-1]: https://github.com/rs/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/
