---
nav_title: "Short and Long Codes"
page_order: 1
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


# Short and Long Codes

Short and long codes are the phone number from which you send messages to your users or customers. They can be 5 to 6-digit short codes, or 10-digit long codes. Each type of code offers specific benefits and all factors should be considered before choosing whether you want a short code, what type of short code you might want, in addition to the long code you will already be assigned.

## Types of Sending Numbers

![SMS Number Graph][3]

{% tabs %}
{% tab Short Codes %}

#### Short Codes

A short code is a memorable 5-6 digit sequence that allows senders to send messages at more consistent rates than long codes. If you are sending several hundred messages a day from a long code, your messages run the risk of being marked as spam. This makes short codes perfect for high-volume time-sensitive sending.

| Pros |
| ---- |
| __Speed and scalability__<br> Short codes offer speed and scalability with sending rates of 100 segments per second, 6,000 segments per minute, 360 thousand segments per hour, and 1 million segments per 2 hours. Short codes can reach such high rates due to the vetting that is required during the short code application process.<br><br>__MMS enabled__<br>Supports MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets(jpg, gif, png) to mobile phones. For more information on MMS at Braze, check out our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons |
| ---- |
| __Short codes are not available everywhere__<br> Short codes are currently available in only the US, UK, and Canada.<br><br>__Long application process__<br> A 8-12 week application process where use cases must be outlined in great detail is required. This involved process is necessary to ensure deliverability because after granted a short code, carriers will audit short codes but will __not__ filter messages allowing for higher sending rates.<br><br>__Higher cost__<br> Short codes cost more than long codes and take longer to get approved for. However, once you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the sending process, as you will have gone through all of the checks during your application for the short code. |
{: .reset-td-br-1}

{% endtab %}
{% tab Long Codes %}
#### Long Codes
A long code number is a standard phone number used to send and receive voice calls and SMS messages. Phone numbers are typically called “long codes” (10-digit numbers in many countries) when comparing them with SMS short codes (5-6 digit numbers).

| Pros |
| ---- |
| __Can be used immediately to send messages__<br>Long codes provide a localized and personal customer experience when sending messages for person-to-person use cases. Unlike SMS short codes, acquiring a long code is a fairly quick process. Long codes can also be set as a fallback number if a short code fails.<br><br>__Greater availability worldwide__<br>Long codes are available in over 100 major countries worldwide. Please reach out to your customer success manager for a list of available countries.<br><br>__MMS enabled__<br>Supports MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets(jpg, gif, png) to mobile phones. For more information on MMS at Braze, check out our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/).|
{: .reset-td-br-1}

| Cons |
| --- |
| __Slower sending speeds__<br>Long codes do not match the speed and sending of short codes. SMS sending rates are 1 segment per second in the US, 10 segments per second internationally. |
{: .reset-td-br-1}

{% endtab %}
{% tab Vanity Short Code %}
#### Vanity Short Codes

A vanity short code is a 5-6 digit phone number that is specifically selected by a brand. Vanity short codes are branded and easier for consumers to remember, though are typically more expensive. For example:
- The NYC health department has a vanity short code of `692-692` which spells out NYC-NYC on a telephone keypad.
- Amazon uses a short code of `262-966` which spells out AMA-ZON for shipment tracking updates.
- Paypal uses a short code of `729-725` that spells PAY-PAL for text message commands.<br><br>

| Pros |
| ---- |
| __Speed and scalability__<br> Short codes offer speed and scalability with sending rates of 100 segments per second, 6,000 segments per minute, 360 thousand segments per hour, and 1 million segments per 2 hours. Short codes can reach such high rates due to the vetting that is required during the short code application process.<br><br>__MMS enabled__<br>Supports MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets(jpg, gif, png) to mobile phones. For more information on MMS at Braze, check out our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons |
| ---- |
| __Short codes are not available everywhere__<br> Short codes are currently available in only the __US and Canada__.<br><br>__Long application process__<br> A 8-12 week application process where use cases must be outlined in great detail is required. This involved process is necessary to ensure deliverability because after granted a short code, carriers will audit short codes but will __not__ filter messages allowing for higher sending rates.<br><br>__Higher cost__<br> Short codes cost more than long codes and take longer to get approved for. However, once you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the sending process, as you will have gone through all of the checks during your application for the short code. |
{: .reset-td-br-1}

