---
nav_title: Treasure Data
article_title: Treasure Data
page_order: 3.5
description: "This article outlines the partnership between Braze and Treasure, an enterprise customer data platform that allows you to write job results from Treasure Data directly to Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure data

> [Treasure Data][4] is the only enterprise Customer Data Platform (CDP) that drives relevant customer experiences by harmonizing Data, Insights, and Engagement to work in perfect unison. Treasure Data empowers brands to give millions of their customers and potential customers the feeling that each one is the one and only. Armed with these actionable indicators, CX Teams, including Marketing, Sales, and Customer Service can effectively optimize spend, and personalize omnichannel interactions across the entire customer journey.

{% include video.html id="Zqdm33TWr0E" align="right" %}

Treasure Data supports the Braze platform by allowing you to write job results from Treasure Data directly to Braze. This integration allows you to:
* __Map external ids__: Map ids from your CRM system to the Braze user account. 
* __Manage opt-out__: When an end-user updates their consent choosing not to participate.
* __Upload your tracking of events, purchases, or custom profile attributes__. This information can help you build precise customer segments that enhance the user experience for your campaigns.

## Requirements

| requirement | origin | access | description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__, __users.delete__, __users.alias.new__, __users.identify__ permissions. | These API keys support the current feature to synchronize Treasure Data profiles to Braze, including: mapping external IDs, Upload Tracking, and opt-out  |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Treasure Data Account and Account Information | Treasure Data | [https://www.treasuredata.com/custom-demo/](https://www.treasuredata.com/custom-demo/) | You must have an active Treasure Data account to utilize their services with Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Export integration

For more detail, check out the document on [Treasure Data Product Documentation][5]

### Step 1: obtain rest api key in braze

Obtain the required Braze endpoints and keys detailed in the previous requirements section. 

### Step 2: create a new connection
In Treasure Data, you must create and configure the data connection before running your query. As part of the data connection, you must provide authentication to access the integration.

1. First, open the Treasure Data console and navigate to the __Catalog__ under the __Integrations Hub__.
2. Next, search for and select __Braze__. From here, a __New Authentication__ prompt will open up.
3. Add the __Braze API Key__ and __Endpoint__ credentials to authenticate.
4. Lastly, name your connection and select __Done__.

![Treasure Data Authentication Dialog][2]{: style="max-width:80%;"}

### Step 3: define your query
1. Navigate to __Queries__ under your __Data Workbench__.
2. Select a query for which you would like to export data.
3. Run the query to validate the result set.
4. Next, select __Export Results__ and then select an existing integration authentication.
5. Define additional Export Results parameters as outlined under the Customization section below and select __Done__.
6. Run your query.
7. Validate that your data moved to the destination you specified.

## Customization

the export results parameters are described in the following table.

![Export Configuration Dialog][3]{: style="max-width:80%;"}

| Parameter | Values | Description |
|---|---|---|
| `mode` | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | Connector mode |
| `pre_formated_fields` | string | Use for array or JSON columns to keep the format. |
| `track_record_type` | Custom Events<br>Purchases<br>User Profile Attributes| Record type for __User - Track__ mode |
| `skip_on_invalid_records` | Boolean | If enabled, continue and ignore any invalid records for the JSON column. <br> Otherwise, the job stops. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Use cases

You can synchronize your consolidated customer profiles from Treasure Data into Braze to build-out target segments. Treasure Data supports 1st party cookie data, Mobile IDs, third-party systems like your CRM, and many more.

## Webhooks

treasure data users can ingest data through the public rest api. you can use treasure data to create custom webhooks into your data. to learn more, visit the [treasure data documentation][6]

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
