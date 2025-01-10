---
nav_title: Locales in Messages
article_title: Locales in Messages
page_order: 6.3
description: "This article provides steps on how to use locales in your messaging."
---

# Locales in messaging

> After adding locales to your workspace, you can target users in different languages all within a single email message.

## Prerequisites

To edit and manage [multi-language support]({{site.baseurl}}/multi_language_support/), you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

## Using locales

To use locales in your messaging, compose an email campaign or Canvas. Select either the HTML editor or drag-and-drop editor, then follow the steps based on your editor.

{% tabs %}
{% tab HTML editor %}

1. Highlight the text you want translated. Select **Insert Translation Tag**. This will wrap your text with translation tags. <br>![]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Save the message as a draft.
3. Select **Multi-language** and add your locales for the message using the dropdown.
4. Select **Download template** to download the translation template as a CSV. Then, fill in the translations in the CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Select **Upload translations** to upload the CSV file with the completed translations.

{% endtab %}
{% tab Drag-and-drop editor %}

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated.<br>![]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
2. After adding the tags, save your message as a draft.
3. Select **Multi-language** and add your locales for the message using the dropdown.
4. Select **Download template** to download the translation template as a CSV. Then, fill in the translations in the CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Select **Upload translations** to upload the CSV file with the completed translations.

{% endtab %}
{% endtabs %}

To update the translations, update the CSV and re-upload the file. This means any changes to the IDs or locales in the CSV will not automatically update in your message.

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

## Preview your locales

In the **Preview & Test** section, select **Multi-language User** to preview the message to check if your message translates as expected.

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
