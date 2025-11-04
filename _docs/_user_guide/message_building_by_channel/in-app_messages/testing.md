---
nav_title: Testing
article_title: Testing In-App Messages
page_order: 4.5
description: "This reference article explains the value of testing your in-app messages, how to test them, as well as a checklist of things to consider before sending."
channel:
  - in-app messages
  
---

# In-app message testing

> It is extremely important to always test your in-app messages before sending your campaigns. Our preview and testing capabilities offer two ways to take a look at your in-app messages. You can preview your message, to help you visualize as you compose it, as well as send a test message to your or a specific user's device. We recommend you take advantage of both.

## Preview

You can preview your in-app message as you compose it. This should help you visualize what your final message will look like from your user's perspective.

{% alert warning %}
In **Preview**, the view of your message might not be identical to its actual rendering on the user's device. We always recommend sending a test message to a device to ensure that your media, copy, personalization, and custom attributes generate correctly.
{% endalert %}

### In-app message generation preview

Preview what your message will look like to a random user, a specific user, or a customized user—the latter two are especially useful if your message contains personalization or multiple languages. You can also preview messages for either mobile devices or tablets to get a better idea of what users will experience.

![Compose tab when building an in-app message showing the preview of what the message will look like. A user is not selected, so the Liquid added in the body section displays as is.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze has three generations of in-app messages available. You can fine-tune to which devices your messages should be sent, based on which Generation they support.

![Switching between generations when previewing an in-app message.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Test

{% alert warning %}
To send a test to either [Content Test Groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, push must be enabled on your test devices before sending. <br><br>For example, you must have push enabled on your iOS device in order to tap the notification before the test message displays.
{% endalert %}

### Preview message as user

You can also preview messages from the **Test** tab, as though you were a user. You can select a specific user, a random user, or create a custom user.

![Test tab when building an in-app message. "Preview message as user" is set to "Custom User" with available profile fields appearing as configurable options.]({% image_buster /assets/img/iam-user-preview.png %})

{% alert important %}
Test sends may result in more than one in-app message being sent to each recipient. 
{% endalert %}

### Test checklist

- Do the images and media show up and act as expected?
- Does the Liquid function as expected? Have you accounted for a [default attribute value]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
- Do your buttons direct the user where they should go?

## Accessibility scanner

To support accessibility best practices, Braze automatically scans the content of in-app messages created using the traditional HTML editor against accessibility standards. This scanner helps identify content that may not meet Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) standards. WCAG is a set of internationally recognized technical standards developed by the World Wide Web Consortium (W3C) to make web content more accessible to people with disabilities.

![Accessibility scan results]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
The in-app message accessibility scanner only runs on messages built with custom HTML. 
{% endalert %}

### How it works

The scanner runs automatically on custom HTML messages and evaluates your entire HTML message against the full [WCAG 2.1 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). For each flagged issue, it shows:

- The specific HTML element involved
- A description of the accessibility issue
- A link to additional context or remediation guidance

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}





