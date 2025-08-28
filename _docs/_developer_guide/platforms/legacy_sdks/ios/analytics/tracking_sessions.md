---
nav_title: Tracking sessions
article_title: Tracking Sessions for iOS
platform: iOS
page_order: 0
description: "This reference article shows how to subscribe to session updates for your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Session tracking for iOS

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Our SDK generates "start session" and "close session" data points that account for session length and session count viewable within the Braze dashboard based on the following session semantics.

## Session lifecycle

A session is started when you call `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, after which by default sessions start when the `UIApplicationWillEnterForegroundNotification` notification is fired (such as the app enters the foreground) and end when the app leaves the foreground (such as when the `UIApplicationDidEnterBackgroundNotification` notification is fired or when the app dies).

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout

Starting with Braze iOS SDK v3.14.1, you can set the session timeout using the Info.plist file. Add the `Braze` dictionary to your `Info.plist` file. Inside the `Braze` dictionary, add the `SessionTimeout` number subentry and set the value to your custom session timeout. Note that prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

You may alternatively set the `ABKSessionTimeoutKey` key to the desired integer value in your `appboyOptions` object passed to [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

If you have set a session timeout, then the session semantics all extend to that customized timeout.

{% alert note %}
The minimum value for `sessionTimeoutInSeconds` is 1 second. The default value is 10 seconds.
{% endalert %}

## Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to **App Usage** on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you expect it to.

![The app usage section of a user profile showing the number of sessions, last used date, and first used date.]({% image_buster /assets/img_archive/test_session.png %})

