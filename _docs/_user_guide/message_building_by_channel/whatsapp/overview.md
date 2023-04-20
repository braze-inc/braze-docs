---
nav_title: Overview
article_title: WhatsApp Overview
alias: /partners/whatsapp/
description: "This article provides an overview of the Braze WhatsApp channel, prerequisties, guidance on getting the integration started."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
---

# WhatsApp Overview

> [WhatsApp](https://www.whatsapp.com/) Business messaging is a popular peer-to-peer messaging platform used across the world offering conversation based messaging for businesses.	

## Prerequisites

Acknowledge the following before proceeding with integration:

- **Opt-in policy:** WhatsApp requires businesses to have customers opt-in to messaging.
- **WhatsApp content rules:** WhatsApp has several [content rules](https://www.whatsapp.com/legal/commerce-policy?l=en) that need to be followed.
- **Compliance:** Comply with all applicable Braze and Meta documentation and any applicable [Meta policies](https://www.whatsapp.com/legal/?lang=en).
- **24-hour conversation limits:** After a business sends an initial templated message or a user sends a message, a 24-hour window will occur where the two parties can message back and forth. 
- **Initiating conversation:** Users can initiate a conversation at any point. A business can only initiate a conversation through an approved message template.
- **Account limitations:** Each Braze app group can hold one WhatsApp Business account, subscription group, and phone number. Additionally, each WhatsApp Business account can only hold [one third-party integration](https://developers.facebook.com/docs/whatsapp/embedded-signup/faq#faq_194614375799047). 
<br><br>

| Requirement| Description|
| ---| --- |
| Meta Business Manager account | A Meta Business account is required to leverage this messaging channel. |
| WhatsApp Business account | A WhatsApp Business account is required to leverage this messaging channel. |
| WhatsApp phone number | You must acquire a phone number that meets [WhatsApp's requirements](https://developers.facebook.com/docs/whatsapp/phone-numbers/) for use of the messaging channel.  | 
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Connect WhatsApp Messenger to Braze

In Braze, go to the **Technology Partners** section and then search **WhatsApp**. On the WhatsApp partner page, select **Login with Facebook** to start the integration process.

![][1]{: style="max-width:70%;"}

It is likely that you already have at least one existing Meta Business account at your company. If that is the case, select the one that you would like your WhatsApp Business account to live within. User permissions and business verification for WhatsApp will be controlled centrally in your Meta Business account.

### Step 2: WhatsApp setup
Next, you will be prompted by Braze's setup wizard. Within this flow, you will:
1. Create or select your Meta and WhatsApp Business accounts.
2. Create your WhatsApp Business profile.
3. Verify your WhatsApp Business number.<br><br>

	![][2]{: style="max-width:100%;"}

{% alert note %}
WhatsApp Business Accounts (WABA) cannot be shared with multiple Business Solution Providers. You will need a specific WABA for each Braze app group.
{% endalert %}	

Once the setup is complete, a dedicated WhatsApp subscription group will be created for your users.

### Step 3: Create WhatsApp templates

Only approved WhatsApp message templates can be used to initiate conversations with customers. WhatsApp templates can be built in the [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343).

1. **Navigate to the [template manager](https://business.facebook.com/wa/manage/message-templates)**<br>
In the Meta Business Manager, under **Account Tools**, select **Message Templates**.
Next, select **Create Templates**.<br><br>![][3]{: style="max-width:100%;"}<br><br>
2. **Message settings**<br>
In the new message template wizard, select the category of your message, name your template, and choose the languages you want to support. You can delete or add more languages later.<br><br> 
	The available message template categories include the following:
	- Marketing: Send promotional offers, product announcements, and more to increase awareness and engagement
	- Utility: Send account updates, order updates, alerts, and more to share important information
	- Authentication: Send codes that allow your customers to access their accounts<br><br> 
	![][4]{: style="max-width:100%;"}<br><br>
3. **Edit template**<br>
Next, you will be prompted to create your message template. <br><br>Here, you can provide a text or media header, the text body, a message footer, and buttons. Note that video and document headers are not currently available, and headers must be of either text or image type. A preview of your message will be shown on the right. <br><br>While Meta does not support Liquid, you can template in variables that can be later replaced in Braze for Liquid variables. Select the **+ Add variable** button to do so.<br><br>![][5]{: style="max-width:100%;"}<br><br>Once you have completed your template, press **Submit**. 

#### Template approval time

You can check the approval status of your message template in either the **Message Template** page in the Meta Business Manager, or when creating a campaign or Canvas in Braze. Additionally, you can be notified by email by the WhatsApp team depending on your notification permissions. 

### Step 4: Create a WhatsApp campaign

Once WhatsApp templates have been approved, you can move over to the dashboard to build out a [WhatsApp Canvas or campaign]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/create/). 

## Next steps

After completing the integration, we recommend completing the two following Meta processes:
- [Business Verification](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- You may already have business verification if you’ve used an existing Meta Business Manager. 
- [Official Business Account](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

We also recommend reading about [user phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) and adding any users who will need access to create message [templates at your organization](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).


[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp2.gif %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp2.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp3.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp4.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp5.png %} 
