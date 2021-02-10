---
nav_title: Advancement Behaviors
platform: Canvas
page_order: 2
description: "Braze’s Advancement Behavior feature allows you to choose the criteria for advancement through your Canvas step. This reference article covers various use cases and scenarios that may come up as you advance through a Canvas."
alias: /auto_advance/
---

# Advancing Your Users through Canvas Steps

Braze’s Advancement Behavior feature allows you to choose the criteria for advancement through your Canvas step.

![auto2.png][1]

When __Message Sent__ is selected, customers will only be advanced to subsequent Canvas steps when one of the following conditions occur:

- An email message is sent
- A push message is sent
- A webhook is sent
- An in-app message is viewed
- A Content Card is sent

When __Immediately Advance Audience__ is selected, customers will be advanced to subsequent Canvas steps when one of the following conditions occur:

- Any message is sent or the in-app message in the step becomes live
- The webhook is not sent because the webhook causes an error or errors
- A push or email is not sent because the user is not reachable by push or email
- Content Card sending is attempted 
- A Card is aborted and not sent
- A message is not sent because it is frequency capped
- A message is not sent because it is aborted

{% alert important %}
  Users must meet the step's criteria in order to be advanced through the step. For a scheduled step, users must meet the audience options for the step in order to be advanced through the step. If the step has an [exception event]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/), users who perform the exception event will not be advanced through the step.
{% endalert %}

For action-based steps, users must perform the trigger action and meet the audience options in order to be advanced through the step. If the step has an exception event, users who perform the exception event will not be advanced through the step.

{% alert important %}
  Customers who advance through a step without receiving messages will not be counted as a unique recipient for the step. Users must receive one or more messages from a step to be counted as a unique recipient.
{% endalert %}

When sending a multi-channel step with intelligent timing, we may send or attempt to send messages at different times for different channels. Braze will Auto-Advance users at the time that the first message in a step attempts to send.   

## Using Canvas Advancement

Advancement works well when subsequent messaging relates to the previous messages. For example, you wouldn't want to send a follow-up push about an email that was __never sent__ to users.

There may be times when you want users to continue to advance through a Canvas even when they do not receive a certain message. For example, you might have a "Welcome" push on __Day 3__ and a "Welcome" email on __Day 6__. Some of your users may not be reachable via push notifications, as not everyone opts in to receive push messages. You may want to send the __Day 6__ email to all users, even if they weren't sent the __Day 3__ push.

In this scenario, you can use Braze's Advancement Behavior options to ensure that users continue down the Canvas, even if they are not sent the __Day 3__ push.

If you want all users to receive the __Day 6__ email, even if they didn't get the __Day 3__ push, you can select __Immediately Advance Audience__ advancement behavior for the __Day 3__ push.

When you select __Immediately Advance Audience__ advancement behavior for the __Day 3__ push, users will advance when Braze attempts to send the push. Users who match the audience options and who are not reachable via push will not be sent the push but will be advanced anyway.

{% details Previous Canvas Advancement Behavior %}

Prior to the release of Advancement Behavior, Braze advanced users through a Canvas step once they'd been sent a message from that step. For example, if a Canvas step included an email and a push, users would not advance to the next steps of the Canvas until:

- Braze sent the user the email, or
- Braze sent the user the push.

If the user wasn't sent the email or the push, they would not advance to subsequent steps in the Canvas.

Braze customers who did not participate in the first round of the Canvas in-app message beta will have the "Message Sent" Advancement Behavior option applied to all Canvas steps created prior to July 30th, 2019. Prior to the Advancement Behavior release, user advancement occurred when messages were sent from Canvas steps.

Braze customers who did participate in the first round of the Canvas in-app message beta will have the "Message Sent" Advancement Behavior option applied to all Canvas steps without in-app messages created prior to July 30th, 2019 and "Advance Audience After Delay" applied to all Canvas steps with in-app messages created prior to July 30th, 2019. Prior to the release of Advancement Behavior, user advancement occurred when Canvas in-app messages became live.

{% enddetails %}

[1]: {% image_buster /assets/img/push-advancement-behavior.png %} "Advancement Behavior"
