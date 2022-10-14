---
nav_title: WhatsApp
article_title: WhatsApp
alias: /partners/whatsapp/
description: "This article outlines the partnership between Braze and WhatsApp, one of the world’s most popular instant messaging platforms."
page_type: partner
search_tag: Partner

---

# WhatsApp

> [WhatsApp](https://www.whatsapp.com/) Business messagins is a poprular peer-to-peer messaging platform used across the world offering conversation based messaging for businesses.	

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Opt-in policy | | | Whats App requires businesses to have customers opt-in to messagin
| https://www.whatsapp.com/legal/commerce-policy?l=et | | | Messaging rules |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


WhatsApp Rules 
24 hour conversation limits 
After a user or business sends an initial message, a 24 window occurs where the two parties can message back and forth. 
Users can initiate a conversation at any point. A business can only initiate a conversation via an approved message template. 


WhatsApp Subscription group
WhatsApp users need a subscription group. These operate similar and use same APIs as email/sms subscription groups


## Integration

### Step 1: Connect WhatsApp Messenger to Braze

In Braze, go to the **Technology Partners** section and then search **WhatsApp**. On the WhatsApp partner page, select **Login with Facebook** to start the integration process.

![Data Import and Web SDK Installation section of the Shopify partner page in Braze.][2]{: style="max-width:80%;"}

### Step 2: WhatsApp setup
Next, you will be prompted by Braze's setup wizard. Within this flow you will:
1. Create or select your Meta and WhatsApp Business accounts
2. Create your WhatsApp Business profile.
3. Verify your WhatsApp Business number. 

User import  (if customer has this audience) 
Download from Meta 
Upload as per Braze instructions 

### Step 3: Create WhatsApp templates

Only approved WhatsApp message templates can be used to initiate conversations with customers. Customers on the otherhand can initiate conversations at any point.  

WhatsApp templates can be built in the [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343).

<!--
	Does this mean they are set emplates or you can make any tempalte, but they need to get approved?
Must be approved by WhatsApp team before sent to customer,
-->

### Step 4: Use WhatsApp templates in Braze/ Using this integration

Templates built and approved in the Meta Business Manager, will be available in Braze under **Templates & Media**. To use them in your campaign select the template

Replace WhatsApp Placeholder variabled with Liquid and add any images from the media library or upload them manually. 

Note that any greyed out words cannot be edited as they are part of the approved WhatsApp template.

## Maintaining your user list

Maintaining your user list (opt in/opt out) 
Subscription status endpoints to manage WhatsApp subscriptions 
Generating opt ins 
HTML phone number capture
Canvas trigger to update user profile subscription state 

## Frequently asked questions

WhatsApp FAQ
How do I affect my WhatsApp send quality? 
How do you build up? 
Quality Rating - what does this affect?
How do I manage language templates between WhatsApp and Braze? 
How can I manage inbound support questions? 
What countries can I access on WhatsApp?
All countries 

