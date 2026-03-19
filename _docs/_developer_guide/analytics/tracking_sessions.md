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

## Defining inactivity

Understanding how inactivity is defined and measured is key to managing session lifecycles effectively in the Web SDK. Inactivity refers to a period during which the Braze Web SDK does not detect any tracked events from the user.

### How inactivity is measured

The Web SDK tracks inactivity based on [SDK-tracked events]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). The SDK maintains an internal timer that resets each time a tracked event is sent. If no SDK-tracked events occur within the configured timeout period, the session is considered inactive and ends.

For more information on how session lifecycle is implemented in the Web SDK, see the session management source code in the [Braze Web SDK GitHub repository](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**What counts as activity by default:**
- Opening or refreshing the web app
- Interacting with Braze-driven UI elements (such as [In-app messages]({{site.baseurl}}/developer_guide/in_app_messages/) or [Content Cards]({{site.baseurl}}/developer_guide/content_cards/))
- Calling SDK methods that send tracked events (such as [custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/) or [user attribute updates]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**What does not count as activity by default:**
- Switching to a different browser tab
- Minimizing the browser window
- Browser focus or blur events
- Scrolling or mouse movements on the page

{% alert note %}
The Web SDK does not automatically track browser visibility changes, tab switching, or user focus. However, you can track these browser-level interactions by implementing custom event listeners using the browser's [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) and sending [custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) to Braze. For an example implementation, refer to [Tracking custom inactivity](#tracking-custom-inactivity).
{% endalert %}

### Session timeout configuration

By default, the Web SDK considers a session inactive after 30 minutes without any tracked events. You can customize this threshold when initializing the SDK using the `sessionTimeoutInSeconds` parameter. For details on configuring this parameter, including code examples, see [Changing the default session timeout](#changing-the-default-session-timeout).

### Example: Understanding inactivity scenarios

Consider the following scenario:

1. A user opens your website, and the SDK starts a session by calling [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. The user switches to a different browser tab to view another website for 30 minutes.
3. During this time, no SDK-tracked events occur on your website.
4. After 30 minutes of inactivity, the session automatically ends.
5. When the user switches back to your website tab and triggers an SDK event (such as viewing a page or interacting with content), a new session begins.

### Tracking custom inactivity

If you need to track inactivity based on browser visibility or tab switching, implement custom event listeners in your JavaScript code. Use browser events such as `visibilitychange` to detect when users leave your page, and manually send [custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/) to Braze or call [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) when appropriate.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

For more information on logging custom events, refer to [Log custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/). For details on session lifecycle and timeout configuration, refer to [Changing the default session timeout](#change-session-timeout).

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

{% tab react native %}
The React Native SDK does not expose a method for subscribing to session updates directly. Session lifecycle is managed by the underlying native SDK, so to subscribe to updates, use the native platform approach for the **Android** or **Swift** tab.
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

{% tab react native %}
The React Native SDK relies on the native SDKs to manage sessions. To change the default session timeout, configure it in the native layer:

- **Android:** Set `com_braze_session_timeout` in your `braze.xml` file. For details, select the **Android** tab.
- **iOS:** Set `sessionTimeout` on your `Braze.Configuration` object. For details, select the **Swift** tab.
{% endtab %}
{% endtabs %}

{% alert note %}
If you set a session timeout, all session semantics will automatically extend to the set timeout.
{% endalert %}

## Troubleshooting

### User profile has 0 sessions

A user profile can have 0 sessions if the user was created outside the SDK:

- **Created by REST API:** If a user is created through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint with an `app_id` in the request, the profile appears associated with that app but has no session data because the SDK was never initialized for that user.
- **Created by CSV import:** If a user is imported through [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) without values for first or last session fields, the profile exists with 0 sessions.
