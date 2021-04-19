---
nav_title: Treasure Data
page_order: 4

description: "Connect your first party data from Treasure Data CDP directly to Braze"

alias: /partners/treasure_data/

page_type: partner
hidden: false
---

# Treasure Data

> Treasure Data is the only enterprise Customer Data Platform (CDP) that drives relevant customer experiences by harmonizing Data, Insights and Engagement to work in perfect unison. Treasure Data empowers brands to give millions of their customers and potential customers the feeling that each one is the one and only. Armed with these actionable indicators, CX Teams, including Marketing, Sales and Customer Service can effectively optimize spend, and personalize omni-channel interactions across the entire customer journey. To learn more, visit [Treasure Data][4].

Watch our video to learn why we are the industry’s best at transforming customer experiences, one brand at a time.

{% include video.html id="Zqdm33TWr0E" %}


Treasure Data supports the Braze platform by allowing you to write job results from Treasure Data directly to Braze.  What can you do with this Integration?
* Map external ids: For example, you can map ids from your CRM system to the Braze user account. 
* Opt-out: When an end-user updates the consent choosing not to participate.
* Upload your own tracking of events, purchases, or custom profile attributes. This information can help you build precise customer segments that enhance the user experience for your campaigns.


## Requirements and Pre-Requisites

An account and basic knowledge of Braze.
An account and basic Knowledge of Treasure Data.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__, __users.delete__, __users.alias.new__, __users.identify__ permissions. | These API keys support the current feature to synchronize Treasure Data profiles to Braze, including: mapping external IDs, Upload Tracking, and opt-out  |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Export Integration

For more detail, check out the document on [Treasure Data Product Documentation][5]

### Step 1: Obtain Rest API Key in Braze

See the list of scopes in the Requirements section

### Step 2: Create a new Connection In Treasure Data
n Treasure Data, you must create and configure the data connection before running your query. As part of the data connection, you provide authentication to access the integration.

1. Open TD Console.
1. Navigate to Integrations Hub > Catalog.
1. Search for and select Braze.
1. Type the credentials to authenticate.
![Treasure Data Authentication Dialog][2]
1. Type a name for your connection.
1. Select Done.

### Step 3: Define your Query
1. Complete the instructions in Step 2.
1. Navigate to Data Workbench > Queries.
1. Select a query for which you would like to export data.
1. Run the query to validate the result set.
1. Select Export Results.
1. Select an existing integration authentication.

1. Define additional Export Results parameters as outlined under Customization.

1. Select Done.
1. Run your query.
1. Validate that your data moved to the destination you specified.

## Customization

The export results parameters are described in the table following the image.
![Export Configuration Dialog][3]

| Parameter | Values | Description |
|---|---|---|
| mode | user_new_alias<br>user_identifying<br>user_track<br>user_delete | Connector mode |
| pre_formated_fields | string | Use for array or JSON columns to keep the format. |
| track_record_type	 | custom_events<br>purchases<br>user_profile_attributes	 | Record type for user_track mode |
| skip_on_invalid_records	 | Boolean | If enabled, continue and ignore the fail records for the JSON column. <br> Otherwise, the job stops. |


## Use Cases

You can synchronize your consolidated customer profiles from Treasure Data into Braze to build the target segment. Treasure Data supports 1st party cookie data, Mobile IDs, third party system like your CRM, and many more.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
