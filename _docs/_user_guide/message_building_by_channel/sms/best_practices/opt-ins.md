---
nav_title: "User Opt-Ins"
article_title: Best Practices for Collecting User SMS Opt-Ins
page_order: 7
description: "This reference article cover three best practices for collecting user opt-ins."
page_type: reference
channel:
  - SMS
  
---

# Collecting user opt-ins

The following article lists some common SMS opt-in methods.

## Option 1: Ask users to text your short or long code

Ask users to text "START", "UNSTOP", "YES", or a custom opt-in keyword to your number to automatically add them to your subscription group. On your website, mobile app, or even advertising, you can request users do this to opt-in, and you can offer an incentive if it's helpful.

## Option 2: Users opt-in via in-app message

If you would like users to opt-in to SMS from an in-app message, see the implementation steps below. We recommend testing this first in a staging app group. 

1. Launch an in-app or in-browser message campaign that requests a user's phone number, encouraging them to opt-in. When a user clicks submit, you will need to log a new custom event like `phone_number_captured`.<br><br>
2. Next, leverage Canvas to opt the user in officially and send a confirmation. Set the entry of the Canvas as action-based on the custom event `phone_number_captured` trigger which was logged from the in-app message above. You can also target users where "External user ID is not blank" and any other relevant attributes for the entry audience, as necessary. <br><br>
3. Add a webhook to the [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) endpoint as the first Canvas step. This puts the user's phone number into the subscription group to officially opt them in. <br>![][1]<br><br>
4. The second and final step of the Canvas is an SMS confirmation to the users, confirming their opt-in status.<br>![][2]

## Option 3: Sign-up flow

When a new user signs up or registers on the website or app, ask for their phone number and email. Include a checkbox to receive promotional emails and SMS. Once the user signs up, leverage the [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) endpoint:

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

[1]: {% image_buster /assets/img/sms/opt-in1.png %}
[2]: {% image_buster /assets/img/sms/opt-in2.png %}