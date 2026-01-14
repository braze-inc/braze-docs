---
nav_title: Best practices
article_title: Canvas Best Practices
page_order: 1
description: "This article provides some best practices for creating and customizing user journeys with Canvas and Canvas Flow."
tool: Canvas

---

# Canvas best practices

> This article provides some best practices for creating and customizing user journeys with Canvas and Canvas Flow.

## Identify your purpose

Dive into the what, who, and why!
- What are you trying to help the users accomplish?
- Who are the users you're trying to reach?
- Why are you building this Canvas?

## Mix and match

Unlock new combinations of user journeys with [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/).
- Split your users with [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) and build different workflows.
- Space out your user journeys with a [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) step.
- Add [standalone messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) anywhere you want in your Canvas flow. 

## Create richer messages

Reel in your users with richer messages.

- Build [in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) for onboarding Canvases to make the most out of your first impression.
- Introduce [Content Cards]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) in a Canvas journey for promotional offers and push notifications.

## Test your user journeys

Determine the impact of your Canvas messaging by incorporating control groups. This way, you can build an understanding of how your Canvas was received!

- Name each step of your Canvas to identify your user journey.
- Leverage the [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) component in your user journey to randomly assign users to different paths you create. 
- Diversify your user journeys with Delay and Message steps to help uncover what path is most effective.
- Check [Canvas analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) to see the performance of each component in your user journey.
- [Edit your Canvas]({{site.baseurl}}/post-launch_edits/) after the initial launch.

## Scheduling your Canvases

{% alert note %}
Canvas will prevent you from using scheduled send with a time that has already passed. However, it's possible to launch a Canvas during the exact same minute that the campaign is scheduled (or in the seconds before). This can lead to the Canvas missing the scheduled entry time and users not entering the Canvas. We recommend sending Canvases immediately in the event that any campaigns are edited within minutes of the scheduled send time.
{% endalert %}

For Canvas steps, consider the following details when scheduling your Canvas:

- Schedule changes will only apply to users who aren't already waiting to receive the step.
- Audience changes by default apply to all users, unless you schedule changes to apply to users who aren't waiting to receive the step.
- Editing a Canvas that is scheduled to deliver as soon as deployed and selecting **Update** will essentially cause it to be sent.
