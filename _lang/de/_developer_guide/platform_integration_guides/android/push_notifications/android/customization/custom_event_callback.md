---
nav_title: Push Event Callback
article_title: Push Event Callback für Android
platform: Android
page_order: 50
description: "Dieser Referenzartikel beschreibt, wie Sie einen Callback für Push-Events in Android verwenden."
channel:
  - push

---

# Push Event Callback {#android-push-listener-callback}

> Dieser Referenzartikel beschreibt, wie Sie einen Callback für Push-Events in Android verwenden.

Braze stellt einen [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) Callback bereit, wenn Push-Benachrichtigungen empfangen, geöffnet oder verworfen werden. Es wird empfohlen, diesen Callback in Ihrem `Application.onCreate()` zu platzieren, um keine Events zu verpassen, die auftreten, während Ihre Anwendung nicht läuft.

{% alert note %}
Wenn Sie bisher einen angepassten Broadcast-Empfänger für diese Funktion in Ihrer Anwendung verwendet haben, können Sie ihn zugunsten dieser Integrationsoption entfernen.
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
Bei Aktions-Buttons für Benachrichtigungen werden die `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` Absichten ausgelöst, wenn Buttons mit den Aktionen `opens app` oder `deep link` angeklickt werden. Die Handhabung von Deeplinks und Extras bleibt unverändert. Buttons mit `close`-Aktionen lösen keine `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`-Absichten aus und beenden die Benachrichtigung automatisch.
{% endalert %}

{% alert important %}
Erstellen Sie Ihren Listener für Push-Benachrichtigungen in `Application.onCreate`, um sicherzustellen, dass er getriggert wird, wenn auf eine Benachrichtigung getippt wird, während sich Ihre App in einem beendeten Zustand befindet.
{% endalert %}
