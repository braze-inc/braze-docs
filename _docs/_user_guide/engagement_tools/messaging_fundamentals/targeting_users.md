---
nav_title: Targeting Users
article_title: Targeting Users
page_order: 9
page_type: reference
description: "This reference article covers how to target your audience in your campaign and Canvas editors."
tool:
    - Campaigns
    - Canvas
---

# Targeting users

> 

After you have [composed your campaign][1] and determined your [delivery schedule][2], you can set the target recipients of your campaign on the **Target Audiences** step.

## Targeting options

In the **Targeting Options** section, you'll find a few options for who you can send your campaign to.

{% alert note %}
Only the users who match your defined criteria will receive the campaign. Keep in mind that exact segment membership is always calculated just before the message is sent.
{% endalert %}

### Target users in an existing segment {#existing-segment}

To target members of a previously created segment, select one segment from the dropdown under **Target Users by Segment**.

### Target users in multiple existing segments {#multiple-existing-segment}

To target users that fall into multiple previously created segments, add multiple segments from the dropdown under **Target Users by Segment**. The resulting target audience will be users both in the first segment and the second segment and the third segment, etc.

### Target users in multiple existing segments and filters {#existing_segment_filter}

You can also target users of one or more previously created segments that also fall under additional filters. After first selecting your segments, you can further refine your audience under the **Additional Filters** section. This is demonstrated in the following screenshot, which targets users that are in the Daily Active Users segment, Not Open Emails segment, and made a purchase less than 30 days ago.

![][25]

### Target users without segments {#without-segment}

To target users without adding a segment, you can use a series of filters. This means you do not need to target a campaign at a pre-existing segment, you can make an impromptu audience during campaign creation by just using the additional filters, and not selecting any segments under **Target Users By Segment**. This will allow you to skip segment creation when sending campaigns to one-off audiences.

![][26]

## Targeting Seed Groups

For email campaigns, you can target Seed Groups under the **Seed Groups** section. Note that Seed Groups aren't available for API campaigns, although you can include Seed Groups via an API-triggered entry in a campaign. For more information, see [Seed Groups]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Testing your audience

After adding segments and filters to your audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm if they match the audience criteria.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## Audience summary

Once you have added segments or filters to fine tune your audience, the **Audience Summary** will show an overview of who is in your target audience. Here, you can further limit your campaign audience by setting a maximum user cap, or [rate-limiting][3] delivery speed. For email and push notification campaigns, you can select which subscription and opt-in status to target.

![][27]

## A/B testing

Under the **A/B Testing** section, you can set up a test to compare users' responses to multiple versions of the same marketing campaign. These versions share similar marketing goals but differ in wording and style. The objective is to identify the version of the campaign that best accomplishes your marketing goals. 

For more information and best practices, refer to [Multivariate & A/B Testing][4].

## Audience statistics

Braze provides detailed audience statistics of the targeted channels in the footer. 

The larger your user base is, the more likely the **Reachable Users** amount is a rough estimate. The number of reachable users may decrease if you use a [Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) or set up message eligibility. Select [Calculate exact statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) to determine an accurate number for your reachable users as this will search through every user in your user base. 

Note the following details for audience statistics:

- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

![][24]

To see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, select **Show Additional Statistics**.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}