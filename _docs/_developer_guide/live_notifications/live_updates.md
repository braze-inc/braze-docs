---
nav_title: Live updates for Android
article_title: Live Updates for the Android Braze SDK
page_order: 0.1
description: "Learn how to set up Live Updates for the Android Braze SDK."
platform: 
  - Android
  - FireOS
---

# Live Updates for Android

> Learn how to use Android Live Updates in the Braze SDK, also known as [Progress Centric Notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications). These notifications are similar to [Live Activities for the Swift Braze SDK]({{site.baseurl}}/developer_guide/live_notifications/live_activities), allowing you to display interactive lock-screen notifications. Android 16 introduces progress-centric notifications to help users seamlessly track user-initiated, start-to-end journeys.

## How it works

You can use the [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interface to customize how Braze push notifications are displayed. By extending `BrazeNotificationFactory`, Braze will call your factory's `createNotification()` method before the notification is displayed to the user. It will then pass a payload containing custom key-value pairs sent through the Braze dashboard or REST API.

## Displaying a Live Update

In this section, you'll partner with Superb Owl, the host of a new game show where wildlife rescue teams compete to see who can save the most owls. They're looking to leverage Live Updates in their Android app, so they can display the status of an on-going match and make dynamic updates to the notification in realtime.

![An example Live Update from Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Step 1: Create a custom notification factory

In your application, create a new file named `MyCustomNotificationFactory.kt` that extends [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) to handle how Braze Live Updates are displayed.

In the following example, Superb Owl created a custom notification factory to display a Live Update for on-going matches. In the next step, you'll create a new method called `getTeamInfo` to map a team's data to the activity.

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

### Step 2: Map custom data

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

### Step 3: Set the custom notification factory

In your application class, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)to set your custom notification factory.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Step 4: Send the activity

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

| Key                          | Description |
|------------------------------|------------|
| `REST_API_KEY`               | A Braze REST API key with `messages.send` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| `BRAZE_REST_ENDPOINT`         | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints). |
| `USER_ID`                    | The ID of the user you are sending the notification to. |
| `messages.android_push.title` | The message's title. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.android_push.alert` | The message's body. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.extra`             | Key-value pairs that the custom notification factory uses for live notifications. You can assign any string to this value&#8212;however, in the example above, `live_updates` is used to determine if it's a default or live push notification. |
| `ASSIGNED_NOTIFICATION_ID`   | The notification ID you want to assign to the chosen user's live notification. The ID must be unique to this game, and must be used in order to [update their existing notification](#android_step-4-update-data-with-the-braze-rest-api) later. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 5: Update the activity

To update the existing Live Update with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the `/messages/send` endpoint again.
