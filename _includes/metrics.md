<!-- Format all definitions as standalone sentences or paragraphs. -->

{% if include.metric == "AMP Clicks" %}
*AMP Clicks* is the total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and AMP HTML versions of the email.
{% endif %}

{% if include.metric == "Audience" %}
*Audience* is the percentage of users who received a particular message. This number is received from Braze.
{% endif %}

{% if include.metric == "Bounces" %}
*Bounces* is the total number of unsuccessful messages. This could occur because there isn’t a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched. An email bounce for customers using SendGrid consists of hard bounces, spam, and emails sent to invalid addresses.
{% endif %}

{% if include.metric == "Body Click" %}
Push Story Notifications record a body click when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.
{% endif %}

{% if include.metric == "Body Clicks" %}
*Body Clicks* occur when someone clicks on any of the following in-app message types:

- Slide-up
- Modal
- Fullscreen that has no buttons
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
*Button 1 Clicks* is the total number of clicks on Button 1 of the message.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
*Button 2 Clicks* is the total number of clicks on Button 2 of the message.
{% endif %}

{% if include.metric == "Choices Submitted" %}
*Choices Submitted* is the total number of choices selected when the user clicks the submit button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
*Click-to-Open Rate* is the percentage of opened emails that were clicked. This metric is only available in the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
*Confirmed Deliveries* are when the carrier has confirmed the SMS was delivered to the target phone number. As a Braze customer, deliveries are charged toward your SMS allotment. 
{% endif %}

{% if include.metric == "Audience %" %}
*Audience %* is the percentage of users who received a particular variant.
{% endif %}

{% if include.metric == "Bounces % or Bounce Rate" %}
*Bounces %* or *Bounce Rate* is the percentage of messages that were unsuccessfully sent or designated as "returned" or "not received" from send services used or not received by the intended emailable users. This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched.

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).
{% endif %}

{% if include.metric == "Click to Open Rate" %}
*Click to Open Rate* is the percentage of unique emails opened that have been clicked at least once.
{% endif %}

{% if include.metric == "Confidence" %}
*Confidence* is the percentage of confidence that a certain variant of a message is outperforming the control group.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
*Confirmation Page Button* is the total clicks on the call to action button on the confirmation page of a [simple survey]({{site.baseurl}}/docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
*Confirmation Page Dismissals* is the total clicks on the close (x) button on the confirmation page of a [simple survey]({{site.baseurl}}/docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Conversion Rate" %}
*Conversion Rate* is the percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined when you build the campaign.
{% endif %}

{% if include.metric == "Conversion Window" %}
*Conversion Window* is the number of days after receiving the message during which user actions are tracked and attributed to a conversion event. Conversions that occur after this window are not attributed to the conversion event.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
*Conversions (B, C, D)* are additional conversion events added after the primary conversion event. The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign.

This defined event is determined by the marketer when building the campaign. For email, push, and webhooks, we start tracking conversions after the initial send. For Content Cards and in-app messages, this count begins when they view a Content Card or message for the first time.
{% endif %}

{% if include.metric == "Deliveries general" %}
*Deliveries* is the total number of message requests that are accepted by the receiving server. This doesn’t mean the message was delivered to a device, only that the message was accepted by the server.
{% endif %}

{% if include.metric == "Deliveries email" %}
*Deliveries* for emails is the total number of messages (Sends) successfully sent to and received by emailable parties.
{% endif %}

{% if include.metric == "Deliveries %" %}
*Deliveries %* is the percentage of total number of messages (Sends) successfully sent to and received by emailable parties.
{% endif %}

{% if include.metric == "Delivery Failures" %}
*Delivery Failures* are when the SMS couldn't be sent because of queues overflowing (sending SMS at a rate higher than your long or short codes can handle).
{% endif %}

{% if include.metric == "Direct Opens" %}
*Direct Opens* is the total number (and percentage) of push notifications that were directly opened from that push.
{% endif %}

{% if include.metric == "Emailable" %}
*Emailable* is the total number of users who have an email address on record and have explicitly opted in or subscribed.
{% endif %}

{% if include.metric == "Errors" %}
*Errors* is the number of errors returned by webhook events (incremented during the sending process).
{% endif %}

{% if include.metric == "Failures" %}
*Failures* are when the WhatsApp message couldn’t send because the internet service provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.
{% endif %}

{% if include.metric == "Influenced Opens" %}
*Influenced Opens* is the total number (and percentage) of users who opened the app after the push notification was sent, without directly opening the push.
{% endif %}

{% if include.metric == "Machine Opens" %}
*Machine Opens* includes the proportion of "opens" that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. For example, if a user opens an email using the Mail app on an Apple device, this will be logged as a Machine Opens. This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.
{% endif %}

{% if include.metric == "Other Opens" %}
*Other Opens* includes emails that haven't been identified as Machine Opens. For example, when a user opens an email on another platform (such as Gmail app on a phone, Gmail on desktop browser), this will be logged as an Other Opens. Note that a user can also open an email (such as the open counts toward Other Opens) before a Machine Opens count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward Other Opens and only once toward Unique Opens.
{% endif %}

{% if include.metric == "Pending Retry" %}
*Pending Retry* is the number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the email service provider (ESP). The ESP will retry delivery until a timeout period is reached (typically after 72 hours).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
*Pending Conversions (A)* or *Primary Conversion Event* is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by the marketer when building the campaign.

For email, push, and webhooks, we start tracking conversions after the initial send. For Content Cards and in-app messages, this count begins when they view a Content Card or message for the first time.
{% endif %}

{% if include.metric == "Reads" %}
*Reads* is when the user reads the WhatsApp message. The user’s read receipts must be “On” for Braze to track reads.
{% endif %}

{% if include.metric == "Received" %}
- Content Cards: Received when users view the card in the app.
- Push: Received when messages are sent from the Braze server to the push provider.
- Email: Received when messages are sent from the Braze server to the email service provider.
- SMS/MMS: “Delivered” after the SMS provider receives confirmation from the upstream carrier and destination device.
- In-app message: Received at the time of display based on the trigger action defined.
- WhatsApp: Received at the time of display based on the trigger action defined.
{% endif %}

{% if include.metric == "Rejections" %}
*Rejections* are when the SMS has been rejected by the carrier. This can happen for several reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, and similar. As a Braze customer, rejections are charged toward your SMS allotment.
{% endif %}

{% if include.metric == "Revenue" %}
*Revenue* is the total revenue in dollars from campaign recipients within the set [primary conversion window]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events).
{% endif %}

{% if include.metric == "Sends or Messages Sent" %}
*Sends* or *Messages Sent* is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent. This metric is provided by Braze.

{% alert tip %}
For Content Cards, this metric is calculated differently depending on what you selected for [Card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).
{% endalert %}
{% endif %}

{% if include.metric == "Sends to Carrier" %}
{% alert note %}
*Sends to Carrier* is deprecated, but will continue to be supported for users that already have it.
{% endalert %}

*Sends to Carrier* is the sum of Confirmed Deliveries, Rejections, and Sends where delivery or rejection wasn’t confirmed by the carrier. This includes instances where carriers don’t provide delivery or rejected confirmation, as some carriers don’t provide this confirmation or can’t do so at the time of send.
{% endif %}

{% if include.metric == "Spam" %}
*Spam* is the total number of emails delivered that were marked as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won't be targeted by future emails.
{% endif %}

{% if include.metric == "Spam % or Spam Rate" %}
*Spam %* or *Spam Rate* is the percentage of emails delivered that were marked or otherwise designated as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won't be targeted by future emails.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
*Survey Page Dismissals* is the total clicks on the close (x) button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).
{% endif %}

