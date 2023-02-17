---
nav_title: ActionIQ
article_title: ActionIQ
description: "The Braze and ActionIQ integration allows brands to map the audience segments (or custom attributes) across both platforms or forward real-time events from ActionIQ to Braze to deliver personalized customer experiences based on the entire breadth of their customer data."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ

---

# ActionIQ

> [ActionIQ][2] brings order to CX chaos. The ActionIQ Customer Experience (CX) Hub gives all teams direct but controlled self-service access to customer data to discover audiences and orchestrate experiences at scale.

The ActionIQ integration to Braze allows customers to sync AIQ segments with Braze or forward qualified real-time events from AIQ to Braze.

The Braze and ActionIQ integration allows brands to sync and map their ActionIQ data directly to Braze, empowering the delivery of extraordinary customer experiences based on the entire breadth of their customer data. The integration enables the users to:
- Map audience segments or custom attributes to Braze directly from ActionIQ
- Forward the events tracked by ActionIQ to Braze in real time to trigger personalized and targeted campaigns

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| ActionIQ account | An ActionIQ account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with `users.track` and `user.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

### Audience Membership
This integration is used to sync ActionIQ Audience membership to Braze by creating custom attributes that denote whether a Braze profile is part of a segment or not. Each ActionIQ audience corresponds to a unique boolean Braze Custom Attribute. The standard naming convention for the custom attribute created is: `AIQ_<Audience ID>_<Split ID>`.

Within the Braze platform, marketers can use these attributes for segmentation by identifying whether a given consumer is part of an Audience in AIQ. Optionally, custom attributes used for message personalization can also be sent. Additional attributes included in the export will show up in Braze with the same name as the AIQ Attribute header.

#### Requirements
To match to consumers in the Braze platform, the following identifiers must be included in your activation setting, depending on how your Braze instance is set up:
- `braze_id`
- `external_id`

### Events
The ActionIQ platform can be configured to receive Event information via its streaming ingest service. This other integration option forwards these Events to Braze for marketers to use to orchestrate or trigger marketing campaigns.

#### Usage
ActionIQ gathers event data through a streaming data collection, evaluates it through the platform’s triggers module, and, if relevant, forwards it to Braze.

The Event integration can send additional ActionIQ Attributes as part of the properties within the Event payload.

#### Requirements
The events integration sends the following information to Braze:
- Event name
- Consumer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event properties, which are populated by any additional attributes in the export setting

### Using this integration

Once your segments have successfully exported to Braze, you can find them as custom attributes on user profiles with the same name as the segment found in ActionIQ. 

To create a segment of these users, In Braze, navigate to **Segments**, create a new segment, and select **Custom Attributes** as your filter. From here, you can choose the ActionIQ custom attribute. Once created, you can select your segment as an audience filter when creating a campaign or Canvas.

{% alert note %}
For more information on this integration, visit Microsoft's Braze [integration article](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze).
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/