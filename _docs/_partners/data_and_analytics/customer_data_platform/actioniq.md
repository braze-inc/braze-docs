---
nav_title: Actioniq
article_title: ActionIQ
description: "This reference article covers the Braze and ActionIQ integration. ActionIQ is an enterprise customer data platform for marketers, analysts, and technologists. This integration allows brands to sync and map their ActionIQ data directly to Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/) is a customer data platform for enterprise brands that gives marketers easy and secure ways to activate data anywhere in the customer experience. ActionIQ’s unique composable architecture means data can stay securely where it lives, and marketing teams only use the tools they need.

_This integration is maintained by ActionIQ._

## About the integration

The Braze and ActionIQ integration allow brands to sync and map their ActionIQ data directly to Braze, empowering the delivery of extraordinary customer experiences based on the entire breadth of their customer data. The integrations available allow users to:

- Update user profiles in Braze with audience membership information and any attributes directly from ActionIQ
- Forward the events tracked by ActionIQ to Braze in real time to trigger personalized and targeted campaigns
- Deliver API-triggered campaigns in Braze directly from touchpoints in an ActionIQ journey

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| ActionIQ account | An ActionIQ account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with the required permissions for the respective integration. See the respective Requirements section for more details. <br><br>This key can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrations

### Audience membership

This integration is used to sync ActionIQ audience membership to Braze by creating custom attributes that denote whether a Braze profile is part of a segment. Each ActionIQ audience corresponds to a unique boolean custom attribute.

The standard naming convention for the custom attribute created is: `AIQ_<Audience ID>_<Split ID>`.

To create a segment of these users, do the following:
1. In Braze, navigate to **Segments**.
2. Create a new segment.
3. Select **Custom Attributes** as your filter.
4. From here, choose the ActionIQ custom attribute. 
5. After the segment is created, you can select it as an audience filter when creating a campaign or Canvas.

Additionally, this integration will update any custom or standard attribute in a Braze user profile with their ActionIQ attribute values.

#### Requirements

A Braze REST API key with `users.track` and `user.export.ids` permissions is required. This can be created in the Braze dashboard from **Settings** > **API Keys**. 

In ActionIQ, set up a Braze connection by providing your REST API key and Braze REST endpoint. 

To match to consumers in the Braze platform, the following identifiers must be included in your activation setting:
- `braze_id`
- `external_id`

### Events

You can configure the ActionIQ platform to receive event information through their streaming ingest service. This integration option forwards these events to Braze for marketers to use for orchestration or for triggering marketing campaigns. The event integration is able to send additional ActionIQ attributes as part of the properties in the event payload.

#### Requirements

A Braze REST API key with `users.track` and `user.export.ids` permissions is required. This can be created in the Braze dashboard from **Settings** > **API Keys**. 

The events integration sends the following information to Braze:
- Event name
- Consumer identifier (either `braze_id` or `external_id`)
- Timestamp
- Event properties, which are populated by any additional attributes in the export setting

### Triggered campaigns

This integration will trigger a campaign in Braze for all users in an ActionIQ segment. After you have configured your campaign's copy, multivariate testing, and re-eligibility rules, you can trigger it from any ActionIQ journey touchpoint by adding the Braze campaign ID to your export setting.

Optionally, you can include any other ActionIQ attributes in your export to populate your campaign copy. Those are sent with the `trigger_properties` object.

#### Requirements

A Braze REST API key with `campaigns.trigger.send` and `campaigns.list` permissions is required. This can be created in the Braze dashboard from **Settings** > **API Keys**.

The following values must be sent in your ActionIQ export to Braze:
- Consumer identifier (either `braze_id` or `external_id`)
- Campaign ID


