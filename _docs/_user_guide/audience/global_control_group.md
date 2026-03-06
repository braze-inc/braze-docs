---
nav_title: Global Control Group
article_title: Global Control Group
alias: /global_control_group/
page_order: 5
page_type: reference
description: "Learn how to set up and use the Global Control Group to measure the overall impact of your messaging efforts over time."
tool: 
  - Reports
search_rank: 1
toc_headers: h2

---

# Global Control Group

> Use the Global Control Group to specify a percentage of all users who shouldn't receive any campaigns or Canvases, allowing you to analyze the overall impact of your messaging efforts over time. 

By comparing the behavior of users who receive messaging with those who don't, you can better understand how your marketing campaigns and Canvases contribute to an uplift in sessions and custom events.

## How the Global Control Group works

With the Global Control Group, you can set a percentage of all users as a control group. When saved, users in the group do not receive any campaigns or Canvases. 

{% alert important %}
Your Global Control Group applies to all channels, campaigns, and Canvases, except for [API campaigns]({{site.baseurl}}/api/api_campaigns). This means users in your control group still receive API campaigns. However, this exception doesn't apply to Content Cards. If you're using an API-triggered Content Card campaign, users in your control group won't receive them.
{% endalert %}

### Assign users randomly to the Global Control Group

Braze randomly selects multiple ranges of [random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) and includes users from those selected buckets. If you are currently using random bucket numbers for any other purposes, check out [Things to watch out for](#things-to-watch-for). 

When your Global Control Group is generated, all users with random bucket numbers are part of the group. Additionally, new users who join after this point (those acquired after the Global Control Group was generated) that have these random bucket numbers are also added to the Global Control Group. Similarly, if many users are deleted, you can expect the size of your Global Control Group to shrink because a percentage of those deleted users has fallen into this group. This maintains the size of your group as a constant percentage relative to your entire user base.

### Assign users randomly to the treatment group for reporting

Braze also creates a treatment group for reporting on uplift. The treatment group is a randomly selected group of users not part of your Global Control Group, and is generated using the same random bucket number method as the Global Control Group. 

Your treatment group is similar in size to your Global Control Group, but it is unlikely to be the exact same size. For [reporting](#reporting), Braze measures the behaviors of users in your control group and users in your treatment sample. Each workspace has a maximum of one Global Control Group and one treatment sample group. The treatment sample group is the same group of users regardless of how you configure your Global Control reporting.

### Exclude users from feature flags

You can't enable [feature flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags/) for users in your Global Control Group. This means users in your Global Control Group also can't be part of feature flag experiments.

### Exclude users from the Global Control Group

You can't remove specific users from the Global Control Group, but you can add [exclusion settings](#step-3-assign-exclusion-settings) so that campaigns and Canvases with specified tags **don't** use the Global Control Group. You can also disable and re-enable your Global Control Group to shuffle membership. The ideal duration for shuffling users varies based on the type of test that you're running, but try to shuffle no more than once a month.

## Create a Global Control Group

### Step 1: Navigate to the Global Control Group settings

From the dashboard, go to **Audience** > **Global Control Group**.

### Step 2: Assign a percentage of all users to this control group

Input a percentage for your control group and select **Save**. When entered, Braze shows you an estimate of how many users fall into your Global Control, treatment, and treatment sample. Keep in mind that the more users you have in your workspace, the more accurate this estimate is. 

The number of users in your Global Control Group automatically updates after its initial setup to remain proportionate to this percentage when more users are added to your workspace. Additionally, users who join after the Global Control Group is set up and who have random bucket numbers are also added to the Global Control Group. If many users are added, the size of your Global Control Group grows to maintain a constant percentage relative to your entire user base. When the size of your Global Control Group grows, the users who were previously in the group still remain in the group (unless you make changes to your group by disabling it and creating a new one).

For percentage guidelines, refer to [Testing best practices](#percentage-guidelines).

![The Global Control Group Settings with the Audience Settings set to "Assign five percent of all users to the Global Control Group".]({% image_buster /assets/img/control_group/control_group4.png %})

### Step 3: Assign exclusion settings

Use tags to add exclusion settings to your Global Control Group. Any campaigns or Canvases that use the tags included in the exclusion settings don't use your Global Control Group. These campaigns and Canvases continue to be sent to every user in the target audience, including those in your Global Control Group.

{% alert tip %}
You may want to add exclusion settings if you have transactional messages that should be sent to every user.
{% endalert %}

![The section to add or edit exclusion settings for your Global Control Group.]({% image_buster /assets/img/control_group/control_group5.png %})

### Step 4: Save your control group

At this point, Braze generates a randomly selected group of users to comprise the selected percentage of your total user base. When saved, all currently active and future campaigns and Canvases no longer send to users in this group, except for campaigns or Canvases that contain any of the tags in your exclusion settings.

## Making changes to your Global Control Group

You can only make changes to your Global Control Group by disabling it and creating a new one. For example, if you set up a Global Control Group that is 10% of your audience and you want to decrease its size to 5%, you must disable your current Global Control Group and re-enable a new Global Control Group. 

You can disable your Global Control Group at any time from the **Global Control Group Settings** tab, but keep in mind that doing so results in users in this group immediately becoming eligible for campaigns and Canvases.

Before disabling your Control Group, [export](#export-group-members) a CSV of users in that group in case you need to reference it at a later point. When you disable a control group, there is no way for Braze to restore the group or identify which users were in this group.

After disabling your Control Group, you can save a new one. When you enter a percentage and save it, Braze generates a new randomly selected group of users. If you enter the same percentage as before, Braze generates a new group of users for your control and treatment groups.

![A dialog box titled "You are making changes to Global Messaging Settings" with text warning that once your Global Control Group is disabled, it is no longer excluded from any new or active campaigns or Canvases.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Export your control group members {#export-group-members}

If you'd like to see which users are in your Global Control Group, you can export your Group's members by CSV or API. 

To run a CSV export, navigate to the **Global Control Group Settings** tab and click <i class="fas fa-download"></i>&nbsp;**Export**. To export by API, use the [`/users/export/global_control_group` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Historical control groups are not preserved, so you can only export the members of your current group. Make sure to export any necessary information before disabling a control group.
{% endalert %}

## View whether a user is in a Global Control Group

You can view Global Control Group membership by going to the **Miscellaneous** section in the **Engagement** tab of an individual user's profile.

![A "Miscellaneous" section reporting that the user has a random bucket number of 6356 and is not in the Global Control Group.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Reporting

The Global Control Group Report allows you to compare your group against a treatment sample. Your treatment sample is a random selection of non-control users, approximately the same number of users as your control, generated using the Random Bucket Number method.

### Viewing a report

To view a report for your Global Control Group from the dashboard, go to **Analytics** > **Global Control Group Report**. 

Next, select the parameter you want to run your report with (sessions or a particular custom event) and select **Run Report**.

![]({% image_buster /assets/img/control_group/control_group6.png %})

### Configuring your report

When generating your report, choose an event—either sessions or any custom event—to compare across your treatment and control groups. Then choose a time period for which to view data. Keep in mind that if you've saved multiple control group experiments at different time periods, you should avoid including data from more than one experiment in your report.

Keep in mind that the percentage metrics in your report are rounded. For example, in cases where the number of conversions is a very low percentage of your overall control or treatment group, the conversion rate may round to 0%.

This report also displays a [confidence]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) percentage for your change from control metric. In cases where the conversion rate between your control and treatment are identical, a confidence of 0% is expected — this indicates that there is a 0% chance of a difference in performance between the two groups. 

#### Group sizes

Before May 2024, the Global Control Group was excluded from user archival, but the treatment sample group was not. Starting May 2024, both groups are excluded from user archival. This could result in your treatment sample group and Global Control Group having significantly different sizes. The next time you reset your Global Control Group, this discrepancy will resolve and you'll see similar group sizes.

{% alert note %}
Each workspace has a maximum of one Global Control Group and one treatment sample group. The treatment sample group is the same group of users regardless of how you configure your Global Control reporting.
{% endalert %}

### Report metrics

| Metric | Definition | Calculation |
| -- | -- | -- |
| Change from Control | This calculates the uplift between the conversion rate for your treatment and control groups. | ((Treatment conversion rate – control conversion rate) ÷ control conversion rate) * 100 |
| Incremental Uplift | The difference in total events between your treatment and control groups. This metric seeks to answer the question of "How many more conversion events did the treatment group achieve?". | Total events for treatment – total events for control |
| Incremental Uplift Percent | The percentage of your treatment's total events that can be attributed to your treatment (versus natural user behavior). This is calculated by dividing incremental uplift (number) by the total number of events for your treatment group. | Incremental uplift (number) ÷ Total events for treatment group |
| Conversion Rate | The estimated percentage of users in your control or treatment group that complete your selected event during the time period selected. This is calculated by adding the number of events from the time period and dividing it by the sum of users within the group each day. This can only be approximated because group size fluctuates regularly as new users enter your Global Control Group, and events are total—and not unique—events. If the number of conversions is very small and your control or treatment groups are very large, then the conversion rate may round to 0%. If the number of events is very high—for example, in cases where one user may do more than one event per day—then the conversion rate can be over 100%. | Sum of the number of events for those users over that time period ÷ sum of users in the group each day |
| Estimated Group Size | The estimated number of users in your control and treatment groups during selected time period. | The maximum membership size your control and treatment groups reached during the time period you chose for the report. |
| Total Number of Events | The total number of times the selected event occurred during the chosen time period. This is not unique (for example, if a user performs an event twice during the time period, the event gets incremented twice). | Sum of the number of times an event occurred each day during the chosen time period. |
| Events Per User | The estimated average number of times users in each group completed your conversion events during the selected time period. | Total events ÷ estimated group size. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Troubleshooting

As you set up your global control groups and view reporting, here are the errors you may run into:

| Issue | Troubleshooting |
| --- | --- |
| Unable to save the percentage entered when designating a Global Control Group. | This issue occurs if you enter a non-integer or an integer that is not between 1 and 15 (inclusive). |
| "Braze is not able to update your Global Control Group" error on the Global Control settings page. | This usually indicates that some component of this page has changed, likely due to actions taken by another user on your Braze account. In this case, refresh the page and retry. |
| Global Control Group report does not have any data. | If you access the Global Control Group Report without having saved a Global Control Group, you do not see any data in the report. Create and save a Global Control Group and try again. |
| My conversion rate is 0% or I'm not seeing the graph display, even though there are more than zero events occurring. | If the number of conversions is very small and your control or treatment groups are very large, then the conversion rate may round to 0%, and thus not show up in the graph. You can verify this by checking the Total Number of Events metric. You could compare the effectiveness of your two groups using the incremental uplift percent metric.  |
| My conversion rate (or other metrics) are changing drastically depending on the time period I'm viewing data for. | If you're viewing data over short time periods, it's possible for your metrics to fluctuate day to day or week to week. View metrics over the course of at least one month. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Things to watch out for {#things-to-watch-for}

#### Overlapping Random Bucket Numbers

Your Global Control Group is formed using Random Bucket Numbers, and thus, if you are running any other tests using Random Bucket Numbers segment filters, keep in mind that there could be an overlap between those segments you create, and your Global Control Group users.

#### Duplicate email addresses

If two users with different external user IDs have the same email address, and one of these users is in the control group and the other is not, then an email is still sent to that email address when the non-control group user is eligible for an email. When this occurs, both user profiles are marked as having received the campaign or Canvas containing that email.

#### Global Control Group and message-specific control groups

It's possible to have both a Global Control Group and also use a campaign-specific or Canvas-specific control group. Having a campaign-specific or Canvas-specific control group lets you measure the impact of a particular message.

Users in your Global Control Group are withheld from receiving any messages other than those with tag exceptions, and if you add a control to a campaign or Canvas, Braze withholds a portion of your global treatment group from receiving that particular campaign or Canvas. That means if a member of the Global Control Group is not eligible to receive a particular campaign or Canvas, they are not present in the control group for that particular campaign or Canvas.

> In short, users in the Global Control Group are filtered out of the campaign or Canvas audience prior to entry. Of the users who enter the campaign or Canvas, a percentage of those are then assigned to the control variant.

#### Global Control Group segments on the Developer Console

You may see multiple **Global Control** segments in the **Additional API Identifiers** section of the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page. This is because each time the Global Control Group is enabled or disabled, a new Global Control Group is formed. This leads to multiple segments labeled "Global Control Group".

Only one of these segments is active and can be queried using the [`/users/export/global_control_group` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), or exported from the dashboard. The export from the dashboard specifically states which subsegments make up this Global Control Group.

## Testing best practices

### Optimal control group size {#percentage-guidelines}

Two main rules to keep in mind:
1. Your control group should be no smaller than 1000 users.
2. Your control group should be no more than 10% of your entire audience.

If you have a total audience that's smaller than 10,000, you should increase your percentage to create a group of over 1000 users; in this case, you should not increase your percentage higher than 15%. Keep in mind that the smaller your overall workspace size is, the more challenging it is to run a statistically rigorous test.

- Some trade-offs to consider when thinking about your control group size are that you need a significantly large number of customers in your control group so that any behavior analysis created is trustworthy. However, the larger your control group is, the fewer customers are getting your campaigns, which is a downside if you're using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience depends on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you need a larger percentage for your control group.

### Experiment duration 

#### Choose an ideal duration {#reshuffle}

How long to run your experiment before reshuffling control group membership depends on what you're testing and what your users' baseline behaviors are. If you aren't sure, a good place to start is one quarter (three months), but you should not go shorter than one month.

To determine the appropriate length of time for your experiment, consider what questions you're hoping to answer. For instance, are you looking to see if there's a difference in sessions? If so, think about how often your users have sessions organically. Brands whose users have sessions every day can run shorter experiments than brands whose users have sessions only a couple of times a month. 

Or, you might be interested in a custom event, so your experiment may need to run for longer than an experiment where you're examining sessions if it's likely your users trigger that custom event less frequently.

{% alert tip %}
The longer you hold the same control group out, the more they diverge from the treatment group, which can create bias. Resetting the Global Control Group rebalances the population.
{% endalert %}

#### Try to limit ending experiments prematurely

Decide how long to run your experiment before beginning it, and then only end your experiment and gather final results after you reach this pre-determined point. Ending your experiment early, or whenever you see promising data, introduces bias.

#### Think about valuable metrics

Consider any baseline behaviors for the metrics you're most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you'd like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. After you decide how long your experiment should run, be sure not to end your experiment or record final results early, or your findings may be biased.
