---
nav_title: Advancement Behavior
permalink: "/advancement_behavior/"
---

# Advancement Behavior

## Canvas Default Behavior

By default, we only advance users through a Canvas step once they've received a message from that step. For example, if a Canvas step includes an email and a push, users will not advance to the next steps of the Canvas until:

- we send the user the email, or
- we send the user the push.

If the user doesn't receive the email or the push, they will not advance to subsequent steps in the Canvas.

## Canvas Advancement Behavior

The default behavior works well when subsequent messaging relates to the previous messages. For example, you wouldn't want to send a follow up push about an email that users never received.

There may be times when you want users to continue to advance through a Canvas even when they do not receive a certain message. For example, you might have a "Welcome" push on __Day 3__ and a "Welcome" email on __Day 6__. Some of your users may not be reachable via push notifications (as not everyone opts into push). You want all users to receive the __Day 6__ email, even if they didn't get the __Day 3__ push.

In this scenario, you can use Braze's Advancement Behavior options to ensure that customers continue down the Canvas, even if they do not receive the __Day 3__ push.

## Using Advancement Behavior

Braze's Advancement Behavior feature allows you to choose the criteria for advancement through your Canvas step.

![auto2.png][1]


When __Only Advance If Message Received__ is selected, customers will only be advanced to subsequent Canvas steps when one of the following conditions occur:

- An email message is sent to the customer.
- A push message is sent to the customer.
- A webhook is sent to the customer.
- An in-app message is viewed by the customer.

When __Advance Entire Audience After Delay__ is selected, customers who meet the filter criteria for the step and do not perform exception events will be advanced through the Canvas regardless of whether they receive a message. Advancement will take place at the time that Braze attempts to send the message. In other words, users will be advanced when Braze attempts to send a message to the customer.

Looping back to the use case at hand - if you want all users to receive the __Day 6__ email, even if they didn't get the __Day 3__ push you can select "Advance Entire Audience After Delay" advancement behavior for the __Day 3__ push.

When you select __Advance Entire Audience After Delay__ advancement behavior for the __Day 3__ push, users will advance when Braze attempts to send the push. Users match the audience options and who are not reachable via push will not actually be sent the push, but will be advanced anyway.

{% alert important %}
  Users must meet the step's criteria in order to be advanced through the step. For a scheduled step, users must meet the audience options for the step in order to be advanced through the step. If the step has an exception event, users who perform the exception event will not be advanced through the step.
{% endalert %}

For action-based steps, users must perform the trigger action and meet the audience options in order to be advanced through the step. If the step has an exception event, users who perform the exception event will not be advanced through the step.

{% alert important %}
  Customers who advance through a step without receiving messages will not be counted as a unique recipient for the step. Users must receive one or more messages from a step to be counted as a unique recipient.
{% endalert %}

When sending a multichannel step with intelligent delivery, we may send or attempt to send messages at different times for different channels. Braze will Auto-Advance users at the time that the first message in a step attempts to send.   

[1]: {% image_buster /assets/img/auto2.png %} "Advancement Behavior"
