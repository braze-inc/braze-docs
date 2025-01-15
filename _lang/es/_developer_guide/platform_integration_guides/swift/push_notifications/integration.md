---
nav_title: Integración
article_title: Integración push para iOS
platform: Swift
page_order: 0
description: "Este artículo de referencia explica cómo configurar las notificaciones push de iOS para el SDK Braze Swift."
channel:
  - push
  
---

# Integración de notificaciones push

> Este artículo de referencia explica cómo configurar las notificaciones push de iOS para el SDK Braze Swift.

[Las notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) te permiten enviar notificaciones desde tu aplicación cuando se producen eventos importantes. Puedes enviar una notificación push cuando tengas nuevos mensajes instantáneos que entregar, alertas de noticias de última hora que enviar o el último episodio del programa de TV favorito de tu usuario listo para que lo descargue para verlo sin conexión. Las notificaciones push también pueden ser [silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), utilizándose sólo para actualizar la interfaz de tu aplicación o desencadenar trabajo en segundo plano. 

Las notificaciones push son estupendas para contenidos esporádicos pero de importancia inmediata, en los que la demora entre las búsquedas en segundo plano puede no ser aceptable. Las notificaciones push también pueden ser mucho más eficientes que la obtención en segundo plano, ya que tu aplicación sólo se lanza cuando es necesario. 

Las notificaciones push tienen una tasa limitada, así que no tengas miedo de enviar tantas como necesite tu aplicación. iOS y los servidores del servicio de notificaciones push de Apple (APN) controlarán la frecuencia con la que se entregan, y no te meterás en problemas por enviar demasiadas. Si tus notificaciones push están estranguladas, podrían retrasarse hasta la próxima vez que el dispositivo envíe un paquete de mantenimiento de conexión o reciba otra notificación.

## Configuración inicial

### Paso 1: Sube tu certificado de APNs

