---
nav_title: Email Analytics Glossary
article_title: Email Analytics Glossary
layout: report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "This glossary includes the terms you will find in the analytics section of your email campaign or Canvas, post-launch. This glossary does not include Currents metrics."
glossary_top_text: "These are terms you'll find in the analytics section of your email campaign or Canvas, post-launch. Search for the metrics you need in this glossary. <br><br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

### Variation

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Calculation: Count</span>

### Emailable

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Calculation: Count</span>

### Audience %

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Calculation: (Number of Recipients in Variant) / (Unique Recipients)</span>

### Unique Recipients

{% multi_lang_include metrics.md metric='Unique Recipients' %} This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

### Sends or Messages Sent

{% multi_lang_include metrics.md metric='Sends or Messages Sent' %}  This metric is provided by Braze.

<span class="calculation-line">Calculation: Count</span>

### Deliveries

{% multi_lang_include metrics.md metric='Deliveries' %} For emails, *Deliveries* is the total number of messages (Sends) successfully sent to and received by emailable parties.

<span class="calculation-line">Calculation: (Sends) - (Bounces) </span>

### Deliveries %

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calculation: (Sends - Bounces) / (Sends) </span>

### Bounces

{% multi_lang_include metrics.md metric='Bounces' %} 

For email, *Bounce %* or *Bounce Rate* is the percentage of messages that were unsuccessfully sent or designated as "returned" or "not received" from send services used or not received by the intended emailable users.

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b>Bounces:</b> Count</li>
        <li><b>Bounce % or Bounce Rate %:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

  

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

---
