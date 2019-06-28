---
nav_title: Canvas Delay Step
permalink: "/delay_step/"
---

# Canvas Delay Step

{% alert update %}
The Canvas Delay Step is currently in Beta. Please reach out to a Braze representative for more information.
{% endalert %}

Delay Steps in Canvas allow you to add a stand alone delay to a Canvas. In other words, you can add a delay to your Canvas without needing to add an associated message.

Canvas Delay Steps can make your Canvases cleaner. Where you've previously needed to create two full steps, you can create one delay step and a single, full step.

You can also use Canvas Delay Steps to delay a step until an exact date, rather than using `in 1 day` or `on the next` you can specify the exact date and time that users move to a full step.

## Create a Delay Step

To create a Delay Step, add a step to your Canvas. Then, use the drop down at the top of the new step to select `Delay Step`.

### Delay Options

{% alert important %}
The first step of a Canvas must be a `Full Step`.
{% endalert %}

{% tabs %}
  {% tab After... %}
The “after” option allows you to delay users for a set number of seconds, minutes, hours or weeks  - for example, you can delay users for 4 hours or for 1 day.
  {% endtab %}
  {% tab Until Exact Date... %}
  The “Until Exact Date” option allows you to hold users in a step until a specific date and time.

  Note: That if the selected date and time has already passed by the time users proceed to the delay step, users will exit the Canvas.

  Note: There can be a maximum of 31 days between the start of the Canvas and the dates chosen for  “Wait until Exact Date” steps.
  {% endtab %}
{% endtabs %}

## Using Delay Steps

Let’s say that it’s June 10th. On June 11th, you’d like users to enter the Canvas and receive a message about an upcoming promotion. Then, you want to hold users in the Canvas until June 17th at 3 pm local time. At 3 pm local time on June 17th, you want to send users a reminder message about the promotion.

You’d start by adding a full step that sends immediately after users enter the Canvas on June 11th. Then, you’d create a delay step that holds users in the step until 3 pm local time on June 17th. After that, you’d link the delay step to a full step that sends it’s message immediately.

## Delay Step Analytics

Delay steps have three statistics available in the analytics view.

Entered: Reflects the number of times the step has been entered. If your canvas has re-eligibility and a user enters a delay step twice, two entries will be recorded.
Proceeded to Next Step: Reflects the number of entries that proceeded to the next step in the Canvas.

Exited Canvas: Reflects the number of entries that exited the Canvas and did not proceed to the next step.

Time series for these analytics are available in the expanded step view.

## Things to Note

A delay step cannot have full step sibling steps. In other words, you cannot create a full step that branches into a delay step and a full step. This restriction exists because if there was a branch with a delay step and a full step, it wouldn’t be clear which branch users would go down.

A delay step can only connect to one next step.

First steps must be full steps.
