{% if include.section == "SDK requirements" %}

## Prerequisites

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. For more information, see [Creating an in-app message with drag-and-drop: Prerequisites]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK versions for text links

To include text links that do not dismiss the message, the following minimum SDK versions are required:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
If you include a link in your in-app message that redirects to a URL and the user isn't on the minimum SDK versions specified, clicking on the link will close the message, and the user won't be able to return to the message to submit the form.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

{% endif %}


<!-- Add this below after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

We recommend including opt-in language and links to your brand’s privacy policy and terms and conditions in your message. Be sure to work with your legal team to develop language that is tailored to your specific brand.

{% alert note %}
Deliverability best practices often exceed legal requirements, and our recommendation is to always obtain explicit consent to send emails and allow users to easily decline.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

If the user enters an email address that includes any unaccepted special characters, they will see a generic error indicator and won't be able to submit the form. This error message isn't customizable. You can view the error behavior in the **Preview & Test** tab and on your test device. Learn more about how Braze formats email addresses in [Email validation]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% endif %}

{% if include.section == "email double opt-in" %}

### Double opt-in verification

To make sure that anyone who signed up for your list meant to sign up for your list and provided the correct email address, we recommend getting a second confirmation from anyone who signed up through your email sign-up form by sending a [double opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in) flow.

One of the ways you can set this up is through Canvas:

1. Build a Canvas that is action-based and set it up to trigger when a user adds an email address to Braze. Make sure that you allow for targeting users who are new to the platform (for example, by using a segment with no filters in the Canvas).
2. Create an email message step with a CTA that has a hyperlink to the {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid tag. This will change the user's email subscription state to `opted_in` when they click the button.
3. Add an [Action Paths step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. For the first path, trigger an email when a user changes their email subscription status to `opted_in`. This email should inform users that their email has been confirmed.
5. Set up the other path to exit the Canvas after the window expires.

{% endif %}

{% if include.section == "reporting" %}

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

{% endif %}