---
nav_title: Mensajes de activación
article_title: Desencadena mensajes dentro de la aplicación a través del SDK de Braze.
page_order: 0.2
description: "Aprende a desencadear mensajes dentro de la aplicación a través del SDK de Braze."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Desencadenar mensajes dentro de la aplicación

> Aprende a desencadear mensajes dentro de la aplicación a través del SDK de Braze.

## Desencadenantes y entrega de mensajes

Los mensajes dentro de la aplicación se desencadenan cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Session Start`,`Push Click` `Any Purchase`, `Specific Purchase`, y`Custom Event`  (los dos últimos contienen filtros de propiedades robustos).

Al inicio de la sesión de un usuario, Braze entregará todos los mensajes dentro de la aplicación elegibles a tu dispositivo, al tiempo que precargará los activos para minimizar la latencia de visualización. Si el evento desencadenante tiene más de un mensaje dentro de la aplicación elegible, solo se entregará el mensaje con la prioridad más alta. Para obtener más información, consulta [Ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/#about-the-session-lifecycle).

{% alert note %}
Los mensajes dentro de la aplicación no se pueden desencadenar a través de la API ni mediante eventos de la API, solo mediante eventos personalizados registrados por el SDK. Para obtener más información sobre el registro, consulta [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Pares clave-valor

Cuando creas una campaña en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación.

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para obtener más información, consulta el [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
El siguiente ejemplo utiliza lógica personalizada para configurar la presentación de un mensaje dentro de la aplicación basándose en sus pares clave-valor en `extras`. Para ver un ejemplo completo de aplicación personalizada, consulta [nuestra aplicación de muestra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Desactivación de los activadores automáticos

De forma predeterminada, los mensajes dentro de la aplicación se desencadenan automáticamente. Para desactivar esta función:

{% tabs %}

{% tab web %}
Elimina la llamada a`braze.automaticallyShowInAppMessages()`  dentro de tu fragmento de código de carga y, a continuación, crea una lógica personalizada para gestionar la visualización o no de un mensaje dentro de la aplicación.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si llamas`braze.showInAppMessage`sin quitar`braze.automaticallyShowInAppMessages()`, los mensajes pueden aparecer dos veces.
{% endalert %}

Para obtener un control más avanzado sobre la sincronización de los mensajes, incluyendo el aplazamiento y la restauración de mensajes desencadenados, consulta nuestro [tutorial: Aplazamiento y restauración de mensajes ]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)desencadenados.
{% endtab %}

{% tab android %}
1. Implementa el[`IInAppMessageManagerListener`](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener)  para establecer un oyente personalizado.
2. Actualiza tu[`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html)método para que devuelva [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

Para obtener un control más avanzado sobre la sincronización de los mensajes, incluyendo la visualización posterior y la reincorporación a la cola, consulta nuestra página [Personalización de mensajes](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener).
{% endtab %}

{% tab swift %}
1. Implementa el`BrazeInAppMessageUIDelegate`delegado en tu aplicación. Para obtener una guía completa, consulta el [Tutorial: Interfaz de usuario de mensajes ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)dentro de la aplicación.
2. Actualiza tu método delegado `inAppMessage(_:displayChoiceForMessage:)` para que devuelva `.discard`.

Para obtener un control más avanzado sobre la sincronización de los mensajes, incluyendo el aplazamiento y la restauración de mensajes desencadenados, consulta nuestro [tutorial: Aplazamiento y restauración de mensajes ]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)desencadenados.
{% endtab %}

