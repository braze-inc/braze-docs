---
nav_title: Opt-In / Opt-Out
article_title: SMS Opt-In/Opt-Out Keywords
page_order: 0
description: "This reference article covers how Braze processes basic opt-in and opt-out keywords for SMS messaging."
page_type: reference
tool:
  - Dashboard

channel:
  - SMS
---

# Opt-in and opt-out keywords

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. Braze automatically processes the following _exact, single-word, case-insensitive_ messages, automatically updating the [Subscription Group state]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) for the user and their associated phone number on all inbound requests.

## Keyword overview

Braze will process the following keywords automatically and update the Subscription Group state for the phone number on all inbound requests. Note that these default keywords and responses may also be customized. 

| Type | Keyword | Change |
|-|-------|---|
|Opt-in| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with one of these `Opt-In` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. <br><br>User will receive your defined Opt-In auto response.  |
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with one of these `Opt-Out` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer.<br><br>User will receive your defined Opt-Out auto response. |
| Help | `HELP`<br> `INFO` | User will receive your defined Help auto response. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Only the **exact, single-word message** will be processed (case _insensitive_). Keywords such as `STOP PLEASE` will be ignored.

If a recipient uses the keywords `HELP` or `INFO`, a response will be triggered automatically. The SMS template for these automatic response messages will be set during your [onboarding][oblink] and phone number procurement period. Note that you may continue to update these responses after the initial onboarding period.

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
