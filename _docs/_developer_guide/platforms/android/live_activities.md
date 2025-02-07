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

Live Activities present a combination of static information and dynamic information that you update. For example, you can create a Live Activity that provides a status tracker for a delivery. This Live Activity would have your company's name as static information, as well as a dynamic "Time to delivery" that would be updated as the delivery driver approaches its destination.

As a developer, you can use Braze to manage your Live Activity lifecycles, make calls to the Braze REST API to make Live Activity updates, and have all subscribed devices receive the update as soon as possible. And, because you're managing Live Activities through Braze, you can use them in tandem with your other messaging channels&mdash;push notifications, in-app messages, Content Cards&mdash;to drive adoption.

## About `IBrazeNotificationFactory`

You can use the [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interface to customize how Braze push notifications are displayed.

If you extend `BrazeNotificationFactory`, Braze will call your factory's `createNotification()` method before the notification is displayed to the user. It will then pass one `Bundle` containing Braze push data and another `Bundle` containing custom key-value pairs sent through the Braze dashboard or REST API.

## Implementing a Live Activity

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Step 1: Add a custom layout

You can add one or more custom Live Activity layouts to your project. These are helpful for handling how notifications are displayed when collapsed or expanded. Your directory structure should be similar to the following:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_expanded.xml
        └── liveupdate_collapsed.xml
```

In your XML file, create your custom layout. For example, in `liveupdate_expanded.xml`: 

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
            android:src="@drawable/team_wbf"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Team 1 Name" />

    </LinearLayout>
</LinearLayout>
```

### Step 2: Create a custom notification factory

In your application, create a new file named `MyCustomNotificationFactory.kt` that extends [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html), handling how your Braze Live Activities are displayed.

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
            val team1 = data["team1"]
            val team2 = data["team2"]
            val score1 = data["score1"]
            val score2 = data["score2"]
            val time = data["time"]
            val half = data["half"]

            // Set up collapsed and expanded layouts
            val collapsedLayout = RemoteViews(context.packageName, R.layout.liveupdate_collapsed)
            val expandedLayout = RemoteViews(context.packageName, R.layout.liveupdate_expanded)

            // Updating the collapsed layout text
            collapsedLayout.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $half"
            )

            // Updating the expanded layout with more details
            expandedLayout.setTextViewText(R.id.notification_title, "$team1 vs $team2")
            expandedLayout.setTextViewText(R.id.details, "$score1 - $score2 • $time $half")

            // Build and return the Live Activity notification
            return NotificationCompat.Builder(context, channelId)
                .setSmallIcon(R.drawable.notification_icon_collapsed)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(collapsedLayout)
                .setCustomBigContentView(expandedLayout)
                .build()
        }

        // Otherwise, fall back to the default Braze notification handling
        return super.createNotification(payload)
    }
}
```

### Step 3: Define custom data handling

In `MyCustomNotificationFactory.kt`, create a new method for handling data when Live Activities are displayed. In the following example, `getTeamInfo` is used to map the team's name and logo when the Live Activity is expanded. 

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

### Step 5: Call the `/messages/send` endpoint

The following curl command uses the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API endpoint to deliver a push notification to the chosen user's Android device.

{% alert tip %}
While curl commands are helpful for testing, we recommend handling this call in your backend where you're already handling your [iOS Live Activities]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/).
{% endalert %}

#### Example curl command

```bash
curl -X POST "https://BRAZE_REST_ENPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
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
| `REST_API_KEY`               | A Braze REST API key with `$TODO` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| `BRAZE_REST_ENPOINT`         | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints). |
| `USER_ID`                    | The ID of the user you are sending the notification to. |
| `messages.android_push.title` | The message's title. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.android_push.alert` | The message's body. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback. |
| `messages.extra`             | Key-value pairs that the custom notification factory uses for live notifications. You can assign any string to this value&#8212;however, in the example above, `live_updates` is used to determine if it's a default or live push notification. |
| `ASSIGNED_NOTIFICATION_ID`   | The notification ID you want to assign to the chosen user's live notification. The ID must be unique to this game, and must be used in order to [update their existing notification](#step-4-update-data-with-the-braze-rest-api) later. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 6: Update the activity

To update the existing Live Activity with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the `/messages/send` endpoint again.
