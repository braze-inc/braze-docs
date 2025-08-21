---
nav_title: Phone Number Acquisition
article_title: Phone Number Acquisition
page_order: 3
description: "This reference article covers how to acquire a phone number from Twilio and Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Phone number acquisition

> To use the WhatsApp messaging channel, you'll need a phone number that meets WhatsApp’s requirements for its [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) or [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

You must acquire your phone number yourself, as Braze won't provision the number for you. You can either purchase a physical phone with a SIM card through your business phone provider or use one of our partners: Twilio or Infoblip. **You must have your own Twilio or Infobip account because this cannot be done through Braze.**

## WhatsApp API requirements

Your phone number must meet these WhatsApp API requirements:

- Owned by your business 
- Have a country and area code (such as a landline and cell numbers)
- Able to receive voice calls or SMS
- Accessible during account setup (to receive verification codes)
- Not a short code
- Not previously used with the WhatsApp Business Platform
- Not connected to a personal WhatsApp account

## Acquiring a Twilio phone number

### Step 1: Buy a phone number from the Twilio console or API

1. From the Twilio console, go to **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. If you don’t see this option, select **Explore Products**, scroll to **Super Networks**, then select **Phone Number** > **Buy a number**. <br><br>![Twilio console with the "Develop" tab opened and "Buy a number" option.]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Enter your desired area code or locality (if you have one). Find a number, then select **Buy**. <br><br> ![A button to buy the listed phone number.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. After purchasing your phone number, go to **Active Numbers** and select the phone number you just purchased. <br><br>!["Active Numbers" showing the purchased phone number.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Step 2: Configure your phone number

Follow Twilio's instructions to [set up your Twilio phone number to receive the verification code via email using Twilio Voice Only](https://www.twilio.com/docs/whatsapp/self-sign-up#setting-up-your-twilio-phone-number-to-receive-the-verification-code-via-email-using-voicemail-transcription). **Do not follow the instructions in any other step, as that will connect your phone number to Twilio, not Braze.**

{% alert warning %}
**Only follow Twilio's instructions to receive a verification code.**

If you follow the next steps in Twilio's instructions, you'll connect your phone number to Twilio. That means you can't connect that number to Braze unless you do a migration or purchase a different number.
{% endalert %}

### Step 3: Complete the embedded sign up workflow

1. After Twilio is configured, go to your Braze dashboard > **Technology Partners** > **WhatsApp** and select **Begin integration** or **Add WhatsApp Business Account**, whichever shows up, to trigger the [embedded sign up workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>In the **Add a phone number for WhatsApp** step, select **Phone call** for how you'd like to verify your phone number. <br><br>![Section with the options to verify your phone number through text message or a phone call.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Wait a few minutes for the verification code to send to your email inbox, then enter the verification code and complete your setup.

## Acquiring an Infobip phone number 

1. In the Infobip console, go to **Channels and Numbers** and select **Numbers**.<br><br>![Infoblip "Channels and Numbers" section with "Numbers" listed beneath.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Select **Buy Number** > the country where you want to send messages > **SMS**.<br><br>![Button to buy a number.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Depending on your selected country, you might need to complete an additional registration process (such as selecting a 10 DLC or toll-free option for US phone numbers). Be sure to select the available option.<br><br>![A page asking for you to select the number type: either 10 DLC or toll-free.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Select the available offer, then proceed through the rest of the steps and wait for your request to be processed. You can check the status by going to **Numbers** > **My Request**. <br><br>![An offer with information including fees and coverage.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Depending on your selected country, wait for the Infobip team to reach out for registration details (such as for 10DLC in the US).<br><br>

6. When your phone number is ready in Infobip, go to your Braze dashboard > **Technology Partners** > **WhatsApp** and select **Begin integration** or **Add WhatsApp Business Account**, whichever shows up, to trigger the [embedded sign up workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> In the **Add a phone number for WhatsApp** step, select **Text message** for how you'd like to verify your phone number.<br><br>![Section with the options to verify your phone number through text message or a phone call.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Check Infobip’s [analyze logs](https://www.infobip.com/docs/analyze/analyze-logs) in their customer portal for the verification code, which could take a few minutes to appear, then enter the verification code and complete setup.




