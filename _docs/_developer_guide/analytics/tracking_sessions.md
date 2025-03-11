---
nav_title: Tracking Sessions
article_title: Tracking sessions through the Braze SDK
page_order: 3.4
description: "Learn how to track sessions through the Braze SDK."

---

# Tracking sessions

> Learn how to track sessions through the Braze SDK.

## About the session lifecycle

A session refers to the period of time the Braze SDK tracks user activity in your app after it's launched. You can also force a new session by [calling the `changeUser()` method]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id). For wrapper SDKs, refer to the relevant Android or Swift information.

{% tabs %}
{% tab android %}
{% alert note %}
If you've set up the [activity lifecycle callback]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) for Android, Braze will automatically call `openSession()` and `closeSession()` for each activity in your app.
{% endalert %}

By default, a session starts when `openSession()` is first called. If your app goes to the background, the session will remain active for `10` seconds (unless you [change the default session timeout](#changing-the-default-session-timeout)) or the user closes your app. Keep in mind, if the user closes your app while its in the background, session data may not be set to Braze until they reopen the app. 

Calling `closeSession()` will not immediately end the session. Instead, it will end the session after 10 seconds if `openSession()` isn't called again by the user starting another activity.
{% endtab %}

{% tab swift %}
By default, a session starts when you call `Braze.init(configuration:)`. This occurs when the `UIApplicationWillEnterForegroundNotification` notification is triggered, meaning the app has entered the foreground.

If your app goes to the background, `UIApplicationDidEnterBackgroundNotification` will be triggered. The session will remain active for `10` seconds (unless you [change the default session timeout](#changing-the-default-session-timeout)) or the user closes your app.
{% endtab %}

{% tab web %}
By default, a session starts when you first call `braze.openSession()`. The session will remain active for up to `30` minutes of inactivity (unless you [change the default session timeout](#changing-the-default-session-timeout)) or the user closes the app.
{% endtab %}
{% endtabs %}

## Changing the default session timeout

You can change the length of time that passes before a session automatically times out. For wrapper SDKs, use the relevant method from Android or Swift.

{% tabs %}
{% tab android %}
By default, the session timeout is set to `10` seconds. To change this, open your `braze.xml` file and add the `com_braze_session_timeout` parameter. It can be set to any integer greater than or equal to `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
By default, the session timeout is set to `10` seconds. To change this, set `sessionTimeout` in the `configuration` object that's passed to [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). It can be set to any integer greater than or equal to `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
By default, the session timeout is set to `30` seconds. To change this, pass the `sessionTimeoutInSeconds` option to your [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) function. It can be set to any integer greater than or equal to `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
If you set a session timeout, all session semantics will automatically extend to the set timeout.
{% endalert %}

## Subscribing to session updates

To subscribe to session updates, use the `subscribeToSessionUpdates()` method. For wrapper SDKs, use the relevant method from Android or Swift.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

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

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
If you register a session end callback, it fires when the app returns to the foreground. Session duration is measured from when the app opens or foregrounds, to when it closes or backgrounds.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

To subscribe to an asynchronous stream, you can use [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) instead.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
At this time, subscribing to  session updates are not supported for the Web Braze SDK.
{% endtab %}
{% endtabs %}

## Testing session tracking

To test session tracking, start a session on your device, then open the Braze dashboard and search for the relevant user. In their user profile, select **Sessions Overview**. If the metrics update as expected, session tracking is working correctly.

![The sessions overview section of a user profile showing the number of sessions, last used date, and first used date.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:60%;"}

{% alert note %}
App-specific details are only shown for users who have used more than one app.
{% endalert %}
