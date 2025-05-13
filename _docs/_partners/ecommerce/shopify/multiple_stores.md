---
nav_title: Multiple Store Support
article_title: Shopify Multiple Store Support
alias: /shopify_multiple_store_support/
page_order: 5
description: "This reference article covers how to connect multiple Shopify stores to a single workspace."
---

# Shopify multiple store support

> Connect multiple Shopify store domains to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.  

Multiple store support for Shopify allows you to connect and configure regional storefronts. 

{% alert important %}
This feature doesn't support Shopify Markets or Markets Pro. If you would like to request support for these, submit a [product request]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Requirements

| Requirement | Description |
| ----------- | ----------- |
| Unique Shopify storefront domains for each region | Multiple store support is intended for use with unique Shopify store domains for different regional storefronts. <br><br>If you want to connect multiple sub-brands to Braze, we recommend creating separate workspaces for each sub-brand. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Setting up an additional store
1. After you install the Braze app to your Shopify store and install your first store, select the **+ Connect New Store** option.

![The "+ Connect New Store" button on the Shopify integration page.][1]{: style="max-width:80%;"}

{: start="2"}
2. Complete the integration setup for each additional Shopify regional store. 

![The "Integration settings" section with a button to "Begin setup".][2]{: style="max-width:80%;"}

{: start="3"}
3. Similar to your initial Shopify store onboarding, you can onboard using either the standard setup or custom setup. 

!["Enable the Braze SDKs" section with options to implement the Braze Web SDK with the standard or custom setup.][3]{: style="max-width:80%;"}

### Integration options

Braze offers two integration options for Shopify merchants that are designed to meet the diverse needs of eCommerce businesses: **Standard integration** and **Custom integration**.

{% tabs local %}
{% tab standard %}
The standard integration is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

To use the standard Shopify integration, refer to [Shopify standard integration setup]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab custom %}
The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. Whether you’re looking to create unique customer experiences or optimize specific workflows, the custom integration provides the tools necessary to fully leverage Braze’s capabilities in a headless setup.

To use the custom Shopify integration, refer to [Shopify custom integration setup]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

To view each store integration and configure advanced settings, select a store in the dropdown menu.

!["Integration settings" with a dropdown menu to select a Shopify store.][4]{: style="max-width:80%;"}

## Shopify user syncing  

### Shopify alias

When you connect multiple stores, synced Shopify users who have logged in or placed an order will receive a new alias in the format: `shopify_customer_id_{{storename}}`.

### Identity management considerations 

#### Using Shopify Customer ID

If you use Shopify's customer ID as your Braze external ID, each store will generate a unique customer ID for each customer. This means that if a customer interacts with multiple stores, they will have separate profiles in Braze.

#### Using Email, Hashed Email, or Custom External IDs 

If you use the email, hashed email, or custom external ID types, users who engage with multiple stores will have their profiles merged into a single consolidated profile when they log in or place an order.

#### Fields that merge when merging profiles

These are notable fields that will merge when you merge user profiles:

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

For full details on merging behavior, refer to [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Subscriber collection

#### Email and SMS subscriber collection (optional) 

When you connect and configure each Shopify store in Braze, you have the option to enable the email and SMS subscriber collection feature. This feature allows Braze to collect email and SMS subscriber opt-ins and organize them into a dedicated subscription group.
To maintain clean data on where subscribers are coming from, create a unique subscription group for each store you connect.

#### Integrate directly to Braze endpoints (alternative) 

If you decide not to enable the email and SMS subscriber collection through the integration, Braze provides several alternatives to sync email and SMS marketing opt-in information directly from Shopify:

##### APIs 
- [Subscription group endpoints]({{site.baseurl}}/api/endpoints/subscription_groups/) to directly replace what is supported by the integration 
- [`Users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) to set subscription group data or the [global email subscription state]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)
- [Braze preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) for more customized marketing opt-in collection options 

##### SDKs 
- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)
- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)
- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)
- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)

## Shopify data 

### Shopify standard and custom attributes

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

### eCommerce recommended events and Shopify custom events 

#### eCommerce recommended events 

When you connect multiple stores, incoming eCommerce recommended events will include a source event property. This property identifies which storefront URL the event originated from, allowing you to use this information for segmentation or triggering specific use cases.

![An action-based Canvas with a trigger to enter users who perform the `ecommerce.order_placed` custom event.][5]{: style="max-width:80%;"}

The supported eCommerce recommended events within the Shopify integration are:
- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify custom events 

Incoming Shopify custom events include an event property called `shopify_storefront`. This property indicates which storefront URL the event came from, enabling you to leverage it for segmentation or triggering use cases.

![An action-based Canvas with a trigger to enter users who perform the `shopify_paid_order` custom event.][6]{: style="max-width:80%;"}

Supported Shopify custom events include:
- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

For a complete overview of all event payloads, refer to [Shopify data features]({{site.baseurl}}/shopify_data_features/).

### Shopify product sync 

When you connect and configure each Shopify store in Braze, you can optionally enable the Shopify product sync as part of the integration.

If you activate the product sync for each store, Braze will include the name of your Shopify store in the catalog name. This helps you distinguish products from different stores.

![Shopify catalogs with their Shopify store in their name.][7]

[2]: {% image_buster /assets/img/Shopify/begin_setup_button.png %}
[3]: {% image_buster /assets/img/Shopify/standard_or_custom.png %}
[4]: {% image_buster /assets/img/Shopify/store_dropdown_menu.png %}
[5]: {% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}
[6]: {% image_buster /assets/img/Shopify/shopify_paid_order.png %}
[7]: {% image_buster /assets/img/Shopify/catalog_store_name.png %}