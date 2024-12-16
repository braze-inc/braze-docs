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

### AMP Opens

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Audience

{% apitags %}
All
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Calculation: (Number of Recipients in Variant) / (Unique Recipients)</span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} This could occur because there isn't a valid push token, the user unsubscribed after the campaign was launched, or the email address is inaccurate or deactivated.

#### Email

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).

For email, *Bounce %* or *Bounce Rate* is the percentage of messages that were unsuccessfully sent or designated as "returned" or "not received" from send services used or not received by the intended emailable users.

#### Push

These users have been automatically unsubscribed from all future push notifications. 

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Bounces</i>: Count</li>
        <li><i>Bounce %</i> or <i>Bounce Rate %</i>: (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

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

{% multi_lang_include metrics.md metric='Body Clicks' %} For more details, refer to the SDK changelogs for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

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

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} As a Braze customer, deliveries are charged toward your SMS allotment. 

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

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} This defined event is determined by you when building the campaign. For email, push, and webhooks, we start tracking conversions after the initial send. For Content Cards, this count begins when they view a Content Card for the first time.

#### In-app messages

For in-app messages, a conversion is counted if the user has received and viewed the in-app message campaign, and subsequently performs the specific conversion event within the defined conversion window, regardless of whether they clicked on the message or not.

Conversions are attributed to the most recently received message. If re-eligibility is enabled, the conversion will be assigned to the latest in-app message received, provided that it occurs within the defined conversion window. However, if the in-app message has already been assigned a conversion, then the new conversion cannot be logged for that specific message. This means that each in-app message delivery is associated with only one conversion.

{% endapi %}

{% api %}

### Total Conversions

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Conversions' %}

When a user views an in-app message campaign only once, only one conversion is counted, even if they perform the conversion event multiple times later on. However, if re-eligibility is turned on and the user sees the in-app message campaign multiple times, *Total Conversions* can increase once for each time the user logs an impression for a new instance of the in-app message campaign. 

For example, if a user triggers an in-app message twice and converts after each in-app message impression (resulting in two conversions), then *Total Conversions* will increase by two. However, if there was only one in-app message impression followed by two conversion events, only one conversion will be logged, and *Total Conversions* will increase by one.

{% endapi %}

{% api %}

### Conversion Rate

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### In-app messages

The metric of total daily <i>Unique Impressions</i> is used to calculate the <i>Conversion Rate</i> for in-app messages.

Impressions for in-app messages can only be counted once per day. On the other hand, the number of times a user completes a desired action (a "conversion") can increase within a 24-hour period. While conversions can happen more than once per day, impressions cannot. Therefore, if a user completes a conversion multiple times within a day, the <i>Conversion Rate</i> can increase accordingly, but impressions will only be counted once.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>In-App Messages</b>: (Primary Conversions) / (Unique Impressions)</li>
        <li><b>Other Channels</b>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

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

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Deliveries</i>: Count</li>
        <li><i>Deliveries %</i>: (Sends - Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Delivery Failures

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

Reach out to <a href="/docs/braze_support/">Braze Support</a> for assistance in understanding the reasons for delivery failures.

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

### Emailable

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Errors

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} Errors are included in the <i>Sends</i> count but are not included in the <i>Unique Recipients</i> count.

{% endapi %}

{% api %}

### Estimated Real Opens

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Failures

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} Failures are included in the <i>Sends</i> count but not in the <i>Deliveries</i> count.</td>

<span class="calculation-line">Calculation (<i>Failure Rate</i>): (Failures) / (Sends)</span>

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

When this occurs, Braze marks the email address as invalid but does not update the user's [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/). If an email receives a hard bounce, we will stop any future requests to this email address.

{% endapi %}

{% api %}

### Help

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} A user reply is measured anytime a user sends an inbound message within four hours of receiving your message.

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

