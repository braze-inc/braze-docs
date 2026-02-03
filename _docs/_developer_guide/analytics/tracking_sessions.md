---
nav_title: Track sessions
article_title: Track sessions through the Braze SDK
page_order: 3.3
description: "Learn how to track sessions through the Braze SDK."

---

# Track sessions

> Learn how to track sessions through the Braze SDK.

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Subscribing to session updates

### Step 1: Subscribe to updates

To subscribe to session updates, use the `subscribeToSessionUpdates()` method.

{% tabs %}
{% tab web %}
At this time, subscribing to  session updates are not supported for the Web Braze SDK.
{% endtab %}

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
{% endtabs %}

### Step 2: Test session tracking (optional)

To test session tracking, start a session on your device, then open the Braze dashboard and search for the relevant user. In their user profile, select **Sessions Overview**. If the metrics update as expected, session tracking is working correctly.

![The sessions overview section of a user profile showing the number of sessions, last used date, and first used date.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
App-specific details are only shown for users who have used more than one app.
{% endalert %}

## Changing the default session timeout {#change-session-timeout}

You can change the length of time that passes before a session automatically times out.

{% tabs %}
{% tab web %}
By default, the session timeout is set to `30` minutes. To change this, pass the `sessionTimeoutInSeconds` option to your [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) function. It can be set to any integer greater than or equal to `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

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
{% endtabs %}

{% alert note %}
If you set a session timeout, all session semantics will automatically extend to the set timeout.
{% endalert %}
