---
nav_title: Tracking sessions
article_title: Tracking Sessions for Windows Universal
platform: Windows Universal
page_order: 0
description: "This reference article covers how to track sessions on the Windows Universal platform."
hidden: true
---

# Analytics
{% multi_lang_include archive/windows_deprecation.md %}

## Session tracking

The Braze SDK reports session data that is used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. based on the following session semantics, our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard.

### Session lifecycle

Our Windows integration logs session opens when the app is launched and logs session closes when the application is closed. The minimum value for `sessionTimeoutInSeconds` is 1 second. If you need to force a new session, you can do so by changing users.

### Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to "App Usage" on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you would expect it to.

![A user profile showing app usage as 25 sessions, last used two hours ago, and first used twenty days ago]({% image_buster /assets/img_archive/test_session.png %})


