---
nav_title: Activación de mensajes
article_title: Desencadenar mensajes dentro de la aplicación a través del SDK Braze
page_order: 0.2
description: "Aprende a desencadenar mensajes dentro de la aplicación a través del SDK de Braze."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Desencadenar mensajes dentro de la aplicación

> Aprende a desencadenar mensajes dentro de la aplicación a través del SDK de Braze.

## Desencadenamiento y entrega de mensajes

Los mensajes dentro de la aplicación se desencadenan cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`,y `Custom Event` (los dos últimos contienen filtros de propiedad robustos).

Al inicio de la sesión de un usuario, Braze entregará todos los mensajes elegibles dentro de la aplicación a su dispositivo, al tiempo que precarga los activos para minimizar la latencia de visualización. Si el evento desencadenado tiene más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje con la prioridad más alta. Para más información, consulta [Ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

{% alert note %}
Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API ni mediante eventos de la API: sólo eventos personalizados registrados por el SDK. Para saber más sobre el registro, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Pares clave-valor

Cuando creas una campaña en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación.

{% tabs %}
{% tab Android %}
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
Para más información, consulta el [KDoc.](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)
{% endalert %}
{% endtab %}

{% tab swift %}
El siguiente ejemplo utiliza lógica personalizada para establecer la presentación de un mensaje dentro de la aplicación basándose en sus pares clave-valor en `extras`. Para ver un ejemplo de personalización completa, consulta [nuestra aplicación de muestra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

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

{% tab Web %}
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
{% endtabs %}

## Desactivar los desencadenantes automáticos

Por predeterminado, los mensajes dentro de la aplicación se desencadenan automáticamente. Para desactivarlo:

{% tabs %}
{% tab android %}
1. Comprueba que estás utilizando el inicializador automático de integración, que está habilitado por defecto en las versiones `2.2.0` y posteriores.
2. Define la operación de mensajes dentro de la aplicación predeterminada en `DISCARD` añadiendo la siguiente línea a tu archivo `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab swift %}
1. Implementa el delegado `BrazeInAppMessageUIDelegate` en tu aplicación. Para un recorrido completo, consulta [Tutorial: Interfaz de usuario de mensajes dentro de la aplicación](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Actualiza tu método delegado `inAppMessage(_:displayChoiceForMessage:)` para que devuelva `.discard`.
{% endtab %}

{% tab Web %}
Elimina la llamada a `braze.automaticallyShowInAppMessages()` dentro de tu fragmento de código de carga y, a continuación, crea una lógica personalizada para mostrar o no un mensaje dentro de la aplicación.

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
Si llamas a `braze.showInAppMessage` sin eliminar `braze.automaticallyShowInAppMessages()`, es posible que los mensajes se muestren dos veces.
{% endalert %}
{% endtab %}

{% tab Unity %}
{% subtabs %}
{% subtab Android %}
Para Android, anula la selección de **Mostrar automáticamente mensajes dentro de la aplicación** en el editor de configuración de Braze. También puedes configurar `com_braze_inapp_show_inapp_messages_automatically` en `false` en la página `braze.xml` de tu proyecto Unity.

La operación inicial de visualización de mensajes dentro de la aplicación puede establecerse en la configuración de Braze mediante la opción "Operación inicial de visualización del administrador de mensajes dentro de la aplicación".
{% endsubtab %}

{% subtab iOS %}
Para iOS, configura los oyentes del objeto del juego en el editor de configuración de Braze y asegúrate de que la opción **Braze Muestra mensajes dentro de la aplicación** no está seleccionada.

La operación inicial de visualización de mensajes dentro de la aplicación puede establecerse en la configuración de Braze mediante la opción "Operación inicial de visualización del administrador de mensajes dentro de la aplicación".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Anular el límite de velocidad predeterminado

De forma predeterminada, puedes enviar un mensaje dentro de la aplicación una vez cada 30 segundos. Para anular esto, añade la siguiente propiedad a tu archivo de configuración antes de que se inicialice la instancia de Braze. Este valor se utilizará como nuevo límite de velocidad en segundos.

{% tabs %}
{% tab Android %}
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

{% tab Web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## Desencadenar mensajes manualmente

Por defecto, los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra un evento personalizado. Sin embargo, además de esto, puedes desencadenar mensajes manualmente utilizando los siguientes métodos.

### Utilizar un evento del lado del servidor

{% tabs %}
{% tab android %}
Para desencadenar un mensaje dentro de la aplicación utilizando un evento enviado por servidor, envía una notificación push silenciosa al dispositivo, que permita una devolución de llamada push personalizada para registrar un evento basado en SDK. Este evento desencadenará el mensaje dentro de la aplicación dirigido al usuario.

#### Paso 1: Crea una devolución de llamada push para recibir el push silencioso

Registra tu devolución de llamada push personalizada para escuchar una notificación push silenciosa específica. Para más información, consulta [Integración push estándar de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

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

![Dos conjuntos de pares clave-valor: IS_SERVER_EVENT ajustado a "true", y CAMPAIGN_NAME ajustado a "nombre de campaña de ejemplo".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

El código de ejemplo de devolución de llamada push anterior reconoce los pares clave-valor y registra el evento personalizado SDK apropiado.

Si quieres incluir propiedades del evento para adjuntarlas a tu evento "desencadenador de mensajes dentro de la aplicación", puedes hacerlo pasándolas a los pares clave-valor de la carga útil push. En este ejemplo, se ha incluido el nombre de la campaña del mensaje dentro de la aplicación posterior. Tu devolución de llamada push personalizada puede entonces pasar el valor como parámetro de la propiedad del evento al registrar el evento personalizado.

#### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado desde dentro de tu devolución de llamada push personalizada.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de entrega basada en acciones en la que se desencadenará un mensaje dentro de la aplicación cuando "nombre_campaña" sea igual a "ejemplo de nombre de campaña de IAM".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

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
{% endtab %}

{% tab Web %}
En este momento, el SDK de Web Braze no permite desencadenar mensajes manualmente mediante eventos del lado del servidor.
{% endtab %}
{% endtabs %}

### Mostrar un mensaje predefinido

Para mostrar manualmente un mensaje dentro de la aplicación predefinido, utiliza el siguiente método:

{% tabs %}
{% tab Android %}
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

{% tab Web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### Mostrar un mensaje en tiempo real 

También puedes crear y mostrar mensajes locales dentro de la aplicación en tiempo real, utilizando las mismas opciones de localización disponibles en el panel. Para ello:

{% tabs %}
{% tab Android %}
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
Llama manualmente al método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) en tu `inAppMessagePresenter`. Por ejemplo:

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

{% tab Web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab Unity %}
Para mostrar el siguiente mensaje de la pila, utiliza el método `DisplayNextInAppMessage()`. Los mensajes se guardarán en esta pila si se elige `DISPLAY_LATER` o `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` como acción de visualización de mensajes dentro de la aplicación.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Mensajes de intención de salida para Web

Los mensajes de intención de salida son mensajes dentro de la aplicación no disruptivos que se utilizan para comunicar información importante a los visitantes antes de que abandonen tu sitio Web.

Para configurar desencadenadores para estos tipos de mensajes en el SDK de la Web, implementa una biblioteca de intención de salida en tu sitio web (como [la biblioteca de código abierto de ouibounce](https://github.com/carlsednaoui/ouibounce)) y, a continuación, utiliza el código siguiente para registrar `'exit intent'` como un evento personalizado en Braze. Ahora tus futuras campañas de mensajería dentro de la aplicación pueden utilizar este tipo de mensaje como desencadenante de un evento personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
