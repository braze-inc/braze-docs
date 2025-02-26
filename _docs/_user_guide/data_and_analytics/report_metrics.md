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

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

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

<span class="calculation-line">Calculation: (Bounces) / (Sends)</span>

{% endapi %}

{% api %}

### Body Click

{% apitags %}
iOS Push, Android Push
{% endapitags %}

Push Story Notifications record a body click when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.

<span class="calculation-line">Calculation: (Body Clicks) / (Impressions)</span>

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

<span class="calculation-line">Calculation: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Button 1 Clicks

{% apitags %}
In-App Message
{% endapitags %}

Total number of clicks on Button 1 of the message.

<span class="calculation-line">Calculation: (Button 1 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Button 2 Clicks

{% apitags %}
In-App Message
{% endapitags %}

Total number of clicks on Button 2 of the message.

<span class="calculation-line">Calculation: (Button 2 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Campaign analytics

{% apitags %}
Feature Flags
{% endapitags %}

The performance of the message across various channels. The metrics shown depend on the selected messaging channel, and whether the [Feature Flag experiment]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) is a multivariate test.

{% endapi %}

{% api %}

### Choices Submitted

{% apitags %}
In-App Message
{% endapitags %}

Total number of choices selected when the user clicks the submit button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Click-to-Open Rate

{% apitags %}
Email
{% endapitags %}

The percentage of opened emails that were clicked. This metric is only available in the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).

<span class="calculation-line">Calculation: (Unique Clicks) / (Unique Opens) (for Email)</span>

{% endapi %}

{% api %}

### Confirmed Deliveries

{% apitags %}
SMS
{% endapitags %}

The carrier has confirmed that the SMS was delivered to the target phone number. As a Braze customer, deliveries are charged toward your SMS allotment.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Confidence

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

The percentage of confidence that a certain variant of a message is outperforming the control group.

{% endapi %}

{% api %}

### Confirmation Page Button

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the call to action button on the confirmation page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Confirmation Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the close (x) button on the confirmation page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

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

<span class="calculation-line">Calculation: (Primary Conversions) / (Unique Recipients)</span>

{% endapi %}

{% api %}

### Conversion Window

{% apitags %}
All
{% endapitags %}

The number of days after receiving the message during which user actions are tracked and attributed to a conversion event. Conversions that occur after this window are not attributed to the conversion event.

{% endapi %}

{% api %}

### Deliveries

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

The total number of message requests that are accepted by the receiving server. This does not mean the message was delivered to a device, only that the message was accepted by the server.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Delivery Failures

{% apitags %}
SMS
{% endapitags %}

The SMS could not be sent due to queues overflow (sending SMS at a rate higher than your long or short codes can handle).

<span class="calculation-line">Calculation: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

### Direct Opens

{% apitags %}
iOS Push
{% endapitags %}

The total number (and percentage) of push notifications that were directly opened from that push.

<span class="calculation-line">Calculation: (Direct Opens) / (Deliveries)</span>

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

### Feature flag experiment performance

{% apitags %}
Feature Flags
{% endapitags %}

Performance metrics for the message in a Feature Flag experiment. The specific metrics shown will vary depending on the messaging channel, and whether or not the experiment was a multivariate test.

{% endapi %}

{% api %}

### Influenced Opens

{% apitags %}
iOS Push, Android Push
{% endapitags %}

The total number (and percentage) of users who opened the app after the push notification was sent, without directly opening the push.

<span class="calculation-line">Calculation: (Influenced Opens) / (Deliveries)</span>

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

### Received

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS, WhatsApp
{% endapitags %}

- Content Cards: Received when users view the card in the app.
- Push: Received when messages are sent from the Braze server to the push provider.
- Email: Received when messages are sent from the Braze server to the email service provider.
- SMS/MMS: "Delivered" once the SMS provider receives confirmation from the upstream carrier and destination device.
- In-App Message: Received at the time of display based on the trigger action defined.
- WhatsApp: Received at the time of display based on the trigger action defined.

