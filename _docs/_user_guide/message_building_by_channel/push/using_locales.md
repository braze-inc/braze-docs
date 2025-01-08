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

To use locales in your messaging, compose a push campaign or Canvas, then follow the steps.

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated.<br><br>![Push notification composer with translation tags added to the title and message fields.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. After adding the tags, save your message as a draft.
3. Select **Manage language** and add your locales for the message using the dropdown.
4. Select **Download template** to download the translation template as a CSV. Then, fill in the translations in the CSV. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. Select **Upload translations** to upload the CSV file with the completed translations. <br><br>![The "Multi-language messages" window with two locales selected and buttons to download a template or upload translations.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

To update the translations, update the CSV and re-upload the file. This means any changes to the IDs or locales in the CSV will not automatically update in your message.

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

## Preview your locales

In the **Preview message as user** dropdown within the **Test** tab, select **Custom user** and enter different languages to preview the message to check if your message translates as expected.

## Frequently asked questions

#### I want to make a change to the translated copy in one of my locales. How can I do that?
Make the edit in the CSV, then upload the file again to make a change to the translated copy.

#### Can I nest translation tags?
No.

#### Can I add HTML styling in the translation tags?
Yes. However, be sure to check that the HTML styling is not translated with the content.

#### What validations or extra checks does Braze do?

| Scenario                                                                                                                                                 | Validation in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| A translation file is missing locales associated with the current message.                                                                               | This translation file won't be uploaded.                                                                       |
| A translation file is missing text blocks, such as a text within Liquid translation tags, from the current email message.                                | This translation file won't be uploaded.                                                                       |
| The translation file includes the default text that doesn't match the text blocks in the current email message.                                          | This translation file won't be uploaded. Fix this in your CSV before attempting to upload again.               |
| The translation file includes locales that don't exist in **Multi-Language Support** settings.                                                           | These locales will not be saved in Braze.                                                                      |
| The translation file includes text blocks that don't exist in the current message (such as the current draft at the time the translations are uploaded). | The text blocks that don't exist in your current message will not be saved from the translation file to Braze. |
| Removing a locale from the message after that locale has already been uploaded to the message as part of the translation file.                           | Removing the locale will remove any translations associated with the locale in your message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }