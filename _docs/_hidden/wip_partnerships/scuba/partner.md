---
nav_title: Scuba Analytics
article_title: Scuba Analytics
page_order: 1
description: "This Scuba and Braze technical reference describes how to activate Scuba's real-time data insight using Braze Segments."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Scuba Analytics

>[Scuba Analytics][1] is a full-stack ML-powered data collaboration platform designed for high-velocity time-series data. It redefines how organizations handle first-party and high-velocity time-series data, offering insights into customers and real-time competition tracking. The platform ingests and queries vast amounts of event data from various customer touch points in real-time. It provides real-time cross-channel measurement, hyper-personalization, privacy-focused no-code data science, and self-service analytics, ensuring speed, precision, and scalability. SCUBA prioritizes data purity and privacy, ensuring GDPR compliance. The platform's features include SCUBACONNECT for schemaless edge ingestion, enabling seamless data source connection, real-time analysis, and activation for agile data management and product development.

## Prerequisites

| Requirement                | Description                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------- |
| Partner Account                   | A partner account is required to take advantage of this partnership.                          |
| Braze REST API key                | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from [**Settings** > **API Keys**](https://your-braze-dashboard-url/settings/api-keys). |
| Braze REST endpoint               | [Your REST endpoint URL](https://your-braze-instance-url/). Your endpoint will depend on the Braze URL for your instance.    |
| Scuba Hostname                    | Hostname of your Scuba instance                                                               |
| Scuba API Token                   | Your Scuba API token. Retrieve this token from the https://{scuba_hostname}/api/create_token endpoint.     |
| Scuba Table Name                  | Name of the [Table][3] in Scuba containing your dataset.                                           |
| Scuba Actor Property Name         | Name of the [Actor Property][4] in Scuba within the dataset to target for activation. Returned data is limited to only actors containing this specified property name. |
| Scuba Actor Property Value Filter | The value which the Scuba Actor Property Name must be assigned to, in order to meet the audience search criteria. |
| Scuba Actor ID                    | Actor ID: the Scuba [Actor][5]'s identity attribute, used as the external_id in Braze.                            |
| Scuba Period Start                | Start of period in [BQL][6] compatible date.                                                       |
| Scuba Period End                  | End of period in [BQL][6] compatible date.                                                         |
| Scuba Record Limit                | **Optional**: Max returned records from Scuba API. Defaults to 100.                           |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

This integration allows you to selectively export users (referred to as actors in Scuba) based on specific property values and then load these users into your Braze instance. In Scuba, custom actor properties are used to analyze behavioral trends, activate your data across various platforms, and conduct predictive modeling using Machine Learning.

## Integration

This integration is invoked via a single REST API call to Scuba, wherein you provide your credentials and details of your target segments/behaviors in Scuba. and 

### Step 1: Gather Details

To use this integration, you can make a single webhook request to Scuba. In this HTTP request, you will provide your credentials along with the details of your target segments and behaviors in Scuba. Ensure you have gathered all the requirements mentioned above before we format the example request.

### Step 2: Create an invoke the HTTP Request to load your data

To perform the data load, make an **HTTP POST** request to the connector url **https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation** and include the required inputs in the request's JSON body. Include a header indicating content-type: application/json.

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

## Creating a segment from Scuba's behavioral data 

Utilizing the behavioral actor properties of users we've imported to Braze, we can create segments of these users in Braze.

1. Navigate to Audience > Segments. Click "Create Segment" and provide a segment name.
   ![Create Segment][501]

2. Now within the Segment Details section, navigate to the Filters section, and click "Select Filter". Choose "Custom Attributes" from the dropdown menu.
   ![Select Custom Attribute Filter][502]

3. Click "Search custom attributes" in the newly created filter. Here, you will see your actor property name from Scuba as one of the custom attributes. Select this attribute.
   ![Select Actor Property][503]

4. Right of the selected actor property name, choose the preferred evaluation operator (equals, by default) and value (if applicable). Your choices will vary depending on how your actor properties are defined in Scuba. In this example, we're simply checking if the value is equal to **true**. A more trivial example could use "is not blank" without a target value.
   ![Evaluation Operator(s)][504]

5. Click "Save" at the bottom of the Segment Details section to save the new segment.

[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/1_segment_name.png %}
[502]: {% image_buster /assets/img/scuba/2_filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/3_select_property.png %}
[504]: {% image_buster /assets/img/scuba/4_operator_end.png %}