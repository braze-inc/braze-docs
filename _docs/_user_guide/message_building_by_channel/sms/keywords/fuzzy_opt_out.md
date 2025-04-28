---
nav_title: Fuzzy Opt-Out
article_title: Fuzzy Opt-Out
description: "This reference article covers how to configure fuzzy opt-out, a setting that attempts to recognize when an inbound message does not match an opt-out keyword."
page_type: reference
channel:
  - SMS
page_order: 1

---

# Fuzzy opt-out

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Users that send SMS with Braze must adhere to the applicable laws, regulations, and industry standards that are defined. For opt-out, the laws dictate that when a user texts "STOP" that all subsequent messaging related to that messaging program will be stopped. Braze automatically processes these messages and unsubscribes the user.<br><br>Fuzzy opt-out attempts to recognize when an inbound message does not match an [opt-out keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/), but indicates opt-out intent. If fuzzy opt-out is enabled and an inbound keyword response is deemed "fuzzy," Braze will automatically respond, asking the user to confirm their intent. 

Currently, only opt-out keywords created using English as the [local language]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) are supported.

## What is deemed as fuzzy?

The criteria for an inbound response to be deemed as "fuzzy" are as follows:
- If switching a letter with the letter one to the left or right of it on a QWERTY keyword yields a matching opt-out keyword.
- A substring of the message matches an opt-out keyword.

For example, "Stpo" or "Please stopppp" will be deemed fuzzy, and a fuzzy opt-out response will be sent.

## Configure fuzzy opt-out

To configure fuzzy opt-out, navigate to the subscription group keyword management page.

1. Go to **Audience** > **Subscriptions** and select an SMS subscription group.

{:start="2"}
2. In **SMS Global Keywords**, find the **opt-out** category and select the pencil icon.
3. Enable **Fuzzy Opt-Out** by toggling it on.
4. Modify the fuzzy opt-out response as desired. 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

