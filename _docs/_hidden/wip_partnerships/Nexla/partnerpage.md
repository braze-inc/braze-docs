---
nav_title: Nexla
page_order: 1

description: "Braze Currents and Nexla Make Data Accessible Across Your Entire Ecosystem to the Data Warehouse of Your Choice."
alias: /partners/nexla/

page_type: partner
hidden: true
---

# Nexla

> Nexla is the leader in unified data operations and a 2021 Gartner Cool Vendor. Our platform makes it simple for anyone to create scalable data flows. Teams working with data get a no/low-code unified experience to integrate, transform, provision, and monitor data for any use case. Nexla lowers the technical expertise needed to understand and use data. It delivers zero-friction, governed data operations, better collaboration, and agility for business and data teams. To learn more, visit https://www.nexla.com.

Utilize Currents to send data to your data warehouse of choice. Leverage Nexla to extract, transform, and load that data to other locations, making data easily accessible across your entire ecosystem. Nexla enables you to use Braze Currents to get data in a custom format delivered to your destination of choice by a simple point and click.

## Requirements or Prerequisites

The only requirements to integrate to Braze are a Nexla account and your data in Braze.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | Save this API key to input into Nexla as part of your Braze credentials. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Save your REST Endpoint to input into Nexla as part of your Braze credentials. |
| Nexla Account | Nexla | [Start your Free Trial] [2] | Access to the Nexla platform and a Nexla account are required to use Braze connectors.

## Integration

Integrating with Braze is simple on Nexla. Once you've created an account and logged onto the platform, Braze connectors come ready for production out of the box. Simply select, add your Braze credentials, and immediately begin integrating, preparing, and monitoring your data in any format.

### Step 1: Create a Nexla Account

If needed, head to our website www.nexla.com to request a free demo and trial so we can get you set up with a Nexla account. Log on to www.dataops.nexla.io and sign on with your new credentials.

### Step 2: Add Your Source

If Braze is your data source, navigate to Flows > Create a New Flow on the left toolbar. Click Create New Source, and select the Braze connector. Click Next, then Add a New Credential. Name the credential, and add your Braze API key and REST endpoint. Click Save, Next, select your data and click Save. Nexla will now search the source for any data it finds and generate a "Nexset" for transformation or sending to destination.

If Braze is your destination, see connecting sources to Nexla: https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source.

For more information on Nexsets, see: https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information

### Step 3: Transform (Optional)

If you want to perform any custom transformations on your data or use Nexla's prebuilt connectors, click the Transform button on the dataset to enter the Transform Builder. For more information: https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations

### Step 4: Send to Destination

Similar to adding a source, click the Send to Destination arrow on the dataset, and select any of Nexla's destination connectors or Braze if you had a different source. Input your credentials, configure the destination options, and click Save. Data will instantly begin flowing in the format you specified to the destination of your choice.

## Using This Integration

Once the flow is set up, nothing more is required. Nexla will handle any changes in the source data and scale to any amount of new data, and notify you of any schema changes or errors for triage. If you'd like to make changes to transformations, the source, or destination, you can simply click and make the change and Nexla will update the flow instantly.


## Use Cases

Nexla's data-as-a-product, Nexsets, make it easy to work with data of any format without worrying about metadata. When you set up your data flows to or from Braze with Nexla, no-code tools make it easy and available in minutes. Once the data flow is easily set up to any destination, Nexla will monitor your flow and scale to any amount of data. Our platform makes it simple for anyone to create scalable data flows. Teams working with data get a no/low-code unified experience to integrate, transform, provision, and monitor data for any use case. 

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: www.nexla.com/get-demo
