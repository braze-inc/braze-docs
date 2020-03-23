---
nav_title: "Short & Long Codes"
page_order: 3
---

# Short & Long Codes

Short and long codes are the phone number from which you send your messages to your users or customers. They can be 6-digit short codes, or 10-digit long codes. Whichever you want is up to you! Braze will take care of procuring either for you.

Besides the obvious "short codes have fewer digits than long codes" spiel, there are other specific benefits to

| Topic | Short Codes | Long Codes |
|---|---|---|
| User Experience | Shorter, more memorable. | Longer, indistinguishable from typical 10-digit phone number. |
| Access | Takes up to 12 weeks to receive permission. However, you are considered a "trusted" number by sending providers. | Available immediately, but subject to more vetting and gates before messages are cleared for send. |
| Sending Limits <br> _SMS are subject to Braze's own [rate limits]({{ site.baseurl }}//user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/)._ | 100 messages per second. | 1 message per second. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Besides these differences, know that a brand will usually have one short code, but multiple, back-up long codes, depending on how many recipients they plan to send SMS.

## Short Code Application

That's right, you actually have to apply for a short code. It's a longer process, but worthwhile if you know you need one! This article will walk you through the pros and cons of both short and long codes, as well as what the application for a short code requires from you and how to migrate your short code from your previous messaging provider.

You'll need to let us know message flows (the responses you want to send to users after they send a [keyword]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/)) for...

| Flow Needed | Example |
| --- | --- |
| Opt-In/Double Opt-In via SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In via Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out via SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2}

Depending on your situation, you may need to provide more or fewer flows the ones listed above. You'll also have to let us know three general examples of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You should also inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, reach out to your Braze representative during the onboarding process to discuss migrating or transferring your short code.
{% endalert %}
