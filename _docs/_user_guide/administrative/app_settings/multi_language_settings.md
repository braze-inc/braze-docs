---
nav_title: Multi-Language Settings
article_title: Multi-Language Settings
alias: "/multi_language_support/"
page_order: 5.5
description: "This article provides an overview of multi-language settings in the Braze dashboard and how to use locales in your messaging."
---

# Multi-language settings

> By adjusting multi-language settings, you can target users in different languages and locations with different messages all within a single email message.

## Prerequisites

To edit and manage multi-language support, you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

## Add a locale

1. Go to **Settings** > **Multi-Language Support** under **Workspace Settings**.
2. Select **Add locale**.
3. Enter a name for the locale.
4. For the **User attributes**, select the language to be added using the **Language** dropdown.
5. (optional) Select the country to be associated with the language.
6. Select **Add locale**. 

![An example of French added as a locale for users whose country is Canada.][2]{: style="max-width:80%;"}

For steps to use these locales in your email campaigns and Canvas, refer to [Using locales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/)

## Frequently asked questions

#### How many locales can I add?
You can add up to 200 locales.

#### Where are the translation files stored in Braze?
Translation files are stored at a campaign level, meaning each message variant will need to have uploaded translations.

#### Does the locale name have to follow a specific pattern or format?
No. You can use your preferred naming convention. The locale name is used when selecting the locale in the editor and will be in the headings of the file you download with translation IDs.

#### Can I use custom attributes to define a locale?
Not currently. Contact your account manager or leave [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) with more details on how you would define locales.

[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}