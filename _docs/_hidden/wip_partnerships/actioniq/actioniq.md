---
nav_title: ActionIQ
article_title: ActionIQ
page_order: 1

description: "The Braze and ActionIQ integration allows brands to map the audience segments (or custom attributes) across both platforms or forwarding real-time events from ActionIQ to Braze to enable the delivery of personalized customer experiences based on the entire breath of their customer data."
alias: /partners/actioniq/

page_type: partner
search_tag: ActionIQ
hidden: true

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

## Use cases

### Audience Membership
This integration is used to sync ActionIQ Audience membership to Braze by creating Custom Attributes that denote whether a Braze profile is part of a segment or not. Each ActionIQ Audience corresponds to a unique boolean Braze Custom Attribute. The standard naming convention for the Custom Attribute created is: `AIQ_<Audience ID>_<Split ID>`.

Within the Braze platform, marketers can use these attributes for segmentation purposes, by identifying whether a given consumer is part of an Audience in AIQ. Optionally, Custom Attributes used for message personalization can also be sent. Additional Attributes included in the export will show up in Braze with the same name as the AIQ Attribute header

#### Requirements
In order to match to consumers in the Braze platform, the following identifiers must be included in your Activation Setting, depending on how your Braze instance is set up:
- `braze_id`
- `external_id`

### Events
The ActionIQ platform can be configured to receive Event information via its streaming ingest service. This other integration option forwards these Events to Braze, for marketers to use for orchestration or the triggering of marketing campaigns.

#### Usage
ActionIQ gathers Event data through a Streaming Data Collection, evaluates it through the platform’s Triggers module and, if relevant, forwards it to Braze.

The Event integration is able to send additional ActionIQ Attributes as part of the properties within the Event payload.

#### Requirements
The Events integration sends the following information to Braze:
- Event name
- Consumer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event Properties, which are populated by any additional Attributes in the export setting

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/
