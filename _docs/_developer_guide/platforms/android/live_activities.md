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

![ALT_TEXT]()

Live Activities present a combination of static information and dynamic information that you update. For example, you can create a Live Activity that provides a status tracker for a delivery. This Live Activity would have your company's name as static information, as well as a dynamic "Time to delivery" that would be updated as the delivery driver approaches its destination.

As a developer, you can use Braze to manage your Live Activity lifecycles, make calls to the Braze REST API to make Live Activity updates, and have all subscribed devices receive the update as soon as possible. And, because you're managing Live Activities through Braze, you can use them in tandem with your other messaging channels&mdash;push notifications, in-app messages, Content Cards&mdash;to drive adoption.

## Prerequisites 

_$TODO_

## Implementing a Live Activity

### Step 1: Add configuration files

Open your terminal and clone the [$TODO-REPOSITORY-LINK]():

```bash
git clone git@github.com:braze-inc/$TODO.git
```

Move the following files to your Android project:

- Place [`FullyCustomNotificationFactory.kt`]() in your application.
- Place [`liveupdate_large.xml`]() and [`liveupdate_small.xml`]() in your layout resources.

Your directory structure should be similar to the following:

```plaintext
Your-Android-Project/
├── app/
│   └── src/
│       └── main/
│           └── java/
│               └── com/
│                   └── yourcompany/
│                       └── yourapp/
│                           └── FullyCustomNotificationFactory.kt
└── res/
    └── layout/
        ├── liveupdate_large.xml
        └── liveupdate_small.xml
```

In _$TODO_, update `FullyCustomNotificationFactory.getTeamInfo()` to return the drawables already being used in your app.

{% tabs %}
{% tab Java %}
```java
$TODO
```
{% endtab %}
{% tab Kotlin %}
```kotlin
$TODO
```
{% endtab %}
{% endtabs %}

### Step 2: Set the custom notification factory

In _$TODO_, add the [`customBrazeNotificationFactory` method](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) to your application class.

{% tabs %}
{% tab Java %}
```java
// Set the custom notification factory
$TODO
```
{% endtab %}
{% tab Kotlin %}
```kotlin
// Set the custom notification factory
Braze.customBrazeNotificationFactory = FullyCustomNotificationFactory()
```
{% endtab %}
{% endtabs %}

### Step 3: Call the `/messages/send` endpoint

The following curl command uses the [`/messages/send` endpoint](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages) to deliver a push notification to the chosen user's Android device. While curl commands are helpful for testing, we recommend handling this call in your backend where you already handle your [iOS Live Activities]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/).

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

### Step 4: Update the activity

To update the existing Live Activity with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the [`/messages/send` endpoint](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages) again.
