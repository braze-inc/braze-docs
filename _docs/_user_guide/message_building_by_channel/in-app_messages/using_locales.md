---
nav_title: Locales in messages
article_title: Locales in Messages
page_order: 4
alias: /iam_locales/
description: "This article provides steps on how to use locales in your in-app messages."
---

# Locales in messages

> After adding locales to your workspace, you can target users in different languages all within a single in-app message.

{% multi_lang_include locales.md section="Prerequisites" %}

## Using locales

To use locales in your messaging, compose an in-app message campaign or Canvas. Select either the drag-and-drop editor or the traditional editor, then follow the steps based on your editor.

{% tabs %}
{% tab traditional editor %}

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated. 
2. Add an ID tag to each translation tag. An example is: {% raw %}`{% translation id_1 %}`{% endraw %}

![Traditional editor with translation IDs.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3. After adding the tags, save your message as a draft.
4. Select **Manage languages** and add your locales for the message using the dropdown.

!["Manage languages" modal with one selected locale.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5. Select **Download template** to download the translation template as a CSV file. Then, fill in the translations in the CSV file.

![An example of a translation CSV file.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6. Select **Upload translations** to upload the CSV file with the completed translations.

{% endtab %}
{% tab Drag-and-drop editor %}

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated. 
2. Add an ID tag to each translation tag. An example is: {% raw %}`{% translation id_1 %}`{% endraw %} 

![Drag-and-drop editor with two translation IDs.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3. After adding the tags, save your message as a draft, and then open the editor again.
4. In the **Build** panel, select **Multi-language** and add your locales for the message using the dropdown.
5. Select **Download template** to download the translation template as a CSV file. 

!["Multi-language" panel with button to download the template.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6. Fill in the translations in the CSV file. If you've copied and pasted the translation tags directly from Step 1, you may need to remove `<code>` from the **Translation tags** column of the CSV file.
7. Select **Upload translations** to upload the CSV file with the completed translations.

!["Multi-language" panel with buttons to download the template and upload translations.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

Any changes to the IDs or locales in the CSV file will not automatically update in your message. To update the translations, update the CSV file and re-upload the file.

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
