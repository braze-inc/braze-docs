---
nav_title: Email sign-up with discount
article_title: Email Sign-up with Discount
alias: "/email_discount/"
page_order: 3
description: "This reference page covers how to use the in-app message drag-and-drop editor to build an email sign-up form that offers a discount for new subscribers."
---

# Email sign-up with discount

> Use the in-app message drag-and-drop editor to build an email sign-up form that offers a discount for new subscribers.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Creating an email sign-up form with a discount

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select **Email sign-up with welcome discount** for your template, then select **Build message**. This template is supported for both mobile apps and web browsers.

![The in-app message editor with the template for an email sign-up form with discount.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})

### Step 2: Set up your message styles

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Step 3: Customize your email sign-up component

To get started building your email sign-up form, select the email capture element in the editor. By default, collected email addresses will have the global subscription group **Subscribed**. To opt in users to specific subscription groups, refer to [Updating email subscription states]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

You can customize the placeholder text and label text of the email capture element.

![The in-app message editor with a side menu for customizing the email capture element.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})

#### Email validation

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Step 4: Add disclaimer language (optional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Step 5: Style your message

Customize the look and feel of your sign-up form and discount using the drag-and-drop [in-app message components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analyzing the results

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Best practices

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



