---
nav_title: SMS FAQs
page_order: 8
description: "This reference article addresses some of the most frequently asked questions that arise when setting up SMS campaigns."
page_type: reference

channel:
  - SMS
---

# SMS Frequently Asked Questions

> On this page, we'll attempt to answer your most stringent questions about SMS!

{% details How will I be billed for SMS? %}
Besides the charges for Short and Long Codes, billing is done by the number of message segments sent per country. To read more about how message segments are calculated see our [Message Segments and Copy Limits]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown) guide. 
For overages, your account manager will reach out to let you know if you are close to reaching your maximum, providing relevant reports to help inform you. For further questions regarding overages, please reach out to your Braze representative.

{% enddetails %}

{% details How can I avoid overages? %}
While we can't promise that you won't occasionally have an overage, you could follow these precautions to decrease the chances of going over your allotted limits:

- Pay attention to the number of characters in your SMS. Unintentionally sending more than one segment could cause overages. More details [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Carefully calculate your SMS characters to account for Liquid or Connected Content. The Braze SMS composer in your dashboard does not estimate or factor in the usage of either of these features.
- Consider the type of encoding your message uses - if your message uses GSM-7 encoding, you can usually estimate that you can send a message with 128 characters per message segment. If your message uses UCS-2 encoding,  you can usually estimate that you can send a message with 67 characters per message segment.
- Test test test! Always test your SMS messages before launch, especially when using Liquid and Connected Content.
{% enddetails %}

{% details Can you include links in an SMS? %}
A client can include any link in any SMS campaign they would like. However, there are a few concerns to consider:
- Links may make use of many characters and take up a lot of the 160 character limit for SMS. If you include a link and text, it may result in two SMS messages, instead of just one. 
- Companies often use link shorteners to limit the character count impact of a link. However, if sending a shortened link through a long code, carriers may block/deny the message as they may be suspicious of the link redirect.
- Using a short code would be the most reliable number type for including links
{% enddetails %}

{% details Do test text messages count toward limits? %}
Yes, they do. Please keep this in mind when testing messages. 
{% enddetails %}

{% details How many characters does an emoji utilize? %}
Emojis can be a bit trickier, as there is no standard character count across all emojis. There is the risk the emoji will exceed the character limit and break the SMS into multiple messages, despite it showing as one message in the Braze composer. When QA'ing your messages, you can better verify if a message will be split using [this tool]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator). 
{% enddetails %}

{% details If a user texts STOP to our short code, are they unsubscribed from the subscription group?  %}
What does that look like on the user profile? The subscription group will revert to 2 dashes (- -), and there will be custom events for subscribe and unsubscribe. 
{% enddetails %}

{% details Is there a way to see if an alias exists on a user profile? %}
Aliases are not visible on the user profile, you would need to use an export API to confirm aliases being set.
{% enddetails %}

{% details How would a client create logic so that when a user opts-in to SMS for VIP vs. Alerts, they are subscribed to the right subscription group?  %}
Custom keywords would be written as custom events, so you would want to create segments based on the keywords customers can text in.
{% enddetails %}

{% details Does Braze de-dupe multiple users with the same phone number? %}
Braze will de-dupe users on the canvas step level, so it should not be possible for a user to receive more than one SMS text for a canvas step, even if multiple users share the same phone number.  **Important to note, if you stagger your users into a canvas and have different schedule times for each canvas step, you can send a user with the same email/phone duplicate messages**
{% enddetails %}

{% details Do clients need to rate-limit how fast they send SMS messages? %}
The default concurrency rate and throughput enables &#126;360k/hour per short code. Additional throughput requires additional short codes.
{% enddetails %}

{% details Is there a character limit to the sms_response event and the property for response? (e.g. will it capture if a user sends an entire sentence) %}
Event properties have a character limit of 256, otherwise, there is no character limit. In order for a keyword to be recognized within a sentence, (e.g. "please stop texting me") you would have to utilize a Liquid statement in the message to recognize the specific word.
{% enddetails %}

{% details What are shared short codes? %}
With a shared short code, all text messages, no matter what business or organization sends them, arrive on a consumer's mobile device from the same 5-6 digit phone number. While shared short codes are relatively low cost and immediately available, this means that your business __will not have a dedicated short code__. Some downsides to this approach include: <br>
- If your customers opt-out of another business's messages that have a shared short code with you, they will have opted out of your messages as well.<br>
- If one business violates the rules, all businesses' messages are suspended.
- Security Issues<br>
{% enddetails %}
