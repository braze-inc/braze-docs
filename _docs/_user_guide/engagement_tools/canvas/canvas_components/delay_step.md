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

Delays can make your Canvas look cleaner. You can also use this component to delay a different step until an exact date, until a specific day, or until a specific day of the week. <br> ![A Delay step with a 1-day delay as the first step of a Canvas.][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## Creating a delay

To create a delay, add a step to your Canvas. Drag and drop the Delay component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Delay**.

There are several details to consider when creating a delay in your Canvas journey.

- The delay limit is 30 days.
- A Delay component can only connect to one next step.

### Personalized delays

{% alert important %}
Personalized delays and extended delays are in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

Select the **Personalize delay** toggle to set up a personalized delay for your users. You can use this with a [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) to select the context variable to delay by.

Braze will exit a user at the step if:

- The context variable doesn't return to any value.
- An embedded Connected Content call fails.
- The context variable types don't match.

Let's say we want to remind our customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, we can select this context variable to delay by. In this case, our Context step would have the following fields:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.][2]

Next, because we want to remind our customers 30 days from now, we'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from our Context step. This means our users will be delayed until the selected Context variable.

![Example of using context variables with a Delay step to delay users based on the "product_reminder_interval".][3]

#### Extended delays

You can now extend Delay steps up to two years. For example, if you're onboarding new users for your app, you can add an extended delay for two months before sending a Message step to nudge the users who haven't started a session.

### Time delay options

You can choose the type of delay before the next message in your Canvas. You can either set a delay for your users to last until after a designated time period, or delay your users until a specific date and time.

{% tabs %}
{% tab After a duration %}

The **After a duration** option allows you to delay users for a set number of seconds, minutes, hours, days, or weeks, and at a specific time. For example, you can delay users for four hours or for one day.
  
Note the difference between how "days" and "calendar days" are calculated.
  
- A "day" is 24 hours and calculated from the time the user enters the Delay step. 
- A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

You can also select **At a specific time** to specify when the users will advance in the Canvas. This option takes into account the time the user entered the Delay step. If this time is beyond the time configured in the settings, we'll append more hours to the delay. As an example, let's say today is December 11, and our Delay step is set to **After a duration** of one week at 8 am UTC. If a user enters the Delay step on December 4, they would be released from the Delay step to continue their journey today if they originally entered the Delay step at a time before 8 am UTC. If they entered the Delay step after this time, the user will be delayed until the next day (the next occurrence of this time). 

{% endtab %}
{% tab Until a specific date %}

The **Until a specific date** option allows you to hold users in the step until a specific date and time.

#### Considerations

##### Users won't receive past-dated steps or messages

If the selected date and time have already passed by the time users proceed to the Delay step, users will exit the Canvas. There can be a maximum of 31 days between the start of the Canvas and the dates chosen for "Wait until Exact Date" steps.

For example, users won't receive steps or messages in these scenarios:
- A message is scheduled to send on May 3rd at 9 pm, but the Delay step expires on May 3rd at 9 am. 
- A Canvas step delays until a specific time in the user's local time zone, but the users don't have a time zone set on their user profile. The delay then defaults to the company time zone for these users, which has already passed the specified time. 
  
##### Users will exit if a subsequent Delay step is within a prior Delay step's timeline

If the Canvas has two Delay steps using "Wait until Exact Date" but the first Delay step is longer than the second Delay step, users will also exit the Canvas. 

For example, let's say a Canvas has these steps:
- Step 1: Message step
- Step 2: Delay step until December 13th at 10 pm
- Step 3: Message step
- Step 4: Delay step until December 13th at 7 pm
- Step 5: Message step
  
The users who enter Step 4 will exit the Canvas before receiving Step 5 because Step 4's delay is part of Step 2's timeframe.

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
| _Entered_ | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Delay step twice, two entries will be recorded. |
| _Proceeded to Next Step_ | Reflects the number of entries that proceeded to the next step in the Canvas. |
| _Exited Canvas_ | Reflects the number of entries that exited the Canvas and did not proceed to the next step. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Time series for these analytics are available in the expanded component view.

[1]: {% image_buster /assets/img/canvas_delay.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}
