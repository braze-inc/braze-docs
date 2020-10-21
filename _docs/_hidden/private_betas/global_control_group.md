---
nav_title: Global Control Group
alias: /global_control_group/
hidden: true
---

# Global Control Groups

> Global control groups allow you to analyze the overall impact of your messaging efforts over a period of time. By allowing you to compare user behavior, global control groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events.

Different Types of Control Groups
- Control: Number of users that will be in the control group.
- Treatment: The number of users that will not be in the Global Control Group.
- Treatment Sample: The number of users in the tratment group used for comparison against the Global Control Group. This sample will consist of the asme percentage of all users as the Global Control Group.



## Create a Global Control Group
1. From the dashboard, navigate to the "Global Control Group" tab located within "Global Message Settings" under "Engagement". 
2. Assign a percentage of all users to this control group. See our best practices section for percentage guidelines. Once saved, Braze will generate a randomly selected group of users comprising that percentage of your total user base.
3. Choose your exclusion settings. You can either exclude your control group for only new campaigns/Canvases by default or exclude this group from both new campaigns/Canvases AND existing campaigns/Canvases. If you choose the latter option, upon saving your control group, all active campaigns will exclude the users in your control group in their sends. Note that on an individual campaign or Canvas level, you will always have the option to override control group settings and still send that message to control group users (this may be helpful for transactional messages).
4. Save your control group.
5. To see the exact sizes for your control, treatment, and treatment sample groups, you’ll need to first save your group and then select the button "Calculate Exact Group Size" button. 
6. From this page, you can export a CSV of users in your global control group.

## Sending Campaigns and Canvases using your Control Group

1. Once you've saved a global control group, your campaign and Canvas wizard will now include a checkbox that, if unchecked (default), will exclude sending to your control group. For campaigns, this can be found under Target Users. For canvases, this can be found in the Target Users section of the Entry Step.
2. If you wish to override this and send a particular campaign/Canvas to your control group, uncheck this box.

## Editing your Global Control Group
You can edit your global control group at any time, but keep in mind that doing so will randomly reshuffle membership and you will not be able to revert back to prior membership. We recommend that you export your group before reshuffling so that you can maintain a record of who was in this group historically.

1. To edit your control group, go to the Global Control Group page. Here, you can view when your group was created and when it was last edited. Read our best practices for guidelines on how frequently to reshuffle group membership.
2. Click "Edit" and then "Proceed" after reading the warning.
3. You may now enter a percentage, then click Save. If you enter the same percentage, Braze will randomly choose a new group of users comprising the same percentage.

## Viewing Reporting
1. To view a report for your global holdout groups, navigate to Control Group Report under Reports. 
2. This report allows you to compare your global control against a treatment sample. The treatment sample is comprised of approximately the same number of users as your control group and is randomly selected from the pool of non-control users.
3. In the "Select an Event" box, select either a sessions or a particular custom event you'd like to compare. Then, select a data time frame you'd like to view, and run the report.
4. This report will show you the percentage of control versus treatment group users that had a session or completed an event during the time frame you selected. A chart will show you the percentage change between your control and treatment sample.

## Best practices for setting up your global control group

### Control group size
The two main rules to keep in mind are:
- Your control group should be no smaller than 1000 users.
- Your control group should be no more than 10% of your entire audience.

If you have a total audience that’s smaller than 10,000, you’ll need to increase your percentage in order to create a group of over 1000 users; in this case, it’s best to not increase your percentage above 15%.
- There are some trade-offs to consider when thinking about your control group size - first, you need a significantly large number of customers in your control group so that any analysis you do on their behaviors is trustworthy, and not based on just a handful of users. However, the larger your control group is, the fewer customers are getting your campaigns, which is a downside if you’re using your campaigns to drive engagement and conversions.
- The ideal percentage of your total audience will depend on how large your total audience is. The bigger your total audience is, the smaller your percentage can be. If you have a small audience, however, you will need a larger percentage for your control group.

### Experiment duration 
- How long to run your experiment before reshuffling control group membership depends on what you’re testing and what your users’ baseline behaviors are. If you aren’t sure, a good place to start is one quarter (3 months), and you should not go shorter than 1 month.
- You should decide how long to run your experiment before beginning it, and then you should only end your experiment and gather final results once you’ve reached this pre-determined point; ending your experiment early, or whenever you see promising data, will introduce bias.
- To determine the appropriate length of time for your experiment, consider what questions you’re hoping to answer. For instance, are you looking to see if there’s a difference in sessions? If so, think about how often your users have sessions organically - companies, where users have sessions every day, can run shorter experiments than companies where users have sessions only a couple of times a month. Or, maybe you’re interested in purchasing behaviors. Then your experiment would probably need to run for longer than an experiment where you’re examining sessions since it’s likely your users make purchases less frequently.
- Consider any baseline behaviors for the metrics you’re most interested in. Are you interested in purchase rates for subscription plans that are renewed only on an annual basis? Or do customers have a weekly habit for the event you’d like to measure? Think about how long it takes users to potentially alter their behaviors due to your messaging. Once you decide how long your experiment should run, be sure to not end your experiment or record final results early, or your findings may be biased.