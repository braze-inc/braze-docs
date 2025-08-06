{% if include.metric == "AMP Clicks" %}
<i>AMP Clicks</i> is the total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and AMP HTML versions of the email.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP Opens</i> is the total count for opens in your AMP HTML email and AMP HTML versions of the email.
{% endif %}

{% if include.metric == "Audience" %}
<i>Audience</i> is the percentage of users who received a particular message. This number is received from Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> is the total number of messages that were unsuccessfully delivered to the intended recipients. 
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>Estimated Real Opens</i> is an estimate of how many unique opens there would be if machine opens did not exist, and is the result of a proprietary Braze statistical model.
{% endif %}

{% if include.metric == "Help" %}
<i>Help</i> is when a user replied to your message with a <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">HELP keyword</a> and was dispatched a HELP auto-response. 
{% endif %}

{% if include.metric == "Hard Bounce" %}
A <i>Hard Bounce</i> is when an email fails to deliver to the recipient due to a permanent delivery error. A hard bounce might occur because the domain name doesn't exist or because the recipient is unknown. 
{% endif %}

{% if include.metric == "Soft Bounce" %}
A <i>Soft Bounce</i> is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid. A soft bounce might occur because the recipient's inbox is full, the server was down, or the message was too large for the recipient's inbox.
{% endif %}

{% if include.metric == "Deferral" %}
A <i>Deferral</i> is when an email was not immediately delivered, but Braze retries the email for up to 72 hours after this temporary delivery failure to maximize the chances of successful delivery before attempts for that specific campaign are stopped.
{% endif %}

{% if include.metric == "Body Click" %}
Push Story Notifications record a <i>Body Click</i> when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> occur when a user clicks on a message that doesn't have buttons (Button 1, Button 2) and was created with the traditional editor, and when a message created with the HTML editor or drag-and-drop editor uses <code>brazeBridge.logClick()</code> with no arguments.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button 1 Clicks</i> is the total number of clicks on Button 1 of the message.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button 2 Clicks</i> is the total number of clicks on Button 2 of the message.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Choices Submitted</i> is the total number of choices selected when the user clicks the submit button on the survey question page of a <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>simple survey</a>.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>Click-to-Open Rate</i> is the percentage of opened emails that have been clicked by a single user or machine at least once, and is only available in the <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Close Message</i> is the total number of clicks on the close button of the message. This only exists for in-app messages created in the drag-and-drop editor, not the traditional editor.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Confirmed Deliveries</i> are when the carrier has confirmed the message was delivered to the target phone number.
{% endif %}

{% if include.metric == "Confidence" %}
<i>Confidence</i> is the percentage of confidence that a certain variant of a message is outperforming the control group.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Confirmation Page Button</i> is the total clicks on the call to action button on the confirmation page of a <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>simple survey</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Confirmation Page Dismissals</i> is the total clicks on the close (x) button on the confirmation page of a <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>simple survey</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>Conversion Rate</i> is the percentage of times a defined event occurred compared to all recipients of a message. This defined event is determined when you build the campaign.
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>Conversion Window</i> is the number of days after receiving the message during which user actions are tracked and attributed to a conversion event. Conversions that occur after this window are not attributed to the conversion event.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Conversions (B, C, D)</i> are additional conversion events added after the primary conversion event. This is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign.
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>Total Conversions</i> is the total number of times a user completes a specific conversion event after viewing an in-app message campaign.
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

{% if include.metric == "Delivery Failures RCS" %}
<i>Delivery Failures</i> are when the RCS couldn't be sent because of queues overflowing (sending RCS at a rate higher than your RCS-verified sender can handle).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
The <i>Failed Delivery Rate</i> is the percentage of sends that failed because the message could not be sent. This can happen for various reasons, including queue overflows, account suspensions, and media errors in the case of MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direct Opens</i> is the total number of users who opened your app or website by directly pressing the notification.
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

