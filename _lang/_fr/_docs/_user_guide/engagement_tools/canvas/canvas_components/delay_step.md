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

Delay Steps allow you to add a stand-alone delay to a Canvas. You can add a delay to your Canvas without needing to add an associated message. Delay Steps can make your Canvas cleaner. Where you've previously needed to create two full steps, you can create one delay step and a single, full step.

You can also use Canvas Delay Steps to delay a step until an exact date, until a specific day, or until a specific day of the week.

!\[Canvas Delay Step\]\[1\]{: style="float:right;max-width:30%;margin-left:15px;"}

## Create a delay step

To create a Delay Step, add a step to your Canvas. Then, use the drop-down at the top of the new step to select **Delay**.

- A Delay Step cannot have full step sibling steps. In other words, you cannot create a full step that branches into a Delay Step and a full step. This restriction exists because if there was a branch with a Delay Step and a full step, it wouldn’t be clear which branch users would go down.
- A Delay Step can only connect to one next step.

### Time delay options

You can choose the type of delay before the next message in your Canvas. You can either set a delay for your users to last until after a designated time period, or delay your users until a specific date and time.

{% tabs %}
  {% tab After a duration %}

  The **After a duration** option allows you to delay users for a set number of seconds, minutes, hours, days or weeks, and at a specific time. For example, you can delay users for four hours or for one day.

  {% endtab %}
  {% tab Until a specific date %}

  The **Until a specific date** option allows you to hold users in the step until a specific date and time.

  {% alert important %}
  If the selected date and time have already passed by the time users proceed to the delay step, users will exit the Canvas. There can be a maximum of 31 days between the start of the Canvas and the dates chosen for “Wait until Exact Date” steps.
  {% endalert %}
  {% endtab %}
  {% tab Until a specific day of the week %}

  The **Until a specific day of the week** option allows you to hold users in the step until a specific day of the week, at a specific time. For example, you can delay users until the next time Thursday arrives at 4pm in the company’s timezone.

  To successfully configure this, you will also need to select what happens if the user enters the Canvas on the selected day of the week (e.g. Thursday), but after the specified time. You can choose to either advance the user on the same day or hold them until the following week.
  {% endtab %}
{% endtabs %}

## Using delay steps

Let’s say that it’s June 10. On June 11, you’d like users to enter the Canvas and receive a message about an upcoming promotion. Then, you want to hold users in the Canvas until June 17 at 3pm local time. At 3pm local time on June 17, you want to send users a reminder message about the promotion.

You’d start by adding a full step that sends immediately after users enter the Canvas on June 11. Then, you’d create a delay step that holds users in the step until 3pm local time on June 17. After that, you’d link the delay step to a full step that sends it’s message immediately.

## Delay step analytics

Delay steps have three statistics available in the analytics view of an active or previously active Canvas.

| Metric                   | Description                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Entered`                | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a delay step twice, two entries will be recorded. |
| `Proceeded to Next Step` | Reflects the number of entries that proceeded to the next step in the Canvas.                                                                                 |
| `Exited Canvas`          | Reflects the number of entries that exited the Canvas and did not proceed to the next step.                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

Time series for these analytics are available in the expanded step view.
[1]: {% image_buster /assets/img/canvas_delay.png %}
