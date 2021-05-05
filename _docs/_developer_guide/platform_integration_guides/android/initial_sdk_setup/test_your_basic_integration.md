---
nav_title: Test Your Basic Integration
page_order: 1

platform: Android
---

# Test your Basic Integration

## Confirm Session Tracking is Working
To test that you have session tracking working, go to the `Overview` section of your dashboard, select your application from the select box (defaulted to `All Apps`), and set `Display Data For` to be `Today`. Then open your app and refresh the page - your main metrics should all have increased by 1.

![Sessions working][55]

You should continue to test your integration by navigating through your application and ensuring that only one session has been logged. Then, background the app for at least 10 seconds and bring it to the foreground again. By default a new session is created if the app is foregrounded after more than 10 seconds, not in the foreground (backgrounded or closed). Once you've done this, confirm that another session was logged.

### Debugging Session Tracking
If session tracking is behaving unexpectedly, turn on [Verbose Logging][56] and observe your app while you reproduce session triggering steps. Observe Braze statements in the logcat to detect where you may have missed logging `openSession` and `closeSession` calls in your activities.

[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/#verbose-logging
[57]: {% image_buster /assets/img_archive/android_device_data.png %}
