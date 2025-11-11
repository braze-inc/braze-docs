---
nav_title: Shopify Product Sync
article_title: Shopify Product Sync
alias: /shopify_catalogs/
page_order: 5
description: "This reference article covers how to import your products from Shopify into Braze catalogs."
---

# Shopify product sync 

> You can sync all products from your Shopify store to a Braze [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) for deeper messaging personalization. 

Shopify catalogs will update in near real-time as you make edits and changes to the products in your Shopify store. You can enrich your abandoned cart, order confirmation, and more with the most up-to-date product details and information.

## Setting up your Shopify product sync {#setting-up}

If you have already installed your Shopify store, you can still sync your products by following the instructions below. 

### Step 1: Turn on the sync

You can sync your products to a Braze catalog through the Shopify install flow or on the Shopify partner page. 

![Step 3 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Products synced to a Braze catalog will contribute to your [Catalog limit]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers).

### Step 2: Select your product identifier

Select what product identifier to use as the catalog ID:
- Shopify Variant ID
- SKU

The ID and header values for the product identifier you choose can only include letters, numbers, hyphens, and underscores. If the product identifier doesn't follow this format, Braze will filter it out of your catalog sync.

This will be the primary identifier you use to reference Braze catalog information. 

{% alert note %}
If you are selecting SKU as your catalog ID, make sure that all your products and variants in your store have a SKU set and they are unique. 
- If an item has a missing SKU, Braze cannot sync that product into the catalog. 
- If you have more than one product with the same SKU, this can cause unexpected behavior or result in product information being overridden unintentionally by the duplicate SKU.
{% endalert %}

### Step 3: Sync in progress

You will receive a dashboard notification, and your status will display as “In Progress” to indicate the initial sync is starting. Note that the time it takes for the sync to finish will depend on how many products and variants Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a dashboard notification or email to notify you when this is complete.

Note that if your initial sync exceeds your [catalog limit]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers), Braze will stop syncing any more products. If you exceed the limit after the sync is successful due to new products being added over time, the sync will no longer be active. In both these cases, product updates from Shopify will no longer be reflected in Braze. Contact your account manager to consider upgrading your tier. 

### Step 4: Sync completed

You will receive a dashboard notification and an email after the sync is successful. The Shopify partner page will also update the status under Shopify catalogs to “Syncing". You can view your products by clicking the catalog name on the Shopify partner page.

Refer to [Catalogs additional use cases]({{site.baseurl}}/user_guide/data/activation/catalogs/use) to learn more about how to leverage catalog data to personalize your message.

#### Supported Shopify catalog data

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Modifying the Shopify catalog in any way may unintentionally interfere with real-time product syncs. Do not make any edits to the Shopify catalog, as these have the potential to be overridden by Shopify. Instead, make the necessary product updates in your Shopify instance.<br><br>To delete your Shopify catalog, go to the Shopify page and deactivate sync. Do not delete the Shopify catalog directly on the catalogs page. 
{% endalert %}

## Back-in-stock and price-drop use cases

To set up back-in-stock notifications, follow the steps [here]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/).

To set up price drop notifications, follow the steps [here]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/).

Note that with the Shopify integration, you'll need to create a custom event that captures a user's subscription status in your catalog for each use case. The custom event will require an event property that maps to either the [SKU or Shopify variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) that you have selected as part of your Shopify product sync. 

## Changing catalog ID

To change the product identifier for your Shopify catalog, you will need to deactivate the sync. Confirm you have stopped sending any messages using this Shopify catalog data first. Re-run the Shopify catalog initial sync and select your desired product identifier by following the [product sync](#setting-up) steps.

## Deactivating your product sync {#deactivate}

Deactivating the Shopify product sync feature will delete your entire catalog and products. This can also impact any messages that may be actively using the product data from this catalog. Confirm that you have either updated or paused these campaigns or Canvases before deactivation, as this could result in sending messages with no product details. Do not delete the Shopify catalog directly on the catalogs page.

## Troubleshooting
If your Shopify product sync runs into an error, it could be a result of the following errors. Follow the instructions on how to correct the issue and resolve the sync:

| Error | Reason | Solution |
| --- | --- | --- |
| Server Error | This occurs if there is a server error on Shopify’s side when we attempt to sync your products. | [Deactivate sync](#deactivate) and re-sync your entire inventory of products again. |
| Duplicate SKU | This occurs if you use a SKU as your catalog item ID and have products with the same SKU. Because the catalog item ID must be unique, all your products must have unique SKUs. | Audit your full list of products and variants in Shopify to make sure that there are no duplicate SKUs. If there are duplicate SKUs, update these to be unique SKUs only in your Shopify store account. After this is corrected, [deactivate sync](#deactivate) and re-sync your entire inventory of products again. |
| Catalog Limit Exceeded | This occurs if you exceed your catalog limit. Braze will be unable to finish the sync or keep the syncing active due to no more storage availability. | There are two solutions to this issue:<br><br>1. Contact your account manager to upgrade your tier to increase your catalog limit. <br><br>2. Free up storage space by deleting any of the following:<br>- Catalog items from other catalogs<br>- Other catalogs<br>- Selections created<br><br> After using either of the solutions, the sync must be deactivated and then re-synced. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

