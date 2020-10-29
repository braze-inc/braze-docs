---
nav_title: Managing Email Subscriptions
page_order: 7
---
   
# Managing Email Subscriptions

Make sure you are familiar with the tools that Braze provides for [managing users' email subscriptions and targeting campaigns at users with particular subscription states][22]. These tools are critical for compliance with [anti-spam laws][23].

## Unsubscribed Email Addresses

Braze will automatically unsubscribe any user that either manually unsubscribes from your email or marks an email as spam. These users won't be targeted by future emails.

If a user unsubscribes and later changes their email, their new email will also be unsubscribed. In other words, once an external user ID is associated with an unsubscribe, future email addresses for that user ID will also be unsubscribed.

## Bounces & Invalid Emails

If an email address hard bounces (due to the fact that the email is invalid or doesn't exist) then we will mark the user's email address as invalid and will not attempt to send further emails to that email address. If that user changes their email address, we will resume sending emails to them, as their new email may be valid. Soft Bounces (inbox full, etc) are automatically retried for 72 hours.

## Duplicate Emails

Braze automatically checks for and removes duplicate email addresses when an email campaign is sent. Even if multiple user profiles share a common email address, that address will not receive multiple messages.

{% alert important %}
This only applies for campaigns triggered from our UI. If you send a campaign through an API call, and multiple users are specified in the segment audience with the same email address, we will send it to that address as many times as are listed in the call. This is because we assume that API calls are purposefully constructed.
{% endalert %}

[22]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
