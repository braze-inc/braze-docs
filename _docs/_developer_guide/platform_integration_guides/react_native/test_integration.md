---
nav_title: Test Your Integration
article_title: Integration Testing for React Native
platform: React Native
page_order: 2
description: "This article covers basic instructions how to test whether Braze SDK integrated correctly."

---

# Test Your Integration

At this point, you can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the `Overview` section).

## User Sessions

You can also open a session for a particular user by calling the following code in your app.

```javascript
ReactAppboy.changeUser("user-id");
```

You can then search for the user with `some-user-id` in the dashboard under __User Search__. There, you can verify the session and device information.

## Content

If you have implemented push notifications, you can test Content Cards, Push Notifications and In-App Messages.

{% alert important %}
You can't test push notification related app behavior on an iOS simulator because simulators don't support the device tokens required to send and receive a push notification.
{% endalert %}
