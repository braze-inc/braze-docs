---
nav_title: Tracking Sessions
article_title: Tracking Sessions for Web
platform: Web
page_order: 0
description: "This reference article covers how to track sessions for web."

---

# Session tracking for web

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard based on the below session semantics.

## Session lifecycle

By default, sessions begin when `appboy.openSession()` is first called and remain open until at least 30 minutes of inactivity. This means that if the user navigates away from the site and returns less than 30 minutes later, the same session will continue. If they return after the 30 minutes have expired, a "close session" data point is automatically generated for the time they navigated away, and a new session opens.

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout

To customize the session timeout, pass the `sessionTimeoutInSeconds` option to your [`initialize`][session_tracking_5] function. The minimum value for `sessionTimeoutInSeconds` is 1 second.

```js
// Sets the session timeout to 15 minutes instead of the default 30
appboy.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

If you have set a session timeout, then the above session semantics all extend to that customized timeout.

## Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to **App Usage** on the user profile. You can confirm that session tracking is working by checking that the session metric increases when you would expect it to.

![A user profile component showing how many sessions have occurred, when the app was first used, and when it was last used.][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
