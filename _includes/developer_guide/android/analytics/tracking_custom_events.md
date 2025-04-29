# Tracking custom events

> You can record custom events in Braze to learn more about your app's usage patterns and segment your users by their actions on the dashboard. This reference article covers how to add and track custom events for your Android or FireOS application.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [analytics overview]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

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

Refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) for more information.

### Adding properties

You can add metadata about custom events by passing a [Braze properties object](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) with your custom event.

Properties are defined as key-value pairs. Keys are `String` objects, and values can be `String`, `int`, `float`, `boolean`, or [`Date`](http://developer.android.com/reference/java/util/Date.html) objects.

{% tabs %}
{% tab JAVA %}

```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```

{% endtab %}
{% endtabs %}

### Reserved keys

The following keys are reserved and cannot be used as custom event properties:

- `time`
- `event_name`

Refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) for more information.

