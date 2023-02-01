---
nav_title: Mozart Data
article_title: Mozart Data
page_order: 1

description: "This document outlines Braze's partnership and integration steps with Mozart Data, an all-in-one modern data platform."
alias: /partners/your_partner_name/

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
| Mozart Data Account | A Mozart Data account is required to take advantage of this partnership. [Sign up using this link.](https://app.mozartdata.com/signup)|
| Snowflake Account - Option 1: New Account | During the Mozart Data account creation process, select the **Create a New Snowflake Account** option. Then, Mozart Data will provision a new Snowflake account for you. |
| Snowflake Account - Option 2: Existing Account | If your organization already has a Snowflake account, we offer the Mozart Data Connected option. Select the **Already Have a Snowflake Account** option to connect an existing Snowflake account. To pursue this option, you will need to involve a user with account-level permissions and follow the steps [in this document](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

The Integration is supported for both syncing data from [Braze to Mozart Data](#syncing-data-from-braze-to-mozart-data) and from [Mozart Data to Braze](#syncing-data-from-mozart-data-to-braze).

### Syncing Data from Braze to Mozart Data

#### Step 1: Go to the Connectors Page in Mozart Data and click "Add Connector"

Provide a short description for each step, including any code, as necessary. Remember that you can offer several different code sets - there's no need to only provide one way to integrate.

#### Step 2: Search for "Braze" and select the connector card

You also can add images to your documentation. We recommend including images of key integration steps as images do a great job of confirming what users should be seeing as they progress through the various steps.

#### Step 3: Enter a destination schema name where all of the synced data from Braze will be stored and click next.

{% alert important %} 
We recommend using the default schema name `braze`.
{% endalert %}

Outline thorough integration usage, especially if it includes inserting Liquid into our message composer. If your integration leverages a Braze webhook, we recommend including the following webhook formatting steps into your partner page.

#### Step 4: 

#### Step 5: 


### Syncing Data from Mozart Data to Braze

{% details Webhook formatting %}
```
### Step 2: Create a [Partner] webhook in Braze
To create a [Partner] webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section in the Braze platform. If you would like to create a one-off [Partner] webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.
Once you have selected the [Partner] webhook template, you should see the following:
- **Webhook URL**: [Partner Webhook URL]
- **Request Body**: Raw Text
#### Request headers and method
[Partner] requires an `HTTP Header` for authorization. The following will already be included within the template as key-value pairs.
{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Request Body**: application/json
{% endraw %}
#### Request body
Include code of your webhook request body. 
### Step 3: Preview your request
Preview your request in the **Preview** panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.
{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}
```
{% enddetails %}

## Customization

Customization is an **optional** section. Here, you could outline specific ways to customize your integration between the two partners.

## Using this integration

This section should describe how to use the integration in Braze. Let users know how to access the data (if any) provided to Braze through the integration and how to leverage it in Braze messaging.

### Step 1: Short description of step one 

This set of steps will walk your users through how to use this integration in Braze.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
