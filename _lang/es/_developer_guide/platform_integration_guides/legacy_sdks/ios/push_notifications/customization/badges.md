---
nav_title: Señales
article_title: Recuento de señales de notificaciones push para iOS
platform: iOS
page_order: 3.1
description: "Este artículo de referencia explica cómo implementar recuentos de señales en tus notificaciones push de iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Señales

Puedes especificar el recuento de señales deseado cuando redactes una notificación push a través del panel de Braze. También puedes actualizar manualmente el recuento de señales a través de la propiedad [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) o la [carga útil de notificación remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). Braze también borrará el recuento de señales cuando se reciba una notificación Braze mientras la aplicación se está ejecutando en primer plano. 

Si no tienes un plan para borrar las señales como parte del funcionamiento normal de la aplicación o mediante el envío de push que borren la señal, debes borrar la señal cuando la aplicación se active añadiendo el siguiente código al método delegado `applicationDidBecomeActive:` de tu aplicación:

{% tabs %}
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
{% endtabs %}

Ten en cuenta que, si estableces el número de la señal en 0, también se borrarán las notificaciones del centro de notificaciones. Por tanto, aunque no establezcas el número de la señal en las cargas útiles push, puedes establecer el número de la señal en 0 para eliminar las notificaciones push en el centro de notificaciones después de que los usuarios hagan clic en la notificación push.

