---
nav_title: SMS, RCS, and WhatsApp sign-up form
article_title: SMS, RCS, and WhatsApp Sign-up Form
alias: "/phone_number_capture/"
page_order: 1
description: "This page covers how to create an SMS, RCS, and WhatsApp sign-up form with the in-app message drag-and-drop editor."
---

# SMS, RCS, and WhatsApp sign-up form

> The SMS, RCS, and WhatsApp sign-up forms are templates available in the drag-and-drop editor for in-app messages. Use these templates to collect users' phone numbers and grow your SMS, MMS, RCS, and WhatsApp subscription groups.

![Three examples of in-app messages created using the phone sign-up form template.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Creating a phone number sign-up form

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select **SMS sign-up** (this accomodates for RCS sign-up) or **WhatsApp sign-up** for your template, then select **Build message**. These templates are supported for both mobile apps and web browsers.

![Modal to select SMS sign-up or WhatsApp sign-up as a template when creating an in-app message.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Step 2: Set up your message styles

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Workflow of uploading and selecting a custom font.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Step 3: Customize your phone number input component

To get started building your sign-up form, select the phone number input component in the editor.

![Preview area when creating a sign-up form with the phone number input component selected.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

From the side menu, specify which subscription group this template will collect phone numbers for. To adhere to compliance best practices, you can only collect consent to one subscription group per phone number sign-up form. However, if desired, you can use multiple forms to collect consent for other subscription groups.

![Subscription group dropdown with a subscription group selected.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

By default, we collect numbers globally, however you can limit the number of countries to collect numbers from. This is helpful if you intend to only message users who have phone numbers in specific countries, and can assist with list cleanliness. To do so, turn off **Collect numbers from all countries** and use the dropdown to select specific countries. Your users will only be able to select countries that you have explicitly added.

![Countries dropdown to select the countries from which you want to collect numbers.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Invalid phone numbers

If your users input a phone number that includes any unaccepted special characters, they will see a generic error indicator that is not customizable and will not be able to submit the form. You can view the error behavior in the **Preview & Test** tab and on your test device. Refer to this article to learn [how Braze formats phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Step 4: Add disclaimer language (for SMS and RCS sign-up forms)

For SMS and RCS sign-up forms, it's important to clearly communicate the type of SMS or RCS you will be sending. Make sure your list growth is compliant by including the following information in your form:

- Description of the types of SMS and RCS messages your customers can expect (cart reminders, promotions and deals, appointment reminders, etc.). You don't need to list every use case, but you should provide a description of the types of messages your brand will send.
- Note that consent is not a condition of any purchase (if applicable).
- Message frequency and reminder that message and data rates apply. If you don't know the exact message frequency, you can say that frequency may vary.
- Links to your Terms & Conditions and SMS and RCS Privacy Policy.
- Reminder of help and opt-out keywords (HELP for help; STOP to cancel).

We have provided a placeholder disclaimer in the template solely as an example—it does not constitute legal advice and should not be relied upon for compliance purposes. It’s important to work with your legal team to develop language that is tailored to your specific brand.

{% alert note %}
This documentation is not intended to provide, nor may it be relied fully upon, as providing legal advise.
{% endalert %}

For more information about SMS and RCS compliance, see [Laws and regulations for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Step 5: Style your message

Customize the look and feel of your message using the drag-and-drop [in-app message components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analyzing the results

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![In-App Message Performance panel showing clicks for each link in the in-app message.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


