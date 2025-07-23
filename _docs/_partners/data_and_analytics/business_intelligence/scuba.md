---
nav_title: Scuba
article_title: Scuba Analytics
description: "This Scuba and Braze technical reference describes how to activate Scuba's real-time data insight using Braze Segments."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) is a full-stack, machine-learning-powered data collaboration platform designed for high-velocity time-series data. Scuba allows you to selectively export users (also called actors) and load them into your Braze platform. In Scuba, custom actor properties are used to analyze behavioral trends, activate your data across various platforms, and conduct predictive modeling using machine learning.

_This integration is maintained by Scuba Analytics._

## Prerequisites

To use Scuba Analytics with Braze, you'll need the following:

| Requirement | Description |
|---|---|
|Scuba API Token | A Scuba API token you can retrieve from the `https://{scuba_hostname}/api/create_token` endpoint. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Uploading your Scuba data to Braze

{% alert important %}
The following request uses curl. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

To upload your Scuba data to Braze, make a POST request to `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` using the `application/json` content-type:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Replace the following:

| Placeholder             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | The Braze REST endpoint URL of your current Braze instance. For more information, see [Rest API keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Your Braze REST API key with the `users.track` permission.                                                                                                                                      |
| `HOSTNAME`              | The hostname of your current Scuba instance.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Your Scuba API token.                                                                                                                                                                           |
| `TABLE_NAME`            | The table your dataset belongs to. For more information, see [Glossary: Dataset table](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | The actor property your dataset belongs to. Only data matching this name will be returned. For more information, see [Glossary: Actor property](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | The audience search filter for your actor property.                                                                                                                                             |
| `ACTOR_ID`              | The ID of the actor property your dataset belongs to. This ID matches your `external_id` in Braze. For more information, see [Glossary: Actor](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | The start period as a BQL-compatible date. For more information, see [BQL syntax and usage](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | The end period as a BQL-compatible date. For more information, see [BQL syntax and usage](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Optional**: The maximum number of records to return. If `scuba_record_limit` is omitted, Scuba will return a maximum of 100 records. To change this, assignin any non-negative number to `scuba_record_limit`.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Default behavior

By default, `update_existing_only` is set to `false` which will update your existing records in Braze, as well as create new records for those that don't exist. To prevent Scuba from creating new records, set `update_existing_only` to `true`.

### Rate limit

Scuba applies a rate limit of 50,000 requests per minute to this endpoint.

## Creating segments using Scuba's behavioral data

After you [upload your data](#uploading-your-scuba-data-to-braze), you can create user segments in Braze using Scuba's behavioral data.

### Step 1: Create a new segment

In Braze, go to **Audience** > **Segments**, then select **Create Segment** and enter a name for your segment.

![Creating a new segment in Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Step 2: Find and select the Scuba attribute

Under **Segment Details** > **Filters**, select **Custom Attributes**.

![Selecting the 'Custom Attribute' filter under 'Segment Details'.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Select **Search custom attributes**, then choose the actor property name you used in your previous POST request.

![Selecting the actor property as a custom attribute.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Step 3: Configure the attribute

Next to your actor property name, choose an operator and a value (if applicable). These values are determined by the actor properties you've defined in Scuba. When you're finished, select **Save**.

![Choosing an operating and value for the selected ]({% image_buster /assets/img/scuba/analytics/operator_end.png %})


