---
nav_title: Multi-Language Settings
article_title: Multi-Language Settings
permalink: "/multi_language_support/"
hidden: true
description: "This article provides an overview of multi-language settings in the Braze dashboard and how to use locales in your messaging."
---

# Multi-language settings

> By adjusting multi-language settings, you can target users in different languages and locations with different messages all within a single email message.

{% alert important %}
Multi-language settings are currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

## Prerequisites

In order to edit and manage multi-language support, you must have the "Manage Multi-Language Settings" user permission.

## Add a locale

1. Go to **Settings** > **Multi-Language Support** under **Workspace Settings**.
2. Select **Add locale**.
3. Enter a name for the locale.
4. For the **User attributes**, select the language to be added using the **Language** dropdown.
5. (Optional) Select the country to be associated with the language.
6. Select **Add locale**. 

![An example of French added as a locale for users whose country is Canada.][2]{: style="max-width:80%;"}

## Use locales in messaging

To use locales in your messaging, follow these steps:

1. Compose an email campaign or Canvas with all text and image or link URLs wrapped in translation tags.<br>![][3]
2. Save the message.
3. In the editor, select **Multi-language** and add your locales for the message using the dropdown.
4. Select **Download template** to download the translation template as a CSV. Then, fill in the translations in the CSV.
5. Select **Upload translations** to upload the CSV file with the completed translations. 

To update the translations, update the CSV and re-upload the file. 

## Preview your locales

In the **Preview & Test** section, select **Multi-language User** to preview the message to check if your message translates as expected.

## Frequently asked questions

### Settings

#### How many locales can I add?
You can add up to 200 locales.

#### Where are the translation files stored in Braze?
Translation files are stored at a campaign level.

#### Does the locale name have to follow a specific pattern or format?
No. You can use your preferred naming convention. The locale name is used when selecting the locale in the editor and will be in the headings of the file you download with translation IDs.

#### Can I use custom attributes to define a locale?
Not currently. Contact your account manager or leave [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) with more details on how you would define locales.

### Composition

#### I want to make a change to the translated copy in one of my locales. How can I do that?
Make the edit in the CSV, then upload the file again to make a change to the translated copy.

#### Can I use Liquid in a translation tag?


#### Can I nest translation tags?
No.

#### Can I add HTML styling in the translation tags?
Yes. However, be sure to check that the HTML styling is not translated with the content.

#### What validations or extra checks does Braze do?

| Scenario | Validation in Braze |
| --- | --- |
| A translation file is missing locales associated with the current message. | This translation file won't be uploaded. |
| A translation file is missing text blocks, such as a text within Liquid translation tags, from the current email message. | This translation file won't be uploaded. |
| The translation file includes the default text that doesn't match the text blocks in the current email message. | This translation file won't be uploaded. |
| The translation file includes locales that don't exist in **Multi-Language Support** settings. | These locales will not be saved in Braze. |
| The translation file includes text blocks that don't exist in the current message (such as the current draft at the time the translations are uploaded). | The text blocks that don't exist in your current message will not be saved from the translation file to Braze. |
| Removing a locale from the message after that locale has already been uploaded to the message as part of the translation file. | Removing the locale will remove any translations associated with the locale in your message. |
{: .reset-td-br-1 .reset-td-br-2}


[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}
[3]: {% image_buster /assets/img/multi-language_support/translation_html_editor_example.png %}