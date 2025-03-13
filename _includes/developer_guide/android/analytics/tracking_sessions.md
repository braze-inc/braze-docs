# Tracking Sessions

> The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard based on the following session semantics. This reference article shows how to subscribe to session updates for your Android or FireOS application.

## Session lifecycle

If you have integrated Braze using our recommended [activity lifecycle callback integration]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), `openSession()` and `closeSession()` will be called automatically for each activity in your app. By default, sessions on Android are opened upon the first call to `openSession()` and are closed after an app has been out of the foreground for longer than 10 seconds. Note that calling `closeSession()` does not close a session immediately. Rather, it closes a session in 10 seconds if the user doesn't call `openSession()` (for example, by navigating to another activity) in the interim.

An Android session times out after 10 seconds without any communication from the host application. This means if a user backgrounds the app and returns 9 seconds later, the same session will be continued. Note that if a session closes while the user has the app in the background, that data may not be flushed to the server until the app is opened again.

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout
To customize the session timeout, add `com_braze_session_timeout` to your [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml) file. The minimum value for `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` is 1 second.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to **App Usage** on the user profile. You can confirm that session tracking is working by checking that the session metric increases when you would expect it to.

![A user profile component showing how many sessions had occurred, when the app was first used, and when it was last used.]({% image_buster /assets/img_archive/test_session.png %})

## Subscribing to session updates

The Braze SDK provides a [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html) subscriber to listen for session updates:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
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
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

