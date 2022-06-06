---
nav_title: Message Step
article_title: Message Step
alias: "/message_step/"
page_order: 5
page_type: reference
description: "This reference article covers how to create a stand-alone message using the Canvas messaging step."
tool: Canvas

---

# Message Step

Message Steps allow you to add a standalone message where you want in your Canvas flow.

## Create a Message Step

![][1]{: style="float:right;max-width:19%;margin-left:15px;"}

To create a Message Step, add a step to your Canvas. Then, use the dropdown at the top of the new step to select **Message**.

With a Message Step, all users who enter the step advance to the next step when any one of the following conditions is met:
- Any message is sent
- A message is not sent because the user is not reachable with a channel
- A message is not sent because it is frequency capped
- A message is not sent because it is aborted

![Set up Messages settings for a Canvas Message Step that includes the option to select your message channel and customize delivery settings.][2]{: style="max-width:75%;"} 

The Message Step also includes settings for Intelligent Delivery, Quiet Hours overrides, and delivery validation.

The Message Step allows you to enable Intelligent Timing with a fallback option when a user’s profile does not have enough data to calculate an optimal time. Select **Using Intelligent Timing** in **Delivery Settings**. Here, you can select either the most popular time or a specific fallback time. 

If Quiet Hours are enabled, the Message Step also allows you to override this setting.

Delivery validations provide an additional check to confirm your audience meets the delivery criteria at message send. This setting is recommended if Quiet Hours, Intelligent Timing, or [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) are activated. You can add a segment or additional filters to validate at the time of the message being sent.

![The Delivery Settings tab for Message Step settings. Quiet Hours are enabled, and the checkbox for Using Intelligent Timing is selected to deliver the message at an optimal time. Delivery Validations are enabled to validate the audience at message send.][4]{: style="max-width:80%;"}

For Canvas Message Steps, `event_properties` are not supported. Instead, use `canvas_entry_properties`. Canvas entry properties are properties from the event that triggered the Canvas. These properties can only be used in the first full step of a Canvas. Conversely, event properties originate from an event or action that occurs as the user goes through their workflow.

## Analytics

Refer to the following table for definitions of Message Step metrics: 

| Metric | Description |
| --- | --- |
| Entries | The number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Message Step twice, two entries will be recorded. |
| Proceeded to Next Step | The number of entries that proceeded to the next step in the Canvas. |
| Sends | The total number of messages the step has sent. If your Canvas re-eligibility and a user enters a Message Step twice, two entries will be recorded. |
| Unique Recipients | The number of users who have received messages from this step. |
| Primary Conversion Event | The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. You define this event when building the campaign. |
| Revenue | The total revenue in dollars from campaign recipients within the set primary conversion window. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
