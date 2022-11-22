---
nav_title: Overview
article_title: WhatsApp Overview
alias: /partners/whatsapp/
description: "This article outlines the partnership between Braze and WhatsApp, one of the world's most popular instant messaging platforms."
page_type: partner
search_tag: Partner
page_order: 0
hidden: true  
---

# WhatsApp Overview

> [WhatsApp](https://www.whatsapp.com/) Business messaging is a popular peer-to-peer messaging platform used across the world offering conversation based messaging for businesses.	

{% alert important %}
Support for the WhatsApp channel is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Prerequisites

Acknowledge the following before proceeding with integration:

- **Opt-in policy:** WhatsApp requires businesses to have customers opt-in to messaging.
- **WhatsApp content rules:** WhatsApp has several [content rules](https://www.whatsapp.com/legal/commerce-policy?l=et) that need to be followed.
- **24-hour conversation limits:** After a user or business sends an initial templated message, a 24-hour window will occur where the two parties can message back and forth. 
- **Initiating conversation:** Users can initiate a conversation at any point. A business can only initiate a conversation through an approved message template.
- **Account limitations:** You can set up multiple WhatsApp numbers in your Braze app group, but only one WhatsApp Business Account. Additionally, each WhatsApp Business Account can only hold [one third-party integration](https://developers.facebook.com/docs/whatsapp/embedded-signup/faq#faq_194614375799047). 
<br><br>

| Requirement| Description|
| ---| --- |
| Meta Business Manager account | A Meta Business account is required to leverage this messaging channel. |
| WhatsApp Business account | A WhatsApp Business account is required to leverage this messaging channel. |
| WhatsApp phone number | A WhatsApp phone number is required to leverage this messaging channel. | 
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Connect WhatsApp Messenger to Braze

In Braze, go to the **Technology Partners** section and then search **WhatsApp**. On the WhatsApp partner page, select **Login with Facebook** to start the integration process.

![][1]{: style="max-width:70%;"}

### Step 2: WhatsApp setup
Next, you will be prompted by Braze's setup wizard. Within this flow, you will:
1. Create or select your Meta and WhatsApp Business accounts.
2. Create your WhatsApp Business profile.
3. Verify your WhatsApp Business number.<br><br>

	![][2]{: style="max-width:100%;"}

Once the setup is complete, a dedicated WhatsApp subscription group will be created for your users.

### Step 3: Create WhatsApp templates

Only approved WhatsApp message templates can be used to initiate conversations with customers. WhatsApp templates can be built in the [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343).

1. **Navigate to the template manager**<br>
In the Meta Business Manager, under **Account Tools**, select **Message Templates**.
Next, select **Create Templates**.<br><br>![][3]{: style="max-width:100%;"}<br><br>
2. **Message settings**<br>
In the new message template wizard, select the category of your message, name your template, and choose the languages you want to support. You can delete or add more languages later.<br><br> 
	The available message template categories include the following:
	- Transactional: Send account updates, order updates, alerts, and more to share important information.
	- Marketing: Send promotional offers, product announcements, and more to increase awareness and engagement.
	- One-time passwords: Send codes that allow your customers to access their accounts.<br><br> 
	![][4]{: style="max-width:100%;"}<br><br>
3. **Edit template**<br>
Next, you will be prompted to create your message template. <br><br>Here, you can provide a text or media header, the text body, a message footer, and buttons. A preview of your message will be shown on the right. <br><br>While Meta does not support Liquid, you can template in variables that can be later replaced in Braze for Liquid variables. Select the **+ Add variable** button to do so.<br><br>![][5]{: style="max-width:100%;"}<br><br>Once you have completed your template, press **Submit**. 

#### Template approval time

WhatsApp may take up to 24 hours to get approved. You can check on the approval status of your message on the **Message Template** page in the Meta Business Manager.

### Step 4: Create a WhatsApp campaign

Once WhatsApp templates have been approved, you can move over to the dashboard to build out a [WhatsApp Canvas or campaign]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/create/). 


[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp2.gif %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp2.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp3.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp4.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp5.png %} 
