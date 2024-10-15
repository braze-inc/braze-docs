---
nav_title: Email Analytics Glossary
article_title: Email Analytics Glossary
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "This glossary includes the terms you will find in the analytics section of your email campaign or Canvas, post-launch. This glossary does not include Currents metrics."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>
glossaries:
  - name: "Variation"
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
  - name: "Emailable"
    description: Users who have an email address on record and have explicitly opted in or subscribed.
    calculation: Count
  - name: "Audience %"
    description: Percentage of users who received a particular variant.
    calculation: Number of Recipients in Variant / Unique Recipients
  - name: "Unique Recipients"
    description: Unique Daily Recipients. The number of users who received a particular message in a day. This number is received from Braze.
    calculation: Count
  - name: "Sends or Messages Sent"
    description: The total number of messages sent in an email campaign. This number is received from Braze. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting.
    calculation: Count
  - name: "Deliveries"
    description: The total number of messages (Sends) successfully sent to and received by emailable recipients.
    calculation: Sends - Bounces
  - name: "Deliveries %"
    description: The total number of messages (Sends) successfully sent to and received by emailable parties.
    calculation: (Sends - Bounces) / (Sends)
  - name: "Bounces"
    description: The total number of messages that were unsuccessfully delivered to the intended recipients. This could occur because the email addresses were incorrect or deactivated. There are two types of <br>bounces:<br><br> -<b>Hard Bounces</b>&#58; A hard bounce is when an email fails to deliver to the recipient due to a permanent delivery error. A hard bounce might occur because the domain name doesn't exist or because the recipient is unknown. If an email receives a hard bounce, we will stop any future requests to this email address. <br><br>-<b>Soft Bounces</b>&#58; A soft bounce is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid. A soft bounce might occur because the recipient's inbox is full, the server was down, or the message was too large for the recipient's inbox. If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver. <br><br> You can view your hard and soft bounces in the <a href='/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab'>Message Activity Log</a>. <br><br><i> An email bounce for customers using SendGrid consists of hard bounces, spam, and emails sent to invalid addresses. </i>
    calculation: Count
  - name: "Bounces % or Bounce Rate"
    description: The percentage of messages that were hard bounced by the intended recipients. This could occur because the email address is invalid, does not exist, or is deactivated.
    calculation: Bounces / Sends
  - name: "Spam"
    description: The total number of emails delivered that were marked as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won't be targeted by future emails.
    calculation: (Marked as Spam) / (Sends)
  - name: "Spam % or Spam Rate"
    description: The percentage of emails delivered that were marked or otherwise designated as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won't be targeted by future emails.
    calculation: (Marked as Spam) / (Sends)
  - name: "Unique Opens"
    description: The total number of delivered emails that have been opened by a single user or machine at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Opens) / (Deliveries)
  - name: "Unique Opens % or Unique Open Rate"
    description: The percentage of delivered emails that have been opened by a single user at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Opens) / (Deliveries)
  - name: "Unique Clicks"
    description: Distinct number of recipients who have clicked within a message at least once. This is tracked over a 7 day period for Email and measured by <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>
    calculation: Count
  - name: "Unique Clicks % or Click Rate"
    description: Distinct number of recipients who have clicked within a message at least once. This is tracked over a 7 day period for Email.
    calculation: Unique Clicks / Deliveries
  - name: "Unsubscribers or Unsub"
    description: Number of messages resulting in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
    calculation: Count
  - name: "Unsubscribers % or Unsub Rate"
    description: Percentage of messages delivered which resulted in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
    calculation: Unsubscribes / Deliveries
  - name: "Revenue"
    description: The total revenue in dollars from campaign recipients within the set <a href='/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event'>primary conversion window</a>.
    calculation: Count
  - name: "Primary Conversions (A) or Primary Conversion Event"
    description: The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign.
    calculation: Count
  - name: "Primary Conversions (A) % or Primary Conversion Event Rate"
    description: The percentage of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign.
    calculation: "Primary Conversions / Unique Recipients"
  - name: "Confidence"
    description: The percentage of confidence that a certain variant of a message is outperforming the control group.
  - name: "Machine Opens"
    description: Includes the proportion of "opens" that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. For example, if a user opens an email using the Mail app on an Apple device, this will be logged as a <i>Machine Opens</i>. This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.
    calculation: Count
  - name: "Other Opens"
    description: Includes emails that haven't been identified as <i>Machine Opens</i> . For example, when a user opens an email on another platform (such as Gmail app on a phone, Gmail on desktop browser), this will be logged as an  <i>Other Opens</i>. Note that a user can also open an email (such as the open counts toward <i>Other Opens</i>) before a <i>Machine Opens</i> count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward <i>Other Opens</i> and only once toward <i>Unique Opens</i>.
    calculation: Count
  - name: "Click to Open Rate"
    description: The percentage of unique emails opened that have been clicked at least once.
    calculation: Unique Clicks / Unique Opens

{% api %}

### Variation

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Emailable

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Audience %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Calculation: (Number of Recipients in Variant) / (Unique Recipients)</span>

{% endapi %}

{% api %}

### Unique Recipients

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %}  This metric is provided by Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Messages Sent

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %}  This metric is provided by Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Deliveries

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} For emails, *Deliveries* is the total number of messages (Sends) successfully sent to and received by emailable parties.

<span class="calculation-line">Calculation: (Sends) - (Bounces) </span>

{% endapi %}

{% api %}

### Deliveries %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calculation: (Sends - Bounces) / (Sends) </span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

For email, *Bounce %* or *Bounce Rate* is the percentage of messages that were unsuccessfully sent or designated as "returned" or "not received" from send services used or not received by the intended emailable users.

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Bounces</i>:</b> Count</li>
        <li><b><i>Bounce %</i> or <i>Bounce Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Spam</i>:</b> Count</li>
        <li><b><i>Spam %</i> or <i>Spam Rate %</i>:</b> (Marked as Spam) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Unique Opens

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} For email, this is tracked over a 7 day period.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Count</li>
        <li><b><i>Unique Opens %</i> or <i>Unique Open Rate</i>:</b> (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Unique Clicks

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} This is tracked over a seven-day period for email and measured by <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. This includes clicks on Braze-provided unsubscribe links.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Clicks</i>:</b> Count</li>
        <li><b><i>Unique Clicks %</i> or <i>Click Rate</i>:</b> (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Unsubscribers or Unsub

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unsubscribers</i> or <i>Unsub</i>:</b> Count</li>
        <li><b><i>Unsubscribers %</i> or <i>Unsub Rate</i>:</b> (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Revenue

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Primary Conversions (A) or Primary Conversion Event

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} For email, push, and webhooks, we start tracking conversions after the initial send.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Primary Conversions (A)</i> or <i>Primary Conversion Event</i>:</b> Count</li>
        <li><b><i>Primary Conversions (A) %</i> or <i>Primary Conversion Event Rate</i>:</b> (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confidence

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Machine Opens
  
{% multi_lang_include metrics.md metric='Machine Opens' %} This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Other Opens

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Note that a user can also open an email (such as the open counts toward <i>Other Opens</i>) before a <i>Machine Opens</i> count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward <i>Other Opens</i> and only once toward <i>Unique Opens</i>.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Click-to-Open Rate

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calculation: (Unique Clicks) / (Unique Opens) (for Email)</span>

{% endapi %}