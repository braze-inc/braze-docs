---
nav_title: Utilizing Badge Count
article_title: Utilizing Badge Count
page_order: 8

page_type: reference
description: "This article covers using the iOS badge count to re-engage users who didn't notice a push, or who have disabled foreground push notifications."
platform: iOS
channel: 
- push
- in-app messages
- news feed

---
# Utilizing Badge Count

The iOS badge count displays the number of unread notifications within your application, taking the form of a red circle in the upper-right hand corner of the app icon. In recent years, badging has come to be an effective means for re-engaging app users.

The badge count can be used to re-engage your users who did not notice a push, or who have disabled foreground push notifications. Similarly, it can be used to notify your users about unviewed messages such as News Feed changes or in-app updates.

## Badge Count with Braze

You can specify the desired badge count when you compose a push notification through Braze's dashboard. This can be set to a user attribute with Braze's personalized messaging, allowing endlessly customizable logic. If you wish to send a silent push that updates the badge count without disturbing the user, add the "Content-Available" flag to your push and leave its message contents empty.

### Removing the Badge Count

Set the badge count to 0 or "" to remove the badge count from the app's icon. Braze will also automatically clear the badge when a push notification is received while the app is in the foreground.

## Best Practices

In order to optimize the re-engagement power of badging, it is crucial that you configure your badge settings in a way that most simplifies the user's experience.

### Keep the Badge Count Low
Research shows that once the badge count increases past double digits, users generally lose interest in the updates and often stop using the app altogether.

>  There can be exceptions to this rule depending on the nature of your app (e.g. email and group messaging apps).

### Limit the Things a Badge Count Can Represent
When badging, you want to make the notifications as clear and direct as possible. By limiting the number of things that a badge notification can represent, you can provide your users with a sense of familiarity with your app's features and updates.

### News Feed and In-app Badging
One of the most powerful features of badging is that it allows you to engage with your users without the immediacy of a push notification through the News Feed and in-app updates. To ensure that your users stay interested in the in-app badging notifications, you should try to focus such badge updates on personalized or urgent messages.
