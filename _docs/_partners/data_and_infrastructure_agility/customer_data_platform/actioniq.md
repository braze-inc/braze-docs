---
nav_title: ActionIQ
article_title: ActionIQ
description: "This reference article covers the Braze and ActionIQ integration. ActionIQ is a enterprise Customer Data platform for marketers, analysts, and technologists. This integration allows brands to sync and map their ActionIQ data directly to Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2] is a new kind of customer data platform for enterprise brands, giving marketers easy and secure ways to activate data anywhere in the customer experience. ActionIQ’s unique composable architecture means data can stay securely where it lives, and marketing teams only use the tools they need.
> 
> Over the last several years, ActionIQ has helped dozens of G2K companies across financial services, media, retail, B2B-Tech, and Travel & Hospitality in addressing challenges related to customer acquisition and retention.
>
> [Get in touch][3] with our experts to learn more.

The Braze and ActionIQ integrations allow brands to sync and map their ActionIQ data directly to Braze, empowering the delivery of extraordinary customer experiences based on the entire breadth of their customer data. The integrations available enable users to:
- Update User Profiles in Braze with Audience Membership information and any attributes directly from ActionIQ
- Forward the events tracked by ActionIQ to Braze in real time to trigger personalized and targeted campaigns
- Deliver API-Triggered Campaigns in Braze directly from touchpoints in an ActionIQ Journey

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| ActionIQ account | An ActionIQ account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with the desired integration's required permissions (see Requirements section of each integration). <br><br> This key can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrations

### Audience Membership

This integration is used to sync ActionIQ audience membership to Braze by creating custom attributes that denote whether a Braze profile is part of a segment. Each ActionIQ audience corresponds to a unique boolean custom attribute.

The standard naming convention for the custom attribute created is: `AIQ_<Audience ID>_<Split ID>`.

To create a segment of these users, in Braze, navigate to **Segments**, create a new segment, and select **Custom Attributes** as your filter. From here, you can choose the ActionIQ custom attribute. After the segment is created, you can select it as an audience filter when creating a campaign or Canvas.

Additionally, this integration will update any Custom or Standard attribute in a user's Braze profile with their ActionIQ attribute values.

#### Requirements

_Required Permissions:_ `users.track` and `user.export.ids`

In ActionIQ, set up a Braze connection by providing your REST API key and Braze REST endpoint. 

To match to consumers in the Braze platform, the following identifiers must be included in your activation setting:
- `braze_id`
- `external_id`

### Events

The ActionIQ platform can be configured to receive event information through its streaming ingest service. This integration option forwards these Events to Braze, for marketers to use for orchestration or the triggering of marketing campaigns.

The event integration is able to send additional ActionIQ attributes as part of the properties within the event payload.

#### Requirements

_Required Permissions:_ `users.track` and `user.export.ids`

The events integration sends the following information to Braze:
- Event name
- Consumer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event properties, which are populated by any additional attributes in the export setting

### Triggered Campaigns

This integration will trigger a Campaign in Braze for all users in an ActionIQ segment. Once you have configured your Campaign's copy, multivariate testing and re-eligibility rules, you can trigger it from any ActionIQ Journey touchpoint by just adding the Braze Campaign ID to your export setting.

Optionally, you can include any other ActionIQ attributes in your export to populate your Campaign copy. Those are sent via the `trigger_properties` object.

#### Requirements

_Required Permissions:_ `campaigns.trigger.send` and `campaigns.list`

The following values must be sent in your ActionIQ export to Braze:
- Consumer identifier (either `braze_id` or `external_id`)
- Campagin ID

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/
[3]: https://www.actioniq.com/get-started/
