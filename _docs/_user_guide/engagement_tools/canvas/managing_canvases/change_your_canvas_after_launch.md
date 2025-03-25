---
nav_title: Editing Canvases After Launch
article_title: Editing Canvases After Launch
page_order: 0
description: "This reference article covers the different aspects of a Canvas that can be changed after the initial launch."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Editing Canvases after launch

> This reference article covers what can be changed in a Canvas after the initial launch.

You can edit your Canvases after launch by:

* Inserting new Canvas steps into the user journey
* Adding new variants and connections
* Adjusting variant distribution
* Stopping or resuming all Canvas steps

{% alert note %}
Control variant distribution may only be decreased after launch.
{% endalert %}

Keep in mind the following permissible post-launch Canvas edits depending on which workflow your Canvas was created with. If your Canvas uses the original Canvas workflow, you'll need to clone to Canvas Flow first in order to perform post-launch edits.

You can delete any of the following in your user journey:

- [Canvas steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Canvas variants 
- Connections between Canvas steps

If you want to edit or add more steps to your Canvas user journey, the following details will apply:

- Users who haven't entered the Canvas yet are eligible for any newly created steps. 
- If your Canvas entry settings allow users to re-enter steps, users who have already passed newly created steps are eligible to re-enter.
- Users who are currently in a launched Canvas, but haven't reached the points of the user journey where new steps are added, are eligible to receive those newly added steps. 

If you delete a [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) or [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step, you can optionally redirect the users currently waiting in the step into another Canvas step. For Delays, users will remain in the step until the end of the delay period. For Action Paths, users will remain in the step until the end of the evaluation window.

Note that when you launch a Canvas initially, Braze enqueues the users for the Message step they're at, not all subsequent messages in the Canvas. If you make an edit to the Canvas after launch, some users will already be enqueued and will not pick up the changes. If you stop the Canvas, duplicate it, then change it and launch this new version, the Canvas will re-evaluate all users again, not just users that have not already been enqueued.

See the [Best practices](#best-practices) section for specific editing use cases. In general, it's best practice to avoid editing live Canvases as there may be unexpected behavior.

{% details Original Canvas editor %}

{% alert important %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It’s an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

You can't edit or delete existing connections, and can't insert a step between existing connected steps. If you want to edit or add more steps to your Canvas user journey, the following details will apply:

- Users who haven't entered the Canvas yet are eligible for any newly created steps. 
- If your Canvas entry settings allow users to re-enter steps, users who have already passed newly created steps are eligible to re-enter.
- Users who are currently in a launched Canvas, but haven't reached the newly added steps in the user journey, are eligible to receive those newly added steps.

If you update the **Delay** or **Window** settings for a Canvas step, only new users entering the Canvas and users that haven't been queued for that step yet will receive the message at the updated delay. If a Delay step is the last step in the Canvas, users who reach that step are automatically advanced out of the Canvas and won't receive any newly created steps. 

{% alert note %}
Stopping a Canvas will not exit users who are waiting to receive a message. If you re-enable the Canvas and users are still waiting for the message, they will receive it (unless the time they should've been sent the message has passed, then they won't receive it).
{% endalert %}

{% enddetails %}

## Canvas details

You can edit the following Canvas settings and information after a Canvas launches:

* Canvas name and description
* Teams and tags
* Entry type, schedule, and controls
* Subscription status
* Rate limiting
* Frequency capping
* Quiet Hours
* Target audience

After a Canvas has launched:

- Conversion events can't be edited. 
- The following steps can't be added or removed, and can't be reordered to adjust the ranking: [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), and [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Workaround 1:** Create a new Audience Path, Action Path, or Experiment Path and reconfigure the paths to that new step.
  - **Workaround 2:** Duplicate the Canvas to make your edits.

### Individual steps

For individual Canvas steps, you can edit the following details after launch:

* Name
* Message content
* Triggers
* Audience
* Exception events
* Delays

However, the step's schedule type and control percentages are not editable after launch. For Action Paths and Audience Paths steps, the rankings aren't editable after launch.

### Canvas variant percentages

After launching a Canvas, you can only decrease the control variant percentages. If a variant percentage is modified in Canvas, you'll find that your users may be redistributed to other variants.

Initially, these users are randomly assigned a particular variant before receiving a campaign for the first time. From then on, each successive time the campaign is received (or the user re-enters a Canvas variant), they will receive the same variant unless the variant percentages are modified.

If the variant percentages change, users may be redistributed to other variants. Users will stay in these variants until percentages are modified again. Note that for Canvases using branching with `NOT` filters with random bucket numbers, users may not receive the same branch each time in their user journey when they re-enter the Canvas.

#### Control groups

Control groups remain consistent if the variant percentage is unchanged. If a control group's percentage is decreased or increased, users who previously received messages wouldn't be able to enter the control group on a later send, nor would any user in the control group ever receive a message.

### Local send time

Canvases scheduled to launch at a local send time can be edited up to 24 hours prior to the scheduled send time. This window is called the "safe zone". 

{% alert tip %}
If you intend to make larger edits that lead to creating a new Canvas copy entirely, remember to exclude users who received the first Canvas and re-adjust the Canvas schedule times to allow for time zone sending.
{% endalert %}

### Deleting variants

When variants are deleted from a Canvas, the following occurs:

- Steps within the variant (including those shared by other variants) will be deleted. 
- The step analytics and the top-level analytics for the Canvas, such as _Total Entries_, _Total Exits_, and _Conversion Rate_, will be deleted.
- Users in deleted variants are exited from the steps, and any following messages are not sent.

### Canvas entry properties

Canvas entry properties aren't templated into steps when sent. This means when Canvas entry properties are edited after a Canvas has launched, these changes will only apply to new users who enter the Canvas. If your Canvas allows users to re-enter the Canvas, any users who re-enter will be determined by the updated Canvas entry properties.

## Best practices

Check out these best practices to keep in mind when editing or adding to your Canvas after it's been launched.

### Disconnected steps

You can launch your Canvas with disconnected steps and also save these Canvases post-launch. Before disconnecting a step from your workflow, we recommend checking the analytics view of the steps for users pending.

Let's say a user is in a disconnected step of your Canvas workflow. This user will advance to the subsequent step if there is one. The step's settings will dictate how the user should advance. 

By creating or editing disconnected steps, you can make changes to these independent steps without having to directly connect them to the rest of your Canvas. This helps with testing your steps prior to going launching your Canvas again. 

### Experiment Path step

If your Canvas has an active or in progress Experiment Path step and you update the active Canvas (even if it's not to the Experiment Path step), the in-progress experiment will restart. To avoid your users from re-entering the experiment path, you can duplicate and create a new Canvas instead of updating the Canvas.

### Time delays

Editing Canvases with time delays can be a bit tricky! So, keep in mind the following details as you make edits to your Canvases.

If you update the delay in a Delay step or evaluation window in the Action Paths step, only new users entering the Canvas and users that haven't been queued for that step will receive the message at the updated time delay.

If you delete a step with a time delay (such as Delay or Action Paths) and decide to redirect those users into another Canvas step, the users will only be redirected after the step's time delay has completed. For example, let's say you delete a Delay step with a one day delay and redirect those users to a Message step. In this case, the users will only be redirected after the one day delay has been completed.

If your Canvas has one or more Experiment Paths steps, deleting steps could invalidate the results of this step.

### Stopping Canvases

Stopping a Canvas won't exit users who are waiting in a step. If you re-enable the Canvas and the users are still waiting, they will complete the step and move to the next step. However, if the time that the user should've progressed to the next step has passed, they will instead exit the Canvas. 

For example, let's say you have a Canvas created using the Canvas Flow workflow set to launch at 2 pm with one variant with two steps: a Delay step with a one hour delay that goes into a Message step. 

A user enters this Canvas at 2:01 pm and enters the Delay step at the same time. This means the user will be scheduled to move on to the next step of the user journey (the Message step) at 3:01 pm. If you stop the Canvas at 2:30 pm and re-enable the Canvas at 3:30 pm, the user will exit the Canvas since it's after 3:01 pm. However, if you re-enable the Canvas at 2:40 pm, the user will move on to the Message step as expected at 3:01 pm.