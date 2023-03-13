---
nav_title: Fonction de rappel événement de notification push
article_title: Fonction de rappel événement de notification push pour Android
platform: Android
page_order: 50
description: "Cet article de référence aborde l’utilisation d’une fonction de rappel pour les événements de notification push sur Android"
channel:
  - Notification push

---
# Custom handling for push receipts, opens, dismissals, and key-value pairs via callback {#android-push-listener-callback}

Braze propose une fonction de rappel [`subscribeToPushNotificationEvents()`][1] pour la réception, l’ouverture ou le rejet des notifications push. Nous vous recommandons de placer cette fonction de rappel dans votre `Application.onCreate()` pour ne manquer aucun événement survenant lorsque votre application n’est pas en fonctionnement.

{% alert note %}
Si vous utilisiez un Récepteur de diffusion personnalisé pour cette fonctionnalité dans votre application, vous pouvez le supprimer en toute sécurité pour adopter cette option d’intégration.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // Le type de notification en soi
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Envoyé lorsque l’utilisateur a rejeté une notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Données de la notification
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Données KVP personnalisées
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
    // Le type de notification en soi
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Envoyé lorsque l’utilisateur a rejeté une notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Données de la notification
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Données KVP personnalisées
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Avec les boutons d’action de notification, les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenchent lorsque les boutons avec les actions `opens app` ou `deep link` sont cliqués. La gestion des liens profonds et des compléments reste la même. Les boutons avec des action `close` ne déclenchent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent automatiquement la notification.
{% endalert %}

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html
