## Requisitos previos

Antes de que puedas implementar la vinculación en profundidad en tu aplicación Flutter, tendrás que configurar la vinculación en profundidad en la capa nativa [de Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android) o [iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## Implementar la vinculación en profundidad

### Paso 1: Configurar el manejo integrado de Flutter

{% tabs %}
{% tab iOS %}
1. En tu proyecto Xcode, abre tu archivo `Info.plist`.
2. Añade un nuevo par clave-valor.
3. Configura la clave en `FlutterDeepLinkingEnabled`.
4. Configura el tipo en `Boolean`.
5. Configura el valor en `YES`.
    ![Archivo `Info.plist` de un proyecto de ejemplo con el par clave-valor añadido.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Archivo Info.plist del proyecto Xcode")
{% endtab %}

{% tab Android %}
1. En tu proyecto de Android Studio, abre tu archivo `AndroidManifest.xml`.
2. Localiza `.MainActivity` en tus etiquetas `activity`.
3. Dentro de la etiqueta `activity`, añade la siguiente etiqueta `meta-data`:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Paso 2: Reenvía los datos a la capa Dart (opcional)

Puedes utilizar la gestión de enlaces nativa, de origen o de terceros para casos de uso complejos, como enviar a un usuario a una ubicación concreta de tu aplicación o llamar a una función específica.

#### Ejemplo: Vinculación en profundidad a un diálogo de alerta

{% alert note %}
Aunque el siguiente ejemplo no depende de paquetes adicionales, puedes utilizar un enfoque similar para implementar paquetes nativos, de origen o de terceros, como por ejemplo [`go_router`](https://pub.dev/packages/go_router). Puede ser necesario un código Dart adicional.
{% endalert %}

En primer lugar, se utiliza un canal de métodos en la capa nativa para reenviar los datos de la cadena URL del vínculo profundo a la capa Dart.

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

A continuación, se utiliza una función de devolución de llamada en la capa Dart para mostrar un diálogo de alerta utilizando los datos de la cadena URL enviados anteriormente.

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
