---
nav_title: Managing Email Subscriptions
page_order: 7

page_type: reference
description: "This article covers best practices for managing email subscriptions, such as unsubscribed, invalid, or duplicate emails."
channel: email
no_index: true
---
   
# Managing Email Subscriptions

Make sure you are familiar with the tools that Braze provides for [managing users' email subscriptions and targeting campaigns at users with particular subscription states][22]. These tools are critical for compliance with [anti-spam laws][23].

## Unsubscribed Email Addresses

Braze will automatically unsubscribe any user that either manually unsubscribes from your email through a custom footer or marks an email as spam. These users won't be targeted by future emails. To read more about how to set up your custom footer, visit this [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

If a user unsubscribes and later changes their email, their new email will also be unsubscribed. In other words, once an external user ID is associated with an unsubscribe, future email addresses for that user ID will also be unsubscribed.

## Bounces & Invalid Emails

If an email address hard bounces (due to the fact that the email is invalid or doesn't exist) then we will mark the user's email address as invalid and will not attempt to send further emails to that email address. If that user changes their email address, we will resume sending emails to them, as their new email may be valid. Soft Bounces (inbox full, etc) are automatically retried for 72 hours.

## Duplicate Emails

Braze automatically checks for and removes duplicate email addresses when an email campaign is sent. This way an email is only sent once and is "deduped" which ensures that it doesn't hit the same email multiple times even if multiple user profiles share a common address. Because deduplication occurs when targeted users are included in the same dispatch, triggered campaigns (excluding API-triggered campaigns, see below) may result in multiple sends to the same email address (even within a time period where users could be excluded due to reeligibility) if differing users with matching emails log the trigger event at different times. 

{% alert important %}
If you send an API campaign through an API call (excluding API-triggered campaigns), and multiple users are specified in the segment audience with the same email address, we will send it to that address as many times are listed in the call. This is because we assume that API calls are purposefully constructed. 
<br><br>
__API-Triggered Campaigns__<br>
Please note that API-triggered campaigns will dedupe or send duplicates __depending on where the audience is defined__. <br>- __Deduping__ will occur if there are duplicate emails in a target segment or duplicate emails due to duplicate IDs within the [recipient field]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) of an API-triggered call. <br>- __Duplicate emails__ will occur if you directly target separate user IDs within the [recipient field]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) of an API-triggered call. 
{% endalert %}

[22]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
