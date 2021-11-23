---
nav_title: Global Control Group
article_title: Global Control Group
alias: /global_control_group/
page_order: 0

description: "This article covers how to set up and properly use the Global Control Group. It also covers how to view reports and metrics brought on by the use of these groups."
page_type: reference
tool: Reports

---

# Global Control Group

> This article covers how to set up and properly use the Global Control Group. It also covers how to view reports and metrics brought on by the use of these groups.

With the Global Control Group, you can set a percentage of all users as a control group. Once saved, users in the group will not receive any campaigns or Canvases. The Global Control Group allows you to analyze the overall impact of your messaging efforts over time. By comparing the behaviors of users that receive messaging to those that don't, you can further understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events.

## How the Global Control Group works

Your Global Control Group is applied to all channels, campaigns, and Canvases, with the exception of News Feed Cards. Users in your control group will still receive News Feed Cards. This exception doesn't extend to Content Cards—if you're using Content Cards, users in your control group won't receive them.

__Assigning users randomly to the Global Control Group:__<br> Braze randomly selects multiple ranges of [Random Bucket Numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) and includes users from those selected buckets. If you are currently using Random Bucket Numbers for any other purposes, please read the section [things to watch out for](#things-to-watch-for) below. <br><br>
__Data tracking for reporting:__<br>Braze measures the behaviors of users in your control group and users in your treatment sample. Your treatment sample is a random selection of users not in your control group, generated using the same Random Bucket Number method mentioned above.

## Create a Global Control Group

### Step 1: Navigate to the Global Control Group Settings.

From the dashboard, go to **Global Message Settings** under **Engagement**, and select the **Global Control Group Settings** tab.

### Step 2: Assign a percentage of all users to this control group

Input a percentage for your control group and click __Save__. Once entered, Braze shows you an estimate of how many users will fall into your Global Control, treatment, and treatment sample. Keep in mind that the more users you have in your app group, the more accurate this estimate will be. 

The number of users in your Global Control Group is automatically updated after its initial setup to remain proportionate to this audience percentage when more users are added to your app group. For percentage guidelines, refer to the [best practices section](#percentage-guidelines) below.

![Global Control Group][4]

### Step 3: Assign exclusion settings

Use tags to add exclusion settings to your Global Control Group. Any campaigns or Canvases that use the tags included in the exclusion settings don't use your Global Control Group. These campaigns and Canvases continue to send to every user in the target audience, including those in your Global Control Group.

{% alert tip %}
You may want to add exclusion settings if you have transactional messages that should send to every user.
{% endalert %}

![Global Control Group][5]

### Step 4: Save your control group

At this point, Braze generates a randomly selected group of users to comprise the selected percentage of your total user base. Once saved, all currently active and future campaigns and Canvases no longer send to users in this group, except for campaigns or Canvases that contain any of the tags in your exclusion settings.

## Disable your Global Control Group

You can disable your Global Control Group at any time, but keep in mind that doing so will result in users in this group immediately becoming eligible for campaigns and Canvases.

__Before disabling your Control Group__ we recommend [exporting](#export-group-members) a CSV of users in that group in case you need to reference it at a later point. Once you disable a control group, there is no way for Braze to restore the group or identify which users were in this group.

__After disabling your Control Group__ you can save a new one. Once you enter a percentage and save it, Braze generates a new randomly selected group of users. If you enter the same percentage as before, Braze still generates a new group of users for your control and treatment groups.

![Global Control Group][2]

## Export your control group members {#export-group-members}

If you'd like to see which users are in your Global Control Group, you can export your Group's members via CSV or API. To run a CSV export, navigate to the **Global Control Group Settings** tab, on the **Global Message Settings** page. To export via API, use the [Users by Global Control Group]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) API endpoint.

{% alert important %}
Historical control groups are not preserved, so you can only export the members of your current group. Make sure to export any necessary information before disabling a control group.
{% endalert %}

## View reporting

To view a report for your Global Control Group from the dashboard, navigate to __Global Control Group__ under __Data__. Next, select the parameter you wish to run your report with (sessions or a particular custom event) and click __Run Report__.

![Global Control Group][6]

### About your report

The Global Control Group Report allows you to compare your group against a treatment sample. Your treatment sample is a random selection of non-control users, approximately the same number of users as your control, generated using the Random Bucket Number method.

When generating your report, choose an event—either sessions or any custom event—to compare across your treatment and control groups. Then choose a time period for which to view data for. Keep in mind that if you’ve saved multiple control group experiments at different time periods, you should avoid including data from more than one experiment in your report.

Lastly, as with several other reports on our platform, this report displays a [confidence]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) percentage for your change from control metric. Note that in cases where the conversion rate between your control and treatment are identical, a confidence of 0% is to be expected; this indicates that there is a 0% chance that there is a difference in performance between the two groups.

### Report metrics

| Metric | Definition | Calculation |
| -- | -- | -- |
| Change from Control | This calculates the uplift between the conversion rate for your treatment and control groups. | ((Treatment conversion rate – control conversion rate) ÷ control conversion rate) * 100 |
| Incremental Uplift | The difference in total events between your treatment and control groups. This metric seeks to answer the question of “How many more conversion events did the treatment group achieve?”. | Total events for treatment – total events for control |
| Incremental Uplift Percent | The percentage of your treatment’s total events that can be attributed to your treatment (versus natural user behavior). This is calculated by dividing incremental uplift (number) by the total number of events for your treatment group. | Incremental uplift (number) ÷ Total events for treatment group |
| Conversion Rate | On average, the percentage of users in your control/ treatment group that complete your selected event each day during the chosen time period. | Average (mean) of the percent of users that perform your selected event each day during the chosen time period. |
| Estimated Group Size | The estimated number of users in your control and treatment groups during selected time period. | The maximum membership size your control and treatment groups reached during the time period you chose for the report. |
| Total Number of Events | The total number of times the selected event occurred during the chosen time period. This is not unique (ie. if a user performs an event twice during time period, the event gets incremented twice). | Sum of the number of times event occurred each day during the chosen time period. |
| Events Per User | The estimated average number of times users in each group completed your conversion events during the selected time period. | Total events ÷ estimated group size. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Troubleshooting

As you set up your global control groups and view reporting, here are errors you may run into:

| Issue | Troubleshooting |
| --- | --- |
| Unable to save the percentage entered when designating a Global Control Group. | This issue occurs if you enter a non-integer or an integer that is not between 1 and 15 (inclusive). |
| "Braze is not able to update your Global Control Group" error on the Global Control settings page. | This usually indicates that some component of this page has changed, likely due to actions taken by another user on your Braze account. In this case, refresh the page and retry. |
| Global Control Group report does not have any data. | If you access the Global Control Group Report without having saved a Global Control Group, you will not see any data in the report. Create and save a Global Control Group and try again. |
{: .reset-td-br-1 .reset-td-br-2}

### Things to watch out for {#things-to-watch-for}

#### Overlapping Random Bucket Numbers

Your Global Control Group is formed using Random Bucket Numbers, and thus if you are running any other tests using Random Bucket Numbers segment filters, keep in mind that there could be an overlap between those segments you create, and your Global Control Group users.

#### Duplicate email addresses

If two users who have different external user IDs have the same email address, and one of these users is in the control group and the other is not, then an email will still be sent to that email address whenever the non-control group user is eligible for an email. When this occurs, we will mark both user profiles as having received the campaign or Canvas containing that email.

#### Global Control Group and message-specific control groups

It's possible to have both a Global Control Group and also use a campaign-specific or Canvas-specific control group. Having a campaign-specific or Canvas-specific control group lets you measure the impact of a particular message.

Users in your Global Control Group are withheld from receiving any messages other than those with tag exceptions, and if you add a control to a campaign or Canvas, Braze withholds a portion of your global treatment group from receiving that particular campaign or Canvas. That means if a member of the Global Control Group is not eligible to receive a particular campaign or Canvas, they will also not be present in the control group for that particular campaign or Canvas.

> In short, users in the Global Control Group are filtered out of the campaign or Canvas audience prior to entry. Of the users who enter the campaign or Canvas, a percentage of those are then assigned to the control variant.

#### Global Control Group segments on the Developer Console

You may see multiple **Global Control** segments in the **Additional API Identifiers** section of the **Developer Console**. This is because each time the Global Control Group is enabled or disabled, a new Global Control Group is formed. This leads to multiple segments labeled "Global Control Group".

Only one of these segments is active and can be queried using the [Users by Global Control Group]({{site.baseurl}}api/endpoints/export/user_data/post_users_global_control_group/) API endpoint, or exported from the dashboard. The export from the dashboard specifically states which subsegments make up this Global Control Group.

## Testing best practices

### Optimal control group size {#percentage-guidelines}

<br>__Two main rules to keep in mind are__:<br>- Your control group should be no smaller than 1000 users.<br>- Your control group should be no more than 10% of your entire audience.

If you have a total audience that’s smaller than 10,000, you should increase your percentage to create a group of over 1000 users; in this case, you should not increase your percentage above 15%. Keep in mind that the smaller your overall app group size is, the more challenging it will be to run a statistically rigorous test.
- Some trade-offs to consider when thinking about your control group size are that you need a significantly large number of customers in your control group so that any behavior analysis created is trustworthy. However, the larger your control group is, the fewer customers are getting your campaigns, which is a downside if you’re using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience will depend on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you will need a larger percentage for your control group.

### Experiment duration 

#### Choose an ideal duration {#reshuffle}

How long to run your experiment before reshuffling control group membership depends on what you’re testing and what your users’ baseline behaviors are. If you aren’t sure, a good place to start is one quarter (3 months), and you should not go shorter than 1 month.

To determine the appropriate length of time for your experiment, consider what questions you’re hoping to answer. For instance, are you looking to see if there’s a difference in sessions? If so, think about how often your users have sessions organically. Brands whose users have sessions every day can run shorter experiments than brands whose users have sessions only a couple of times a month. 

Or, maybe you’re interested in purchasing behaviors. Then your experiment would most likely need to run for longer than an experiment where you’re examining sessions, since it’s likely your users make purchases less frequently.

{% alert tip %}
The longer you hold the same control group out the more they diverge from the treatment group, which can create bias. Resetting the Global Control Group rebalances the population.
{% endalert %}

#### Try to limit ending experiments prematurely

You should decide how long to run your experiment before beginning it, and then you should only end your experiment and gather final results once you’ve reached this pre-determined point. Ending your experiment early, or whenever you see promising data, will introduce bias.

#### Think about valuable metrics

Consider any baseline behaviors for the metrics you’re most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you’d like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. Once you decide how long your experiment should run, be sure to not end your experiment or record final results early, or your findings may be biased.

[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}
