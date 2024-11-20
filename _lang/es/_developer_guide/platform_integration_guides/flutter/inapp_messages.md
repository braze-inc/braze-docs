---
nav_title: Mensajes dentro de la aplicación
article_title: Mensajes dentro de la aplicación para Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "Este artículo trata de los mensajes dentro de la aplicación para aplicaciones de iOS y Android que utilizan Flutter, incluida la personalización y el análisis de registro."
channel: in-app messages

---

# Integración de mensajes dentro de la aplicación

> Aprende a integrar y personalizar mensajes dentro de la aplicación para Android e iOS utilizando Flutter.

## Habilitar la interfaz de mensajes dentro de la aplicación

Para integrar la mensajería dentro de la aplicación de Flutter con iOS, [habilita la mensajería dentro de la aplicación utilizando el SDK Swift de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages). No hay pasos adicionales para Android.

## Análisis de registros

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

## Desactivar la visualización automática

Para desactivar la visualización automática de mensajes dentro de la aplicación, realiza estas actualizaciones en la capa nativa.

{% tabs %}
{% tab Android %}

1. Asegúrate de que utilizas el inicializador automático de integración, que está habilitado por defecto a partir de la versión `2.2.0`.
2. Define la operación de mensajes dentro de la aplicación predeterminada en `DISCARD` añadiendo la siguiente línea a tu archivo `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en nuestro [artículo sobre iOS aquí](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Actualiza tu método delegado `inAppMessage(_:displayChoiceForMessage:)` para que devuelva `.discard`.

{% endtab %}
{% endtabs %}

## Recepción de datos de mensajes dentro de la aplicación

Para recibir datos de mensajes dentro de la aplicación en tu aplicación Flutter, `BrazePlugin` admite el envío de datos de mensajes dentro de la aplicación utilizando [Dart Streams](https://dart.dev/tutorials/language/streams).

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

### Opción 1 - Utilizar `BrazeInAppMessageUIDelegate`

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en nuestro artículo de iOS sobre [el delegado principal de mensajes dentro de la aplicación](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Actualiza la [implementación de tu delegado `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) para que llame a `BrazePlugin.process(inAppMessage)`.

### Opción 2 - Presentador personalizado de mensajes dentro de la aplicación

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

{% endtab %}
{% endtabs %}

#### Repetición de la devolución de llamada para mensajes dentro de la aplicación

Para almacenar cualquier mensaje dentro de la aplicación desencadenado antes de que la devolución de llamada esté disponible y reproducirlo después de que se haya establecido, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Prueba de un ejemplo de mensaje dentro de la aplicación

Sigue estos pasos para probar un ejemplo de mensaje dentro de la aplicación.

1. Establece un usuario activo en la aplicación React llamando al método `braze.changeUser('your-user-id')`.
2. Dirígete a la página **Campañas** de tu panel y sigue [esta guía]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) para crear una nueva campaña de mensajería dentro de la aplicación.
3. Redacta tu campaña de mensajería dentro de la aplicación de prueba y dirígete a la pestaña **Prueba**. Añade el mismo `user-id` que el usuario de prueba y haz clic en **Enviar prueba**.
4. Toca la notificación push y debería aparecer el mensaje dentro de la aplicación en tu dispositivo.

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![Una campaña de mensajería dentro de la aplicación Braze que muestra que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu mensaje dentro de la aplicación.]({% image_buster /assets/img/react-native/iam-test.png %} "Prueba de mensajería dentro de la aplicación")