{% tab flutter %}
1. Verifica que estás utilizando el inicializador de integración automática, que está habilitado de forma predeterminada en las versiones`2.2.0`  y posteriores.
2. Define la operación de mensajes dentro de la aplicación predeterminada en `DISCARD` añadiendo la siguiente línea a tu archivo `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
En Android, deselecciona **Mostrar automáticamente mensajes dentro de la aplicación** en el editor de configuración de Braze. También puedes configurar`com_braze_inapp_show_inapp_messages_automatically`  en`false`  en el archivo `braze.xml`.

La operación inicial de visualización de mensajes dentro de la aplicación se puede configurar en Braze utilizando la opción «Operación inicial de visualización del administrador de mensajes dentro de la aplicación».
{% endsubtab %}

{% subtab iOS %}
Para iOS, configura los oyentes de objetos del juego en el editor de configuración de Braze y asegúrate de que **la opción «Braze muestra mensajes dentro de la aplicación»** no esté seleccionada.

La operación inicial de visualización de mensajes dentro de la aplicación se puede configurar en Braze utilizando la opción «Operación inicial de visualización del administrador de mensajes dentro de la aplicación».
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Anular el límite de velocidad predeterminado

De forma predeterminada, puedes enviar un mensaje dentro de la aplicación una vez cada 30 segundos. Para anular esto, añade la siguiente propiedad a tu archivo de configuración antes de que se inicialice la instancia de Braze. Este valor se utilizará como nuevo límite de velocidad en segundos.

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Activación manual de mensajes desencadenados

De forma predeterminada, los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra un evento personalizado. Sin embargo, además de esto, puedes desencadear mensajes manualmente utilizando los siguientes métodos.

### Uso de un evento del lado del servidor del servidor

{% tabs %}
{% tab web %}
En este momento, el SDK de Web Braze no admite el envío manual de mensajes mediante eventos del lado del servidor.
{% endtab %}

{% tab android %}
Para desencadenar un mensaje dentro de la aplicación mediante un evento enviado por el servidor, envía una notificación push silenciosa al dispositivo, lo que permite que una devolución de llamada push personalizada registre un evento basado en SDK. Este evento desencadenará el mensaje dentro de la aplicación dirigido al usuario.

#### Paso 1: Crea una devolución de llamada push para recibir el push silencioso

Registra tu devolución de llamada push personalizada para escuchar una notificación push silenciosa específica. Para obtener más información, consulta [Configuración de notificaciones push]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications).

Se registrarán dos eventos para que se entregue el mensaje dentro de la aplicación, uno por parte del servidor y otro desde dentro de tu devolución de llamada push personalizada. Para asegurarte de que no se duplica el mismo evento, el evento registrado desde dentro de tu devolución de llamada push debe seguir una convención de nomenclatura genérica, por ejemplo, "evento de desencadenamiento de mensaje dentro de la aplicación", y no el mismo nombre que el evento enviado por el servidor. Si no se hace así, la segmentación y los datos de usuario pueden verse afectados por el registro de sucesos duplicados para una única acción de usuario.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Paso 2: Crear una campaña push

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) desencadenada a través del evento enviado por el servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campaña push debe incluir extras de par clave-valor que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Dos conjuntos de pares clave-valor:IS_SERVER_EVENT  establecido en «true» yCAMPAIGN_NAME  establecido en «nombre de campaña de ejemplo».]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

El código de ejemplo de devolución de llamada push anterior reconoce los pares clave-valor y registra el evento personalizado SDK apropiado.

Si quieres incluir propiedades del evento para adjuntarlas a tu evento "desencadenador de mensajes dentro de la aplicación", puedes hacerlo pasándolas a los pares clave-valor de la carga útil push. En este ejemplo, se ha incluido el nombre de la campaña del mensaje dentro de la aplicación posterior. Tu devolución de llamada push personalizada puede entonces pasar el valor como parámetro de la propiedad del evento al registrar el evento personalizado.

#### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado desde dentro de tu devolución de llamada push personalizada.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de entrega basada en acciones en la que se desencadenará un mensaje dentro de la aplicación cuando"campaign_name"  sea igual a «ejemplo de nombre de campaña IAM».]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si se registra un evento enviado por el servidor mientras la aplicación no está en primer plano, el evento se registrará, pero no se mostrará el mensaje dentro de la aplicación. Si quieres que el evento se retrase hasta que la aplicación esté en primer plano, debes incluir una comprobación en tu receptor push personalizado para descartar o retrasar el evento hasta que la aplicación haya entrado en primer plano.
{% endtab %}

{% tab swift %}
#### Paso 1: Manejar el push silencioso y los pares clave-valor

Implementa la siguiente función y llámala dentro del [método`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)::

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