{% endtab %}
{% tab Alphanumeric Sender ID %}
#### Alphanumeric Sender ID

![picture]({% image_buster /assets/img/sms/alphanumericsenderid.jpg %}){: style="float:right;max-width:30%;margin-left:15px;border: 0"}

Sender IDs are the short or long codes that appear at the top of an SMS message that denotes who the message was sent from. If a user is unfamiliar with a Sender ID, they may opt to ignore these messages altogether. Through the use of Alphanumeric sender IDs, users are able to quickly identify who they are receiving messages from, increasing open rates. 

Alphanumeric Sender IDs allow you to set your company name or brand as the Sender ID when sending one-way messages to mobile users. They may be up to 11 characters and accepts upper (A-Z) and lower (a-z) case letters, spaces, and digits (0-9). There __may not__ be only numbers. 

| Pros | Cons |
| ---- | ---- | 
|- No additional charge to implement<br>- Improves brand awareness<br>- Increases SMS open rates<br>- Matches sending speed of phone numbers inside the subscription group.<br>- Available immediately if pre-registration is not required|- [Two-way messaging]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses) is not supported<br>- Not all coutries support this feature<br>- Some countries require an additional approval processes. This may take additional time.<br>- MMS is not enabled |
{: .reset-td-br-1 .reset-td-br-2}

For more information on Alphanumeric Sender ID, please reach out to your Customer Success Manager. 
{% endtab %}
{% tab Toll-Free Number %}
#### SMS Enabled Toll-Free Number

A toll-free telephone number, or a freephone number, is a telephone number that is billed for all arriving calls instead of incurring charges at the originating telephone subscriber. Toll-free numbers in the US and Canada are SMS-enabled, where subscribers are charged for incoming and outgoing texts.

| Pros | Cons |
| ---- | ---- | 
| - Can be used immediately to send messages | - Toll-free numbers are only the __US and Canada__<br>- Slower sending speed of 1 segment per second.<br>- MMS is not enabled |
{: .reset-td-br-1 .reset-td-br-2}


{% endtab %} 
{% endtabs %}

Besides these differences, know that a brand will usually have one short code, but multiple, back-up long codes, depending on how many recipients they plan to send SMS.

{% alert important %}
Wondering what shared short codes are all about? To learn more about why we recommend straying away from shared short codes, visit the topic in our SMS FAQ [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/). 
{% endalert %}

## How Do I Get a Short Code?

Going through the short code application process can be a long process. However, it can be a worthwhile one! If you'd like a short code, reach out to your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you - they'll ask for some basic information that will help you qualify. Then, all there is to do is wait! Short codes can take up to 12 weeks to receive approval to start using your short code.

### Short Code Application

While Braze is responsible for actually applying for the short code, there is some information that we need from you. We recommend reviewing these questions before you reach out to Braze. 

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. You will need to let us know the specific message flows (the responses you want to send to users after they send a [keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)) that you want for...

| Flow Needed | Type | Example |
| ----------- | ---- | ------- |
| Opt-In <br><br>Double Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | n/a | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Depending on your situation, you may need to provide more or fewer flows like the ones listed above. You'll also have to let us know __three general examples__ of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You also must inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, reach out to your Customer Success Manager  __during the onboarding process__ to discuss migrating or transferring your short code. Short codes must be set up by your Customer Success Manager. 
{% endalert %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[3]: {% image_buster /assets/img/sms/sms_graph.png %}