---
nav_title: Email sign-up form
article_title: Email Sign-up Form
alias: "/email_capture/"
page_order: 2
description: "This page covers how to create an email sign-up form with the in-app message drag-and-drop editor."
---

# Email sign-up form

> Use the drag-and-drop email sign-up in-app message template to collect users' email addresses and grow your subscription groups.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Creating an email sign-up form

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select **Email sign-up** for your template, then select **Build message**. This template is supported for both mobile apps and web browsers.

![The in-app message editor with the template for an email capture form.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Step 2: Set up your message styles

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Step 3: Customize your email sign-up component

To get started building your email sign-up form, select the email capture element in the editor. By default, collected email addresses will have the global subscription group **Subscribed**. To opt in users to specific subscription groups, refer to [Updating email subscription states]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

You can customize the placeholder text and label text of the email capture element.

![The in-app message editor with a side menu for customizing the email capture element.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Email validation

If the user enters an email address that includes any unaccepted special characters, they will see a generic error indicator and won't be able to submit the form. This error message isn't customizable. You can view the error behavior in the **Preview & Test** tab and on your test device. Learn more about how Braze formats email addresses in [Email validation]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Step 4: Add disclaimer language (optional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Step 5: Style your message

Customize the look and feel of your sign-up form using the drag-and-drop [in-app message components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analyzing the results

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Best practices

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

