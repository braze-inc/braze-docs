---
nav_title: Universal Deep Link Delegate
platform: FireOS
page_order: 5

---

## Universal Deep Link Delegate

Android SDK [v2.0.0][2] added the ability to set a single delegate object to custom handle all deep links opened by Braze across in-app messages, push, and the News Feed. Prior to v2.0.0, deep link delegates needed to be set separately for each channel.

Your delegate object should implement the `IAppboyNavigator` interface and be set using `AppboyNavigator.setAppboyNavigator()`. In most cases, the delegate should be set in your app's `Application.onCreate()`.

See [`CustomAppboyNavigator.java`][1] for an example implementation.

>  You must also provide instructions for Braze to navigate to your app's (optional) News Feed implementation. To use Braze's default handling, call `AppboyNavigator.executeNewsFeedAction(context, uriAction)`.

>  Prior to v2.0.0, Braze Navigator was only used when opening in-app messages.

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomAppboyNavigator.java
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#200
