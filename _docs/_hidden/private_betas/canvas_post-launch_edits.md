---
nav_title: Post-Launch Edits
permalink: "/post-launch_edits/"
hidden: true
---

# Post-launch edits

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

In the Canvas V2 workflow, you can now edit your Canvases after they have launched. This includes deleting the following:

- [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components)
- Canvas variants 
- Connections between Canvas steps  

You can edit the connections between Canvas components by clicking the connection between Canvas components and moving it elsewhere. Need to delete a step? Click on the step's gear icon and select **Delete**.

If you delete a [Delay Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) or [Action Paths Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), you can optionally redirect the users currently waiting in the step into another Canvas V2 step. For Delay Steps, users will remain in the step until the end of the delay period. For Action Paths Steps, users will remain in the step until the end of the evaluation window.

{% alert important %}
You can only perform post-launch edits on the Canvas V2 workflow. If your Canvas uses the Canvas V1 workflow, you will need to migrate the Canvas to Canvas V2 first.
{% endalert %}

## Editing your Canvas

There are several things to keep in mind when editing or adding to your Canvas after it’s been launched. If you want to edit or add more steps to your Canvas, the following details will apply:
- After creating a new step, users who haven’t entered the Canvas yet will be eligible to enter this new step. 
- If your Canvas Entry Settings allow users to re-enter steps, users who have already passed newly created steps will be eligible to re-enter.
- Users currently in a Canvas are eligible to receive newly added Canvas steps.

Note the following details for editing Canvas steps with a time delay:
- If you update the delay in the Delay Step or evaluation window in the Action Paths Step, only new users entering the Canvas and users that haven’t been queued for that step will receive the message at the updated time delay.
- If you delete a step with a time delay (i.e., Delay Step or Action Paths Step) and decide to redirect those users into another Canvas step, the users will only be redirected after the step's time delay has completed. For example, let’s say you delete a Delay Step with a one day delay and redirect those users to a Message Step. In this case, the users will only be redirected after the one day delay has been completed.

If your Canvas contains one or more [Experiment Paths Steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/), deleting steps could invalidate the results of this step.

Stopping a Canvas will not exit users who are waiting in a step. If you re-enable the Canvas and the users are still waiting, they will complete the step and move onto the next step. However, if the time that the user should’ve progressed to the next step has passed, they will instead exit the Canvas. 

For example, let's say you have a Canvas created using the Canvas V2 workflow set to launch at 2pm with one variant with two steps: a Delay Step with a one hour delay that goes into a Message Step. A user enters this Canvas at 2:01pm and enters the Delay Step at the same time. This means the user will be scheduled to move on to the next step (the Message Step) at 3:01pm. If you stop the Canvas at 2:30pm and re-enable the Canvas at 3:30pm, the user will exit the Canvas since it’s after 3:01pm. However, if you re-enable the Canvas at 2:40pm, the user will move on to the Message Step as expected at 3:01pm.

[1]: {% image_buster /assets/img_archive/canvasv2_delete_step_post-launch.png %} 