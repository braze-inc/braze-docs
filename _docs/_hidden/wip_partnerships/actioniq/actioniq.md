---
nav_title: ActionIQ
article_title: ActionIQ
page_order: 1

description: "This is the Google Search and SEO description that will appear; try to make this informative and concise, yet brief."
alias: /partners/actioniq/

page_type: partner
search_tag: Partner
hidden: true

---

# ActionIQ

The ActionIQ integration to Braze allows customers to either sync segments across the two platforms or forward real-time events. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Partner account | An ActionIQ account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with `users.track` and `user.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |

## Use cases

### Audience Membership
This integration is used to sync ActionIQ Audience membership to Braze by creating Custom Attributes that denote whether a Braze profile is part of a segment or not. Each ActionIQ Audience corresponds to a unique boolean Braze Custom Attribute. The standard naming convention for the Braze Custom Attribute created is: `AIQ_<Audience ID>_<Split ID>`.

Within the Braze platform, users can use these attributes for segmentation purposes, by identifying whether a given customer is part of an Audience in AIQ. Optionally, Custom Attributes used for message personalization can also be sent.

Additional Custom Attributes included in the export will show up in Braze with the same name as the AIQ Attribute header. Attributes are set at the Braze profile level, not at the Braze segment level given Braze's limitations around updating Segments. This means there's a risk that two Segments that include the same profile overwrite the same profile attribute.

#### Requirements
In order to match to customers in the Braze platform, the following identifiers must be included in your Activation Setting, depending on how your Braze instance is set up:
- `braze_id`
- `external_id`

### Events
The ActionIQ platform can be configured to receive Event information via its streaming ingest service. This other integration option forwards these Events to Braze, for clients to use for orchestration or the triggering of marketing campaigns.

#### Usage
ActionIQ gathers Event data through a Streaming Data Collection, evaluates it through the platform’s Triggers module and, if relevant, passes it to Braze via its APIs.

The Event integration allows the client to send additional ActionIQ Attributes as part of the properties within the Event payload.

#### Requirements
The Events integration sends the following information to Braze:
- Event name
- Customer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event Properties, which are populated by any additional Attributes in the export setting

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
