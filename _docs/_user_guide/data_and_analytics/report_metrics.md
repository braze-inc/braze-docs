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

{% multi_lang_include metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Audience

{% apitags %}
All
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} This could occur because there isn't a valid push token, the user unsubscribed after the campaign was launched, or the email address is inaccurate or deactivated.

<span class="calculation-line">Calculation: (Bounces) / (Sends)</span>

{% endapi %}

{% api %}

### Bounces % or Bounce Rate

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces % or Bounce Rate' %}

This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched.

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).

{% endapi %}

{% api %}

### Body Click

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Click' %}

<span class="calculation-line">Calculation: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Body Clicks

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Clicks' %}

<span class="calculation-line">Calculation: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Button 1 Clicks

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 1 Clicks' %}

<span class="calculation-line">Calculation: (Button 1 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Button 2 Clicks

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 2 Clicks' %}

<span class="calculation-line">Calculation: (Button 2 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### Choices Submitted

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Click-to-Open Rate

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calculation: (Unique Clicks) / (Unique Opens) (for Email)</span>

{% endapi %}

{% api %}

### Confirmed Deliveries

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Confidence

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Confirmation Page Button

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Confirmation Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversions (B, C, D)

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} This defined event is determined by the marketer when building the campaign. For email, push, and webhooks, we start tracking conversions after the initial send. For Content Cards and in-app messages, this count begins when they view a Content Card or message for the first time.

{% endapi %}

{% api %}

### Conversion Rate

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion rate' %}

<span class="calculation-line">Calculation: (Primary Conversions) / (Unique Recipients)</span>

{% endapi %}

{% api %}

### Conversion Window

{% apitags %}
All
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Deliveries

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} For emails, *Deliveries* is the total number of messages (Sends) successfully sent to and received by emailable parties.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Delivery Failures

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

<span class="calculation-line">Calculation: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

### Direct Opens

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">Calculation: (Direct Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

### Errors

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %}

{% endapi %}

{% api %}

### Failures

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} A hard bounce might occur because the domain name doesn't exist or because the recipient is unknown. If an email receives a hard bounce, we will stop any future requests to this email address.

{% endapi %}

{% api %}

### Influenced Opens

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Calculation: (Influenced Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

### Machine Opens

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %} This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

{% endapi %}

{% api %}

### Other Opens

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Note that a user can also open an email (such as the open counts toward Other Opens) before a Machine Opens count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward Other Opens and only once toward Unique Opens.

{% endapi %}

{% api %}

### Pending Retry

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Primary Conversions (A) or Primary Conversion Event

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} For email, push, and webhooks, we start tracking conversions after the initial send. For Content Cards and in-app messages, this count begins when they view a Content Card or message for the first time.

{% endapi %}

{% api %}

### Reads

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Received

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Received' %} 

- Content Cards: Received when users view the card in the app.
- Push: Received when messages are sent from the Braze server to the push provider.
- Email: Received when messages are sent from the Braze server to the email service provider.
- SMS/MMS: “Delivered” after the SMS provider receives confirmation from the upstream carrier and destination device.
- In-app message: Received at the time of display based on the trigger action defined.
- WhatsApp: Received at the time of display based on the trigger action defined.

{% endapi %}

{% api %}

### Rejections

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %} As a Braze customer, rejections are charged toward your SMS allotment.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %}  This metric is provided by Braze.

{% alert tip %}
For Content Cards, this metric is calculated differently depending on what you selected for [Card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).
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

{% multi_lang_include metrics.md metric='Sends to Carrier' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} A soft bounce might occur because the recipient's inbox is full, the server was down, or the message was too large for the recipient's inbox. If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

{% endapi %}

{% api %}

### Spam

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

<span class="calculation-line">Calculation: (Marked as Spam) / (Sends)</span>

{% endapi %}

{% api %}

### Survey Page Dismissals

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Survey Submissions

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Total Clicks

{% apitags %}
Email, Content Cards, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Clicks' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>Email:</b> (Total Clicks) / (Deliveries)</li>
        <li><b>Content Cards:</b> (Total Clicks) / (Total Impressions)</li>
        <li><b>SMS:</b> (Click Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total Dismissals

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Dismissials' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Opens

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %}

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

{% multi_lang_include metrics.md metric='Total Revenue' %}

{% endapi %}

{% api %}

### Unique Clicks

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %}

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

{% multi_lang_include metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Calculation: (Unique Dismissals) / (Unique Impressions)</span>

{% endapi %}

{% api %}

### Unique Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Impressions' %}  For in-app messages, unique impressions can be incremented again after 24 hours if re-eligibility is on and a user performs the trigger action. Conversely, the count should not increment the second time a user views a Content Card. This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unique Opens

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.

<span class="calculation-line">Calculation: (Unique Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

### Unique Recipients

{% apitags %}
All
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unsubscribes

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Calculation: (Unsubscribes) / (Deliveries)</span>

{% endapi %}

{% api %}

### Variation

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}