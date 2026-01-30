{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Registro de datos de mensajes

Para registrar análisis utilizando tu `BrazeInAppMessage`, pasa la instancia a la función de análisis deseada:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (junto con el índice de botones)

Por ejemplo:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Acceder a los datos de los mensajes

Para acceder a los datos de mensajes dentro de la aplicación Flutter, `BrazePlugin` admite el envío de datos de mensajes dentro de la aplicación mediante [Dart Streams](https://dart.dev/tutorials/language/streams).

El objeto `BrazeInAppMessage` admite un subconjunto de campos disponibles en los objetos del modelo nativo, como `uri`, `message`, `header`, `buttons`, `extras`, etc.

### Paso 1: Escucha los datos de mensajes dentro de la aplicación en la capa Dart

Para recibir los datos de los mensajes dentro de la aplicación en la capa Dart, utiliza el código siguiente para crear un `StreamSubscription` y llama a `braze.subscribeToInAppMessages()`. Recuerda `cancel()` la suscripción de streaming cuando ya no la necesites.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Para ver un ejemplo, consulta [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) en nuestra aplicación de ejemplo.

### Paso 2: Reenvía datos de mensajes dentro de la aplicación desde la capa nativa

Para recibir los datos en la capa Dart del paso 1, añade el siguiente código para reenviar los datos de los mensajes dentro de la aplicación desde las capas nativas.

{% tabs %}
{% tab Android %}

Los datos de los mensajes dentro de la aplicación se reenvían automáticamente desde la capa de Android.

{% endtab %}
{% tab iOS %}
{% subtabs %}

Puedes reenviar datos de mensajes dentro de la aplicación de una de estas dos formas:

{% subtab UI Delegate %}

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en nuestro artículo de iOS sobre [el delegado principal de mensajes dentro de la aplicación](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Actualiza la [implementación de tu delegado `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) para que llame a `BrazePlugin.process(inAppMessage)`.
{% endsubtab %}

{% subtab custom presenter %}
1. Asegúrate de haber habilitado la interfaz de mensajes dentro de la aplicación y configura `inAppMessagePresenter` con tu presentador personalizado.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. Crea tu clase de presentador personalizada y llama a `BrazePlugin.process(inAppMessage)` dentro de [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
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

### Paso 3: Repetición de la devolución de llamada para mensajes dentro de la aplicación (opcional)

Para almacenar cualquier mensaje dentro de la aplicación desencadenado antes de que la devolución de llamada esté disponible y reproducirlo después de que se haya establecido, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
