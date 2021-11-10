---
nav_title: Testing
article_title: Testing In-App Messages
page_order: 3
description: "It is extremely important to always test your in-app messages before sending your campaigns. Our preview and testing capabilities offer two ways to take a look at your in-app messages."
channel:
  - in-app messages
  
---

# Testing

It is extremely important to always test your in-app messages before sending your campaigns. Our preview and testing capabilities offer two ways to take a look at your in-app messages. You can preview your message, to help you visualize as you compose it, as well as send a test message to your or a specific user's device. We recommend you take advantage of both.

## Preview

You can preview your in-app message as you compose it. This should help you visualize what your final message will look like from your user's perspective.

{% alert warning %}
In __Preview__, the view of your message might not be identical to its actual rendering on the user's device. We always recommend sending a test message to a device to ensure that your media, copy, personalization, and custom attributes generate correctly.
{% endalert %}

### In-app message generation preview

Preview what your message will look like to a random user, a specific user, or a customized user - the latter two are especially useful if your message contains personalization or multiple languages. You can also preview messages for either mobile devices or tablets to get a better idea of what users will experience.

![In-App_Message_Preview][1]

Braze has three generations of in-app messages available. You can fine-tune to which devices your messages should be sent, based on which Generation they support.

![In-App_Messages_Generations][2]{: height="50%" width="50%"}

## Test

{% alert warning %}
  To send a test to either [Content Test Groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, push must be enabled on your test devices before sending.
{% endalert %}

### Preview message as user

You can also preview messages from the **Test** tab, as though you were a user. You can select a specific user, a random user, or create a custom user.

![Custom_User_Preview][3]

### Test checklist

- Do the images and media show up and act as expected?
- Does the Liquid function as expected? Have you accounted for a [default attribute value]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
- Do your buttons direct the user where they should go?

[1]: {%image_buster /assets/img/in-app-message-preview.png %}
[2]: {% image_buster /assets/img/iam-generations.gif %}
[3]: {% image_buster /assets/img/iam-user-preview.png %}
