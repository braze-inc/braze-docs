## 前提条件

ディープリンクをFlutterアプリに実装する前に、ネイティブの[Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android)または[iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift)レイヤーでディープリンクを設定する必要があります。

## ディープリンクの実装

### ステップ 1:Flutter の組み込み処理を設定する

{% tabs %}
{% tab iOS %}
1. Xcodeプロジェクトで、`Info.plist`ファイルを開封します。
2. 新しいキーと値のペアを追加します。
3. キーを `FlutterDeepLinkingEnabled` に設定します。
4. タイプを`Boolean`に設定します。
5. 値を`YES`に設定します。
    ![サンプルプロジェクトの\`Info.plist\` ファイルにキーと値のペアが追加されています。]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Android Studio プロジェクトで、`AndroidManifest.xml` ファイルを開封します。
2. `activity` タグで `.MainActivity` を見つけます。
3. `activity`タグ内に、次の`meta-data`タグを追加します:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### ステップ2:データをDartレイヤーに転送する（オプション）

ネイティブ、ファーストパーティ、またはサードパーティのリンク処理を使用して、アプリ内の特定の場所にユーザーを送信したり、特定の機能を呼び出したりするなどの複雑な使用例に対応できます。

#### 例: アラートダイアログへのディープリンク

{% alert note %}
次の例では追加のパッケージに依存していませんが、[`go_router`](https://pub.dev/packages/go_router)のようなネイティブ、ファーストパーティ、またはサードパーティのパッケージを実装するために同様のアプローチを使用できます。追加のDartコードが必要になる場合があります。
{% endalert %}

まず、メソッドチャネルがネイティブ層で使用され、ディープリンクのURL文字列データをDart層に転送します。

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

次に、コールバック関数がDartレイヤーで使用され、以前に送信されたURL文字列データを使用してアラートダイアログを表示します。

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
