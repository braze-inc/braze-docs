---
nav_title: Push-Rückruf-Rundfunkempfänger
article_title: Benutzerdefinierter Broadcast-Empfänger Push Callback für Android
description: "Dieser Referenzartikel behandelt die Erstellung eines benutzerdefinierten Broadcast-Empfängers für Android-Push-Benachrichtigungen"
---

# Benutzerdefinierte Handhabung für Push-Empfang, Öffnen, Verwerfen und Schlüssel-Wert-Paare über Broadcast Receiver {#android-push-listener-broadcast-receiver}

{% alert important %}
Die Verwendung eines benutzerdefinierten `BroadcastReceiver` für Push-Benachrichtigungen ist nicht mehr sinnvoll. Verwenden Sie stattdessen [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/) stattdessen.
{% endalert %}

Braze sendet auch benutzerdefinierte Intents, wenn Push-Benachrichtigungen empfangen, geöffnet oder verworfen werden. Wenn Sie einen speziellen Anwendungsfall für diese Szenarien haben (wie z.B. die Notwendigkeit, auf benutzerdefinierte Schlüssel-Wert-Paare oder die proprietäre Behandlung von Deep Links zu achten), müssen Sie auf diese Intents achten, indem Sie ein benutzerdefiniertes `BroadcastReceiver` erstellen.

## Schritt 1 Registrieren Sie Ihren BroadcastReceiver

Registrieren Sie Ihre benutzerdefinierte `BroadcastReceiver`, um auf die geöffneten und empfangenen Push-Intents von Braze in Ihrem [`AndroidManifest.xml`][71]:

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Schritt 2 Erstellen Sie Ihren BroadcastReceiver

Ihr Empfänger sollte die von Braze gesendeten Intents verarbeiten und Ihre Aktivität mit ihnen starten:

- Sie sollte die Unterklasse [`BroadcastReceiver`][53] untergliedern und `onReceive()` außer Kraft setzen.
- Die Methode `onReceive()` sollte auf die von Braze gesendeten Intents warten.
  - Eine `NOTIFICATION_RECEIVED` Absicht wird empfangen, wenn eine Push-Benachrichtigung eintrifft.
  - Eine `NOTIFICATION_OPENED` Absicht wird empfangen, wenn der Benutzer auf eine Push-Benachrichtigung klickt.
  - Eine `NOTIFICATION_DELETED` Absicht wird empfangen, wenn eine Push-Benachrichtigung vom Benutzer zurückgewiesen (weggewischt) wird.
- Es sollte Ihre eigene Logik für jeden dieser Fälle ausführen. Wenn Ihr Empfänger Deep Links öffnet, stellen Sie sicher, dass Sie das automatische Öffnen von Deep Links deaktivieren, indem Sie `com_braze_handle_push_deep_links_automatically` auf `false` in Ihrem `braze.xml` einstellen.

Ein ausführliches Beispiel für einen benutzerdefinierten Empfänger finden Sie in den folgenden Codeschnipseln:

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
Bei Schaltflächen mit Benachrichtigungsaktionen wird `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` ausgelöst, wenn Schaltflächen mit den Aktionen `opens app` oder `deep link` angeklickt werden. Die Handhabung von Deep Links und Extras bleibt unverändert. Schaltflächen mit `close` Aktionen lösen keine `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` Intents aus und schließen die Benachrichtigung automatisch.
{% endalert %}

## Schritt 3: Zugriff auf benutzerdefinierte Schlüssel-Werte-Paare

Benutzerdefinierte Schlüssel-Wert-Paare, die entweder über das Dashboard oder die Nachrichten-APIs gesendet werden, sind in Ihrem benutzerdefinierten Broadcast-Empfänger für den von Ihnen gewünschten Zweck zugänglich:

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
Die Dokumentation zu den Braze Push-Daten-Tasten finden Sie im [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

[53]: https://developer.android.com/reference/android/content/BroadcastReceiver.html
[71]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml "AndroidManifest.xml"
