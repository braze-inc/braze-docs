---
nav_title: Locales in messages
article_title: Translating locales
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "This article provides steps on how to use locales in your messages."
---

# Translating locales

> After adding locales to your workspace, you can target users in different languages all within a single push, email, banner, in-app message, or Content Block.

## Prerequisites

{% tabs %}
{% tab Multi-language locales %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Message types %}

| Feature | Required user permissions |
| --- | --- |
| Message types | You need these permissions to add locales and translations to campaigns and Canvases:<br><br> {::nomarkdown}Granular permissions: <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul> Legacy permissions: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Templates %}

| Feature | Required user permissions |
| --- | --- |
| Templates | You need these permissions for the template type you want to add locales and translations to:<br><br> {::nomarkdown}Granular permissions: <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul> Legacy permissions: <ul><li>Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Use locales

### Step 1: Set up locales

Before you can add translations to a message, you must first [create the locales you want to support]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Locales define the language (and optionally region) variants available for messaging. 

### Step 2: Mark content for translation

Wrap text you want to translate with the Liquid translation tags {% raw %}`{% translation your_id_here %}` and `{% endtranslation %}`{% endraw %} and assign a tag ID. Translation tag IDs must be unique within a message. Consider using semantic ID names that plainly describe the text, such as {% raw %}`{% translation header %}`{% endraw %}.

Here is an example message marked for translation: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Highlight the text you want to translate and use the keyboard shortcut **Cmd + Alt + L** (macOS) or **Ctrl + Alt + L** (Windows) to wrap in translation tags.<br><br> This shortcut works in all channels that support multi-language messaging except for the drag-and-drop editors for email and Content Blocks. For those, use the **Add personalization** button in the left sidebar to add translation tags.
{% endalert %}

#### Localize URLs

When translating content, URLs require special handling to prevent broken links. 

##### Standard (static) URLs

Static URLs are entered manually in the editor (for example, `https://example.com`). We also recommend the following:

| Recommendation | Reasoning |
| --- | --- |
| Keep the protocol (`https://`) outside of translation tags. Wrap only the domain and path (for example, `example.com/en`). | Translators may accidentally alter or remove special characters, causing broken links. |
| Do not include query parameters inside translation tags (for example, `?utm_source=promo`). | Translators may accidentally alter or remove special characters, resulting in broken links. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

An standard URL that follows both recommendations is:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
If you are using [email link tracking](#email-link-tracking) (link aliasing or Link Templates), additional configuration is required when URLs are wrapped in translation tags.
{% endalert %}

#### HTML attributes and structure

Only wrap human-readable text in translation tags. Avoid wrapping HTML attributes (such as `class`, `style`, or `id`) or other structural code. HTML attributes control layout, styling, and functionality. Wrapping them in translation tags can break formatting or styles in localized versions of your message.

This text is correctly wrapped:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Incorrectly wrapped text %}

This text is **incorrectly** wrapped:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Step 3: Add locales to your message

After adding translation tags to your message, select **Manage languages** in the editor (**Languages** in the drag-and-drop editors for email and Content Blocks) and select at least one locale you want to add translations for.

