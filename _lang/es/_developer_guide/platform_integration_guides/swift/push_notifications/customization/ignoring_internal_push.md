---
nav_title: Ignorar el push interno
article_title: Ignorar las notificaciones push internas de Braze para iOS
platform: Swift
page_order: 6
description: "Este artículo explica cómo ignorar las notificaciones push internas de Braze para el SDK de Swift."
channel:
  - push

---

# Ignorar las notificaciones push internas

> Braze utiliza [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) para la implementación interna de ciertas características avanzadas. Para la mayoría de las integraciones, esto no requiere ningún cambio por parte de tu aplicación. Sin embargo, si integras una característica de Braze que depende de notificaciones push internas (como Uninstall Tracking o geovallas), puede que quieras actualizar tu aplicación para ignorar las notificaciones push internas de Braze.

Si tu aplicación lleva a cabo acciones automáticas en el lanzamiento de aplicaciones o notificaciones push en segundo plano, considera la posibilidad de controlar esa actividad para que no la desencadenen nuestras notificaciones push internas. Por ejemplo, si tienes una lógica que llama a tus servidores para obtener nuevo contenido en cada push de fondo o lanzamiento de una aplicación, probablemente no querrás que los push internos de Braze desencadenen eso porque incurrirías en un tráfico de red innecesario. Además, como Braze envía ciertos tipos de push internos a todos los usuarios aproximadamente al mismo tiempo, no separar las llamadas de red en el lanzamiento de los push internos podría introducir una carga significativa en el servidor.

## Comprobar las acciones automáticas de tu aplicación

Comprueba si tu aplicación realiza acciones automáticas en los siguientes lugares y actualiza tu código para ignorar los push internos de Braze:

1. **Receptores push.** Las notificaciones push en segundo plano llamarán a `application:didReceiveRemoteNotification:fetchCompletionHandler:` en la dirección `UIApplicationDelegate`.
2. **Delegado de Aplicación.** Los push en segundo plano pueden lanzar aplicaciones [suspendidas](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) en segundo plano, desencadenando los métodos `application:willFinishLaunchingWithOptions:` y `application:didFinishLaunchingWithOptions:` en tu `UIApplicationDelegate`. Comprueba las `launchOptions` de estos métodos para determinar si la aplicación se ha lanzado desde un push en segundo plano.

## Utilizando el método interno de la utilidad push

Puedes utilizar el método de utilidad estática en `Braze.Notifications` para comprobar si tu aplicación ha recibido o ha sido lanzada por un push interno Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) devolverá `true` en todas las notificaciones push internas de Braze, que incluyen seguimiento de desinstalación, sincronización de banderas de características y notificaciones de sincronización de geovallas.

## Ejemplo de aplicación {#internal-push-implementation-example}

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

