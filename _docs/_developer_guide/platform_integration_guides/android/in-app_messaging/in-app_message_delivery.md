---
nav_title: In-App Message Delivery
article_title: In-App Message Delivery for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article covers Android and FireOS in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps."
channel:
  - in-app messages

---

# In-app message delivery

> This reference article covers Android and FireOS in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps.

## Trigger types

Our in-app message product allows you to trigger an in-app message display due to several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

{% alert note %}
Triggered in-app messages only work with custom events logged through the Braze SDK. In-app messages can't be triggered through the API or by API events (such as purchase events). Make sure to check out how to [log custom events]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/).
{% endalert %}

## Delivery semantics

All in-app messages that a user is eligible for are delivered to the user's device on the [session start][84]. Upon delivery, the SDK will prefetch assets to be available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

There can be some latency for in-app messages that display immediately on delivery (i.e., session start and push click) due to assets not being prefetched.

## Minimum time interval between triggers

By default, we rate limit in-app messages to once every 30 seconds to ensure a quality user experience.

To override this value, set `com_braze_trigger_action_minimum_time_interval_seconds` in your `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Server-side event triggering

By default, in-app messages are triggered by custom events logged by the SDK. If you want to trigger in-app messages by server-sent events, you can also achieve this.

To enable this feature, a silent push is sent to the device, which allows a custom push callback to log an SDK-based event. This SDK event will subsequently trigger the user-facing in-app message.

### Step 1: Create a Push Callback to Receive the Silent Push

Register your custom push callback to listen for a specific silent push notification. For more information, take a look at [Braze's push documentation][78].

Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom push callback. To make sure the same event is not duplicated, the event logged from within your push callback should follow a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done, segmentation and user data may be affected by duplicate events being logged for a single user action.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

### Step 2: Create a push campaign

Create a [silent push campaign][73] triggered via the server sent event.

![][75]

The push campaign must include key-value pair extras that indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![Two sets of key-value pairs: IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example campaign name".][76]{: style="max-width:70%;" }

The earlier push callback sample code recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your "in-app message trigger" event, you can achieve this by passing these in the key-value pairs of the push payload. In this example, the campaign name of the subsequent in-app message has been included. Your custom push callback can then pass the value as the parameter of the event property when logging the custom event.

### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign from within Braze's dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within your custom push callback.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery campaign where an in-app message will trigger when "campaign_name" equals "IAM campaign name example."][77]

If a server-sent event is logged while the app is not in the foreground, the event will log, but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.

## Local in-app messages

In-app messages can be created within the app and displayed locally in real-time. All customization options available on the dashboard are also available locally. This is particularly useful for displaying messages you wish to trigger within the app in real-time.

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Do not display in-app messages when the soft keyboard is displayed on the screen as rendering is undefined in this circumstance.
{% endalert %}

### Manually triggering in-app message display

The following method will manually display your in-app message:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/iam_event_trigger.png %}
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[84]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