{% if include.metric == "Survey Submissions" %}
*Survey Submissions* is the total clicks on the submit button of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).
{% endif %}

{% if include.metric == "Total Clicks" %}
*Total Clicks* is the total number (and percentage) of users who clicked within the delivered email, card, or message. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Total Dismissals" %}
*Total Dismissals* is the number of times Content Cards from a campaign have been dismissed. If a user dismisses a message twice, they will be only counted once.
{% endif %}

{% if include.metric == "Total Impressions" %}
*Total Impressions* is the number of times the in-app message has been viewed (if a user is shown a message twice, they will be counted twice). This number is a sum of the number of impression events that Braze receives from the SDKs.
{% endif %}

{% if include.metric == "Total Opens" %}
*Total Opens* is the total number of messages that were opened. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Total Revenue" %}
*Total Revenue* is the total revenue in dollars from campaign recipients within the set primary conversion window. This metric is only available on Campaign Comparison Reports through the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).
{% endif %}

{% if include.metric == "Unique Clicks" %}
*Unique Clicks* is the distinct number of recipients who have clicked within a message at least once. This is tracked over a seven-day period for email. This includes clicks on Braze-provided unsubscribe links.

For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Unique Clicks % or Click Rate" %}
*Unique Clicks %* or *Click Rate* is the distinct number of recipients who have clicked within a message at least once. This is tracked over a seven day period for email.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
*Unique Dismissals* is the number of users who have dismissed Content Cards from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.
{% endif %}

{% if include.metric == "Unique Impressions" %}
*Unique Impressions* is the total number of users who received and viewed a given in-app message or card in a day. For in-app messages, unique impressions can be incremented again after 24 hours if re-eligibility is on and a user performs the trigger action. Conversely, the count should not increment the second time a user views a Content Card. This number is received from Braze.
{% endif %}

{% if include.metric == "Unique Opens" %}
*Unique Opens* is the total number of delivered emails that have been opened by a single user at least once and are tracked over a seven-day period. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Unique Opens % or Unique Open Rate" %}
*Unique Opens %* or *Unique Open Rate* is the percentage of delivered emails that have been opened by a single user at least once. This is tracked over a seven-day period.
{% endif %}

{% if include.metric == "Unique Recipients" %}
*Unique Recipients* is the number of unique daily recipients, or users who received a particular message in a day. This number is received from Braze.
{% endif %}

{% if include.metric == "Unsubscribers % or Unsub Rate" %}
*Unsubscribers %* or *Unsub Rate* is the percentage of messages delivered which resulted in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
*Unsubscribers* or *Unsub* is the number of messages resulting in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
{% endif %}

{% if include.metric == "Unsubscribes" %}
*Unsubscribes* is the number of recipients whose subscription state changed to unsubscribed as a result of clicking the Braze provided unsubscribe URL.
{% endif %}

{% if include.metric == "Variation" %}
*Variation* is the number of variations of a campaign, differing as defined by the creator.
{% endif %}


