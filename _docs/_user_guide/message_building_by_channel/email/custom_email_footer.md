---
nav_title: Custom Email Footer
article_title: Custom Email Footer
page_order: 6.5
description: "This article describes how to set up a workspace-wide custom email footer."
channel:
  - email

---

# Custom email footer

> You can set a workspace-wide custom email footer which you can template into every email using the {% raw %}`{{${email_footer}}}`{% endraw %} Liquid attribute.

By using custom email footers, you no longer have to create a new footer for every email template or email campaign you use. Changes you make to your custom footer will be reflected in all new and existing email campaigns. Remember that compliance with the [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requires you to include a physical address for your company and an unsubscribe link in your emails.

{% alert warning %}
It is your responsibility to make sure that your custom footer meets the aforementioned requirements.
{% endalert %}

## Creating your custom footer

To create or edit your custom footer, do the following:

1. Go to **Settings** > **Email Preferences**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is called **Email Settings** and is located under **Manage Settings**.
{% endalert %}

{: start="2"}
2. Go to the **Custom Footer** section and turn on custom footers.
3. Edit your footer in the **Compose** section and send a test message. 

![]({% image_buster /assets/img_archive/custom_footer.png %})

The default footer uses the {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} attribute and our physical mailing address. To comply with CAN-SPAM regulations, your custom footer must include {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. You won't be able to save a custom footer without this attribute.

If using the default footer, which uses the {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} attribute, be sure to select **&#60;other&#62;** for the **Protocol**.

![Protocol and URL values needed for the custom footer.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Footers without unsubscribe links

Be very careful when using a template with the custom footer {% raw %}`{{${email_footer}}}` but without the `{{${set_user_to_unsubscribed_url}}}`{% endraw %} unsubscribe link tag. A warning will appear, but it'll be your choice to send an email with or without an unsubscribe link.

**Warning within email composer:**<br>![Example email composed without a footer.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

**Warning within campaign composer:**<br>![No-footer campaign composition.]({% image_buster /assets/img_archive/no_footer_test.png %})

## Best practices

Braze suggests the following best practices when creating and using custom footers.

### Personalizing with attributes

When creating a custom footer, Braze suggests using [attributes for personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). The full set of default and custom attributes are available, but here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | {% raw %}`{{${email_address}}}`{% endraw %} |
| User's Custom Unsubscribe URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>This tag replaces the previous {% raw %}`{{${unsubscribe_url}}}`{% endraw %} tag. We recommend that you use the newer {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} tag instead. |
| User's Custom Opt-In URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| User's Custom Subscribe URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| User's Custom Braze Preference Center URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2}

### Including an unsubscribe link and opt-in link

{% raw  %}
As a best practice, Braze recommends including both an unsubscribe link (such as ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (such as ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way, users will be able to both unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.
{% endraw %}

### Setting custom footers for plaintext emails

You can also choose to set a custom footer for plaintext emails from the **Subscription Pages and Footers** tab on the **Email Preferences** page, which follows the same rules as the custom footer for HTML emails. If you don't include a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, click **Save** at the bottom of the page.

![Email with Set Custom Plaintext Footer option selected.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
