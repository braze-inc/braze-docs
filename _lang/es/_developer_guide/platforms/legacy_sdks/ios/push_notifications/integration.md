---
nav_title: Integración
article_title: Integración push para iOS
platform: iOS
page_order: 0
description: "Este artículo de referencia explica cómo integrar notificaciones push en tu aplicación iOS."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración push

## Paso 1: Sube tu token de APNs

{% multi_lang_include developer_guide/swift/apns_token.md %}

## Paso 2: Habilitar las capacidades push

En la configuración de tu proyecto, asegúrate de que, en la pestaña **Capacidades**, está alternada la opción **Notificaciones push**.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Si tienes certificados push de desarrollo y producción separados, asegúrate de desmarcar la casilla **Gestionar automáticamente la firma** en la pestaña **General**. Esto te permitirá elegir distintos perfiles de aprovisionamiento para cada configuración de compilación, ya que la característica de firma automática de código de Xcode sólo realiza la firma de desarrollador.

![Configuración del proyecto Xcode mostrando la pestaña "general". En esta pestaña, la opción "Gestionar automáticamente la firma" está desmarcada.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Paso 3: Registro para notificaciones push

Para que el dispositivo de tus usuarios se registre en APN, debes incluir el código de ejemplo adecuado en el método delegado `application:didFinishLaunchingWithOptions:` de tu aplicación. Asegúrate de que llamas a todo el código de integración push en el hilo principal de tu aplicación.

Braze también proporciona categorías push predeterminadas para el soporte del botón de acción push, que deben añadirse manualmente a tu código de registro push. Consulta los [botones de acción para notificación push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons/) para conocer los pasos adicionales de la integración.

{% alert warning %}
Si has implementado una solicitud push personalizada como se describe en nuestras [mejores prácticas push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting/), asegúrate de que llamas al código siguiente **cada vez que se ejecuta la aplicación** después de que concedan permisos push a tu aplicación. **Las aplicaciones tienen que volver a registrarse con los APN, ya que [los token de los dispositivos pueden cambiar arbitrariamente](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Utilizar el marco UserNotification (iOS 10+)

Si utilizas el framework `UserNotifications` (recomendado) introducido en iOS 10, añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación.

{% alert important %}
El siguiente ejemplo de código incluye la integración para la autenticación push provisional (líneas 5 y 6). Si no piensas utilizar la autorización provisional en tu aplicación, puedes eliminar las líneas de código que añaden `UNAuthorizationOptionProvisional` a las opciones de `requestAuthorization`.<br>Visita [las opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber más sobre la autenticación provisional push.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Debes asignar tu objeto delegado utilizando `center.delegate = self` de forma sincrónica antes de que tu aplicación termine de ejecutarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. Si no lo haces, puede que tu aplicación no reciba notificaciones push. Visita la documentación [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) de Apple para obtener más información.
{% endalert %}

### Sin marco UserNotifications

Si no utilizas el framework `UserNotifications`, añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## Paso 4: Registrar tokens de notificaciones push con Braze

Una vez completado el registro de APN, hay que modificar el siguiente método para pasar el `deviceToken` resultante a Braze, de modo que el usuario quede habilitado para las notificaciones push:

{% tabs %}
{% tab OBJECTIVE-C %}

Añade el siguiente código a tu método `application:didRegisterForRemoteNotificationsWithDeviceToken:`:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Añade el siguiente código al método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Se llama al método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` cada vez que se llama a `[[UIApplication sharedApplication] registerForRemoteNotifications]`. Si estás migrando a Braze desde otro servicio push y el dispositivo de tu usuario ya se ha registrado con APN, este método recogerá tokens de los registros existentes la próxima vez que se llame al método, y los usuarios no tendrán que volver a abrirse al push.
{% endalert %}

## Paso 5: Habilitar la gestión push

El siguiente código pasa las notificaciones push recibidas a Braze y es necesario para registrar los análisis push y la gestión de enlaces. Asegúrate de llamar a todo el código de integración push en el hilo principal de tu aplicación.

### iOS 10+

Cuando construyas para iOS 10+, te recomendamos que integres el framework `UserNotifications` y hagas lo siguiente:

{% tabs %}
{% tab OBJECTIVE-C %}

Añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

A continuación, añade el siguiente código al método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Manejo del push en primer plano**

Para mostrar una notificación push mientras la aplicación está en primer plano, implementa `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Si se hace clic en la notificación en primer plano, se llamará al delegado push de iOS 10 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`, y Braze registrará un evento de clic push.

{% endtab %}
{% tab swift %}

Añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

A continuación, añade el siguiente código al método `userNotificationCenter(_:didReceive:withCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Manejo del push en primer plano**

Para mostrar una notificación push mientras la aplicación está en primer plano, implementa `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Si se hace clic en la notificación en primer plano, se llamará al delegado push de iOS 10 `userNotificationCenter(_:didReceive:withCompletionHandler:)`, y Braze registrará un evento de clic push.

{% endtab %}
{% endtabs %}

### Antes de iOS 10

iOS 10 actualizó el comportamiento de forma que ya no llama a `application:didReceiveRemoteNotification:fetchCompletionHandler:` cuando se hace clic en un push. Por esta razón, si no actualizas a la construcción en la versión 10 de iOS y posteriores y utilizas el framework `UserNotifications`, tendrás que llamar a Braze desde ambos delegados antiguos, lo que supone una ruptura con nuestra integración anterior.

Para aplicaciones que se construyen con versiones del SDK anteriores a la versión iOS 10, utiliza las siguientes instrucciones:

{% tabs %}
{% tab OBJECTIVE-C %}

Para habilitar el seguimiento de aperturas en las notificaciones push, añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Para soportar los análisis push en iOS 10, también debes añadir el siguiente código al método delegado `application:didReceiveRemoteNotification:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Para habilitar el seguimiento de aperturas en las notificaciones push, añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Para soportar los análisis push en iOS 10, también debes añadir el siguiente código al método delegado `application(_:didReceiveRemoteNotification:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Paso 6: Vínculos profundos

Los vínculos profundos desde un push a la aplicación se gestionan automáticamente a través de nuestra documentación estándar de integración push. Si quieres saber más sobre cómo añadir vínculos profundos a ubicaciones concretas de tu aplicación, consulta nuestros [casos de uso avanzado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation).

## Paso 7: Pruebas unitarias (opcional)

Para añadir cobertura de pruebas a los pasos de integración que acabas de seguir, implementa [pruebas unitarias push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/).

