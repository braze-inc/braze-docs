---
nav_title: Sunset Policies
article_title: Sunset Policies for Push
page_order: 3
page_type: reference
description: "This article provides best practices for sunsetting push notifications to a segment of users."
channel: push

---

# Sunset policies for push {#push-sunset-policies}

Even when you make sure to send only relevant, timely push notifications, some users may still be unresponsive to them and find them spammy. If a user shows a history of repeatedly ignoring your push notifications, it's a good idea to stop sending them pushes before they become annoyed with your app's communications or uninstall your app altogether. To do this, create a [sunset policy][1] that eventually stops sending push notifications to users who haven't had a direct or influenced open for a long period of time. 

Before you stop sending push notifications to a segment of users, you should deliver one final notification that explains why they will no longer receive pushes and gives them a chance to demonstrate their interest in continued pushes by opening that notification. After the sunset policy goes into effect, use an [in-app message][2] or [News Feed card][3] to remind these users that while they will no longer receive pushes, in-app messaging channels will continue to deliver interesting, helpful information.

Although you may be reluctant to stop sending pushes to users who originally opted in to them, keep in mind that there are other messaging channels that can more effectively reach these users, especially if they have previously ignored your pushes. If the user opens your emails, then email campaigns are a good way to reach them outside of your app. If not, then in-app messages and News Feed cards are the best way to deliver content without risking the user uninstalling your app.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/
[3]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
