## Acerca de las tarjetas de contenido de Flutter

El SDK de Braze incluye una fuente de tarjetas predeterminada para que empieces a utilizar las tarjetas de contenido. Para mostrar la fuente de tarjetas, puedes utilizar el método `braze.launchContentCards()`. La fuente predeterminada de tarjetas incluida en el SDK de Braze gestionará todo el seguimiento de análisis, los descartes y la representación de las tarjetas de contenido de un usuario.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Métodos de tarjeta

Puedes utilizar estos métodos adicionales para crear una fuente de tarjetas de contenido personalizada dentro de tu aplicación, usando los siguientes métodos disponibles en la [interfaz pública del complemento](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Método                                         | Descripción                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Solicita las últimas tarjetas de contenido al servidor del SDK de Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Registra un clic para el objeto de tarjeta de contenido dado.                                                            |
| `braze.logContentCardImpression(contentCard)` | Registra una impresión para el objeto de tarjeta de contenido dado.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Registra un descarte para el objeto de tarjeta de contenido dado.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recepción de datos de tarjetas de contenido

Para recibir datos de tarjetas de contenido en tu aplicación Flutter, `BrazePlugin` admite el envío de datos de tarjetas de contenido mediante [Dart Streams](https://dart.dev/tutorials/language/streams).

El [objeto](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` admite un subconjunto de campos disponibles en los objetos del modelo nativo, como `description`, `title`, `image`, `url`, `extras`, etc.

### Escuchar datos de tarjetas de contenido en la capa Dart

Para recibir los datos de tarjetas de contenido en la capa Dart, utiliza el código siguiente para crear un `StreamSubscription` y llamar a `braze.subscribeToContentCards()`. Recuerda llamar a `cancel()` en la suscripción al stream cuando ya no la necesites.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Para ver un ejemplo, consulta [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) en la aplicación de ejemplo del SDK de Braze para Flutter.

### Transmitir datos de tarjetas de contenido desde la capa nativa de iOS

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Los datos de tarjetas de contenido se transmiten automáticamente desde las capas nativas de Android e iOS. No se requiere configuración adicional.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Si estás utilizando Flutter SDK 17.1.0 o anterior, la transmisión de datos de tarjetas de contenido desde la capa nativa de iOS requiere configuración manual. Es probable que tu aplicación contenga una devolución de llamada `contentCards.subscribeToUpdates` que llame a `BrazePlugin.processContentCards(contentCards)`. Para migrar a Flutter SDK 18.0.0, elimina la llamada a `BrazePlugin.processContentCards(_:)`: la transmisión de datos ahora se gestiona automáticamente.

Para ver un ejemplo, consulta [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) en la aplicación de ejemplo del SDK de Braze para Flutter.

{% endtab %}
{% endtabs %}

#### Repetición de la devolución de llamada para tarjetas de contenido

Para almacenar las tarjetas de contenido desencadenadas antes de que la devolución de llamada esté disponible y reproducirlas una vez establecida, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
