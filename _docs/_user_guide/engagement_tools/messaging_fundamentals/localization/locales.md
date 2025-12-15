---
nav_title: Locales in messages
article_title: Locales in messages
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "This article provides steps on how to use locales in your messages."
---

# Locales in messages



{% multi_lang_include locales.md section="Prerequisites" %}

## Using locales

### 1. Set up locales in your workspace {#workspace-setup}

Before locales and translation tags can be used, you must first [add locales to your workspace]({{ site.baseurl }}/user_guide/administrative/app_settings/multi_language_settings).

### 2. Add translation liquid tags to your message {#add-translation-tags}

Add translation tags {% raw %}`{% translation your_id_here %}` and `{% endtranslation %}`{% endraw %} to wrap all text, image, or link URLs that you will be translating.

Each translation should have a unique `id`. For example, when translating a simple greeting, you may name the ID "greeting":

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localizing HTML blocks
A more complicated paragraph may have multiple translation tags ("offer_text" and "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Wrapping large HTML blocks may have unintended consequences related to stylesheet and styling. Try to only wrap as small text sections as possible.
{% endalert %}

#### Localizing Links

To localize anchor tag links, be sure to wrap the entire `href` URL attribute. If you only wrap a part of the URL, link templating may not function correctly.


{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}">
  {% translation link_text %}Click Me{% endtranslation %}
</a>
```
{% endraw %}

### 3. Choose message locales {#choose-locales}

Once your translation tags are in the message choose your locales for this message.

In the dropdown, select one or more locales which you plan to translate.

![List of locales][todo]

To access this menu, go to the message's Multi-Language setting:

{% tabs %}
{% tab Email %}
Select **Multi-Language** from the Content menu when editing your message.

![][todo]

{% endtab %}

{% tab Push %}
Select **Manage Languages** when editing your message.

![][todo]

{% endtab %}

{% tab In-App Message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Select **Manage Languages** at the bottom of the **Build** section.

![][todo]

{% endsubtab %}
{% subtab Traditional Editor %}

Select **Manage Languages** when editing your message.

![][todo]

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Select **Manage Languages** when editing your message.
{% endtab %}

### 4. Download CSV template {#download-csv}

Once you've selected your locales, download a CSV template containing a matrix of translation IDs and locales selected.

![Example CSV][todo]


### 5. Upload a completed CSV {#upload-csv}

{% alert important %}
Any changes to the IDs or locales in the CSV file will not automatically update in your message. To update the translations, update the CSV file and re-upload the file.
{% endalert %}

The completed CSV is in the following format:

```csv
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### 6. Preview Locales {#preview-locales}

When previewing your message, choose the **Multi-Language User** option from the "Preview as User" dropdown.

This lets you switch between different locale definitions to preview all translations of your message.

![locale previews][]

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

### Using the multi-language API with Canvases

To use the [multi-language API with Canvases]({{site.baseurl}}/api/endpoints/translations/), you must include the `workflow_id`, `step_id`, and `message_variation_id` in the parameter list.

#### Canvas steps added to post-launch drafts

When using the multi-language API with Canvas steps that were created after the Canvas has been launched, the `message_variation_id` that you pass into the API will be empty or blank.

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
| A translation file is missing text blocks, such as a text within Liquid translation tags, from the current email message.                                | This translation file won't be uploaded.                                                                       |
| The translation file includes the default text that doesn't match the text blocks in the current email message.                                          | This translation file won't be uploaded. Fix this in your CSV before attempting to upload again.               |
| The translation file includes locales that don't exist in **Multi-Language Support** settings.                                                           | These locales will not be saved in Braze.                                                                      |
| The translation file includes text blocks that don't exist in the current message (such as the current draft at the time the translations are uploaded). | The text blocks that don't exist in your current message will not be saved from the translation file to Braze. |
| Removing a locale from the message after that locale has already been uploaded to the message as part of the translation file.                           | Removing the locale will remove any translations associated with the locale in your message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
