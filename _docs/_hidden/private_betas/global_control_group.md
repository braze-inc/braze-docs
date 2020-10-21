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

1. __Navigate to the global control group tab__<br>From the dashboard, navigate to the "Global Control Group" tab located within "Global Message Settings" under "Engagement". <br><br>
2. __Assign a percentage of all users to this control group__<br> See our [best practices section](#percentage-guidelines) for percentage guidelines. Once saved, Braze will generate a randomly selected group of users comprising that percentage of your total user base.<br><br>
3. __Choose your exclusion settings__<br> You can either exclude your control group for only new campaigns/Canvases by default or exclude this group from both new campaigns/Canvases AND existing campaigns/Canvases. If you choose the latter option, upon saving your control group, all active campaigns will exclude the users in your control group in their sends. <br>Note that on an individual campaign or Canvas level, you will always have the option to override control group settings and still send that message to control group users (this may be helpful for transactional messages).<br><br>
4. __Save your control group__<br><br>
5. __View your groups__<br>Once saved, select the "Calculate Exact Group Size" button to calculate the exact sizes for your control, treatment, and treatment sample groups. <br><br>__Available Group Types:__<br>- Control: Number of users that will be in the control group.<br>- Treatment: The number of users that will not be in the global control group.<br>- Treatment Sample: The number of users in the treatment group used for comparison against the global control group. This sample will consist of the same percentage of all users as the global control group.<br><br>
6. __Export a User CSV (Optional)__<br> From this same page, you can export a CSV of users in your global control group.

## Sending Campaigns and Canvases using your Control Group

Once saved, your campaign and Canvas wizard will __now include a checkbox__ that, if unchecked (default), will __exclude__ sending to your control group. For campaigns, this can be found under Target Users. For Canvases, this can be found in the Target Users section of the Entry Step.<br><br>If you wish to override this and send a particular campaign/Canvas to your control group, uncheck this box.

## Editing your Global Control Group

You can edit your global control group at any time, but keep in mind that doing so will randomly reshuffle membership and you will not be able to revert to prior membership. We recommend that you export your group before reshuffling so that you can maintain a record of who was in this group historically.

1. __Navigate to the Global Control Group page__ to edit your global control group. Here, you can view when your group was created and when it was last edited. Read our [best practices](#reshuffle) for guidelines on how frequently to reshuffle group membership.
2. __Click "Edit" and then "Proceed"__ after reading the warning.
3. __Enter a new percentage__, then click Save. If you enter the same percentage, Braze will randomly choose a new group of users comprising the same percentage.

## Viewing Reporting

The Global Control Group Report allows you to compare your global control against a treatment sample. The treatment sample is comprised of approximately the same number of users as your control group and is randomly selected from the pool of non-control users.

1. __Navigate to the reporting page__<br>To view a report for your global holdout groups, navigate to Control Group Report under Reports.
2. __Select an event and time frame__<br>In the "Select an Event" box, select either sessions or a particular custom event you'd like to compare. Then, select a data time frame you'd like to view and run the report.
3. __Report Metrics__<br>This report shows the percentage of control versus treatment group users that had a session or completed an event during the time frame you selected. The chart shows the percentage change between your control and treatment sample. Here you may export, share, or save this report. 

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