{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Métodos de registro

Puedes utilizar estos métodos pasando tu instancia `BrazeInAppMessage` para registrar análisis y realizar acciones:

| Método                                                    | Descripción                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Registra un clic para los datos de mensajes dentro de la aplicación proporcionados.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Registra una impresión para los datos de mensajes dentro de la aplicación proporcionados.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Registra un clic de botón para los datos de mensaje dentro de la aplicación y el ID de botón proporcionados.               |
| `hideCurrentInAppMessage()`                               | Descarta el mensaje dentro de la aplicación que se está mostrando.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Realiza la acción para un mensaje dentro de la aplicación.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Realiza la acción de un botón de mensaje dentro de la aplicación.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Tratamiento de datos de mensajes

En la mayoría de los casos, puedes utilizar el método `Braze.addListener` para registrar escuchadores de eventos que gestionen los datos procedentes de mensajes dentro de la aplicación. 

Además, puedes acceder a los datos de los mensajes dentro de la aplicación en la capa JavaScript llamando al método `Braze.subscribeToInAppMessage` para que los SDK publiquen un evento `inAppMessageReceived` cuando se desencadene un mensaje dentro de la aplicación. Pasa una devolución de llamada a este método para ejecutar tu propio código cuando el mensaje dentro de la aplicación sea desencadenado y recibido por el oyente.

Para personalizar cómo se gestionan los datos de los mensajes, consulta los siguientes ejemplos de implementación:

{% tabs local %}
{% tab basic %}
Para mejorar el comportamiento predeterminado, o si no tienes acceso a personalizar el código nativo de iOS o Android, te recomendamos que desactives la interfaz de usuario predeterminada mientras sigues recibiendo eventos de mensajes dentro de la aplicación desde Braze. Para desactivar la interfaz predeterminada, pasa `false` al método `Braze.subscribeToInAppMessage` y utiliza los datos del mensaje dentro de la aplicación para construir tu propio mensaje en JavaScript. Ten en cuenta que tendrás que registrar manualmente los análisis de tus mensajes si decides desactivar la interfaz predeterminada.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```
{% endtab %}

{% tab advanced %}
Para incluir una lógica más avanzada que determine si mostrar o no un mensaje dentro de la aplicación utilizando la interfaz de usuario integrada, implementa mensajes dentro de la aplicación a través de la capa nativa.

{% alert warning %}
Puesto que se trata de una opción de personalización avanzada, ten en cuenta que anular la implementación predeterminada de Braze también anulará la lógica para emitir eventos de mensajes dentro de la aplicación a tus oyentes de JavaScript. Si deseas seguir utilizando `Braze.subscribeToInAppMessage` o `Braze.addListener` como se describe en [Acceder a los datos de mensajes dentro de la aplicación](#accessing-in-app-message-data), tendrás que encargarte tú mismo de publicar los eventos.
{% endalert %}

{% subtabs %}
{% subtab Android %}
Implementa el `IInAppMessageManagerListener` tal y como se describe en nuestro artículo de Android sobre [la escucha personalizada del administrador]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). En tu implementación de `beforeInAppMessageDisplayed`, puedes acceder a los datos de `inAppMessage`, enviarlos a la capa JavaScript y decidir mostrar o no el mensaje nativo en función del valor devuelto.

Para más información sobre estos valores, consulta nuestra [documentación de Android]({{site.baseurl}}/developer_guide/in_app_messages/).

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab iOS %}
### Anular el delegado de interfaz predeterminado

Por predeterminado, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) se crea y asigna cuando inicializas la instancia `braze`. `BrazeInAppMessageUI` es una implementación del protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) y viene con una propiedad `delegate` que puede utilizarse para personalizar la gestión de los mensajes dentro de la aplicación que se han recibido.

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en [nuestro artículo sobre iOS aquí](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. En el método delegado `inAppMessage(_:displayChoiceForMessage:)`, puedes acceder a los datos de `inAppMessage`, enviarlos a la capa JavaScript y decidir mostrar o no el mensaje nativo en función del valor de retorno.

Para más detalles sobre estos valores, consulta nuestra [documentación sobre iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```

Para utilizar este delegado, asígnalo a `brazeInAppMessagePresenter.delegate` después de inicializar la instancia `braze`. 

{% alert note %}
`BrazeUI` solo puede importarse en Objective-C o Swift. Si utilizas Objective-C++, tendrás que manejar esto en un archivo aparte.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### Sobreescribir la interfaz de usuario nativa predeterminada

Si deseas personalizar completamente la presentación de tus mensajes dentro de la aplicación en la capa nativa de iOS, sigue el protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) y asigna tu presentador personalizado siguiendo el siguiente ejemplo:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