Antes de poder enviar una notificación push de iOS utilizando Braze, debes proporcionar tu archivo de notificación push `.p8` proporcionado por Apple. Como se describe en [la documentación para desarrolladores](https://developer.apple.com/documentation/usernotifications) de Apple:

1. En tu cuenta de desarrollador de Apple, ve a [**Certificados, identificadores y perfiles**](https://developer.apple.com/account/ios/certificate).
2. En **Claves**, selecciona **Todas** y haz clic en el botón de añadir (+) de la esquina superior derecha.
3. En **Descripción de la** clave, introduce un nombre único para la clave de firma.
4. En **Servicios clave**, selecciona la casilla **Servicio de notificaciones push de Apple (APN)** y, a continuación, haz clic en **Continuar**. Haz clic en **Confirmar**.
5. Nota el ID de la clave. Haz clic en **Descargar** para generar y descargar la clave. Asegúrate de guardar el archivo descargado en un lugar seguro, ya que no puedes descargarlo más de una vez.
6. En Braze, ve a **Configuración** > **Configuración de la aplicación** y carga el archivo `.p8` en **Certificado Apple Push**. Puedes subir tu certificado push de desarrollo o de producción. Para probar las notificaciones push después de que tu aplicación esté en vivo en el App Store, se recomienda configurar un espacio de trabajo separado para la versión de desarrollo de tu aplicación.
7. Cuando se te solicite, introduce el [ID del paquete](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), el [ID de la llave](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) y el [ID del equipo](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) de tu aplicación, y luego haz clic en **Guardar**.

{% alert note %}
Si utilizas la [navegación anterior]({{site.baseurl}}/navigation), puedes subir tu archivo `.p8` desde **Administrar configuración** > **Configuración**.
{% endalert %}

### Paso 2: Habilitar las capacidades push

En Xcode, ve a la sección **Firma y capacidades** del objetivo principal de la aplicación y añade la capacidad de notificaciones push.

![La sección "Firma y capacidades" en un proyecto Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## Integración push automática

El SDK de Swift proporciona un enfoque basado únicamente en la configuración para automatizar el procesamiento de las notificaciones remotas recibidas de Braze. Este enfoque es la forma más sencilla de integrar las notificaciones push y se recomienda para la mayoría de los clientes.

Para habilitar la integración push automática, establece la propiedad `automation` de la configuración de `push` en `true`:

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

Esto indica al SDK lo siguiente:
- Registra tu aplicación para notificaciones push en el sistema.
- Solicita la autorización/permiso de notificación push en la inicialización.
- Proporciona dinámicamente implementaciones para los métodos de delegado del sistema relacionados con las notificaciones push.

{% alert note %}
Los pasos de automatización realizados por el SDK son compatibles con las integraciones de gestión de notificaciones push preexistentes en tu código base. El SDK solo automatiza el procesamiento de la notificación remota recibida de Braze. Cualquier controlador del sistema implementado para procesar tus propias notificaciones remotas SDK o las de terceros seguirá funcionando cuando `automation` esté habilitado.
{% endalert %}

{% alert warning %}
El SDK debe inicializarse en el hilo principal para habilitar la automatización de las notificaciones push. La inicialización del SDK debe producirse antes de que la aplicación haya terminado de ejecutarse o en tu implementación de AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Si tu aplicación requiere una configuración adicional antes de inicializar el SDK, consulta la página de documentación [Inicialización retardada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/).
{% endalert %}

### Anular configuraciones individuales

Para un control más granular, cada paso de la automatización puede habilitarse o deshabilitarse individualmente:

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

Consulta [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) para conocer todas las opciones disponibles y [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) para más información sobre el comportamiento de la automatización.

Puedes saltarte la siguiente sección y continuar con la [vinculación en profundidad](#deep-linking) si utilizas la integración push automática.

## Integración push manual

Las notificaciones push también se pueden integrar manualmente. Esta sección describe los pasos necesarios para esta integración. 

{% alert note %}
Si dependes de las notificaciones push para un comportamiento adicional específico de tu aplicación, aún puedes utilizar la integración push automática en lugar de la integración manual de notificaciones push. El método [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) permite recibir notificaciones remotas procesadas por Braze.
{% endalert %}

### Paso 1: Registro para notificaciones push con APNs

Incluye el ejemplo de código apropiado en el [método delegado`application:didFinishLaunchingWithOptions:` ](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de tu aplicación para que los dispositivos de tus usuarios puedan registrarse con las APN. Asegúrate de que llamas a todo el código de integración push en el hilo principal de tu aplicación.

Braze también proporciona categorías push predeterminadas para el soporte del botón de acción push, que deben añadirse manualmente a tu código de registro push. Consulta los [botones de acción para notificación push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/) para conocer los pasos adicionales de la integración.

Añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación. 

{% alert note %}
El siguiente ejemplo de código incluye la integración para la autenticación push provisional (líneas 5 y 6). Si no piensas utilizar la autorización provisional en tu aplicación, puedes eliminar las líneas de código que añaden `UNAuthorizationOptionProvisional` a las opciones de `requestAuthorization`.<br>Visita [las opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber más sobre la autenticación provisional push.
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
Debes asignar tu objeto delegado utilizando `center.delegate = self` de forma sincrónica antes de que tu aplicación termine de ejecutarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. Si no lo haces, puede que tu aplicación no reciba notificaciones push. Visita la documentación [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) de Apple para obtener más información.
{% endalert %}

### Paso 2: Registrar tokens de notificaciones push con Braze

Una vez completado el registro de APN, pasa el `deviceToken` resultante a Braze para habilitar las notificaciones push para el usuario.  

{% tabs %}
{% tab Swift %}

Añade el siguiente código al método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de tu aplicación:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJETIVO-C %}

Añade el siguiente código al método `application:didRegisterForRemoteNotificationsWithDeviceToken:` de tu aplicación:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
Se llama al método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` cada vez que se llama a `application.registerForRemoteNotifications()`. <br><br>Si estás migrando a Braze desde otro servicio push y el dispositivo de tu usuario ya se ha registrado con APN, este método recogerá tokens de los registros existentes la próxima vez que se llame al método, y los usuarios no tendrán que volver a abrirse al push.
{% endalert %}

### Paso 3: Habilitar la gestión push

A continuación, pasa las notificaciones push recibidas a Braze. Este paso es necesario para registrar los análisis push y la gestión de enlaces. Asegúrate de que llamas a todo el código de integración push en el hilo principal de tu aplicación.

#### Manejo predeterminado de las notificaciones push

{% tabs %}
{% tab Swift %}
Para habilitar la gestión de push predeterminada de Braze, añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

A continuación, añade lo siguiente al método `userNotificationCenter(_:didReceive:withCompletionHandler:)` de tu aplicación:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab OBJETIVO-C %}
Para habilitar la gestión de push predeterminada de Braze, añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

A continuación, añade el siguiente código al método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### Manejo de las notificaciones push en primer plano

{% tabs %}
{% tab Swift %}
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciban, implementa `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push de `userNotificationCenter(_:didReceive:withCompletionHandler:)` y Braze registrará el evento push click.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab OBJETIVO-C %}
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciban, implementa `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push de `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` y Braze registrará el evento push click.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## Vínculos profundos

Los vínculos profundos desde un push a la aplicación se gestionan automáticamente a través de nuestra documentación estándar de integración push. Si quieres saber más sobre cómo añadir vínculos profundos a ubicaciones concretas de tu aplicación, consulta nuestros [casos de uso avanzado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation).

## Suscribirse a las actualizaciones de las notificaciones push

Para acceder a las cargas útiles de notificación push procesadas por Braze, utiliza el método [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Puedes utilizar el parámetro `payloadTypes` para especificar si quieres suscribirte a las notificaciones de eventos push abiertos, eventos push recibidos o ambos.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Ten en cuenta que los eventos push recibidos sólo se desencadenarán para las notificaciones en primer plano y `content-available` para las notificaciones en segundo plano. No se desencadenará para las notificaciones recibidas mientras están terminadas ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJETIVO-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Ten en cuenta que los eventos push recibidos sólo se desencadenarán para las notificaciones en primer plano y `content-available` para las notificaciones en segundo plano. No se desencadenará para las notificaciones recibidas mientras están terminadas ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Cuando utilices la integración push automática, `subscribeToUpdates(_:)` es la única forma de recibir notificaciones remotas procesadas por Braze. Los métodos del sistema `UIAppDelegate` y `UNUserNotificationCenterDelegate` no se llaman cuando la notificación es procesada automáticamente por Braze.
{% endalert %}

{% alert tip %}
Crea tu suscripción a notificaciones push en `application(_:didFinishLaunchingWithOptions:)` para asegurarte de que tu suscripción se desencadena cuando un usuario final toca una notificación mientras tu aplicación está en estado finalizado.
{% endalert %}

## Prueba {#push-testing}

Si quieres probar las notificaciones dentro de la aplicación y las notificaciones push a través de la línea de comandos, puedes enviar una única notificación a través del terminal mediante CURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` - disponible en **Configuración** > **Claves de API**.
- `YOUR_EXTERNAL_USER_ID` - disponible en la página **Buscar usuarios**. Para más información, consulta [asignar ID de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), estas páginas se encuentran en una ubicación diferente: <br>- **Las claves de API** se encuentran en **Consola para desarrolladores** > **Configuración de API** <br>- **Buscar usuarios** se encuentra en **Usuarios** > **Búsqueda de usuarios**
{% endalert %}

En el siguiente ejemplo, se utiliza la instancia `US-01`. Si no estás en esta instancia, consulta nuestra [documentación de la API]({{site.baseurl}}/api/basics/) para ver a qué punto final debes hacer solicitudes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Push primers {#push-primers}

Las campañas push primer animan a tus usuarios a habilitar las notificaciones push de tu aplicación en sus dispositivos. Esto puede hacerse sin necesidad de personalizar el SDK utilizando nuestro [primer push sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

