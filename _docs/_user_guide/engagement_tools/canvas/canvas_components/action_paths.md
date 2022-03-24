---
nav_title: Action Paths Step
article_title: Action Paths Step
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "This reference article covers Action Paths and how to use them in your Canvases."
tool: Canvas
---

# Action Paths Step

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Action Paths in Canvas allow you to sort your users based on their actions. Using Action Paths, you can do the following: 
 
* Customize user paths based on a specific action, including user engagement events and custom events
* Hold users for a given duration to prioritize their next path based on their actions during this evaluation period

## Create Action Paths

To create Action Paths, add a step to your Canvas. Then, using the dropdown menu at the top of the new step, select **Action Paths**.

### Action settings

In the **Action Settings** module, you can choose how long you’d like to hold users in the action step by setting the **Evaluation Window**. By default, users are evaluated within one day, but you can adjust this window by seconds, minutes, hours, days, and weeks depending on your Canvas.

Within the **Action Settings**, you can also turn on the ranked order for your steps by switching the **Advance users based on ranked order** toggle to on.

![][4]

By default, **Ranking** is off. When a user enters the action path and performs the trigger event attached to any action group, they will immediately advance through the relevant action group. If a user doesn't perform a trigger event, then they will advance through the default **Everyone Else** group at the end of the evaluation period.

When **Advanced users based on ranked order** is enabled, this means that **Ranking** is on. So, all users will be held until the end of the evaluation window. At the end of the evaluation period, users will advance through the highest priority action group that they are eligible for at the end of the evaluation window. Users who do not perform any of the actions during the evaluation window will advance through the default **Everyone Else** group.

#### Ranking status example

Let's say you have an action path with an evaluation period of one day with two action groups: Group 1 and Group 2. Group 1 has a trigger event "Start Session", and Group 2 has "Make Purchase". If **Ranking** is turned on, then all users in the action path are "held" for one day. At the end of the day, if a user has started a session and made a purchase, then they advance to the highest rank path. In this case, the user would advance to Group 1. 

In the precedeing example, if **Ranking** is off and when a user performs one of the trigger events ("Start Session" or "Make Purchase"), that user is advanced in the relevant action group based on the trigger action.

### Action groups

Add a trigger or multiple triggers to define your action groups. Here, you can select a range of trigger events such as [custom events][2], engagement events like interactions with your app, and more.

![][3]

Within each action group settings, you also have the option to select the checkbox **I want this group to exit the Canvas**, meaning that the users within this group will exit the Canvas at the end of the evaluation period.

### Canvases with re-eligibility

If users enter into an action path multiple times and have multiple entries in the action path at the same time, the expected behavior varies depending on the **Ranking**status. 

| Ranking Status | Action Path Behavior |
|---|--------------|
| **Off** | When a relevant action is performed, Braze will deduplicate entries and immediately advance the earliest entry through the relevant action group. <br><br/> When a relevant action is not performed, all entries will advance at the end of the relevant evaluation window. No deduplication will occur. |
| **On** | All entries will advance at the end of the relevant evaluation window. No deduplication will occur. |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img/canvas_actionpath.png %} 
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events
[3]: {% image_buster /assets/img/actionpath_group.png %} 
[4]: {% image_buster /assets/img/actionpath_settings.png %} 
