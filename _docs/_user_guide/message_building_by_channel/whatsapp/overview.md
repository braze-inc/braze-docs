---
nav_title: Overview
article_title: WhatsApp Overview
alias: /partners/whatsapp/
description: "This article outlines the partnership between Braze and WhatsApp, one of the world’s most popular instant messaging platforms."
page_type: partner
search_tag: Partner
page_order: 0

---

# WhatsApp Overview

> [WhatsApp](https://www.whatsapp.com/) Business messaging is a poprular peer-to-peer messaging platform used across the world offering conversation based messaging for businesses.	

## Prerequisites

Acknowledge the following before proceeding with integration:

Facebook does not allow the usage of the Messenger platform to send marketing messages.
You will need the user’s explicit permission for messages from your page.
To send messages to users who are not test users of your Facebook App, your app will need to pass Facebook’s app review .

- **Opt-in policy**: WhatsApp requires businesses to have customers opt-in to messaging.
- **WhatsApp content rules**: WhatsApp has several [content rules](https://www.whatsapp.com/legal/commerce-policy?l=et) that need to be followed.
- **24 hour conversation limits**: After a user or business sends an initial templated message, a 24 hour window will occur where the two parties can message back and forth. 
- **Initating conversation**: Users can initiate a conversation at any point. A business can only initate a conversation through an approved message template.
<br><br>

| Requirement| Description|
| ---| --- |
| WhatsApp Business account | A WhatsApp Business account is required to leverage this messaging channel. |
| WhatsApp subcription group | A dedicated [WhatsApp subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/) is required before starting the following integration. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Connect WhatsApp Messenger to Braze

In Braze, go to the **Technology Partners** section and then search **WhatsApp**. On the WhatsApp partner page, select **Login with Facebook** to start the integration process.

![][1]{: style="max-width:80%;"}

### Step 2: WhatsApp setup
Next, you will be prompted by Braze's setup wizard. Within this flow you will:
1. Create or select your Meta and WhatsApp Business accounts
2. Create your WhatsApp Business profile.
3. Verify your WhatsApp Business number. 

![][2]{: style="max-width:80%;"}

### Step 3: Create WhatsApp templates

Only approved WhatsApp message templates can be used to initiate conversations with customers. WhatsApp templates can be built in the [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343).

{% alert note %}
WhatsApp may take up to 24 hours to get approved.
{% endalert %}

### Step 4: Create a WhatsApp campaign

Once WhatsApp templates have been approved, you can move over to the dashboard to build out a [WhatsApp Canvas or campaign]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/create/). 


[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp.gif %} 
