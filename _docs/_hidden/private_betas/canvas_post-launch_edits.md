---
nav_title: Post-Launch Edits
permalink: "/post-launch_edits/"
hidden: true
---

# Post-launch edits

In the Canvas V2 workflow, you can now edit your Canvases after they have been launched. This includes the following:

- Deleting Canvas Components 
- Deleting variants that only contain non-full steps
- Deleting the connections where the origin or destination is a non-full step  

When a non-full step with a time delay (specifically, a Delay Step (where users can remain in the step for a delay period), or an Action Paths (where users can remain in the step until the evaluation window ends)) is deleted, you can choose to redirect those users into other Canvas V2 steps.

Note that you still won't be able to delete the following:

- Canvas full steps
- Canvas variants that contain at least one full step
- Connections between Canvas full steps

## Making edits post-launch

There are a number of things to know if you plan to edit or add more steps to any other step in Canvas after launching:

If you want to edit or add more steps to your Canvas, 

- Users who have not yet entered the Canvas will be eligible for newly created steps.
- Users who have already passed newly created steps will be eligible next time they re-enter if you have allowed users to re-enter the Canvas in Canvas Entry Settings.
Users who are currently in a Canvas, but have not reached the points where new steps are added will be eligible to receive those new steps.
- You cannot edit or delete existing connections between two Canvas full steps nor can you insert a step between existing connected Canvas full steps once a Canvas is launched.
- If you update the Delay or Window for a step, only new users entering the Canvas and users that haven’t been queued for that step yet will receive the message at the updated delay.
- If you delete a step with a time delay (i.e Delay or Action Paths) and choose to redirect users in those steps into another Canvas step, the users will only be redirected after the step's time delay has completed. For example, if you delete a Delay step with delay = 1 day and redirect those users to a Message step, then the users will only be redirected after the step's 1 day delay has completed
If your Canvas contains one or more Experiment Step(s), deleting steps could invalidate the results of the Experiment step

{% alert note %}
Stopping a Canvas won’t flush users who are waiting to receive messages. If you re-enable the Canvas and users are still waiting for the message, they will receive it. However, if the time that they should’ve been sent the message has passed, they won’t receive it).
{% endalert %}
