---
nav_title: Global Control Group
alias: /global_control_group/
page_order: 0

description: "This article covers how to set up and properly use Global Control Groups. It also covers how to view reports and metrics brought on by the use of these groups."
page_type: reference
tool: 
- Campaigns
- Canvas
- Reports
---

# Global Control Groups

> Global Control Groups allow you to analyze the overall impact of your messaging efforts over time. These Groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events, by comparing the behaviors of users that receive messaging to those that don't.

## Create a Global Control Group

1. __Navigate to the Global Control Group settings__<br>From the dashboard, navigate to the Global Control Group tab located within __Global Message Settings__ under __Engagement__. <br><br>
2. __Assign a percentage of all users to this control group__<br> Input a percentage for your control group and __Save__. Once entered, Braze will show you an estimate of how many users will fall into your Global Control, treatment, and treatment sample. Keep in mind that the more users you have in your app group, the more accurate this estimate will be. Visit our [best practices section](#percentage-guidelines) for percentage guidelines.<br><br>![Global Control Group][4] <br><br>
3. __Assign exclusion settings__<br>Add exclusion settings to your global control group by using tags. Any campaigns that use the tags included here in the exclusion settings will __not use__ your global control group. These campaigns will continue to send to every user in the target audience (including those in your global control group). You may want to add exclusion settings if you have transactional messages that should send to every user.<br><br>![Global Control Group][5] <br><br>
4. __Save your control group__<br>At this point, Braze will generate a randomly selected group of users comprising the selected percentage of your total user base. Once saved, all currently active as well as future campaigns/Canvases __will no longer send to users in this group__, with the exception being campaigns/Canvases that contain any of the tags in your exclusion settings.

## How the Global Control Group Works

Your global control group will be applied to __all channels, campaigns as well as Canvases__, with the exception of News Feed Cards. Users in your control group _will not_ be excluded from News Feed Cards. If you are using Content Cards, users in your control group _will_ also be excluded from Content Cards.

__Assigning users randomly to the Global Control Group:__<br> Braze will randomly select multiple ranges of [Random Bucket Numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute), and include users from those selected buckets. If you are currently using Random Bucket Numbers for any other purposes, please read the “[things to watch out for](#things-to-watch-for)” section of this article. <br><br>
__Data tracking for reporting:__<br>Braze will measure the behaviors of those in your control group and those in your treatment sample. Your treatment sample is a random selection of users not in your control group, generated using the same Random Bucket Number method mentioned above.

## Disabling your Global Control Group

You can disable your global control group at any time, but keep in mind that doing so will result in users in this group immediately becoming eligible for campaigns/Canvases.

1. __Before Disabling your Control Group__ we recommend exporting a CSV of users in that group in case you need to reference it at a later point. Once you disable a control group, there will be no way for Braze to restore the group or identify which users were in this group.<br><br>
2. __After Disabling your Control Group__ you can save a new one. Once you enter a percentage and save it, Braze will generate a new randomly selected group of users. If you enter the same percentage as before, Braze will still generate a new group of users for your control and treatment groups.
 <br><br>![Global Control Group][2]
 
## Exporting your Control Group Members
 
If you'd like to see which users are in your global control group, you can export your Group's members via CSV or API. To run a CSV export, navigate to the global control group set up page under Global Message Settings. To export via API, use the [global control group API endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

Historical control groups are not preserved, so you can only export the members of your current Group. Make sure to export any necessary information before disabling a control group.

## Viewing Reporting

To view a reporting for your global control group, from the dashboard, navigate to __Global Control Group__ under __Data__. Next, select the parameter you wish to run your report with (sessions or a particular custom event) and click __Run Report__.

![Global Control Group][6]

### Understanding Your Report 

The global control group report allows you to compare your group against a treatment sample.
Your treatment sample is a random selection of con-control users, approximately the same number of users as your Control, generated using the Random Bucket Number method.

When generating your report, you will choose an event - either sessions or any custom event - to compare across your treatment and control groups. You will also choose a time period for which to view data for. Keep in mind that if you’ve saved multiple control group experiments at different time periods, you should avoid including data from more than 1 experiment in your report. Lastly, as with several other reports on our platform, this report displays a [confidence]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) percentage for your change from control metric. 

Tooltips within the product also contain information related to the descriptions of each report metric.

### Report Metrics

{% tabs %}
{% tab Conversion Rate %}
#### Conversion rate
On average, the percentage of users in your control/ treatment group that complete your selected event each day during the chosen time period

__Calculation__<br>
Average (mean) of the percent of users that perform your selected event each day during the chosen time period
{% endtab %}
{% tab Estimated Group Size%}
#### Estimated Group Size
The estimated number of users in your control and treatment groups during selected time period

__Calculation__<br>
The maximum membership size your control and treatment groups reached during the time period you chose for "Show Data For"
{% endtab %}
{% tab Total Number of Events%}
#### Total Number of Events
The total number of times the selected event occurred during the chosen time period - this is not unique (ie. if a user performs an event twice during time period, the event gets incremented twice)

__Calculation__<br>
Sum of the number of times event occurred each day during the chosen time period
{% endtab %}
{% tab Events Per User %}
#### Events Per User
The estimated average number of times users in each group completed your conversion events during the selected time period

__Calculation__<br>
Total events ÷ estimated group size
{% endtab %}
{% tab Change from Control %}
#### Change from Control
This calculates the uplift between the conversion rate for your treatment and control groups

__Calculation__<br>
((Treatment conversion rate - control conversion rate) ÷ control conversion rate) * 100
{% endtab %}
{% tab Incremental Lift %}
#### Incremental Lift
##### Incremental Lift (Number)
The difference in total events between your treatment and control groups. This metric seeks to answer the question of “How many more conversion events did the treatment group achieve?”

__Calculation__<br>
Total events for treatment - total events for control
##### Incremental Lift (Percentage)
The percentage of your treatment’s total events that can be attributed to your treatment (versus natural user behavior) - this is calculated by dividing incremental uplift (number) by the total number of events for your treatment group 

__Calculation__<br>
Incremental uplift (number) ÷ Total events for treatment group
{% endtab %}
{% endtabs  %}

## Potential Errors / Things to Watch For
As you set up your global control groups and view reporting, here are errors you may run into:

##### Unable to save the percentage entered when designating a Global Control Group
This issue occurs if you enter a non-integer or an integer that is not between 1 and 15 (inclusive). 

##### "Braze is not able to update your Global Control Group" error on the Global Control settings page
This usually indicates that some component of this page has changed, likely due to actions taken by another user on your Braze account. In this case, refresh the page and retry.

##### Global control group report does not have any data
If you access the global control report without having saved a global control group, you will not see any data in the report. Create and save a global control group and retry.

#### Things to Watch Out For {#things-to-watch-for}
- Your global control group is formed using Random Bucket Numbers, and thus if you are running any other tests using Random Bucket Numbers segment filters, keep in mind that there could be an overlap between those segments you create, and your global control group users.
- __If two users who have different external user IDs have the same email address,__ and one of these users is in the control group and the other is not, then an email will still be sent to that email address whenever the non-control group user is eligible for an email. When this occurs, we will mark both user profiles as having received the campaign or Canvas containing that email.
- It is possible to have a global control group and also use a campaign-specific or Canvas-specific control group. Having a campaign-specific or Canvas-specific control group lets you measure the impact of a particular message. Users in your global control group are withheld from receiving any messages (other than those with tag exceptions), and if you add a control to a campiagn or Canvas, Braze will withhold a portion of your Global Treatment group from receiving that particular campaign or Canvas. That is, if a member of the Global Control Group is not eligible to receive a particular campaign/Canvas, they will also not be present in the control group for that particular campaign/Canvas.

## Testing Best Practices

### Optimal Control Group Size {#percentage-guidelines}

<br>__Two main rules to keep in mind are__:<br>- Your control group should be no smaller than 1000 users.<br>- Your control group should be no more than 10% of your entire audience.

If you have a total audience that’s smaller than 10,000, you should increase your percentage to create a group of over 1000 users; in this case, you should not increase your percentage above 15%. Keep in mind that the smaller your overall app group size is, the more challenging it will be to run a statistically rigorous test.
- Some trade-offs to consider when thinking about your control group size are that you need a significantly large number of customers in your control group so that any behavior analysis created is trustworthy. However, the larger your control group is, the fewer customers are getting your campaigns, which is a downside if you’re using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience will depend on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you will need a larger percentage for your control group.

### Experiment Duration 

#### Choose an Ideal Duration {#reshuffle}

- How long to run your experiment before reshuffling control group membership depends on what you’re testing and what your users’ baseline behaviors are. If you aren’t sure, a good place to start is one quarter (3 months), and you should not go shorter than 1 month.
- To determine the appropriate length of time for your experiment, consider what questions you’re hoping to answer. For instance, are you looking to see if there’s a difference in sessions? If so, think about how often your users have sessions organically - companies, where users have sessions every day, can run shorter experiments than companies where users have sessions only a couple of times a month. Or, maybe you’re interested in purchasing behaviors. Then your experiment would most likely need to run for longer than an experiment where you’re examining sessions since it’s likely your users make purchases less frequently.

#### Try to Limit Ending Experiments Prematurely

- You should decide how long to run your experiment before beginning it, and then you should only end your experiment and gather final results once you’ve reached this pre-determined point; ending your experiment early, or whenever you see promising data, will introduce bias.

#### Think About Valuable Metrics

- Consider any baseline behaviors for the metrics you’re most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you’d like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. Once you decide how long your experiment should run, be sure to not end your experiment or record final results early, or your findings may be biased.

[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}
