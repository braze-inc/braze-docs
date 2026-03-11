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

{% multi_lang_include locales.md section="Prerequisites" %}

## Using locales

### Step 1: Set up locales

Before you can add translations to a message, you must first [create the locales you want to support]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). Locales define the language (and optionally region) variants available for messaging. 

### Step 2: Mark content for translation

Wrap text you want to translate with the Liquid translation tags {% raw %}`{% translation your_id_here %}` and `{% endtranslation %}`{% endraw %} and assign a tag ID. Translation tag IDs must be unique within a message. Consider using semantic ID names that plainly describe the text, such as {% raw %}`{% translation header %}`{% endraw %}.

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Highlight the text you want to translate and use the keyboard shortcut **Cmd + Alt + L** (MacOS) or **Ctl + Alt + L** (windows) to wrap in translation tags.<br><br> This shortcut works in all channels that support multi-language messaging except for the drag-and-drop editors for email and Content Blocks. For those, use the **Add personalization** button in the left sidebar to add translation tags.
{% endalert %}

#### Localizing URLs

When translating content, URLs require special handling to prevent broken links. 

##### Standard (static) URLs

Static URLs are entered manually in the editor (for example, `https://example.com`). We also recommend the following:

| Recommendation | Reasoning |
| --- | --- |
| Keep the protocol (`https://`) outside of translation tags. Wrap only the domain and path (for example, `example.com/en`) | Translators may accidentally alter or remove special characters, causing broken links. |
| Do not include query parameters inside translation tags (for example, `?utm_source=promo`) | Translators may accidentally alter or remove special characters, resulting in broken links. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation }

An standard URL that follows both recommendations is:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz%}{% endtranslation %}">Click Here</a>
```
{% endraw %}

{% alert important %}
If you are using [email link tracking]() (link aliasing or Link Templates), additional configuration is required when URLs are wrapped in translation tags.
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

{% details Incorectlly wrapped text %}

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

!["Manage languages" section with a dropdown for selecting supported locales.]()

#### Content Blocks containing translation

If your message contains Content Blocks that already have translations saved, you do not need to re-upload those translations. Saved translations are automatically applied when the Content Block is added to your message.

In the **Manage languages** modal, Content Blocks with saved translations will appear in the list, alongside the locales they support. This allows you to see which parts of your message are already localized before adding new translations.

!["Manage languages" section with a list of Content Blocks that have saved translations.]()

{% alert important %}
Make sure each Content Block includes translations for every locale added to your message. If a Content Block is missing translations for one of the locales you've added, it will be shown in its original language for users in that locale.
{% endalert %}

### Step 4: Add translations

After selecting locales, add translations to your message using one of the following methods:

!["Add translations" tab with options to upload translations by CSV or by connecting to translation partners.]()

{% tabs %}
{% tab Upload CSV template %}

{% endtab %}
{% tab Connect to translation API %}

{% endtab %}
{% endtabs %}








### Step 4: Download CSV template {#download-csv}

After selecting your locales, select **Download template** to download a CSV template containing a matrix of your selected translation IDs and locales.

![Example CSV for en, fr, and es locales.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Step 5: Upload a completed CSV {#upload-csv}

{% alert important %}
Any changes to the IDs or locales in the CSV file will not automatically update in your message. To update the translations, update the CSV file and re-upload the file.
{% endalert %}

Here is the format for an example completed CSV:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Step 6: Preview locales {#preview-locales}

When previewing your message, select the **Multi-Language User** option from the **Preview as User** dropdown. This lets you switch between different locale definitions to preview all translations of your message.

![Locale previews]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Check out our [Translation API]({{site.baseurl}}/api/endpoints/translations) to manage and update translations in your campaigns and Canvases.
{% endalert %}

## Right-to-left messages

When filling in the translation file for languages that are written from right-to-left (like Arabic), wrap the translation with `span` so that it is properly formatted:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Managing translations

### Editing translations for launched campaigns and Canvases

After a campaign or Canvas has been launched, you can still modify translations when you're in draft mode. This applies whether you're editing translations directly in the composer, by CSV upload, or through the API. 

For more details on managing campaigns and Canvases after launch, refer to [Editing launched campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) and [Canvas drafts and post-launch editing]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicating Canvas steps or campaigns, and translations

Translations are copied along with a canvas step, campaign, or campaign variation. This is also true when copying across workspaces, so long as the locales are defined in that destination workspace. Be sure to review and update translations accordingly when making modifications to your Canvas or campaign.

### Using the Multi-Language API with Canvases

To use the [Multi-Language API with Canvases]({{site.baseurl}}/api/endpoints/translations/), you must include the `workflow_id`, `step_id`, and `message_variation_id` in the parameter list.

#### Canvas steps added to post-launch drafts

When using the Multi-Language API with Canvas steps that were created after the Canvas has been launched, the `message_variation_id` that you pass into the API will be empty or blank.

## Frequently asked questions

#### Can I make a change to the translated copy in one of my locales?
Yes. First, make the edit in the CSV, then upload the file again to make a change to the translated copy.

#### Can I nest translation tags?
No.

#### Do translations support HTML for styling?
Yes, but be sure to check that the HTML styling is not translated with the content.

#### Can I wrap entire HTML messages in a translation tag?
No, your translation tags should be as small as possible to avoid performance or size limitations.

#### What validations or extra checks does Braze do?

| Scenario                                                                                                                                                 | Validation in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| A translation file is missing locales associated with the current message.                                                                               | This translation file won't be uploaded.                                                                       |
| A translation file is missing text blocks, such as text within Liquid translation tags, from the current email message.                                | This translation file won't be uploaded.                                                                       |
| The translation file includes the default text that doesn't match the text blocks in the current email message.                                          | This translation file won't be uploaded. Fix this in your CSV before attempting to upload again.               |
| The translation file includes locales that don't exist in the **Multi-Language Support** settings.                                                       | These locales will not be saved in Braze.                                                                      |
| The translation file includes text blocks that don't exist in the current message (such as the current draft at the time the translations are uploaded). | The text blocks that don't exist in your current message will not be saved from the translation file to Braze. |
| Removing a locale from the message after that locale has already been uploaded to the message as part of the translation file.                           | Removing the locale will remove any translations associated with the locale in your message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
