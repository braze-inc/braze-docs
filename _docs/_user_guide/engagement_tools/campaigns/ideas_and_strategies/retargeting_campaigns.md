---
nav_title: Retargeting campaigns
article_title: Retarget Campaigns
page_order: 2
page_type: reference
description: "This reference article goes over how and why you should consider retargeting campaigns based on messages your users receive."
tool:
  - Campaigns
  
---

# Retarget campaigns

> By retargeting campaigns based on the user's previous actions, like whether or not they opened an email, you can help reclassify your users, opening the door to an effective, data-driven marketing approach.

Braze provides support for retargeting users based on messages they have received. You can retarget users based upon their interactions with your campaigns and Canvases. 

Each of these retargeting filters provides you with several options after you add them. For more on targeting users, check out our [Braze Learning course](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup!

![Segment Details section with the dropdown menu for the available filters.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Retargeting filters

You can use the retargeting filters in this section for your users within your campaigns and Canvases.

### Clicked/Opened Campaign

Use this filter to find users who have or have not:

- Clicked an email
- Clicked an in-app message
- Directly opened a push notification
- Opened an email
- Viewed an in-app message

![]({% image_buster /assets/img_archive/clickedopened.png %})

This can be further specified by selecting which campaign you want to retarget.

### Clicked or opened Campaign or Canvas with tag

Use this filter to find users who have or have not interacted with campaigns or Canvases with a given tag:

- Clicked an email
- Clicked an in-app message
- Directly opened a push notification
- Opened an email
- Viewed an in-app message

![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Converted From Campaign 

Use this filter to find users who have or have not converted (based on the primary conversion) in your target campaign. 

For recurring campaigns, this filter refers to whether users have converted on the most recent message from the campaign.

![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Converted From Canvas 

Use this filter to find users who have or have not converted (based on the primary conversion) in your target Canvas.

For recurring Canvases this filter refers to whether users have ever converted anytime they've gone through the Canvas.

![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### In Campaign Control Group 

Use this filter to find users who are or are not in the control group of your target campaign.

![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### In Canvas Control Group 

Use this filter to find users who are or are not in the control group of your target Canvas, which can be selected in the dropdown.

![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Last received message from specific campaign 

Use this filter to find users who last received a specific campaign before or after a specified date or number of days. This filter doesn't consider when users received other campaigns.

![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Last received message from specific campaign or Canvas with tag 

Use this filter to find users who last received a specific campaign or Canvas with a given tag before or after a specified date or number of days. This filter doesn't consider when users received other campaigns or Canvases.

![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Received message from campaign 

Use this filter to find users who have or have not received your target campaign.

![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Received message from campaign or Canvas with tag 

Use this filter to find users who have or have not received a campaign or Canvas that has your target tag.

![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Advantages with retargeting campaigns

Retargeting is particularly effective when the original segment also included a specific action you want to see users take. For example, let's say you have a card targeted at users who have never made a purchase. The card advertises a promotion for a discounted in-app purchase. The initial segment looks like the following:

- Money Spent in App is exactly 0
- Last Used App less than 14 days ago

The total number of users in the segment is 100,000 and you know from the Content Card stats that 60,000 unique users viewed the card and 20,000 unique users clicked the card. Through the segmenter we can see how many of those users who clicked the card actually made a purchase:

- Money Spent in App is more than 0
- Clicked Card is Name of Card

After examining those stats, we can make a segment of users who clicked the card, but did not make a purchase:

- Money Spent in App is exactly than 0
- Clicked Card is Name of Card

We can retarget this segment with additional messaging around the promotion or another in-app purchase. Retargeting can be done with a messaging campaign. A multichannel approach allows you to reach users where they're most likely to respond, thus increasing the effectiveness of your campaigns.

