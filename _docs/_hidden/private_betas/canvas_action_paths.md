---
nav_title: Action Paths in Canvas
permalink: /user_guide/engagement_tools/canvas/canvas_components/action_paths
hidden: true
platform: Canvas

page_type: reference
description: "This reference article covers action paths and how to use them in your Canvases."
tool: Canvas
---
<br>
{% alert note %}
Canvas Action Paths are currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

# Action Paths in Canvas

Action Paths in Canvas allow you to sort your users based on their actions. Using Action Paths, you can: 
 
* Customize user paths based on a specific action
* Hold users for a given duration to prioritize their next path based on their actions during this evaluation period

## Create Action Paths

![canvas_actionpath][1]{: style="float:right;max-width:50%;margin-left:15px;"}

To create Action Paths, add a step to your Canvas. Then, using the drop-down at the top of the new step, select `Action Paths`.

## Define Action Settings 

In the **Action Settings** module, you can choose how long you’d like to hold users in the action step. 

When the **Ranking** is off, users who perform actions after they enter the action path and before the end of the evaluation window will immediately advance through the relevant action group as soon as they perform the action. Users who do not perform a relevant action during the evaluation period will advance through the default **Everyone Else** group at the end of the evaluation period. 

When the **Ranking** is on, all users will be held until the end of the evaluation period. At the end of the evaluation period, users will advance through the highest priority action group that they are eligible for. Users who do not perform any action during the evaluation period will advance through the default **Everyone Else** group. 

## Define Action Groups

Add a trigger or multiple triggers to define your action groups. 

When **Ranking** is off, users who perform one or more of the triggers will immediately advance through the relevant action group. 

When **Ranking** is on, you can prioritize action groups. The user will continue down the highest priority group that they are eligible for at the end of the evaluation period. 

## Canvases With Re-eligibility 

If users enter into an action path multiple times and have multiple entries in the action path at the same time, the expected behavior varies depending on **Ranking**: 

| Ranking Filter | Action Path Behavior |
|---|--------------|
| **Off** | * When a relevant action is performed, Braze will deduplicate entries and immediately advance the earliest entry through the relevant action group <br /> * When a relevant action is not performed, all entries will advance at the end of the relevant evaluation window. No deduplication will occur. |
| **On** | All entries will advance at the end of the relevant evaluation window. No deduplication will occur. |

{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img/canvas_actionpath.png %} 
