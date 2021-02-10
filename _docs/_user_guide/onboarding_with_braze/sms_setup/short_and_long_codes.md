---
nav_title: "Sending Phone Numbers"
page_order: 4
description: "This article will walk you through important concepts involved in sending phone numbers with Braze. Included are considerations to keep in mind when using short codes and long codes, an explanation of the application process for a short code, and other topics like handling unknown numbers and high volume and multi-country sending."
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

# Phone Numbers

> This article will walk you through important concepts involved in sending phone numbers with Braze. Included are considerations to keep in mind when using short codes and long codes, an explanation of the application process for a short code, and other topics like handling unknown numbers and high volume and multi-country sending.

## Short & Long Codes

Short and long codes are the phone number from which you send your messages to your users or customers. They can be 5 to 6-digit short codes, or 10-digit long codes. Whichever you want is up to you! Braze will take care of procuring either for you.

Besides the length difference between short and long codes, there are other specific benefits too and all factors should be considered before choosing whether you want a short code in addition to the long code you will already be assigned.

| Topic | Short Codes | Long Codes |
|---|---|---|
| Length | Five (5) to six (6) digits | Ten (10) digits |
| User Experience | Shorter, more memorable. | Longer, indistinguishable from typical 10-digit phone number. |
| Access | Takes up to 12 weeks to receive permission. However, you are considered a "trusted" number by sending providers. | Available immediately, but subject to more vetting and gates before messages are cleared for send. |
| Sending Limits/Speed <br> _SMS are subject to Braze's own [rate limits]({{site.baseurl}}//user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/)._ | 100 messages per second. | 1 message per second (US)<br> 10 messages per second (International) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

In addition, Short codes cost more than long codes and take longer to get approved for. However, once you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the send process, as you will have gone through all of the checks during your application for the short code.

Besides these differences, know that a brand will usually have one short code, but multiple, back-up long codes, depending on how many recipients they plan to send SMS.

### How Do I Get a Short Code?

Going through the short code application process can be a long process. However, it can be a worthwhile one! If you'd like a short code, reach out to your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you - they'll ask for some basic information that will help you qualify. Then, all there is to do is wait! Short codes can take up to 12 weeks to receive approval to start using your short code.

### Short Code Application

While Braze is responsible for actually applying for the short code, there is some information that we need from you. We recommend reviewing these questions before you reach out to Braze. 

Regulations require that there are responses to all opt-in, opt-out and help/info keyword responses. You will need to let us know the specific message flows (the responses you want to send to users after they send a [keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/)) that you want for...

| Flow Needed | Type | Example |
| ----------- | ---- | ------- |
| Opt-In <br><br>Double Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | n/a | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Depending on your situation, you may need to provide more or fewer flows the ones listed above. You'll also have to let us know __three general examples__ of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You also must inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, reach out to your Customer Success Manager  __during the onboarding process__ to discuss migrating or transferring your short code. Short codes must be set up by your Customer Success Manager. 
{% endalert %}

## Handling Unknown Phone Numbers
You may find that once you get SMS up and running with Braze that you receive messages from unknown users. Noted below are the steps through which an unidentified user and number get processed.

Braze automatically addresses an unknown number in one of three ways:
1. If an opt-in keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.<br><br>
2. If an opt-out keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Unsubscribes the user form the corresponding subscription group based on what opt-out keyword was received by Braze.<br><br>
3. If any other custom keyword is texted:
  * Braze ignores the text message and does nothing.

## Alphanumeric Sender ID
![picture][senderID]{: style="float:right;max-width:30%;margin-left:15px;border: 0"}

Sender IDs are the short or long codes that appear at the top of an SMS message that denotes who the message was sent from. If a user is unfamiliar with a Sender ID, they may opt to ignore these messages altogether. Through the use of Alphanumeric sender IDs, users are able to quickly identify who they are receiving messages from, increasing open rates. 

Alphanumeric Sender IDs allow you to set your company name or brand as the Sender ID when sending one-way messages to mobile users. They may be up to 11 characters and accepts upper (A-Z) and lower (a-z) case letters, spaces, and digits (0-9). There __may not__ be only numbers. 

| Pros | Cons |
|- No additional charge to implement<br>- Improves brand awareness<br>- Increases SMS open rates<br>- Matches sending speed of phone numbers inside the subscription group. |- [Two-way messaging][2] is not supported<br>- Not all countries support this feature<br>- Some countries require an additional approval processes. This may take additional time. |
{: .reset-td-br-1 .reset-td-br-2}

For more information on Alphanumeric Sender ID, please reach out to your Customer Success Manager. 

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses
[senderID]: {% image_buster /assets/img/sms/alphanumericsenderid.jpg %}