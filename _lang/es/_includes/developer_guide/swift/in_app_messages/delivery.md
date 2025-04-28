{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Mensajes desencadenados

### Tipos de desencadenantes

Los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Ten en cuenta que los desencadenadores `Specific Purchase` y `Custom Event` también contienen sólidos filtros de propiedades.

{% alert note %}
Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API ni mediante eventos de la API: sólo eventos personalizados registrados por el SDK. Para saber más sobre el registro, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Semántica de la entrega

Todos los mensajes elegibles dentro de la aplicación se entregan al dispositivo del usuario al inicio de su sesión. Cuando se entreguen, el SDK precargará los activos, para que estén disponibles en el momento de desencadenar, minimizando la latencia de visualización. Si el evento desencadenado tiene más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje con la prioridad más alta.

Para más información sobre la semántica de inicio de sesión del SDK,[consultaCiclo de vida de]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift) la sesión.

### Límite de velocidad predeterminado

De forma predeterminada, puedes enviar un mensaje dentro de la aplicación una vez cada 30 segundos.

Para anular esto, añade la propiedad `triggerMinimumTimeInterval` a tu configuración de Braze antes de que se inicialice la instancia de Braze. Se puede establecer en cualquier número entero positivo y representa el intervalo de tiempo mínimo en segundos. Por ejemplo:

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

## Pares clave-valor

Cuando creas una campaña en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación. Por ejemplo:

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

## Desactivar los desencadenantes automáticos

Para evitar que los mensajes dentro de la aplicación se desencadenen automáticamente:

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en nuestro [artículo sobre iOS aquí](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Actualiza tu método delegado `inAppMessage(_:displayChoiceForMessage:)` para que devuelva `.discard`.

## Desencadenar mensajes manualmente

### Utilizar un evento del lado del servidor

Para desencadenar mensajes dentro de la aplicación utilizando eventos del lado del servidor, envía un push silencioso al dispositivo para que éste registre un evento basado en SDK. Este evento SDK puede desencadenar posteriormente el mensaje dentro de la aplicación dirigido al usuario.

#### Paso 1: Manejar el push silencioso y los pares clave-valor

Implementa la siguiente función y llámala dentro del [método`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)::

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Cuando se reciba el push silencioso, se registrará un evento "desencadenado de mensaje dentro de la aplicación" registrado en el SDK contra el perfil de usuario. 

{% alert important %}
Debido a que se utiliza un mensaje push para registrar un evento personalizado registrado en SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario para habilitar esta solución. Para los usuarios de iOS, Braze sólo almacenará un token a partir del momento en que un usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.
{% endalert %}

#### Paso 2: Crea una campaña push silenciosa

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) que se desencadene a través del evento enviado por el servidor. 

![Una campaña de mensajería dentro de la aplicación basada en acciones que se entregará a los usuarios cuyos perfiles de usuario tengan el evento personalizado "evento_servidor".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campaña push debe incluir extras de par clave-valor, que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Una campaña de mensajería dentro de la aplicación de entrega basada en acciones que tiene dos pares clave-valor. "CAMPAIGN_NAME" configurado como "Ejemplo de nombre de mensaje dentro de la aplicación", y "IS_SERVER_EVENT" configurado como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si hay una clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si la hay.

Puedes modificar el nombre o las propiedades del evento enviando el valor deseado dentro de los extras del par clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como propiedad del evento.

#### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de mensajes dentro de la aplicación de entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "Desencadenante de mensajes dentro de la aplicación" donde "nombre_campaña" es igual a "Ejemplo de nombre de campaña de IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Ten en cuenta que estos mensajes dentro de la aplicación sólo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.
{% endalert %}

### Visualización de un

Para mostrar manualmente un mensaje dentro de la aplicación predefinido, utiliza el siguiente método:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Mostrar un mensaje en tiempo real

También puedes mostrar mensajes locales dentro de la aplicación en tiempo real llamando manualmente al método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) en tu `inAppMessagePresenter`. Por ejemplo:

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

{% alert note %}
Al crear tu propio mensaje dentro de la aplicación, te excluyes de cualquier seguimiento de análisis y tendrás que gestionar manualmente el registro de clics e impresiones utilizando tu `message.context`.
{% endalert %}

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
