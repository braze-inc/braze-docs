---
nav_title: Adobe for currents
article_title: Adobe for Currents
alias: /partners/adobe_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Adobe, a customer data platform that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe for Currents

> [Adobe](https://www.adobe.com/) is a customer data platform that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real time.

The Braze and Adobe integration allows you to seamlessly control the flow of information between the two systems. With [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), you can also connect data to Adobe to make it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Currents | To export data back into Adobe, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Adobe Experience Platform account | An [Adobe Experience Platform account](https://experience.adobe.com/#/platform/home) is required to take advantage of this partnership. |
| Permission to create a connector | You need permissions to create a streaming source connection to use this integration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create an XDM schema in Adobe

1. In Adobe Experience Platform, go to **Schemas** > select **Create schema** > select **Experience Event** > select **Next**.<br><br>![Adobe Schemas page for the schema called "Braze Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Provide a name and description for your schema. 
3. In the **Composition** panel, configure your schema attributes:
- In **Field groups**, select **Add** and then add the **Braze Currents User Event** field group.
- Select **Save**.

For more information on schemas, refer to Adobe's documentation on [creating schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Step 2: Connect Braze to the Adobe Experience Platform

1. In Adobe Experience Platform, go to **Sources** > **Catalog** > **Marketing automation**.
2. Select **Add data** for Braze Currents.
3. Upload the [Braze Currents sample file](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Adobe "Add data page".]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. After your file is uploaded, provide your dataflow details, including information about your dataset and the schema that you are mapping to. 
    - If this is your first time connecting a Braze Currents source, create a new dataset and make sure to use the schema you created in [Step 1](#step-1-create-an-xdm-schema-in-adobe). 
    - If this isn't your first time, use any existing dataset that references the Braze schema.
5. Configure mapping for your data and resolve the issues.
    - Change the mapping for `id` from `to _braze.appID` to `_id` at the root level of the schema.
    - Make sure `properties.is_amp` is mapped to `_braze.messaging.email.isAMP`.
    - Delete the `time` and `timestamp` mapping, then select the add icon > **Add calculated field** and enter **time * 1000**. Select **Save**.
    - Select **Map target field** next to the new source field and map it to **timestamp** at the root level of the schema. <br><br>![Adobe "Add data" page with mappings.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Select **Validate** to confirm you resolved the issues.

{% alert important %}
Braze timestamps are expressed in seconds. To accurately reflect timestamps in Adobe Experience Platform, your calculated fields need to be in milliseconds. To convert seconds to milliseconds, use the calculation **time * 1000**.
{% endalert %}

{: start="7"}
7. Select **Next**, review your dataflow details, and then select **Finish**.<br><br>![Adobe "Add data" page with no mapping errors.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Step 3: Gather credentials

Collect the following creditials to input into Braze, which will allow Braze to send data to Adobe Experience Platform.

| Field         |Description                          |
|---------------|-------------------------------------|
| Client ID     | The client ID associated with your Adobe Experience Platform source. |
| Client Secret | The client secret associated with your Adobe Experience Platform source. |
| Tenant ID     | The tenant ID associated with your Adobe Experience Platform source. |
| Sandbox Name  | The sandbox associated with your Adobe Experience Platform source.   |
| Dataflow ID   | The dataflow ID associated with your Adobe Experience Platform source.   |
| Streaming Endpoint  | The streaming endpoint associated with your Adobe Experience Platform source. Braze automatically converts this to the batch streaming endpoint. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 4: Configure Currents to stream data to your data source

1. In Braze, go to **Partner Integrations** > **Data Export**, and then select **Create New Current**. 
2. Provide the following:
    - A name for the connector
    - Contact information for notifications about the connector
    - The credentials from [Step 3](#step-3-gather-credentials)
3. Select the events you want to receive.
4. Optionally configure any desired field exclusions or transformations.
5. Select **Launch Current**.

