---
nav_title: Localization
article_title: Localization
page_order: 7
description: "This reference article covers the basics of localization, lists the benefits of different orchestration approaches across campaigns and Canvases, and lists different ways users can handle personalization in their messaging."
tool:
    - Campaigns
    - Canvas
---

# Localization

> For companies with customers in many countries, handling localization early in your Braze journey can save your companies time and resources.

## How it works

Locale information is stored on a user's profile based on data you collect using a [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/) (automatically), or [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track). The locale contains the language and a region identifier. This information is available in the Braze segmentation tool under **Country** and **Language**.

{% alert tip %}
For technical details on how locale is collected by our SDKs, refer to the official [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html), and [Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) documentation.
{% endalert %}

## Translation management

Consider the following approaches for managing your translations.

{% tabs local %}
{% tab campaign %}
### One template for all

In this approach, localization is applied to a single template in Braze using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). After sending, the dashboard provides aggregated campaign analytics. User-level engagement can be measured using custom segment funnels, for example, by combining **Country** and **Received Campaign** filters.

| Advantages | Considerations |
| --- | --- |
| - Centralized approach<br>- Reduced email build time, no need to build out an email multiple times | - Manual report building<br>- Campaign report shows aggregated metrics rather than metrics per country<br>- Need to thoroughly test Liquid to ensure it populates as expected<br>- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country<br>- Harder to schedule sends for specific times across time zones<br>- Harder to use if you want to send separate content per country. |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### One template per country 

This approach separates templating into different sending locales. After sending, the dashboard reports sending analytics based on each country separately, and any downstream user-level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events will also be tied to a specific campaign.

- Templates benefit from implementing [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) for maintenance and tracking purposes.
- Campaigns can inherit the configurations from the same [Braze template]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) and [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (such as [email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) that contain Liquid).
- Pre-existing campaigns and templates can be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/) to allow a faster time time-to-value.

| Advantages | Considerations |
| --- | --- |
| - Scalable to multiple locations<br>- Reporting on revenue per country within Braze (such as per campaign)<br>- Flexibility if there is drastically different content per country | - Requires strategic structuring<br>- More build effort required (such as separate campaigns for each country) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### One journey for all

In this approach, localization is handled within [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) and Liquid to define messaging for each user. 

After a Canvas is sent, the dashboard provides aggregated [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), whereas the user level engagement can be measured via custom [segment funnels]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/), such as combining [**Country**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) and [**Received Canvas Step**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) filters.

| Advantages | Considerations |
| --- | --- |
| - Centralized approach<br>- Reduced email build time - no need to build out an email multiple times. | - Manual report building<br>- Canvas report shows aggregated metrics rather than metrics per country<br>- Need to thoroughly test Liquid to ensure it populates as expected<br>- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country<br>- Harder to schedule sends for specific times across time zones<br>- Harder to use if you want to send separate content per country. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### One journey per country

In this approach, the [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) journey builder provides the flexibility of creating user journeys via multiple [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). These components can be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating) at the component and overall journey level.

Localization can be achieved with the following methods:

- Separate Canvases per country, this ensures the complex user journeys are defined at the top of the funnel using audience filters
- Bespoke user journeys per country, the implementation of [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) to intuitively segment users on a large scale for each journey by creating separate message threads for each country in a single Canvas

Once sent, the dashboard provides dynamic analytics per country and within user-level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events based on the customer’s current location.

| Advantages | Considerations |
| --- | --- |
| - Reporting on revenue per country within Braze (such as per Canvas, variant, or step)<br>- Flexibility if there is drastically different content per country<br>- Can add other channels as part of the journey in the future | - Requires strategic structuring<br>- More build effort required (such as separate message steps for each country)<br>- Canvas can become large and difficult to read if you have custom, complex journeys for each country in a single Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Sending translated messages

To send personalized messages based on a user's language, locale, or custom attributes, use one of the following methods.

### Translation Liquid tags (recommended) {#translation-liquid-tag}

Braze supports a {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} Liquid tag to target users in different languages with a single message. 

For a full walkthrough, refer to the [guide on using translation tags]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales).
  
### Alternative approaches

{% tabs local %}
{% tab Custom Liquid %}
You can manually paste your content into the body of your message and use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to [conditionally]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) display the correct language to the recipient. To do this:

1. Compose your message, then select **Language** to generate Liquid conditional logic for each of your selected languages.
2. You can use the following Liquid template to help build out your message. For each field with templating, you should enter the variations after the bracketed segment of templating. The variation should correspond to the language code referenced in the brackets before it.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Test your message before sending it by entering a user's ID or email to check how a message would appear to an individual depending on their language. 

