---
nav_title: Push Event Callback
article_title: Push Event Callback for Android
platform: Android
page_order: 50
description: "This reference article covers how to use a callback for Android push events."
channel:
  - push

---

# Push event callback {#android-push-listener-callback}

> This reference article covers how to use a callback for Android push events

Braze provides a [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) callback for when push notifications are received, opened, or dismissed. It is recommended to place this callback in your `Application.onCreate()` in order to not miss any events occurring while your application is not running.

{% alert note %}
If previously using a Custom Broadcast Receiver for this functionality in your application, you can safely remove it in favor of this integration option.
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
With notification action buttons, `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents fire when buttons with `opens app` or `deep link` actions are clicked. Deep link and extras handling remains the same. Buttons with `close` actions don't fire `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents and dismiss the notification automatically.
{% endalert %}

{% alert tip %}
If you want your push notification listener to be triggered upon clicking on a notification while in the terminated state, you should create your listener in `Application.onCreate`. This will ensure that the listener is set up prior to processing the push click.
{% endalert %}
