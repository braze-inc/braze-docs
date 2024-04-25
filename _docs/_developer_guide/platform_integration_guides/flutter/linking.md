---
nav_title: Deep Linking
article_title: Deep Linking for Flutter
platform: Flutter
page_order: 5
description: "This article covers how to implement deep linking for your Flutter apps on Android and iOS."

---

# Deep linking

> Deep linking is a way of providing a link that launches an app, shows specific content, or takes some specific action. Native code can forward deep links to your app's Flutter layer for handling. If you're looking to implement deep links in your iOS and/or Android Flutter app for the first time, follow these steps.

For general information on what deep links are, refer to our [FAQ article][4]. 

## Step 1: Native deep link handling

Integrating deep links into a Flutter app requires native layer deep link set up as a pre-requisite. You can follow our guides for setting up deep links on [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/).

Additionally, if you intend to use Flutter's default deep link handling plugin, you will need to [set one key-value pair in your iOS project's `Info.plist` file](https://docs.flutter.dev/cookbook/navigation/set-up-universal-links#2-adjust-ios-build-settings). Using Xcode to edit your `Info.plist` file, add a new key-value pair, set the key to `FlutterDeepLinkingEnabled `, the type to `Boolean`, and the value to `YES`.

If you do not plan on using third-party plugins to handle deep links in Flutter instead of the default handler, skip this step as setting that key-value pair can break those third-party plugins. In the example code provided later in this guide, we will not be using third-party plugins.

## Step 2: Flutter layer deep link handling and native layer deep link forwarding

The preceeding step is sufficient for enabling your Flutter app to open when a user clicks a deep link. For handling deep links in more intricate ways, such as navigating to a particular part of the app or calling a function, additional Dart code as well as additional native code may be necessary. This is where first-party packages such as `go_router` as well as third-party plugins can be helpful.

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

{% tabs %}
{% tab Dart %}

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

{% endtab %}
{% endtabs %}