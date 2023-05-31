---
nav_title: Phone Number Capture
article_title: Phone Number Capture
permalink: "/phone_number_capture/"
description: "This reference page covers how to create a phone number capture form with the in-app message drag & drop editor."
layout: dev_guide
---

# Phone number capture form

> Learn how to create an in-app message to collect users' phone numbers capture  form.

The phone number capture form is a template available in the Drag & Drop Editor for in-app messages. Use this template to collect users' phone numbers and grow your subscription groups.

![][img1]{: style="max-width:35%"}

## SDK requirements

In addition to the [minimum SDK versions][1] required to receive messages built using the Drag & Drop Editor, users will need to be on the following minimum SDK versions to include text links that do not dismiss the message:

{% sdk_min_versions swift:6.2.0 android:0.0.0 %}

## Creating a phone number capture form

When creating a drag-and-drop in-app message, select **Phone number capture form** for your template.

![][img2]{: style="max-width:30%"}

This template is supported for both mobile apps and web browsers.

### Step 1: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 2: Customize your phone number capture component

To get started building your phone number capture form, select the phone number input element in the editor.

![][img3]{: style="max-width:40%"}

From the side menu, specify which subscription group this template will collect phone numbers for. As a best practice, you should use a new form to get the user’s consent for each subscription group.

![][img4]{: style="max-width:40%"}

By default, we collect numbers globally, however you can limit the number of countries to collect numbers from. To do so, turn off **Collect numbers from all countries** and use the dropdown to select specific countries. Your users will only be able to select countries that you have explicitly added.

![][img5]{: style="max-width:40%"}

#### Invalid phone numbers

If your users input a phone number that includes any unaccepted special characters, they will see a generic error and will not be able to submit the form. The error message text cannot be customized. You can view the error behavior in the **Preview & Test** tab and on your test device. Refer to this article to learn [how Braze formats phone numbers][2].

### Step 3: Add disclaimer language

Be sure to include opt-in language and links to your brand’s privacy policy and terms and conditions in your message. We have provided a placeholder disclaimer in the template solely as an example—it does not constitute [legal advice][4] and should not be relied upon for compliance purposes. Work with your legal team to develop language that is tailored to your specific brand.

### Step 4: Style your message

You can customize the look and feel of your message using the Drag & Drop Editor [in-app message components][3].

## Reporting

Once your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, refer to _______.

> img


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}