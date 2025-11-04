---
nav_title: Duplicate emails
article_title: Duplicate Emails
page_order: 7
page_type: reference
description: "This article covers best practices for managing duplicate emails."
channel: email

---

# Duplicate emails

> For duplicate emails, if one email unsubscribes, other profiles (up to 100 profiles) with that email address are updated to reflect the same subscription state. This applies for unsubscribes and other changes to subscription state, such as global email subscription state and individual subscription group statuses.

## Email subscription updates

Braze automatically checks for and removes duplicate email addresses when an email campaign is sent. This way an email is only sent once and is "deduped," which checks that it doesn't hit the same email multiple times even if multiple user profiles share a common address.

{% alert tip %}
Make sure you're familiar with the tools that Braze provides for [managing user email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) and targeting campaigns at users with particular subscription states. These tools are critical for compliance with [anti-spam laws]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

If users share an email address, updating one of these users will propagate the subscription changes across these users (up to 100 users).

## Message sending behavior

Because deduplication occurs when targeted users are included in the same dispatch, triggered campaigns (excluding API-triggered campaigns) and Canvases may result in multiple sends to the same email address (even within a time period where users could be excluded due to reeligibility) if differing users with matching emails log the trigger event at different times.

## Examples

For example, if user A and user B share the email `johndoe@example.com` but their profile is in a different time zone, when the campaign trigger event includes sending in a user's time zone, the email `johndoe@example.com` will receive two emails.

If you set or update the email address for User A to another email address that's shared by an existing User B, User A will inherit the subscription state that already exists from User B unless the **Resubscribe users when they update their email** setting is turned on.

{% alert important %}
If you send an API campaign through an API call (excluding API-triggered campaigns), and multiple users are specified in the segment audience with the same email address, we will send it to that address as many times are listed in the call. This is because we assume that API calls are purposefully constructed.
<br><br>
**API-triggered campaigns**<br>
Note that API-triggered campaigns will dedupe or send duplicates depending on where the audience is defined. <br>- Deduping may occur if there are duplicate emails in a target segment or duplicate emails due to duplicate IDs within the [recipient field]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) of an API-triggered call. <br>- Duplicate emails will occur if you directly target separate user IDs within the recipient field of an API-triggered call. 
{% endalert %}
