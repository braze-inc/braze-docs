---
nav_title: Multi-language settings
article_title: Translation and multi-language settings
alias: "/multi_language_support/"
page_order: 5.5
description: "This article provides an overview of multi-language settings in the Braze dashboard and how to use locales in your messaging."
---

# Translation and multi-language settings

> The multi-language feature allows you to use [translation tags]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) to target users in different languages and locations all within a single message.

## Prerequisites

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Add a locale

1. Go to **Settings** > **Localization Settings**.
2. Select **Add locale**, and then select **Default locale** or **Custom Attributes**.

![The "Add locale" dropdown with options to select the default locale or custom attributes.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Enter a name for the locale.
4. [Select a language for accessibility]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/#language-settings-and-accessibility). This setting allows assistive technologies like screen readers to correctly pronounce text.
5. Select the respective user attributes for your chosen locale option. When setting up a locale, you can either select languages from the default user attributes or custom attributes. You can't select from both.

{% tabs %}
{% tab Default locale %}

For **Default locale**, use the dropdowns to select the language to be added and, optionally, the country to be associated with the language.

![A window called "Add locale - Default Language and Country" to specify the language and country.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

For **Custom Attributes**, use the dropdown to select the associated custom attribute and in the text field, enter the value.

![A window called "Add locale - Custom Attributes" to specify the custom attribute and value.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Select **Add locale**.

For steps to use these locales in your messages, see [Translating locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

## Considerations

- You can select up to two custom attributes in a single locale, or up to two default user attribute languages. In both cases, the second attribute is optional.
- When making edits to the translated values in the CSV file, avoid modifying any default values in the file.
- The locale key in your uploaded file must match the one in your multi-language settings.

### Support and prioritization

- If a user matches both a locale defined by custom attributes and one defined by default user attributes, the custom attribute locale is prioritized.
- Custom attributes support text (string) values with exact matching.
- If a custom attribute is deleted or its type is changed, the user can no longer fall into that locale and will either go down the priority list of locales they fall under or receive default marketing translations.
- If a locale is invalid (the custom attribute changed or is deleted), the error will appear on the **Multi-Language Support** page.

## Frequently asked questions

#### How many locales can I add?

You can add up to 200 locales.

#### Where are the translation files stored in Braze?

Translation files are stored at a campaign level, meaning each message variant must have uploaded translations. Translations can also be stored in Content Blocks. When the block is added to a message, its translations are automatically included.

#### Does the locale name have to follow a specific pattern or format?

No. You can use your preferred naming convention. The locale name is used when selecting the locale in the editor and will be in the headings of the file you download with translation IDs.