### Lifetime Revenue

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Lifetime Value Per User

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Average Daily Revenue

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS,LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Daily Purchases

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Daily Revenue Per User

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Machine Opens

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %} This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

{% endapi %}

{% api %}

### Opens

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-Out

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Out' %} A user reply is measured anytime a user sends an inbound message within four hours of receiving your message.

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

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Primary Conversions (A) or Primary Conversion Event</i>: Count</li>
        <li><i>Primary Conversions (A) %</i> or <i>Primary Conversion Event Rate</i>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

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

### Revenue

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Sent

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sent' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} This metric is provided by Braze. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting.

{% alert tip %}
For Content Cards, this metric is calculated differently depending on what you selected for [Card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **At launch or step entry:** The number of cards created and available to be seen. This doesn't count whether the users viewed the card.
- **At first impression:** The number of cards displayed to users.
{% endalert %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Messages Sent

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %}  This metric is provided by Braze. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting.

{% alert tip %}
For Content Cards, this metric is calculated differently depending on what you selected for [Card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **At launch or step entry:** The number of cards created and available to be seen. This doesn't count whether the users viewed the card.
- **At first impression:** The number of cards displayed to users.
{% endalert %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends to Carrier

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends to Carrier' %} 

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

{% endapi %}

{% api %}

### Spam

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Spam</i>: Count</li>
        <li><i>Spam %</i> or <i>Spam Rate %</i>: (Marked as Spam) / (Sends)</li>
    </ul>
</span>
{:/}

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

{% multi_lang_include metrics.md metric='Total Clicks' %} For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached. For AMP emails, this is the total clicks in the HTML and plaintext versions.

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

{% multi_lang_include metrics.md metric='Total Dismissals' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Impressions

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %} This number is a sum of the number of impression events that Braze receives from the SDKs. For Content Cards, this is the total count of impressions logged for a given Content Card. This can increment multiple times for the same user.

For in-app messages, if there are multiple devices and re-eligibility is off, the user should only see the in-app message once. Even if the user uses multiple devices, they will only see it on the first device that is targeted. This assumes that the profile has consolidated devices and a user has one user ID that they are logged into across devices. If re-eligibility is on an impression is logged for every time that user sees the in-app message.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Total Opens

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %}  For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached. For AMP emails, this is the total opens for the HTML and plaintext versions. 

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

{% multi_lang_include metrics.md metric='Total Revenue' %} This metric is only available on Campaign Comparison Reports through the <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>

{% endapi %}

{% api %}

### Unique Clicks

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} This is tracked over a seven-day period for email. This includes clicks on Braze-provided unsubscribe links. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Unique Clicks</i>: Count</li>
        <li><b>Content Cards</b> <i>Unique Clicks %</i> or <i>Unique Clicks Rate</i>: (Unique Clicks) / (Unique Impressions)</li>
        <li><b>Email</b> <i>Unique Clicks %</i> or <i>Unique Clicks Rate</i>: (Unique Clicks) / (Deliveries)</li>
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

{% multi_lang_include metrics.md metric='Unique Impressions' %} For in-app messages, unique impressions can be incremented again after 24 hours if re-eligibility is on and a user performs the trigger action. If re-eligibilty is on, <i>Unique Impressions</i> = <i>Unique Recipients</i>. <br><br>For Content Cards, the count should not increment the second time a user views a card. 

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unique Opens

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} For email, this is tracked over a 7 day period. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Unique Opens</i>: Count</li>
        <li><i>Unique Opens %</i> or <i>Unique Open Rate</i>: (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Unique Recipients

{% apitags %}
All
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %}

Because a viewer can be a unique recipient every day, you should expect this to be higher than <i>Unique Impressions</i>. This number is received from Braze and is based on the `user_id`.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Unsubscribers or Unsub

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><i>Unsubscribers</i> or <i>Unsub</i>: Count</li>
        <li><i>Unsubscribers %</i> or <i>Unsub Rate</i>: (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

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