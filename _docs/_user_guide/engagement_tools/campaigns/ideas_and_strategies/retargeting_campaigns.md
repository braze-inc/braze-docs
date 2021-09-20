---
nav_title: Retargeting Campaigns
article_title: Retargeting Campaigns
page_order: 2
page_type: reference
description: "This reference article goes over how and why you should consider retargeting campaigns based on messages your users receive."
tool:
  - Campaigns
  
---

# Retargeting Campaigns

> This reference article goes over the concept of retargeting campaigns and how it can be a beneficial marketing strategy. 
> <br>
> <br>
> By retargeting campaigns based on the user's previous actions, like whether or not they opened an email, you can help reclassify your users, opening the door to an effective, data-driven marketing approach.

Braze provides support for retargeting users based on messages they have received. You can retarget users based upon their interactions with your campaigns, Canvases, and News Feed cards.

![Retargeting Campaigns][1]{: style="max-width:80%;"}

Each of these retargeting filters provides you with several options after you add them.

For more on targeting users, check out our [Campaign Setup LAB course](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

## Retargeting Filters

### Clicked Card Filter

![Click Card][2]

Use the filter to find users who Have/Have Not clicked a specific News Feed card (which you specify in the drop-down).

### Clicked/Opened Campaign Filter

![Clicked/Opened][3]

Use this filter to find users who Have/Have Not:

- Clicked Email
- Clicked In-App Message
- Directly Opened Push Notification
- Opened Email
- Viewed In-App Message

This can be further specified by selecting which campaign you want to retarget in the drop-down.

### Clicked/Opened Campaign or Canvas With Tag Filter

![Clicked/Opened][16]

Use this filter to find users who have or have not interacted with campaigns or Canvases with a given tag:

- Clicked Email
- Clicked In-App Message
- Directly Opened Push Notification
- Opened Email
- Viewed In-App Message

### Converted From Campaign Filter

![Converted from Campaign][12]

Use this filter to find users who Have/Have Not converted (based on the primary conversion) in your target campaign, which is selected in the drop-down menu.

>  For recurring campaigns this filter refers to whether users have converted on the _most recent_ message from the campaign.

### Converted From Canvas Filter

![Converted from Canvas][18]

Use this filter to find users who Have/Have Not converted (based on the primary conversion) in your target Canvas, which is selected in the drop-down menu.

>  For recurring Canvases this filter refers to whether users have ever converted anytime they've gone through the Canvas.

### In Campaign Control Group Filter

![Campaign Control Group][13]

Use this filter to find users who Are/Are Not in the control group of your target campaign, which can be selected in the drop-down.

### In Canvas Control Group Filter

![Canvas Control Group][19]

Use this filter to find users who Are/Are Not in the control group of your target Canvas, which can be selected in the drop-down.

### Last Received Message from Specific Campaign Filter

![Last Received Specific Campaign Filter][14]

Use this filter to find users who last received a specific campaign before or after a specified date or number of days.

### Last Received Message from Specific Campaign or Canvas with Tag Filter

![Last Received Campaign with Tag][17]

Use this filter to find users who last received a specific campaign or Canvas with a given tag before or after a specified date or number of days.

### Received Message from Campaign Filter

![Received Campaign][4]

\" this filter to find users who Have/Have Not received your target campaign, which you select in the drop-down.

### Received Message from Campaign or Canvas with Tag Filter

![Received Campaign with Tag][15]

Use this filter to find users who Have/Have Not received a campaign or Canvas that has your target tag, which you select in the drop-down.

## Why Use Retargeting Campaigns?

Retargeting is particularly effective when the original segment also included a specific action you want to see users take. For example, let's say you have a card targeted at users who have never made a purchase. The card advertises a promotion for a discounted in-app purchase. The initial segment looks like:

- Money Spent in App is exactly 0
- Last Used App less than 14 days ago

The total number of users in the segment is 100,000 and you know from the News Feed stats that 60,000 unique users viewed the card and 20,000 unique users clicked the card. Through the segmenter we can see how many of those users who clicked the card actually made a purchase:

- Money Spent in App is more than 0
- Clicked Card is {Name of Card}

After examining those stats, we can make a segment of users who clicked the card, but did not make a purchase:

- Money Spent in App is exactly than 0
- Clicked Card is {Name of Card}

We can retarget this segment with additional messaging around the promotion or another in-app purchase. Retargeting can be done via another News Feed card or through a messaging campaign. A multichannel approach allows you to reach users where they’re most likely to respond, thus increasing the effectiveness of your campaigns.

[1]: {% image_buster /assets/img_archive/retarget.png %}
[2]: {% image_buster /assets/img_archive/clickedcard.png %}
[3]: {% image_buster /assets/img_archive/clickedopened.png %}
[4]: {% image_buster /assets/img_archive/receivedcamp.png %}
[12]: {% image_buster /assets/img_archive/converted_from_campaign.png %}
[13]: {% image_buster /assets/img_archive/campaign_control_group.png %}
[14]: {% image_buster /assets/img_archive/last_received_specific_campaign.png %}
[15]: {% image_buster /assets/img_archive/received_campaign_with_tag.png %}
[16]: {% image_buster /assets/img_archive/retarget_tag_filter.png %}
[17]: {% image_buster /assets/img_archive/last_received_campaign_with_tag.png %}
[18]: {% image_buster /assets/img_archive/converted_from_canvas.png %}
[19]: {% image_buster /assets/img_archive/canvas_control_group.png %}
