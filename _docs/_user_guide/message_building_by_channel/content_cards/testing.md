---
nav_title: Testing
article_title: Testing Content Cards
page_order: 3
description: "This reference article covers how to preview and test Content Cards, as well as some best practices."
channel:
  - content cards
  
---

# Testing

It is __extremely important__ to __always__ test your Content Cards before sending your campaigns. Our preview and testing capabilities offer two ways to take a look at your Content Cards. You can preview your message to help you visualize as you compose it, as well as send a test message to yourself or a specific user's device. We recommend you take advantage of __both__.

## Preview

You can preview your Card as you compose it. This should help you visualize what your final message will look like from your user's perspective.

In __Preview__, the view of your message might not be identical to its actual rendering on the user's device. We __always__ recommend sending a test message to a device to ensure that your media, copy, personalization, and custom attributes generate correctly.

## Test

To send a test to either [Content Test Groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, push must be enabled on your test devices before sending.

### Preview Message As User

You can also preview messages from the Test tab as though you were a user. You can select a specific user, a random user, or create a custom user.

![Custom_User_Preview][3]

### Test Checklist

- Do the images and media show up and act as expected?
- Does the Liquid function as expected? Have you accounted for a [default attribute value]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
- Do your links direct the user to where they should go?

[3]: {% image_buster /assets/img/cc-user-preview.png %}
