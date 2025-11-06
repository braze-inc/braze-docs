---
nav_title: Mozart Data
article_title: Mozart Data
description: "This reference article outlines the partnership between Braze and Mozart Data, an all-in-one modern data platform, allowing you to use Fivetran to import data to Snowflake, create transforms, combine data, and more."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) is an all-in-one modern data platform powered by Fivetran, Portable, and Snowflake.

The Braze and Mozart Data integration allows you to:
- Use Fivetran to import Braze data into Snowflake
- Create transforms by combining Braze data with other applications data and effectively analyze user behaviors
- Import data from Snowflake into Braze to create new customer engagement opportunities
- Combine Braze data with other applications data to gain a more holistic understanding of user behaviors
- Integrate with a business intelligence tool to further explore the data that is stored in Snowflake

## Prerequisites

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Requirement | Description |
| ----------- | ----------- |
| Mozart Data account | A Mozart Data account is required to take advantage of this partnership. [Sign up here.](https://app.mozartdata.com/signup)|
| Snowflake Account<br>Option 1: New Account | Select **Create a New Snowflake Account** during the Mozart Data account creation process for Mozart Data to provision a new Snowflake account for you. |
| Snowflake Account<br>Option 2: Existing Account | If your organization already has a Snowflake account, you can use the Mozart Data Connected option.<br><br>Select the **Already Have a Snowflake Account** option to connect an existing Snowflake account. To pursue this option, a user with account-level permissions must [follow these steps](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

The integration is supported for both syncing data from [Braze to Mozart Data](#syncing-data-from-braze-to-mozart-data) and [Mozart Data to Braze](#syncing-data-from-mozart-data-to-braze).

### Syncing data from Braze to Mozart Data

#### Step 1: Set up Braze connector

1. In Mozart Data, go to **Connectors** and click **Add Connector**.
2. Search for "Braze" and select the connector card.
3. Enter a destination schema name where all of the synced data from Braze will be stored. We recommend using the default schema name `braze`.
4. Click **Add Connector**.

#### Step 2: Fill out the Fivetran connector form

You will be redirected to the Fivetran connector page. On this page, fill out the given fields. Next, click **Continue** > **Save & Test** to complete the Fivetran connector.

Fivetran will begin syncing data from your Braze account to your Snowflake data warehouse. You can access query data from Mozart Data after the connector has finished syncing. 

### Syncing data from Mozart Data to Braze

#### Step 1: Set up a Snowflake data warehouse

Follow the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) instructions to set up a table, user, and permission from the Snowflake interface. Note that this step requires admin-level Snowflake access.

#### Step 2: Set up your Snowflake integration in Braze

After setting up your Snowflake warehouse, in Mozart Data, go to the **Integration** page and select **Braze**. Here, you will find the credentials you will need to provide Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Next, while signed into Braze, go to **Integrations > Technology Partners > Snowflake** to begin the integration process. Copy the credentials from Mozart Data and add them to the Snowflake Data import page. Click **Set up sync details** and input your Snowflake account and source table information. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Next, choose a name for your sync, provide contact emails, and select a data type and a sync frequency. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Step 3: Add a public key to the Braze user
At this point, you will need to go back to Snowflake to complete the setup. Add the public key displayed on the Braze dashboard to the user you created for Braze to connect to Snowflake.

For additional information on how to do this, see the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). If you want to rotate the keys at any point, Mozart Data can generate a new key pair and provide you with the new public key.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Step 4: Test connection

Once the user is updated with the public key, return to the Braze dashboard and click **Test connection**. If successful, you'll see a preview of the data. If, for some reason, the connection is unsuccessful, an error message will display to help troubleshoot the issue.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
You must successfully test an integration before it can move from Draft to Active state. If you need to close out of the creation page, your integration will be saved, and you can revisit the details page to make changes and test.  
{% endalert %}

## Using this integration

### How to access Braze data as a Mozart Data user
Upon successfully creating a Mozart Data account, you can access your Braze data synced to your Snowflake data warehouse from Mozart Data.

#### Transforms
Mozart Data offers a SQL transformation layer to allow users to create a view or table. You can create a user-level dimension table (for example, `dim_users`) to summarize each user's product usage data, transactional history, and engagement activities with Braze messages. 

#### Analysis
Using the transform models or raw data synced from Braze, you can analyze users' engagement with Braze messages. Additionally, you can combine the Braze data with other application data and analyze how the insights you gained from users' interaction with the Braze messages relate to other data you may have about the users. For example,  their demographic information, shopping history, product usage, and customer service engagement. 

This can help you make more informed decisions about engagement strategies to improve user retention. This can all be done within Mozart Data's interface using the Query tool, where you can export the results into a Google Sheet or CSV to prepare for a presentation.

#### Business intelligence (BI)
Ready to visualize and share your insights with other team members? Mozart Data integrates with almost every BI tool. If you do not already have a BI tool, contact Mozart Data to set up a free Metabase account.