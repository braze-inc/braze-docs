---
nav_title: FAQs
article_title: In-App Messages FAQs
page_order: 19
description: "This article provides answers to frequently asked questions about In-App Messages."
tool: in-app messages

---

# In-App Messages FAQs

> This article provides answers to some frequently asked questions about in-app messages.

### Will an in-app message display if a device is offline?

It depends. Because in-app messages are delivered at session start, the device is able to download the payload prior to going offline, the in-app message can still be displayed while offline. If the payload is not downloaded, then the in-app message will not display.

### If a user already has an in-app message payload on their device and the message expiration is changed, will the expiration be updated on their device?

When a user starts a session, Braze checks if changes have been made to any in-app messages that they are eligible for and updates them accordingly. So if the expiration has changed and they log a session, then the in-app message is sent to the device with the updated information.

### How do I set up Quiet Hours for an in-app message campaign?

The Quiet Hours feature isn't available for use with in-app message campaigns. This feature is used to prevent messages from being sent to your users during specific hours. For in-app message campaigns, your users will only receive in-app messages if they are active within the app. 

As a workaround to send in-app messages during a specific time, use the following sample Liquid code. This allows the message to be aborted if the in-app message is displayed after 7:59 pm or before 8 am at the specified timezone.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### When is eligibility for an in-app message calculated?

Eligibility for an in-app message is calculated at the time of delivery. If an in-app message is scheduled to send at 7 am, then eligibility is checked for this in-app message at 7 am.

Once the in-app message is displayed, the eligibility will depend on when the in-app message is downloaded and triggered.

### Why is my archived in-app message campaign still delivering in-app message impressions?

This can occur for users who met the segment criteria when the in-app message campaign was active.

To prevent this, during your campaign setup, select **Re-evaluate campaign eligibility before displaying**. 

### How does Braze calculate an in-app message expiration set to "after 1 day(s)"?

Braze calculates an expiration time of one day as 24 hours after users are eligible to receive a message.