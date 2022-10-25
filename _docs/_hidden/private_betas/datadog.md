---
nav_title: DataDog
article_title: "DataDog"
description: "This article outlines the partnership with Braze and DataDog, an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services, through a SaaS-based data analytics platform."
page_type: partner
search_tag: Partner
hidden: true
permalink: /partners/datadog/

---

# DataDog

> [DataDog](https://www.datadoghq.com/) is an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services, through a SaaS-based data analytics platform.

The Braze and DataDog integration allows customers to collect Braze data in DataDog and create alerts on the data we send. For example, setting up a monitor and slert if your weekly newsletter campaign sends an abnormally low volume of messages, or a Canvas step that usually only senda a few messages a day starts sending thousands. 

{% alert important %}
The DataDog partner integration is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites 

| Requirement | Description |
|---|---|
| DataDog account | A DataDog account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Generate DataDog key

In DataDog, you will need to create an application key. To add an application key, navigate to **Organization Settings** > **Application Keys** > **New Key**.

### Step 2: Add key to Braze

In the Braze dashboard, navigate to the **Technology Partners** section and then search **DataDog**. On the DataDog partner page, provide the DataDog application key. 

## Braze events

After the connection is integrated, Braze will send the following events to DataDog:

- `braze.messaging.sent` - The count of sends
- `braze.messaging.abort_message` - The count of aborted messages

Each of these events will have metadata in the form of DataDog tags to give you information such as:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (if available)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (if available)

These events and tags can be monitored on the DataDog **Metrics Explorer** page.

![][1]

[1]: {% image_buster /assets/img/datadog.png %}



