---
nav_title: Product Messages
article_title: Product Messages
page_order: 1
description: "This page covers how to use WhatsApp product messages to send interactive WhatsApp messages that showcase products from your Meta catalog."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Product messages

> Product messages empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog. 

{% alert important %}
WhatsApp product messages are currently in early access and are planned to have rolling updates through the early access duration. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

When you send a WhatsApp product message to a user, the user goes on the following customer journey: 

1. The user receives your product or catalog message in WhatsApp.
2. The user adds products to their cart directly from WhatsApp.
3. The user taps "Place order" in WhatsApp.
4. Your website or app recieves the cart data from Braze and generates a checkout link.
5. The user is directed to your website or app to complete their checkout.

## Requirements

| Requirement | Description |
| --- | --- |
| WhatsApp Business Account | To use WhatsApp product messages, you must have a WhatsApp Business Account connected with Braze. |
| Meta catalog | You need to set up a Meta catalog in your Commerce Manager. |
| Term compliance | Comply with the [Meta Commerce Terms and Policies](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Setting up product messages

1. In the [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), follow [Meta's instructions](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) to create your Meta catalog. Make sure you’re in the same Meta Business Portfolio where your Braze-connected WhatsApp Business Accont resides.
2. Follow Meta's instructions to [connect your Meta catalog](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) to your Braze-connected WhatsApp Business Account by assigning catalog permissions in Meta Business Manager. Make sure to use the Braze Business Manager ID, `332231937299182`, when assigning Braze as a partner with the “Manage Catalog” permission.
3. Select your Meta catalog settings. You must select “Show catalog icon in chat header” to send catalog messages. 
4. In Braze, go through the [embedded signup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) process to provide permissions. This will unlock the Braze integrated product selector. 

{% alert tip %}
For best practices to follow when creating Meta catalogs, refer to [Tips for building a high-quality catalog in Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Building product messages