Cuando se reciba el push silencioso, se registrará un evento "desencadenado de mensaje dentro de la aplicación" registrado en el SDK contra el perfil de usuario. 

{% alert important %}
Debido a que se utiliza un mensaje push para registrar un evento personalizado registrado en SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario para habilitar esta solución. Para los usuarios de iOS, Braze sólo almacenará un token a partir del momento en que un usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.
{% endalert %}

#### Paso 2: Crea una campaña push silenciosa

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) que se desencadene a través del evento enviado por el servidor. 

![Campaña de mensajes dentro de la aplicación basada en acciones que se entregará a los usuarios cuyos perfiles de usuario tengan el evento "server_event".]({%image_buster/assets/img_archive/iosServerSentPush.pngpersonalizado    %})

La campaña push debe incluir extras de par clave-valor, que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Una campaña de mensajes dentro de la aplicación basada en acciones que tiene dos pares clave-valor."CAMPAIGN_NAME"  establecido como «Ejemplo de nombre de mensaje dentro de la aplicación» y"IS_SERVER_EVENT"  establecido en «verdadero».]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si hay una clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si la hay.

Puedes modificar el nombre o las propiedades del evento enviando el valor deseado dentro de los extras del par clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como propiedad del evento.

#### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de mensajes dentro de la aplicación basada en acciones que se entregará a los usuarios que realicen el evento personalizado «Activador de mensajes dentro de la aplicación» donde"campaign_name"  es igual a «Ejemplo de nombre de campaña IAM».]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Ten en cuenta que estos mensajes dentro de la aplicación sólo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.
{% endalert %}
{% endtab %}
{% endtabs %}

### Mostrar un mensaje predefinido

Para mostrar manualmente un mensaje dentro de la aplicación predefinido, utiliza el siguiente método:

{% tabs %}
{% tab web %}
Para el SDK web, utiliza`braze.showInAppMessage(inAppMessage)`  para mostrar cualquier mensaje dentro de la aplicación. Para obtener más información y ver un ejemplo, consulta [Mostrar un mensaje en tiempo real](#displaying-a-message-in-real-time).
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### Mostrar un mensaje en tiempo real 

También puedes crear y mostrar mensajes dentro de la aplicación en tiempo real, utilizando las mismas opciones de personalización disponibles en el panel. Para hacerlo:

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
No muestres mensajes dentro de la aplicación cuando el teclado de software se muestra en la pantalla, ya que la representación no está definida en esta circunstancia.
{% endalert %}
{% endtab %}

{% tab swift %}
Llama manualmente al[`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))método en tu `inAppMessagePresenter`. Por ejemplo:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Al crear tu propio mensaje dentro de la aplicación, te excluyes de cualquier seguimiento de análisis y tendrás que gestionar manualmente el registro de clics e impresiones utilizando tu `message.context`.
{% endalert %}
{% endtab %}

{% tab unity %}
Para mostrar el siguiente mensaje de la pila, utiliza el`DisplayNextInAppMessage()`método . Los mensajes se guardarán en esta pila si se `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER`elige`DISPLAY_LATER`  o  como acción de visualización de mensajes dentro de la aplicación.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Mensajes de intención de salida para la Web

Los mensajes de intención de salida son mensajes no intrusivos que se muestran dentro de la aplicación y se utilizan para comunicar información importante a los visitantes antes de que abandonen tu sitio web.

Para configurar activadores para estos tipos de mensajes en el SDK web, implementa una biblioteca de intención de salida en tu sitio web (como [la biblioteca de código abierto de ouibounce](https://github.com/carlsednaoui/ouibounce)) y, a continuación, utiliza el siguiente código para registrarlo`'exit intent'`como un evento personalizado en Braze. Ahora, tus futuras campañas de mensajes dentro de la aplicación pueden utilizar este tipo de mensaje como desencadenante de eventos personalizados.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
