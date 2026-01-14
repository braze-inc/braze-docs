---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "This reference article outlines the partnership between Braze and Antavo, a next-gen loyalty program that goes beyond rewarding purchases."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) is an enterprise-grade SaaS loyalty technology provider that builds comprehensive loyalty programs to foster brand love and change customer behavior.

_This integration is maintained by Antavo._

## About the integration

The Antavo and Braze integration allows you to use loyalty program-related data to build personalized campaigns to enhance the customer experience. Antavo supports loyalty data synchronization between the two platforms—this is a one-way data synchronization only, from Antavo to Braze. The integration supports the `external_id` Braze field, which Antavo uses to synchronize the loyalty member ID.

## Prerequisites

| Requirement          | Description                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo account       | An [Antavo](https://antavo.com/) account with the Braze integration enabled is required to take advantage of this partnership.                                                |
| Braze REST API key   | A Braze REST API key with the following permissions: `users.track`, `events.list`, `events.data_series`, and `events.get`.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**.  |
| Braze REST endpoint  | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                |
| Braze app identifier | Your app identifier key. <br><br>To locate this key in the Braze dashboard, go to **Settings** > **API Keys** and find the **Identification** section. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect Braze in Antavo

In Antavo, go to **Modules** > **Braze** and click **Configure**. When first navigating to the Braze integration configuration page in Antavo, the interface will prompt you to connect the two systems.

Provide the following credentials:

- **Instance URL:** The Braze REST endpoint of the instance you are provisioned to.
- **API Token (Identifier):** The Braze REST API key that Antavo should use when sending requests to Braze.
- **App Identifier:** The Braze app identifier.

After you enter the credentials, click **Connect**.

![Connect Braze screen in Antavo with Instance URL, API Token, and App Identifier.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Step 2: Configure field mapping

After the connection is established, you’ll be redirected to the **Sync Fields** page automatically in Antavo to configure the field synchronization between the two systems.   You can reach this page at any time through **Modules** > **Braze**.

To configure field mapping in Antavo:

1. Click **Add new field** <i class="fas fa-plus" alt=""></i>.
2. Use the dropdown field to select the Antavo **Loyalty field** that you want to synchronize to Braze.
3. Enter the **Remote field** that represents the equivalent custom attribute in Braze to which the data will be populated.  

{% alert note %}
You can find your list of custom attributes in Braze under **Data Settings** > **Custom Attributes**. If the field you enter is not defined in Braze, a new field will automatically be generated with the first sync.
{% endalert %}

{:start="4"}
4. To add additional field pairings, repeat steps 1–3.
5. To remove a field from the list of synchronized data, click <i class="fa-solid fa-rectangle-xmark" title="Delete"></i> at the end of the row.
6. Click **Save**.

When any value of the configured fields changes in Antavo, not only the synchronization of that single value is triggered, but every field added to the field mapping is included in the request.

![Sync Fields page in Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
To minimize data point usage, we recommend only mapping the fields that will be actioned on within Braze.
{% endalert %}

#### Supported data types

The integration supports all Braze custom attribute [data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage), namely: number (integer, float), string, array, boolean, object, array of objects, and date.

![Braze profile showing different custom attributes.]({% image_buster /assets/img/antavo/braze_profile.png %})

The data fields are populated based on the configured field mapping.

## Triggers

In addition to configuring field mapping, the integration provides further capabilities through features built into Antavo’s [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) tool. All Braze custom attribute [data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) and custom event property [data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) can be synchronized through workflows as well.

### Synchronizing loyalty data occasionally

Use this option if the data is not stored in loyalty fields in Antavo or if the data is not added to the list of mapped fields. The synchronization of requested data is triggered when the configured workflow criteria are met.

Visit the step-by-step guide to learn how to configure the synchronization of [loyalty data related to the last purchase](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Synchronizing loyalty program events

Use events synchronized from Antavo to enter loyalty members in action-based Braze Canvases. The integration can synchronize any Antavo event (including purchase events) that appears in Braze as custom events.

Visit the step-by-step guide to learn how to configure the synchronization of the [loyalty program enrollment event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) and the synchronization of the [loyalty program benefit earning event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).


