---
nav_title: Live Updates für Android
article_title: Live Updates für das Android Braze SDK
page_order: 0.1
description: "Erfahren Sie, wie Sie Live Updates für das Android Braze SDK einrichten."
platform: 
  - Android
  - FireOS
---

# Live Updates für Android

> Lernen Sie, wie Sie Android Live Updates im Braze SDK verwenden, auch bekannt als [Progress Centric Notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Diese Benachrichtigungen ähneln den [Live-Aktivitäten für das Swift Braze SDK]({{site.baseurl}}/developer_guide/live_notifications/live_activities) und erlauben es Ihnen, interaktive Sperrbildschirm-Benachrichtigungen anzuzeigen. Android 16 führt fortschrittsorientierte Benachrichtigungen ein, mit denen Nutzer:innen nahtlos das Tracking der vom Benutzer initiierten End-to-End-Reise verfolgen können.

## Funktionsweise

Sie können über die [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) Schnittstelle anpassen, wie die Push-Benachrichtigungen von Braze angezeigt werden. Durch die Erweiterung von `BrazeNotificationFactory` ruft Braze die Methode `createNotification()` Ihrer Fabrik auf, bevor die Benachrichtigung dem Nutzer:innen angezeigt wird. Es wird dann eine Nutzlast übergeben, die angepasste Schlüssel-Wert-Paare enthält, die über das Braze-Dashboard oder die REST API gesendet werden.

## Ein Live Update anzeigen

In diesem Abschnitt werden Sie Partner von Superb Owl, dem Moderator einer neuen Spielshow, in der Teams zur Rettung von Wildtieren gegeneinander antreten, um zu sehen, wer die meisten Eulen retten kann. Sie möchten Live Updates in ihrer Android App nutzen, um den Status eines laufenden Spiels anzuzeigen und dynamische Updates der Benachrichtigung in Echtzeit vorzunehmen.

![Ein Beispiel für ein Live Update von Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Schritt 1: Angepasste Benachrichtigungs-Factory erstellen

Erstellen Sie in Ihrer Anwendung eine neue Datei namens `MyCustomNotificationFactory.kt`, die die [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) erweitert, um die Anzeige von Braze Live Updates zu steuern.

Im folgenden Beispiel hat Superb Owl eine angepasste Benachrichtigungsfabrik erstellt, um ein Live Update für laufende Spiele anzuzeigen. Im nächsten Schritt erstellen Sie eine neue Methode namens `getTeamInfo`, um die Daten eines Teams der Aktivität zuzuordnen.

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### Schritt 2: Angepasste Daten abbilden

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

### Schritt 3: Die angepasste Benachrichtigungsfabrik einstellen

Verwenden Sie in Ihrer Anwendungsklasse [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)um Ihre angepasste Benachrichtigungsfabrik einzustellen.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Schritt 4: Senden Sie die Aktivität

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
| `ASSIGNED_NOTIFICATION_ID`   | Die ID der Benachrichtigung, die Sie der Live-Benachrichtigung des gewählten Nutzers:innen zuweisen möchten. Die ID muss für dieses Spiel eindeutig sein und muss verwendet werden, um [ihre bestehende Benachrichtigung später zu aktualisieren](#android_step-4-update-data-with-the-braze-rest-api). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 5: Aktivität aktualisieren

Um das vorhandene Live Update mit neuen Daten zu aktualisieren, ändern Sie die entsprechenden Schlüssel-Wert-Paare, die `messages.extra` zugewiesen sind, verwenden Sie dann dieselbe `notification_id` und rufen Sie den Endpunkt `/messages/send` erneut auf.
