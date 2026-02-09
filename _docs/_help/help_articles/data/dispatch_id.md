---
nav_title: Dispatch ID behavior
article_title: Dispatch ID Behavior
page_order: 0

page_type: solution
description: "This help article covers dispatch ID behavior, including its usage, implications, and limitations."
---

# Dispatch ID behavior

A `dispatch_id` is the ID of the message dispatch—a unique ID for each "transmission" sent from Braze. Users who are sent a scheduled message receive the same `dispatch_id`. Typically, action-based or API-triggered messages will receive a unique `dispatch_id` per user, but messages sent within close proximity to another may share the same `dispatch_id` across multiple users.

This can result in two different users having different dispatch IDs for a single campaign if messages were sent at two different times. This is often because the API requests were made separately. If both users were in the same campaign audience in a single send, their dispatch IDs would be the same.

## Dispatch ID behavior in campaigns

Scheduled campaign messages get the same `dispatch_id`. Action-based or API-triggered campaign messages may get a unique `dispatch_id` per user, or the `dispatch_id` may be the same for multiple users when sent within close proximity or in the same API call, as described above. For example, two users in your scheduled campaign audience will have the same `dispatch_id` each time the campaign is scheduled. However, two users in the audience of an API-triggered campaign may have different dispatch IDs if they were sent in separate API calls and not in close proximity to each other.

Multichannel campaigns will have the same behavior as described for their delivery type.

{% alert warning %}
A `dispatch_id` is generated randomly for all Canvas steps because Braze treats Canvas steps as triggered events, even when they are "scheduled". This may result in inconsistencies generating the IDs. Sometimes, a Canvas component will have a unique `dispatch_id` per user per send, or it may have shared dispatch IDs across users per send.
{% endalert %}

## Template dispatch ID into messages with Liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this under Canvas Attributes in our list of [supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The ID is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages since in-app messages don't have a `dispatch_id`.
{% endalert %}

## Dispatch ID Currents field for email

In the effort to continue enhancing our Currents capabilities, `dispatch_id` is also a field in Currents email events across all connector types. The `dispatch_id` is the unique ID generated for each transmission, or dispatch, sent from the Braze platform.

While all customers who are sent a scheduled message get the same `dispatch_id`, customers who receive either action-based or API-triggered messages will get a unique `dispatch_id` per message. The `dispatch_id` field enables you to identify which instance of a recurring campaign is responsible for conversion, thus equipping you with more insights and information on which types of campaigns are helping push the needle on your business goals.

You can use `dispatch_id` as a [personalization tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [message engagement events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), or when you use [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events), or [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) for Currents.

_Last updated on July 15, 2021_
