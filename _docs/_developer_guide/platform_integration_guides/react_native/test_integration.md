---
nav_title: Test Your Integration
platform: React Native
page_order: 1
description: "This article covers basic instructions how to test whether Braze SDK integrated correctly."
---

# Test Your Integration

At this point, you can verify that the SDK is integrated by checking session statistics in the Dashboard. If you run your application on either platform, you should see a new session in Dashboard (in the `Overview` section).

### User Sessions

You can also open a session for a particular user by calling the following code in your app.

```javascript
ReactAppboy.changeUser('some-user-id');
```

You can then search for the user with `some-user-id` in the Dashboard under `User Search`. There, you can verify the session and device information.

### Content

If you have implemented push notifications, you can test Content Cards, Push Notifications and In-App Messages.

# Alert -- you can't test these on an iOS simulator