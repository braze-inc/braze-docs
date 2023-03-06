---
nav_title: ActionIQ
article_title: ActionIQ
description: "This reference article covers the Braze and ActionIQ integration. ActionIQ is a enterprise Customer Data platform for marketers, analysts, and technologists. This integration allows brands to sync and map their ActionIQ data directly to Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ

---

# ActionIQ

> [ActionIQ][2] brings order to customer experience chaos. The ActionIQ Customer Experience (CX) Hub gives all teams direct but controlled self-service access to customer data to discover audiences and orchestrate experiences at scale.

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

## Integration

### Connect ActionIQ to Braze

In ActionIQ, set up a Braze connection by providing your REST API key and Braze REST endpoint. 

To match to consumers in the Braze platform, the following identifiers must be included in your activation setting:
- `braze_id`
- `external_id`

Once your integration has been connected, information will start sending to Braze.

#### Event integration

The ActionIQ platform can also be configured to receive event information via its streaming ingest service. This integration option forwards these events to Braze for marketers to use to orchestrate or trigger marketing campaigns. The event integration can send additional ActionIQ attributes as part of the properties within the event payload.

The events integration sends the following information to Braze:
- Event name
- Consumer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event properties, which are populated by any additional attributes in the export setting

## Using this integration

Once your segments have successfully exported to Braze, you can find them as custom attributes on user profiles with the following naming convention:`AIQ_<Audience ID>_<Split ID>`.

Optionally, custom attributes used for message personalization can also be sent. Additional attributes included in the export will appear in Braze with the same name as the ActionIQ Attribute header.

To create a segment of these users, In Braze, navigate to **Segments**, create a new segment, and select **Custom Attributes** as your filter. From here, you can choose the ActionIQ custom attribute. Once created, you can select your segment as an audience filter when creating a campaign or Canvas.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/