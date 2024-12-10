---
nav_title: Email Sign-up with Image
article_title: Email Sign-up with Background Image
alias: "/email_image/"
page_order: 4
description: "This reference page covers how to use the in-app message drag-and-drop editor to show off your brand style with one simple message and build your email list."
---

# Email sign-up with background image

> Use the in-app message drag-and-drop editor to show off your brand style with one simple message and build your email list.

## SDK requirements

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. See the [Prerequisites][1] section of the [Creating an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) article for more details and nuances to be aware of.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK versions for text links

If you want to include text links that do not dismiss the message, users must be on the following minimum SDK versions:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
If you include a link in your in-app message that redirects to a URL and the user isn't on the minimum SDK versions specified, clicking on the link will close the message, and the user won't be able to return to the message to submit the form.
{% endalert %}

## Creating an email sign-up form with a background image

When creating a drag-and-drop in-app message, select **Email sign-up with background image** for your template and select **Build message**. This template is supported for both mobile apps and web browsers.

![The in-app message editor with the template for an email sign-up form with a background image.][img1]

### Step 1: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 2: Customize your email sign-up component

To get started building your email sign-up form, select the email capture element in the editor. By default, collected email addresses will have the global subscription group **Subscribed**. To opt in users to specific subscription groups, refer to [Updating email subscription states]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

You can customize the placeholder text and label text of the email capture element.

![The in-app message editor with a side menu for customizing the email capture element.][img2]

#### Email validation

If the user enters an email address that includes any unaccepted special characters, they will see a generic error indicator and won't be able to submit the form. This error message isn't customizable. You can view the error behavior in the **Preview & Test** tab and on your test device. Learn more about how Braze formats email addresses in [Email validation]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Step 3: Add disclaimer language (optional)

We recommend including opt-in language and links to your brand’s privacy policy and terms and conditions in your message. We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes. Be sure to work with your legal team to develop language that is tailored to your specific brand.

{% alert note %}
Deliverability best practices often exceed legal requirements, and our recommendation is to always obtain explicit consent to send emails and allow users to easily decline.
{% endalert %}

### Step 4: Style your message

Customize the look and feel of your message using the drag-and-drop [in-app message components][3]. Add your own background image by replacing the default background image URL in the **Message container** menu or remove the URL and select your image from the [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/).

## Reporting

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can [create a segment][5] of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

## Best practices

### Double opt-in verification

To make sure that anyone who signed up for your list meant to sign up for your list and provided the correct email address, we recommend getting a second confirmation from anyone who signed up through your email sign-up form by sending a [double opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in) flow.

One of the ways you can set this up is through Canvas Flow:

1. Build a Canvas that is action-based and set it up to trigger when a user adds an email address to Braze. Make sure that you allow for targeting users who are new to the platform (for example, by using a segment with no filters in the Canvas).
2. Create an email message step with a CTA that has a hyperlink to the {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid tag. This will change the user's email subscription state to `opted_in` when they click the button.
3. Add an [Action Paths step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. For the first path, trigger an email when a user changes their email subscription status to `opted_in`. This email should inform users that their email has been confirmed.
5. Set up the other path to exit the Canvas after the window expires.

[img1]: {% image_buster /assets/img/templates/email_capture_image.png %} 
[img2]: {% image_buster /assets/img/templates/email_capture_field_image.png %} 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/