---
nav_title: Mozart Data
article_title: Mozart Data
page_order: 1

description: "This document outlines Braze's partnership and integration steps with Mozart Data, an all-in-one modern data platform."
alias: /partners/mozartdata/

page_type: partner
search_tag: Partner
hidden: true

---
{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

# Mozart Data

> [Mozart Data](https://mozartdata.com/) is an all-in-one modern data platform powered by Fivetran, Portable, and Snowflake. We empower customers to centralize, clean, and analyze their data in all one place.


The Braze integration with Mozart Data allows you to:
- Use Fivetran to import Braze data into Snowflake cloud data warehouse in minutes
- Create transforms by coming the Braze data with the data from all of your other applications and effectively analyze user behaviors
- Import data from the Snowflake data warehouse into Braze to create new customer engagement opportunities based
- Combine Braze data with the data from all of your other applications to gain a more holistic understanding of user behaviors
- Integrate with a business intelligence tool to further explore the data that is stored in Snowflake data warehous


## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Mozart Data Account | A Mozart Data account is required to take advantage of this partnership. [Sign up here.](https://app.mozartdata.com/signup)|
| Snowflake Account - Option 1: New Account | During the Mozart Data account creation process, select the **Create a New Snowflake Account** option. Then, Mozart Data will provision a new Snowflake account for you. |
| Snowflake Account - Option 2: Existing Account | If your organization already has a Snowflake account, we offer the Mozart Data Connected option. Select the **Already Have a Snowflake Account** option to connect an existing Snowflake account. To pursue this option, you will need to involve a user with account-level permissions and follow the steps [in this document](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2}


## Integration

The Integration is supported for both syncing data from [Braze to Mozart Data](#syncing-data-from-braze-to-mozart-data) and from [Mozart Data to Braze](#syncing-data-from-mozart-data-to-braze).


### Syncing Data from Braze to Mozart Data

#### Step 1: Go to the Connectors Page in Mozart Data and click "Add Connector"
![]({% image_buster /assets/img/mozartdata/mozartdata-braze-connector-add.png %})


#### Step 2: Search for "Braze" and select the connector card
![]({% image_buster /assets/img/mozartdata/mozartdata-braze-connector-select.png %})


#### Step 3: Enter a destination schema name where all of the synced data from Braze will be stored and click "Add Connector"
{% alert important %} 
We recommend using the default schema name `braze`.
{% endalert %}
![]({% image_buster /assets/img/mozartdata/mozartdata-braze-connector-schema.png %})


#### Step 4: You will be redirected to a Fivetran connector page. Click "Continue" to complete the Fivetran connector
Mozart Data is powered by Fivetran. Within the Fivetran connector form, fill out the given fields.
![]({% image_buster /assets/img/mozartdata/mozartdata-braze-fivetran.png %})


#### Step 5: Click "Save & Test"
Fivetran will begin syncing data from your Braze account to your Snowflake data warehouse. You will be able to access and query the data from Mozart Data once the connector has finished syncing data.


### Syncing Data from Mozart Data to Braze
Please note, as Mozart Data is powered by Snowflake, the steps below resemble the instructions from the [Cloud Data Ingestion for Snowflake page](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/snowflake/) in the [Braze User Guide](https://www.braze.com/docs/user_guide/introduction).

#### Step 1: Use the Braze user guide to set up a table, user, and permissions from the Snowflake interface
{% alert important %} 
This step requires a Snowflake user with admin-level access.
{% endalert %}

[Step-by-step instructions from Braze](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/snowflake/)

#### Step 2: After setting up your Snowflake data warehouse, go to the Integrations Page in Mozart Data and select Braze

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %})


#### Step 3: Go to technology partners... page
Copy the credentials as displayed above from Mozart Data and paste in the Snowflake Data Imports. Click "Set up sync details" and input the information for your Snowflake account and source table.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %})


#### Step 4: Configure sync details
You will choose a name for your sync, input contact emails to notify of any integration errors, the data type, and the sync frequency.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %})


#### Step 5: Add a public key to the Braze user
At this point, you will need to go back to Snowflake to complete the setup. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake.

For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, we can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Step 6: Test connection

Once the user is updated with the public key, return to the Braze dashboard and click **Test connection**. If successful, you’ll see a preview of the data. If for some reason, we can’t connect, we’ll display an error message to help you troubleshoot the issue.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %})

{% alert note %}
You must successfully test an integration before it can move from Draft into Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}


## Using this integration

### How to access Braze data as a Mozart Data user
If you successfully created a Mozart Data account, you will be able to access all of your Braze data synced to your Snowflake data warehouse from Mozart Data.

#### Transforms
Mozart Data offers a SQL transformation layer to allow users to create a view or table. You can create a user-level dimension table (e.g. `dim_users`) to summarize each user's product usage data, transactional history, and engagement activities with Braze messages. 

#### Analysis
Using the transform models or raw data synced from Braze, you can perform an analysis on users' engagement with Braze messages. Additionally, you can combine the Braze data with other data from all of your applications and analyze how the insights you gained from users' interaction with the Braze messages relate to other data that you may have about the users, such as their demographic information, shopping history, product usage, and customer service engagement. 

This can help you make more informed decision about engagement strategies to improve user retention. This can all be done within Mozart Data's interface using the Query tool, where you can also export the results in to a Google Sheet or csv to prepare for a presentation.

#### Business Intelligence (BI)
Ready to visualize and share your insights with other team members? We integrate with almost every BI tool. If you do not already have a BI tool, reach out to Mozart Data to set up a free Metabase acccount. 
