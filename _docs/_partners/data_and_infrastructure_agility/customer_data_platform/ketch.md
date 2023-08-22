---
title: Ketch
nav_title: Ketch
description: "This reference article covers the Braze and Ketch integration. Ketch provides simplified privacy operations and complete, dynamic data control and intelligence."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
page_order: 4.3
---

# Ketch

> [Ketch](https://www.ketch.com) enables businesses to be responsible stewards of their data. Ketch provides simplified privacy operations and complete, dynamic data control and intelligence.

The Braze and Ketch integration allows you to control customer communication preferences within the Ketch preference center to be automatically propagated to Braze in order to manage customer communication and privacy preferences. 

## Prerequisites

| Requirements | Description |
|---|---|
| Ketch Account | A [Ketch](https://www.ketch.com) account with admin privileges is required activate this integration. |
| Braze API key | A Braze REST API key with `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe`, and `email.blacklist` permissions. <br><br> This can be created within the **Braze Dashboard** > **Developer Console** > **REST API Key** > **Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

The following steps will allow you to configure and setup your Ketch and Braze systems so that Ketch can orchestrate user communications and preference signals directly to Braze.

### Step 1: Set up the Braze connection

1. In your [Ketch instance](https://app.ketch.com), navigate to **Data Systems**, and select **Braze**. Then, click **New Connection**.
2. Give your Braze connection an identifiable name, note that a code will also be created for that connection, this code should be unique across all connections and will be used to refer to this connection in API based processes.
3. Confirm the identity mapping of the users, by default, we will map user identities based off of email addresses for the user, but we can also configure it based off the `external_id` in Braze.
4. Next, add the Braze API key, and provide the API endpoint. Note this [API endpoint](https://www.braze.com/docs/api/basics/#endpoints) is based on which Braze instance your organization is using.

### Step 2: Configure subscription preferences

The subscriptions tab displays the available subscriptions. Each subscription represents a specific marketing category, while the channels under each topic represent the medium by which your users will be contacted on those topics. There is also the Global Control tab which controls the universal opt-outs from your user.

1. Go to **Policy Center > Subsriptions**. If you do not see the subscriptions tab under **Policy Center**, make sure you have purchased the marketing preference center and verify that you have the correct account permissions to access this portion of the product.
2. To create a topic, you can click the create new subscription button. Each subscription will have a name and a code, the code will be how each subscription gets referred to when referenced by the API. You can also add language translations for each of your topics in case this marketing preference center is deployed to sites supporting multiple languages. Next, you will want to add the channels which you send the subscription topics through. For each channel that you enable, that option will show up in the marketing preference center for your users.
3. Under each channel that you enable, you can also add the details of how you want the Ketch preference center to orchestrate the signals of that particular opt-in or opt-out.
4. For the integration with Braze, select the Braze connection you would like to orchestrate the opt-in and opt-out signals.
5. Enter the `subscription_group_id` for the subscription group you want to propagate the user preferences to in Braze. Ketch will then use the `user.track`, `subscriptions`, and `email` Braze REST API endpoints to orchestrate user preference. Ketch will also occasionally use the `users` endpoint to validate propagated signals.

![Braze Subscription Group ID.][1]

{% alert note %}
In order for subscription preferences to collect and orchestrate user opt-in and opt-out signals, identities must be properly configured. Ketch recommends configuring email as the identity to orchestrate user preference signals for this integration.
{% endalert %}

### Step 3: Configure identities

The ability for a user to see marketing preference center is gated behind whether Ketch can capture a proper marketing preference identity for that user. If Ketch cannot capture the user identity properly, then the marketing preferences page will not show since Ketch would be unable to orchestrate any user preferences without knowing how they are identified.

1. In order to configure the marketing preference identity, go to the settings page in the Ketch platform, and click  **Identity space**. You will need to either create a new identity space or edit an existing identity space to assign that identity space as the marketing preference identity.
2. Once you have selected the desired identity space as the marketing preference identity. We will need to make sure the Ketch tag deployed on the property properly captures that identity space.
3. Go to **Experience Server** > **Properties**, and edit the desired property. Under the data layer for that property, make sure to enable the custom identity space. Then, configure how the marketing preference identity is captured on this site.
4. Once you have the identity space configured, you can open the preference center on the website where the Ketch tag has been deployed, and test to see if the preference center shows up.


[1]: {% image_buster /assets/img/ketch/ketch1.png %}