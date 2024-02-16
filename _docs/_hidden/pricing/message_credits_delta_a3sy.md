---
nav_title: Message Credits - Delta
permalink: "/message_credits_delta_a3sy/"
hidden: true
noindex: true
---

# Message Credits - Delta (Confidential)

> Message Credits is our billing methodology for our native SMS, MMS, and WhatsApp channels. We use Message Credits to provide a flexible and transparent experience when taking advantage of Braze messaging channels. You may use the credits you purchased across any of these channels in any way you want.

Below is the reference table for each channel and message destination we offer.

Definition for the columns are as follows:

**Channel:** High level channel grouping we use to organize our billing

**Channel Credit Ratio:** Baseline credit amount for each channel

**Destination:** Specific region or country messages are being sent to as part of a given channel

**Multiplier:** Tied to the channel/destination combination; will scale the channel credit ratio down or up depending on how cheap or expensive the destination is

**Credits Consumed with One Message:** Exactly how many credits you are using for per message

{% alert note %}
Different channels will have different units of measure for what defines a credit consumed.<br><br>
<b>WhatsApp:</b> Conversations<br>
<b>SMS:</b> Segments<br>
<b>MMS:</b> Segments<br><br>
In other words, credits used for WhatsApp messages will be calculated on conversation initiations, and credits used for both SMS and MMS messages will be calculated on segments sent.
<br><br>
Lastly, carrier fees are billed separately (in arrears) and are not considered as part of this Message Credits SKU.
{% endalert %}

| Channel | Channel Credit Ratio | Destination | Multiplier | Credits Used with One Message | 
| --- | --- | --- | --- | --- |
| Argentina| 16.5 | 11 | 8.5 | 9.5 |
| Brazil | 16.5 | 9.5 | 8 | 8.5 |
| Chile | 23.5| 15.5 | 12 | 14 |
| Colombia | 3.5 | 2.5 | 1.5 | 2 |
| Egypt | 28.5 | 18 | 17 | 16.5 |
| France | 38| 20.5 | 3 | 18.5 |
| Germany | 36| 22.5 | 21.5 | 20.5 |
| India | 2.5 | 1 | 1 | N/A |
| Indonesia | 11 | 5.5 | 5 | N/A |
| Israel | 9.5 | 5 | 5 | 4.5 |
| Italy | 18.5 | 11 | 10 | 10 |
| Malaysia | 23 | 5.5 | 6 | 5 |
| Mexico | 11.5 | 7 | 3 | 6.5 |
| Netherlands | 42.5 | 21 | 23.5 | 19 |
| Nigeria | 13.5 | 8.5 | 8 | 7.5 |
| North America | 6.5 | 4| 2.5 | 3.5 |
| Other | 16 | 9 | 4 | 8 |
| Pakistan | 12.5 | 6.5 | 4 | 6 |
| Peru | 18.5 | 11 | 4.5 | 10 |
| Rest of Africa | 6 | 4 | 9.5 | 4 |
| Rest of Asia Pacific | 19.5 | 12.5 | 6 | 11.5 |
| Rest of Central & Eastern Europe | 23 | 16.5| 6.5 | 15 |
| Rest of Latin America | 19.5 | 13 | 11 | 12 |
| Rest of Middle East | 9 | 5.5 | 6 | 4.5 |
| Rest of Western Europe | 15.5 | 11 | 10.5 | 10 |
| Russia | 21.5 | 12.5 | 10.5 | 11.5 |
| Saudi Arabia | 11 | 6.5 | 5 | 6 |
| South Africa | 10 | 5.5 | 4.5 | 5 |
| Spain | 16.5 | 10 | 10 | 9 |
| Turkey | 3 | 2.5 | 1 | 2 |
| United Arab Emirates | 9 | 5.5 | 5 | 4.5 |
| United Kingdom | 18.5 | 10.5 | 10.5 | 9.5 |
{: .reset-td-br-1 .reset-td-br-2}

## WhatsApp channel details

### Conversation type definitions

**Marketing Conversations:** Business-initiated conversations that may include promotions or offers, informational updates like a back-in-stock alert, or invitations for customers to respond or take action

**Utility Conversations:** Business-initiated conversations facilitating a specific, agreed-upon request or transaction, or update to a customer about an ongoing transaction, including post-purchase notifications and recurring billing statements

**Authentication Conversations:** Enable businesses to authenticate users with one-time passcodes, potentially at multiple steps in the login process (for example, account verification, account recovery, integrity challenges). 
* Authentication conversations will only be supported on a case-by-case basis and Braze cannot guarantee specific SLAs. Additionally, Braze does not support PIN generation. 

**Service Conversations:** User-initiated conversations that are responded to with a non-templated
message. 

{% alert note %}
User-initiated conversations that are responded to with a message template will be billed based on the template that the business responds with (for example, marketing, utility, or authentication).
{% endalert %}

### Billing region breakdown

#### North America
United States, Canada

#### Rest of Africa
Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Chad, Congo, Eritrea, Ethiopia, Gabon, Gambia, Ghana,  Guinea-Bissau, Ivory Coast, Kenya, Lesotho, Liberia, Libya,
Madagascar, Malawi, Mali, Mauritania, Morocco, Mozambique, Namibia, Niger, Rwanda, Senegal, Sierra Leone, Somalia, South Sudan, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia

#### Rest of Asia Pacific
Afghanistan, Australia, Bangladesh, Cambodia, China, Hong Kong, Japan, Laos, Mongolia, Nepal, New Zealand, Papua New Guinea, Philippines, Singapore, Sri Lanka, Taiwan, Tajikistan, Thailand,
Turkmenistan, Uzbekistan, Vietnam

#### Rest of Central & Eastern Europe
Albania, Armenia, Azerbaijan, Belarus, Bulgaria, Croatia, Czech Republic, Georgia, Greece, Hungary, Latvia, Lithuania, Macedonia, Moldova, Poland, Romania, Serbia, Slovakia, Slovenia, Ukraine

#### Rest of Latin America
Bolivia, Costa Rica, Dominican Republic, Ecuador, El Salvador,
Guatemala, Haiti, Honduras, Jamaica, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

#### Rest of Middle East
Bahrain, Iraq, Jordan, Kuwait, Lebanon, Oman, Qatar, Yemen

#### Rest of Western Europe
Austria, Belgium, Denmark, Finland, Ireland, Norway, Portugal, Sweden, Switzerland
