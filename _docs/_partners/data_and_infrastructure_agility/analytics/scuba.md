---
nav_title: Scuba
article_title: Scuba Analytics
description: "This Scuba and Braze technical reference describes how to activate Scuba's real-time data insight using Braze Segments."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Scuba Analytics

>[Scuba Analytics][1] is a full-stack, machine-learning-powered data collaboration platform designed for high-velocity time-series data. It redefines how organizations handle first-party and high-velocity time-series data, offering insights into customers and real-time competition tracking.

The Scuba platform ingests and queries vast amounts of event data from various customer touch points in real-time. It provides real-time cross-channel measurement, hyper-personalization, privacy-focused no-code data science, and self-service analytics, ensuring speed, precision, and scalability. SCUBA prioritizes data purity and privacy, ensuring GDPR compliance. The platform's features include SCUBACONNECT for schemaless edge ingestion, enabling seamless data source connection, real-time analysis, and activation for agile data management and product development.

## Prerequisites

| Requirement                       | Description                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Partner Account                   | A partner account is required to take advantage of this partnership.                                                                                                                             |
| Braze REST API key                | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from [**Settings** > **API Keys**](https://your-braze-dashboard-url/settings/api-keys). |
| Braze REST endpoint               | [Your REST endpoint URL](https://your-braze-instance-url/). Your endpoint will depend on the Braze URL for your instance.                                                                        |
| Scuba Hostname                    | Hostname of your Scuba instance                                                                                                                                                                  |
| Scuba API Token                   | Your Scuba API token. Retrieve this token from the https://{scuba_hostname}/api/create_token endpoint.                                                                                           |
| Scuba Table Name                  | Name of the [Table][3] in Scuba containing your dataset.                                                                                                                                         |
| Scuba Actor Property Name         | Name of the [Actor Property][4] in Scuba within the dataset to target for activation. Returned data is limited to only actors containing this specified property name.                           |
| Scuba Actor Property Value Filter | The value which the Scuba Actor Property Name must be assigned to, in order to meet the audience search criteria.                                                                                |
| Scuba Actor ID                    | Actor ID: the Scuba [Actor][5]'s identity attribute, used as the external_id in Braze.                                                                                                           |
| Scuba Period Start                | Start of period in [BQL][6] compatible date.                                                                                                                                                     |
| Scuba Period End                  | End of period in [BQL][6] compatible date.                                                                                                                                                       |
| Scuba Record Limit                | **Optional**: Max returned records from Scuba API. Defaults to 100.                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Scuba allows you to selectively export users (also referred to as actors) based on specific property values, then load these users into Braze. In Scuba, custom actor properties are used to analyze behavioral trends, activate your data across various platforms, and conduct predictive modeling using Machine Learning.

## Integrating Scuba

This integration is invoked via a single REST API call to Scuba, wherein you provide your credentials and details of your target segments/behaviors in Scuba.

### Step 1: Get your credentials

To use this integration, you can make a single webhook request to Scuba. In this HTTP request, you will provide your credentials along with the details of your target segments and behaviors in Scuba. Ensure you have gathered all the requirements mentioned above before we format the example request.

### Step 2: Make a POST request

To load your data, make an **HTTP POST** request to the connector url **https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation** and include the required inputs in the request's JSON body. Include a header indicating content-type: application/json.

```
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"<<insert Braze REST endpoint here>>", \
"braze_api_key":"<<insert Braze REST API key here>>", \
"scuba_host":"<<insert Scuba Hostname here>>", \
"scuba_token":"<<insert Scuba API Token here>>", \
"scuba_table_name":"<<insert Scuba Table Name here>>", \
"scuba_actor_property_name":"<<insert Scuba Actor Property Name here>>", \
"scuba_actor_property_value_filter":"<<insert Scuba Actor Property Value Filter here>>" \
"scuba_actor_id":"<<insert Scuba Actor ID here>>", \
"scuba_period_start":"<<insert Scuba Period Start here>>", \
"scuba_period_end":"<<insert Scuba Period End here>>", \
"scuba_record_limit":"<<OPTIONAL: insert Scuba Record Limit here>>"}'
```

{% alert important %}
The example above loads data from Scuba to Braze using a CURL command. However, for enhanced usability and better management of API requests, its recommended to utilize an API client, such as Postman.
{% endalert %}

#### Default behavior

By default, Scuba configures `update_existing_only` to `false`. By setting `update_existing_only` to `false`, Scuba will create new records in Braze if they don't already exist, in addition to updating your existing records.

#### Rate limits

To comply with Braze API rate limits, this endpoint restricts the number of entities processed to a maximum of 50,000 per minute.

## Creating a segment from Scuba's behavioral data

Utilizing the behavioral actor properties of users we've imported to Braze, we can create segments of these users in Braze.


### Step 1: Create a new segment

In Braze, go to **Audience** > **Segments**, then select **Create Segment** and enter a name for your new segment.

![Create Segment][501]

### Step 2: Find and select the Scuba attribute

Now within the Segment Details section, navigate to the Filters section, and click "Select Filter". Choose "Custom Attributes" from the dropdown menu.

![Select Custom Attribute Filter][502]

Click "Search custom attributes" in the newly created filter. Here, you will see your actor property name from Scuba as one of the custom attributes. Select this attribute.

![Select Actor Property][503]

### Step 3: Configure the attribute

Right of the selected actor property name, choose the preferred evaluation operator (equals, by default) and value (if applicable). Your choices will vary depending on how your actor properties are defined in Scuba. In this example, we're simply checking if the value is equal to **true**. A more trivial example could use "is not blank" without a target value. When you're finished, select **Save**.

![Evaluation Operator(s)][504]

[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
