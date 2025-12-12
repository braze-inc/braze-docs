---
nav_title: Zeotap for Currents
article_title: Zeotap for Currents
description: "This reference article outlines the partnership between Braze Currents and Zeotap, a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap for Currents

> [Zeotap](https://zeotap.com/) is a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment.

The Braze and Zeotap integration empowers you to extend the scale and reach of your campaigns by syncing Zeotap customer segments to Braze user profiles. With [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), you can also connect data to Zeotap to make it actionable across the entire growth stack.

{% alert important %}
The custom HTTP connector is currently in beta. If you're interested in setting up this integration, reach out to your customer success manager.
{% endalert %}

## Prerequisites

| Requirement | Description |
| --- | --- |
|Zeotap account | A [Zeotap account](https://zeotap.com/) is required to take advantage of this partnership. |
| Currents | To export data back into Zeotap, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Implementation

### Step 1: Create a Currents source

1. In Zeotap, go to **Sources** under **Integrate**.
2. Select **Create Source**.
3. Select **Customer Engagement Channels** as the category.<br><br>![A "Create Source" window listing different categories, including "Customer Engagement Channels".]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Select **Braze** as the data source.
5. Enter a source name.
6. Select your region.<br><br>![Window with options for selecting your region and data entity.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Select **Create Source**.
8. Go to the **Implementation Details** tab and take note of the **API URL** and **Write Key**.<br><br>![Implementation details for Braze Currents that contains the API URL and Write Key.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Step 2: Configure data streaming in Currents

1. In Braze, go to **Partner Integrations** > **Data Export**.
2. Select **Create New Current** and **Custom Currents Export**.<br><br>![The "Create New Current" button with a dropdown that contains "Custom Currents Export".]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Enter an integration name and email to be contacted if errors occur with the integration.
4. Under **Credentials**, enter the following information you noted from [Step 1](#step-1-create-a-currents-source):
- The API URL as the **Endpoint**
- The Write Key as the **Bearer Token**<br><br>![Sections to input integration details and credentials.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Select the message engagement events that you want to send to Zeotap.<br><br>![The "General Settings" tab with a section to select message engagement events.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Select **Launch Current** to save the changes and start sending events to Zeotap.

{% alert important %}
The Currents connector doesn't support anonymous users (users without an `external_id`).
{% endalert %}