{% endapi %}

{% api %}

### Rejections

{% apitags %}
SMS
{% endapitags %}

The SMS has been rejected by the carrier. This can happen for a number of reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, etc. As a Braze customer, rejections are charged toward your SMS allotment.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

*Sends*, or *Messages Sent*, is the total number of messages sent in a campaign. Upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This does not mean the message was received or delivered to a device, only that the message was sent. This metric is provided by Braze.

{% alert tip %}
For Content Cards, this metric is calculated differently depending on what you selected for **Card creation**. See [Card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) for details.
{% endalert %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends to Carrier

{% apitags %}
SMS
{% endapitags %}

{% alert note %}
*Sends to Carrier* is deprecated, but will continue to be supported for users that already have it.
{% endalert %}

This stat is the sum of Confirmed Deliveries, Rejections, and Sends where delivery or rejection was not confirmed by the carrier. There are instances where carriers do not provide delivery or rejected confirmation, as some carriers do not provide this confirmation or were unable to do so at the time of send.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Spam

{% apitags %}
Email
{% endapitags %}

The total number of emails delivered that were marked as "spam."

<span class="calculation-line">Calculation: (Marked as Spam) / (Sends)</span>

{% endapi %}

{% api %}

### Survey Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the close (x) button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Survey Submissions

{% apitags %}
In-App Message
{% endapitags %}

Total clicks on the submit button of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).

{% endapi %}

{% api %}

### Total Clicks

{% apitags %}
Email, Content Cards
{% endapitags %}

The total number (and percentage) of users who clicked within the delivered email or card.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>Email:</b> (Total Clicks) / (Deliveries)</li>
        <li><b>Content Cards:</b> (Total Clicks) / (Total Impressions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total Dismissals

{% apitags %}
Content Cards
{% endapitags %}

The number of times Content Cards from a campaign have been dismissed. If a user dismisses a message twice, they will be only counted once.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

The number of times the in-app message has been viewed (if a user is shown a message twice, they will be counted twice). This number is a sum of the number of impression events that Braze receives from the SDKs.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Opens

{% apitags %}
Email, iOS Push, Android Push, Web Push
{% endapitags %}

The total number of messages that were opened.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>Email:</b> (Opens) / (Deliveries)</li>
        <li><b>Web push:</b> (Direct Opens) / (Deliveries)</li>
        <li><b>iOS, Android, and Kindle push:</b> (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}


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

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>Email:</b> (Unique Clicks) / (Deliveries)</li>
        <li><b>Content Cards:</b> (Unique Clicks) / (Unique Impressions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Unique Dismissals

{% apitags %}
Content Cards
{% endapitags %}

The number of users who have dismissed Content Cards from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.

<span class="calculation-line">Calculation: (Unique Dismissals) / (Unique Impressions)</span>

{% endapi %}

{% api %}

### Unique Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

The total number of users who received and viewed a given in-app message or card in a day. For in-app messages, unique impressions can be incremented again after 24 hours if re-eligibility is on and a user performs the trigger action. Conversely, the count should not increment the second time a user views a Content Card. This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unique Opens

{% apitags %}
Email
{% endapitags %}

The total number of delivered emails that have been opened by a single user at least once. This is tracked over a 7-day period for Email.

<span class="calculation-line">Calculation: (Unique Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

### Unique Recipients

{% apitags %}
All
{% endapitags %}

Unique Daily Recipients. The number of users who received a particular message in a day. This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unsubscribes

{% apitags %}
Email
{% endapitags %}

The number of recipients whose subscription state changed to unsubscribed as a result of clicking the Braze provided unsubscribe URL.

<span class="calculation-line">Calculation: (Unsubscribes) / (Deliveries)</span>

{% endapi %}

{% api %}

### Variation

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

Variation of a campaign, differing as defined by the creator.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}
