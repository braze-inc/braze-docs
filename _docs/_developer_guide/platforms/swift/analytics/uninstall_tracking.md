---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking for iOS
platform: Swift
page_order: 7
description: "This article covers how to configure uninstall tracking for the Swift SDK."

---

# Uninstall tracking

> Learn how to set up uninstall tracking for your iOS application, so you can ensure your app doesn't take any unwanted automatic actions upon receiving a Braze uninstall tracking push. Uninstall tracking utilizes background push notifications with a Braze flag in the payload. For general information, see [uninstall tracking][6].

{% alert important %}
Keep in mind, uninstall tracking can be imprecise. The metrics you see on Braze may be delayed or inaccurate.
{% endalert %}

## Step 1: Enable background push

In your Xcode project, go to **Capabilities** and ensure you have **Background Modes** enabled. For more information, see [silent push notification]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/silent/).

## Step 2: Check for Braze background push

Braze uses background push notifications to collect uninstall tracking analytics. Ensure that your application [does not take any unwanted actions]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/ignoring_internal/) upon receiving our uninstall tracking notifications.

## Step 3: Test from the Braze dashboard

Next, send yourself a test push from the Braze dashboard. Keep in mind, this test push will not update your user profile.

1. On the **Campaigns** page, create a push notification campaign and select **iOS push** as your platform.
2. On the **Settings** page, add the key `appboy_uninstall_tracking` with corresponding value `true` and check **Add Content-Available Flag**.
3. Use the **Preview** page to send yourself a test uninstall tracking push.
4. Check that your app does not take any unwanted automatic actions upon receiving the push.

{% alert important %}
These testing steps are a proxy for sending an uninstall tracking push from Braze. If you have badge counts enabled, a badge number will be sent along with the test push, but Braze's uninstall tracking pushes will not set a badge number on your application.
{% endalert %}

## Step 4: Enable uninstall tracking

Follow the instructions for [enabling uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

