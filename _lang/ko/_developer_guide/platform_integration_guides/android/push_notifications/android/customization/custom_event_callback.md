---
nav_title: 푸시 이벤트 콜백
article_title: Android용 푸시 이벤트 콜백
platform: Android
page_order: 50
description: "이 참조 문서에서는 Android 푸시 이벤트에 콜백을 사용하는 방법을 다룹니다."
channel:
  - push

---

# 푸시 이벤트 콜백 {#android-push-listener-callback}

> 이 참조 문서에서는 Android 푸시 이벤트에 콜백을 사용하는 방법에 대해 설명합니다.

Braze는 푸시 알림을 수신하거나 열람하거나 해제하는 경우에 대한 [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) 콜백을 제공합니다. 애플리케이션이 실행되지 않는 동안 발생하는 이벤트를 놓치지 않도록 `Application.onCreate()`에 이 콜백을 배치하는 것이 좋습니다.

{% alert note %}
이전에 애플리케이션에서 이 기능을 위해 사용자 지정 생방송 수신기를 사용했다면 이 통합 옵션을 위해 해당 수신기를 안전하게 제거할 수 있습니다.
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
알림 실행 버튼의 경우 `opens app` 또는 `deep link` 동작이 있는 버튼을 클릭하면 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도가 실행됩니다. 딥링크 및 추가 항목 처리 기능은 동일하게 유지됩니다. `close` 동작이 있는 버튼은 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도를 실행하지 않으며 알림을 자동으로 해제합니다.
{% endalert %}

{% alert important %}
`Application.onCreate` 에서 푸시 알림 리스너를 생성하여 최종 사용자가 앱이 종료된 상태에서 알림을 탭하면 리스너가 트리거되도록 하세요.
{% endalert %}
