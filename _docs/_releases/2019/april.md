---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "This article contains release notes for April 2019."
---

# April 2019

## New Currents events & fields

In addition to some corrections to the section, a new [Subscription Event]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) has been added to the Message Engagement Events page. 

You can now export subscription group state change data from Braze to [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) and [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents/), as well as that and Install Attribution Events in [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

Additionally, the property `canvas_step_id` has been added to available [Conversion Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events).

{% alert important %}
To take advantage of these updates, you will need to edit your Currents connector settings and enable the events you want to use. Reach out to your account manager if you have any questions.
{% endalert %}

## Subscription groups archiving

You can now [archive Subscription Groups]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Archived Subscription Groups cannot be edited and will no longer appear in Segment Filters.  If you attempt to archive a group which is being used as a Segment Filter in any email, campaign, or Canvas, you will receive an error message that will prevent you from archiving the Group until you remove all usages of it.
