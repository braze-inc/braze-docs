---
nav_title: Push Callback Rundfunkempfänger
article_title: Angepasster Broadcast-Empfänger Push Callback für Android
description: "Dieser referenzierte Artikel behandelt die Erstellung eines angepassten Broadcast-Empfängers für Push-Benachrichtigungen unter Android."
---

# Angepasste Behandlung von Push-Eingängen, Öffnungen, Entlassungen und Schlüssel-Wert-Paaren über Broadcast Receiver {#android-push-listener-broadcast-receiver}

{% alert important %}
Die Verwendung eines angepassten `BroadcastReceiver` für Push-Benachrichtigungen ist nicht mehr zeitgemäß. Verwenden Sie stattdessen [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) stattdessen.
{% endalert %}

Braze sendet auch angepasste Absichten, wenn Push-Benachrichtigungen empfangen, geöffnet oder abgelehnt werden. Wenn Sie einen speziellen Anwendungsfall für diese Szenarien haben (z.B. die Notwendigkeit, auf angepasste Schlüssel-Wert-Paare oder proprietäre Handhabung von Deeplinks zu achten), müssen Sie auf diese Absichten achten, indem Sie eine angepasste `BroadcastReceiver` erstellen.

## Schritt 1: Registrieren Sie Ihren BroadcastReceiver

Registrieren Sie Ihre angepasste `BroadcastReceiver`, um auf geöffnete und empfangene Push-Absichten von Braze in Ihrem [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml):

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Schritt 2: Erstellen Sie Ihren BroadcastReceiver

Ihr Empfänger sollte die von Braze gesendeten Absichten verarbeiten und Ihre Aktivität mit ihnen starten:

- Sie sollte die Unterklasse [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) untergliedern und `onReceive()` außer Kraft setzen.
- Die Methode `onReceive()` sollte auf von Braze gesendete Absichten warten.
  - Eine `NOTIFICATION_RECEIVED` Absicht wird empfangen, wenn eine Push-Benachrichtigung eintrifft.
  - Eine `NOTIFICATION_OPENED` Absicht wird empfangen, wenn der Nutzer:innen auf eine Push-Benachrichtigung klickt.
  - Eine `NOTIFICATION_DELETED` Absicht wird empfangen, wenn eine Push-Benachrichtigung vom Nutzer:innen zurückgewiesen (weggewischt) wird.
- Es sollte Ihre angepasste Logik für jeden dieser Fälle ausführen. Wenn Ihr Empfänger Deeplinks öffnet, stellen Sie sicher, dass Sie das automatische Öffnen von Deeplinks deaktivieren, indem Sie `com_braze_handle_push_deep_links_automatically` auf `false` in Ihrem `braze.xml` einstellen.

Ein ausführliches Beispiel für einen angepassten Empfänger finden Sie in den folgenden Code-Snippets:

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
Bei Aktions-Buttons für Benachrichtigungen werden die `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` Absichten ausgelöst, wenn Buttons mit den Aktionen `opens app` oder `deep link` angeklickt werden. Die Handhabung von Deeplinks und Extras bleibt unverändert. Buttons mit `close`-Aktionen lösen keine `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`-Absichten aus und beenden die Benachrichtigung automatisch.
{% endalert %}

## Schritt 3: Zugriff auf angepasste Schlüssel-Wert-Paare

Angepasste Schlüssel-Wert-Paare, die entweder über das Dashboard oder die Messaging APIs gesendet werden, sind in Ihrem angepassten Broadcast-Empfänger für den von Ihnen gewählten Zweck zugänglich:

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
Die Dokumentation zu den Push-Daten von Braze finden Sie im [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

