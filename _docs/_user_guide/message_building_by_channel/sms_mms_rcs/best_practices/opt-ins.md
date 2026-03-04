---
nav_title: "Collecting user opt-ins"
article_title: Best Practices for Collecting User SMS Opt-Ins
page_order: 7
description: "This reference article cover three best practices for collecting user opt-ins."
page_type: reference
channel:
  - SMS
  
---

# Collecting user opt-ins

> The following article lists some common SMS opt-in methods.

## Option 1: Ask users to text your short or long code

Ask users to text "START", "UNSTOP", "YES", or a custom opt-in keyword to your number to automatically add them to your subscription group. On your website, mobile app, or even advertising, you can request users do this to opt-in, and you can offer an incentive if it's helpful.

## Option 2: Users opt-in via in-app message

To allow users to opt into SMS from an in-app message, use the [phone number capture form]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) provided by Braze to create a branded form that allows you to collect phone numbers and grow your SMS list.

![In-app message composer with a template for phone number capture.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recommends that you also use the [SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) feature. This feature automatically works with the in-app message phone number capture form, prompting users to confirm their intent after submitting their phone number via the form.

## Option 3: Sign-up flow

When a new user signs up or registers on the website or app, ask for their phone number and email. Include a checkbox to receive promotional emails and SMS. 

After the user signs up, do the following:

1. Use the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) to create the user and save their attributes.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to subscribe the user to SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
To enter users into the [SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) workflow when subscribing them through the REST API, set the `use_double_opt_in_logic` parameter to `true` in your request. If you omit this parameter, users are subscribed without receiving a double opt-in confirmation.

This parameter is supported by the following endpoints:
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}