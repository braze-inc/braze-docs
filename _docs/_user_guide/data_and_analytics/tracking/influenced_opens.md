---
nav_title: Influenced Opens
article_title: Influenced Opens
page_order: 7
page_type: reference
description: "This reference article explains Influenced Opens and how you can track them to provide a richer level of detail into the effect of your push campaigns."
channel: push

---
# Influenced Opens

Push notifications are a good way to catch users attention and increase engagement. Often that is through direct opens when users click on the notification and are sent to the app. However, the behavior of users who do not click the message may still be influenced by your push campaigns. Braze provides data on Influenced Opens to provide a richer level of detail into the effect of your push campaigns. 

At their base, Influenced Opens measure the number of users who open the app after receiving a notification without clicking on the notification. Because there is no direct action linking the notification to the app open, an influenced open is awarded if the user opens the app 30 minutes since the user received the push notification, or under half the average time since the user's last session.

As an example, say you are sending a push to users of a messaging app, and you have a group of users who don't click through the notification. If a user who normally opens the app 30 times a day opens the app 6 hours after receiving the push, the push would get little to no credit for influencing the open. However, if a user who normally uses the app once a month opens the app 6 hours after receiving the push, the open would have a much better chance of being counted as an influenced open. This differs from setting app opens as a conversion event for a push campaign. For conversions, all opens within the conversion window will be attributed to the campaign. Influenced Opens sets a time window and attribution credit based on an individual user's behavior.

Influenced Opens are added to the direct opens of a campaign to give a number of total opens. This can be seen on the Details page of a push campaign. Total opens and direct opens are shown in the Message Performance and Historical Performance sections. Influenced Opens are the difference between the two measures.

![Influenced Open Details][1]

For more information on tracking opens, check out the conversion tracking section of our [best practices for push][bp].

[bp]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[1]: {% image_buster /assets/img_archive/Influenced_Opens2.png %}
