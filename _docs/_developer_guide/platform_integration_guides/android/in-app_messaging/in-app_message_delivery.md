---
nav_title: In-App Message Delivery
article_title: In-App Message Delivery for Android/FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This article covers Android in-app message delivery, listing different trigger types, delivery semantics, and event triggering steps."
channel:
  - in-app messages

---

# In-app message delivery

## Trigger types

Our in-app message product allows you to trigger an in-app message display due to several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

{% alert note %}
Triggered in-app messages only work with custom events logged through the SDK and not through the REST APIs. Make sure to check out how to log custom events [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events).
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

By default, in-app messages are triggered by custom events logged by the SDK. If you would like to trigger in-app messages by server-sent events, you can also achieve this.

To enable this feature, a silent push is sent to the device, which allows a custom push receiver to log an SDK-based event. This SDK event will subsequently trigger the user-facing in-app message.

### Step 1: Register a custom BroadcastReceiver to log custom event

Register your custom `BroadcastReceiver` to listen for a specific silent push within your `AndroidManifest.xml`. For more information on registering a custom `BroadcastReceiver` review [Braze's push documentation][78].

### Step 2: Create your BroadcastReceiver

Your receiver will handle the intent broadcast by the silent push and log an SDK event. It will subclass `BroadcastReceiver` and override `onReceive()`. See [`EventBroadcastReceiver.java`][72] for a detailed example.

Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom `BroadcastReceiver`. To ensure the same event is not duplicated, the event logged from within your `BroadcastReceiver` should follow a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done, segmentation and user data may be affected by duplicate events being logged for a single user action.

For further details on custom handling push receipts, opens, and key-value pairs, review [Braze's push documentation][78].

### Step 3: Create a push campaign

Create a [silent push campaign][73] triggered via the server sent event.

![][75]

The push campaign must include key-value pair extras that indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![Two sets of key-value pairs: IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example campaign name".][76]{: style="max-width:70%;" }

The [`EventBroadcastReceiver.java`][72] recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your "in-app message trigger" event, you can achieve this by passing these in the key-value pairs of the push payload. In the example above, the campaign name of the subsequent in-app message has been included. Your custom `BroadcastReceiver` can then pass the value as the parameter of the event property when logging the custom event.

### Step 4: Create an in-app message campaign

Create your user-visible in-app message campaign from within Braze’s dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within the custom [`EventBroadcastReceiver.java`][72].

In the example below, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

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

[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/iam_event_trigger.png %}
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[84]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
