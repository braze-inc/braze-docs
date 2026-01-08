---
nav_title: Multi-language settings
article_title: Multi-language Settings
alias: "/multi_language_support/"
page_order: 5.5
description: "This article provides an overview of multi-language settings in the Braze dashboard and how to use locales in your messaging."
---

# Translation and Multi-language settings

> The multi-language feature allows you to use [translation tags]({{ site.baseurl }}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) to target users in different languages and locations all within a single message.

{% multi_lang_include locales.md section="Prerequisites" %}

## Add a locale

1. Go to **Settings** > **Multi-Language Support** under **Workspace Settings**.
2. Select **Add locale**, and then select **Default locale** or **Custom Attributes**.<br><br>![The "Add locale" dropdown with options to select the default locale or custom attributes.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Enter a name for the locale.
4. Select the respective user attributes for your chosen locale option.

{% tabs %}
{% tab Default locale %}

For **Default locale**, use the dropdowns to select the language to be added and, optionally, the country to be associated with the language.<br><br>![A window called "Add locale - Default Language and Country" to specify the language and country.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

For **Custom Attributes**, use the dropdown to select the associated custom attribute and in the text field, enter the value.<br><br>![A window called "Add locale - Custom Attributes" to specify the custom attribute and value.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5. Select **Add locale**. 

For steps to use these locales in your email campaigns and Canvas, refer to [Using locales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Considerations

- When setting up a locale, you can either select languages from the default user attributes or custom attributes. You can't select from both.
- You can select up to two custom attributes in a single locale, or up to two default user attribute languages. In both cases, the second attribute is optional.
- When making edits to the translated values in the CSV file, avoid modifying any default values in the file.
- The locale key in your uploaded file must match the one in your multi-language settings.

### Support and prioritization

- Users that match a custom attribute locale get prioritized before users that match a default user attribute.
- Custom attribute support is limited to string types and the `equals` comparison key.
- If a custom attribute is deleted or its type is changed, the user can no longer fall into that locale and will either go down the priority list of locales they fall under or receive default marketing translations.
- If a locale is invalid (the custom attribute changed or is deleted), the error will appear on the **Multi-Language Support** page.

## Frequently asked questions

#### How many locales can I add?

You can add up to 200 locales.

#### Where are the translation files stored in Braze?

Translation files are stored at a campaign level, meaning each message variant must have uploaded translations.

#### Does the locale name have to follow a specific pattern or format?

No. You can use your preferred naming convention. The locale name is used when selecting the locale in the editor and will be in the headings of the file you download with translation IDs.
