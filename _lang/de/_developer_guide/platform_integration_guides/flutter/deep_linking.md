---
nav_title: Deeplinking
article_title: Deeplinking für Flutter setzen
platform: Flutter
page_order: 6
description: "Dieser Artikel beschreibt, wie Sie Deeplinks für Ihre Flutter Apps auf Android und iOS setzen."

---

# Deeplinks setzen

> Lernen Sie, wie Sie mit Flutter Deeplinks in Ihre iOS- oder Android-App setzen. Wenn Sie sich eine Beispiel-App ansehen möchten, besuchen Sie [GitHub: Braze Flutter SDK Beispiel](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example). Allgemeine Informationen zum Deeplinking finden Sie in unseren [FAQ zum Deeplinking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Voraussetzungen

Bevor Sie Deeplinks in Ihre Flutter App implementieren können, müssen Sie Deeplinks in der nativen [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/) oder [iOS-Schicht]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/) einrichten.

## Implementieren von Deeplinking

### Schritt 1: Einrichten der in Flutter eingebauten Funktionen

{% tabs %}
{% tab iOS %}
1. Öffnen Sie in Ihrem Xcode-Projekt die Datei `Info.plist`.
2. Fügen Sie ein neues Schlüssel-Wert-Paar hinzu.
3. Stellen Sie den Schlüssel auf `FlutterDeepLinkingEnabled`.
4. Setzen Sie den Typ auf `Boolean`.
5. Setzen Sie den Wert auf `YES`.
    ![Die `Info.plist` Datei eines Beispielprojekts mit dem hinzugefügten Schlüssel-Wert-Paar.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Öffnen Sie in Ihrem Android Studio-Projekt die Datei `AndroidManifest.xml`.
2. Suchen Sie `.MainActivity` in Ihren `activity`-Tags.
3. Fügen Sie innerhalb des Tags `activity` den folgenden Tag `meta-data` hinzu:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Schritt 2: Daten an die Dart-Schicht weiterleiten (optional)

Sie können native Links, Links von Erstanbietern oder Links von Drittanbietern für komplexe Anwendungsfälle verwenden, z. B. um einen Nutzer:in Ihrer App an einen bestimmten Standort zu schicken oder eine bestimmte Funktion aufzurufen.

#### Beispiel: Deeplinking mit Warndialogfeld

{% alert note %}
Das folgende Beispiel basiert zwar nicht auf zusätzlichen Paketen, aber Sie können einen ähnlichen Ansatz verwenden, um native Pakete oder Pakete von Drittanbietern zu implementieren, wie z. B. [`go_router`](https://pub.dev/packages/go_router). Ein zusätzlicher Dart Code kann erforderlich sein.
{% endalert %}

Zunächst wird im nativen Layer ein Methodenkanal verwendet, um die Daten des URL-Strings des Deeplinks an den Dart-Layer weiterzuleiten.

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

Als Nächstes wird eine Callback-Funktion im Dart-Layer verwendet, um einen Warndialog mit den zuvor gesendeten Daten des URL-Strings anzuzeigen.

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

