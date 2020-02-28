---
nav_title: "Sending Phone Numbers"
page_order: 1
description: "description"
page_type: reference
channel: SMS
---

# Phone Numbers


## Handling Unknown Phone Numbers

Braze automatically addresses an unkown number in one of three ways:
1. If an opt-in keyword is texted:
- Braze creates an anonymous profile
- Sets the phone attribute
- Subscribes the user to the cooresponding subscription group based on what opt-in keyword was recieved by Braze.
2. If an opt-out keyword is texted:
- Braze creates an anonymous profile
- Sets the phone attribute
- Unsubscribes the user form the cooresponding subscription group based on what opt-out keyword was recieved by Braze.
3. If any other custom keyword is texted:
- Braze ignores the text message and does nothing.

## How do I get a short code?

Getting a short code can be a long process. However, it can be a worthwhile one! If you'd like a short code, reach out to your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you - they'll ask for some basic information that will help you qualify. Then, all there is to do is wait! Short codes can take up to 12 weeks to receive approval to start using your short code.

You can [learn more about Short Codes and Long Codes here]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/).


## What is the difference between a short code and a long code?

A short code has five (5) digits, while a long code has ten (10). Each come with their own benefits and you should consider all of the factors before choosing whether you want a short code in addition to the long code you will already be assigned.

Short codes cost more than long codes and take longer to receive. However, once you have a short code, you are considered "pre-approved" to send messages at better, faster rates and are subject to less scrutiny during the send process, as you will have gone through all of the checks during your application for the short code.

You can [learn more about long codes and the short code application process here]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/).


## Short & Long Codes

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

| Flow Needed | Type | Example |
| ----------- | ---- | ------- |
| Opt-In <br><br>Double Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | n/a | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Depending on your situation, you may need to provide more or fewer flows the ones listed above. You'll also have to let us know three general examples of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You should also inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, reach out to your Braze representative during the onboarding process to discuss migrating or transferring your short code.
{% endalert %}

## Multi-Country SMS Sending

In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, short codes can only send SMS to phone numbers from the same country the short code was created in. 

To overcome this limitation, Subscription Groups can hold long and short codes from multiple different countries and will automatically use the appropriate short code or long code when targeting a user for SMS. 

## High Volume Sending

Plan on doing some high volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate-limiting for your campaign/canvases as needed, based on target audience size. This will ensure that (1) you reach the send volume that you need and (2) Braze sends the messages at the rate that Twilio is expecting and can handle

- Look to AE/leadership to assist with increased MPS rate discussions with Twilio
Please note: higher throughput pricing needs to go through deal desk

- Ensure you are sticking to the 160 character limit, and aware of special characters double counting, i.e. \ ^ ~ 
