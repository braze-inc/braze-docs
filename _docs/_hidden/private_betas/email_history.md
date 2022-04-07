---
nav_title: Email History Tab FAQ
permalink: "/email_history/"
hidden: true
---

# Email History Tab FAQ

{% alert note %}
The **Email History** tab is an experimental feature rolled out only to select customers.
{% endalert %}

## What is the Email History tab?

The **Email History** tab of the user profile enables you to see recent email events (approximately 40) for an individual user from the past 30 days. It is currently an experimental feature rolled out only to select customers.

## Which events are included in the table?

The table displays the following email events:

- [Bounce]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-bounce-event)
- [Click]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events)
- [Delivery]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-delivery-events)
- [Marked as spam]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-spam-events)
- [Open]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-open-events)
- [Send]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-send-events)
- [Soft bounce]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-soft-bounce-event)
- [Unsubscribe]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-unsubscribe-events)

## Is the open event reliable?

Email open tracking is error prone in any tool, including Braze. With a variety of privacy protection features offered by different email clients that either block the automatic loading of images or load them proactively on the server, email open events are susceptible to both false postiives and false negatives. 

While email open statistics can be useful in aggregate, for example to compare the effectiveness of different subject lines, you should not assume an individual open event for an individual user is meaningful.

## Can I see other events in this table?

If you have feedback on this table, or would like to see specific events, we'd love to hear that feedback. Send an email with your feedback to [smb-product@braze.com](mailto:smb-product@braze.com?subject=Email%20History%20Tab%20Feedback) with the subject line "Email History Tab Feedback".