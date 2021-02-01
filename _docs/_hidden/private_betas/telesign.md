---
nav_title: TeleSign
alias: /partners/telesign/

description: "This article outlines the partnership between Braze and TeleSign, a cloud communications platform helping the world’s leading websites and mobile applications."
page_type: partner

---

# TeleSign

> [TeleSign][1] is a cloud communications platform helping the world’s leading websites and mobile applications across SMS messaging, voice messaging, mobile app verification, and phone intelligence.

## Using TeleSign Example and Walkthrough

For this example, we’ll configure the Braze webhook channel to send SMS to your users, via [TeleSign's SMS API.][2]

To use TeleSign’s SMS web service to send a request, you’ll need to use the following Webhook URL when composing a webhook in Braze:
```
https://rest-api.telesign.com/v1/messaging
```

{% alert important %}
Customers using Telesign's SMS product will need to [purchase a number](https://standard.telesign.com/api-reference/additional-features/inbound-sms#buy-a-phone-number-sender-id) from them.
{% endalert %}

### Step 1: Set Up Your Request Body

The TeleSign API expects the request body to be URL-encoded, so you must change the request type in the Braze Webhook composer to Raw Text. The required parameters for the body of the request are Phone Number (phone_number), Message (message), and Message Type (message_type). You’ll need to have _valid_ phone numbers on each user profile in your target audience. TeleSign defines a valid phone number as the end user's phone number _with country code included._


![telesign_step1.png][3]

The image below depicts an example of what your request might look like if you are sending an SMS to each user’s phone number, with the body “Hello from Braze!”.

### Step 2: Compose Request Headers and HTTP Method

TeleSign requires two request headers, the request Content-Type, and an HTTP Basic Authentication header.

![headerchart.png][6]

Add these to your webhook by clicking the gear icon on the right side of the Webhook composer, then clicking _Add New Pair_ twice.

When you add them to your webhook, be sure to replace `TELESIGN_CUSTOMER_ID` and `TELESIGN_API_KEY` in the Header Values with values from your TeleSign dashboard. Lastly, TeleSign’s API endpoint expects an HTTP POST request, so choose that option in the dropdown for the HTTP Method.

![telesign_step2.png][4]


### Step 3: Preview Your Request

Use the Webhook composer to preview the request for a random user, or for a user with particular credentials, to ensure that the request is rendering properly.

![telesign_step3.png][5]

Make adjustments as needed, and be sure to save your template! Happy messaging!



[1]: https://www.telesign.com/
[2]: https://standard.telesign.com/docs/sms-api
[3]: {% image_buster /assets/img_archive/telesign_step1.png %}
[4]: {% image_buster /assets/img_archive/telesign_step2.png %}
[5]: {% image_buster /assets/img_archive/telesign_step3.png %}
[6]: {% image_buster /assets/img_archive/headerchart.png %}