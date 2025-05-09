---
nav_title: Live Updates für Android
article_title: Live-Aktivitäten für das Android Braze SDK
page_order: 0.1
description: "Erfahren Sie, wie Sie Live-Aktivitäten für das Android Braze SDK einrichten."
platform: 
  - Android
  - FireOS
---

# Live-Aktivitäten für Android

> Lernen Sie, wie Sie Live Updates im Android Braze SDK emulieren können. Obwohl Live Updates nicht offiziell unterstützt werden, zeigt Ihnen diese Anleitung, wie Sie ihr Verhalten emulieren können, so dass Sie interaktive Sperrbildschirm-Benachrichtigungen ähnlich wie [Live Activities für das Swift Braze SDK]({{site.baseurl}}/developer_guide/live_notifications/live_activities) anzeigen können. Im Gegensatz zu offiziellen Live Updates kann diese Funktion auch für ältere Android-Versionen implementiert werden.

## Funktionsweise

Sie können über die [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) Schnittstelle anpassen, wie die Push-Benachrichtigungen von Braze angezeigt werden. Durch die Erweiterung von `BrazeNotificationFactory` ruft Braze die Methode `createNotification()` Ihrer Fabrik auf, bevor die Benachrichtigung dem Nutzer:innen angezeigt wird. Es wird dann eine Nutzlast übergeben, die angepasste Schlüssel-Wert-Paare enthält, die über das Braze-Dashboard oder die REST API gesendet werden.

## Emulation eines Live Updates

{% alert important %}
Live Updates werden vom Android Betriebssystem nicht nativ unterstützt. Der folgende Abschnitt zeigt Ihnen nur, wie Sie deren allgemeines Verhalten nachahmen können.
{% endalert %}

In diesem Abschnitt werden Sie Partner von Superb Owl, dem Moderator einer neuen Spielshow, in der Teams zur Rettung von Wildtieren gegeneinander antreten, um zu sehen, wer die meisten Eulen retten kann. Sie möchten Live Updates in ihrer Android App nutzen, um den Status eines laufenden Spiels anzuzeigen und dynamische Updates der Benachrichtigung in Echtzeit vorzunehmen.

![Das Live Update, das Superb Owl machen will, zeigt ein laufendes Spiel zwischen 'Wild Bird Fund' und 'Owl Rescue'. Es ist das vierte Viertel und der Spielstand ist 2:4, wobei OWL in Führung liegt.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Schritt 1: Ein angepasstes Layout hinzufügen

Sie können ein oder mehrere angepasste Live Update-Layouts zu Ihrem Projekt hinzufügen. Diese sind hilfreich bei der Handhabung, wie Benachrichtigungen angezeigt werden, wenn sie eingeklappt oder ausgeklappt sind. Ihre Verzeichnisstruktur sollte in etwa so aussehen wie die folgende:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

Erstellen Sie in jeder XML-Datei ein angepasstes Layout. Superb Owl hat die folgenden Layouts für ihre zusammengeklappten und erweiterten Live Updates erstellt:

{% tabs local %}
{% tab  Beispiel: Zusammengeklapptes Layout %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

Beispiel: {% tab  Erweitertes Layout %}
{% details Zeigen Sie den Beispielcode %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### Schritt 2: Angepasste Benachrichtigungs-Factory erstellen

Erstellen Sie in Ihrer Anwendung eine neue Datei namens `MyCustomNotificationFactory.kt`, die die [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) erweitert, um die Anzeige von Braze Live Updates zu steuern.

Im folgenden Beispiel hat Superb Owl eine angepasste Benachrichtigungsfabrik erstellt, um ein Live Update für laufende Spiele anzuzeigen. Im [nächsten Schritt](#android_step-3-map-custom-data) erstellen Sie eine neue Methode namens `getTeamInfo`, um die Daten eines Teams auf die Aktivität abzubilden.

{% details Zeigen Sie den Beispielcode %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### Schritt 3: Angepasste Daten abbilden

Erstellen Sie in `MyCustomNotificationFactory.kt` eine neue Methode zur Behandlung von Daten, wenn Live Updates angezeigt werden.

Superb Owl hat die folgende Methode entwickelt, um den Namen und das Logo eines jeden Teams den erweiterten Live Updates zuzuordnen:

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### Schritt 4: Die angepasste Benachrichtigungsfabrik einstellen

Verwenden Sie in Ihrer Anwendungsklasse [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)um Ihre angepasste Benachrichtigungsfabrik einzustellen.

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Schritt 5: Senden Sie die Aktivität

Sie können den [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API Endpunkt verwenden, um eine Push-Benachrichtigung an das Android Gerät eines Nutzers:innen zu senden.

#### Beispiel curl-Befehl

Superb Owl hat seine Anfrage mit dem folgenden curl-Befehl gesendet:

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
Auch wenn curl-Befehle für Tests hilfreich sind, empfehlen wir, diesen Aufruf in Ihrem Backend zu erledigen, wo Sie bereits Ihre [iOS Live-Aktivitäten]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) verwalten.
{% endalert %}

#### Parameter der Anfrage

| Schlüssel                          | Beschreibung |
|------------------------------|------------|
| `REST_API_KEY`               | Ein Braze REST API-Schlüssel mit `messages.send` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| `BRAZE_REST_ENDPOINT`         | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| `USER_ID`                    | Die ID des Nutzers:innen, an den Sie die Benachrichtigung senden. |
| `messages.android_push.title` | Der Titel der Nachricht. Standardmäßig wird dies nicht für die Live-Benachrichtigungen der angepassten Benachrichtigungsfabrik verwendet, aber es kann als Fallback verwendet werden. |
| `messages.android_push.alert` | Der Text der Nachricht. Standardmäßig wird dies nicht für die Live-Benachrichtigungen der angepassten Benachrichtigungsfabrik verwendet, aber es kann als Fallback verwendet werden. |
| `messages.extra`             | Schlüssel-Wert-Paare, die die angepasste Benachrichtigungsfabrik für Live-Benachrichtigungen verwendet. Sie können diesem Wert einen beliebigen String zuweisen. Im obigen Beispiel wird jedoch `live_updates` verwendet, um festzustellen, ob es sich um eine Standard- oder eine Live-Push-Benachrichtigung handelt. |
| `ASSIGNED_NOTIFICATION_ID`   | Die ID der Benachrichtigung, die Sie der Live-Benachrichtigung des gewählten Nutzers:innen zuweisen möchten. Die ID muss für dieses Spiel eindeutig sein und muss verwendet werden, um [ihre bestehende Benachrichtigung](#android_step-4-update-data-with-the-braze-rest-api) später [zu aktualisieren](#android_step-4-update-data-with-the-braze-rest-api). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 6: Aktivität aktualisieren

Um das vorhandene Live Update mit neuen Daten zu aktualisieren, ändern Sie die entsprechenden Schlüssel-Wert-Paare, die `messages.extra` zugewiesen sind, verwenden Sie dann dieselbe `notification_id` und rufen Sie den Endpunkt `/messages/send` erneut auf.
