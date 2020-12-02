---
nav_title: Global Control Group
alias: /global_control_group/
description: "This article covers how to set up and properly use Global Control Groups. It also covers how to view reports and metrics brought on by the use of these groups."
hidden: true
page_type: reference
---

# Global Control Groups

> Global Control Groups allow you to analyze the overall impact of your messaging efforts over time. These Groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events, by comparing the behaviors of users that receive messaging to those that don't.

## Create a Global Control Group

1. __Navigate to the Global Control Group settings__<br>From the dashboard, navigate to the Global Control Group tab located within __Global Message Settings__ under __Engagement__. <br><br>
2. __Assign a percentage of all users to this control group__<br> Input a percentage for your Control Group and __Save__. Once entered, Braze will show you an estimate of how many users will fall into your Global Control, treatment, and treatment sample. Keep in mind that the more users you have in your app group, the more accurate this estimate will be. Visit our [best practices section](#percentage-guidelines) for percentage guidelines.<br>![Global Control Group][4] <br><br>
3. __Assign Exclusion Settings__<br>Add exclusion settings to your Global Control Group by using tags. Any campaigns that use the tags included here in the exclusion settings will __not use__ your Global Control Group. These campaigns will continue to send to every user in the target audience (including those in your Global Control Group). You may want to add exclusion settings if you have transactional messages that should send to every user.<br>![Global Control Group][5] <br><br>
4. __Save your Control Group__<br>At this point, Braze will generate a randomly selected group of users comprising the selected percentage of your total user base. Once saved, all currently active as well as future campaigns/Canvases __will no longer send to users in this group__, with the exception being campaigns/Canvases that contain any of the tags in your exclusion settings. <br><br>
5. __Export a CSV of users (Optional)__<br>If you’d like to save who is in your group, make sure to export a CSV of Control Group users before disabling the group, as you will no longer be able to export this information once your group is disabled.

## How the Global Control Group Works

Your Global Control Group will be applied to __all channels, campaigns as well as Canvases__, with the exception of News Feed Cards. Users in your Control Group _will not_ be excluded from News Feed Cards. If you are using Content Cards, users in your Control Group _will_ also be excluded from Content Cards.

__Assigning users randomly to the Global Control Group:__<br> Braze will randomly select multiple ranges of [Random Bucket Numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute), and include users from those selected buckets. <br><br>
__Data tracking for reporting:__<br>Braze will measure the behaviors of those in your Control Group and those in your treatment sample. Your treatment sample is a random selection of users not in your Control Group, generated using the same Random Bucket Number method mentioned above.

## Disabling your Global Control Group

You can disable your Global Control Group at any time, but keep in mind that doing so will result in users in this group immediately becoming eligible for campaigns/Canvases.

1. __Before Disabling your Control Group__ we recommend exporting a CSV of users in that group in case you need to reference it at a later point. Once you disable a Control Group, there will be no way for Braze to restore the group or identify which users were in this group.<br><br>
2. __After Disabling your Control Group__ you can save a new one. Once you enter a percentage and save it, Braze will generate a new randomly selected group of users. If you enter the same percentage as before, Braze will still generate a new group of users for your control and treatment groups.
 <br><br>![Global Control Group][2]

## Viewing Reporting

![Global Control Group][6]
1. __Navigate to the reporting page__ -  To view a report for your Global Control, from the dashboard, navigate to __Global Control Group__ under __Data__.
2. __Select your report parameters__ - Select either sessions or a particular custom event and click __Run Report__.

#### Understanding Your Report 

The Global Control Group Report allows you to compare your group against a treatment sample.
Your treatment sample is a random selection of con-control users, approximately the same number of users as your Control, generated using the Random Bucket Number method.

This report takes the percentage of users in your control and treatment groups that have completed your selected event each day and averages this percentage out over the last 30 days. This calculates during this time period, on average, what percentage of Global Control and treatment group users would complete this event. The __Change from Control__ field indicates the percentage change between the two groups.

## Potential Errors
As you set up your Global Control Groups and view reporting, here are errors you may run into:

##### Unable to save the percentage entered when designating a Global Control Group
This issue occurs if you enter a non-integer or an integer that is not between 1 and 15 (inclusive). 

##### "Braze is not able to update your Global Control Group" error on the Global Control settings page
This usually indicates that some component of this page has changed, likely due to actions taken by another user on your Braze account. In this case, refresh the page and retry.

##### Global Control Group report does not have any data
If you access the Global Control report without having saved a Global Control Group, you will not see any data in the report. Create and save a Global Control Group and retry.

## Best Practices

### Optimal Control Group Size {#percentage-guidelines}

<br>__Two main rules to keep in mind are__:<br>- Your Control Group should be no smaller than 1000 users.<br>- Your Control Group should be no more than 10% of your entire audience.

If you have a total audience that’s smaller than 10,000, you should increase your percentage in order to create a group of over 1000 users; in this case, you should not increase your percentage above 15%. Keep in mind that the smaller your overall app group size is, the more challenging it will be to run a statistically rigorous test.
- Some trade-offs to consider when thinking about your Control Group size are that you need a significantly large number of customers in your Control Group so that any behavior analysis created is trustworthy. However, the larger your Control Group is, the fewer customers are getting your campaigns, which is a downside if you’re using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience will depend on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you will need a larger percentage for your Control Group.

### Experiment Duration 

#### Choose an Ideal Duration {#reshuffle}

- How long to run your experiment before reshuffling Control Group membership depends on what you’re testing and what your users’ baseline behaviors are. If you aren’t sure, a good place to start is one quarter (3 months), and you should not go shorter than 1 month.
- To determine the appropriate length of time for your experiment, consider what questions you’re hoping to answer. For instance, are you looking to see if there’s a difference in sessions? If so, think about how often your users have sessions organically - companies, where users have sessions every day, can run shorter experiments than companies where users have sessions only a couple of times a month. Or, maybe you’re interested in purchasing behaviors. Then your experiment would most likely need to run for longer than an experiment where you’re examining sessions since it’s likely your users make purchases less frequently.

#### Try to Limit Ending Experiments Prematurely

- You should decide how long to run your experiment before beginning it, and then you should only end your experiment and gather final results once you’ve reached this pre-determined point; ending your experiment early, or whenever you see promising data, will introduce bias.

#### Think About Valuable Metrics

- Consider any baseline behaviors for the metrics you’re most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you’d like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. Once you decide how long your experiment should run, be sure to not end your experiment or record final results early, or your findings may be biased.

[1]: {% image_buster /assets/img/control_group/control_group1.png %}
[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[3]: {% image_buster /assets/img/control_group/control_group3.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}