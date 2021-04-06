---
nav_title: Treasure Data
page_order: 4

description: "Treasure Data is the only independent CDP with proven experience in solving the most complex data problems for the enterprise. We have 170+ connectors to work with any existing technology stack and are schema-flexible to ingest all types of data. We deliver enterprise-level security, scalability and continuity so you can unlock the power of customer data to deliver stellar brand experiences at scale.
Watch our video to learn why we are the industry’s best at transforming customer experiences, one brand at a time."
alias: /partners/treasure_data/

page_type: partner
hidden: false
---

# Treasure Data

> Treasure Data is the only independent CDP with proven experience in solving the most complex data problems for the enterprise. We have 170+ connectors to work with any existing technology stack and are schema-flexible to ingest all types of data. We deliver enterprise-level security, scalability and continuity so you can unlock the power of customer data to deliver stellar brand experiences at scale.https://www.treasuredata.com/

Treasure Data supports the Braze platform by allowing you to write job results from Treasure Data directly to Braze.  What can you do with this Integration?
* Map external ids: For example, you can map ids from your CRM system to the Braze user account. 
* Opt-out: When an end-user updates the consent choosing not to participate.
* Upload your own tracking of events, purchases, or custom profile attributes. This information can help you build precise customer segments that enhance the user experience for your campaigns.


## Requirements or Pre-Requisites

An account and Basic knowledge of Braze.
An account and Basic Knowledge of Treasure Data.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__, __users.delete__, __users.alias.new__, __users.identify__ permissions. | These API keys support the current feature to synchronize Treasure Data profiles to Braze, including: mapping external IDs, Upload Tracking, and opt-out  |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Export Integration

### Step 1: Obtain Rest API Key in Braze

See the list of scopes in the Requirements section

### Step 2: Create a new Connection
n Treasure Data, you must create and configure the data connection before running your query. As part of the data connection, you provide authentication to access the integration.

1. Open TD Console.
1. Navigate to Integrations Hub > Catalog.
1. Search for and select Braze.
1. Type the credentials to authenticate.

You have the option to put images in your documentation, so we recommend you do and do so mindfully.

### Step 3: Define your Query
1. Complete the instructions in Step 2
1. Navigate to Data Workbench > Queries.
1. Select a query for which you would like to export data.
1. Run the query to validate the result set.
1. Select Export Results.
1. Select an existing integration authentication.

1. Define any additional Export Results details. In your export integration content review the integration parameters. For example, your Export Results screen might be different, or you might not have additional details to fill out:

1. Select Done.
1. Run your query.
1. Validate that your data moved to the destination you specified.

## Customization

The export results parameters are described in the table following the image.

| Parameter | Values | Description |
|---|---|---|
| mode | user_new_alias<br>user_identifying<br>user_track<br>user_delete | Connector mode |
| pre_formated_fields | string | Use for array or JSON columns to keep the format. |
| track_record_type	 | custom_events<br>purchases<br>user_profile_attributes	 | Record type for user_track mode |
| skip_on_invalid_records	 | Boolean | If enabled, continue and ignore the fail records for the JSON column. <br> Otherwise, the job stops. |


## Use Cases

You can synchronize your consolidated customer profiles from Treasure Data into Braze to build the target segment. Treasure Data supports 1st party cookie data, Mobile IDs, third party system like your CRM, and many more.

[1]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
