---
nav_title: Global Control Group
alias: /global_control_group/
description: "This article covers how to set up and properly use Global Control Groups. It also covers how to view reports and metrics brought on by the use of these groups."
hidden: true
page_type: reference
---

# Global Control Groups

> Global control groups allow you to analyze the overall impact of your messaging efforts over a period of time. By allowing you to compare user behavior, global control groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events.

## Create a Global Control Group

1. __Navigate to the global control group tab__<br>From the dashboard, navigate to the Global Control Group tab located within Global Message Settings under Engagement.
2. __Assign a percentage of all users to this control group__<br> See our [best practices section](#percentage-guidelines) for percentage guidelines. Once saved, Braze will generate a randomly selected group of users comprising that percentage of your total user base.
3. __Save your control group__<br>Your saved control group will go into effect right away. As soon as you save your control group, all currently active as well as future campaigns/Canvases will no longer send to users in this group.
4. __Export a CSV of users (Optional)__<br>From this page, you can export a CSV of users in your global control group. <br><br>![Global Control Group][1]

## How to Global Control Group Works

Your global control group will be applied to __all channels, campaigns as well as Canvases__, with the exception of News Feed Cards. Users in your control group will not be excluded from News Feed Cards. If you are using Content Cards, users in your control group will also be excluded from Content Cards.

__To assign users randomly to the global control group:__<br> Braze will randomly select multiple ranges of Random Bucket Numbers, and include users from those selected buckets. <br><br>
__To track data for reporting:__<br>Braze will measure the behaviors of those in your control group and those in your treatment sample. Once a control group is saved, Braze generates a non-overlapping treatment sample of users using the same method.

## Disabling your Global Control Group
You can disable your global control group at any time, but keep in mind that doing so will result in users in this group immediately becoming eligible for campaigns/ Canvases.

1. __Before Disabling your Control Group__, we recommend exporting a CSV of users in that group in case you need to reference it at a later point. Once you disable a control group, there will be no way for Braze to restore that group or identify which users were in this group.
2. __After Disabling your Control Group__ you can save a new one. Once you enter a percentage and save it, Braze will generate a new randomly selected group of users. <br><br>![Global Control Group][2]

## Viewing Reporting

1. __Navigate to the reporting page.__ To view a report for your global holdout groups, navigate to Control Group Report under Reports.
2. __Select your report parameters.__ Select either sessions or a particular custom event, and click Run Report.

### Understanding Your Report 

The global control group allows you to compare it against a treatment sample of approximately the same number of users as your control group, and is randomly selected from the pool of non-control users.

This report takes the percentage of users in your control and treatment groups that have completed your selected event each day and averages this percentage out over the last 30 days. 

It calculates during this time period, on average, what percentage of control group and treatment group users would complete this event. This "Change from Control" indicates the percentage change between the two groups.<br><br>![Global Control Group][3]

## Best Practices

### Optimal Control Group Size {#percentage-guidelines}

<br>__Two main rules to keep in mind are__:<br>- Your control group should be no smaller than 1000 users.<br>- Your control group should be no more than 10% of your entire audience.

If you have a total audience that’s smaller than 10,000, you should increase your percentage in order to create a group of over 1000 users; in this case, it’s best to not increase your percentage above 15%.
- Some trade-offs to consider when thinking about your control group size are that you need a significantly large number of customers in your control group so that any analysis you do on their behaviors is trustworthy. However, the larger your control group is, the fewer customers are getting your campaigns, which is a downside if you’re using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience will depend on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you will need a larger percentage for your control group.

### Experiment Duration 

#### Choose an Ideal Duration {#reshuffle}

- How long to run your experiment before reshuffling control group membership depends on what you’re testing and what your users’ baseline behaviors are. If you aren’t sure, a good place to start is one quarter (3 months), and you should not go shorter than 1 month.
- To determine the appropriate length of time for your experiment, consider what questions you’re hoping to answer. For instance, are you looking to see if there’s a difference in sessions? If so, think about how often your users have sessions organically - companies, where users have sessions every day, can run shorter experiments than companies where users have sessions only a couple of times a month. Or, maybe you’re interested in purchasing behaviors. Then your experiment would probably need to run for longer than an experiment where you’re examining sessions since it’s likely your users make purchases less frequently.

#### Try to Limit Ending Experiments Prematurely

- You should decide how long to run your experiment before beginning it, and then you should only end your experiment and gather final results once you’ve reached this pre-determined point; ending your experiment early, or whenever you see promising data, will introduce bias.

#### Think About Valuable Metrics

- Consider any baseline behaviors for the metrics you’re most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you’d like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. Once you decide how long your experiment should run, be sure to not end your experiment or record final results early, or your findings may be biased.

[1]: {% image_buster /assets/img/control_group/control_group1.png %}
[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[3]: {% image_buster /assets/img/control_group/control_group3.png %}