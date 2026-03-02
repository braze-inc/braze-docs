---
nav_title: Billing calculator
article_title: "Billing calculator"
page_order: 8
description: "This reference article covers what an SMS segment is, how they are counted for billing, as well as things to keep in mind when creating SMS and RCS message copy."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# SMS and RCS billing calculators

> At Braze, SMS messages are charged per message segment, while RCS messages are charged per message. Understanding what defines an SMS segment and the different RCS billing types will inform your understanding of how you will be billed and will help prevent accidental overages.

## SMS message copy and segment calculator

SMS messages are charged per message segment. Understanding how SMS messages are split is key to understanding your billing.

### What is an SMS segment?

The Short Messaging Service (SMS) is a standardized communication protocol that enables devices to send and receive brief text messages. It was designed to "fit in between" other signaling protocols, which is why SMS message length is limited to 160 7-bit characters, such as 1120 bits, or 140 bytes. SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so clients leveraging SMS greatly benefit from understanding the nuances of how messages will be split.

As you create an SMS campaign or Canvas using Braze, the messages you build in the composer are representative of what your users may see when the message gets delivered to their phone, but **is not indicative of how your message will be split into segments and ultimately how you be charged**. Understanding how many segments will be sent and being aware of the potential overages that could occur is your responsibility, but we provide some resources to make this easier for you. Check out our in-house [segment calculator](#segment-calculator).

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Segment breakdown

The character limit for **a stand-alone SMS segment** is 160 characters ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) encoding) or 70 characters ([UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding) based on the encoding type. However, most phones and networks support concatenation, offering longer-form SMS messages of up to 1530 characters (GSM-7) or 670 characters (UCS-2). So while a message may include several segments, if it does not exceed these concatenation limits, it will be viewed as one message, and reported as such.

It's important to note that **as you pass the character limit of your first segment, additional characters will cause your entire message to be split and segmented based on new character limits**:
- **GSM-7 encoding**
    - Messages exceeding the 160 character limit will now be segmented into 153 character segments and sent individually, then rebuilt by the recipient's device. For example, a 161 character message will be sent as two messages, one with 153 characters and the second with 8 characters.
- **UCS-2 encoding**
    - If you include non-GSM characters such as Emojis, Chinese, Korean, or Japanese script in SMS messages, those messages have to be sent via UCS-2 encoding. Messages exceeding the initial segment limit of 70 characters will cause the entire message to be concatenated into 67 character message segments. For example, a 71 character message will be sent as two messages, one with 67 characters and the second with 4 characters.

Regardless of the encoding type, each SMS message sent out by Braze has a limit of up to 10 segments and is compatible with [Liquid templating]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis, and links.

{% tabs %}
{% tab GSM-7 encoding %}
| Number of characters | How many segments? |
| -------------------- | ----------------- |
| 0 - 160 characters | 1 segment |
| 161 - 306 characters | 2 segments |
| 307 - 459 characters | 3 segments |
| 460 - 612 characters | 4 segments |
| 613 - 765 characters | 5 segments |
| 766 - 918 characters | 6 segments |
| 919 - 1071 characters | 7 segments |
| 1072 - 1224 characters | 8 segments |
| 1225 - 1377 characters | 9 segments |
| 1378 - 1530 characters | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
| Number of characters | How many segments? |
| -------------------- | ----------------- |
| 0 - 70 characters | 1 segment |
| 71 - 134 characters | 2 segments |
| 135 - 201 characters | 3 segments |
| 202 - 268 characters | 4 segments |
| 269 - 335 characters | 5 segments |
| 336 - 402 characters | 6 segments |
| 403 - 469 characters | 7 segments |
| 470 - 536 characters | 8 segments |
| 537 - 603 characters | 9 segments |
| 604 - 670 characters | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Things to keep in mind as you create your copy

- **Character limit per segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) has a 160 character limit for a single SMS segment. For messages with more than 160 characters, all messages will be segmented with a 153 character limit.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) has a 70 character limit per message segment. For messages with more than 70 characters, all messages will be segmented with a 67 character limit.<br><br>
- **Segment limit per message**
    - There is a maximum amount of segments you can send due to the medium's limitations. No more than **10 segments** of messages may be sent in a single Braze SMS message.
    - Those 10 segments will be limited to 1530 characters (GSM-7 encoding) or 670 characters (UCS-2 encoding).<br><br>
- **Compatible with Liquid templating, Connected Content, emojis, and links**
    - Liquid templating and Connected Content may put your message at risk of going over the character limit for your encoding type. You may be able to use the [truncate words filter](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) to limit the number of words that your Liquid could bring to the message.
    - Emojis have no standard character count across all emojis, so make sure to test that your messages are segmenting and displaying correctly.
    - Links may make use of many characters, resulting in more message segments than intended. Though the use of link shorteners is possible, they are best used with short codes. Visit our [SMS FAQ]({{site.baseurl}}/sms_faq/) for more information.<br><br>
- **Testing**
    - Always test your SMS messages before launch, especially when using Liquid and Connected Content as going over message or copy limits may result in additional charges. Note that test messages will count toward your message limits.

### SMS segment calculator {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## RCS message billing

RCS messages are billed based on their content and the country the message is delivered in. To accurately estimate costs, it's essential to understand the different message types and how they are billed.

### RCS billing types

Our platform supports two primary billing models: a global model and a United States model.

#### Global model (non-US markets)

Messages are billed per message and classified as either Basic or Single.

{% tabs local %}
{% tab Basic %}

Basic RCS messages are text-only messages up to 160 characters and are billed as a single message.

{% alert note %}
Adding buttons or any rich elements will change the message type to a Single RCS message.
{% endalert %}

{% endtab %}
{% tab Single %}

Single RCS messages are messages that are over 160 characters OR include any rich elements like buttons or media. These are billed as a single message, regardless of message length.

{% alert note %}
Sending a text message and a separate media file is still billed as two distinct messages.
{% endalert %}

{% endtab %}
{% endtabs %}

#### United States model

Messages are categorized as either Rich or Rich Media.

{% tabs local %}
{% tab Rich messages %}

Rich messages are text-only messages with or without buttons. They are billed per segment, with each segment limited to 160 UTF-8 bytes, which means **the number of characters per segment is not fixed**. A message with only 160 plain English characters is one segment, but a message with longer text and emojis could be multiple segments.

{% endtab %}
{% tab Rich media messages %}

Rich media messages include a media file (image, video) or a Rich Card and are billed as a single message.

{% endtab %}
{% endtabs %}

### Message composer and Message Usage dashboard

As you create your message, the message composer will display the billing type in real-time through a label (Basic RCS, Single RCS, Rich, or Rich Media), helping you track costs before you send.

Your [Message Usage dashboard]({{site.baseurl}}/message_usage_dashboard/) will reflect these billing types and will provide the number of segments used for US messages, providing a transparent view of your message credit consumption.
