# Beacon integration

> This article will walk you through how to integrate specific kinds of beacons with Braze to allow for segmentation and messaging.

## Infillion Beacons

Once you have your Infillion Beacons set up and integrated into your app, you can log custom events for things like a visit starting or ending, or a beacon being sighted. You can also log properties for these events, like the place name or the dwell time.

To log a custom event when a user enters a place, include this code in the `onVisitStart` method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

The `requestImmediateDataFlush` verifies that your event will log even if the app is in the background, and the same process can be implemented for leaving a location. Note that the activity and context that you are working in may change exactly how you integrate the `logCustomEvent` and `requestImmediateDataFlush` lines. Also, note that this code will create and increment a unique custom event for each new place that the user enters. As such, if you anticipate creating more than 50 places we recommend you create one generic "Place Entered" custom event and include the place name as an event property.
