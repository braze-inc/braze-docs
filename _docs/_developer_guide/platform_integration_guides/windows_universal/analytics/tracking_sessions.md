---
nav_title: Tracking Sessions
article_title: Tracking Sessions for Windows Universal
platform: Windows Universal
page_order: 0
description: "This reference article covers how to track sessions on the Windows Universal platform."

---

# Analytics
{% include archive/windows_deprecation.md %}

## Session tracking

The Braze SDK reports session data that is used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. based on the following session semantics, our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard.

### Session lifecycle

Our Windows integration logs session opens when the app is launched and logs session closes when the application is closed. The minimum value for `sessionTimeoutInSeconds` is 1 second. If you need to force a new session, you can do so by changing users.

### Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to "App Usage" on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you would expect it to.

![A user profile showing app usage as 25 sessions, last used two hours ago, and first used twenty days ago][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

