---
nav_title: SMS FAQs
page_order: 20
---

# SMS Frequently Asked Questions

On this page, we'll attempt to answer your most stringent questions about SMS!

{% details Who does Braze use to send SMS? %}

We have an extensive SMS partnership with [Twilio](https://www.twilio.com/), who we work with to send messages to carriers and other SMS stakeholders.

{% enddetails %}


{% details What laws do I need to follow to send SMS with Braze? %}

We recommend you use your best judgment, but we, as well as our sending partners, have checks in place that prevent most SMS abuses. There are a few general rules you should follow:

- Do not SPAM.
- Offer your recipients a way to opt-out and get help via SMS.
- Send at a healthy cadence - do not overwhelm your customers.
- Do not send abusive or inappropriate content (for example, sending marketing content to someone who only wants transactional content).

You can see our [Compliance Best Practices here]({{ site.baseurl }}/help/best_practices/sms/compliance.md).

{% enddetails %}


{% details How will I be billed for SMS? %}

Besides the charges for Short and Long Codes, billing is done by the number of messages sent per country. Overages will cost a bit more per message. Different providers and carriers down the send pipeline will charge different rates in different circumstances, so billing can vary per region.

You should reach out to your Braze representative for more exact details.

{% enddetails %}

{% details How do I get a short code? %}

Getting a short code can be a long process. However, it can be a worthwhile one! If you'd like a short code, reach out to your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you - they'll ask for some basic information that will help you qualify. Then, all there is to do is wait! Short codes can take up to 12 weeks to receive approval to start using your short code.

You can [learn more about Short Codes and Long Codes here]({{ site.baseurl }}/).
{% enddetails %}



{% details What is the difference between a short code and a long code? %}

A short code has five (5) digits, while a long code has ten (10). Each come with their own benefits and you should consider all of the factors before choosing whether you want a short code in addition to the long code you will already be assigned.

Short codes cost more than long codes and take longer to receive. However, once you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the send process, as you will have gone through all of the checks during your application for the short code.

You can [learn more about long codes and the short code application process here]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms/short_code_application/).

{% enddetails %}


{% details How can I avoid overages? %}

While we can't promise that you won't occasionally have an overage, you could follow these precautions to decrease chances of going over your allotted limits:

- Pay attention to the number of characters in your SMS. Unintentionally sending more than one segment could cause overages.
- Carefully calculate your SMS characters to account for Liquid or Connected Content. The Braze SMS composer in your dashboard does not estimate or factor in usage of either of these features.
- Consider the type of encoding your message uses - if your message uses GSM-7 encoding, you can usually estimate that you can send a message with 128 characters per message segment. If your message uses UCS-2 encoding,  you can usually estimate that you can send a message with 67 characters per message segment.
- Test test test! Always test your SMS messages before launch, especially when using Liquid and Connected Content.
{% enddetails %}



{% details What keywords does Braze automatically process? %}

Braze will only automatically process the following _exact, single-word, case-insensitive_ messages:

- `START`, `YES`, `UNSTOP`: Subscribes user to messages from that number pool.
- `STOP`, `STOPALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT`: Unsubscribes user from messages from that number pool.
- `HELP`, `INFO`: Triggers custom "help" message built fduring onboarding process.

[Learn more about Keyword Processing and Management here]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/).
{% enddetails %}
