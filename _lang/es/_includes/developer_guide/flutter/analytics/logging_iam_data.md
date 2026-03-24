{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Registro de datos de mensajes

Para registrar análisis utilizando tu `BrazeInAppMessage`, pasa la instancia a la función de análisis deseada:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (junto con el índice del botón)

Por ejemplo:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Acceso a los datos de los mensajes

Para acceder a los datos de mensajes dentro de la aplicación en tu aplicación Flutter, `BrazePlugin` admite el envío de datos de mensajes dentro de la aplicación mediante [Dart Streams](https://dart.dev/tutorials/language/streams).

El objeto `BrazeInAppMessage` admite un subconjunto de campos disponibles en los objetos del modelo nativo, como `uri`, `message`, `header`, `buttons`, `extras`, etc.

### Escuchar los datos de mensajes dentro de la aplicación en la capa Dart

Para recibir los datos de los mensajes dentro de la aplicación en la capa Dart, utiliza el código siguiente para crear un `StreamSubscription` y llama a `braze.subscribeToInAppMessages()`. Recuerda llamar a `cancel()` en la suscripción al stream cuando ya no la necesites.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Para ver un ejemplo, consulta [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) en la aplicación de ejemplo del SDK de Braze para Flutter.

### Reenviar datos de mensajes dentro de la aplicación desde la capa nativa

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Los datos de los mensajes dentro de la aplicación se reenvían automáticamente desde las capas nativas de Android e iOS. No se requiere configuración adicional.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Si estás utilizando Flutter SDK 17.1.0 o anterior, el reenvío de datos de mensajes dentro de la aplicación desde la capa nativa de iOS requiere configuración manual. Es probable que tu aplicación contenga uno de los siguientes. Para migrar a Flutter SDK 18.0.0, elimina la llamada a `BrazePlugin.processInAppMessage(_:)`: el reenvío de datos ahora se gestiona automáticamente.

{% subtabs %}
{% subtab UI Delegate %}

Elimina la llamada a `BrazePlugin.processInAppMessage(_:)` de tu [implementación del delegado `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv).

{% endsubtab %}

{% subtab Custom presenter %}

Elimina la llamada a `BrazePlugin.processInAppMessage(message)` de la implementación de [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) de tu presentador personalizado:

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Reproducir la devolución de llamada para mensajes dentro de la aplicación (opcional)

Para almacenar cualquier mensaje dentro de la aplicación desencadenado antes de que la devolución de llamada esté disponible y reproducirlo después de que se haya establecido, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
