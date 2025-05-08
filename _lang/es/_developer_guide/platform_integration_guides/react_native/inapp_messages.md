---
nav_title: Mensajes dentro de la aplicación
article_title: Mensajes dentro de la aplicación para React Native
platform: React Native
page_order: 4
page_type: reference
description: "Este artículo trata de los mensajes dentro de la aplicación para aplicaciones de iOS y Android que utilizan React Native, incluida la personalización y el análisis de registro."
channel: in-app messages

---

# Integración de mensajes dentro de la aplicación

> Los mensajes nativos dentro de la aplicación se muestran automáticamente en Android e iOS cuando se utiliza React Native. Este artículo trata sobre la personalización y el registro de análisis de tus mensajes dentro de la aplicación para aplicaciones que utilizan React Native.

## Acceder a datos de mensajes dentro de la aplicación

En la mayoría de los casos, puedes utilizar el método `Braze.addListener` para registrar escuchadores de eventos que gestionen los datos procedentes de mensajes dentro de la aplicación. 

Además, puedes acceder a los datos de los mensajes dentro de la aplicación en la capa JavaScript llamando al método `Braze.subscribeToInAppMessage` para que los SDK publiquen un evento `inAppMessageReceived` cuando se desencadene un mensaje dentro de la aplicación. Pasa una devolución de llamada a este método para ejecutar tu propio código cuando el mensaje dentro de la aplicación sea desencadenado y recibido por el oyente.

Para personalizar aún más el comportamiento predeterminado, o si no tienes acceso a personalizar el código nativo de iOS o Android, te recomendamos que desactives la interfaz de usuario predeterminada mientras sigues recibiendo eventos de mensajes dentro de la aplicación de Braze. Para desactivar la interfaz predeterminada, pasa `false` al método `Braze.subscribeToInAppMessage` y utiliza los datos del mensaje dentro de la aplicación para construir tu propio mensaje en JavaScript. Ten en cuenta que tendrás que [registrar manualmente los análisis](#analytics) de tus mensajes si decides desactivar la interfaz predeterminada.

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

## Personalización avanzada

Para incluir una lógica más avanzada que determine si mostrar o no un mensaje dentro de la aplicación utilizando la interfaz de usuario integrada, implementa mensajes dentro de la aplicación a través de la capa nativa.

{% alert warning %}
Puesto que se trata de una opción de personalización avanzada, ten en cuenta que anular la implementación predeterminada de Braze también anulará la lógica para emitir eventos de mensajes dentro de la aplicación a tus oyentes de JavaScript. Si deseas seguir utilizando `Braze.subscribeToInAppMessage` o `Braze.addListener` como se describe en [Acceder a los datos de mensajes dentro de la aplicación](#accessing-in-app-message-data), tendrás que encargarte tú mismo de publicar los eventos.
{% endalert %}

{% tabs %}
{% tab Android %}

Implementa el `IInAppMessageManagerListener` tal y como se describe en nuestro artículo de Android sobre [la escucha personalizada del administrador]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). En tu implementación de `beforeInAppMessageDisplayed`, puedes acceder a los datos de `inAppMessage`, enviarlos a la capa JavaScript y decidir mostrar o no el mensaje nativo en función del valor devuelto.

Para más información sobre estos valores, consulta nuestra [documentación de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

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
{% endtab %}
{% tab iOS %}
### Anular el delegado de interfaz predeterminado

Por predeterminado, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) se crea y asigna cuando inicializas la instancia `braze`. `BrazeInAppMessageUI` es una implementación del protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) y viene con una propiedad `delegate` que puede utilizarse para personalizar la gestión de los mensajes dentro de la aplicación que se han recibido.

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en [nuestro artículo sobre iOS aquí](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. En el método delegado `inAppMessage(_:displayChoiceForMessage:)`, puedes acceder a los datos de `inAppMessage`, enviarlos a la capa JavaScript y decidir mostrar o no el mensaje nativo en función del valor de retorno.

Para más detalles sobre estos valores, consulta nuestra [documentación sobre iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}

Para utilizar este delegado, asígnalo a `brazeInAppMessagePresenter.delegate` después de inicializar la instancia `braze`. 

{% alert note %}
`BrazeUI` solo puede importarse en Objective-C o Swift. Si utilizas Objective-C++, tendrás que manejar esto en un archivo aparte.
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### Sobreescribir la interfaz de usuario nativa predeterminada

Si deseas personalizar completamente la presentación de tus mensajes dentro de la aplicación en la capa nativa de iOS, sigue el protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) y asigna tu presentador personalizado siguiendo el siguiente ejemplo:

{% subtabs %}
{% subtab OBJECTIVE-C %}
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

## Métodos de análisis y acción

Puedes utilizar estos métodos pasando tu instancia `BrazeInAppMessage` para registrar análisis y realizar acciones:

