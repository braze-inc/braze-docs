---
nav_title: Using codes
article_title: Using promotion codes
page_order: 0.2
description: "Learn how to use promotion codes and view usage for your campaigns and Canvases."
---

# Using promotion codes

> Learn how to use promotion codes and view usage for your campaigns and Canvases.

## Prerequisites

Before you can use promotion codes, you'll need to [create a promotion code list]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Using promotion codes

To send a promotion code in a message, select **Copy Snippet** next to the promotion code list [you previously created](#create).

![An option to copy the snippet to paste into your message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Paste the code snippets into one of your messages in Braze, then use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) to insert one of the unique promotion codes from your list. That code will be marked as sent, ensuring no other message sends the same code.

![An example message "Treat yourself to something nice this spring with our exclusive offer" followed by the code snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Across canvas steps

When a code snippet is used in a campaign or Canvas with multichannel messages, each user receives a unique code. In a Canvas with multiple steps that reference promotion codes, a user gets a new code for every step they enter.

To assign one promotion code in a Canvas and reuse it across steps:

1. Assign the promotion code as a custom attribute in the first step (User Update).
2. Use Liquid in later steps to reference that custom attribute instead of generating a new code.

When a user qualifies for a code across multiple channels, they receive the same code in each channel. For example, if they get messages by email and push, the same code is sent to both. Reporting also reflects a single code.

{% alert note %}
If no promotion codes are available, test or live messages that rely on codes will not send.
{% endalert %}

### In-app message campaigns {#promotion-codes-iam-campaigns}

{% alert important %}
Using promotion codes in in-app message campaigns is currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

After creating an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), you can insert a [promotion code list snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) into your in-app message message body. Promotion codes in in-app messages will be deducted and used only when a user triggers the display of the in-app message.

### Test messages

Test sends and seed group email sends will use up promotion codes unless requested otherwise. Contact your Braze account manager to update this feature behavior so promotion codes aren't used during test sends and seed group email sends.

## Saving promotion codes to user profiles {#save-to-profile}

To reference the same promotion code in subsequent messages, the code must be saved to the user profile as a custom attribute. This can be done through a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) that assigns the discount code to a custom attribute, like “Promo Code”, directly before a Message step.

First, select the following for each field in the User Update step:

- **Attribute Name:** Promo Code
- **Action:** Update
- **Key Value:** The promotion code's Liquid code snippet, such as {% raw %}`{% promotion('spring25') %}`{% endraw %}

Second, add the custom attribute (in this example, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) to a message. The discount code will be templated in.

## Viewing promotion code usage

You can find the remaining code count in the **Remaining** column of the promotion code list on the **Promotion Codes** page.

![An example of a promotion code with unused codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

This code count can also be found when revisiting a pre-existing promotion code list page. You can also export unused codes as a CSV file. 

![A promotion code named "Black Friday Sale" with 992 remaining codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}
