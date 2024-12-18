---
nav_title: Ignorar el push interno
article_title: Ignorar las notificaciones push internas de Braze para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia explica cómo ignorar las notificaciones push internas de Braze."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ignorar las notificaciones push internas de Braze

Braze utiliza notificaciones push silenciosas para la implementación interna de ciertas características avanzadas. Para la mayoría de las integraciones, esto no requiere ningún cambio por parte de tu aplicación. Sin embargo, si integras una característica de Braze que depende de notificaciones push internas (por ejemplo, Uninstall Tracking o geovallas), puede que quieras actualizar tu aplicación para ignorar nuestras notificaciones push internas.

Si tu aplicación realiza acciones automáticas en el lanzamiento de la aplicación o en las notificaciones push en segundo plano, deberías plantearte controlar esa actividad para que no la desencadenen las notificaciones push internas. Por ejemplo, si tienes una lógica que llama a tus servidores para obtener nuevo contenido en cada push de fondo o lanzamiento de una aplicación, probablemente no querrás que nuestros push internos desencadenen eso porque incurrirías en un tráfico de red innecesario. Además, como Braze envía ciertos tipos de push internos a todos los usuarios aproximadamente al mismo tiempo, no separar las llamadas de red en el lanzamiento de los push internos podría introducir una carga significativa en el servidor.

## Comprobar las acciones automáticas de tu aplicación

Debes comprobar si tu aplicación realiza acciones automáticas en los siguientes lugares y actualizar tu código para ignorar nuestros push internos:

1. **Receptores push.** Las notificaciones push en segundo plano llamarán a `application:didReceiveRemoteNotification:fetchCompletionHandler:` en la dirección `UIApplicationDelegate`.
2. **Delegado de Aplicación.** Los push en segundo plano pueden lanzar aplicaciones [suspendidas](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3) en segundo plano, desencadenando los métodos `application:willFinishLaunchingWithOptions:` y `application:didFinishLaunchingWithOptions:` en tu `UIApplicationDelegate`. Puedes comprobar las `launchOptions` de estos métodos para determinar si la aplicación se ha lanzado desde un push en segundo plano.

## Utilizar los métodos internos de la utilidad push de Braze

Puedes utilizar los métodos de utilidad de `ABKPushUtils` para comprobar si tu aplicación ha recibido o ha sido lanzada por un push interno de Braze. `isAppboyInternalRemoteNotification:` devolverá `YES` en todas las notificaciones push internas de Braze, mientras que `isUninstallTrackingRemoteNotification:` y `isGeofencesSyncRemoteNotification:` devolverán `YES` para las notificaciones de seguimiento de desinstalación y de sincronización de geovallas, respectivamente. Consulta [`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h) para las declaraciones de métodos.

## Ejemplo de aplicación {#internal-push-implementation-example}

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

