---
nav_title: Test Your Basic Integration
article_title: Test Your Basic Integration for Android and FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "This article covers how to test your basic integration for your Android or FireOS application."

---

# Test your basic integration

## Confirm session tracking is working

At this point, you should have session tracking working in your Braze integration. To test this, go to **Overview**, select your application from the selected app name dropdown (defaulted to "All Apps"), and set **Display Data For** to "Today". Then open your app and refresh the page - your main metrics should all have increased by 1.

![][55]

You should continue to test your integration by navigating through your application and ensuring that only one session has been logged. Then, background the app for at least 10 seconds and bring it to the foreground again. By default, a new session is created if the app is brought to the foreground after being backgrounded or closed for more than 10 seconds. Once you've done this, confirm that another session was logged.

## Debugging session tracking
If session tracking is behaving unexpectedly, turn on [verbose logging][56] and observe your app while you reproduce session triggering steps. Observe Braze statements in the logcat to detect where you may have missed logging `openSession` and `closeSession` calls in your activities.

[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#android-verbose-logging