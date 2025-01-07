---
nav_title: Delay 
article_title: Delay 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "This reference article covers how to add a delay to your Canvas without needing to add an associated message."
tool: Canvas

---

# Delay

> Delay components allow you to add a stand-alone delay to a Canvas. You can add a delay to your Canvas without needing to add an associated message. 

Delays can make your Canvas look cleaner. You can also use this component to delay a different step until an exact date, until a specific day, or until a specific day of the week. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## Create a delay

To create a delay, first add a step to your Canvas. Drag and drop the Delay component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Delay**.

There are several details to consider when creating a delay in your Canvas journey.

- The delay limit is 30 days.
- A Delay component can only connect to one next step.

### Time delay options

You can choose the type of delay before the next message in your Canvas. You can either set a delay for your users to last until after a designated time period, or delay your users until a specific date and time.

{% tabs %}
  {% tab After a duration %}

  The **After a duration** option allows you to delay users for a set number of seconds, minutes, hours, days, or weeks, and at a specific time. For example, you can delay users for four hours or for one day. 
  
  Note the difference between how "days" and "calendar days" are calculated. 
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  {% endtab %}
  {% tab Until a specific date %}

  The **Until a specific date** option allows you to hold users in the step until a specific date and time.

  {% alert important %}
  If the selected date and time have already passed by the time users proceed to the Delay step, users will exit the Canvas. There can be a maximum of 31 days between the start of the Canvas and the dates chosen for "Wait until Exact Date" steps.
  {% endalert %}
  {% endtab %}
  {% tab Until a specific day of the week %}

  The **Until a specific day of the week** option allows you to hold users in the step until a specific day of the week, at a specific time. For example, you can delay users until the next time Thursday arrives at 4 pm in the company's time zone. 

  To successfully configure this, you will also need to select what happens if the user enters the Canvas on the selected day of the week (for example, Thursday), but after the specified time. You can choose to either advance the user on the same day or hold them until the following week.
  {% endtab %}
{% endtabs %}

## Using Delay steps

Let's say that it's June 10. On June 11, you'd like users to enter the Canvas and receive a message about an upcoming promotion. Then, you want to hold users in the Canvas until June 17 at 3 pm local time. At 3 pm local time on June 17, you want to send users a reminder message about the promotion.

The sequence Canvas steps could look like the following:

1. Start by adding a Message step that sends immediately after users enter the Canvas on June 11.
2. Create a Delay step that holds users until 1 pm local time on June 17.
3. Link the Delay step to another Message step that sends its message immediately.

### Delay components at the end of a Canvas {#delay-as-last-step}

If you add a Delay component to your Canvas, but there are no more steps after the delay component, any user that reaches the last step is automatically advanced out of the Canvas. This is true even if the time of the Delay step hasn't been reached yet. This means that, for users that have already reached the Delay step, they will not receive any messages you add after the Delay step. However, if a user has not reached the Delay step and a message is added, then they would receive that message.

## Delay analytics

Delays have three statistics available in the analytics view of an active or previously active Canvas.

| Metric | Description |
|---|---|
| `Entered` | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Delay step twice, two entries will be recorded. |
| `Proceeded to Next Step` | Reflects the number of entries that proceeded to the next step in the Canvas. |
| `Exited Canvas` | Reflects the number of entries that exited the Canvas and did not proceed to the next step. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Time series for these analytics are available in the expanded component view.

[1]: {% image_buster /assets/img/canvas_delay.png %}
