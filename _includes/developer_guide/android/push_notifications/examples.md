{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Custom notification layout

Braze notifications are sent as [data messages](https://firebase.google.com/docs/cloud-messaging/concept-options), which means that your application will always have a chance to respond and perform behavior accordingly, even in the background (in contrast to notification messages, which can be handled automatically by the system when your app is in the background). As such, your application will have a chance to customize the experience by, for example displaying personalized UI elements within the notification delivered to the notification tray. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of using custom view components to create an engaging experience!

{% alert important %}
Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.
{% endalert %}

You can use the [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interface to customize how Braze push notifications are displayed. By extending `BrazeNotificationFactory`, Braze will call your factory's `createNotification()` method before the notification is displayed to the user. It will then pass a payload containing custom key-value pairs sent through the Braze dashboard or REST API.

In this section, you'll partner with Superb Owl, the host of a new game show where wildlife rescue teams compete to see who can save the most owls. They're looking to leverage live updating notifications in their Android app, so they can display the status of an on-going match and make dynamic updates to the notification in realtime.

![The Live Update that Superb Owl wants to show, displaying an on-going match between 'Wild Bird Fund' and 'Owl Rescue'. It's currently the fourth quarter and the score is 2-4 with OWL in the lead.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### Step 1: Add a custom layout

You can add one or more custom notification RemoteView layouts to your project. These are helpful for handling how notifications are displayed when collapsed or expanded. Your directory structure should be similar to the following:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

In each XML file, create a custom layout. Superb Owl created the following layouts for their collapsed and expanded RemoteView layouts:

{% tabs local %}
{% tab  Example: Collapsed layout %}
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

{% tab Example: Expanded layout %}
{% details Show the sample code %}
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

### Step 2: Create a custom notification factory

In your application, create a new file named `MyCustomNotificationFactory.kt` that extends [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) to handle how custom RemoteView layouts are displayed.

In the following example, Superb Owl created a custom notification factory to display a RemoteView layout for on-going matches. In the [next step](#android_step-3-map-custom-data), they'll create a new method called `getTeamInfo` to map a team's data to the activity.

{% details Show the sample code %}
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

### Step 3: Map custom data

In `MyCustomNotificationFactory.kt`, create a new method for handling data when Live Updates are displayed.

Superb Owl created the following method to map each team's name and logo to expanded Live Updates:

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

### Step 4: Set the custom notification factory

In your application class, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)to set your custom notification factory.

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

### Step 5: Send the activity

You can use the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API endpoint to send a push notification to a user's Android device.

#### Example curl command

Superb Owl sent their request using the following curl command:

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
While curl commands are helpful for testing, we recommend handling this call in your backend where you're already handling your [iOS Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Request parameters

| Key                           | Description                                                                                                                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | A Braze REST API key with `messages.send` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**.                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints).                                                                                                                  |
| `USER_ID`                     | The ID of the user you are sending the notification to.                                                                                                                                                                                          |
| `messages.android_push.title` | The message's title. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback.                                                                                                    |
| `messages.android_push.alert` | The message's body. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback.                                                                                                     |
| `messages.extra`              | Key-value pairs that the custom notification factory uses for live notifications. You can assign any string to this value&#8212;however, in the example above, `live_updates` is used to determine if it's a default or live push notification.  |
| `ASSIGNED_NOTIFICATION_ID`    | The notification ID you want to assign to the chosen user's live notification. The ID must be unique to this game, and must be used in order to [update their existing notification](#android_step-4-update-data-with-the-braze-rest-api) later. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 6: Update the activity

To update the existing RemoteView notification with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the `/messages/send` endpoint again.

## Personalized push notifications

Push notifications can display user-specific information inside a custom view hierarchy. In the following example, an API-trigger is used to send personalized push notification to a user so they can track check their current progress after completing a specific task in the app.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

To set up a personalized push in the dashboard, register the specific category you want to be displayed, then set any relevant user attributes you'd like to display using Liquid.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
