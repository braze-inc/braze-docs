---
nav_title: "Best Practices"
page_order: 5
description: "This reference article covers best practices surrounding SMS campaigns."
page_type: reference
channel: SMS
---

# SMS Best Practices

## Default Opt-In/ Opt-Out

|| Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer. |

- Regulations require that there are responses to all opt-in, opt-out and help/info keyword responses.
- When user responds with default keyword, Braze will automatically update the subscription status for all user profiles with that phone number.

## Two-Way Messaging

Managing Custom Keyword Responses

| Custom Keyword Message Handling |
| ---- | --- | -- |
| Custom Event Fired | `sms_response_subscriptionName_custom` | Response examples => __Status, Coupon, News__ |
| Included Event Properties | `message_body`<br>`to_number`<br> `from_number`<br> `sms_messsage_id` | __Message Body__ => User response returned as lower-case |

- An incoming SMS response with a keyword other than default opt-in/out will fire a custom event with event properties to Braze
- Use this custom event with property “message_body” to trigger an SMS campaign from Braze
- Make sure that the “message_body” value is lowercase

## Handling Unknown Phone Numbers

Braze automatically addresses an unkown number in one of three ways:
1. If an opt-in keyword is texted:
- Braze creates an anonymous profile
- Sets the phone attribute
- Subscribes the user to the cooresponding subscription group based on what opt-in keyword was recieved by Braze.
2. If an opt-ou keyword is texted:
-Braze creates an anonymous profile
- Sets the phone attribute
- Unsubscribes the user form the cooresponding subscription group based on what opt-out keyword was recieved by Braze.
3. If any other custom keyword is texted:
- Braze ignores the text message and does nothing.

## Double Opt-In Process

You might find that some users who might send a text to your short/long code, won't yet be opted-in to your SMS Subscription Group. Regulations require that you obtain a user’s explicit consent before you send them any promotional or informational messaging. We highly recommend implementing a Double-Opt In to ensure compliance. 

We suggest setting a triggered entry in Canvas whenever there's an incoming event `sms_response_subscriptionGroupName_custom`.

### Step 1: Create Webhook

We first suggest to create a webhook campaign that makes a request to the subscription/status/set endpoint to subscribe the user to that SMS subscription group.

### Step 2: Send a SMS campaign
Next, we recommend sending an SMS campaign a few second later, with clear call-to-actions along the lines of:

[IMAGE]

## Multi-Country SMS Sending

In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, short codes can only send SMS to phone numbers from the same country the short code was created in. 

To overcome this limitation, Subscription Groups can hold long and short codes from multiple different countries and will automatically use the appropriate short code or long code when targeting a user for SMS. 

## High Volume Sending

Plan on doing some high volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate-limiting for your campaign/canvases as needed, based on target audience size. This will ensure that (1) you reach the send volume that you need and (2) Braze sends the messages at the rate that Twilio is expecting and can handle

- Look to AE/leadership to assist with increased MPS rate discussions with Twilio
Please note: higher throughput pricing needs to go through deal desk

- Ensure you are sticking to the 160 character limit, and aware of special characters double counting, i.e. \ ^ ~ 