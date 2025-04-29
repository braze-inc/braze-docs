## Prerequisites

Before you can implement deep linking into your Flutter app, you'll need to set up deep linking in the native [Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android) or [iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift) layer.

## Implementing deep linking

### Step 1: Set up Flutter's built-in handling

{% tabs %}
{% tab iOS %}
1. In your Xcode project, open your `Info.plist` file.
2. Add a new key-value pair.
3. Set the key to `FlutterDeepLinkingEnabled`.
4. Set the type to `Boolean`.
5. Set the value to `YES`.
    ![An example project's `Info.plist` file with the added key-value pair.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. In your Android Studio project, open your `AndroidManifest.xml` file.
2. Locate `.MainActivity` in your `activity` tags.
3. Within the `activity` tag, add the following `meta-data` tag:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Step 2: Forward data to the Dart layer (optional)

You can use native, first-party, or third-party link handling for complex use cases, such as sending a user to a specific location in your app, or calling a specific function.

#### Example: Deep linking to an alert dialog

{% alert note %}
While the following example does not rely on additional packages, you can use a similar approach to implement native, first-party, or third-party packages, such as [`go_router`](https://pub.dev/packages/go_router). Additional Dart code may be required.
{% endalert %}

First, a method channel is used in the native layer to forward the deep link's URL string data to the Dart layer.

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

Next, a callback function is used in the Dart layer to display an alert dialogue using the URL string data sent previously.

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
