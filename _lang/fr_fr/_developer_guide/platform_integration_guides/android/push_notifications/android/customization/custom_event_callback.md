---
nav_title: Fonction de rappel événement de notification push
article_title: Fonction de rappel événement de notification push pour Android
platform: Android
page_order: 50
description: "Cet article de référence aborde l’utilisation d’une fonction de rappel pour les événements de notification push sur Android."
channel:
  - push

---

# Fonction de rappel d’événement de notification push {#android-push-listener-callback}

> Cet article de référence aborde l’utilisation d’une fonction de rappel pour les événements de notification push sur Android

Braze propose une fonction de rappel [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) pour la réception, l’ouverture ou le rejet des notifications push. Nous vous recommandons de placer cette fonction de rappel dans votre `Application.onCreate()` pour ne manquer aucun événement survenant lorsque votre application n’est pas en fonctionnement.

{% alert note %}
Si vous utilisiez un Récepteur de diffusion personnalisé pour cette fonctionnalité dans votre application, vous pouvez le supprimer en toute sécurité pour adopter cette option d’intégration.
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
Avec les boutons d’action de notification, les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenchent lorsque les boutons avec les actions `opens app` ou `deep link` sont cliqués. La gestion des liens profonds et des compléments reste la même. Les boutons avec des actions `close` ne déclenchent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent automatiquement la notification.
{% endalert %}

{% alert important %}
Créez votre listener de notification push dans `Application.onCreate` pour vous assurer que votre listener est déclenché après qu'un utilisateur final ait tapé une notification alors que votre application est dans un état terminé.
{% endalert %}
