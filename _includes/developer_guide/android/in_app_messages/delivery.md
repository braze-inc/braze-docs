{% multi_lang_include developer_guide/prerequisites/android.md %}

## Message triggers

### Trigger types

In-app messages are automatically triggered when the SDK logs one of the following custom event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Note that the `Specific Purchase` and `Custom Event` triggers also contain robust property filters.

{% alert note %}
In-app messages can't be triggered through the API or by API events&#8212;only custom events logged by the SDK. To learn more about logging, see [Logging Custom Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Delivery semantics

All eligible in-app messages are delivered to a user's device at the start of their session. When delivered, the SDK will prefetch assets, so they're available at trigger time, minimizing display latency. If the trigger event has more than one eligible in-app message, only the message with the highest priority will be delivered.

For more information about the SDK's session start semantics, see[Session Lifecycle]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Rate limit

By default, we rate limit in-app messages to once every 30 seconds to support a quality user experience.

To override this value, set `com_braze_trigger_action_minimum_time_interval_seconds` in your `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Key-value pairs

When you create a campaign in Braze, you can set key-value pairs as `extras`, which the the in-app messaging object can use to send data to your app. For example:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
For more information, refer to the [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Disabling automatic triggers

To prevent in-app messages from automatically triggering:

1. Ensure you are using the automatic integration initializer, which is enabled by default starting in version `2.2.0`.
2. Set the in-app message operation default to `DISCARD` by adding the following line to your `braze.xml` file.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Manually triggering messages

By default, in-app messages are automatically triggered when the SDK logs a custom event. However, you can manually trigger a message using the following methods.

### Using a server-side event

To trigger an in-app message using a server-sent event, send a silent push notification to the device, which allows a custom push callback to log an SDK-based event. This event will then trigger the user-facing in-app message.

#### Step 1: Create a push callback to receive the silent push

Register [your custom push even callback]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) to listen for a specific silent push notification.

In the following example, two events will be logged for the in-app message to be delivered, one by the server and one from within your custom push callback. To make sure the same event is not duplicated, the event logged from within your push callback should follow a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done, segmentation and user data may be affected by duplicate events being logged for a single user action.

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

#### Step 2: Create a push campaign

Create a [silent push campaign]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) triggered via the server sent event.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

The push campaign must include key-value pair extras that indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![Two sets of key-value pairs: IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

The earlier push callback sample code recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your "in-app message trigger" event, you can achieve this by passing these in the key-value pairs of the push payload. In this example, the campaign name of the subsequent in-app message has been included. Your custom push callback can then pass the value as the parameter of the event property when logging the custom event.

#### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within your custom push callback.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery campaign where an in-app message will trigger when "campaign_name" equals "IAM campaign name example."]({% image_buster /assets/img_archive/iam_event_trigger.png %})

If a server-sent event is logged while the app is not in the foreground, the event will log, but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.

### Displaying a pre-defined message

To manually display a pre-defined in-app message, use the following method:

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

### Displaying a message in real-time 

You can also create and display local in-app messages in real-time, using the same customization options available on the dashboard. To do so:

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
