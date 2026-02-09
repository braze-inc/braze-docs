---
nav_title: Multiple business accounts
article_title: Multiple WhatsApp Business Accounts and Phone Numbers
page_order: 3
description: "This reference article covers the steps to add WhatsApp Business accounts and phone numbers."
page_type: reference
channel:
  - WhatsApp
---

# Multiple WhatsApp Business accounts and phone numbers

> You can add multiple WhatsApp Business accounts and subscription groups (and phone numbers) to each workspace. <br><br>Each subscription group is connected to one unique phone number, so you can't connect the same phone number to multiple subscription groups or connect multiple phone numbers to a subscription group.

## Multiple WhatsApp Business accounts 

Having multiple WhatsApp Business accounts is useful if you want to send WhatsApp messages to users in a Braze workspace that has multiple brands. This is because each business account operates separately within WhatsApp and has its own phone number, message template, and quality rating.

Business accounts that are nested within the same Meta Business Manager will also share user access permission management and catalogs (not yet supported on Braze).

![Diagram of the Braze and WhatsApp ecosystem, showing how workspaces and WhatsApp Business accounts connect to each other: you can connect one subscription group to one phone number, multiple WhatsApp Business accounts to one workspace, and one workspace to multiple Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Adding a WhatsApp Business account

You can add up to 10 WhatsApp Business accounts per workspace. The business accounts can be nested in different Meta Business Managers. To add an account:

1. Go to **Technology Partners** > **WhatsApp** and select **Add WhatsApp Business Account**. 

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Go through the sign-up workflow. For a detailed step-by-step walkthrough, refer to [WhatsApp embedded signup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
Your phone number must follow all the requirements of any WhatsApp phone number, including not being registered to any other WhatsApp accounts. 
{% endalert %}

## Multiple subscription groups and phone numbers

Message templates are shared among all phone numbers in the same WhatsApp Business account. For details about WhatsApp subscription groups, view [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Each WhatsApp phone number will appear as a separate WhatsApp chat to users. Each phone number within a WhatsApp Business account operates independently from each other, so they can have the same or different values for the following: 
- Display name 
- Status 
- Quality rating 
- Messaging limit 

### Adding a subscription group and phone number

You can add up to 20 subscription groups (and sending phone numbers) per WhatsApp Business account. To add a subscription group and phone number:

1. Go to **Technology Partners** > **WhatsApp** and select **Add Subscription Group and Number**.

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Go through the sign-up workflow. <br><br> In the **Select your WhatsApp Business Account** step, select your existing WhatsApp Business account and add a new phone number. This number must follow all the requirements of any WhatsApp phone number, including not being registered to any other WhatsApp accounts.

### Removing a subscription group and phone number 

1. Go **Audience** > **Subscriptions** and archive the subscription group.
2. Go to your Meta Business manager and delete the phone number.
