---
nav_title: Keyword Processing & Management
page_order: 3
description: "This reference article covers how Braze processes certain keywords for SMS, as well as best practices."
page_type: reference
channel: SMS
---

# Keyword Processing & Management

> Keywords are a foundational aspect of automated SMS messaging. With keywords, users are able to message a preset list of single-word commands that do some type of action, for example, opting in and out of receiving SMS messages. With Braze, you also have the capability of setting custom keywords that can be leveraged for more marketing options. This article will cover how Braze approaches Keyword Processing and Management, as well as some best practices.

## Default Opt-In/ Opt-Out Keywords

Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

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

Braze automatically creates a user when a user with a new phone number responds with a `START` or `STOP` (or any other variation of these keywords).  When creating the user, Braze will set their phone field with the [E.164][e.164] number provided by our SMS provider.  In addition, the [User Alias][ualink] ('phone') will be set with the same value.<br><br>Customers can use the [User Attributes Object][uaolink] in tandem with the [Track Endpoint][telink] to find users based on their alias and set an `external_id`.

# Best Practices

## Two-Way Messaging (Custom Keyword Responses)

| Custom Keyword Message Handling |
| ---- | --- | -- |
| Custom Event Fired | `sms_response_subscriptionName_custom` | Response examples =><br> __Status, Coupon, News__ |
| Included Event Properties | `message_body`<br>`to_number`<br> `from_number`<br> `sms_messsage_id` | __Message Body__ =><br> User response returned as lower-case |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

- Anytime a user texts an SMS response to a phone number in a given Subscription Group other than the default opt-in/opt-out keywords, will fire a custom event like  __sms_response_SubscriptionGroupName_custom__ with event properties __message_body__, __to_number__, __from_number__, and __sms_message_id__ to Braze. 
- Use this custom event with property __message_body__ assigned as a custom keyword to trigger an SMS campaign from Braze.
- Make sure that the __message_body__ custom keyword value is lowercase.

![picture][IMAGE2]

Note: This feature relies on user aliases in order to properly assign custom events to user profiles in Braze. By default, if no Braze profile exists with a user alias of the user's phone number in E.164 format, the call to the users/track endpoint will fail silently. <br>
The alias should be set in the format below either through the SDK or the [new user alias endpoint][endpoint]:
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

![picture][IMAGE]

[oblink]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-states
[ualink]: {{ site.baseurl }}/api/objects_filters/user_alias_object/
[telink]: {{ site.baseurl }}/api/endpoints/user_data/post_user_track/
[uaolink]: {{ site.baseurl }}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
[endpoint]: {{ site.baseurl }}/api/endpoints/user_data/post_user_alias/
[SSSendpoint]: {{ site.baseurl }}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %}
[IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}




