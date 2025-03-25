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

> Determining how to target your users is one of the most crucial steps when creating a campaign or Canvas. By understanding how to segment your audience based on their behaviors, preferences and demographics, you can tailor and personalize your messaging.

## Targeting options for campaigns and Canvases

In the **Targeting Options** section, you'll find a few options to determine the audience for your campaign and Canvas. Only the users who match your defined criteria will receive the message. Keep in mind that exact segment membership is always calculated just before the message is sent.

### Users in an existing segment {#existing-segment}

To target members of a previously created segment, select one segment from the dropdown under **Target Users by Segment**.

### Users in multiple existing segments {#multiple-existing-segment}

To target users that fall into multiple previously created segments, add multiple segments from the dropdown under **Target Users by Segment**. The resulting target audience will be users both in the first segment and the second segment and the third segment, etc.

### Users in multiple existing segments and filters {#existing_segment_filter}

You can also target users of one or more previously created segments that also fall under additional filters. After first selecting your segments, you can further refine your audience under the **Additional Filters** section. This is demonstrated in the following screenshot, which targets users that are in the "Daily Active Users" segment, "Never opened email" segment, and made a purchase more than 30 days ago.

![Targeting options for a message that include two segments and have an additional filter for a last purchase made less than 30 days ago.][25]{: style="max-width:70%;"}

### Users without segments {#without-segment}

To target users without adding a segment, you can use a series of filters. This is an impromptu audience during message creation and allows you to skip segment creation when sending to one-off audiences.

![Additional filters for a message that targets users who've last opened an app within the day, have never received a campaign or Canvas step, and who made a purchase less than 30 days ago.][26]{: style="max-width:70%;"}

## Targeting Seed Groups

For email campaigns, you can target Seed Groups under the **Seed Groups** section. Note that Seed Groups aren't available for API campaigns, although you can include Seed Groups via an API-triggered entry in a campaign. For more information, see [Seed Groups]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Testing your audience

After adding segments and filters to your audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm if they match the audience criteria.

![The "User Lookup" section with a button "Lookup User".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%"}

### Audience summary

After adding segments or filters to fine tune your audience, the **Audience Summary** will show an overview of who is in your target audience. Here, you can further limit your audience by setting a maximum user cap or [rate-limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) delivery speed.

![The "Audience Summary" section with options to set a maximum user cap or rate limit delivery speed.][27]

### A/B testing

In the **A/B Testing** section, you can set up a test to compare users' responses to multiple versions of the same marketing campaign. These versions share similar marketing goals but differ in wording and style. The objective is to identify the version of the campaign that best accomplishes your marketing goals. 

For more information and best practices, refer to [Multivariate & A/B Testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Audience statistics

Braze provides detailed audience statistics of the targeted channels in the footer. 

The larger your user base is, the more likely the **Reachable Users** amount is a rough estimate. The number of reachable users may decrease if you use a [Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) or set up message eligibility. 

Select [Calculate exact statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) to determine an accurate number for your reachable users as this will search through every user in your user base.

To see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, select **Show Additional Statistics**.

Note the following details for audience statistics:

- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

![The "Total Population" section with estimated counts for reachable users in each targeted channel.][24]

To see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, select **Show Additional Statistics**.


[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
