---
nav_title: Entrega de mensajes dentro de la aplicación
article_title: Entrega de mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 2
description: "Este artículo trata sobre la entrega de mensajes dentro de la aplicación de iOS, enumerando los distintos tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos para el SDK de Swift."
channel:
  - in-app messages

---

# Entrega de mensajes dentro de la aplicación

> Este artículo de referencia proporciona un resumen de la entrega de mensajes dentro de la aplicación de iOS, enumerando los diferentes tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos.

## Tipos de desencadenantes

Los mensajes dentro de la aplicación son desencadenados por eventos registrados por el SDK. Puedes desencadenar un mensaje dentro de la aplicación a partir de los siguientes tipos de eventos: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Además, los desencadenantes `Specific Purchase` y `Custom Event` contienen filtros de propiedades sólidos.

{% alert note %}
Los mensajes desencadenados dentro de la aplicación sólo funcionan con eventos personalizados registrados a través del SDK de Braze. Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API o por eventos de la API (como eventos de compra). Si trabajas con iOS, visita nuestro artículo sobre [seguimiento de eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para obtener más información.
{% endalert %}

## Habilitación de mensajes dentro de la aplicación

Para permitir que Braze muestre mensajes dentro de la aplicación, crea una implementación del protocolo `BrazeInAppMessagePresenter` y asígnala a la opción `inAppMessagePresenter` de tu instancia de Braze. También puedes utilizar el presentador predeterminado de la interfaz de usuario Braze instanciando un objeto `BrazeInAppMessageUI`.

Ten en cuenta que tendrás que importar la biblioteca `BrazeUI` para acceder a la clase `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## Semántica de la entrega

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan al dispositivo del usuario al inicio de la sesión. Tras la entrega, el SDK precargará los activos para que estén disponibles inmediatamente en el momento del desencadenamiento, minimizando la latencia de visualización.

Cuando un evento desencadenante tiene asociado más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje dentro de la aplicación con la prioridad más alta.

Puede haber cierta latencia en los mensajes dentro de la aplicación que se muestran inmediatamente después de la entrega (inicio de sesión, clic push) debido a que los activos no se han precargado. Para más información sobre la semántica de inicio de sesión del SDK, lee sobre nuestro [ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

## Intervalo de tiempo mínimo entre desencadenamientos

De forma predeterminada, limitamos la tasa de mensajes dentro de la aplicación a una vez cada 30 segundos para facilitar una experiencia de usuario de calidad.

Puedes anular este valor estableciendo la propiedad `triggerMinimumTimeInterval` en tu configuración de Braze. Asegúrate de configurar este valor antes de inicializar tu instancia de Braze. Establece en `triggerMinimumTimeInterval` el valor entero que desees como tiempo mínimo en segundos entre mensajes dentro de la aplicación:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## No se encuentra un desencadenante adecuado

Cuando Braze no encuentre un desencadenante que coincida con un evento concreto, llamará a [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/). Implementa este método en tu clase adoptando `BrazeDelegate` para manejar este escenario. 

## La pila de mensajes dentro de la aplicación

### Añadir mensajes dentro de la aplicación al stack

Los usuarios son elegibles para recibir un mensaje dentro de la aplicación en las siguientes situaciones:

- Se dispara un evento desencadenador de mensajes dentro de la aplicación
- Se inicia una sesión
- La aplicación se abre desde una notificación push

Cuando se dispara el evento desencadenante de un mensaje dentro de la aplicación, se coloca en una "pila". Si hay varios mensajes dentro de la aplicación en la pila y esperando a ser mostrados, Braze mostrará primero el mensaje dentro de la aplicación recibido más recientemente (último en entrar, primero en salir).

Cuando un usuario sea elegible para recibir un mensaje dentro de la aplicación, la `BrazeInAppMessagePresenter` solicitará el último mensaje dentro de la aplicación de la pila de mensajes dentro de la aplicación. El stack solo conserva los mensajes dentro de la aplicación almacenados en la memoria y se borra entre los lanzamientos de la aplicación desde el modo suspendido.

### Devolver mensajes dentro de la aplicación al stack

Un mensaje dentro de la aplicación desencadenado puede volver al stack en las siguientes situaciones:

- El mensaje dentro de la aplicación se desencadena cuando la aplicación está en segundo plano.
- Actualmente hay visible otro mensaje dentro de la aplicación.
- El [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` devuelve `.reenqueue`.

El mensaje dentro de la aplicación desencadenado se colocará en la parte superior de la pila para su posterior visualización cuando un usuario sea elegible para recibir un mensaje dentro de la aplicación.

### Descartar mensajes dentro de la aplicación

Un mensaje dentro de la aplicación desencadenado se descartará en las siguientes situaciones:

- El [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` devuelve `.discard`.
- No se ha podido descargar el activo (imagen o archivo ZIP) del mensaje dentro de la aplicación.
- El mensaje dentro de la aplicación está listo para mostrarse, pero ha superado el tiempo de espera.
- La orientación del dispositivo no coincide con la orientación del mensaje dentro de la aplicación desencadenado.

El mensaje dentro de la aplicación se eliminará de la pila. Tras ser descartado, el mensaje dentro de la aplicación puede ser desencadenado posteriormente por otra instancia del evento desencadenante.

## Creación y visualización de mensajes dentro de la aplicación en tiempo real

Si deseas mostrar un mensaje dentro de la aplicación en otros momentos, puedes llamar manualmente al método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) en tu `inAppMessagePresenter`. Los mensajes dentro de la aplicación pueden crearse localmente dentro de la aplicación y mostrarse a través de Braze. Esto es especialmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real.

Ten en cuenta que al crear tu propio mensaje dentro de la aplicación, te excluyes de cualquier seguimiento de análisis y tendrás que gestionar manualmente el registro de clics e impresiones utilizando tu `message.context`.

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## Extras del par clave-valor

Los objetos `Braze.InAppMessage` pueden llevar pares clave-valor como `extras`. Se especifican en el panel al crear una campaña. Los pares clave-valor pueden utilizarse para enviar datos hacia abajo con un mensaje dentro de la aplicación para que tu aplicación los gestione posteriormente.

Por ejemplo, considera un caso en el que queremos personalizar la presentación de un mensaje dentro de la aplicación basándonos en el contenido de sus extras. Podríamos acceder a los pares clave-valor de su propiedad `extras` y definir una lógica personalizada que se ejecute en torno a ella:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Para una implementación completa, puedes consultar los ejemplos de personalización de mensajes dentro de la aplicación en nuestra [aplicación de ejemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

