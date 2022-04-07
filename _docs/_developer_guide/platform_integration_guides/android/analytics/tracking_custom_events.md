---
nav_title: Tracking Custom Events
article_title: Tracking Custom Events for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "This reference article covers how to add and track custom events for your Android or FireOS application."

---

# Tracking custom events for Android and FireOS

You can record custom events in Braze to learn more about your app's usage patterns and segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [analytics overview][0], as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Adding a custom event

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```

{% endtab %}
{% endtabs %}

Refer to our [KDoc][2] for more information.

### Adding properties

You can add metadata about custom events by passing a [Braze properties object][4] with your custom event.

Properties are defined as key-value pairs. Keys are `String` objects, and values can be `String`, `int`, `float`, `boolean`, or [`Date`][3] objects.

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties eventProperties = new BrazeProperties();
eventProperties.addProperty("key", "value");
Braze.getInstance(YOUR_ACTIVITY.this).logCustomEvent(YOUR_EVENT_NAME, eventProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val eventProperties = BrazeProperties()
eventProperties.addProperty("key", "value")
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME, eventProperties)
```

{% endtab %}
{% endtabs %}

### Reserved keys

The following keys are reserved and cannot be used as custom event properties:

- `time`
- `event_name`

Refer to our [KDoc][2] for more information.

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-custom-event.html
[3]: http://developer.android.com/reference/java/util/Date.html
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
