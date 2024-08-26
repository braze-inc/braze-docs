
# Sending Phone Numbers

Short and long codes are the phone number from which you send messages to your users or customers. They can be 5 to 6-digit short codes, or 10-digit long codes. Each type of code offers specific benefits and all factors should be considered before choosing whether you want a short code, what type of short code you might want, in addition to the long code you will already be assigned.

## Types of sending numbers

{% tabs %}
{% tab Short Codes %}

#### Short codes

A short code is a memorable 5-6 digit sequence that allows senders to send messages at higher rates than long codes. This makes short codes perfect for high-volume time-sensitive sending.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 5-6 digits | 8-12 week application| 100 messages per second or more | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros and cons

| Pros |
| ---- |
| **Speed and scalability**<br> Short codes offer speed and scalability with sending rates of 100 segments per second, 6,000 segments per minute, 360 thousand segments per hour, and 1 million segments per 2 hours. Short codes can reach such high rates due to the vetting that is required during the short code application process.<br><br>**MMS enabled**<br>Some short codes can support MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets (JPEG, GIF, PNG) to mobile phones. For more information on MMS at Braze, refer to [About MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons |
| ---- |
| **Short codes are available in fewer countries**<br> Short codes are currently available in only the US, UK, and Canada.<br><br>**Longer application process**<br> A 8-12 week application process where use cases must be outlined in great detail is required. This involved process is necessary to support deliverability because after granted a short code, carriers will audit short codes but will **not** filter messages allowing for higher sending rates.<br><br>**Higher cost**<br> Short codes cost more than long codes and take longer to get approved for. However, after you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the sending process, as you will have gone through all of the checks during your application for the short code. |
{: .reset-td-br-1}

{% endtab %}
{% tab Long Codes %}

#### Long codes

A long code is a standard phone number used to send and receive voice calls and SMS messages. Phone numbers are typically called “long codes” (10-digit numbers in many countries) when comparing them with SMS short codes (5-6 digit numbers).

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits | 4-6 week application (can be shorter or longer for different countries) | In the US, throughput is dependent on your 10DLC trust score; in international markets, throughput can vary or be increased in some circumstances. | Yes | 2-way (depending on where you're sending) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros and cons

| Pros |
| ---- |
| **Can be used immediately to send messages (for some countries)**<br>Long codes provide a localized and personal customer experience when sending messages for person-to-person use cases. Unlike SMS short codes, acquiring a long code is a fairly quick process for some countries. (For other countries, it takes as long as or longer than a short code.). Long codes can also be set as a fallback number if a short code fails.<br><br>**Greater availability worldwide**<br>Long codes are available in over 100 major countries worldwide. Please reach out to your Customer Success Manager or Braze [support]({{site.baseurl}}/braze_support/) for a list of available countries.<br><br>**MMS enabled for several countries**<br>Supports MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets (JPEG, GIF, PNG) to mobile phones. For more information on MMS at Braze, check out our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/).|
{: .reset-td-br-1}

| Cons |
| --- |
| **Slower sending speeds**<br>Long codes do not match the speed and sending of short codes. SMS sending rates are dependent on your 10DLC trust score in the US. |
{: .reset-td-br-1}

{% endtab %}
{% tab Vanity Short Code %}

#### Vanity short codes

A vanity short code is a 5-6 digit phone number that is specifically selected by a brand. Vanity short codes are branded and easier for consumers to remember, though are typically more expensive. For example:
- The NYC health department has a vanity short code of `692-692` which spells out NYC-NYC on a telephone keypad.
- Amazon uses a short code of `262-966` which spells out AMA-ZON for shipment tracking updates.
- PayPal uses a short code of `729-725` that spells PAY-PAL for text message commands.<br><br>

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 5-6 digits | 8-12 week application | 100 messages per second | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros and cons

| Pros |
| ---- |
| **Speed and scalability**<br> Short codes offer speed and scalability with sending rates of 100 segments per second, 6,000 segments per minute, 360 thousand segments per hour, and 1 million segments per 2 hours. Short codes can reach such high rates due to the vetting that is required during the short code application process.<br><br>**MMS enabled**<br>Supports MMS, also known as Multimedia Message Service, allowing you to send messages containing multimedia assets(jpg, GIF, png) to mobile phones. For more information on MMS at Braze, refer to [About MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Cons |
| ---- |
| **Short codes are not available everywhere**<br> Short codes are currently available in only the **US and Canada**. <br><br>**Longer application process**<br> A 8-12 week application process where use cases must be outlined in great detail is required. This involved process is necessary to support deliverability because after granted a short code, carriers will audit short codes but will **not** filter messages allowing for higher sending rates.<br><br>**Higher cost in the US**<br> In the US, short codes cost more than long codes and take longer to get approved for. However, after you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the sending process, as you will have gone through all of the checks during your application for the short code. |
{: .reset-td-br-1}

{% endtab %}
{% tab Alphanumeric Sender ID %}

#### Alphanumeric sender ID

Sender IDs are the short or long codes that appear at the top of an SMS message that denotes who the message was sent from. If a user is unfamiliar with a Sender ID, they may opt to ignore these messages altogether. Through the use of alphanumeric sender IDs, users are able to quickly identify who they are receiving messages from, increasing open rates. 

Alphanumeric Sender IDs allow you to set your company name or brand (such as "Kitchenerie" or "CashBlastr") as the Sender ID when sending one-way messages to mobile users. They may be up to 11 characters and accepts upper (A-Z) and lower (a-z) case letters, spaces, and digits (0-9). There **may not** be only numbers. 

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| Up to 11 characters	 | Available immediately if pre-registration is not required | 110 messages per second | No | 1-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros and cons

| Pros | Cons |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> No additional charge to implement </li> <li> Improves brand awareness </li> <li> Increases SMS open rates </li> <li> Matches sending speed of phone numbers inside the subscription group </li> <li> Available immediately if pre-registration is not required </li> </ul> {:/} | {::nomarkdown} <ul> <li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Two-way messaging</a> is not supported </li> <li> Not all countries support this feature </li> <li> Some countries require an additional approval processes </li> <li> MMS is not enabled </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

For more information on Alphanumeric Sender ID, please reach out to your customer success manager. 
{% endtab %}
{% tab Toll-Free Number %}

#### SMS-enabled toll-free number

A toll-free telephone number, or a freephone number, is a telephone number that is billed for all arriving calls instead of incurring charges at the originating telephone subscriber. Toll-free numbers in the US and Canada are SMS-enabled, where subscribers are charged for incoming and outgoing texts.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits	 | 2-4 week application | Depends on your approval and can be raised by paying more | No | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros and cons

| Pros | Cons |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Must be resgistered before sending. </li> </ul> {:/} | {::nomarkdown} <ul> <li> Toll-free numbers are only the US and Canada </li><li> MMS is not enabled </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2} 

{% endtab %} 
{% endtabs %}

{% alert important %}
If throughput is exceeded, some messages may fail.
{% endalert %}

Besides these differences, know that a brand will usually have one short code, but multiple, back-up long codes, depending on how many recipients they plan to send SMS.

{% alert important %}
Wondering what shared short codes are all about? To learn more about why we recommend straying away from shared short codes, visit the topic in our [SMS FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/). 
{% endalert %}

## How do I get a short code?

Going through the short code application process can be a long process. However, it can be a worthwhile one! If you'd like a short code, reach out to your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you—they'll ask for some basic information that will help you qualify. Then, all there is to do is wait!

### Short code application

While Braze is responsible for actually applying for the short code, there is some information that we need from you. We recommend reviewing these questions before you reach out to Braze. 

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. You will need to let us know the specific message flows (the responses you want to send to users after they send a [keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)) that you want for the following situations.

| Flow Needed | Type | Example |
| ----------- | ---- | ------- |
| Opt-In <br><br>Double Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | N/A | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Depending on your situation, you may need to provide more or fewer flows like the ones listed in the preceding table. You'll also have to let us know **three general examples** of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You also must inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, reach out to your Customer Success Manager during the onboarding process to discuss migrating or transferring your short code. Short codes must be set up by your Customer Success Manager. 
{% endalert %}

## Application-to-Person 10-Digit Long Codes (A2P 10DLC)

A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. This service helps alleviate those issues, improving overall message deliverability, allowing brands to send messages at scale including links and calls to action, and helping further protect consumers from unwanted messages. 

All customers who currently have and/or use US long codes to send to US customers are required to register their long codes for 10DLC. This application process takes 4-6 weeks. To read more about the specifics of 10DLC and why it's required, visit our dedicated [10DLC article]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/