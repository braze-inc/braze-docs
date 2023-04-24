---
nav_title: Localization
permalink: "/localization/"
hidden: true
description: "The article outlines the benefits of different orchestration approaches across campaigns and Canvases and lists different ways users can handle personalization in their messaging."

---

# Localization

For companies with customers in many countries, handling localization early on in your Braze journey can be important in saving your companies time and resources. The following article lists the benefits of different orchestration approaches across campaigns and Canvases and also lists different ways users can handle personalization in their messaging.

- **Orchestration options**
	- [Campaigns](#campaigns) (one template for all vs. one template per country)
	- [Canvas](#canvas) (one journey for all vs. one journey per country)<br><br>
- **Personalization options**
	- [Manual entry](#option-1-manual-entry)
	- [Content Blocks](#option-2-content-blocks)
	- [Localization partners](#option-3-braze-localization-partners)
	- [Housing translations in a public Google Sheet](#option-4-housing-translations-in-a-public-google-sheet)
	- [Turn a Google spreadsheet into a JSON API via Sheetdb](#option-5-turn-a-google-spreadsheet-into-a-json-api-via-sheetdb)
	- [Catalogs](#option-6-catalogs)

## Orchestration

### Campaigns

{% tabs local %}
{% tab One template for all %}

In the "one template for all" approach, localization is applied to a single template in Braze using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).

Once sent, the dashboard provides aggregated campaign analytics. User-level engagement can be measured using custom segment funnels, for example, by combining **Country** and **Received Campaign** filters.

| Advantages | Considerations |
| --- | --- |
| - Centralized approach<br>- Reduced email build time, no need to build out an email multiple times | - Manual report building<br>- Campaign report shows aggregated metrics rather than metrics per country<br>- Need to thoroughly test Liquid to ensure it populates as expected<br>- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country<br>- Harder to schedule sends for specific times across time zones<br>- Harder to use if you want to send separate content per country. |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab One template per country %}

The "one template per country" approach separates templating into different sending locals.

Once sent, dashboard reports sending analytics based on each country separately, and any downstream user-level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events will also be tied to a specific campaign. 

- Templates benefit from implementing [Braze Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) for maintenance and tracking purposes.
- Campaigns can inherit the configurations from the same [Braze Template]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) and [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (i.e., [Email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template?redirected=true#creating-an-email-template) built with the use of Liquid).
- Pre-existing campaigns and templates can be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/) to allow a faster time time-to-value.

| Advantages | Considerations |
| --- | --- |
| - Scalable to multiple locations<br>- Reporting on revenue per country within Braze (i.e., per campaign)<br>- Flexibility if there is drastically different content per country | - Requires strategic structuring<br>- More build effort required (i.e., separate campaigns for each country) |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Canvases

{% tabs local %}
{% tab One journey for all %}

In the "one journey for all" approach, localization is handled within [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) and Liquid to define messaging for each user. 

Once sent, the dashboard provides aggregated [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), whereas the user level engagement can be measured via custom [Segment Funnels]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_funnels/), i.e., combining [**Country**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) and [**Received Canvas Step**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) filters.

| Advantages | Considerations |
| --- | --- |
| - Centralized approach<br>- Reduced email build time - no need to build out an email multiple times. | - Manual report building<br>- Canvas report shows aggregated metrics rather than metrics per country<br>- Need to thoroughly test Liquid to ensure it populates as expected<br>- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country<br>- Harder to schedule sends for specific times across time zones<br>- Harder to use if you want to send separate content per country. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab One journey per country %}

In the "one journey per country" approach, the [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) journey builder provides the flexibility of creating user journeys via multiple [Canvas Components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components). These componenets can even be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-canvases) at the component and overall journey level.

Localization can be achieved through the following methods:
- Separate Canvases per country, this ensures the complex user journeys are defined at the top of the funnel using audience filters
- Bespoke user journeys per country, the implementation of [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) to intuitively segment users on a large scale for each journey by creating separate message threads for each country in a single Canvas

Once sent, the dashboard provides dynamic analytics per country and within user-level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events based on the customer’s current location.

| Advantages | Considerations |
| --- | --- |
| - Reporting on revenue per country within Braze (i.e., per Canvas, variant, or step)<br>- Flexibility if there is drastically different content per country<br>- Can add other channels as part of the journey in the future | - Requires strategic structuring<br>- More build effort required (i.e., separate message steps for each country)<br>- Canvas can become large and difficult to read if you have custom, complex journeys for each country in a single Canvas. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Personalization

### Option 1: Manual entry

Manual entry requires you manually paste your content into the body of your message and use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to [conditionally]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) display the correct language to the recipient.

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

### Option 2: Content Blocks

Braze [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) are reusable blocks of content. When a block is changed, everywhere that references that block changes. For example, an email header or footer used in all emails or to house translations. These blocks can also be [created]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) and [updated]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) using the REST API, and users can programmatically upload translations. 

When building a campaign in the dashboard, Content Blocks can be referenced using tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. These blocks could contain all translations housed within conditional logic for each language, as shown in option 1, or a separate block for each language can be utilized.

Content Blocks can also be utilized as a translation management process where content that requires translation is housed within a Content Block, fetched, translated, and then updated:
1. Manually create a Content Block in the dashboard with the tag "Needs Translation".
2. Your service performs a nightly fetch of all Content Blocks using the [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) endpoint.
3. Your service fetches details on each Content Block through the [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) endpoint to see which blocks are tagged for translation.
4. Your translation service translates the body of all "Needs Translation" Content Blocks.
5. Your service hits the [`/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) endpoint to update translated content and update the tag to "Translation Complete".

### Option 3: Localization partners

Many Braze partners offer localization solutions, including [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) and [Crowdin](https://crowdin.com/). Typically users use the platform alongside an internal team and translation agency. These translations are then uploaded there and are then accessible via REST API. These services also often leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), allowing users to fetch the translations via API.

For example, the following Connected Content calls call Transifex and Crowdin to fetch a translation, leveraging {% raw %}`{{${language}}}`{% endraw %} to identify the correct translation for a given user. This translation is then saved in the JSON block "strings" and referenced.

{% tabs local %}
{% tab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endtab %}
{% tab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Option 4: Housing translations in a public Google Sheet 

Another translation option includes housing translations in Google Sheets; often, this may be handled in partnership with a translation agency. Translations housed here can be queried using Connected Content. Relevant translation for a user based on their language will then be pulled into the campaign body at the time of sending. 

{% alert note %}
The Google Sheets API has a limit of 500 requests per 100 seconds per project. Connected Content calls can be cached, but this solution is not scalable for a high-traffic campaign.
{% endalert %}

### Option 5: Turn a Google spreadsheet into a JSON API via Sheetdb  

This option provides an alternative method of transforming Google Sheets into JSON objects queried via Connected Content. By turning a spreadsheet into a JSON API via Sheetdb, you can choose from [multiple subscription tiers](https://sheetdb.io/pricing) depending on the cadence of the API calls.

The spreadsheet structure follows the steps captured in option 4, but Sheetdb also provides [additional filters](https://docs.sheetdb.io/#sheetdb-api) to query the objects.

Some users may prefer to implement Sheetdb with fewer Liquid and Connected Block dependencies by implementing Sheetdb’s [search method](https://docs.sheetdb.io/#get-search-in-document) in GET request calls to filter the JSON objects based on {% raw %}`{{${language}}}`{% endraw %} Liquid tag to automatically return the results for a single language rather than building large conditional blocks.

#### Step 1: Format the Google sheet

First, build out the Google sheet so that the languages are different objects:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |

#### Step 2: Use the language Liquid tag in a Connected Content call

Next, implement the {% raw %}{{${language}}}{% endraw %} Liquid tag within a Connected Content call. Note that Sheetdb will auto-generate the `sheet_id` upon creating the spreadsheet.

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
- Sheetdb offers a limited freemium account and multiple paying options that should be considered based on your campaign Strategy. 
- Connected Content calls can be cached. Braze recommends measuring the projected cadence of the API calls and investigating an alternative approach of calling the main Sheetdb endpoint instead of using the search method.

### Option 6: Catalogs

Catalogs allow you to access data from imported JSON objects via API and CSV files to enrich your messages, similar to custom attributes or custom event properties through Liquid. For example:

{% tabs local %}
{% tab API %}

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
{% endtab%}
{% tab CSV %}
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

{% endtab %}
{% endtabs %}