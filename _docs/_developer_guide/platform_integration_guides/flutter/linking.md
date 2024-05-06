---
nav_title: Deep Linking
article_title: Deep Linking for Flutter
platform: Flutter
page_order: 6
description: "This article covers how to implement deep linking for your Flutter apps on Android and iOS."

---

# Deep linking

> Deep linking is a way of providing a link that launches an app, shows specific content, or takes some specific action. Native code can forward deep links to your app's Flutter layer for handling. If you're looking to implement deep links in your iOS and/or Android Flutter app for the first time, follow these steps.

For general information on what deep links are, refer to our [FAQ article][1]. You can see [an example app][5] with all of these steps implemented in our public repository.

## Step 1: Native deep link handling

Integrating deep links into a Flutter app requires setting up native layer deep links as a pre-requisite. You can follow our guides for setting up deep links on [Android][2] and [iOS][3].

## Step 2: Native project configuration.

If you intend to use Flutter's default deep link handling, you will need to modify your iOS project's `Info.plist` file as well as your Android project's `AndroidManifest.xml` file. If you plan on using third-party plugins to handle deep links in Flutter instead of the default handler, skip this step as it can disrupt those third-party plugins. In the example code provided later in this guide, we will not be using third-party plugins.

{% tabs %}
{% tab iOS %}
Using Xcode, edit your `Info.plist` file:
1. Add a new key-value pair.
2. Set the key to `FlutterDeepLinkingEnabled`.
3. Set the type to `Boolean`.
4. Set the value to `YES`.

![An example project's `Info.plist` file with the added key-value pair.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
In your `AndroidManifest.xml` file:
1. Locate your `.MainActivity` `activity` tag.
2. Inside of that `activity` tag, add the following `meta-data` tag:

```xml
  <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
```
{% endtab %}
{% endtabs %}

## Step 3: Dart layer deep link handling and native layer deep link forwarding

The preceding step is sufficient for enabling your Flutter app to open when a user clicks a deep link. For handling deep links in more intricate ways, such as navigating to a particular part of the app or calling a function, additional Dart code as well as additional native code may be necessary. This is where first-party packages such as [`go_router`][6] as well as third-party plugins can be helpful.

To keep this guide dependency-agnostic, we'll show an example that does not use additional dependencies. In this example, we'll handle deep links by presenting an alert modal after the app launches.

We will utilize a method channel to forward the string data of the deep link URL from the native layer to the Dart layer. Start by creating and invoking the method channel in the deep link delegate methods of your native code.

{% tabs %}
{% tab iOS %}

```swift
extension AppDelegate {
  
  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }
  
  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```

{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```

{% endtab %}
{% endtabs %}

Now, in your Dart code, establish the corresponding channel and set the callback to do whatever URL handling you want. In this example, we'll display an alert containing the text of the URL.

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[4]: {% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File"
[5]: https://github.com/braze-inc/braze-flutter-sdk/tree/master/example
[6]: https://pub.dev/packages/go_router
