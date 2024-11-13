---
nav_title: Devolución de llamada de evento push
article_title: Devolución de llamada de eventos push para Android
platform: Android
page_order: 50
description: "En este artículo de referencia se explica cómo utilizar una devolución de llamada para eventos push de Android."
channel:
  - push

---

# Devolución de llamada de evento push {#android-push-listener-callback}

> En este artículo de referencia se explica cómo utilizar una devolución de llamada para eventos push de Android.

Braze proporciona una [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) devolución de llamada para cuando se reciben, abren o descartan notificaciones push. Se recomienda colocar esta devolución de llamada en tu `Application.onCreate()` para no perderte ningún evento que ocurra mientras tu aplicación no se esté ejecutando.

{% alert note %}
Si antes utilizabas un Receptor de difusión personalizado para esta funcionalidad en tu aplicación, puedes eliminarlo sin problemas en favor de esta opción de integración.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Con los botones de acción de notificación, las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se disparan cuando se hace clic en los botones con acciones `opens app` o `deep link`. El tratamiento de los vínculos profundos y los extras sigue siendo el mismo. Los botones con acciones `close` no disparan las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` y descartan la notificación automáticamente.
{% endalert %}

{% alert important %}
Crea tu receptor de notificaciones push en `Application.onCreate` para asegurarte de que se desencadena cuando un usuario final toca una notificación mientras tu aplicación está en estado finalizado.
{% endalert %}
