---
nav_title: Quick Replies
article_title: Quick Replies
description: "This reference article covers how to implement two-way messaging in Canvas using WhatsApp quick replies."
page_type: partner
search_tag: Partner
page_order: 6
channel:
  - WhatsApp
---

# Quick Replies

![Phone screen showing a call to action button will reply the text of the button clicked.][1]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

> WhatsApp's Quick Reply calls-to-action (CTAs) are a great way to encourage user engagement with your WhatsApp messaging. Braze can process these messages and configure actions based on user selection. Additionally, these CTAs can reduce back-and-forth errors by providing an easily clickable button, eliminating the need for your users to type out responses.

Quick Reply CTA buttons come in as inbound messages to the Braze system, meaning you'll use the "Inbound WhatsApp message" action step when creating and filtering responses from your users. 

## What is a quick reply?

Quick replies appear as clickable button options within the conversation but act as if a user replied with text. Braze then processes these as inbound messages and can send back set responses based on the button clicked.

![A WhatsApp message showing text and three call to action buttons.][3]{: style="max-width:50%;"}

## Configure the Quick Reply experiences in Canvas

### Step 1: Build out CTAs

First, build out your Quick Reply CTAs in the [WhatsApp Message Template Manager](https://business.facebook.com/wa/manage/message-templates/) within a message template. 

![The WhatsApp message template manager UI showing how to create a CTA button, providing the button type (custom) and the buton text.][2]{: style="max-width:80%;"}

Once your template has been submitted and approved by WhatsApp, you can use it to build a Canvas within Braze. 

{% alert tip %}
You can build the Canvas before receiving the approval on your message template. 
{% endalert %}

### Step 2: Build your Canvas

Next, build a Canvas with a message step that includes your created template. 

![][4]

Create an action step that follows the message step. Create one group per quick reply option in this action step.

![A Canvas where the evaluation action is "send a whatsapp inbound message".][5]

For each quick reply option group, specify the exact text as the button you are matching. Note that the keywords must be in uppercase. 

![A Canvas step where the action "send a whatsapp inbound message" is set to send when a specific message body is received.][6]

If you would like a default response for users who respond to the message with text instead of quick replies, create an additional group with no matching message body.

Continue building the Canvas as you would otherwise from this point forward.

## Responses

You will most likely want a reply message for each response. We recommend having a catch-all option for responses that are outside the bounds of quick replies (i.e., for customers who respond with a general message rather than a predetermined prompt). For example, "We’re sorry, we didn’t recognize your response. For support issues, please message <support channel>."

![A Canvas built out showing the responses for each call-to-action button.][8]

Note that you can use any subsequent actions that the Braze Canvas offers, such as messages in response, user profile updates, or Braze-to-Braze webhooks. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp11.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp12.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp13.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp14.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp15.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp16.png %} 
[7]: {% image_buster /assets/img/whatsapp/whatsapp17.png %} 
[8]: {% image_buster /assets/img/whatsapp/whatsapp18.png %} 