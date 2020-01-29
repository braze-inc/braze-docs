---
nav_title: Keyword Processing & Management
page_order: 2
description: "This reference article covers how Braze proccesses certain keywords for SMS."
page_type: reference
channel: SMS
---

# Keyword Processing & Management

> Braze will process the following keywords automatically and update the [Subscription Group state]({{ site.basurl }}/) for the phone number on all inbound requests.

| Keyword | Change |
|-------|---|
| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. |
| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer. |

{% alert warning %}
Only the __exact, single-word message__ will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.
{% endalert %}

If a recipient uses the keywords `HELP` or `INFO`, a response will be triggered automatically. The SMS template for these automatic response messages will be set during your [onboarding][oblink] and phone number procurement period. If you need to change this response, please reach out to your Braze representative.

{% alert important %}
Our delivery vendor manages a blacklist. Occasionally, there is a delay in sync between our blacklist and theirs. For more information or if you suspect this is a current issue for you, reach out to support.
{% endalert %}

## New users

Braze  automatically creates a user when a user with a new phone number responds with a START or STOP (or any other variation of these keywords).  When creating the user, Braze will set their phone field with the E.164 number provided by our SMS provider.  In addition, the [User Alias][ualink] ('phone') will be set with the same value.<br><br>Customers can use the [User Attributes Object][uaolink] in tandem with the [Track Endpoint][telink] to find users based on their alias and set an `external_id`.

[oblink]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-states
[ualink]: {{ site.baseurl }}/api/objects_filters/user_alias_object/
[telink]: {{ site.baseurl }}/api/endpoints/user_data/post_user_track/
[uaolink]: {{ site.baseurl }}/api/objects_filters/user_attributes_object/