![The Add locale dropdown with options to select the default locale or custom attributes.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks containing translation

If your message contains Content Blocks that already have translations saved, you do not need to re-upload those translations. Saved translations are automatically applied when the Content Block is added to your message.

In the **Manage languages** modal, Content Blocks with saved translations will appear in the list, alongside the locales they support. This allows you to see which parts of your message are already localized before adding new translations.

![The Manage languages section with a list of Content Blocks that have saved translations.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Make sure each Content Block includes translations for every locale added to your message. If a Content Block is missing translations for one of the locales you've added, it will be shown in its original language for users in that locale.
{% endalert %}

### Step 4: Add translations

After selecting locales, add translations to your message using one of the following methods:

![The Add translations tab with options to upload translations by CSV or by connecting to translation partners.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Upload CSV template %}

Select **Download template** to download a CSV containing a matrix of your selected translation IDs and locales. Enter translations for each locale. Upload the completed file and translations will be applied to your message. 

{% alert important %}
To prevent display issues with non-English characters, avoid using Excel for your translation CSV.
{% endalert %}

![CSV with translation tags for a title, offer text, offer amount, and CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Use the translation API %}

Use a partner translation API to manage and update translations in your campaigns and Canvases. This is useful if you use an external system for localization or want to directly connect with a translation partner.

To use the translations endpoints with Canvases, include the following parameters:
  - `workflow_id`
  - `step_id`
  - `message_variation_id` 

{% alert note %}
When using the translation API with Canvas steps that were created after the Canvas launched, the `message_variation_id` that you pass into the API will be empty or blank.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 5: Preview translations

To preview your message, select the **Multi-Language User** option from the **Preview as User** dropdown. This lets you switch between different locale definitions to preview all translations of your message.

![Locale previews]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Manage translations

### Duplicate Canvas steps or campaigns, and translations

When you duplicate a Canvas step, campaign, or variation, translations are included. This is also true when copying across workspaces, so long as the locales are defined in that destination workspace. Be sure to review and update translations accordingly when making modifications to your Canvas or campaign.

### Save translations in Content Blocks

Content Blocks support multi-language in the same way as messages. When creating or editing Content Blocks, you can tag content for translation, add locales, and upload translations using a CSV or the [translation API]({{site.baseurl}}/api/endpoints/translations/).

Saved translations remain associated with the Content Block. When the block is added to a message, its translations are automatically included.

### Right-to-left messages

When filling in the translation file for languages that are written from right-to-left (like Arabic), wrap the translation with `span` so that it is properly formatted:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Email link tracking

In email campaigns, Braze tracks links by adding tracking information (query parameters) to each URL. This behavior supports both [link aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) and [link templating]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template).

When a URL is wrapped in translation tags, Braze may not be able to determine where to add this tracking information. To ensure this works correctly, you must include a special character at the end of the URL to indicate where tracking should be added.

URLs use two special characters to control how this works:
  - `?` adds tracking to a URL that does not already have it.
  - `&` adds additional tracking if a `?` is already present in the URL. A URL can only contain one `?`.

| URL | Contains `?` | Description | Example |
| --- | --- | --- | --- |
| Standard URL | No | Add `?` after the closing translation tag if the URL does not already contain one. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| Standard URL | Yes | Use `&` at the end of the URL (after the closing translation tag) if it already contains `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid generated | No | Use `?` after the closing translation tags if the generated URL does not already contain one. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid generated | Yes | Use `&` after the closing translation tag if the generated URL already contains a `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Language settings and accessibility

For HTML-based channels (email, In-app message, Banners, Landing Pages, and Content Cards), Braze adds an accessibility language (`lang`) attribute to the rendered message. This attribute helps assistive technologies like screen readers correctly interpret and pronounce text.

Without this, a screen reader assumes content is in the default language the user set on their device during setup. If the message is in a different language, the screen reader may not pronounce everything correctly.

#### Configuring the accessibility language

You can set the accessibility language at two levels:

##### Message level

In your message settings, go to the **Accessibility** section and select a language from the dropdown or use Liquid to dynamically set the accessibility language. This applies to all content in the message. 

##### Locale level

For multi-language messages, set the accessibility language on each locale in **Localization Settings**. When new messages are created, {% raw %}`{{accessibility_language}}`{% endraw %} will be selected by default in the **Accessibility** section. This maps the accessibility language to your locale settings.

#### Standards

The accessibility language maps to the HTML `lang` attribute, a [WCAG 2.1 Level A requirement](https://dequeuniversity.com/rules/axe/4.2/html-has-lang) (Success Criterion 3.1.1). For multi-language content, you can also set the language on individual content blocks using the `lang` attribute directly in your HTML.

## Frequently asked questions

### Does Braze provide translations?

No. You must [provide your own translations](#step-4-add-translations) either by uploading a CSV or using the translation API.

### Can I nest translation tags?

No.

#### Can I wrap entire HTML messages in a translation tag?

No. As a best practice, you should only wrap human-readable text or content that must be localized. This helps prevent broken formatting, links, or other non-text elements.

Additionally, consider wrapping smaller, semantically-related pieces of text to create accurate translations and avoid performance or size limitations.

#### Can I make a change to the translated copy in one of my locales?

Yes. If using a CSV, first make the edit in the file, then upload it again to make a change to the translated copy. If  using the [translation API]({{site.baseurl}}/api/endpoints/translations/), use the Update endpoints to make changes.

#### What validations or extra checks does Braze do?

| Scenario | Validation in Braze |
| --- | --- |
| A message contains two or more matching translation IDs that map to different text. | This translation file won't be downloaded. |
| A translation file is missing one or more translation tag IDs. | This translation file won't be uploaded. |
| A translation file contains locales that are missing from the message. | This translation file won't be uploaded. |
| Translation tags must be added to a message before downloading the translation template. | This translation file won't be downloaded. |
| Translation tags found in your uploaded file are missing from your message. | Extra translations won't be saved to the message. |
| {% raw %}A message contains one or more broken Liquid tags. To open tags use `{% translation your_id_here %}`, close translation tags with `{% endtranslation %}`.{% endraw %} | This translation file won't be downloaded. |
| A translation file contains default text that doesn't match what's in the message. | Translations are added, but original message text is not updated. |
| One or more of the locales in a message have been deleted in settings and no longer exist. | Translations that have already been added continue to exist within the message. If deleted from the message, translations will be lost. |
| Translation tags contain full URLs or Liquid-generated URLs. | Translation tags containing URLs are identified in case issues with broken links or link tracking occur. |
| Translation tags include query parameters. | Translation tags containing query parameters are identified in case issues with broken links or link tracking occur. |
| Translation tags contain HTML attributes or structures. | Translation tags containing HTML attributes or structures are identified in case issues with styles and formatting occur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
