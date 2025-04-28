---
nav_title: Locales in Messages
article_title: Locales in Messages
page_order: 9
description: "This article provides steps on how to use locales in your push notifications."
---

# Locales in messages

> After adding locales to your workspace, you can target users in different languages all within a single push notification.

## Prerequisites

To edit and manage [multi-language support]({{site.baseurl}}/multi_language_support/), you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

## Using locales

To use locales in your messaging, compose a push campaign or Canvas, then complete the following:

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated.<br><br>![Push notification composer with translation tags added to the title and message fields.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. Save your message as a draft.
3. Select **Manage language** and add your locales for the message using the dropdown.
4. Select **Download template**, then fill in the translations within the CSV template. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. To upload the completed CSV template, select **Upload translations**. <br><br>![The "Multi-language messages" window with two locales selected and buttons to download a template or upload translations.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

To update the translations, update the CSV and re-upload the file. This means any changes to the IDs or locales in the CSV will not automatically update in your message.

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

## Preview your locales

In the **Preview message as user** dropdown within the **Test** tab, select **Custom user** and enter different languages to preview the message to check if your message translates as expected.

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
