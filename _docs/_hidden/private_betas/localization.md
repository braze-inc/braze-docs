---
nav_title: Localization
permalink: "/localization/"
hidden: true
---

# Localization

## Orchestrations

### Campaigns

{% tabs local %}
{% tab One template for all %}

In the following approach, the localization is applied to a single template in Braze using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).

The dashboard provides aggregated campaign analytics. The user level engagement can be measured using custom segment funnels.

##### Advantages 
- Centralised approach
- Reduced email build time - no need to build out an email multiple times

##### Considerations
- Manual report building
- Campaign report shows aggregated metrics rather than broken down metrics per country
- Need to thoroughly test to ensure Liquid populates exactly as expected
- Depending on how you pull in country value - it could be tricky to test each country
- Testing becomes more cumbersome when you have many countries
- Harder to accommodate if you want to schedule sends for specific times across time zones.
- Harder to accommodate if you want very separate content per country. 

{% endtab %}
{% tab One template per country %}

The templating can also be separated into sending locales, i.e., one per country. The templates benefit from implementing [Braze Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) for maintenance and tracking purposes, and the Campaigns can also inherit the configurations from the same [Braze Template]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) and [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (i.e., [Email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template?redirected=true#creating-an-email-template) built with the use of Liquid). The pre-existing campaigns and templates can also be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/) to allow a faster time time-to-value.

In this scenario, the dashboard reports sending analytics based on each country separately, and the downstream user-level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events will also be tied to a specific campaign. 

##### Advantages
- Scalable to multiple locations
- Can report on revenue per country within Braze (i.e., per campaign)
- More flexibility if there is very specific content per country / if you need a different layout per country.

##### Considerations
- Requires strategic structuring
- More build effort required - i.e., build a separate campaign for each country

{% endtab %}
{% endtabs %}

### Canvases

{% tabs local %}
{% tab One journey for all %}

It is possible to replicate the Centralised Campaign solution within [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) in tandem with Liquid to define the message for each user. The dashboard provides aggregated [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), whereas the user level engagement can be measured via custom [Segment Funnels]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_funnels/), i.e., combining [Country]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) and [Received Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) filters.

##### Advantages
- Considerations
- Centralised approach
- Reduced email build time - no need to build out an email multiple times.

##### Considerations
- Manual report building
- Canvas report shows aggregated metrics rather than broken down metrics per country
- Need to thoroughly test to ensure Liquid populates exactly as expected
- Depending on how you pull in country value - it could be tricky to test each country
- Testing becomes more cumbersome when you have many countries
- Harder to accommodate if you want to schedule sends for specific times across time zones.
- Harder to accommodate if you want very separate content per country. 

{% endtab %}
{% tab One journey per country %}

The [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) journey builder provides the flexibility of creating user journeys via multiple [Canvas Components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components). The localization efforts can be achieved in the following ways:
Separate Canvases per country - this ensures the complex user journeys are defined at the top of the funnel, i.e., via the audience filters.
Bespoke User Journeys per country - the implementation of [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) to intuitively segment users on a large scale for each journey, i.e., creating separate message threads for each country in a single canvas.

These solutions yield dynamic analytics per country directly via the dashboard and within the user level [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) events based on the customer’s current location. The Canvas can also be [duplicated]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-canvases) at the component and overall journey level.

##### Advantages
- Can report on revenue per country within Braze (i.e., per Canvas / variant / step)
- More flexibility if there is very specific content per country / if you need a different layout per country.
- Ability to add in specific delays to ensure delivery at a specific time to a country.
- Can add Push notifications and other channels as part of the journey in the future.

##### Considerations
- Requires strategic structuring
- More build effort required - i.e., build a separate message step for each country
- Canvas can become large and difficult to read if you have custom, complex journeys for each country in a single Canvas

{% endtab %}
{% endtabs %}

## Personalization

### Option 1: Manual Entry
Paste the content manually into the body of the message, and use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to [conditionally]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) display the correct language to the recipient. For example: 

{% raw %}
```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This will go to anyone who did not match the other specified languages!
{% endif %}
```
{% endraw %}

### Option 2: Content Blocks
Braze supports [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks), which are reusable blocks of content. When the block is changed, everywhere that references that block changes. For example, an email header or footer used in all emails or to house translations. These blocks can also be [created]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) and [updated]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) via REST API, and clients can programmatically upload translations. 

