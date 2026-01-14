---
nav_title: Nexla
article_title: Nexla
description: "This reference article outlines the partnership between Braze and Nexla, a unified data operations platform that allows Braze Currents users to extract, transform, and load data lake data to other locations in a custom format."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) is a leader in unified data operations and a 2021 Gartner Cool Vendor. The Nexla platform provides tools for creating scalable data flows, delivering governed data operations, collaboration, and agility for business and data teams. Teams working with data get a no/low-code unified experience to integrate, transform, provision, and monitor data for any use case. 

The Braze and Nexla integration allows customers that use [Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) to leverage Nexla to extract, transform, and load data lake data to other locations in a custom format, making data easily accessible across your entire ecosystem.

## Prerequisites

| Requirement | Description |
|---|---|
| Nexla account | A [Nexla account](https://www.nexla.com/get-demo) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Nexla's data-as-a-product, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), enables working with data of any format without managing metadata. When you set up data flows to or from Braze with Nexla, no-code tools are available within minutes. After the data flow is set to a destination, Nexla monitors the flow and scales to any amount of data.

## Integration

### Step 1: Create a Nexla account

If you do not already have a Nexla account, head to the Nexla [website](https://www.nexla.com) to request a free demo and trial. Next, log on to [www.dataops.nexla.io](https://www.dataops.nexla.io) and sign on with your new credentials.

### Step 2: Add your source

#### If Braze is your data source
1. In the Nexla platform, navigate to **Flows > Create a New Flow** on the left toolbar.
2. Click **Create New Source**, select the Braze connector, and click **Next**. 
3. Select **Add a New Credential**, name the credential, add your Braze API key and REST endpoint, and **Save**.
4. Lastly, select your data and click **Save**. 

Nexla will search the source for available data and generate a [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) for transformation or sending to a destination.

#### If Braze is your destination

Visit Nexla documentation on [connecting sources to Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Step 3: Transform (optional)

If you want to perform any custom [transformations](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) on your data or use Nexla's prebuilt connectors, click the **Transform** button on the dataset to enter the Transform Builder. Guidance on using the Transform Builder can be found in [Nexla's documentation](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Step 4: Send to destination

To send data to a destination, click the **Send to Destination** arrow on the dataset, and select any of Nexla's destination connectors or Braze if you had a different source. Input your credentials, configure the destination options, and click **Save**. Data will instantly begin flowing in the format you specified to the destination of your choice.

## Using this integration

Once the flow is set up, nothing more is required. Nexla will handle any changes in the source data, scale to any new data, and notify you of any schema changes or errors for triage. If you'd like to make changes to transformations, the source, or the destination, you can click into these options and make the change, and Nexla will update the flow instantly.

