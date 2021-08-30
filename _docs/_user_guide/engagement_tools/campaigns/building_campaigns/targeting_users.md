---
nav_title: Targeting Users
article_title: Targeting Users
page_order: 4
tool: Campaigns
page_type: reference
description: "This reference article "
---

# Targeting Users

Once you have [composed your campaign][1] and determined your [delivery schedule][2], you can set the target recipients of your campaign on the **Target Users** step. Only the users who match your defined criteria will receive the campaign. Keep in mind that exact segment membership is always calculated just before the message is sent.

## Targeting Options

Under the **Targeting Options** section, you'll find a few options for who you can send your campaign to.

### Target Members of an Existing Segment

To target members of a previously created segment, select one segment from the dropdown under **Target Users by Segment**.

### Target Users in Multiple Existing Segments

To target users that fall into multiple previously created segments, add multiple segments from the dropdown under **Target Users by Segment**. The resulting target audience will be users both in the first segment and the second segment and the third segment, etc.

### Target Users in Multiple Existing Segments and Filters

You can also target users of one or more previously created segments that also fall under additional filters. After first selecting your segments, you can further refine your audience under the **Additional Filters** section. This is demonstrated in the screenshot below, which targets users that are in the 10 Unread Messages segment and in the Active Users segment, and made a purchase less than 30 days ago.

> Update this screenshot

![Multi-Channel Footer][25]

### Target Users Without Segments

To target users without adding a segment, you can use a series of filters. This means you do not need to target a campaign at a pre-existing segment, you can make an ad hoc audience during campaign creation by just using the additional filters, and not selecting any segments under **Target Users By Segment**. This will allow you to skip segment creation when sending campaigns to one-off audiences.

## Audience Summary

## A/B Testing

## Audience Statistics

Braze provides detailed audience statistics of the targeted channels in the footer. 

![Segmenter][24]

In order to see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, click **Show Additional Stats** located below the stats footer.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}