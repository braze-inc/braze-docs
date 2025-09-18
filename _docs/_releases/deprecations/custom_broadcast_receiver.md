---
nav_title: Push callback broadcast receiver
article_title: Custom Broadcast Receiver Push Callback for Android
description: "This reference article covers creating a custom Broadcast Receiver for Android push notifications"
---

# Custom handling for push receipts, opens, dismissals, and key-value pairs via Broadcast Receiver {#android-push-listener-broadcast-receiver}

{% alert important %}
Using a custom `BroadcastReceiver` for push notifications has been deprecated. Use [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) instead.
{% endalert %}

Braze also broadcasts custom intents when push notifications are received, opened, or dismissed. If you have a specific use case for these scenarios (such as the need to listen for custom key-value pairs or proprietary handling of deep links), you will need to listen for these intents by creating a custom `BroadcastReceiver`.

## Step 1: Register your BroadcastReceiver

Register your custom `BroadcastReceiver` to listen for Braze push opened and received intents in your [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml):

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Step 2: Create Your BroadcastReceiver

Your receiver should handle intents broadcast by Braze and launch your activity with them:

- It should subclass [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) and override `onReceive()`.
- The `onReceive()` method should listen for intents broadcast by Braze.
  - A `NOTIFICATION_RECEIVED` intent will be received when a push notification arrives.
  - A `NOTIFICATION_OPENED` intent will be received when the user clicks a push notification.
  - An `NOTIFICATION_DELETED` intent will be received when a push notification is dismissed (swiped away) by the user.
- It should perform your custom logic for each of these cases. If your receiver will open deep links, be sure to turn off automatic deep link opening by setting `com_braze_handle_push_deep_links_automatically` to `false` in your `braze.xml`.

For a detailed custom receiver example, see the following code snippets:

{% tabs %}
{% tab JAVA %}

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
{% tab KOTLIN %}

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
With notification action buttons, `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents fire when buttons with `opens app` or `deep link` actions are clicked. Deep link and extras handling remains the same. Buttons with `close` actions don't fire `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents and dismiss the notification automatically.
{% endalert %}

## Step 3: Access custom key-value pairs

Custom key-value pairs sent either via the dashboard or the messaging APIs will be accessible in your custom broadcast receiver for whatever purpose you choose:

{% tabs %}
{% tab JAVA %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab KOTLIN %}

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
For documentation on Braze push data keys, refer to the [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

