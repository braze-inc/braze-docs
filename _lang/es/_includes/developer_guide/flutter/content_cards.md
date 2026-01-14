## Acerca de las tarjetas de contenido de Flutter

El SDK de Braze incluye una fuente de tarjetas predeterminada para que empieces a utilizar las tarjetas de contenido. Para mostrar la fuente de la tarjeta, puedes utilizar el método `braze.launchContentCards()`. La fuente predeterminada de tarjetas incluida en el SDK de Braze gestionará todos los análisis de seguimiento, descarte de tarjetas y representación de las tarjetas de contenido de un usuario.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Métodos de tarjeta

Puedes utilizar estos métodos adicionales para crear una fuente de tarjetas de contenido personalizada dentro de tu aplicación utilizando los siguientes métodos disponibles en la [interfaz pública del complemento](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Método                                         | Descripción                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Solicita las últimas tarjetas de contenido al servidor SDK de Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Registra un clic para el objeto Tarjeta de contenido dado.                                                            |
| `braze.logContentCardImpression(contentCard)` | Registra una impresión para el objeto Tarjeta de contenido dado.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Registra el despido del objeto Tarjeta de contenido dado.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recepción de datos de la tarjeta de contenido

Para recibir datos de la tarjeta de contenido en tu aplicación Flutter, `BrazePlugin` admite el envío de datos de la tarjeta de contenido mediante [Dart Streams](https://dart.dev/tutorials/language/streams).

El [objeto](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` admite un subconjunto de campos disponibles en los objetos del modelo nativo, como `description`, `title`, `image`, `url`, `extras`, etc.

### Paso 1: Escucha los datos de la tarjeta de contenido en la capa Dart

Para recibir los datos de la tarjeta de contenido en la capa Dart, utiliza el código siguiente para crear un `StreamSubscription` y llamar a `braze.subscribeToContentCards()`. Recuerda `cancel()` la suscripción de streaming cuando ya no la necesites.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Para ver un ejemplo, consulta [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) en nuestra aplicación de ejemplo.

### Paso 2: Transmite los datos de la tarjeta de contenido de la capa nativa

Para recibir los datos de la capa Dart del paso 1, añade el siguiente código para reenviar los datos de la tarjeta de contenido desde las capas nativas.

{% tabs %}
{% tab Android %}

Los datos de la tarjeta de contenido se envían automáticamente desde la capa de Android.

{% endtab %}
{% tab iOS %}

1. Implementa `contentCards.subscribeToUpdates` para suscribirte a las actualizaciones de las tarjetas de contenido como se describe en la documentación [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)).

2. Tu implementación de devolución de llamada a `contentCards.subscribeToUpdates` debe llamar a `BrazePlugin.processContentCards(contentCards)`.

Para ver un ejemplo, consulta [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) en nuestra aplicación de ejemplo.

{% endtab %}
{% endtabs %}

#### Repetición de la devolución de llamada para tarjetas de contenido

Para almacenar las tarjetas de contenido desencadenadas antes de que esté disponible la devolución de llamada y reproducirlas una vez establecida, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
