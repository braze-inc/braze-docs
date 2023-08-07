---
nav_title: Shopify Catalogs
article_title: Shopify Catalogs
alias: /shopify_catalogs/
page_order: 5
description: "This reference article covers how to import your products from Shopify into Braze catalogs."
---

# Shopify catalogs 

> Shopify catalogs allow you to import your products from your Shopify store into a Braze [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), making it easier and automated to bring in product data for deeper personalization of your messages. This Shopify catalog will update in near real-time as you make edits and changes to the products in your Shopify store. You can enrich your abandoned cart, order confirmation, and more with the most up-to-date product details and information.

## Setting up Shopify catalog sync

If you have already installed your Shopify store, you can still import your products by following the instructions below. 

### Step 1: Turn on the sync

You can activate the sync for importing your products to our catalog through the Shopify install flow or on the Shopify partner page. Products imported into a catalog will contribute to your [Catalog limit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits).

### Step 2: Select your product identifier

Select what product identifier to use as the catalog ID:
- Shopify Variant ID
- SKU

This will be the primary identifier you use to reference Braze catalog information. 

{% alert note %}
If you are selecting SKU as your catalog ID, ensure that all your products and variants in your store have a SKU set and they are unique. 
- If an item has a missing SKU, Braze cannot import that product into the catalog. 
- If you have more than one product with the same SKU, this can cause unexpected behavior, such as an error in the import, or result in product information being overridden unintentionally by the duplicate SKU. 
{% endalert %}

### Step 3: Import in progress

You will receive a dashboard notification, and your status will display as “In Progress” to indicate the initial import is starting. Note that the time it takes for the import to finish will depend on how many products and variants Braze will need to sync over from Shopify. During this time, you can leave this page and wait for a dashboard notification or email to notify you when this is complete.

Note that if your initial import exceeds your [catalog limit](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits), the import will stop syncing any more products. If you exceed the limit after the import is successful due to new products being added over time, the sync will no longer be active. In both these cases, product updates from Shopify will no longer be reflected in Braze. Reach out to your account manager to consider upgrading your tier. 

### Step 4: Import completed

You will receive a dashboard notification and an email after the import has been completed. The Shopify partner page will also update the status under Shopify catalogs to “Syncing,” you can view your products by clicking the catalog name on the Shopify partner page.

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
Modifying the Shopify catalog in any way may unintentionally interfere with real-time product syncs. Do not make any edits to the Shopify catalog, as these have the potential to be overridden by Shopify. Instead, make the necessary product updates in your Shopify instance.<br><br>To delete your Shopify catalog, go to the Shopify page and deactivate sync. Do not delete the Shopify catalog directly on the catalogs page. 
{% endalert %}

## Changing catalog ID

To change the product identifier for your Shopify catalog, you will need to deactivate the sync.   Ensure you have stopped any sends using this Shopify catalog data first. Re-run the Shopify catalog initial import and select your desired product identifier by following the [catalog sync](#setting-up-shopify-catalog-sync) steps.

## Deactivating your Shopify catalogs

Deactivating the Shopify catalog feature will delete your entire catalog and products. This can also impact any sends that may be actively using the product data from this catalog. Ensure you either update or pause these sends before deactivation, as this could result in your messaging sending missing product details. Do not delete the Shopify catalog directly on the catalogs page.

## Troubleshooting
If your Shopify catalog runs into an error during import or syncing, it could be a result of the following errors. Follow the instructions on how to correct the issue and resolve the sync:

| Error | Reason | Solution |
| --- | --- | --- |
| Server Error | This occurs if there is a server error on Shopify’s side when we attempt to import or sync your products. | [Deactivate sync](#deactivating-your-shopify-catalogs) and re-import your entire inventory of products again. |
| Duplicate SKU Error | This occurs if you use a SKU as your catalog item ID and have products with the same SKU. Since catalog item ID has to be unique, all your products must have unique SKUs. | Audit your full list of products and variants in Shopify to ensure that there are no duplicate SKUs. If there are duplicate SKUs, update these to be unique SKUs only in your Shopify store account. After this is corrected, [deactivate sync](#deactivating-your-shopify-catalogs) and re-import your entire inventory of products again. |
| Catalog Limit Exceeded | This occurs if you exceed your catalog limit. Braze will be unable to finish the import or keep the syncing active due to no more storage availability. | There are two solutions to this issue:<br><br>1. Reach out to your account manager to upgrade your tier to increase your catalog limit. <br><br>2. Free up storage space by deleting any of the following:<br>- Catalog items from other catalogs<br>- Other catalogs<br>- Selections created |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}
