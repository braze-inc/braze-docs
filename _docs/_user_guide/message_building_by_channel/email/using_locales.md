---
nav_title: Locales in messages
article_title: Locales in Messages
page_order: 6.3
description: "This article provides steps on how to use locales in your messaging."
---

# Locales in messaging

> After adding locales to your workspace, you can target users in different languages all within a single email message.

## Prerequisites

To edit and manage [multi-language support]({{site.baseurl}}/multi_language_support/), you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

{% alert important %}
Multi-language support and locales in messages are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Using locales

To use locales in your messaging, compose an email campaign or Canvas. Select either the HTML editor or drag-and-drop editor, then follow the steps based on your editor.

{% tabs %}
{% tab HTML editor %}

1. Highlight the text you want translated. Select **Insert Translation Tag**. This will wrap your text with translation tags. <br>![HTML editor with one selected locale.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Save the message as a draft.
3. Select **Multi-language** and add your locales for the message using the dropdown.
4. Select **Download template** to download the translation template as a CSV file. Then, fill in the translations in the CSV file. <br>![An example of a translation CSV file.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Select **Upload translations** to upload the CSV file with the completed translations.

{% endtab %}
{% tab Drag-and-drop editor %}

1. Add translation tags {% raw %}`{% translation %}` and `{% endtranslation %}`{% endraw %} to wrap all text and image or link URLs to be translated. 
2. Add an ID tag to each translation tag. An example is: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Drag-and-drop editor with two translation IDs.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. After adding the tags, save your message as a draft.
4. Select **Multi-language** and add your locales for the message using the dropdown.
5. Select **Download template** to download the translation template as a CSV file. 
6. Fill in the translations in the CSV file. If you've copied and pasted the translation tags directly from Step 1, you may need to remove `<code>` from the **Translation tags** column of the CSV file.
7. Select **Upload translations** to upload the CSV file with the completed translations.

{% endtab %}
{% endtabs %}

Any changes to the IDs or locales in the CSV file will not automatically update in your message. To update the translations, update the CSV file and re-upload the file.

## Preview your locales

In the **Preview & Test** section, select **Multi-language User** to check if your message translates as expected.

## Managing translations

### Editing translations for launched campaigns and Canvases

After a campaign or Canvas has been launched, you can still modify translations when you're in draft mode. This applies whether you're editing translations directly in the composer, by CSV upload, or through the API. 

Before making any translation updates, the campaign or Canvas must first be saved as a draft.

1. Select **Edit campaign/Canvas** and then make your edits in the composer.
2. Select **Save as draft**, and then select **Yes** in the modal.
3. Go to the **Review Summary** step and select **Update campaign/Canvas**.
4. Select **Update campaign/Canvas** in the modal.

For more details on managing campaigns and Canvases after launch, refer to [Editing launched campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) and [Canvas drafts and post-launch editing]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicating Canvas steps or campaigns, and translations

When duplicating a Canvas step or a campaign, whether in the draft mode after launch or during initial creation, the translations associated with that step won't be carried over. Any necessary translations need to be added to the new step or campaign. Be sure to review and update translations accordingly when making modifications to your Canvas or campaign.

### Using the multi-language API with Canvases

To use the [multi-language API with Canvases]({{site.baseurl}}/api/endpoints/translations/), you must include the `workflow_id`, `step_id`, and `message_variation_id` in the parameter list.

#### Canvas steps added to post-launch drafts

When using the multi-language API with Canvas steps that were created after the Canvas has been launched, the `message_variation_id` that you pass into the API will be empty or blank.

{% multi_lang_include locales.md section="Frequently Asked Questions" %}