{% if include.metric == "Lifetime Revenue" %}
<i>Lifetime Revenue</i> is the total <code>PurchaseEvents</code> price value (in USD) received since inception.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>Lifetime Value Per User</i> is the <i>Lifetime revenue</i> divided by your total <i>Users</i> (located on your home page).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>Average Daily Revenue</i> is the average of the sum of the campaign and Canvas revenue for a given day.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Daily Purchases</i> is the average of the total unique <code>PurchaseEvents</code> over the time period.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>Daily Revenue Per User</i> is the average daily revenue per daily active user. 
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Machine Opens</i> includes the proportion of "opens" that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. For example, if a user opens an email using the Mail app on an Apple device, this will be logged as a <i>Machine Opens</i>.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Other Opens</i> includes emails that haven't been identified as <i>Machine Opens</i>. For example, when a user opens an email on another platform (such as Gmail app on a phone, Gmail on desktop browser), this will be logged as an <i>Other Opens</i>.
{% endif %}

{% if include.metric == "Opens" %}
<i>Opens</i> are instances including both <i>Direct Opens</i> and <i>Influenced Opens</i> in which the Braze SDK has determined, using a proprietary algorithm, that a push notification has caused a user to open the app.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>Opt-Out</i> is when a user replied to your message with an <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">opt-out keyword</a> and was unsubscribed from your SMS or RCS program. 
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retry</i> is the number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the email service provider (ESP). The ESP will retry delivery until a timeout period is reached (typically after 72 hours).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Primary Conversions (A)</i> or <i>Primary Conversion Event</i> is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign.
{% endif %}

{% if include.metric == "Reads" %}
<i>Reads</i> is when the user reads the message. The user’s read receipts must be “On” for Braze to track reads.
{% endif %}

{% if include.metric == "Read Rate" %}
<i>Read Rate</i> is the percentage of sends that resulted in a read. This is only given for users who have read receipts turned on.
{% endif %}

{% if include.metric == "Received" %}
<i>Received</i> is defined differently per channel, and can be when users view the message, users perform a defined trigger action, or the message is sent to the message provider.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Rejections</i> are when the SMS or RCS has been rejected by the carrier. This can happen for several reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, and similar. 
{% endif %}

{% if include.metric == "Revenue" %}
<i>Revenue</i> is the total revenue in dollars from campaign recipients within the set <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>primary conversion window</a>.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Messages Sent</i> is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.
{% endif %}

{% if include.metric == "Sent" %}
<i>Sent</i> is every time a campaign or Canvas step has been launched or triggered, and an SMS or RCS has been sent from Braze. It's possible that the SMS or RCS didn't reach a user's device due to errors.
{% endif %}

{% if include.metric == "Sends" %}
<i>Sends</i> is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Sends to Carrier</i> is deprecated, but will continue to be supported for users that already have it. It's the sum of <i>Confirmed Deliveries</i>, <i>Rejections</i>, and <i>Sends</i> where delivery or rejection wasn’t confirmed by the carrier. This includes instances where carriers don’t provide delivery or rejected confirmation, as some carriers don’t provide this confirmation or can’t do so at the time of send.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>Sends to Carrier Rate</i> is the percentage of total messages sent that were classified as <i>Sends to Carrier</i>. This includes instances where carriers don’t provide delivery or reject confirmation, as some carriers don’t provide this confirmation or can’t do so at the time of sending. This metric is deprecated but will continue to be supported for users who already have it.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> is the total number of emails delivered that were marked as "spam" by the recipient. While Braze doesn't change the subscription state of these users, these users will be automatically excluded in future emails, unless you're sending a transactional email, which is configured to "send to all users including unsubscribe".
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Survey Page Dismissals</i> is the total clicks on the close (x) button on the survey question page of a <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>simple survey</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Survey Submissions</i> is the total clicks on the submit button of a <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>simple survey</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Total Clicks</i> is the number of unique recipients who clicked on a link in the delivered message.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Total Dismissals</i> is the number of times Content Cards from a campaign have been dismissed. 
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Total Impressions</i> is the number of times the message has been loaded and appears on a user's screen, regardless of prior interaction (for example, if a user is shown a message twice, they will be counted twice).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Total Opens</i> is the total number of messages that were opened.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Total Revenue</i> is the total revenue in dollars from campaign recipients within the set primary conversion window.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Unique Clicks</i>  is the distinct number of recipients who have clicked a link within a message at least once and is measured by <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Unique Dismissals</i> is the number of unique recipients who dismissed a Content Card from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Unique Impressions</i> is the total number of users who received and viewed a message from a given campaign.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Unique Recipients</i> is the number of unique daily recipients, or users who received a new message in a day. For this count to increment for a user more than once, the user must receive a new message on a different day.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opens</i> is the total number of delivered messages that have been opened by a single user at least once and are tracked over a seven-day period.
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
