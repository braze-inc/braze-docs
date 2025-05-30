## Conditions préalables

Avant de pouvoir implémenter des liens profonds dans votre application Flutter, vous devrez configurer les liens profonds dans la couche [Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android) ou [iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift) native.

## Implémentation de liens profonds

### Étape 1 : Configurer la gestion intégrée de Flutter

{% tabs %}
{% tab iOS %}
1. Dans votre projet Xcode, ouvrez votre fichier `Info.plist`.
2. Ajoutez une nouvelle paire clé-valeur.
3. Définissez la clé sur `FlutterDeepLinkingEnabled`.
4. Réglez le type sur `Boolean`.
5. Définissez la valeur sur `YES`.
    ![Fichier `Info.plist` d'un projet exemple avec la paire clé-valeur ajoutée.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Fichier Info.plist du projet Xcode")
{% endtab %}

{% tab Android %}
1. Dans votre projet Android Studio, ouvrez votre fichier `AndroidManifest.xml`.
2. Recherchez `.MainActivity` dans vos balises `activity`.
3. À l'intérieur de la balise `activity`, ajoutez la balise `meta-data` suivante :
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Étape 2 : Transmettre les données à la couche Dart (facultatif)

Vous pouvez utiliser le traitement des liens natifs, de première partie ou de tierce partie pour des cas d'utilisation complexes, tels que l'envoi d'un utilisateur à un emplacement/localisation spécifique dans votre application, ou l'appel d'une fonction spécifique.

#### Exemple : Lien profond vers une boîte de dialogue d'alerte

{% alert note %}
Bien que l'exemple suivant ne repose pas sur des paquets supplémentaires, vous pouvez utiliser une approche similaire pour implémenter des paquets natifs, first-party ou third-party, tels que [`go_router`](https://pub.dev/packages/go_router). Un code Dart supplémentaire peut être nécessaire.
{% endalert %}

Tout d'abord, un canal de méthode est utilisé dans la couche native pour transmettre les données de la chaîne de caractères de l'URL du lien profond à la couche Dart.

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

Ensuite, une fonction de rappel est utilisée dans la couche Dart pour afficher un dialogue d'alerte en utilisant les données de la chaîne de caractères URL envoyées précédemment.

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
