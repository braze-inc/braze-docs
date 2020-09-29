---
nav_title: Keyword Handling
page_order: 0
description: "This reference article covers the new beta process of handling custom keyword."
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

alias: /keyword_handling/
hidden: true
---

{% alert note %}
This new SMS keyword handling process is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Default Opt-In/ Opt-Out Keywords

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

To support this, Braze has the following keyword categories, each with its own keyword set and action that will take effect once we receive an inbound SMS requests. Note that these default keywords and responses can also be customized.

| Type | Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. <br><br>User will receive your defined Opt-In auto response.  |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer.<br><br>User will receive your defined Opt-Out auto response. |
| Other | `HELP`<br> `INFO` | User will receive your defined Help auto response. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Only the __exact, single-word message__ will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.

If a recipient uses the keywords `HELP` or `INFO`, a response will be triggered automatically. The SMS template for these automatic response messages will be set during your [onboarding][oblink] and phone number procurement period. If you need to change this response, please reach out to your Braze representative.

{% alert important %}
Our delivery vendor manages a blacklist. Occasionally, there is a delay in sync between our blacklist and theirs. For more information or if you suspect this is a current issue for you, reach out to support.
{% endalert %}

## Editing Keywords

If you would like to edit the default keywords set by Braze and add a new keyword to trigger an Opt-In, Opt-Out, or Help action, you can do this by navigating to your SMS subscription group and clicking into the group to edit your settings: 

![picture][1]

Here, you will see the default keywords and responses and have the ability to modify those responses by clicking the "edit" icon to the right of the keyword category:

![picture][2]

This will bring up an edit modal to allow you to add keywords or modify responses. Note that Braze enforces global keywords (e.g START, YES, UNSTOP) to be set so these defaults cannot be changed. The following rules apply to add keywords:
- Valid UTF8 encoded characters
- Maximum of 20 keywords per category total 
- Maximum length of 34 characters
- Minimum length of 1 character 
- Cannot be blank keyword ("") or empty space (" ")
- Keywords cannot contain spaces
- Keywords are required to be case insensitive unique across the subscription group

![picture][3]{: style="max-width:80%;"}

## Multi-Language Support

When sending to certain countries, a sender may be required to support inbound keywords and outbound replies with a local language. To support this, Braze allows you to create a language-specific keyword setting. 

![picture][4]{: style="float:right;max-width:40%;margin-left:10px;"}
To get started, click "Add A Language" and select your target language or search for a language within the dropdown.

Please note that other languages do NOT come with preset keywords/responses like English, so senders will need to work with their marketing and legal teams to add any required keywords to this set. Otherwise, Braze will not handle localized incoming messages for those languages. If you need to delete a language, click the "Delete Langauge" button at the bottom right:

![picture][5]

## SMS Custom Keyword Categories

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), customers will be able to create their own keyword categories. This allows the customer to create arbitrary keywords and responses specific to their business. Keyword categories have a limit of 10 per customer to avoid abuse. As we have to store a field on a customer's user profile for __each__ category they respond to, having 100s of custom keywords makes it difficult for analytics and storage. 

Therefore, keyword categories should be set up for those business-specific keywords that you want to operate in an "always-on" capacity meaning anytime a user who is subscribed to your SMS program text one of them in, they are eligible to receive a message.

## Retargeting

In addition to changing the user's subscription state and sending auto-responders based on incoming keywords, Braze will also record interactions to the user profile for filtering and triggering messages.

### Filter by Recency

Filter for the recency of a user responding to your SMS Program. This filter will evaluate the LAST date a user sent an inbound SMS that is within one of the keyword categories. 

![picture][6]

### Trigger Messages by Keyword

Messages can be triggered as users send messages inbound based on keyword categories or arbitrary keywords. These triggers are set in the Delivery step of the campaign builder.

__Trigger by Inbound Keyword Category__<br>
![picture][7]{: style="margin-top:10px;"}

__Trigger by Arbitrary Keywords__<br>
![picture][8]{: style="margin-top:10px;"}

## Currents Event
Any inbound SMS event can be sent as a Currents event through the SMS InboundRecieved event. Reach out to your account manager to learn more. 

[1]: {% image_buster /assets/img/sms/sms_channel.png %}
[2]: {% image_buster /assets/img/sms/sms_keywords.png %}
[3]: {% image_buster /assets/img/sms/keyword_edit.png %}
[4]: {% image_buster /assets/img/sms/multi-language.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
