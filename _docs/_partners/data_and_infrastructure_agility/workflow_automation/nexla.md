---
nav_title: Nexla
article_title: Nexla
page_order: 1
description: "Braze Currents and Nexla make data accessible across your entire ecosystem to the data warehouse of your choice."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) is the leader in unified data operations and a 2021 Gartner Cool Vendor. The Nexla platform makes it simple for anyone to create scalable data flows. Teams working with data get a no/low-code unified experience to integrate, transform, provision, and monitor data for any use case. Nexla lowers the technical expertise needed to understand and use data. It delivers zero-friction, governed data operations, better collaboration, and agility for business and data teams.

Customers that use [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) to send data to data warehouses can leverage Nexla to extract, transform, and load that data to other locations, making data easily accessible across your entire ecosystem. Nexla enables you to use Braze Currents to get data in a custom format delivered to your destination of choice by a simple point and click.

## Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | Save this API key to input into Nexla as part of your Braze credentials. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Save your REST Endpoint to input into Nexla as part of your Braze credentials. |
| Nexla Account | Nexla | [Start your Free Trial] [2] | Access to the Nexla platform and a Nexla account are required to use Braze connectors. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

Integrating with Braze is simple on Nexla. Once you've created an account and logged on to the platform, Braze connectors come ready for production out of the box. Simply select the connector, add your Braze credentials, and immediately begin integrating, preparing, and monitoring your data in any format.

### Step 1: Create a Nexla account

If you do not already have a Nexla account, head to the Nexla [website](https://www.nexla.com) to request a free demo and trial. Next, log on to [www.dataops.nexla.io](https://www.dataops.nexla.io) and sign on with your new credentials.

### Step 2: Add your source

#### If Braze is your data source: 
1. Navigate to __Flows > Create a New Flow__ on the left toolbar.
2. Click __Create New Source__, and select the Braze connector. 
3. Click __Next__, then __Add a New Credential__. 
4. Name the credential, and add your Braze API key and REST endpoint, and click __Save__.
5. Next, select your data and click __Save__. 
Nexla will now search the source for any data it finds and generate a [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) for transformation or sending to destination.

#### If Braze is your destination
Visit Nexla documentation on [connecting sources to Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Step 3: Transform (optional)

If you want to perform any custom [transformations](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) on your data or use Nexla's prebuilt connectors, click the __Transform__ button on the dataset to enter the Transform Builder.

### Step 4: Send to destination

Similar to adding a source, click the __Send to Destination__ arrow on the dataset, and select any of Nexla's destination connectors or Braze if you had a different source. Input your credentials, configure the destination options, and click __Save__. Data will instantly begin flowing in the format you specified to the destination of your choice.

## Using this integration

Once the flow is set up, nothing more is required. Nexla will handle any changes in the source data and scale to any amount of new data and notify you of any schema changes or errors for triage. If you'd like to make changes to transformations, the source, or the destination, you can click and make the change, and Nexla will update the flow instantly.

## Use cases

Nexla's data-as-a-product, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), make it easy to work with data of any format without worrying about metadata. When you set up your data flows to or from Braze with Nexla, no-code tools make it easy and available in minutes. Once the data flow is set to a destination, Nexla will monitor your flow and scale to any amount of data. Our platform makes it simple for anyone to create scalable data flows. Teams working with data get a no/low-code unified experience to integrate, transform, provision, and monitor data for any use case. 

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo
