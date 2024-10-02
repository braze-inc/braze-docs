{% if include.metric == "AMP Clicks" %}
<i>AMP Clicks</i> is the total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and <span style="white-space: nowrap">AMP HTML</span> versions of the email.
{% endif %}

{% if include.metric == "Audience" %}
<i>Audience</i> is the percentage of users who received a particular message. This number is received from Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> is the total number of messages that were unsuccessfully delivered to the intended recipients. 
{% endif %}

{% if include.metric == "Hard Bounce" %}
A <i>Hard Bounce</i> is when an email fails to deliver to the recipient due to a permanent delivery error. 
{% endif %}

{% if include.metric == "Soft Bounce" %}
A <i>Soft Bounce</i> is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid.
{% endif %}

{% if include.metric == "Body Click" %}
Push Story Notifications record a <i>Body Click</i> when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> occur when someone clicks on any of the following in-app message types: slide-up, modal, or fullscreen that has no buttons.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button 1 Clicks</i> is the total number of clicks on Button 1 of the message.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button 2 Clicks</i> is the total number of clicks on Button 2 of the message.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Choices Submitted</i> is the total number of choices selected when the user clicks the submit button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>Click-to-Open Rate</i> is the percentage of delivered emails that have been opened by a single user or machine at least once, and is only available in the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Confirmed Deliveries</i> are when the carrier has confirmed the SMS was delivered to the target phone number. As a Braze customer, deliveries are charged toward your SMS allotment. 
{% endif %}

{% if include.metric == "Confidence" %}
<i>Confidence</i> is the percentage of confidence that a certain variant of a message is outperforming the control group.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Confirmation Page Button</i> is the total clicks on the call to action button on the confirmation page of a [simple survey]({{site.baseurl}}/docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Confirmation Page Dismissals</i> is the total clicks on the close (x) button on the confirmation page of a [simple survey]({{site.baseurl}}/docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey).
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>Conversion Rate</i> is the percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined when you build the campaign.
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>Conversion Window</i> is the number of days after receiving the message during which user actions are tracked and attributed to a conversion event. Conversions that occur after this window are not attributed to the conversion event.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Conversions (B, C, D)</i> are additional conversion events added after the primary conversion event. The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Deliveries</i> is the total number of message requests that are accepted by the receiving server. This doesn’t mean the message was delivered to a device, only that the message was accepted by the server. 
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Deliveries %</i> is the percentage of total number of messages (Sends) successfully sent to and received by emailable parties.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Delivery Failures</i> are when the SMS couldn't be sent because of queues overflowing (sending SMS at a rate higher than your long or short codes can handle).
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direct Opens</i> is the total number (and percentage) of push notifications that were directly opened from that push.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Emailable</i> is the total number of users who have an email address on record and have explicitly opted in or subscribed.
{% endif %}

{% if include.metric == "Errors" %}
<i>Errors</i> is the number of errors returned by webhook events (incremented during the sending process).
{% endif %}

{% if include.metric == "Failures" %}
<i>Failures</i> are when the WhatsApp message couldn’t send because the internet service provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Influenced Opens</i> is the total number (and percentage) of users who opened the app after the push notification was sent, without directly opening the push.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Machine Opens</i> includes the proportion of "opens" that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. For example, if a user opens an email using the Mail app on an Apple device, this will be logged as a Machine Opens.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Other Opens</i> includes emails that haven't been identified as Machine Opens. For example, when a user opens an email on another platform (such as Gmail app on a phone, Gmail on desktop browser), this will be logged as an Other Opens.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retry</i> is the number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the email service provider (ESP). The ESP will retry delivery until a timeout period is reached (typically after 72 hours).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Pending Conversions (A)</i> or <i>Primary Conversion Event</i> is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign.
{% endif %}

{% if include.metric == "Reads" %}
<i>Reads</i> is when the user reads the WhatsApp message. The user’s read receipts must be “On” for Braze to track reads.
{% endif %}

{% if include.metric == "Received" %}
<i>Received</i> is defined differently per channel, and can be when users view the message, users perform a defined trigger action, or the message is sent to the message provider.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Rejections</i> are when the SMS has been rejected by the carrier. This can happen for several reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, and similar. 
{% endif %}

{% if include.metric == "Revenue" %}
<i>Revenue</i> is the total revenue in dollars from campaign recipients within the set [primary conversion window]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events).
{% endif %}

{% if include.metric == "Sends or Messages Sent" %}
<i>Sends</i> or <i>Messages Sent</i> is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
{% alert note %}
<i>Sends to Carrier</i> is deprecated, but will continue to be supported for users that already have it.
{% endalert %}

<i>Sends to Carrier</i> is the sum of Confirmed Deliveries, Rejections, and Sends where delivery or rejection wasn’t confirmed by the carrier. This includes instances where carriers don’t provide delivery or rejected confirmation, as some carriers don’t provide this confirmation or can’t do so at the time of send.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> is the total number of emails delivered that were marked as "spam." Braze automatically unsubscribes users that marked an email as spam, and those users won't be targeted by future emails.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Survey Page Dismissals</i> is the total clicks on the close (x) button on the survey question page of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Survey Submissions</i> is the total clicks on the submit button of a [simple survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/).
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Total Clicks</i> is the total number (and percentage) of users who clicked within the delivered email, card, or message. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Total Dismissals</i> is the number of times Content Cards from a campaign have been dismissed. If a user dismisses a message twice, they will be only counted once.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Total Impressions</i> is the number of times the in-app message has been viewed (if a user is shown a message twice, they will be counted twice). This number is a sum of the number of impression events that Braze receives from the SDKs.
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Total Opens</i> is the total number of messages that were opened. For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Total Revenue</i> is the total revenue in dollars from campaign recipients within the set primary conversion window. This metric is only available on Campaign Comparison Reports through the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/).
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Unique Clicks</i> is the distinct number of recipients who have clicked within a message at least once. This is tracked over a seven-day period for email. This includes clicks on Braze-provided unsubscribe links.

For LINE, this is tracked after a minimum threshold of 20 messages per day has been reached.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Unique Dismissals</i> is the number of users who have dismissed Content Cards from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.
{% endif %}

{% if include.metric == "Unique Impressions" %}
<i>Unique Impressions</i> is the total number of users who received and viewed a given in-app message or card in a day.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opens</i> is the total number of delivered emails that have been opened by a single user at least once and are tracked over a seven-day period.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Unique Recipients</i> is the number of unique daily recipients, or users who received a particular message in a day. This number is received from Braze.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i> or <i>Unsub</i> is the number of messages resulting in an unsubscription. Unsubscriptions occur when a user clicks on the Braze unsubscribe link.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Unsubscribes</i> is the number of recipients whose subscription state changed to unsubscribed as a result of clicking the Braze provided unsubscribe URL.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variation</i> is the number of variations of a campaign, differing as defined by the creator.
{% endif %}