| Método                                                    | Descripción                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Registra un clic para los datos de mensajes dentro de la aplicación proporcionados.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Registra una impresión para los datos de mensajes dentro de la aplicación proporcionados.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Registra un clic de botón para los datos de mensaje dentro de la aplicación y el ID de botón proporcionados.               |
| `hideCurrentInAppMessage()`                               | Descarta el mensaje dentro de la aplicación que se está mostrando.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Realiza la acción para un mensaje dentro de la aplicación.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Realiza la acción de un botón de mensaje dentro de la aplicación.                                     |

## Prueba de visualización de un mensaje dentro de la aplicación de ejemplo

Sigue estos pasos para probar un ejemplo de mensaje dentro de la aplicación.

1. Establece un usuario activo en la aplicación React llamando al método `Braze.changeUserId('your-user-id')`.
2. Dirígete a **Campañas** y sigue [esta guía]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) para crear una nueva campaña de mensajería dentro de la aplicación.
3. Redacta tu campaña de mensajería dentro de la aplicación de prueba y dirígete a la pestaña **Prueba**. Añade el mismo `user-id` que el usuario de prueba y haz clic en **Enviar prueba**. En breve podrás lanzar un mensaje dentro de la aplicación en tu dispositivo.

![Una campaña de mensajería dentro de la aplicación Braze que muestra que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu mensaje dentro de la aplicación.]({% image_buster /assets/img/react-native/iam-test.png %} "Prueba de mensajería dentro de la aplicación")

Puedes encontrar un ejemplo de implementación en BrazeProject, dentro del [SDK de React Native](https://github.com/braze-inc/braze-react-native-sdk). Puedes encontrar más ejemplos de implementación para Android e iOS en el SDK de [Android](https://github.com/braze-inc/braze-android-sdk) e [iOS](https://github.com/braze-inc/braze-swift-sdk).

## Modelo de datos de mensajes dentro de la aplicación

El modelo de mensajes dentro de la aplicación está disponible en el SDK de React Native. Braze tiene cuatro tipos de mensajes dentro de la aplicación que comparten el mismo modelo de datos: **deslizamiento hacia arriba**, **modal**, **completo** y **HTML completo**.

### Propiedades del modelo de mensajes dentro de la aplicación

El modelo de mensajes dentro de la aplicación proporciona la base para todos los mensajes dentro de la aplicación.

|Propiedad          | Descripción                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | La representación JSON del mensaje.                                                                                |
|`message`         | El texto del mensaje.                                                                                                      |
|`header`          | La cabecera del mensaje.                                                                                                    |
|`uri`             | La URI asociada a la acción de hacer clic en el botón.                                                                       |
|`imageUrl`        | La URL de la imagen del mensaje.                                                                                                 |
|`zippedAssetsUrl` | Los activos comprimidos preparados para mostrar contenido HTML.                                                                    |
|`useWebView`      | Indica si la acción de hacer clic en el botón debe redirigirse utilizando una vista Web.                                            |
|`duration`        | La duración de la visualización del mensaje.                                                                                          |
|`clickAction`     | El tipo de acción de clic del botón. Los tres tipos son: `NEWS_FEED`, `URI`, y `NONE`.                                     |
|`dismissType`     | El tipo de cierre del mensaje. Los dos tipos son: `SWIPE` y `AUTO_DISMISS`.                                                 |
|`messageType`     | El tipo de mensaje dentro de la aplicación admitido por el SDK. Los cuatro tipos son: `SLIDEUP`, `MODAL`, `FULL` y `HTML_FULL`.          |
|`extras`          | El diccionario de extras de mensajes. Valor predeterminado: `[:]`.                                                                   |
|`buttons`         | La lista de botones del mensaje dentro de la aplicación.                                                                             |
|`toString()`      | El mensaje como representación de una cadena.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa del modelo de mensajes dentro de la aplicación, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Propiedades del modelo del botón de mensajes dentro de la aplicación

Se pueden añadir botones a los mensajes dentro de la aplicación para realizar acciones y registrar análisis. El modelo de botón proporciona la base para todos los botones de mensajes dentro de la aplicación.

|Propiedad          | Descripción                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | El texto del botón.                                                                                                     |
|`uri`             | La URI asociada a la acción de hacer clic en el botón.                                                                            |
|`useWebView`      | Indica si la acción de hacer clic en el botón debe redirigirse utilizando una vista Web.                                                 |
|`clickAction`     | El tipo de acción de clic que se procesa cuando el usuario hace clic en el botón. Los tres tipos son: `NEWS_FEED`, `URI`, y `NONE`. |
|`id`              | El ID del botón del mensaje.                                                                                               |
|`toString()`      | El botón como representación de una cadena.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa del modelo de botones, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

