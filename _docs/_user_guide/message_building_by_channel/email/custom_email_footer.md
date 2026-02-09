---
nav_title: Custom email footer
article_title: Custom Email Footer
page_order: 6.5
description: "This article describes how to set up a workspace-wide custom email footer."
channel:
  - email

---

# Custom email footer

> You can set a workspace-wide custom email footer, which you can template into every email using the {% raw %}`{{${email_footer}}}`{% endraw %} Liquid attribute.

By using custom email footers, you no longer have to create a new footer for every email template or email campaign you use. All new and existing email campaigns reflect changes you make to your custom footer. Remember that compliance with the [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requires you to include a physical address for your company and an unsubscribe link in your emails.

{% alert warning %}
It is your responsibility to make sure that your custom footer meets the aforementioned requirements.
{% endalert %}

## Creating your custom footer

To create or edit your custom footer, do the following:

1. Go to **Settings** > **Email Preferences** > **Subscription Pages and Footers**.
2. Go to the **Custom footer** section and turn on custom footers.
3. Select **Edit** then edit your footer in the **Compose** section.
4. Select **Preview** to preview how your email footer will appear in a customer’s inbox. You can optionally select **Copy preview link** to generate and copy a shareable preview link that shows what the email will look like for a random user. The link will last for seven days before it needs to be regenerated.
5. Send a test message. 

![An example of a custom footer.]({% image_buster /assets/img_archive/custom_footer.png %})

The default footer uses the {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} attribute and our physical mailing address. If you're using this default, be sure to select **&#60;other&#62;** for the **Protocol**.

{% alert important %}
To comply with CAN-SPAM regulations, your custom footer must include an unsubscribe link. You can use this Liquid attribute {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} or your own custom unsubscribe URL. You won’t be able to save a custom footer without an unsubscribe link.
{% endalert %}

![Protocol and URL values needed for the custom footer.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Footers without unsubscribe links

Be very careful when using a template with the custom footer {% raw %}`{{${email_footer}}}` but without the `{{${set_user_to_unsubscribed_url}}}`{% endraw %} unsubscribe link tag. A warning will appear, but it'll be your choice to send an email with or without an unsubscribe link.

Here's a warning in the email composer:

![Example email composed without a footer.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Here's a warning in the campaign composer:

![No-footer campaign composition.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Adding a custom unsubscribe link

To add a custom unsubscribe link, you can change the unsubscribe link in the custom footer from {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} to a link to your own website with a query parameter that includes the user ID. An example is: 
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Next, call the [`/email/status` endpoint]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) to update the user's subscription status. For more details, see our documentation on [changing email subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Then, save this new link. The default Braze unsubscribe tag {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} must be in the footer. This means you need to include the default link by "hiding" it by either placing the tag in a comment or in a hidden `<div>` tag.

## Best practices

We suggest the following best practices when creating and using custom footers.

### Personalizing with attributes

When creating a custom footer, Braze suggests using [attributes for personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). The full set of default and custom attributes are available, but here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | {% raw %}`{{${email_address}}}`{% endraw %} |
| User's Custom Unsubscribe URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>This tag replaces the previous {% raw %}`{{${unsubscribe_url}}}`{% endraw %} tag. We recommend that you use the newer {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} tag instead. |
| User's Custom Opt-In URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| User's Custom Subscribe URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| User's Custom Braze Preference Center URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Including an unsubscribe link and opt-in link

{% raw  %}
As a best practice, Braze recommends including both an unsubscribe link (such as ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (such as ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way, users will be able to both unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.
{% endraw %}

### Setting custom footers for plaintext emails

You can also choose to set a custom footer for plaintext emails from the **Subscription Pages and Footers** tab on the **Email Preferences** page, which follows the same rules as the custom footer for HTML emails. 

If you don't include a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, select **Save**.

![Email with Set Custom Plaintext Footer option selected.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

