---
nav_title: Opt-In / Opt-Out
page_order: 0
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

# Opt-In/ Opt-Out Keywords

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

## Keyword Overview

Braze will process the following keywords automatically and update the Subscription Group state for the phone number on all inbound requests. Note that these default keywords and responses may also be customized. 

| Type | Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer. |
| Other | `HELP`<br> `INFO` | Triggers custom "help" message built during the onboarding process. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Only the __exact, single-word message__ will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.

If a recipient uses the keywords `HELP` or `INFO`, a response will be triggered automatically. The SMS template for these automatic response messages will be set during your [onboarding][oblink] and phone number procurement period. Note that you may continue to update these responses after the initial onboarding period.

{% alert important %}
Our delivery vendor manages a blacklist. Occasionally, there is a delay in sync between our blacklist and theirs. For more information or if you suspect this is a current issue for you, reach out to support.
{% endalert %}

## Managing Keywords and Auto Responses

SMS with Braze gives you the option to create keyword triggers, custom responses, and define keyword sets for multiple languages. 

### Add Keyword Triggers
In addition to the default opt-in and opt-out keywords listed above, you may also define your own keywords to trigger Opt-In, Opt-Out, and Help responses.

![Home][1]{: style="float:right;max-width:40%;margin-left:10px;""}
1. To define your own keywords, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select a keyword category to add a keyword to by selecting the pencil icon. 
3. In the dialogue box that pops up, add a keyword you would like to trigger this keyword category. Note that keywords are case sensitive, and universal keywords like `START`, `YES`, and `UNSTOP` cannot be changed.

### Manage Responses
You are able to manage your own responses that get sent to users after they text in a keyword to a specific keyword category.
1. To manage your keyword responses, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select a keyword category to edit a response for by selecting the pencil icon. 
3. In the dialogue box that pops up, edit and save your response. Please be mindful of the [Six Rules to get Compliance Right]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) as you create your response.<br><br>
![Responses][2]

### Define Keyword Sets
You can create keyword sets for different languages so the keywords received for different languages can be appropriately replied to.
![Language][3]{: style="float:right;max-width:30%;margin-left:15px;margin-top:15px;"}

1. To define a keyword set, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select __Add a Language__, and choose the appropriate language for your keyword set. Once clicked, a new global keyword list will be added to fill out with the necessary keywords and responses in the language you chose.<br>

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[3]: {% image_buster /assets/img/sms/keyword_language.png %}