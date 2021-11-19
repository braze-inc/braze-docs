---
nav_title: Custom Keyword Handling
article_title: Non-Native SMS Custom Keyword Handling
page_order: 1.5
description: "This reference article covers how Braze processes custom keywords for non-native SMS users."
page_type: reference
channel:
  - SMS

---

# Two-way messaging (custom keyword responses)

Two-way messaging uses short codes and keywords to deliver text messages to mobile users. It requires end users to send a keyword to Braze to which that user will receive an automatic reply. Applied correctly, two-way messaging can be a simple, immediate, and dynamic solution to customer marketing, saving time and resources along the way. 

## Two-way messaging speeds

Two-way messaging leverages custom events to make this seemingly smooth customer client exchange possible. Due to the nature of two-way messaging, you may find a slight increase in response time. Below are the implications of including two-way messaging:

| Type | Speed | Notes | 
| ----- | ----- | ---- | 
| Known Phone Numbers | 3-5 Seconds | A known number is a number that has already been assigned a phone attribute and is already subscribed to a subscription group within Braze.
| Unknown Phone Numbers |  10-15 Seconds | An unknown number is one that has not yet been identifier. For more information on how Unknown phone numbers are dealt with, check out our [documentation][unknown].|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you require faster sending speeds for unknown phone numbers, reach out to your Customer Success Manager or contact support to discuss your options.

## Custom keyword messaging handling

| Custom Event Fired |
| ------- | ------ |
| `sms_response_subscriptionName_custom` | Response Examples => Status, Coupons, News |
{: .reset-td-br-1 .reset-td-br-2}

| Included Event Properties |
| ------- | ------ |
| - `message_body`: users SMS response<br>- `to_number`: usually short code the clients used to send SMS<br>- `from_number`: user's phone number<br>- `sms_message_id`: messaging service ID | Message Body => <br>Users response returned as all lower case |
{: .reset-td-br-1 .reset-td-br-2}

- Anytime a user texts an SMS response that is not a default keyword to a phone number in a given Subscription Group, a custom event like `sms_response_SubscriptionGroupName_custom` with event properties `message_body`, `to_number`, `from_number`, and `sms_message_id` will be sent to Braze. 
- Use this custom event with the property `message_body` assigned as a custom keyword to trigger an SMS campaign from Braze.
- The `message_body` custom keyword value must be __lowercase__.

![picture][IMAGE2]

Note: This feature relies on user aliases in order to properly assign custom events to user profiles in Braze. If no Braze profile exists with a user alias of the user's phone number in E.164 format, the call to the users/track endpoint will fail silently. The alias should be set in the format below either through the SDK or the [new user alias endpoint][endpoint]:
1. alias_label: `phone` and alias_name: `users_phone_number`
2. Phone numbers must be in the E.164 format (e.g +19173337578). 

If using the new user alias endpoint, to ensure E.164 compliance, please add a "+" prefix as the default "phone" field does not automatically include this symbol.

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#handling-unknown-phone-numbers
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}