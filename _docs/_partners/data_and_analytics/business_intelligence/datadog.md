---
nav_title: Datadog
article_title: "Datadog"
description: "This reference article outlines the partnership with Braze and Datadog, an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services through a SaaS-based data analytics platform."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) is an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services through a SaaS-based data analytics platform.

The Braze and Datadog integration allows customers to collect Braze data in Datadog and create alerts on the data we send. For example, setting up a monitor and alert if your weekly newsletter campaign sends an abnormally low volume of messages or if a Canvas step that usually only sends a few messages a day starts sending thousands. 

## Prerequisites 

| Requirement | Description |
|---|---|
| Datadog account | A Datadog account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Generate Datadog key

In Datadog, you will need to create an [API key](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). To add an API key, navigate to **Organization Settings** > **API Keys** > **New Key**.

### Step 2: Add key to Braze

In the Braze dashboard, navigate to **Partner Integrations** > **Technology Partners** and then search **Datadog**. On the Datadog partner page, provide the Datadog API key. This will create a connection to allow Braze to send data to Datadog.

## Braze events

After the connection is integrated, Braze will send the following events to Datadog:

- `braze.messaging.sent` - The count of sends

Each of these events will have metadata in the form of Datadog tags to give you information such as:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (if available)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (if available)

These events and tags can be monitored on the Datadog **Metrics Explorer** page. These metrics are logged as [distributions](https://docs.datadoghq.com/metrics/distributions/) to DataDog. Given the nature of metrics and the imprecision of DataDog's aggregations and rollups, Braze does not retry intermittent network errors or other DataDog API errors that may be encountered during transmission. This means that these metric counts may differ slightly from counts seen in the Braze dashboard and/or through Currents.

![]({% image_buster /assets/img/datadog.png %})

