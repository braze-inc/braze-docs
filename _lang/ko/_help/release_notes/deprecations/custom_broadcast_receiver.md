---
nav_title: 푸시 콜백 브로드캐스트 수신기
article_title: Android용 사용자 지정 방송 수신기 푸시 콜백
description: "이 참조 문서에서는 Android 푸시 알림을 위한 커스텀 브로드캐스트 수신기 만들기에 대해 설명합니다."
---

# 브로드캐스트 수신기를 통한 푸시 수신, 열기, 해지 및 키-값 페어에 대한 커스텀 처리 {#android-push-listener-broadcast-receiver}

{% alert important %}
푸시 알림에 사용자 지정 `BroadcastReceiver` 사용은 더 이상 사용되지 않습니다. 대신 [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) 대신 사용하세요.
{% endalert %}

또한 Braze는 푸시 알림을 수신, 열거나 해제할 때 커스텀 의도를 브로드캐스트합니다. 이러한 시나리오에 대한 특정 사용 사례(예: 커스텀 키-값 페어를 수신해야 하거나 딥링크를 독점적으로 처리해야 하는 경우)가 있는 경우 커스텀 `BroadcastReceiver`를 생성하여 이러한 의도를 수신해야 합니다.

## 1단계: BroadcastReceiver 등록하기

커스텀 `BroadcastReceiver`를 등록하여 [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml)에서 Braze 푸시 열기 및 수신 의도를 수신하기 위한 조건:

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## 2단계: BroadcastReceiver 만들기

수신기는 Braze가 브로드캐스트한 의도를 처리하고 활동을 시작해야 합니다:

- [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) 하위크래스에 포함하고 `onReceive()`를 재정의해야 합니다.
- `onReceive()` 메서드는 Braze가 브로드캐스트하는 인텐트를 수신해야 합니다.
  - 푸시 알림이 도착하면 `NOTIFICATION_RECEIVED` 인텐트가 수신됩니다.
  - 사용자가 푸시 알림을 클릭하면 `NOTIFICATION_OPENED` 인텐트가 수신됩니다.
  - 사용자가 푸시 알림을 해제(스와이프)하면 `NOTIFICATION_DELETED` 의도가 수신됩니다.
- 이러한 각 경우에 대해 커스텀 로직을 수행해야 합니다. 수신기가 딥링크를 열 경우 `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`를 `false`로 설정하여 자동 딥링크 열기를 해제해야 합니다.

자세한 사용자 지정 수신기 예제는 다음 코드 스니펫을 참조하세요:

{% tabs %}
{% tab 자바 %}

```java
public class CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class.getName();

  @Override
  public void onReceive(Context context, Intent intent) {
    String pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED;

    String action = intent.getAction();
    Log.d(TAG, String.format("Received intent with action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log.d(TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent.");
    } else {
      Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action));
    }
  }
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    val notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    val notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED

    val action = intent.action
    Log.d(TAG, String.format("Received intent with action %s", action))

    when (action) {
      pushReceivedAction -> {
        Log.d(TAG, "Received push notification.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action))
      }
    }
  }

  companion object {
    private val TAG = CustomBroadcastReceiver::class.java.name
  }
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
알림 실행 버튼의 경우 `opens app` 또는 `deep link` 동작이 있는 버튼을 클릭하면 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도가 실행됩니다. 딥링크 및 추가 처리 기능은 동일하게 유지됩니다. `close` 동작이 있는 버튼은 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도를 실행하지 않으며 알림을 자동으로 해제합니다.
{% endalert %}

## 3단계: 사용자 지정 키-값 쌍에 액세스

대시보드 또는 메시징 API를 통해 전송된 커스텀 키-값 페어는 원하는 목적에 따라 커스텀 생방송 수신기에서 액세스할 수 있습니다.

{% tabs %}
{% tab 자바 %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
// intent is the Braze push intent received by your custom broadcast receiver.
val deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY)

// The extras bundle extracted from the intent contains all custom key-value pairs.
val extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY)

// example of getting specific key-value pair from the extras bundle.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Braze 푸시 데이터 키에 대한 설명서는 [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants)를 참조하세요.
{% endalert %}

