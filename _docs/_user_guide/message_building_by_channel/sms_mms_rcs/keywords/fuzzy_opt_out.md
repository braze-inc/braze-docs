---
nav_title: Fuzzy Opt-Out
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

1. Go to **Audience** > **Subscriptions** and select an **SMS/MMS/RCS** subscription group.

{:start="2"}
2. In **Global Keywords**, find the **opt-out** category and select the pencil icon.
3. Enable **Fuzzy Opt-Out** by toggling it on.
4. Modify the fuzzy opt-out response as desired. 

![]({% image_buster /assets/img/sms/fuzzy2.png %}){: style="max-width:70%;"}


