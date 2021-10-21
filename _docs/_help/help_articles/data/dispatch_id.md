---
nav_title: Dispatch ID Behavior
article_title: Dispatch ID Behavior
page_order: 1

page_type: solution
description: "This article covers dispatch ID behavior, including it's usage, implications, and limitations."
---

# Dispatch id behavior

A `dispatch_id` is the ID of the message dispatch - a unique ID for each "transmission" sent from Braze. Users who are send a scheduled message get the same `dispatch_id`, while action-based or API-triggered messages will receive a unique `dispatch_id` per user.

{% alert important %}
Note that `dispatch_ids` are per user, per campaign for triggered (action-based or API-triggered) messages.
{% endalert %}

This can result in two different users having different `dispatch_ids` for a single campaign if messages were sent at two different times. This is often because the API requests were made separately. If both users were in the same campaign audience in a single send, their Dispatch IDs would be the same.

## Dispatch id behavior in campaigns

Scheduled campaign messages get the same `dispatch_id`. Action-based or API-triggered campaign messages will get a unique `dispatch_id` per user.

Multichannel campaigns will have the same behavior as described above.

For example, if Becky and Tom are both included in your scheduled campaign audience, then they will have the same `dispatch_id`.

If they are included in the audience of an API-triggered campaign, they will have different `dispatch_ids`.

{% alert warning %}
Dispatch IDs are generated randomly for all Canvas Steps because Braze treats Canvas Steps as triggered events, even when they are "scheduled". This may result in inconsistencies generating the ids. Sometimes, a Canvas step will have unique `dispatch_ids` per user per send, or it may have shared `dispatch_ids` across users per send.
{% endalert %}

## Template dispatch id into messages with liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

## Dispatch id currents field for email

In the effort to continue enhancing our Currents capabilities, we're adding `dispatch_id` as a field to Currents Email events across all connector types.

The `dispatch_id` is the unique id generated for each transmission – or, dispatch – sent from the Braze platform.

While all customers who are sent a scheduled message get the same `dispatch_id`, customers who receive either action-based or API-triggered messages will get a unique `dispatch_id` per message. The `dispatch_id` field enables you to identify which instance of a recurring campaign is responsible for conversion, thus equipping you with more insights and information on which types of campaigns are helping push the needle on your business goals.

You can use `dispatch_id` as a [Personalization Tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/), or when you use [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events), or [Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) for Currents.

_Last updated on July 15, 2021_
