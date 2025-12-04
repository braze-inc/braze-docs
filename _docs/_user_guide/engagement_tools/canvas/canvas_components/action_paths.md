---
nav_title: Action paths
article_title: Action Paths 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "This reference article covers how to use Action Paths, a component that allows you to sort users based on their actions."
tool: Canvas
---

# Action Paths 

> Action Paths in Canvas allow you to sort your users based on their actions. 

![An Action Paths step  in a Canvas user journey.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Using Action Paths, you can:

* Customize user paths based on a specific action, including user engagement events and custom events
* Hold users for a given duration to prioritize their next path based on their actions during this evaluation period

## Creating an action path

To create an action path, add a component to your Canvas. Drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Action Paths**.

### Action settings

In the **Action Settings**, set the **Evaluation Window** to determine how long users are held in the step. By default, users are evaluated within one day, but you can adjust this window by seconds, minutes, hours, days, and weeks depending on your Canvas. The maximum evaluation window for an action path is 31 days.

Within the **Action Settings**, you can also turn on the ranked order for your components by switching on the **Advance users based on ranked order** toggle.

![The Action Settings with an evaluation window of 1 day.]({% image_buster /assets/img/actionpath_settings.png %})

By default, **Ranking** is off. When a user enters the action path and performs the trigger event attached to any action group, they will immediately advance through the relevant action group. If a user doesn't perform a trigger event, then they will advance through the default **Everyone Else** group at the end of the evaluation period.

When **Advanced users based on ranked order** is turned on, this means **Ranking** is on. So, all users will be held until the end of the evaluation window. At the end of the evaluation period, users will advance through the highest priority action group that they are eligible for at the end of the evaluation window. Users who do not perform any of the actions during the evaluation window will advance through the default **Everyone Else** group.

Note that you can trigger an action path when a nested custom attribute object changes, but not for changes to object array data types.

#### In-app messages

Note that when the action group trigger is starting a session and the next step is an in-app message, the user will need to perform two session starts to receive the in-app message. The first session assigns the user to the action group within the action path, and the second session triggers the in-app message.

#### Ranking status example

Let's say you have an action path with an evaluation period of one day with two action groups: Group 1 and Group 2. Group 1 has a trigger event "Start Session", and Group 2 has "Make Purchase". If **Ranking** is turned on, then all users in the action path are "held" for one day. At the end of the day, if a user has started a session and made a purchase, then they advance to the highest rank path. In this case, the user would advance to Group 1. 

In the preceding example, if **Ranking** is off and a user performs one of the trigger events ("Start Session" or "Make Purchase"), that user is advanced in the relevant action group based on the trigger action.

Note that Canvas entry properties differ from event properties. Canvas entry properties are properties from the event that triggered the Canvas. These properties can only be used in the first full step of a Canvas when using the original Canvas workflow. When using Canvas, persistent entry properties are enabled and allow the entry properties to be reused throughout the Canvas. Conversely, event properties originate from an event or action that occurs as the user goes through their workflow.

### Action groups

Add a trigger or multiple triggers to define your action groups. Here, you can select a range of triggers, such as if users:

- Make a purchase
- Start a session
- Perform a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Perform a conversion event
- Add an email address
- Change a custom attribute value (including arrays, but not nested custom attributes). This includes adding a new attribute with a value to a user profile for the first time (when the attribute was not previously present).
- Update their subscription status or subscription group status
- Interact with a campaign or Content Card
- Enter a location
- Trigger a geofence
- Send an SMS or WhatsApp inbound message

![An action group named "Group 1" for users who make any purchase.]({% image_buster /assets/img/actionpath_group.png %})

In each action group setting, you also have the option to select the checkbox **I want this group to exit the Canvas**, meaning that the users within this group will exit the Canvas at the end of the evaluation period.

### Canvases with re-eligibility

If users enter an action path multiple times and have multiple entries in the action path at the same time, the expected behavior varies depending on the **Ranking** status.

| Ranking Status | Action Path Behavior |
|---|--------------|
| **Off** | When a relevant action is performed, Braze will deduplicate entries and immediately advance the earliest entry through the relevant action group. <br><br/> When a relevant action is not performed, all entries will advance at the end of the relevant evaluation window. No deduplication will occur. |
| **On** | All entries will advance at the end of the relevant evaluation window. No deduplication will occur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Note that the rankings aren't [editable after launch]({{site.baseurl}}/post-launch_edits/).
