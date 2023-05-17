---
nav_title: User Messages
article_title: User Messages
description: "This reference article covers how Braze will go about handling user messages."
page_type: reference
channel:
  - WhatsApp

---

# User messages

> WhatsApp is a two-way communication channel. Not only can your brand send users messages, but they can engage in conversations using templated campaigns and Canvases. There are various ways to do this, including WhatsApp Quick Replies and trigger words. 

## Action-based triggers 

Both campaigns and Canvases can start, branch, and have mid-journey changes from an inbound WhatsApp message (a user messaging your WhatsApp), i.e., a trigger word. 

Ensure that your trigger word matches what you are expecting from users. 

### Campaign: 

![][4]

![][3]

{% alert note %}
Text must be in full caps when configured, but Braze will not hold the case-sensitive property (i.e., customers can text lowercase, uppercase, etc., which will still work).
{% endalert %} 

### Canvas:

![][2]

![][1]

If no trigger word is specified on the entry schedule action-based trigger, the campaign or canvas will run for ALL inbound WhatsApp messages. This includes messages that have matched phrases across active campaigns and Canvases, in which case the user will receive two WhatsApp messages.  

## Unrecognized responses

We recommend that you include an option for unrecognized responses on interactive Canvases. This guides users to understand what are available prompts and sets expectations for the channel. Expectation management can be especially helpful if you have WhatsApp channels with live agent chat. 

In the action step, after creating the action groups for the custom filter phrases, add an additional action group for “Send WhatsApp message”, but do not check **Where the message body**. This will catch all unrecognized user responses, similar to an “else” clause. 

We recommend following up with a WhatsApp message informing the user that this channel is not manned and guiding them to a support channel if needed. 

## Quick replies 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 
