---
nav_title: FAQs
title: SMS FAQs
page_order: 8
description: "This article addresses some of the most frequently asked questions that arise when setting up SMS campaigns."
page_type: FAQ

channel:
  - SMS
---

# SMS FAQs

> On this page, we'll attempt to answer your most stringent questions about SMS!

## Can you include links in an SMS?

You can include any link in any SMS campaign you would like. However, there are a few concerns to consider:

- Links may take up much of the 160 character limit for SMS. If you include a link and text, it may result in two SMS messages, instead of just one.
- Companies often use link shorteners to limit the character count impact of a link. However, if sending a shortened link through a long code, carriers may block or deny the message, as they may be suspicious of the link redirect.
- Using a [short code]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) would be the most reliable number type for including links.

## Do test text messages count toward limits?

Yes, they do. Please keep this in mind when testing messages.

## Do you need to rate-limit how fast you send SMS messages?

The default concurrency rate and throughput enables about 360,000 messages an hour per short code. Additional throughput requires additional short codes.

## How can I avoid overages?

While we can't promise that you won't occasionally have an overage, you could follow these precautions to decrease the chances of going over your allotted limits:

- Pay attention to the number of characters in your SMS. Unintentionally sending more than one segment could cause overages. More details [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Carefully calculate your SMS characters to account for Liquid or Connected Content. The Braze SMS composer in your dashboard does not estimate or factor in the usage of either of these features.
- Consider the type of encoding your message uses - if your message uses GSM-7 encoding, you can usually estimate that you can send a message with 128 characters per message segment. If your message uses [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding, you can usually estimate that you can send a message with 67 characters per message segment.
- Test test test! Always test your SMS messages before launch, especially when using Liquid and Connected Content.

## How do you create logic for selective opt-ins to SMS so users are in the right subscription group?

Custom keywords would be written as custom events, so you would want to create segments based on the keywords customers can text in. For example, if a user opts in to SMS for VIP messages, but not Alerts, you can create a VIP segment and an Alerts segment, then assign the user to the appropriate segment.

## How many characters does an emoji utilize?

Emojis can be a bit tricky, as there is no standard character count across all emojis. There is the risk the emoji will exceed the character limit and break the SMS into multiple messages, despite it showing as one message in the Braze composer. When QA'ing your messages, you can better verify if a message will be split using [this tool]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

## How will I be billed for SMS?

Besides the charges for Short and Long Codes, billing is done by the number of message segments sent per country. To read more about how message segments are calculated see our [Message Segments and Copy Limits]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown) guide. 
For overages, your account manager will reach out to let you know if you are close to reaching your maximum, providing relevant reports to help inform you. For further questions regarding overages, please reach out to your Braze representative.

## If a user texts STOP to our short code, are they unsubscribed from the subscription group?

What does that look like on the user profile? The subscription group will revert to 2 dashes (- -), and there will be custom events for subscribe and unsubscribe.

## Is there a way to see if an alias exists on a user profile?

Aliases are not visible on the user profile, you would need to use the Export User Data endpoints to confirm aliases being set.

## What are shared short codes?

With a shared short code, all text messages, no matter what business or organization sends them, arrive on a consumer's mobile device from the same 5-6 digit phone number. While shared short codes are relatively low cost and immediately available, this means that your business will not have a dedicated short code.

Some downsides to this approach include:

- If your customers opts-out of another business's messages that have a shared short code with you, they will have opted out of your messages as well.
- If one business violates the rules, all businesses' messages are suspended.
- Security Issues

## What happens if multiple users have the same phone number?

Braze will de-dupe users on the Canvas step level, so it should not be possible for a user to receive more than one SMS text for a Canvas step, even if multiple users share the same phone number.

{% alert important %} If you stagger your users into a Canvas and have different schedule times for each Canvas step, you can send a user with the same email or phone duplicate messages. {% endalert %}

## Will SMS event properties capture keywords in a sentence?

In order for a keyword to be recognized within a sentence, (e.g. "please stop texting me") you'll need to use a Liquid statement in the message to recognize the specific word. Event properties have a character limit of 256, otherwise, there is no character limit.

