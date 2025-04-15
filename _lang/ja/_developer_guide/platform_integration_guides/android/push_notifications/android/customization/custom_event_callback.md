---
nav_title: プッシュイベントコールバック
article_title: Android 向けプッシュイベントコールバック
platform: Android
page_order: 50
description: "このリファレンス記事では、Android プッシュイベントにコールバックを使用する方法について説明します。"
channel:
  - push

---

# プッシュイベントコールバック {#android-push-listener-callback}

> このリファレンス記事では、Android プッシュイベントにコールバックを使用する方法について説明します

Braze には、プッシュ通知が受信されたとき、開かれたとき、または却下されたときのための [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) コールバックが用意されています。アプリケーションが実行されていないときに発生するイベントを見逃さないように、このコールバックを `Application.onCreate()` に配置することをお勧めします。

{% alert note %}
以前にアプリケーションでこの機能にカスタムブロードキャストレシーバーを使用していた場合は、この統合オプションを優先して、レシーバーを削除しても問題ありません。
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
通知アクションボタンを使用すると、`opens app` または `deep link` アクションを持つボタンがクリックされると、`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントが起動します。ディープリンクとエクストラの処理は変わりません。`close` アクション付きのボタンは `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントを起動せず、通知を自動的に閉じます。
{% endalert %}

{% alert important %}
`Application.onCreate` でプッシュ通知リスナーを作成し、アプリが終了状態にある間にエンドユーザーが通知をタップした後にリスナーがトリガーされるようにします。
{% endalert %}
