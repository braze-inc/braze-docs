---
nav_title: Messaging Users
article_title: Messaging Users
description: "This reference article covers how Braze will go about handling user messages."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# User messages

> WhatsApp is a two-way communication channel. Not only can your brand send users messages, but they can engage in conversations using templated campaigns and Canvases. There are various ways to do this, including WhatsApp Quick Replies and trigger words. Quick Reply calls-to-action (CTAs) are a great way to encourage user engagement with your WhatsApp messaging.

## Action-based triggers 

Both campaigns and Canvases can start, branch, and have mid-journey changes from an inbound WhatsApp message (a user messaging your WhatsApp),  such as a trigger word. 

Ensure that your trigger word matches what you are expecting from users.

**Things to know:**
- Each letter of your trigger word must be capitalized when configured. Braze does not require inbound trigger words sent by users to be capitalized. For example, messaging "jOin2023" will still trigger the Canvas or campaign.
- If no trigger word is specified on the entry schedule action-based trigger, the campaign or Canvas will run for ALL inbound WhatsApp messages. This includes messages that have matched phrases across active campaigns and Canvases, in which case the user will receive two WhatsApp messages.

{% tabs %}
{% tab Campaign %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## Unrecognized responses

We recommend that you include an option for unrecognized responses on interactive Canvases. This guides users to understand what are available prompts and sets expectations for the channel. Expectation management can be especially helpful if you have WhatsApp channels with live agent chat. 
- In the action step, after creating the action groups for the custom filter phrases, add an additional action group for "Send WhatsApp message", but **do not check Where the message body**. This will catch all unrecognized user responses, similar to an "else" clause. 
- We recommend following up with a WhatsApp message informing the user that this channel is not manned and guiding them to a support channel if needed. 

## Quick replies 

![Phone screen showing a call to action button will reply the text of the button clicked.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Quick replies appear as clickable button options within the conversation but act as if a user replied with text. Braze then processes these as inbound messages, and can send back set responses based on the button clicked. Use the "Inbound WhatsApp message action" step when creating and filtering responses from your users.

![A WhatsApp message showing text and three call to action buttons.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configure the Quick Reply experiences in Canvas

#### Step 1: Build out CTAs

First, build out your Quick Reply CTAs in the [WhatsApp Message Template Manager](https://business.facebook.com/wa/manage/message-templates/) within a message template. 

![The WhatsApp message template manager UI showing how to create a CTA button, providing the button type (custom) and the button text.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Once your template has been submitted and approved by WhatsApp, you can use it to build a Canvas within Braze. 

{% alert tip %}
You can build the Canvas before receiving the approval on your message template. 
{% endalert %}

#### Step 2: Build your Canvas

Next, build a Canvas with a message step that includes your created template. 

![]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Create an action step that follows the message step. Create one group per quick reply option in this action step.

![A Canvas where the evaluation action is "send a whatsapp inbound message".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

For each quick reply option group, specify the exact text as the button you are matching. Note that the keywords must be in uppercase. 

![A Canvas step where the action "send a whatsapp inbound message" is set to send when a specific message body is received.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

If you would like a default response for users who respond to the message with text instead of quick replies, create an additional group with no matching message body.

Continue building the Canvas as you would otherwise from this point forward.

### Responses

You will most likely want a reply message for each response. We recommend having a catch-all option for responses outside the bounds of quick replies (such as for customers who respond with a general message rather than a predetermined prompt). For example, "We’re sorry, we didn’t recognize your response. For support issues, please message <support channel>."

![A Canvas built out showing the responses for each call-to-action button.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Note that you can use any subsequent actions that the Braze Canvas offers, such as messages in response, user profile updates, or Braze-to-Braze webhooks. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %} 
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %} 
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %} 
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %} 
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %} 
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %} 
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %} 
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
