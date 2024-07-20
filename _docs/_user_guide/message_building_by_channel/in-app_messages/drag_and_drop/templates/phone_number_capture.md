---
nav_title: SMS and WhatsApp Sign-up Form
article_title: SMS and WhatsApp Sign-up Form
alias: "/phone_number_capture/"
description: "This reference page covers how to create an SMS and WhatsApp sign-up form with the in-app message drag-and-drop editor."
---

# SMS and WhatsApp sign-up form

> The SMS and WhatsApp sign-up forms are templates available in the drag-and-drop editor for in-app messages. Use these templates to collect users' phone numbers and grow your SMS and WhatsApp subscription groups.

![Three examples of in-app messages created using the phone sign-up form template.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

## SDK requirements

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. See the [Prerequisites]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites) section of [Creating an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) for more details and nuances to be aware of.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK versions for text links

If you want to include text links that do not dismiss the message, users must be on the following minimum SDK versions:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
If you include a link in your in-app message that redirects to a URL and the end user is not on the minimum SDK versions specified, clicking on the link will close the message and the user will not be able to return to the message to submit the form.
{% endalert %}

## Creating a phone number sign-up form

When creating a drag-and-drop in-app message, select **SMS sign-up** or **WhatsApp sign-up** for your template.

![Modal to select SMS sign-up or WhatsApp sign-up as a template when creating an in-app message.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:70%"}

These templates are supported for both mobile apps and web browsers.

### Step 1: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

![Workflow of uploading and selecting a custom font.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Step 2: Customize your phone number input component

To get started building your sign-up form, select the phone number input component in the editor.

![Preview area when creating a sign-up form with the phone number input component selected.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:40%"}

From the side menu, specify which subscription group this template will collect phone numbers for. To adhere to compliance best practices, you can only collect consent to one subscription group per phone number sign-up form. However, if desired, you can use multiple forms to collect consent for other subscription groups.

![Subscription group dropdown with a subscription group selected.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

By default, we collect numbers globally, however you can limit the number of countries to collect numbers from. This is helpful if you intend to only message users who have phone numbers in specific countries, and can assist with list cleanliness. To do so, turn off **Collect numbers from all countries** and use the dropdown to select specific countries. Your users will only be able to select countries that you have explicitly added.

![Countries dropdown to select the countries from which you want to collect numbers.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Invalid phone numbers

If your users input a phone number that includes any unaccepted special characters, they will see a generic error indicator that is not customizable and will not be able to submit the form. You can view the error behavior in the **Preview & Test** tab and on your test device. Refer to this article to learn [how Braze formats phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Step 3: Add disclaimer language (for SMS sign-up forms)

For SMS sign-up forms, it's important to clearly communicate the type of SMS you will be sending. Make sure your list growth is compliant by including the following information in your form:

- Description of the types of SMS messages your customers can expect (cart reminders, promotions and deals, appointment reminders, etc.). You don't need to list every use case, but you should provide a description of the types of messages your brand will send.
- Note that consent is not a condition of any purchase (if applicable).
- Message frequency and reminder that message and data rates apply. If you don't know the exact message frequency, you can say that frequency may vary.
- Links to your Terms & Conditions and SMS Privacy Policy.
- Reminder of help and opt-out keywords (HELP for help; STOP to cancel).

We have provided a placeholder disclaimer in the template solely as an example—it does not constitute legal advice and should not be relied upon for compliance purposes. It’s important to work with your legal team to develop language that is tailored to your specific brand.

{% alert note %}
This documentation is not intended to provide, nor may it be relied fully upon, as providing legal advise.
{% endalert %}

For more information about SMS compliance, see [SMS Laws and Regulations]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

### Step 4: Style your message

You can customize the look and feel of your message using the drag-and-drop [in-app message components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components).

## Reporting

After your campaign has launched, you can analyze results in real-time to see how many users have engaged with your campaign. To see how many users have opted into the subscription group, you can [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

![In-App Message Performance panel showing clicks for each link in the in-app message.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


