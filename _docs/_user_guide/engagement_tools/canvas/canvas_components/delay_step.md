---
nav_title: Delay Step
article_title: Delay Step
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "This reference article covers how to add a delay to your Canvas without needing to add an associated message."
tool: Canvas

---

# Delay Step

Delay Steps in Canvas allow you to add a stand-alone delay to a Canvas. In other words, you can add a delay to your Canvas without needing to add an associated message.

Delay Steps can make your Canvas cleaner. Where you've previously needed to create two full steps, you can create one delay step and a single, full step.

You can also use Canvas Delay Steps to delay a step until an exact date, rather than using `in 1 day` or `on the next` you can specify the exact date and time that users move to a full step.

## Create a delay step

To create a Delay Step, add a step to your Canvas. Then, use the drop-down at the top of the new step to select `Delay Step`.

![Canvas Delay Step][1]

- A delay step __cannot have full step sibling steps__. In other words, you cannot create a full step that branches into a delay step and a full step. This restriction exists because if there was a branch with a delay step and a full step, it wouldn’t be clear which branch users would go down.
- A delay step can __only__ connect to one next step.

### Time delay options

You can choose the type of delay before the next message in your Canvas. You can either set a delay for your users to last until `After...` a designated time period, or delay your users until a specific date and time.

{% tabs %}
  {% tab After... %}

  The `After` option allows you to delay users for a set number of seconds, minutes, hours, or weeks - for example, you can delay users for four hours or for one day.

  {% endtab %}
  {% tab Until Exact Date... %}

  The `Until Exact Date` option allows you to hold users in a step until a specific date and time.

  {% alert important %}
  If the selected date and time have already passed by the time users proceed to the delay step, users will exit the Canvas. There can be a maximum of 31 days between the start of the Canvas and the dates chosen for  “Wait until Exact Date” steps.
  {% endalert %}

  {% endtab %}
{% endtabs %}

## Using delay steps

Let’s say that it’s June 10th. On June 11th, you’d like users to enter the Canvas and receive a message about an upcoming promotion. Then, you want to hold users in the Canvas until June 17th at 3:00 PM local time. At 3:00 PM local time on June 17th, you want to send users a reminder message about the promotion.

You’d start by adding a full step that sends immediately after users enter the Canvas on June 11th. Then, you’d create a delay step that holds users in the step until 3:00 PM local time on June 17th. After that, you’d link the delay step to a full step that sends it’s message immediately.

## Delay step analytics

Delay steps have three statistics available in the analytics view of an active or previously active Canvas.

| Metric | Description |
|---|---|
| `Entered` | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a delay step twice, two entries will be recorded. |
| `Proceeded to Next Step` | Reflects the number of entries that proceeded to the next step in the Canvas. |
| `Exited Canvas` | Reflects the number of entries that exited the Canvas and did not proceed to the next step. |
{: .reset-td-br-1 .reset-td-br-2}

Time series for these analytics are available in the expanded step view.


[1]: {% image_buster /assets/img/canvas_delay.gif %}
