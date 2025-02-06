---
nav_title: Live Activities
article_title: Live Activities for the Android Braze SDK
platform: Android
page_order: 6
description: "This article covers using Braze to manage your Live Activities tokens for the Android Braze SDK."

---

# Live Activities

> Live Activities are persistent, interactive notifications displayed on your lock screen, allowing you to keep an eye on things in real-time. Because they appear on the lock screen, Live Activities ensure that your notifications won't be missed. Because they're persistent, you can display up-to-date content to your users without even having them unlock their phone. 

## About Live Activities

![A delivery tracker live activity on an iPhone lockscreen. A status bar with a car is almost half-way filled up. Text reads "2 min until pickup"]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Live Activities present a combination of static information and dynamic information that you update. For example, you can create a Live Activity that provides a status tracker for a delivery. This Live Activity would have your company's name as static information, as well as a dynamic "Time to delivery" that would be updated as the delivery driver approaches its destination.

As a developer, you can use Braze to manage your Live Activity lifecycles, make calls to the Braze REST API to make Live Activity updates, and have all subscribed devices receive the update as soon as possible. And, because you're managing Live Activities through Braze, you can use them in tandem with your other messaging channels&mdash;push notifications, in-app messages, Content Cards&mdash;to drive adoption.

## About `IBrazeNotificationFactory`

You can use the [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interface to customize how Braze push notifications are displayed.

If you extend `IBrazeNotificationFactory`, Braze will call your factory's `createNotification()` method before the notification is displayed to the user. It will then pass one `Bundle` containing Braze push data and another `Bundle` containing custom key-value pairs sent through the Braze dashboard or REST API.

## Implementing a Live Activity

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Step 1: Add a custom layout

You can add one or more custom Live Activity layouts to your project. These are helpful for handling how notifications are displayed when collapsed or expanded. Your directory structure should be similar to the following:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_large.xml
        └── liveupdate_small.xml
```

In your XML file, create your custom layout. For example, in `liveupdate_small.xml`: 

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="8dp">

    <TextView
        android:id="@+id/notification_title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Live Activity Update"
        android:textStyle="bold"
        android:textSize="16sp" />
</LinearLayout>
```

### Step 2: Create a custom notification factory

In your application, create a new file named `MyCustomNotificationFactory.kt` that extends [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) and handles how your Braze Live Activities are displayed.

```kotlin
package com.appboy.sample

import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Check if this is a Live Activity update
        if (payload.extras.containsKey("live_update")) {
            val context = payload.context ?: return null
            val channelId = getOrCreateNotificationChannelId(payload)
            val data = payload.extras

            // Extract relevant data (e.g., the two teams, score, time)
            val team1 = data["team1"] ?: "WBF"
            val team2 = data["team2"] ?: "OWL"
            val score1 = data["score1"] ?: "0"
            val score2 = data["score2"] ?: "0"
            val time = data["time"] ?: "0:00"
            val quarter = data["quarter"] ?: "1st half"

            // Set up small (collapsed) and large (expanded) layouts
            val smallLayout = RemoteViews(context.packageName, R.layout.liveupdate_small)
            val largeLayout = RemoteViews(context.packageName, R.layout.liveupdate_large)

            // Example: updating the small layout text
            smallLayout.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            // Example: updating the large layout with more details
            largeLayout.setTextViewText(R.id.notification_title, "WBF vs OWL")
            largeLayout.setTextViewText(R.id.details, "$score1 - $score2 • $time $quarter")

            // Build and return the Live Activity notification
            return NotificationCompat.Builder(context, channelId)
                .setSmallIcon(R.drawable.ic_notification) // Replace with your icon
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(smallLayout)
                .setCustomBigContentView(largeLayout)
                .build()
        }

        // Otherwise, fall back to the default Braze notification handling
        return super.createNotification(payload)
    }
}
```

### Step 3: Create a method to retrieve data

In `MyCustomNotificationFactory.kt`, create a new method for retrieving relevant data or drawables when displaying a Live Activity.

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("WBF Wildlife Fund", R.drawable.nba_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.nba_owl)
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

### Step 5: Call the `/messages/send` endpoint

The following curl command uses the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API endpoint to deliver a push notification to the chosen user's Android device.

{% alert tip %}
While curl commands are helpful for testing, we recommend handling this call in your backend where you're already handling your [iOS Live Activities]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/).
{% endalert %}

#### Example curl command

```bash
curl -X POST "https://{BRAZE_REST_ENPOINT}/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["{USER_ID}"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 5:30 1st half",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "5:30",
          "quarter": "1st half"
        },
        "notification_id": ASSIGNED_NOTIFICATION_ID
      }
    }
  }'
```

#### Request parameters

| Key                          | Description |
|------------------------------|------------|
| `BRAZE_REST_ENPOINT`         | The REST endpoint that corresponds with your region; full list available [here](https://www.braze.com/docs/api/basics/#endpoints). |
| `REST_API_KEY`               | Your secret REST API key, available through your dashboard. |
| `USER_ID`                    | The ID of the user you want to send the notification to. |
| `messages.android_push.title` | The message's title. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.android_push.alert` | The message's body. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.extra`             | Key-value pairs that the custom notification factory uses for live notifications. You can assign any string to this value&#8212;however, in the example above, `live_updates` is used to determine if it's a default or live push notification. |
| `ASSIGNED_NOTIFICATION_ID`   | The notification ID you want to assign to that user's live notification. The ID must be unique to this game, and must be used in order to [update the existing notification](#step-4-update-data-with-the-braze-rest-api). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 6: Update the activity

To update the existing Live Activity with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the `/messages/send` endpoint again.
