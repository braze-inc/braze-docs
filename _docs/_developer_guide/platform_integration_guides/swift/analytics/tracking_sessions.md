---
nav_title: Session Tracking
article_title: Session Tracking for iOS
platform: Swift
page_order: 0
search_rank: 1
description: "This reference article shows how to subscribe to session updates for the Swift SDK."

---

# Session tracking

> The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. 

Our SDK generates "start session" and "close session" data points that account for session length and session count viewable within the Braze dashboard based on the following session semantics.

## Session lifecycle

A session is started when you call `Braze.init(configuration:)`. By default, this occurs when the `UIApplicationWillEnterForegroundNotification` notification is fired (when the app enters the foreground). Session end occurs when the app leaves the foreground (such as when the `UIApplicationDidEnterBackgroundNotification` notification is fired or when the app dies).

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout

You can set the `sessionTimeout` to the desired integer value in your `configuration` object passed to [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

{% tabs %}
{% tab swift %}

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
{% endtab %}
{% tab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

If you have set a session timeout, then the session semantics all extend to that customized timeout.

{% alert note %}
The minimum value for `sessionTimeout` is 1 second. The default value is 10 seconds.
{% endalert %}

## Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to **Sessions Overview** on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you expect it to. App-specific details will display after the user has used more than one app.

![The sessions overview section of a user profile showing the number of sessions, last used date, and first used date.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

App-specific details will display only if the user has used more than one app.

## Subscribing to session updates

To listen to session updates, use the [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)) method. Session start and end events will only be logged when the app is running in the foreground. If you register a callback to session end events and the app is backgrounded, the callback will fire when the app is foregrounded again. Session duration, however, is still measured as the time from app open or foregrounding until app closing or backgrounding.

{% tabs %}
{% tab swift %}
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
{% endtab %}

{% tab objective-c %}
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
{% endtab %}
{% endtabs %}

Alternatively, in Swift, you can use the [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) `AsyncStream` to observe asynchronous changes:

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

