---
nav_title: Dispatch ID Behavior
page_order: 1
---

# Dispatch ID Behavior

> Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled".

A `dispatch_id` is the ID of the message dispatch - a unique ID for each "transmission" sent from Braze. Users who are send a scheduled message get the same `dispatch_id`, while action-based or API-triggered messages will receive a unique `dispatch_id` per user.

These IDs are __per user, per Campaign/Canvas Step for triggered (action-based or API-triggered) messages__. This can result in two different users having different `dispatch_ids` for a single Campaign or Canvas Step.

## Dispatch ID Behavior in Canvas

Even through Canvas steps beyond the scheduled Entry Step are called "scheduled", they are technically triggered Campaigns, which are triggered "to send at a scheduled time" relative to when the recipient received the previous step or entered the canvas.

Thus, all Canvas steps beyond the first will have a unique `dispatch_id`.

For example, if Becky and Tom are both included in your Canvas entry step audience, then they will have the same `dispatch_id` for that step. If they both advance to the next step, they will have different `dispatch_ids` for that step, even if they advance through to the same next step.

## Dispatch ID Behavior in Campaigns

Scheduled Campaign messages get the same `dispatch_id`. Action-based or API-triggered Campaign messages will get a unique `dispatch_id` per user.

Multi-channel Campaigns will have the same behavior as described above.

For example, if Becky and Tom are both included in your scheduled Campaign audience, then they will have the same `dispatch_id`.

If they are included in the audience of an API-triggered Campaign, they will have different `dispatch_ids`.

# More on Using Dispatch ID

## Template Dispatch ID into Messages with Liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at Campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

## Dispatch ID Currents Field for Email

In the effort to continue enhancing our Currents capabilities, we're adding `dispatch_id` as a field to Currents Email events across all connector types.

The `dispatch_id` is the unique id generated for each transmission – or, dispatch – sent from the Braze platform.

While all customers who are sent a scheduled message get the same `dispatch_id`, customers who receive either action-based or API triggered messages will get a unique `dispatch_id` per message. The `dispatch_id` field enables you to identify which instance of a recurring campaign is responsible for conversion, thus equipping you with more insights and information on which types of campaigns are helping push the needle on your business goals.

You can use `dispatch_id` as a [Personalization Tag]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [Message Engagement Events]({{ site.baseurl }}/partners/braze_currents/data_storage_events/message_engagement_events/), or when you use [Segment]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{ site.baseurl }}/partners/technology_partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events), or [Amplitude]({{ site.baseurl }}/partners/technology_partners/insights/behavioral_analytics/amplitude_for_currents/#email-events) for Currents. 
