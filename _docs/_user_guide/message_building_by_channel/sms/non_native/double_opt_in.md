---
nav_title: Double Opt-In Process
article_title: Non-Native SMS Double Opt-In Process
page_order: 5
description: "This reference article covers how Braze processes certain keywords for non-native SMS users, as well as best practices when creating an SMS webhook campaign."
page_type: reference
channel:
  - SMS
  - webhooks

---

# Double Opt-In Process

You might find that some users who might send a text to your short/long code, won't yet be opted-in to your SMS Subscription Group. Regulations require that you obtain a user’s explicit consent before you send them any promotional or informational messaging. We highly recommend implementing a double opt-in to ensure compliance. 

![picture][IMAGE1]{: style="float:right;max-width:30%;margin-left:15px;"}
We suggest setting a __triggered entry__ in Canvas whenever there's an incoming event `sms_response_subscriptionGroupName_custom`.

## Step 1: Create Webhook

We first suggest creating a webhook campaign that makes a request to the [subscription/status/set endpoint][SSSendpoint] to subscribe the user to that SMS subscription group.

## Step 2: Send an SMS campaign
Next, we recommend sending an SMS campaign a few seconds later, with clear call-to-actions along the lines of:

![picture][IMAGE]{: style="border: 0"}

[SSSendpoint]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %}
[IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}
