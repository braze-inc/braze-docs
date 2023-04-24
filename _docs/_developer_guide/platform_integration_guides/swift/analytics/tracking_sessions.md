---
nav_title: Session Tracking
article_title: Session Tracking for iOS
platform: Swift
page_order: 0
description: "This reference article shows how to subscribe to session updates for your iOS application."

---

# Session tracking for iOS

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Our SDK generates "start session" and "close session" data points that account for session length and session count viewable within the Braze dashboard based on the following session semantics.

## Session lifecycle

A session is started when you call `Braze.init(configuration:)`. By default, this occurs when the `UIApplicationWillEnterForegroundNotification` notification is fired (when the app enters the foreground). Session end occurs when the app leaves the foreground (such as when the `UIApplicationDidEnterBackgroundNotification` notification is fired or when the app dies).

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout

You can set the `sessionTimeout` to the desired integer value in your `configuration` object passed to [`init(configuration)`][session_tracking_1].

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
{% tab OBJECTIVE-C %}

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

To detect sessions via your user, find your user on the dashboard and navigate to **App Usage** on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you expect it to.

![The app usage section of a user profile showing the number of sessions, last used date, and first used date.][session_tracking_7]

[session_tracking_1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class
[session_tracking_3]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
