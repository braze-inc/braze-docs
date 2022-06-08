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

# Double opt-in process

You might find that some users who might send a text to your short or long code, won't yet be opted-in to your SMS subscription group. Regulations require that you obtain a user’s explicit consent before you send them any promotional or informational messaging. We highly recommend implementing a double opt-in to ensure compliance. 

![][IMAGE1]{: style="float:right;max-width:30%;margin-left:15px;"}
We suggest setting a triggered entry in Canvas whenever there's an incoming event `sms_response_subscriptionGroupName_custom`. Refer to [Custom keyword messaging handling][1] for more information.

## Step 1: Create a webhook

We first suggest creating a webhook campaign that makes a request to the [subscription/status/set endpoint][SSSendpoint] to subscribe the user to that SMS subscription group.

## Step 2: Send an SMS campaign

Next, we recommend sending an SMS campaign a few seconds later, with clear call-to-actions along the lines of:

![SMS message with the text "Braze: Thanks for your interest in Deal Texts! Expect three messages a month! Reply YES to join, STOP to stop, HELP for help. Message and data rates may apply."][IMAGE]{: style="border: 0"}

[SSSendpoint]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %}
[IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/custom_keyword_handling#custom-keyword-messaging-handling
