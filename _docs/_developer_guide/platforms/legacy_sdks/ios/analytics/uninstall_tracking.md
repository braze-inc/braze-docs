---
nav_title: Uninstall tracking
article_title: Uninstall Tracking for iOS
platform: iOS
page_order: 7
description: "This article covers how to configure uninstall tracking for your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uninstall tracking for iOS

> This article covers how to configure uninstall tracking for your iOS application, and how to test so that your app does not take any unwanted automatic actions upon receiving a Braze uninstall tracking push.

Uninstall tracking utilizes background push notifications with a Braze flag in the payload. For more information, see [uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) in our user guide.

## Step 1: Enabling background push

Make sure that you have enabled the **Remote notifications** option from the **Background Modes** section of your Xcode project's **Capabilities** tab. Refer to our [silent push notification]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/) documentation for additional details.

## Step 2: Checking for Braze background push

Braze uses background push notifications to collect uninstall tracking analytics. Make sure that your application [does not take any unwanted actions]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) upon receiving our uninstall tracking notifications.

## Step 3: Test from the dashboard

Next, send yourself a test push from the dashboard. This test push will not update your user profile.

1. On the **Campaigns** page, create a push notification campaign and select **iOS push** as your platform.<br><br>
2. On the **Settings** page, add the key `appboy_uninstall_tracking` with corresponding value `true` and check **Add Content-Available Flag**.<br><br>
3. Use the **Preview** page to send yourself a test uninstall tracking push.<br><br>
4. Check that your app does not take any unwanted automatic actions upon receiving the push.

{% alert important %}
These testing steps are a proxy for sending an uninstall tracking push from Braze. If you have badge counts enabled, a badge number will be sent along with the test push, but the Braze uninstall tracking pushes will not set a badge number on your application.
{% endalert %}

## Step 4: Enable uninstall tracking

Follow the instructions for [enabling uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

