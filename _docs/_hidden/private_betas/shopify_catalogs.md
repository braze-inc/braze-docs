---
nav_title: Shopify Catalogs
article_title: Shopify Catalogs
permalink: "/shopify_catalogs/"
description: "This reference article covers how to import your products from Shopify into Braze catalogs"
hidden: true
---

# Shopify Catalogs 

> Shopify Catalogs allow you to import your products from your Shopify store into Braze [Catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), making it easier and automated to bring in product data for deeper personalization of your messages. This Shopify catalog will update in near real-time as you make edits and changes to the products in your Shopify store. You can enrich your abandoned cart, order confirmation, and more with the most up-to-date product details and information.

## Setting up Shopify catalog sync
If you have already installed your Shopify store, you can still import your products by following the instructions below. 

### Step 1: Turn on the sync
You can activate the sync for importing your products to our catalog through the Shopify install flow or on the Shopify partner page. Products imported into a catalog will contribute to your [Catalog limit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits).

### Step 2: Select your product identifier 
Select what product identifier to use as the catalog ID:
- Shopify Variant ID
- SKU

This will be the primary identifier you utilize to reference catalog information in Braze. 

{% alert note %}
If you select SKU as your catalog ID, check that all your products and variants in your store have a unique SKU set. If SKU is missing, we cannot import that product into Braze. If you have more than one product with the same SKU, this can also cause data from multiple products to be overridden unintentionally.
{% endalert %}

### Step 3: Import in progress
You will receive a dashboard notification, and your status will display as “In Progress” to indicate the initial import is starting. Note that the time it takes for the import to finish will depend on how many products and variants Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a dashboard notification or email to notify you when this is complete.

Note that if your import exceeds your catalog limit, **the entire import will be rejected**. If you exceed the limit after the import is successful due to new products being added over time, we will not delete your existing Shopify catalog, but we will not be able to sync any more new products. Reach out to your Account Manager to consider upgrading your tier. 

### Step 4: Import completed
You will receive a dashboard notification and an email once the import has been completed. The Shopify partner page will also update the status under Shopify Catalogs to “Syncing,” you can view your products by clicking the catalog name on the Shopify partner page.

Refer to [Catalogs additional use cases](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases) to learn more about how to leverage catalog data to personalize your message.

#### Supported Shopify catalog data
- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `body_html`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Modifying the Shopify catalog in any way may unintentionally interfere with real-time product syncs. Do not make any edits to the Shopify catalog, as these have the potential to be overridden by Shopify. Instead, make the necessary product updates in your Shopify instance. 
{% endalert %}

## Changing catalog ID
To change the product identifier for your Shopify catalog, you will need to deactivate the sync.   Ensure you have stopped any sends using this Shopify catalog data first. Re-run the Shopify catalog initial import and select your desired product identifier by following the [Catalog sync](#setting-up-shopify-catalog-sync) steps.

## Deactivating your Shopify catalogs
Deactivating the Shopify catalog feature will delete your entire catalog and products. This can also impact any sends that may be actively using the product data from this catalog. Ensure you update those sends before deactivation. 