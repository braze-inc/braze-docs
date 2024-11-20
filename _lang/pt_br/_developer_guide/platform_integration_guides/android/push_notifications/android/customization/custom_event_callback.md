---
nav_title: Evento de push de retorno de chamada
article_title: Callback de Evento de Push para Android
platform: Android
page_order: 50
description: "Este artigo de referência explica como usar um retorno de chamada para eventos de push do Android."
channel:
  - push

---

# Evento de push de retorno de chamada {#android-push-listener-callback}

> Este artigo de referência explica como usar um retorno de chamada para eventos push do Android

A Braze fornece um retorno de chamada [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) para quando notificações por push são recebidas, abertas ou descartadas. Recomenda-se colocar este retorno de chamada no seu `Application.onCreate()` para não perder nenhum evento que ocorra enquanto seu aplicativo não estiver em execução.

{% alert note %}
Se anteriormente usava um Receptor de Transmissão Personalizado para essa funcionalidade em seu aplicativo, você pode removê-lo com segurança em favor desta opção de integração.
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
Com os botões de ação de notificação, as intenções `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` são acionadas quando os botões com ações `opens app` ou `deep link` são clicados. A administração de deep linking e extras permanece a mesma. Os botões com ações do `close` não disparam as intenções do `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` e dispensam a notificação automaticamente.
{% endalert %}

{% alert important %}
Crie seu ouvinte de notificação por push em `Application.onCreate` para garantir que o ouvinte seja disparado depois que um usuário final tocar em uma notificação enquanto o app estiver em um estado finalizado.
{% endalert %}
