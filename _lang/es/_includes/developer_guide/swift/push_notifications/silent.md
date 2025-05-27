{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Limitaciones de iOS

El sistema operativo iOS puede incluir notificaciones para algunas características. Ten en cuenta que si experimentas dificultades con estas características, la puerta de notificaciones silenciosas de iOS podría ser la causa. Para más detalles, consulta la documentación de Apple sobre [el método de instancia](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) y [las notificaciones no recibidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

## Configuración de notificaciones push silenciosas

Para utilizar las notificaciones push silenciosas para desencadenar el trabajo en segundo plano, debes configurar tu aplicación para que reciba notificaciones incluso cuando esté en segundo plano. Para ello, añade la capacidad Modos de fondo utilizando el panel **Firma y capacidades** al objetivo principal de la aplicación en Xcode. Selecciona la casilla **Notificaciones remotas**.

![Xcode muestra la casilla de verificación del modo "notificaciones remotas" en "capacidades".]({% image_buster /assets/img_archive/background_mode.png %} "modo en segundo plano habilitado")

Incluso con el modo de fondo de notificaciones remotas habilitado, el sistema no lanzará tu aplicación en segundo plano si el usuario ha forzado la salida de la aplicación. El usuario debe iniciar explícitamente la aplicación o reiniciar el dispositivo para que el sistema pueda iniciar automáticamente la aplicación en segundo plano.

Para más información, consulta la sección ["push background updates"](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) y la [documentación](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) de `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Enviar notificaciones push silenciosas

Para enviar una notificación push silenciosa, establece la bandera `content-available` en `1` en una carga útil de notificación push. 

{% alert note %}
Lo que Apple llama notificación remota no es más que una notificación push normal con la bandera `content-available` activada.
{% endalert %}

La bandera `content-available` puede establecerse en el panel de Braze, así como dentro de nuestro [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) en la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
No se recomienda adjuntar un título y un cuerpo con `content-available=1` porque puede provocar un comportamiento indefinido. Para asegurarte de que una notificación es realmente silenciosa, excluye tanto el título como el cuerpo cuando configures la flag `content-available` en `1.`. Para más detalles, consulta la [documentación de Apple sobre actualizaciones en segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) oficial.
{% endalert %}

![El panel de Braze muestra la casilla "contenido disponible" que se encuentra en la pestaña "configuración" del compositor push.]({% image_buster /assets/img_archive/remote_notification.png %} "contenido disponible")

Al enviar una notificación push silenciosa, puede que también quieras incluir algunos datos en la carga útil de la notificación, para que tu aplicación pueda hacer referencia al evento. Esto podría ahorrarte unas cuantas peticiones de red y aumentar la capacidad de respuesta de tu aplicación.

## Ignorar las notificaciones push internas

Braze utiliza notificaciones push silenciosas para gestionar internamente ciertas características avanzadas, como el seguimiento de desinstalaciones o las geovallas. Si tu aplicación lleva a cabo acciones automáticas en el lanzamiento de aplicaciones o notificaciones push en segundo plano, considera la posibilidad de desencadenar esa actividad mediante notificaciones push internas.

Por ejemplo, si tienes una lógica que llama a tus servidores para obtener nuevo contenido en cada push de fondo o lanzamiento de aplicación, puede que quieras evitar desencadenar los push internos de Braze para evitar un tráfico de red innecesario. Dado que Braze envía ciertos tipos de push internos a todos los usuarios aproximadamente al mismo tiempo, puede producirse una carga significativa del servidor si no se controlan las llamadas a la red durante el lanzamiento de los push internos.

### Paso 1: Comprueba las acciones automáticas de tu aplicación

Comprueba si tu aplicación realiza acciones automáticas en los siguientes lugares y actualiza tu código para ignorar los push internos de Braze:

1. **Receptores push.** Las notificaciones push en segundo plano llamarán a `application:didReceiveRemoteNotification:fetchCompletionHandler:` en la dirección `UIApplicationDelegate`.
2. **Delegado de Aplicación.** Los push en segundo plano pueden lanzar aplicaciones [suspendidas](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) en segundo plano, desencadenando los métodos `application:willFinishLaunchingWithOptions:` y `application:didFinishLaunchingWithOptions:` en tu `UIApplicationDelegate`. Comprueba las `launchOptions` de estos métodos para determinar si la aplicación se ha lanzado desde un push en segundo plano.

### Paso 2: Utiliza el método interno de la utilidad push

Puedes utilizar el método de utilidad estática en `Braze.Notifications` para comprobar si tu aplicación ha recibido o ha sido lanzada por un push interno Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) devolverá `true` en todas las notificaciones push internas de Braze, que incluyen seguimiento de desinstalación, sincronización de banderas de características y notificaciones de sincronización de geovallas.

Por ejemplo:

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}
