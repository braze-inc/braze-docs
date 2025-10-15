---
nav_title: WhatsApp messages with optimized delivery
article_title: WhatsApp messages with optimized delivery
page_order: 1
description: "This reference article covers the steps involved in building out and creating a WhatsApp message with optimized delivery."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# WhatsApp messages with optimized delivery

> Leverage Meta’s advanced AI systems to deliver your marketing messages to more users who are most likely to engage with them, significantly boosting deliverability and message engagement.

WhatsApp messages with optimized delivery are sent using Meta's new [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/), which provides superior performance compared to the traditional Cloud API. This new sending pipeline helps you better reach users who value and want to receive your messages.

Benefits of using optimized delivery include:

- **Dynamic messaging limits:** The new API offers more dynamic per-user messaging limits, allowing high-engagement marketing messages (those more likely to be read or clicked) to reach more users.
- **Optimized deliverability:** You can expect lower delivery rates but higher engagement rates for the delivered messages, as Meta’s advanced AI will optimize for users that it expects to value and engage with the message. 
- **Proven results:** In India, messages identified as more likely to be read or clicked had up to 9% more messages delivered compared to sending through Cloud API.
- **Targeted delivery:** Meta’s advanced AI identifies high-engagement messages and delivers them to more users, allowing you to deliver the right message to more of the right people on WhatsApp.


### Regional availability

The availability and optimization capabilities of optimized delivery depend on the region of the business phone number and the user. To learn more, refer to [Geographic availability of features](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Setting up optimized delivery

1. In Braze, go to **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. In the section **Optimize your sending with optimized delivery**, select **Upgrade setting** to trigger the [embedded sign-up workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

![The WhatsApp Message Integration section with an option to optimize sending with optimized delivery.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. After optimized delivery is enabled, your account details in **WhatsApp Business Account Management** will display the optimized delivery status.

![WhatsApp Business Account Management section with a listed subscription group that has an Active number status.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Alternatively, you can enable optimized delivery directly in your WhatsApp manager and then begin sending in Braze.

### Troubleshooting your setup

- **General error:** If something goes wrong during the upgrade, this error banner will display and advise you to [contact Support]({{site.baseurl}}/braze_support/).
- **Ineligible error:** If you are restricted by Meta, this error banner will display: "At least one WhatsApp Business Account is restricted by Meta. Accounts must be in good standing to upgrade.” This can’t be dismissed until the issue is resolved.

## Using optimized delivery in campaigns and Canvases

Optimized delivery should be used for **marketing messages**. Braze will automatically remove the optimized delivery option for **utility, authentication, service, and response messages**, which should continue to be sent through the Cloud API, which is the default setting. 

### Selecting the delivery method

1. In the Braze WhatsApp composer for a campaign or a Canvas message step, go to the **Settings** tab.
2. In the **Delivery method** section, the checkbox for **Optimized Delivery (Recommended)** will be checked by default if your WhatsApp Business Account (WABA) is enabled. If you don’t want to use optimized delivery for that specific message, uncheck the checkbox.
- If you select optimized delivery but it isn’t available, the message will automatically fall back to the Cloud API method.

![Message composer with a preview tab that has a checkbox to select optimized delivery.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})