{% alert tip %}
We always recommend including a {% raw %}`{% else %}`{% endraw %} statement in your messaging. While most users will see messaging for their specific language, the text will be visible to those that:
- Do not have a language selected
- Have a language that Braze does not support
- Have a device where the language is undetectable
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Braze [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) are reusable blocks of content. When a block is changed, all references to that block changes. For example, updates to an email header or footer will be reflected in all emails or to house translations. These blocks can also be [created]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) and [updated]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) using the REST API, and users can programmatically upload translations. 

When building a campaign in the dashboard, Content Blocks can be referenced using tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. These blocks could contain all translations housed within conditional logic for each language, as shown in option 1, or a separate block for each language can be used.

Content Blocks can also be utilized as a translation management process where content that requires translation is housed within a Content Block, fetched, translated, and then updated:
1. Manually create a Content Block in the dashboard with the tag "Needs Translation".
2. Your service performs a nightly fetch of all Content Blocks using the [`/content_blocks/list` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Your service fetches details on each Content Block through the [`/content_blocks/info` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) to see which blocks are tagged for translation.
4. Your translation service translates the body of all "Needs Translation" Content Blocks.
5. Your service hits the [`/content_block/update` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) to update translated content and update the tag to "Translation Complete".
{% endtab %}

{% tab Catalogs %}
[Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/) allow you to access data from imported JSON objects via API and CSV files to enrich your messages, similar to custom attributes or custom event properties through Liquid. For example:

{% subtabs local %}
{% subtab API %}

Create a catalog via the following API call:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Add items via the following API call:

```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Create a CSV in the following format:

| id | context | language | body |
| --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

These catalog items can them be referenced using [personalization]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#using-catalogs-in-a-message), shown below, or [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) that allow you to create groups of data. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Braze partners %}
Many Braze partners offer localization solutions, including [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) and [Crowdin](https://crowdin.com/). Typically users use the platform alongside an internal team and translation agency. These translations are then uploaded there and are then accessible via REST API. These services also often leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), allowing users to fetch the translations via API.

For example, the following Connected Content calls call Transifex and Crowdin to fetch a translation, leveraging {% raw %}`{{${language}}}`{% endraw %} to identify the correct translation for a given user. This translation is then saved in the JSON block "strings" and referenced.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
Host translations in a spreadsheet, then use one of the following methods to send your message in the relevant language.

{% subtabs local %}
{% subtab Connected Content %}
You can with a translation agency to store translations in a Google spreadsheet, then query this content using [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). When you send a message, the relevant translation for each user will be pulled into your campaign body based on their selected language. 

{% alert note %}
The Google Sheets API has a limit of 500 requests per 100 seconds per project. Connected Content calls can be cached, but this solution is not scalable for a high-traffic campaign.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
This option provides an alternative method of transforming Google Sheets into JSON objects queried via Connected Content. By turning a spreadsheet into a JSON API via SheetDB, you can choose from [multiple subscription tiers](https://sheetdb.io/pricing) depending on the cadence of the API calls.

The spreadsheet structure follows the steps in option 4, but SheetDB also provides [additional filters](https://docs.sheetdb.io/#sheetdb-api) to query the objects.

Some users may prefer to implement SheetDB with fewer Liquid and Connected Block dependencies by implementing SheetDB's [search method](https://docs.sheetdb.io/#get-search-in-document) in GET request calls to filter the JSON objects based on {% raw %}`{{${language}}}`{% endraw %} Liquid tag to automatically return the results for a single language rather than building large conditional blocks.

#### Step 1: Format the Google sheet

First, build out the Google sheet so that the languages are different objects:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### Step 2: Use the language Liquid tag in a Connected Content call

Next, implement the {% raw %}`{{${language}}}`{% endraw %} Liquid tag within a Connected Content call. Note that SheetDB will auto-generate the `sheet_id` upon creating the spreadsheet.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Step 3: Template your messages

Lastly, use Liquid for templating your messages:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considerations

- The {% raw %}`{{${language}}}`{% endraw %} field has to be defined for all users; otherwise, a Liquid conditional block has to be featured as a fallback handler for users without a language.
- Data modeling within Google Sheets has to follow a different language-driven vertical as opposed to having message objects.
- SheetDB offers a limited free account and multiple paying options that should be considered based on your campaign strategy. 
- Connected Content calls can be cached. We recommend measuring the projected cadence of the API calls and investigating an alternative approach of calling the main SheetDB endpoint instead of using the search method.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