When building a campaign in the dashboard,  Content Blocks are referenced via the tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} - the relevant translation block can be referenced using this approach. The block could contain all the translations housed within conditional logic for each language (as in Option 1), or a separate block for each language could be utilized. 

Content Blocks can also be utilized as a Translation Management Process whereby content that requires translation is housed within a Content Block, fetched, translated, and then updated. The steps to do this are as follows: 
1. End user manually creates a Content Block in the dashboard with the tag "Needs Translation"
2. Customer's service performs a nightly fetch of all Content Blocks from the [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) endpoint
3. Customer's service fetches details on each Content Block through the [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) endpoint to see which are tagged for translation and shared with relevant agency/team members.
4. Customer/Translation Service translates the body of all "Needs Translation" content blocks for all various languages and updates to include Liquid IF statements
5. Customer's service hits our new [`/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) endpoint to update the translated content and change the tag to "Translation Completed".

### Option 3: Braze Partners
There are many translation tools available online that our clients use successfully, including [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) and [Crowdin](https://crowdin.com/). Typically clients use the platform alongside an internal team and/or translation agency. The translations are uploaded there and are then accessible via REST API. 

[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) allows clients to fetch content at the time of campaign send by calling an external REST API endpoint. In this scenario, clients can use Connected Content to call Transifex or Crowdin and fetch the required translation for your user. 

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

These examples make a call to the translation partner's (either Transifex or CrowdIn) REST API endpoint and templates in the user's {% raw %}`{{${language}}}`{% endraw %} to identify the correct translation for that user. Then, it saves it as a variable called "strings". Strings is a block of JSON, so we're fetching the translation within {% raw %}`{{strings[0].translation}}}`{% endraw %}.

### Option 4: Housing Translations in a Public Google Sheet 
Option four will see the client house translations in a public Google Sheet (this may be handled in partnership with a translation agency). This sheet will then be accessed via Connected Content (see option 3 for more info on Connected Content). The relevant translation for a user based on their language will be pulled into the campaign body at the time of sending. 
Considerations
- Google Sheets API has a limit of 500 requests per 100 seconds per project. Connected Content calls can be cached, but this solution is not scalable for a high-traffic campaign.

### Option 5: Turn a Google spreadsheet into a JSON API via Sheetdb  
This option provides an alternative method of transforming Google Sheets into JSON objects queried via Connected Content. This solution provides better accessibility to translations hosted on Google Sheets, where clients can choose from [multiple subscription tiers](https://sheetdb.io/pricing) depending on the cadence of the API calls.

The spreadsheet structure follows the same steps as the one captured in option 4, but Sheetdb also provides additional filters to query the objects as described [here](https://docs.sheetdb.io/#sheetdb-api).

Clients may prefer to implement Sheetdb with fewer Liquid & Content Block dependencies by implementing Sheetdb’s [search method](https://docs.sheetdb.io/#get-search-in-document) in GET request calls to filter the JSON objects based on {% raw %}`{{${language}}}`{% endraw %} Liquid tag to automatically return the results for a single language rather than building large conditional blocks.

#### Step 1: Build the Google sheet in the following way so that the languages are different objects

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |

#### Step 2: Implement the {% raw %}{{${language}}}{% endraw %} Liquid tag within a Connected Content call
{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}
Sheetdb will auto-generate the `sheet_id` upon creation of the spreadsheet (it’s a unique key identifier)

#### Step 3: Use Liquid to template your messages
{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}
Considerations
- The {% raw %}`{{${language}}}`{% endraw %} field has to be defined for all users; otherwise, a Liquid conditional block has to be featured as a fallback handler for users without a language.
- Data modeling within Google Sheets has to follow a different language-driven vertical as opposed to having message objects.
- Sheetdb offers a limited freemium account and multiple paying options that should be considered based on the Campaign Strategy. 
- Connected Content calls can be cached. Braze recommends measuring the projected cadence of the API calls and investigating an alternative approach of calling the main sheetdb endpoint instead of using the search method.

### Option 6: Catalogs

Catalogs allow you to access data from imported JSON objects via API and CSV files to enrich your messages, similar to custom attributes or custom event properties through Liquid.

#### Create the Catalog via API or CSV

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