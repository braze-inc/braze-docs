---
nav_title: Report Metrics Glossary
article_title: Report Metrics Glossary
layout: report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "This glossary defines terms you'll find in your reports in your Braze account."
tool: Reports
---

{% api %}

### AMP Clicks

{% apitags %}
Email
{% endapitags %}

The total number of users who clicked into the AMP version of your AMP HTML Email.

{% endapi %}

{% api %}

### Audience

{% apitags %}
All
{% endapitags %}

Percentage of users who received a particular message. This number is received from Braze.

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

The total number of messages that were unsuccessful. This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched. An email bounce for customers using SendGrid consists of hard bounces, spam, and emails sent to invalid addresses.

*Calculation: (Bounces) / (Sends)*

{% endapi %}

{% api %}

### Body Click

{% apitags %}
iOS Push, Android Push
{% endapitags %}

Push Story Notifications record a body click when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.

*Calculation: (Body Clicks) / (Impressions)*

{% endapi %}

{% api %}

### Body Clicks

{% apitags %}
In-App Message
{% endapitags %}

Occurs when someone clicks on any of the following in-app message types:
- Slide-up
- Modal
- Fullscreen that has no buttons

*Calculation: (Body Clicks) / (Impressions)*

{% endapi %}

{% api %}

### Button 1 Clicks

{% apitags %}
In-App Message
{% endapitags %}

Total number of clicks on Button 1 of the message.

*Calculation: (Button 1 Clicks) / (Impressions)*

{% endapi %}

{% api %}

### Button 2 Clicks

{% apitags %}
In-App Message
{% endapitags %}

Total number of clicks on Button 2 of the message.

*Calculation: (Button 2 Clicks) / (Impressions)*

{% endapi %}

{% api %}

### Choices Submitted

{% apitags %}
In-App Message
{% endapitags %}

