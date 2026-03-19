---
nav_title: "Ads That Click to WhatsApp"
article_title: Ads That Click to WhatsApp
page_order: 1
description: "This reference article provides a step-by-step guide for setting up and using Ads That Click to WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Ads That Click to WhatsApp

> This page provides a step-by-step guide for setting up and using Ads That Click to WhatsApp, so you and your team can elevate your WhatsApp program.

Ads That Click to WhatsApp are an efficient way to bring both new and existing customers from Meta ads on Facebook, Instagram, or other platforms. Use these ads to promote your products and services while making users aware of your WhatsApp presence.

![A Facebook ad from Calorie Rocket that advertises free delivery, and the respective WhatsApp conversation that occurs when a user selects the ad's button.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Setting up Ads That Click to WhatsApp

1. In the Meta Ads Manager, create an ad on Facebook, Instagram, or other platforms by following the step-by-step guide [How to create Ads That Click to WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **Do not** set up automated responses; you will set up responses in Braze instead.

![Ads Manager with a composer to create an engagment ad.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

When setting up the pre-filled message, which will be sent by the user to your WhatsApp Business Account, include a specific word or phrase that you’ll use to trigger a response specific to the particular ad. In this example, a food delivery app is using "free delivery" because that is promoted in their ad. 

![Ads Manager template composer with a pre-filled message of "I want free delivery".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Make it clear in the ad description that clicking the ad will start a conversation with your brand by using phrases like “Chat now on WhatsApp". 
{% endalert %}

{: start="2"}
2. In Braze, set up an action-based Canvas where the action-based option is **Send a WhatsApp inbound message** and the message body is “YOUR_TRIGGER_WORD”. In this example, a food delivery app is using "free delivery".

![Entry schedule for an action-based Braze Canvas, with the trigger event of "Send a WhatsApp inbound message" and a message body that matches regex of "free delivery".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. Set up a response message in the Canvas that sends immediately after the customer enters the Canvas (for example, after no delay). Although clicking the ad technically constitutes opt-in, we recommend setting up your response message to ask the user if they’d like to receive future marketing messages from you on WhatsApp. 

{% alert tip %}
Set up your response message with quick replies (such as "Yes" or "No Thanks") so users can quickly indicate whether they'd like to opt in.
{% endalert %}

Don’t forget to also provide any discount code, offer, or other information promised in the ad!

![WhatsApp message composer with button replies of "Yes" and "No Thanks".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Canvas step with an "Opting in" group with a trigger event of "Sent inbound WhatsApp to subscription group" and a trigger word of "YES".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. Opt-in users by updating the subscription status of user profiles with one of the following update methods:
    - Create a Braze-to-Braze webhook that updates the subscription status through the REST API.  
    - Use the advanced JSON editor to update the user profile with the template to [update a user's subscription status to a WhatsApp Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process).

![User Update Canvas step that uses the advanced JSON editor to update the user profile.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas showing the workflow for sending Ads That Click to WhatsApp, including three action paths: Opting in, Opting Out, and Everyone Else.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Considerations

Conversations that start from an Ad That Clicks to WhatsApp are free of charge if the following conditions are met:

- If a user messages you through a [Free Entry Point](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), such as an Ad That Clicks to WhatsApp, a 24-hour [customer service window](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) opens in which you can send that user any type of message.
- If you respond within the customer service window (within 24 hours), a free entry point opens for 72 hours, and all messages within the 72-hour window will be free of charge.
- Response messaging is free of charge.