---
nav_title: Fuzzy opt-out
article_title: Fuzzy Opt-Out
description: "This reference article covers how to configure fuzzy opt-out, a setting that attempts to recognize when an inbound message does not match an opt-out keyword."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Fuzzy opt-out

![iOS message chat that shows outbound opt-out messages in response to the inbound fuzzy opt-out "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Users that send SMS, MMS, and RCS with Braze must adhere to the applicable laws, regulations, and industry standards that are defined. For opt-out, the laws dictate that when a user texts "STOP" that all subsequent messaging related to that messaging program will be stopped. Braze automatically processes these messages and unsubscribes the user.<br><br>Fuzzy opt-out attempts to recognize when an inbound message does not match an [opt-out keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), but indicates opt-out intent. If fuzzy opt-out is enabled and an inbound keyword response is deemed "fuzzy," Braze will automatically respond with a response message that instructs users to opt out.

Currently, only opt-out keywords created using English as the [local language]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) are supported.

## What is deemed as fuzzy?

The criteria for an inbound response to be deemed as "fuzzy" are as follows:
- If switching a letter with the letter one to the left or right of it on a QWERTY keyword yields a matching opt-out keyword.
- A substring of the message matches an opt-out keyword.

For example, "Stpo" or "Please stopppp" will be deemed fuzzy, and a fuzzy opt-out response will be sent. If the user then responds with an opt-out keyword, an unsubscribe event will trigger.

## Configure fuzzy opt-out

To configure fuzzy opt-out, navigate to the subscription group keyword management page.

1. Go to **Audience** > **Subscription Group Management** and select an **SMS/MMS/RCS** subscription group.
2. In **Global Keywords**, find the **opt-out** category and select the pencil icon.
3. Enable **Fuzzy Opt-Out** by toggling it on.
4. Modify the fuzzy opt-out response as desired. 

![Section to edit opt-out keywords.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Best practices for fuzzy opt-out messages

To ensure a clear, compliant, and positive experience for your subscribers, it's crucial to configure your fuzzy opt-out message thoughtfully. The main purpose of the fuzzy opt-out message is to **guide users who send a message similar to, but not exactly, your designated opt-out keyword**. The message prompts users on how to successfully unsubscribe.

### Critical considerations

{% alert warning %}
**DO NOT** configure your fuzzy opt-out message to confirm an unsubscribe. Your fuzzy opt-out message must not contain language that implies a user has already successfully unsubscribed. For example, **do not** use "You have been unsubscribed," "You will not receive any more messages from this number," or "You are now opted out".
{% endalert %}

The fuzzy opt-out message is sent before the user has successfully opted out. Using confirmation language misleads the subscriber into believing they are unsubscribed when they are not, leading to continued unwanted messages, subscriber frustration, and significant compliance risks.

{% alert warning %}
**DO NOT** configure your fuzzy opt-out message to be identical or similar to your exact opt-out keyword.
{% endalert %}

If your fuzzy message is the same as, or too close to, your exact opt-out keyword (for example, if "STOP" is your exact keyword and your fuzzy message is "Text STOP to unsubscribe"), it can create confusion about whether the user's initial message actually resulted in an unsubscribe or if they need to take another action. The fuzzy message should always clarify what action the user needs to take.

### Examples of fuzzy opt-out messages

Focus on guiding users. For example, if your opt-out keyword is "STOP", these are good and poor examples of fuzzy opt-out messages you could create:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Good examples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Poor examples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"To unsubscribe from all messages, please reply with the word STOP."</td>
      <td>"You have successfully been unsubscribed. You will not receive any more messages from this number. Reply START to resubscribe." (This is a direct confirmation of unsubscribe, which is misleading in a fuzzy opt-out scenario.)</td>
    </tr>
    <tr>
      <td>"We received your message. If you'd like to stop receiving texts, please text STOP."</td>
      <td>"STOP." (This is just the exact keyword itself, which doesn't guide the user.)</td>
    </tr>
    <tr>
      <td>"Did you mean to unsubscribe? Reply STOP to opt out of all future messages."</td>
      <td>"Text STOP to unsubscribe." (If "STOP" is also your exact keyword, this is redundant and doesn't clarify the action if the initial message was fuzzy.)</td>
    </tr>
  </tbody>
</table>
