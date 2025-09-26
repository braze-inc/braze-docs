---
nav_title: Influenced opens
article_title: Influenced Opens
page_order: 7
page_type: reference
description: "This reference article explains influenced opens and how you can track them to provide a richer level of detail into your push campaigns."
channel: push

---

# Influenced opens

> When a user selects a push notification and is sent to your app, Braze logs it as a direct open. When users don't select the notification but may still be influenced by the push notification, Braze logs it as an influenced open. This provides a richer level of detail into the effect of your push campaigns.

## How it works

At their base, influenced opens measure the number of users who open the app after receiving a notification without selecting the notification. Because there is no direct action linking the notification to the app open, an influenced open is logged if the user opens the app less than thirty minutes after receiving the push notification or under half the average time since that user's last session.

For example, say you send a push notification to your app users. If a user who normally opens the app 30 times a day opens your app six hours after receiving the push, the push gets little to no credit for influencing the open. However, if a user who normally uses the app once a month opens the app six hours after receiving the push, the open has a much better chance of being counted as an influenced open. 

This differs from setting app opens as a conversion event for a push campaign. For conversions, all opens within the conversion window will be attributed to the campaign. Influenced opens set a time window and attribution credit based on an individual user's behavior.

## Viewing a campaign's influenced opens

Influenced opens are added to the direct opens of a campaign to give a number of total opens. This is displayed on a push campaign's **Campaign Analytics** page. Total opens and direct opens are shown in the message performance and **Historical Performance** sections. Influenced opens are the difference between the two measures.

![Influenced opens statistics on the Campaign Details page for a campaign]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

For more information on tracking opens, check out the conversion tracking section of our [best practices for push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

