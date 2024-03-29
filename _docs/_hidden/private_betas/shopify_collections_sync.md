---
nav_title: Shopify Collections Sync
article_title: Shopify Collections Sync
permalink: "/shopify_collections_sync/"
description: "This reference article covers how to set up the Shopify collections sync, which allows you to group your products into collections so customers can find your products by category."
hidden: true
---

# Shopify collections sync beta

> The Shopify collections sync allows you to group your products into collections so customers can find your products by category. For a more seamless shopper experience, you can incorporate items within your shop’s collections in your Braze messaging.

{% alert important %}
Shopify collections sync is currently in beta. Contact your Braze account manager if you want to participate in the beta.
{% endalert %}

## Setting up Shopify collections sync

To sync your products from your Shopify store to Braze, select the checkbox to **Sync Shopify collections** in the **Sync products** step of [integrating Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Step 4 of the Shopify product sync with the "Sync Shopify collections" checkbox selected.][1]

Once your products have been synced, you can view which products are associated with your collections by viewing your Shopify catalog. <br><br>![Catalog table row showing a product in the collections of "best-sellers" and "frontpage".][2]

From your Shopify catalog, you can view your Shopify collection in the **Selections** tab. <br><br>![The Selections tab showing a list of two collections: "best-sellers" and "frontpage".][3]

### Beta functionality

- Braze will support up to 30 collections
- Sort order for your collection is not maintained or supported at this time. For now, the sort order that is based on the following:
    - The most recent items added to your collection.
    - The order in which items are updated during continuous syncs.
    - The order you select in the selection tab for your Shopify collection.

## Using Shopify collections

Use your Shopify collections to personalize a message for each user in your campaign, similar to how you'd use a [Braze selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Be aware of the following behavior in the beta: <br><br>If you update the Shopify collection description or the filter settings, you will break your Shopify collection sync. As a result, your Shopify collection will not work as expected. 
{% endalert %}

### Step 1: Configure the sort order of your Shopify collection

1. Specify the order in which your Shopify collection results are returned by selecting the **Sort Order** in the selection tab for your Shopify collection. This includes an option to randomize the sort order.
2. Enter the maximum number of results (up to 50) for the **Limit number**.
3. Select **Update Selection**.

![The Edit Selection page where you can select the filter settings, sort type, and results limit.][4]

### Step 2: Use the collection in a campaign

1. Create a campaign, then select **+ Personalization** in the Message composer.
2. Select the following:<br>- **Catalog Items** as the **Personalization type**<br>- The catalog name<br>- The item selection method<br>- The selection name (your Shopify collection name) <br>- The information to display in your message

{: start="3"}
3. Copy and paste the Liquid snippet where you want the information to appear in your message.

![The "Add Personalization" section with fields to select your catalog, item selection method, and the information to display.][5]{: style="max-width:30%;"}

#### Liquid in selection results

Using any results in catalogs, such as custom attributes and custom events, can cause different results to return for each user in your selection.

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
