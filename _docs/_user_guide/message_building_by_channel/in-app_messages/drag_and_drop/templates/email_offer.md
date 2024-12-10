---
nav_title: Email Sign-up with Offer
article_title: Email Sign-up with Special Offer
alias: "/email_offer/"
page_order: 5
description: "This reference page covers how to use the in-app message drag-and-drop editor to build your email list by offering a special discount on sign-up."
---

# Email sign-up with special offer

> Use the in-app message drag-and-drop editor to build your email list by offering a special discount on sign-up.

{% multi_lang_include templates.md section='SDK requirements' %}

## Creating an email sign-up form with a special offer

When creating a drag-and-drop in-app message, select **Email sign-up with special offer** for your template and select **Build message**. This template is supported for both mobile apps and web browsers.

![The in-app message editor with the template for an email sign-up form with a special offer.][img1]

### Step 1: Set up your message styles

{% multi_lang_include templates.md section='message style' %}

### Step 2: Customize your email sign-up component

To get started building your email sign-up form, select the **Email sign-up** page, then select the email capture element in the editor. By default, collected email addresses will have the global subscription group **Subscribed**. To opt in users to specific subscription groups, refer to [Updating email subscription states]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

You can customize the placeholder text and label text of the email capture element.

![The in-app message editor with a side menu for customizing the email capture element.][img2]

#### Email validation

If the user enters an email address that includes any unaccepted special characters, they will see a generic error indicator and won't be able to submit the form. This error message isn't customizable. You can view the error behavior in the **Preview & Test** tab and on your test device. Learn more about how Braze formats email addresses in [Email validation]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Step 3: Add disclaimer language (optional)

{% multi_lang_include templates.md section='email disclaimer' %}

### Step 4: Style your message

Customize the special offer and the look and feel of your message using the drag-and-drop [in-app message components][3].

## Reporting

{% multi_lang_include templates.md section='reporting' %}

## Best practices

### Double opt-in verification

To make sure that anyone who signed up for your list meant to sign up for your list and provided the correct email address, we recommend getting a second confirmation from anyone who signed up through your email sign-up form by sending a [double opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in) flow.

One of the ways you can set this up is through Canvas Flow:

1. Build a Canvas that is action-based and set it up to trigger when a user adds an email address to Braze. Make sure that you allow for targeting users who are new to the platform (for example, by using a segment with no filters in the Canvas).
2. Create an email message step with a CTA that has a hyperlink to the {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid tag. This will change the user's email subscription state to `opted_in` when they click the button.
3. Add an [Action Paths step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. For the first path, trigger an email when a user changes their email subscription status to `opted_in`. This email should inform users that their email has been confirmed.
5. Set up the other path to exit the Canvas after the window expires.

[img1]: {% image_buster /assets/img/templates/email_capture_offer.png %} 
[img2]: {% image_buster /assets/img/templates/email_capture_field_offer.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components