---
nav_title: Quick Replies
article_title: Quick Replies
description: "  "
page_type: partner
search_tag: Partner
page_order: 0
hidden: true  
---

# Two-way Messaging in Canvas using Quick Replies

WhatsApp's Quick Reply calls-to-action (CTA) are a great way to encourage user engagement with your WhatsApp messaging. Braze can process these messages and configure actions based on what the user taps. Additionally, these CTAs can reduce error in the back and forth by providing an easily clickable button, eliminating the need for your users to type out a response.

The Quick Reply CTA buttons come in as inbound messages to the Braze system. This means you'll use the "Inbound WhatsApp message" action step when creating and filtering responses from your users. 

## What is a quick reply?

Quick replies appear as clickable button options within the conversation but act as if a user replied with text. Braze processes these as inbound messages.

![][1]

## How to configure Quick Reply experiences in Canvas

Build messages with Quick reply buttons and create responses based on the end user's selections. 

## Step 1: Build out CTAs

First, build out your Quick Reply CTAs in the [WhatsApp Message Template Manager](https://business.facebook.com/wa/manage/message-templates/) within a message template. 

![][2]

Once your template has been submitted and approved by WhatsApp, you can use it to build a Canvas within Braze. 

![][3]

{% alert tip %}
You can build the Canvas before receiving the approval on your message template. 
{% endalert %}

## Step 2: Build your Canvas

Create a message step that includes the template you created. 

![][4]

Create an action step that follows the message step. You will create one group per quick reply option in this action step.

![][5]

For each quick reply option group, specify the same text as the button you are matching. Note that the keywords must be in uppercase. 

![][6]

If you would like a default response for users who respond to the message with text instead of quick replies, create an additional group with no matching message body.

![][7]

Continue building the Canvas as you would otherwise from this point forward.

## Responses

![][8]

For each of the responses, you will most likely want to have a reply message to that particular response. 

Note that you can use any subsequent actions that the Braze Canvas offers, such as messages in response, user profile updates, or Braze-to-Braze webhooks. 

We recommend having a catch-all option for responses that are outside the bounds of quick replies (i.e., for customers who respond with a general message rather than a predetermined prompt). For example, "We're sorry, we didn't recognize your response. For support issues, please message <URL of Support WhatsApp thread>."

[1]: {% image_buster /assets/img/whatsapp/whatsapp11.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp12.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp13.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp14.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp15.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp16.png %} 
[7]: {% image_buster /assets/img/whatsapp/whatsapp17.png %} 
[8]: {% image_buster /assets/img/whatsapp/whatsapp18.png %} 