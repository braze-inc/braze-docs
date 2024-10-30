---
nav_title: Adobe for Currents
article_title: Adobe for Currents
alias: /partners/adobe_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Adobe, a customer data platform that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe for Currents

> Adobe is a customer data platform that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time.

The Braze and Adobe integration allows you to seamlessly control the flow of information between the two systems. With [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), you can also connect data to Adobe to make it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Currents | In order to export data back into Adobe, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Adobe Experience Platform account | An [Adobe Experience Platform account](https://experience.adobe.com/#/platform/home) is required to take advantage of this partnership. |
| Permission to create a connector | You need permissions to create a streaming source connection to use this integration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create an XDM schema in Adobe

1. In Adobe Experience Platform, go to **Schemas** > select **Create schema** > select **Experience Event** > select **Next**.
2. Provide a name and description for your schema. 
3. In the **Composition** panel, configure your schema attributes:
- In **Field groups**, select **Add** and then add the **Braze Currents User Event** field group.
- Select **Save**.

For more information on schemas, refer to Adobe's documentation on [creating schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Step 2: Connect Braze to the Adobe Experience Platform





