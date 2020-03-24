---
nav_title: Keyword Processing & Management
page_order: 3
description: "This reference article covers how Braze processes certain keywords for SMS, as well as best practices."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# Keyword Processing & Management

> Keywords are a foundational aspect of automated SMS messaging. With keywords, your users are able to message a preset list of single-word commands that do some type of action. For example, opting in and out of receiving SMS messages. With Braze, you also have the capability of setting custom keywords that can be leveraged for more marketing options. This article will cover how Braze approaches Keyword Processing and Management, as well as some best practices.

## Default Opt-In/ Opt-Out Keywords

Regulations require that there are responses to all opt-in, opt-out and help/info keyword responses. Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

| Type | Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer. |
| Other | `HELP`<br> `INFO` | Triggers custom "help" message built during the onboarding process. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Only the __exact, single-word message__ will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.

If a recipient uses the keywords `HELP` or `INFO`, a response will be triggered automatically. The SMS template for these automatic response messages will be set during your [onboarding][oblink] and phone number procurement period. If you need to change this response, please reach out to your Braze representative.

{% alert important %}
Our delivery vendor manages a blacklist. Occasionally, there is a delay in sync between our blacklist and theirs. For more information or if you suspect this is a current issue for you, reach out to support.
{% endalert %}

## New Users

Braze has the ability to automatically creates a user when a user with a new phone number responds with a `START` or `STOP` (or any other variation of these keywords).  When creating the user, Braze will set their phone field with the [E.164][e.164] number provided by our SMS provider.  In addition, the [User Alias][ualink] ('phone') will be set with the same value.<br><br>Customers can use the [User Attributes Object][uaolink] in tandem with the [Track Endpoint][telink] to find users based on their alias and set an `external_id`.

{% alert important %}
If you would like to enable this functionality, please contact your Onboarding Manager or Customer Success Manager.
{% endalert %}

# Best Practices

## Two-Way Messaging (Custom Keyword Responses)

Two-way messaging uses short codes and keywords to deliver text messages to mobile users. It requires end users to send a keyword to Braze to which that user will receieve an automatic reply. Applied correctly, two-way messaging can be an simple, immediate and dynamic solution to customer marketing, saving time and resources along the way. 

### Two Way Messaging Speeds

Two-way messaging leverges custom events to make this seemingly smooth customer client exchange possible. Due to the nature of two-way messaging, you may find a slight increase in response time. Below are the implications of including two-way messaging:

| Type | Speed | Notes | 
| ----- | ----- | ---- | 
| Known Phone Numbers | 3-5 Seconds | A known number is a number that has already been assigned a phone attribute and is already subscribed to a subscription group within Braze.
| Unknown Phone Numbers |  10-15 Seconds | An unknown number is one that has not yet been identifier. For more information on how Unknown phone numbers are dealt with, check out our [documentation][unknown].|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you require a faster sending speeds for unknown phone numbers, reach out to your customer sucess manager to discuss your options.

### Custom Keyword Messaging Handling

| Custom Event Fired |
| ------- | ------ |
| `sms_response_subscriptionName_custom` | Response Examples => Status, Coupons, News |
{: .reset-td-br-1 .reset-td-br-2}

| Included Event Properties |
| ------- | ------ |
| - `message_body`: users SMS response<br>- `to_number`: usually shortcode the clients used to send SMS<br>- `from_number`: user's phone number<br>- `sms_messsage_id`: messaging service ID | Message Body => <br>Users response returned as all lower case |
{: .reset-td-br-1 .reset-td-br-2}

- Anytime a user texts an SMS response that is not a default keyword to a phone number in a given Subscription Group, a custom event like `sms_response_SubscriptionGroupName_custom` with event properties `message_body`, `to_number`, `from_number`, and `sms_message_id` will be sent to Braze. 
- Use this custom event with the property `message_body` assigned as a custom keyword to trigger an SMS campaign from Braze.
- The `message_body` custom keyword value must be __lowercase__.

![picture][IMAGE2]

Note: This feature relies on user aliases in order to properly assign custom events to user profiles in Braze. If no Braze profile exists with a user alias of the user's phone number in E.164 format, the call to the users/track endpoint will fail silently. The alias should be set in the format below either through the SDK or the [new user alias endpoint][endpoint]:
1. alias_label: `phone` and alias_name: `users_phone_number`
2. Phone numbers must be in the E.164 format (e.g +19173337578)

## Double Opt-In Process

You might find that some users who might send a text to your short/long code, won't yet be opted-in to your SMS Subscription Group. Regulations require that you obtain a user’s explicit consent before you send them any promotional or informational messaging. We highly recommend implementing a double opt-in to ensure compliance. 

![picture][IMAGE1]{: style="float:right;max-width:30%;margin-left:15px;"}
We suggest setting a __triggered entry__ in Canvas whenever there's an incoming event `sms_response_subscriptionGroupName_custom`.

### Step 1: Create Webhook

We first suggest creating a webhook campaign that makes a request to the [subscription/status/set endpoint][SSSendpoint] to subscribe the user to that SMS subscription group.

### Step 2: Send an SMS campaign
Next, we recommend sending an SMS campaign a few seconds later, with clear call-to-actions along the lines of:

![picture][IMAGE]{: style="border: 0"}

[oblink]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[ualink]: {{ site.baseurl }}/api/objects_filters/user_alias_object/
[telink]: {{ site.baseurl }}/api/endpoints/user_data/post_user_track/
[uaolink]: {{ site.baseurl }}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
[endpoint]: {{ site.baseurl }}/api/endpoints/user_data/post_user_alias/
[SSSendpoint]: {{ site.baseurl }}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %}
[IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[unknown]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#handling-unknown-phone-numbers




