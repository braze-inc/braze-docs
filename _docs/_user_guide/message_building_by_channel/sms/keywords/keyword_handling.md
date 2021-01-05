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

# SMS Keyword Handling

> Keywords are a foundational aspect of automated SMS messaging. With keywords, your users are able to message a list of single-word commands that do some type of action. For example, opting in and out of receiving SMS messages. With Braze, you also have the capability of setting custom keywords and groups that can be leveraged for more marketing options. Read more about our new SMS keyword handling process below. 

## Default Opt-In/ Opt-Out Keywords

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

To support this, Braze has the following keyword categories, each with its own keyword set and action that will take effect once we receive an inbound SMS requests. Note that these default keywords and responses can also be customized.

| Type | Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with one of these `Opt-In` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. <br><br>User will receive your defined Opt-In auto response.  |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with one of these `Opt-In` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer.<br><br>User will receive your defined Opt-Out auto response. |
| Help | `HELP`<br> `INFO` | User will receive your defined Help auto response. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Only the __exact, single-word message__ will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.

## Editing Keywords

If you would like to edit the default keywords set by Braze and add a new keyword to trigger an Opt-In, Opt-Out, or Help action, you can do this by navigating to your SMS subscription group and clicking into the group to edit your settings: 

![picture][1]

Here, you will see the default keywords and responses and have the option to modify those responses by clicking the "Edit" icon to the right of each keyword category.

![picture][2]

This will bring up an edit modal to allow you to add keywords or modify responses. Note that Braze enforces global keywords (e.g START, YES, UNSTOP) to be set so these defaults cannot be changed. Please read the rules below that apply to keywords and keyword responses. 

![picture][3]{: style="max-width:50%;"}

| Keywords | Keyword Responses |
| -------- | ----------------- |
| - Valid UTF8 encoded characters<br>- Maximum of 20 keywords per category total<br>- Maximum length of 34 characters<br>- Minimum length of 1 character <br>- Cannot contain spaces<br>- Required to be case insensitive and unique across the subscription group | - Cannot be blank<br>- Maximum length of 300 characters<br>- Valid UTF8 characters |
{: .reset-td-br-1 .reset-td-br-2}

## Multi-Language Support

When sending to certain countries, a sender may be required to support inbound keywords and outbound replies with a local language. To support this, Braze allows you to create a language-specific keyword setting. 

![picture][4]{: style="float:right;max-width:40%;margin-left:10px;"}
To get started, click "Add A Language" and select your target language or search for a language within the dropdown.

Please note that other languages do NOT come with preset keywords/responses like English, so senders will need to work with their marketing and legal teams to add any required keywords to this set. Otherwise, Braze will not handle localized incoming messages for those languages. If you need to delete a language, click the "Delete Language" button at the bottom right.

![picture][5]

## Custom Keyword Categories

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you are also able to create up to 10 of your own keyword categories. This allows you to identify arbitrary keywords and set up responses specific to your business. An example category might be "PROMO" or "DISCOUNT" which might prompt a response about promos that are happening this month. 

These custom keywords operate in an "always-on" capacity, meaning that any user subscribed to your message service can text keywords and receive a response at any point. In addition to this behavior, you also have the option to define specific keywords that can only be sent to at [certain points]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) of your user's lifecycle. 

![picture][12]

### Create a Custom Category
![picture][13]{: style="float:right;max-width:40%;margin-left:10px;"}
To create a custom keyword category, edit the appropriate subscription group, and click "Add Custom Keyword Category". Here, you will be able to provide a keyword category name and define which keywords a user can text in to receive the reply message.

Once created, this keyword category will be available to [filter]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#filter-by-recency) and [trigger]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword)  against in your campaigns and Canvases.

Keywords created in custom keyword categories adhere to all of the rules and validations stated above for the creation of new keywords. 

### Lifecycle Specific Keywords

If you have a use case where you would like to limit when a customer can send a specific keyword during their lifecycle (e.g during their first initial onboarding) to receive a response, you can use the trigger "Send inbound SMS to subscription group within keyword category OTHER" in your campaign/Canvas and define some ad-hoc keywords that your users can send in at a point in time. 

#### Canvas

![picture][14]{: style="max-width:80%;"}

#### Campaign

![picture][15]{: style="max-width:80%;"}

## Retargeting

In addition to changing the user's subscription state and sending auto-responders based on incoming keywords, Braze will also record interactions to the user profile for filtering and triggering messages.

### Filter by Recency

Filter for the recency of a user responding to your SMS Program. This filter will evaluate the LAST date a user sent an inbound SMS that is within one of the keyword categories. 

![picture][6]

### Trigger Messages by Keyword

Messages can be triggered as users send messages inbound based on keyword categories (user sent any one of the keywords) or other keywords (user sent a keyword that does not fall into one of the existing categories). These triggers are set in the Delivery step of the campaign builder.

__Trigger by Inbound Keyword Category__<br>
![picture][7]{: style="margin-top:10px;"}

__Trigger by Arbitrary Keywords__<br>
Note triggering a message on an "Other" keyword response, you will have the opportunity to evaluate the keyword body on an exact text match. This match follows the same rules as noted above: Only the __exact, single-word message__ will be processed (case _insensitive_). A keyword sent of `Hello Braze!` would not match the criteria shown in the example below. 
![picture][8]{: style="margin-top:10px;"}

__Template Keywords__<br>
When triggering a Campaign or Canvas Step on an inbound SMS, you can optionally template the text that your user sent into the body of your Campaign or Canvas with Liquid. This will enable you to access the user's response which you can then include in your reply, apply conditional logic to, or anything else you can do with Liquid. 

![picture][16]{: style="max-width:80%;"}
<br><br>
![picture][17]{: style="max-width:80%;"}

## Currents Event
Any inbound SMS event can be sent as a Currents [event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) through the SMS InboundRecieved event. To get this feature flipped on so you can enable it within your own Currents integration, reach out to your account manager. Please note that inbound messages are truncated past 1600 characters. 

![picture][9]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_channel.png %}
[2]: {% image_buster /assets/img/sms/sms_keywords.png %}
[3]: {% image_buster /assets/img/sms/keyword_edit.png %}
[4]: {% image_buster /assets/img/sms/multi-language.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[9]: {% image_buster /assets/img/sms/sms_currents.png %}
[10]: {% image_buster /assets/img/sms/custom_category.png %}
[11]: {% image_buster /assets/img/sms/keyword_list.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}