Total number of choices selected when the user clicks the submit button on the survey question page of a [Simple Survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Click-to-Open Rate

{% apitags %}
Email
{% endapitags %}

The percentage of opened emails that were clicked. This metric is only available in the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

*Calculation: (Unique Clicks) / (Unique Opens) (for Email)*

{% endapi %}

{% api %}

### Confirmed Deliveries

{% apitags %}
SMS
{% endapitags %}

The carrier has confirmed that the SMS was delivered to the target phone number. As a Braze customer, deliveries are charged toward your SMS allotment.

*Calculation: Count*

{% endapi %}

{% api %}

### Confirmation Page Button

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the call to action button on the confirmation page of a [Simple Survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Confirmation Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the close (x) button on the confirmation page of a [Simple Survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Confidence

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

The percentage of confidence that a certain variant of a message is outperforming the control group.

{% endapi %}

{% api %}

### Conversions (B, C, D)

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

Additional conversion events added after the Primary Conversion Event. The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign. For Email, Push and Webhooks, we start tracking conversions after the initial send. For Content Cards and In-App Messages, this count begins when they view a Content Card or Message for the first time.

{% endapi %}

{% api %}

### Conversion Rate

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

The percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined when you build the campaign.

*Calculation: (Primary Conversions) / (Unique Recipients)*

{% endapi %}

{% api %}

### Deliveries

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

The total number of message requests that are accepted by the receiving server. This does not mean the message was delivered to a device, only that the message was accepted by the server.

*Calculation: Count*

{% endapi %}

{% api %}

### Delivery Failures

{% apitags %}
SMS
{% endapitags %}

The SMS could not be sent due to queues overflow (sending SMS at a rate higher than your long or short codes can handle).

*Calculation: (Sends) - (Sends to Carrier)*

{% endapi %}

{% api %}

### Errors

{% apitags %}
Webhook
{% endapitags %}

The number of errors returned by webhook events (incremented during the sending process).

{% endapi %}

{% api %}

### Failures

{% apitags %}
WhatsApp
{% endapitags %}

The WhatsApp message could not send because the Internet Service Provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.

{% endapi %}

{% api %}

### Influenced Opens

{% apitags %}
iOS Push, Android Push
{% endapitags %}

The total number (and percentage) of users who opened the app after the push notification was sent, without directly opening the push.

*Calculation: (Influenced Opens) / (Deliveries)*

{% endapi %}

{% api %}

### Pending Retry

{% apitags %}
Email
{% endapitags %}

The number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the ESP. The ESP will retry delivery until a timeout period is reached (typically after 72 hours).

{% endapi %}

{% api %}

### Primary Conversions (A) or Primary Conversion Event

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign. For Email, Push, and Webhooks, we start tracking conversions after the initial send. For Content Cards and In-App Messages, this count begins when they view a Content Card or Message for the first time.

{% endapi %}

{% api %}

### Reads

{% apitags %}
WhatsApp
{% endapitags %}

When a WhatsApp message is read by the end user. The end user's read receipts must be "On" for Braze to track reads.

{% endapi %}

{% api %}

### Rejections

{% apitags %}
SMS
{% endapitags %}

The SMS has been rejected by the carrier. This can happen for a number of reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, etc. As a Braze customer, rejections are charged toward your SMS allotment.

*Calculation: Count*

{% endapi %}

{% api %}

### Revenue per Recipient

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push
{% endapitags %}

The total direct revenue divided by unique recipients. This metric is only available on Campaign Comparison Reports, via the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

*Calculation: (Total Direct Revenue) / (Unique Recipients)*

{% endapi %}

{% api %}

### Sends

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

The total number of messages sent in a campaign. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This does not mean the message was received or delivered to a device, only that the message was sent. This metric is provided by Braze.

*Calculation: Count*

{% endapi %}

{% api %}

### Sends to Carrier

{% apitags %}
SMS
{% endapitags %}

This stat is the sum of Confirmed Deliveries, Rejections, and Sends where delivery or rejection was not confirmed by the carrier. There are instances where carriers do not provide delivery or rejected confirmation, as some carriers do not provide this confirmation or were unable to do so at the time of send.

*Calculation: Count*

{% endapi %}

{% api %}

### Spam

{% apitags %}
Email
{% endapitags %}

The total number of emails delivered that were marked as "spam."

*Calculation: (Marked as Spam) / (Sends)*

{% endapi %}

{% api %}

### Survey Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the close (x) button on the survey question page of a [Simple Survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Survey Submissions

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the submit button of a [Simple Survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Total Clicks

{% apitags %}
Email, Content Cards
{% endapitags %}

The total number (and percentage) of users who clicked within the delivered email or card.

*Calculation:*

- _**Email:** (Total Clicks) / (Deliveries)_
- _**Content Cards:** (Total Clicks) / (Total Impressions)_

{% endapi %}

{% api %}

### Total Direct Purchases

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push
{% endapitags %}

The total number of purchases made, based on last-click attribution*. This metric counts multiple purchases from a single user, for example if one user makes two purchases, the count will increment by two. This metric is only available on Campaign Comparison Reports, via the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

*Last-click attribution means that in order for revenue to be attributed to a campaign, that campaign must:

1. Be the last campaign the user clicked prior to purchasing, and
2. Be clicked by the user less than 3 days prior to purchasing.

{% endapi %}

{% api %}

### Total Direct Revenue

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push
{% endapitags %}

The amount of revenue generated by this campaign, based on last-click attribution*. This metric is only available on Campaign Comparison Reports, via the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

*Last-click attribution means that in order for revenue to be attributed to a campaign, that campaign must:

1. Be the last campaign the user clicked prior to purchasing, and
2. Be clicked by the user less than 3 days prior to purchasing.

{% endapi %}

{% api %}

### Total Dismissals

{% apitags %}
Content Cards
{% endapitags %}

The number of times Content Cards from a campaign have been dismissed. If a user dismisses a message twice, they will be only counted once.

*Calculation: Count*

{% endapi %}

{% api %}

### Total Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

The number of times the in-app message has been viewed (if a user is shown a message twice, they will be counted twice). This number is a sum of the number of impression events that Braze receives from the SDKs.

*Calculation: Count*

{% endapi %}

{% api %}

### Total Opens

{% apitags %}
Email, iOS Push, Android Push, Web Push
{% endapitags %}

The total number of messages that were opened.

*Calculation:*

- _**Email:** (Opens) / (Deliveries)_
- _**Web push:** (Direct Opens) / (Deliveries)_
- _**iOS, Android, and Kindle push:** (Unique Opens) / (Deliveries)_

{% endapi %}

{% api %}

### Total Revenue

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

The total revenue in dollars from campaign recipients within the set primary conversion window. This metric is only available on Campaign Comparison Reports, via the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

{% endapi %}

{% api %}

### Unique Clicks

{% apitags %}
Email, Content Cards
{% endapitags %}

Distinct number of recipients who have clicked within a message at least once. This is tracked over a 7-day period for Email. Note that clicks on Braze-provided unsubscribe links are counted as unique clicks.

*Calculation:*

- _**Email:** (Unique Clicks) / (Deliveries)_
- _**Content Cards:** (Unique Clicks) / (Unique Impressions)_

{% endapi %}

{% api %}

### Unique Dismissals

{% apitags %}
Content Cards
{% endapitags %}

The number of users who have dismissed Content Cards from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.

*Calculation: (Unique Dismissals) / (Unique Impressions)*

{% endapi %}

{% api %}

### Unique Opens

{% apitags %}
Email
{% endapitags %}

The total number of delivered emails that have been opened by a single user at least once. This is tracked over a 7-day period for Email.

*Calculation: (Unique Opens) / (Deliveries)*

{% endapi %}

{% api %}

### Unsubscribes

{% apitags %}
Email
{% endapitags %}

The number of recipients whose subscription state changed to unsubscribed as a result of clicking the Braze provided unsubscribe URL.

*Calculation: (Unsubscribes) / (Deliveries)*

{% endapi %}
