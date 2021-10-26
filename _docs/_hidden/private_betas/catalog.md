---
nav_title: Catalog
permalink: "/catalog/"
hidden: true
---

# Catalog

You can use a catalog to reference non-user data in your Braze campaigns through Liquid.

To do so, first import your catalog (a CSV of non-user data) into Braze, and then access that information to enrich your messages. You can bring in any type of data into a catalog. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

Once this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

{% alert important %}
Catalogs are currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

If you'd like to share your feedback on this feature or make a request, you can [book a session](https://calendly.com/d/yzvf-frpy/catalog-beta-working-session?month=2021-10) with the Braze Data Ingestion team on Calendly!

## Creating a catalog

To create a catalog in Braze, upload a CSV to the **Catalogs** page. Each CSV you upload will be its own distinct catalog. Each catalog has an identifier, which you can use to reference data from that catalog in a later step.

### Step 1: Create your CSV

First, create your CSV file. The CSV must have one column with a header of **id**, and each item's **id** must be unique. Additionally, the following limitations apply to catalog CSV files:

- Maximum of 1,000 items (rows)
- Maximum of 20 fields (columns)
- Maximum field value (cell) size of 0.5kb
- Maximum CSV file size of 10MB

For this tutorial, we're using a catalog that lists two games, their cost, and an image link:

![The table shows two example games with columns for id, title, price, and image_link][5]

### Step 2: Upload your CSV

After you've created your CSV, navigate to the **Catalogs** page and upload the file. Drag and drop your file to the upload zone, or click **Upload CSV** and choose your file.

![Catalog CSV upload zone][1]

### Step 3: Take note of your catalog ID

After successfully uploading your catalog, the catalog displays in a list below the upload zone. Each catalog has an associated catalog ID—a 24 digit alphanumeric code. Keep that ID handy, you'll need it in the next step.

![Example catalog ID and associated CSV files in a list below the upload zone][2]

## Using a catalog in a message

To use a catalog in a message, you'll need the catalog ID. For our example scenario, the catalog ID for our Games catalog is `6171a881759044006998ed9a`.

### Step 1: Retrieve an item

In the message composer of your choice, use the `catalogs` Liquid tag to retrieve an item:

{% raw %}
```liquid
{% catalogs /catalogs/<CATALOG_ID>/items/<ITEM_ID> %}
```
{% endraw %}

Replace `<CATALOG_ID>` with your catalog ID and `<ITEM_ID>` with an item (row) ID from the catalog. 

For example, let's say we want to reference the tales_storefront item:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}
```
{% endraw %}

### Step 2: Reference attributes for that item

Below the `catalogs` tag, use the `item` object to reference different attributes for that item.

{% alert note %}
Remember, Liquid is case sensitive! Make sure you exactly match the case used in your catalog. In our example catalog, we used lowercase for our columns, so we're using lowercase in the `item` objects.
{% endalert %}

For example, to reference the title and price of the tales_storefront item we could add the following:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}
 
Get {{ item.title }} for just {{ item.price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!

#### Multiple items

You aren't limited to just one item in a single message! To reference multiple items from your catalog in one message, repeat the `catalog` tag and replace the `<ITEM_ID>` with a different item from your catalog. Refer to the following as an example:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}
 
Get {{ item.title }} for just {{ item.price }}!
 
{% catalogs /catalogs/6171a881759044006998ed9a/items/reformation_storefront %}
 
Get {{ item.title }} for just {{ item.price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!<br>
> Get Reformation for just 22.49 USD!

#### Using images

You can also reference images in the catalog to use in your messaging. To do so, use the `catalogs` tag and `item` object in the Liquid field for images.

For example, to add the image_link from our Games catalog to our promotional message for Tales, we can add the following to our image field:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}

{{ item.image_link }}
```
{% endraw %}

![Push message composer with catalog Liquid tag used in the Push Icon Image field][3]

Here's what this looks like when the Liquid is rendered:

![Example iOS push notification with catalog Liquid tags rendered][4]{: style="max-width:60%" }

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/catalog_id.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
