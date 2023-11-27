---
nav_title: Phone Number Capture
article_title: Phone Number Capture
alias: "/phone_number_capture/"
description: "This reference page covers how to create a phone number capture form with the in-app message drag-and-drop editor."
---

# Phone number capture form

> Learn how to create an in-app message to collect users' phone numbers capture form.

The phone number capture form is a template available in the drag-and-drop editor for in-app messages. Use this template to collect users' phone numbers and grow your SMS and WhatsApp subscription groups.

![Three examples of in-app messages created using the phone capture form template.][img7]

## SDK requirements

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. See the [Prerequisites][1] section of Creating an in-app message with drag-and-drop for more details and nuances to be aware of.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK versions for text links

If you want to include text links that do not dismiss the message, users must be on the following minimum SDK versions:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
If you include a link in your in-app message that redirects to a URL and the end user is not on the minimum SDK versions specified, clicking on the link will close the message and the user will not be able to return to the message to submit the form.
{% endalert %}

## Creating a phone number capture form

When creating a drag-and-drop in-app message, select **Phone number capture form** for your template.

![Modal to select Phone number capture as a template when creating an in-app message.][img2]

This template is supported for both mobile apps and web browsers.

### Step 1: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

![Workflow of uploading and selecting a custom font.][img6]

### Step 2: Customize your phone number capture component

To get started building your phone number capture form, select the phone number input element in the editor.

![Preview area when creating a phone number capture form with the Phone Number Input element selected.][img3]{: style="max-width:40%"}

From the side menu, specify which subscription group this template will collect phone numbers for. To adhere to compliance best practices, you can only collect consent to one subscription group per phone number capture form. However, you can use multiple forms to collect consent for other subscription groups if desired.

![Subscription group dropdown with a subscription group selected.][img4]{: style="max-width:40%"}

By default, we collect numbers globally, however you can limit the number of countries to collect numbers from. This is helpful if you intend to only message users who have phone numbers in specific countries, and can assist with list cleanliness. To do so, turn off **Collect numbers from all countries** and use the dropdown to select specific countries. Your users will only be able to select countries that you have explicitly added.

![Countries dropdown to select the countries from which you want to collect numbers.][img5]{: style="max-width:40%"}

#### Invalid phone numbers

If your users input a phone number that includes any unaccepted special characters, they will see a generic error indicator that is not customizable and will not be able to submit the form. You can view the error behavior in the **Preview & Test** tab and on your test device. Refer to this article to learn [how Braze formats phone numbers][2].

### Step 3: Add disclaimer language

For SMS messaging, it's important to clearly communicate the type of SMS you will be sending. Make sure your list growth is compliant by including the following information in your form:

- Description of the types of SMS messages your customers can expect (cart reminders, promotions and deals, appointment reminders, etc.). You don't need to list every use case, but you should provide a description of the types of messages your brand will send.
- Note that consent is not a condition of any purchase (if applicable).
- Message frequency and reminder that message and data rates apply. If you don't know the exact message frequency, you can say that frequency may vary.
- Links to your Terms & Conditions and SMS Privacy Policy.
- Reminder of help and opt-out keywords (HELP for help; STOP to cancel).

We have provided a placeholder disclaimer in the template solely as an example—it does not constitute legal advice and should not be relied upon for compliance purposes. It’s important to work with your legal team to develop language that is tailored to your specific brand.

{% alert note %}
This documentation is not intended to provide, nor may it be relied fully upon, as providing legal advise.
{% endalert %}

For more information about SMS compliance, see [SMS Laws and Regulations][4].

### Step 4: Style your message

You can customize the look and feel of your message using the drag-and-drop [in-app message components][3].

## Reporting

Once your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can [create a segment][5] of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

![In-App Message Performance panel showing clicks for each link in the in-app message.][img8]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}
