---
nav_title: Multi-Language Settings
article_title: Multi-Language Settings
permalink: "/multi_language_support/"
hidden: true
description: "This article provides an overview of multi-language settings in the Braze dashboard and how to use locales in your messaging."
---

# Multi-language settings

> By adjusting multi-language settings, you can target users in different languages and locations with different messages all within a single email campaign or Canvas.

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
2. In the editor, select **Multi-language** and add your locales for the message using the dropdown.
3. Select **Download template** to download the translation template as a CSV. Then, fill in the translations in the CSV.
4. Select **Upload translations** to upload the CSV file with the completed translations. 

To update the translations, update the CSV and re-upload the file. In the **Preview & Test** section, you can select **Multi-language User** to preview the message to check if your message translates as expected.

[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}
[3]: {% image_buster /assets/img/multi-language_support/translation_html_editor_example.png %}