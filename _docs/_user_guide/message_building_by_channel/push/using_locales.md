---
nav_title: Locales in messages
article_title: Locales in Messages
page_order: 9
description: "This article provides steps on how to use locales in your push notifications."
---

# Locales in messages

> After adding locales to your workspace, you can target users in different languages all within a single push notification.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
Multi-language support and locales in messages are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Using locales

To use locales in your messaging, compose a push campaign or Canvas, then complete the following:

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated.

![Push notification composer with translation tags added to the title and message fields.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2. Save your message as a draft.
3. Select **Manage language** and add your locales for the message using the dropdown.
4. Select **Download template**, then fill in the translations within the CSV template.

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5. To upload the completed CSV template, select **Upload translations**. 

![The "Multi-language messages" window with two locales selected and buttons to download a template or upload translations.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Any changes to the IDs or locales in the CSV file will not automatically update in your message. To update the translations, update the CSV file and re-upload the file.

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
