---
nav_title: Email Analytics Glossary
article_title: Email Analytics Glossary 
page_order: 20
layout: glossary_page
glossary_top_header: "Email Analytics Glossary"
glossary_top_text: "These are terms you'll find in the analytics section of your email campaign or Canvas, post-launch. Search for the metrics you need in this glossary. <br><br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

description: "This glossary includes the terms you will find in the analytics section of your email campaign or Canvas, post-launch. This glossary does not include Currents metrics."
channel:
  - email

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
    description: The total number of messages sent in an email campaign. This number is received from Braze.
    calculation: Count
  - name: "Deliveries"
    description: The total number of messages (Sends) successfully sent to and received by emailable parties.
    calculation: Sends - Bounces
  - name: "Deliveries %"
    description: The total number of messages (Sends) successfully sent to and received by emailable parties.
    calculation: (Sends - Bounces) / (Sends)
  - name: "Bounces"
    description: The total number of messages that were unsuccessfully sent or designated as 'returned' or 'not received' from send services used or not received by the intended emailable users. This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched. <br><br> <b>Hard Bounces</b>&#58; A hard bounce is an email message that has been returned to the sender because the recipient's address is invalid. A hard bounce might occur because the domain name doesn't exist or because the recipient is unknown. If an email has received a hard bounce, we will stop any future requests to this email address. <br><br><b>Soft Bounces</b>&#58; A soft bounce is an email message that gets as far as the recipient's mail server but is bounced back undelivered before it gets to the recipient. A soft bounce might occur because the recipient's inbox is full, the server was down, or the message was too large for the receipient's inbox. If an email has received a soft bounce, we will usually retry within a 72 hour period, but the number of retry attempts varies from receiver to receiver. <br><br> You can also track hard and soft bounces in the <a href='/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab'>Message Activity Log</a>. <br><br><i> An email bounce for customers using Sendgrid consists of hard bounces, spam, and emails sent to invalid addresses. </i>
    calculation: Count
  - name: "Bounces % or Bounce Rate"
    description: The percentage of messages that were unsuccessfully sent or designated as 'returned' or 'not received' from send services used or not received by the intended emailable users. This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched. <br> <i> An email bounce for customers using Sendgrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`). </i>
    calculation: Bounces / Sends
  - name: "Spam"
    description: The total number of emails delivered that were marked as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won’t be targeted by future emails.
    calculation: (Marked as Spam) / (Sends)
  - name: "Spam % or Spam Rate"
    description: The percentage of emails delivered that were marked or otherwise designated as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won’t be targeted by future emails.
    calculation: (Marked as Spam) / (Sends)
  - name: "Unique Opens"
    description: The total number of delivered emails that have been opened by a single user or machine at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Opens) / (Deliveries)
  - name: "Unique Opens % or Unique Open Rate"
    description: The percentage of delivered emails that have been opened by a single user at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Opens) / (Deliveries)
  - name: "Unique Clicks"
    description: Distinct number of recipients who have clicked within a message at least once. This is tracked over a 7 day period for Email.
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
  - name: "Primary Conversions (A) or Primary Conversion Event"
    description: The percentage of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign.
    calculation: "Primary Conversions / Unique Recipients"
  - name: "Confidence"
    description: The percentage of confidence that a certain variant of a message is outperforming the control group.
  - name: "Machine Opens"
    description: Includes the proportion of “opens” that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. For example, if a user opens an email using the Mail app on an Apple device, this will be logged as a "Machine Opens". This metric is tracked starting November 11, 2021 for Sendgrid and December 2, 2021 for Sparkpost.
    calculation: Count
  - name: "Other Opens"
    description: Includes emails that haven't been identified as "Machine opens". For example, when a user opens an email on another platform (i.e., Gmail app on a phone, Gmail on desktop browser), this will be logged as an "Other opens". Note that a user can also open an email (i.e., the open counts toward "Other opens") before a "Machine open" count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated towards “Other Opens” and only once towards “Unique Opens”.
    calculation: Count
  - name: "Click to Open Rate"
    description: The percentage of unique emails opened that have been clicked at least once.
    calculation: Unique Clicks / Unique Opens

---
