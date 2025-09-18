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

Delays can make your Canvas look cleaner. You can also use this component to delay a different step until an exact date, until a specific day, or until a specific day of the week. <br> ![A Delay step with a 1-day delay as the first step of a Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Creating a delay

To create a delay, add a step to your Canvas. Drag and drop the Delay component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Delay**.

There are several details to consider when creating a delay in your Canvas journey.

- The delay limit is 30 days.
- A Delay component can only connect to one next step.

#### Extended delays

You can now extend Delay steps up to two years. For example, if you're onboarding new users for your app, you can add an extended delay for two months before sending a Message step to nudge the users who haven't started a session.

## Time delay types

You can choose the type of delay before the next message in your Canvas. You can either set a delay for your users to last until after a designated time period, or delay your users until a specific date and time.

{% tabs %}
{% tab Duration %}

Selecting **Duration** allows you to delay users for a set number of seconds, minutes, hours, days, or weeks, and at a specific time. For example, you can delay users for four hours or for one day.
  
Note the difference between how "days" and "calendar days" are calculated.
  
- A "day" is 24 hours and is calculated from the time the user enters the Delay step. 
- A "calendar day" defines the time to wait until the next specified time, which could be less than 24 hours. You can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

You can also select **At a specific time** to specify when the users will advance in the Canvas. This option takes into account the time the user entered the Delay step. If this time is beyond the time configured in the settings, we'll append more hours to the delay. 

As an example, let's say today is December 11, and our Delay step is set to **Duration** of one week at 8 am UTC. If a user enters the Delay step on December 4, they would be released from the Delay step to continue their journey today if they originally entered the Delay step at a time before 8 am UTC. If they entered the Delay step after this time, the user will be delayed until the next day (the next occurrence of this time). 

{% endtab %}
{% tab Calendar date %}

Selecting **Calendar date** allows you to hold users in the step until a specific date and time.

#### Considerations

##### Users won't receive past-dated steps or messages

If the selected date and time have already passed by the time users proceed to the Delay step, users will exit the Canvas. There can be up to 31 days between the start of the Canvas and the dates chosen for "wait until an exact day" steps.

{% alert important %}
If you're participating in the [Context step early access]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), you can set delays of up to 2 years.
{% endalert %}

For example, users won't receive steps or messages in these scenarios:

- A message is scheduled to be sent on May 3rd at 9 pm, but the Delay step expires on May 3rd at 9 am. 
- A Canvas step delays until a specific time in the user's local time zone, but the users don't have a time zone set on their user profile. The delay then defaults to the company time zone for these users, which has already passed the specified time. 
  
##### Users will exit if a subsequent Delay step is within a prior Delay step's timeline

If the Canvas has two Delay steps but the first Delay step is longer than the second Delay step, users will also exit the Canvas. 

For example, let's say a Canvas has these steps:
- Step 1: Message step
- Step 2: Delay step until December 13th at 10 pm
- Step 3: Message step
- Step 4: Delay step until December 13th at 7 pm
- Step 5: Message step
  
The users who enter Step 4 will exit the Canvas before receiving Step 5 because Step 4's delay is part of Step 2's timeframe.

{% endtab %}
{% tab Day of the week %}

Selecting **Day of the week** allows you to hold users in the step until a specific day of the week, at a specific time. For example, you can delay users until the next time Thursday arrives at 4 pm in the company's time zone. 

To successfully configure this, you will also need to select what happens if the user enters the Canvas on the selected day of the week (for example, Thursday), but after the specified time. You can choose to either advance the user on the same day or hold them until the following week.
{% endtab %}
{% endtabs %}

## Using Delay steps

Let's say that it's June 10. On June 11, you'd like users to enter the Canvas and receive a message about an upcoming promotion. Then, you want to hold users in the Canvas until June 17 at 3 pm local time. At 3 pm local time on June 17, you want to send users a reminder message about the promotion.

The sequence of Canvas steps could look like the following:

1. Start by adding a Message step that sends immediately after users enter the Canvas on June 11.
2. Create a Delay step that holds users until 1 pm local time on June 17.
3. Link the Delay step to another Message step that sends its message immediately.

### Delay components at the end of a Canvas {#delay-as-last-step}

If you add a Delay component to your Canvas and there are no subsequent steps, any user who reaches the last step will be automatically advanced out of the Canvas. This is true even if the time of the Delay step hasn't been reached yet. This means that users who have already reached the Delay step will not receive any messages you add after this step. However, if a user has not reached the Delay step and a message is added, then they would receive that message.

### Personalized delays

{% alert important %}
Personalized delays and extended delays are in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

Select the **Personalize delay** toggle to set up a personalized delay for your users. You can use this with a [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) to select the context variable to delay by. This will override the time of day set in the selected attribute or property. This is useful when applying an offset in days or weeks, and you want users to move forward at a specific time. The time zone comes from the attribute or property, or uses the fallback if none is available. 

Note that it's possible for a custom attribute or context variable to have neither a specific time nor a time zone if it's a string data type. If it's a time data type, you'll need to specify the time and time zone. However, if the custom attribute or context variable is an "irrelevant" string (such as "product_name"), the user will exit the Canvas.

#### Use case

Let's say you want to remind your customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, you can select this context variable to delay by. In this case, your Context step would have the following fields:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.]({% image_buster /assets/img/context_step1.png %})

Next, because you want to remind your customers 30 days from now, you'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from your Context step. This means your users will be delayed until the selected Context variable.

## Delay analytics

Delay components have the following metrics available in the analytics view of an active or previously active Canvas.

| Metric | Description |
|---|---|
| _Entered_ | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Delay step twice, two entries will be recorded. |
| _Proceeded to Next Step_ | Reflects the number of entries that proceeded to the next step in the Canvas. |
| _Exited Canvas_ | Reflects the number of entries that exited the Canvas and did not proceed to the next step. |
| _Personalization Failed_ | Reflects the number of times a personalized message or content intended for a user couldn't be delivered due to the following:<br> {::nomarkdown}<ul><li>Delay value is in the past</li><li>Delay value is over 2 years into the future</li><li><b>After a duration</b> value isn't a number</li><li><b>Until a specific day</b> value isn't a date or date-formatted string</li></ul>{:/} <br>See [Personalization failed errors](#personaliztion-failed-errors) for more details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Time series for these analytics are available in the expanded component view.

## Troubleshooting

### Personalization failed errors

If users aren't triggering a personalized delay, it could be because the Context step you set to qualify them for the Delay step is not working as you expected. When a [context variable is invalid]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), a user will continue through your Canvas without having their context set by the Context step. This can cause them to not qualify for steps later in your Canvas, such as personalized delays.

