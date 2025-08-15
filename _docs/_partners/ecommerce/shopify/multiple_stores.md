---
nav_title: Connecting multiple stores
article_title: Shopify Multiple Store Support
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "This reference article covers how to connect and configure multiple Shopify stores to a single workspace."
---

# Connecting multiple Shopify stores

> Connect multiple Shopify store domains to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.  

{% alert important %}
This feature doesn't support Shopify Markets or Markets Pro. If you would like to request support for these, submit a [product request]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Requirements

| Requirement | Description |
| ----------- | ----------- |
| Enable multiple stores | Contact your customer success manager to enable Shopify multiple store support. |
| Set up a Shopify store | Be sure that you've already [set up at least one Shopify store with Braze]({{site.baseurl}}/shopify_overview/). |
| Unique Shopify storefront domains for each region | Multiple store support is intended for use with unique Shopify store domains for different regional storefronts. <br><br>If you want to connect multiple sub-brands to Braze, we recommend creating separate workspaces for each sub-brand. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Connecting an additional store
After you install the Braze app to your Shopify store and install your first store, select **+ Connect New Store**.

![The "+ Connect New Store" button on the Shopify integration page.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

For your additional Shopify regional store, select **Begin setup**.

![The "Integration settings" section with a button to "Begin setup".]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Like your first Shopify store integration, you can choose either between a standard or custom setup.

!["Enable the Braze SDKs" section with options to implement the Braze Web SDK with the standard or custom setup.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Choose the option that best fits your needs:

{% multi_lang_include shopify.md section='Integration Tabs' %}

To view each store integration and configure advanced settings, select a store in the dropdown menu.

!["Integration settings" with a dropdown menu to select a Shopify store.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Syncing users across stores

### Shopify alias

When you connect multiple stores, synced Shopify users who have logged in or placed an order will receive a new alias in the format: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Braze external ID

You can choose from the following options for your Braze external ID:

|Option|Description|
|------|-----------|
|Shopify Customer ID|If you use Shopify's customer ID as your Braze external ID, each store will generate a unique customer ID for each user. This means that if a user interacts with multiple stores, they will have separate profiles in Braze.|
|Email, Hashed Email, or Custom External ID|If you use the email, hashed email, or custom external ID types, users who engage with multiple stores will have their profiles merged into a single consolidated profile when they log in or place an order.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Merged fields

When a user profile is synced, the following fields will be merged. For full details on merging behavior, refer to [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Device information
- Total session count (combined from both profiles)
- Custom event and purchase data
- Custom event properties for segmentation (for example, “X times in Y days” where X ≤ 50 and Y ≤ 30)
- Event count (combined from both profiles)
- Dates of first and last events (Braze selects the earliest and latest dates)
- Campaign interaction data (most recent date fields)
- Workflow summaries (most recent date fields)
- Message and engagement history
- Subscription groups

### Collecting subscribers (optional)

You can choose to collect subscribers directly through Braze (in your Shopify connector settings) or through API and SDK alternatives that sync data from Shopify.

{% tabs local %}
{% tab Shopify connector %}
In the **Manage users** step of your Shopify connector settings, you can use Braze to collect email and SMS subscriber opt-ins and organize them into a dedicated subscription group:

1. Create a unique subscription group for each store you connect. This helps you maintain accurate data about where subscribers are coming from.
2. Enable email and SMS subscriber collection.
{% endtab %}

{% tab Braze API or SDKs %}
Alternatively, you can sync email and SMS marketing opt-in information directly from Shopify using the Braze API or SDKs.

|Option|Resources|
|------|---------|
|API |- [Subscription group endpoints]({{site.baseurl}}/api/endpoints/subscription_groups/) to directly replace what is supported by the integration<br>- [`Users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) to set subscription group data or the [global email subscription state]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Braze preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) for more customized marketing opt-in collection options|
|SDKs |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Shopify data 

### Synced attributes

When you connect more than one store, the following attributes will be synced with the most recent state of the Shopify profile:
- First Name
- Last Name
- Email
- Gender
- Date of Birth
- Country
- City
- Last Used App
- Language
- Time Zone
- Shopify Tags
- Shopify Order Count
- Shopify Total Spent

### Supported events

#### eCommerce recommended events 

When you connect multiple stores, incoming eCommerce recommended events will include a source event property. This property identifies which storefront URL the event originated from, allowing you to use this information for segmentation or triggering specific use cases.

![An action-based Canvas with a trigger to enter users who perform the `ecommerce.order_placed` custom event.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

The supported eCommerce recommended events within the Shopify integration are:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify custom events 

Incoming Shopify custom events include an event property called `shopify_storefront`. This property indicates which storefront URL the event came from, allowing you to leverage it for segmentation or triggering use cases.

![An action-based Canvas with a trigger to enter users who perform the `shopify_paid_order` custom event.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Supported Shopify custom events include:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

For a complete overview of all event payloads, refer to [Shopify data features]({{site.baseurl}}/shopify_data_features/).

### Shopify product sync 

When you connect and configure each Shopify store in Braze, you can optionally enable the Shopify product sync as part of the integration.

If you activate the product sync for each store, Braze will include the name of your Shopify store in the catalog name. This helps you distinguish products from different stores.

![Shopify catalogs with their Shopify store in their name.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

