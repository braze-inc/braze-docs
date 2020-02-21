---
nav_title: SMS FAQs
page_order: 6
description: "This reference article addreses some of the most frequently asked questions that arise when setting up SMS campaigns."
page_type: reference
channel: SMS
---

# SMS Frequently Asked Questions

> On this page, we'll attempt to answer your most stringent questions about SMS!

{% details How will I be billed for SMS? %}

Besides the charges for Short and Long Codes, billing is done by the number of messages sent per country. Overages will cost a bit more per message. Different providers and carriers down the send pipeline will charge different rates in different circumstances, so billing can vary per region.

You should reach out to your Braze representative for more exact details.

{% enddetails %}

{% details How can I avoid overages? %}

While we can't promise that you won't occasionally have an overage, you could follow these precautions to decrease chances of going over your allotted limits:

- Pay attention to the number of characters in your SMS. Unintentionally sending more than one segment could cause overages.
- Carefully calculate your SMS characters to account for Liquid or Connected Content. The Braze SMS composer in your dashboard does not estimate or factor in usage of either of these features.
- Consider the type of encoding your message uses - if your message uses GSM-7 encoding, you can usually estimate that you can send a message with 128 characters per message segment. If your message uses UCS-2 encoding,  you can usually estimate that you can send a message with 67 characters per message segment.
- Test test test! Always test your SMS messages before launch, especially when using Liquid and Connected Content.
{% enddetails %}
