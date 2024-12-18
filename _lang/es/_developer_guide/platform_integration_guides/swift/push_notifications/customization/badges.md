---
nav_title: Señales
article_title: Recuento de señales de notificaciones push para iOS
platform: Swift
page_order: 2
description: "En este artículo se explica cómo implementar los recuentos de señales de iOS para el SDK Swift."
channel:
  - push

---

# Señales

> Las señales son pequeños iconos ideales para llamar la atención del usuario. Puedes especificar un recuento de señales en los [**Configuración**]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/) cuando redactes una notificación push utilizando el panel de Braze. También puedes actualizar manualmente el recuento de señales a través de la propiedad [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) o la [carga útil de notificación remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

Braze borrará automáticamente el recuento de señales cuando se reciba una notificación Braze mientras la aplicación esté en primer plano. Si estableces manualmente el número de la señal en 0, también se borrarán las notificaciones del centro de notificaciones. 

Si no tienes un plan para borrar las señales como parte del funcionamiento normal de la aplicación o mediante el envío de push que borren la señal, debes borrar la señal cuando la aplicación se active añadiendo el siguiente código al método delegado `applicationDidBecomeActive:` de tu aplicación:

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

