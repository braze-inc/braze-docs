---
nav_title: Delivery and entry types
article_title: Delivery and Entry Types
page_order: 5
page_type: reference
description: "This reference article describes the delivery types for campaigns, entry types for Canvases, and the time-based features when setting up a campaign or Canvas."
tool:
    - Campaigns
    - Canvas
---

# Scheduling your message

> In Braze, there are three different ways you can schedule your message: scheduled, action-based, and API-triggered. Choosing how and when your message gets delivered is crucial in developing an effective message. 

## Delivery and entry types

For campaigns, the delivery type determines when your users will enter your campaign and when it will be sent. Since a Canvas is built as an ongoing user journey, the messaging concept of a scheduling is referred to as an entry type.

| Delivery<nobr> and entry types | Description                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scheduled**       | This type of schedule is designed for one-off messages that you wish to send immediately, such as campaigns about a current event. <br><br>When sending test messages aimed at just yourself or your team, this option allows you to deliver them immediately.                                                                                   |
| **Action-Based**    | Action-based delivery messages, or event-triggered campaigns and Canvases, are very effective for transactional or achievement-based messages. You can trigger them to send after a user completes a certain event instead of sending your message on certain days.                                                                                           |
| **API-Triggered**   | API-triggered messages allow you to manage message copy, multivariate testing, and re-eligibility rules in the Braze dashboard while triggering the delivery of that content from your own servers and systems. <br><br>The API request to trigger the message can also include additional data to be templated into the message in real-time. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Time-based options

{% tabs %}
{% tab campaign %}
You can choose from the following options when using scheduled delivery:

- Send as soon as the campaign is launched
- Send at a designated time
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
With scheduled delivery, users will enter on a time schedule, similarly to how you would schedule a campaign. You can enroll users in a Canvas as soon as it's launched or at a designated time.

#### Designated times

You can choose to send your Canvas at a specific entry frequency, including just once, daily, weekly, or monthly. For Canvases with a recurring scheduled delivery, you can set the recurrence to allow users to enter the Canvas up to 30 designated times.
{% endtab %}
{% endtabs %}

### Action-based options

{% tabs %}
{% tab campaign %}
Action-based delivery will send campaigns to users who perform a specific action. After this action occurs, you can decide when to send the campaign: immediately, after a specific time, on a specific time, or at a time in the future.
{% endtab %}

{% tab canvas %}
The action-based options determine what actions (or triggers) a user needs to perform in order to enter a Canvas and at what specific time they're allowed to start entering. For example, you could evaluate your users by the following actions:

- Opening your app
- Adding an email address
- Entering a location

#### Entry window

The entry window of your Canvas determines which users can enter the Canvas at the designated start time (and optional end time). Similar to action-based campaigns, you can choose to enter users in their local time zone.
{% endtab %}
{% endtabs %}

### API trigger options

{% tabs %}
{% tab campaign %}
When you select API-triggered as your delivery option, you'll receive a campaign ID to identify which campaign to send in with the [`/campaigns/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites). 
{% endtab %}

{% tab canvas %}
When you select API-triggered as your entry type, you'll receive a Canvas ID to identify which campaign to send in with the [`/canvas/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
