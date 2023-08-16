---
nav_title: Antavo Loyalty Cloud
article_title: Antavo Loyalty Cloud
page_order: 1

description: "Next-gen loyalty programs that go beyond rewarding purchases: learn more about why to use Antavo Loyalty Cloud and Braze together."
alias: /partners/antavo/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Antavo Loyalty Cloud

[Antavo](https://antavo.com/) is an enterprise-grade SaaS loyalty technology provider that builds comprehensive loyalty programs to foster brand love and change customer behavior.

The Antavo and Braze integration allows you to use loyalty program-related data to build personalized campaigns thus enhancing the customer experience. Antavo supports **loyalty data synchronization** between the two platforms - this is a one-way data synchronization only, from Antavo to Braze.
The integration supports the **external_id** Braze field, this is the field Antavo synchronizes the loyalty member ID to.

## Prerequisites

| REQUIREMENT          | DESCRIPTION                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Antavo account       | An [Antavo](https://antavo.com/) account with the Braze integration enabled is required to take advantage of this partnership.                                               |
| Braze REST API key   | A Braze REST API key with users.track permissions.<br>A new API key can be created within the **Braze Dashboard > Settings > API keys > REST API Key > Create New API Key**. |
| Braze REST endpoint  | [Your REST endpoint URL](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.               |
| Braze App identifier | Identifier of your Braze app.Locate the App identifier by navigating to **Braze Dashboard > Settings > App Settings > API key.**                                             |

## Connect Braze in Antavo

In Antavo, go to **Modules > Braze** and click **Configure**. When first navigating to the Braze integration configuration page in Antavo, the interface will prompt you to connect the two systems.

The following credentials should be provided:

- **Instance URL**: Insert the Braze REST endpoint of the instance you are provisioned to.

- **API Token (Identifier)**: Enter the Braze REST API key that Antavo should use when sending requests to Braze.

- **App Identifier**: Enter the Braze App identifier.

After you have entered the credentials, click **Connect**.

![topic_name][1]


## Configure field mapping

After the connection is established, you’ll be redirected to the **Sync Fields** page automatically in Antavo to configure the field synchronization between the two systems.  
You can reach this page anytime through **Modules > Braze.**

![topic_name][2]

- Click **Add new field +.**

- Use the dropdown field to select the Antavo **Loyalty field** that you’d like to synchronize to Braze.

- Enter the **Remote field** that represents the equivalent field in Braze to which the data will be populated.  
  Find your Braze fields under **Braze Dashboard > Data Settings > Custom Attributes**. If the field you enter is not defined in Braze, a new field will automatically be generated with the first sync.

- You can add further field pairings by repeating the first 3 steps.

- To remove a field from the list of synchronized data, click **X** at the end of the row.

- Click **Save**.

When any value of the configured fields changes in Antavo, not only the synchronization of that single value is triggered, but every field added to the field mapping is included in the request.

{% alert important %}
To ensure you minimize data point consumption, we recommend only mapping the fields that will be actioned on within Braze.
{% endalert %}

The integration supports all the Braze custom attribute [data types](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage), namely: number (integer, float), string, array, boolean, object, array of objects, and date.

![topic_name][3]
The data fields are populated based on the configured field mapping.


## Triggers

In addition to configuring field mapping, the integration provides further capabilities through features built into Antavo’s [Workflows](/wiki/spaces/AUM/pages/581402629) tool. All the Braze custom attribute [data types](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) and custom event property [data types](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events#expected-format) can be synchronized through workflows as well.

- **Synchronizing loyalty data occasionally**  
  Use this option if the data is not stored in loyalty fields in Antavo or if the data is not added to the list of mapped fields. The synchronization of requested data is triggered when the configured workflow criteria are met.
  Visit the step-by-step guide to learn how to configure the [synchronization of loyalty data related to the last purchase](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

- **Synchronizing loyalty program events**  
  Use events synchronized from Antavo to enter loyalty members in action-based Braze Canvases. The integration can synchronize any Antavo event (including purchase events) that appear in Braze as custom events.
  Visit the step-by-step guide to learn how to configure the [synchronization of the loyalty program enrollment event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) and the [synchronization of the loyalty program benefit earning event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).

[1]: {% image_buster /assets/img/antavo/connect_braze.png %}
[2]: {% image_buster /assets/img/antavo/data_field_mapping.png %}
[3]: {% image_buster /assets/img/antavo/braze_profile.png %}