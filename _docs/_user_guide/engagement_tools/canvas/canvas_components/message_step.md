---
nav_title: Message 
article_title: Message 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "This reference article covers how to create a stand-alone message using the Canvas messaging step."
tool: Canvas

---

# Message 

Message Steps allow you to add a standalone message where you want in your Canvas flow.

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Create a Message component

To create a Message component, first add a step to your Canvas. For Canvas Flow, drag and drop the Delay component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Message**. For the original Canvas editor, use the dropdown at the top of the new full step in your workflow to select **Message**.

### Set up messages

With a Message component, all users who enter the step advance to the next step when any one of the following conditions is met:
- Any message is sent
- A message is not sent because the user is not reachable with a channel
- A message is not sent because it is frequency capped
- A message is not sent because it is aborted

![Set up Messages settings for a Canvas Message component that includes the option to select your message channel and customize delivery settings.][2]{: style="max-width:75%;"} 

### Edit delivery settings

The Message component also includes settings for Intelligent Delivery, Quiet Hours overrides, and delivery validation. You can enable [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) with a fallback option when a user’s profile does not have enough data to calculate an optimal time. We recommend enabling Intelligent Timing and [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) as an additional check for any delays between users entering the Message Step and the actual message sending.

Select **Using Intelligent Timing** in the **Delivery Settings** tab. Here, you can select either the most popular time or a specific fallback time. If Quiet Hours are enabled, the Message Step also allows you to override this setting.

Delivery validations provide an additional check to confirm your audience meets the delivery criteria at message send. This setting is recommended if Quiet Hours, Intelligent Timing, or rate limiting are activated. You can add a segment or additional filters to validate at the time of the message being sent.

![The Delivery Settings tab for Message Step settings. Quiet Hours are enabled, and the checkbox for Using Intelligent Timing is selected to deliver the message at an optimal time. Delivery Validations are enabled to validate the audience at message send.][4]{: style="max-width:80%;"}

Canvas entry properties are properties from the event that triggered the Canvas. These properties can only be used in the first full step of a Canvas using the original workflow. These event properties originate from an event or action that occurs as the user goes through their workflow. 

Conversely, in Canvas Flow, action-based delivery event properties that trigger Canvas entry are not ephemeral, and can be used in Liquid in any Message step. For Canvas Flow, make sure to use ``{% raw %} canvas_entry~properties${property_name} {% endraw %}`` if referencing these Canvas entry properties. These events must be custom events or purchase events to be used this way in the Message component.

## Analytics

Refer to the following table for definitions of Message component metrics: 

| Metric | Description |
| --- | --- |
| Entries | The number of times the component has been entered. If your Canvas has re-eligibility and a user enters a Message component twice, two entries will be recorded. |
| Proceeded to Next Step | The number of entries that proceeded to the next step in the Canvas. |
| Sends | The total number of messages the component has sent. If your Canvas re-eligibility and a user enters a Message component twice, two entries will be recorded. |
| Unique Recipients | The number of users who have received messages from this component. |
| Primary Conversion Event | The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. You define this event when building the campaign. |
| Revenue | The total revenue in dollars from campaign recipients within the set primary conversion window. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
