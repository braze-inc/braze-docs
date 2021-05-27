---
nav_title: Tracking Sessions
platform: Android
page_order: 0
description: "This reference article shows how to subscribe to session updates for your Android application."
---
{% include archive/session_tracking.md platform="Android"%}

### Subscribing to Session Updates

The Braze SDK provides a [`subscribeToSessionUpdates`][1] subscriber to listen for session updates.

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#subscribeToSessionUpdates-com.appboy.events.IEventSubscriber-