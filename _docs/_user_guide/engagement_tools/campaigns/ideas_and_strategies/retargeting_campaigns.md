---
nav_title: Retargeting Campaigns
article_title: Retargeting Campaigns
page_order: 2
page_type: reference
description: "This reference article goes over how and why you should consider retargeting campaigns based on messages your users receive."
tool:
  - Campaigns
  
---

# Retargeting campaigns

> By retargeting campaigns based on the user's previous actions, like whether or not they opened an email, you can help reclassify your users, opening the door to an effective, data-driven marketing approach.

{% alert note %}
This article includes information on News Feed, which is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

Braze provides support for retargeting users based on messages they have received. You can retarget users based upon their interactions with your campaigns, Canvases, and News Feed cards. 

Each of these retargeting filters provides you with several options after you add them. For more on targeting users, check out our [Braze Learning course](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup!

![Segment Details section with the dropdown menu for the available filters.][1]{: style="max-width:80%;"}

## Retargeting filters

You can use the retargeting filters in this section for your users within your campaigns, Canvases, and News Feed cards.

### Clicked Card

Use the filter to find users who have and have not clicked a specific News Feed card.

![][2]

### Clicked/Opened Campaign

Use this filter to find users who have or have not:

- Clicked an email
- Clicked an in-app message
- Directly opened a push notification
- Opened an email
- Viewed an in-app message

![][3]

This can be further specified by selecting which campaign you want to retarget.

### Clicked or opened Campaign or Canvas with tag

Use this filter to find users who have or have not interacted with campaigns or Canvases with a given tag:

- Clicked an email
- Clicked an in-app message
- Directly opened a push notification
- Opened an email
- Viewed an in-app message

![][16]

### Converted From Campaign 

Use this filter to find users who have or have not converted (based on the primary conversion) in your target campaign. 

For recurring campaigns, this filter refers to whether users have converted on the most recent message from the campaign.

![][12]

### Converted From Canvas 

Use this filter to find users who have or have not converted (based on the primary conversion) in your target Canvas.

For recurring Canvases this filter refers to whether users have ever converted anytime they've gone through the Canvas.

![][18]

### In Campaign Control Group 

Use this filter to find users who are or are not in the control group of your target campaign.

![][13]

### In Canvas Control Group 

Use this filter to find users who are or are not in the control group of your target Canvas, which can be selected in the dropdown.

![][19]

### Last received message from specific campaign 

Use this filter to find users who last received a specific campaign before or after a specified date or number of days. This filter doesn't consider when users received other campaigns.

![][14]

### Last received message from specific campaign or Canvas with tag 

Use this filter to find users who last received a specific campaign or Canvas with a given tag before or after a specified date or number of days. This filter doesn't consider when users received other campaigns or Canvases.

![][17]

### Received message from campaign 

Use this filter to find users who have or have not received your target campaign.

![][4]

### Received message from campaign or Canvas with tag 

Use this filter to find users who have or have not received a campaign or Canvas that has your target tag.

![][15]

## Advantages with retargeting campaigns

Retargeting is particularly effective when the original segment also included a specific action you want to see users take. For example, let's say you have a card targeted at users who have never made a purchase. The card advertises a promotion for a discounted in-app purchase. The initial segment looks like the following:

- Money Spent in App is exactly 0
- Last Used App less than 14 days ago

The total number of users in the segment is 100,000 and you know from the News Feed stats that 60,000 unique users viewed the card and 20,000 unique users clicked the card. Through the segmenter we can see how many of those users who clicked the card actually made a purchase:

- Money Spent in App is more than 0
- Clicked Card is Name of Card

After examining those stats, we can make a segment of users who clicked the card, but did not make a purchase:

- Money Spent in App is exactly than 0
- Clicked Card is Name of Card

We can retarget this segment with additional messaging around the promotion or another in-app purchase. Retargeting can be done with another News Feed card or through a messaging campaign. A multichannel approach allows you to reach users where they're most likely to respond, thus increasing the effectiveness of your campaigns.

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
