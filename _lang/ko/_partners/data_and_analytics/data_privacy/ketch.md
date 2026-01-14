---
title: Ketch
nav_title: Ketch
description: "This reference article covers the Braze and Ketch integration. Ketch provides simplified privacy operations and complete, dynamic data control, and intelligence."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) enables businesses to be responsible stewards of their data. Ketch provides simplified privacy operations and complete, dynamic data control and intelligence. 

_This integration is maintained by Ketch._

## About the integration

The Braze and Ketch integration allows you to control customer communication preferences within the Ketch preference center and automatically propagate these changes to Braze. 

{% alert note %}
Looking for guidance on creating subscription groups? Check out our articles for <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS subscription groups</a> and <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>email subscription groups</a>.
{% endalert %}

## Prerequisites

| Requirements | Description |
|---|---|
| Ketch Account | A [Ketch](https://www.ketch.com) account with admin privileges is required activate this integration. |
| Braze API key | A Braze REST API key with `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe`, and `email.blacklist` permissions. <br><br> This can be created in the Braze dashboard (**Developer Console** > **REST API Key** > **Create New API Key**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up the Braze connection

1. In your [Ketch instance](https://app.ketch.com), navigate to **Data Systems**, and select **Braze**. Then, click **New Connection**.
2. Give your Braze connection an identifiable name, which will be used to refer to this connection in API-based processes. Note that a code will also be created for that connection. This code should be unique across all connections.
3. Confirm the identity mapping of your users. By default, Ketch will map user identities by a user's email address, or by the `external_id` in Braze.
4. Add the Braze API key and provide the API endpoint. Note this [API endpoint]({{site.baseurl}}/api/basics/#endpoints) is based on which Braze instance your organization is using.

### Step 2: Configure subscription preferences

1. Go to **Policy Center > Subscriptions**. If you do not see the subscriptions tab under **Policy Center**, make sure you have access to the marketing preference center, and verify that you have the correct account permissions to access this portion of the product.
2. Click **Create New Subscription** to create a new topic. Each subscription will have a name and a code.
3. Add the channels for sending your subscription topics. Each channel will show in the marketing preference center for your users. You can also add the details of how you want the Ketch preference center to orchestrate a particular opt-in or opt-out signal.
4. Select the Braze connection you would like to use to orchestrate the opt-in and opt-out signals.
5. Enter the Braze `subscription_group_id` for the subscription group to which you want to send the Ketch user preferences.

![Braze Subscription Group ID.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
In order to collect and orchestrate user opt-in and opt-out signals, identities must be properly configured. Ketch recommends configuring email as the identifier to orchestrate user preference signals for this integration.
{% endalert %}


### Step 3: Configure identities

A user can only see the marketing preference center when Ketch can confirm that user's marketing preference identity. If Ketch cannot capture the user's identity properly, then the marketing preferences page will not display to that user since Ketch is be unable to manage their user preferences.

1. To configure the marketing preference identity, go to the **Settings** page in Ketch, and click  **Identity space**. You will need to either create a new identity space or edit an existing identity space to assign that identity space as the marketing preference identity. Check that the Ketch tag deployed on the property properly captures that identity space.
2. Go to **Experience Server** > **Properties**, and edit the desired property. Under the data layer for that property, make sure to enable the custom identity space. Then, configure how the marketing preference identity is captured on this site.
3. After you have the identity space configured, test to see if the preference center appears by opening the preference center on the website where the Ketch tag has been deployed.


