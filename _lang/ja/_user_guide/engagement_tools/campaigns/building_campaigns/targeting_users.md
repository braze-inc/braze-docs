---
nav_title: Targeting Users
article_title: Targeting Users
page_order: 4
tool: Campaigns
page_type: reference
description: "This reference article covers the Targeting Options found in the Target Audiences step of campaign creation."
---

# Targeting users

> After you have [composed your campaign][1] and determined your [delivery schedule][2], you can set the target recipients of your campaign on the **Target Audiences** step. 

## Targeting options

Under the **Targeting Options** section, you'll find a few options for who you can send your campaign to.

{% alert note %}
Only the users who match your defined criteria will receive the campaign.Keep in mind that exact segment membership is always calculated just before the message is sent.
{% endalert %}

### Target users in an existing segment {#existing-segment}

To target members of a previously created segment, select one segment from the dropdown under **Target Users by Segment**.

### Target users in multiple existing segments {#multiple-existing-segment}

To target users that fall into multiple previously created segments, add multiple segments from the dropdown under **Target Users by Segment**.The resulting target audience will be users both in the first segment and the second segment and the third segment, etc.

### Target users in multiple existing segments and filters {#existing_segment_filter}

You can also target users of one or more previously created segments that also fall under additional filters.After first selecting your segments, you can further refine your audience under the **Additional Filters** section.This is demonstrated in the following screenshot, which targets users that are in the Daily Active Users segment, Not Open Emails segment, and made a purchase less than 30 days ago.

![][25]

### Target users without segments {#without-segment}

To target users without adding a segment, you can use a series of filters.This means you do not need to target a campaign at a pre-existing segment, you can make an impromptu audience during campaign creation by just using the additional filters, and not selecting any segments under **Target Users By Segment**.This will allow you to skip segment creation when sending campaigns to one-off audiences.

![][26]

## Targeting Seed Groups

For email campaigns, you can target Seed Groups under the **Seed Groups** section.Note that Seed Groups aren't available for API campaigns, although you can include Seed Groups via an API-triggered entry in a campaign.For more information, see [Seed Groups]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Testing your audience

オーディエンスにセグメントとフィルターを追加したら、[ユーザーを検索]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/)してオーディエンスの条件と一致するかどうかを確認することで、オーディエンスが期待どおりに設定されているかどうかをテストできます。

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## オーディエンスの概要

Once you have added segments or filters to fine tune your audience, the **Audience Summary** will show an overview of who is in your target audience.Here, you can further limit your campaign audience by setting a maximum user cap, or [rate-limiting][3] delivery speed.For email and push notification campaigns, you can select which subscription and opt-in status to target.

![][27]

## A/B testing

Under the **A/B Testing** section, you can set up a test to compare users' responses to multiple versions of the same marketing campaign.These versions share similar marketing goals but differ in wording and style.The objective is to identify the version of the campaign that best accomplishes your marketing goals. 

For more information and best practices, refer to [Multivariate & A/B Testing][4].

## Audience statistics

Braze は、ターゲットチャンネルの詳細な視聴者統計をフッターに表示します。 

キャンペーンの場合、**正確な統計を計算**を選択して、到達可能なユーザーの正確な数を決定します。これにより、ユーザー群内のすべてのユーザーが検索されます。到達可能なユーザーの数は、[グローバルコントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)を使用するか、メッセージの適格性を設定すると減少する可能性があります。

セグメントの場合、ユーザー群が大きいほど、**到達可能なユーザー数**の量は概算である可能性が高くなります。詳細については、[正確な統計の計算]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)を参照してください。

![][24]

In order to see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, click **Show Additional Stats** located after the statistics footer.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
