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

> Message Steps allow you to add a standalone message where you want in your Canvas flow.

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Create a Message component

To create a Message component, first add a step to your Canvas. Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Message**. 

### Set up messages

All users who enter the Message step will advance to the next step when any one of the following conditions is met:
- Any message is sent
- A message is frequency capped and not sent
- A message is aborted
- A user isn't reachable by channel, so the message is not sent

![Set up Messages settings for a Canvas Message component that includes the option to select your message channel and customize delivery settings.][2]{: style="max-width:75%;"}

{% raw %}
If an action-based Canvas is triggered by an inbound SMS message, you can reference SMS properties in the first Message step of the Canvas. For example, in the Message step, you could use `{{sms.${inbound_message_body}}}` or `{{sms.${inbound_media_urls}}}`.
{% endraw %}

### Edit delivery settings

The Message component also includes settings for Intelligent Delivery, Quiet Hours overrides, and delivery validation. You can enable [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) with a fallback option when a user's profile does not have enough data to calculate an optimal time. We recommend enabling Intelligent Timing and [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) as an additional check for any delays between users entering the Message step and the actual message sending.

Select **Using Intelligent Timing** in the **Delivery Settings** tab. Here, you can select either the most popular time or a specific fallback time. If Quiet Hours are enabled, the Message step also allows you to override this setting.

Delivery validations provide an additional check to confirm your audience meets the delivery criteria at message send. This setting is recommended if Quiet Hours, Intelligent Timing, or rate limiting are activated. You can add a segment or additional filters to validate at the time of the message being sent. If a user doesn't meet the set delivery validations for a Message step, they will exit the Canvas at the step.

![The Delivery Settings tab for Message component settings. Quiet Hours are enabled, and the checkbox for Using Intelligent Timing is selected to deliver the message at an optimal time. Delivery Validations are enabled to validate the audience at message send.][4]{: style="max-width:80%;"}

### Canvas entry properties

Canvas entry properties are configured in the Entry Schedule step of creating a Canvas and will indicate the trigger that enters a user into a Canvas. These properties can also access the properties of entry payloads in API-triggered Canvases. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB. 

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas Flow and in the original Canvas editor if you have persistent entry properties enabled in the original editor as part of the previous early access.
{% endalert %}

#### Original workflow

For the Canvases built with the original editor, `canvas_entry_properties` can be referenced only in the first full step of a Canvas.

#### Canvas Flow

For Canvas Flow messaging, entry properties can be used in Liquid in any Message step. Use the following Liquid when referencing these entry properties: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Events must be custom events or purchase events to be used this way.

Use the following Liquid when referencing these entry properties: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Note that the events must be custom events or purchase events to be used this way.

{% raw %}
For example, consider the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. You could add the word "shoes" to a message with the Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

You can also leverage [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) in any Message step to guide your users through personalized steps throughout your Canvas workflow.

### Event properties

Event properties refer to the properties that you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases. 

#### Original workflow

`event_properties` can be used in the first full step in an action-based Canvas using the original workflow, even if the full step is scheduled. 

#### Canvas Flow

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step. For Canvas Flow, use this Liquid `` {% raw %} {{event_properties.${property_name}}} {% endraw %}`` when referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

{% alert important %}
`event_properties` cannot be used independently of Action Paths for Canvas Flow.
{% endalert %}

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. You can have other steps (that are not another Action Paths or Message step) in between this Action Paths step and the Message step. Note that you'll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Path step.

{% alert important %}
For the original Canvas editor and Canvas Flow, you can't use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event before the Message step that includes `event_properties`.
{% endalert %}

For more information and examples, check out [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).

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
