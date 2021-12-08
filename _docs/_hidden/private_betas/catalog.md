---
nav_title: Catalogs
permalink: "/catalogs/"
hidden: true
---

# Catalogs

You can use catalogs to reference non-user data in your Braze campaigns through Liquid.

To do so, first import your catalog (a CSV of non-user data) into Braze, and then access that information to enrich your messages. You can bring in any type of data into a catalog. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

Once this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

{% alert important %}
Catalogs are currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

If you'd like to share your feedback on this feature or make a request, you can [book a session](https://calendly.com/d/yzvf-frpy/catalog-beta-working-session?month=2021-10) with the Braze Data Ingestion team on Calendly!

## Creating a catalog

To create a catalog in Braze, upload a CSV to the **Catalogs** page. Each CSV you upload will be its own distinct catalog. Each catalog has an identifier; you'll use it to reference data from that catalog in a later step.

### Step 1: Create your CSV

First, create your CSV file. The CSV must have one column with a header of `id`, and each item's `id` must be unique. Additionally, the following limitations apply to catalog CSV files:

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

## Using catalogs in a message

To use your catalog in a message, you'll need the catalog ID. For our example scenario, the catalog ID for our Games catalog is `6171a881759044006998ed9a`.

### Step 1: Retrieve an item {#step-one-retrieve-item}

In the message composer of your choice, use the `catalogs` Liquid tag to retrieve an item:

{% raw %}
```liquid
{% catalogs /catalogs/<CATALOG_ID>/items/<ITEM_ID> %}
```
{% endraw %}

Replace `<CATALOG_ID>` with your catalog ID and `<ITEM_ID>` with an item (row) ID from the catalog. 

For example, let's say we want to reference the `tales_storefront` item:

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

For example, to reference the title and price of the `tales_storefront` item we could add the following:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}
 
Get {{ item.title }} for just {{ item.price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!

## Additional use cases

### Multiple items

You aren't limited to just one item in a single message! To reference multiple items from your catalog in one message, repeat the `catalogs` tag and replace the `<ITEM_ID>` with a different item from your catalog. Refer to the following as an example:

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

### Using images {#using-images}

You can also reference images in the catalog to use in your messaging. To do so, use the `catalogs` tag and `item` object in the Liquid field for images.

For example, to add the `image_link` from our Games catalog to our promotional message for Tales, we can add the following to our image field:

{% raw %}
```liquid
{% catalogs /catalogs/6171a881759044006998ed9a/items/tales_storefront %}

{{ item.image_link }}
```
{% endraw %}

![Push message composer with catalog Liquid tag used in the Push Icon Image field][3]

Here's what this looks like when the Liquid is rendered:

![Example iOS push notification with catalog Liquid tags rendered][4]{: style="max-width:50%" }

### Templating catalog items

You can also use templating to dynamically pull catalog items based on custom attributes. For example, let's say a user has the custom attribute `wishlist`, which contains an array of game IDs from your catalog.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["tales_storefront", "teslagrad_storefront"]
        }
    ]
}
```

Using Liquid templating, you can dynamically pull out the wishlist IDs and then use them in your message. To do so, [assign a variable][10] to your custom attribute, then use the `catalogs` tag to pull a specific item from the array.

{% alert tip %}
Remember, arrays start at `0`, not `1`.
{% endalert %}

For example, to let a user know that `tales_storefront` (an item in our catalog that they've wished for) is on sale, we can add the following to our message composer:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalogs /catalogs/6171a881759044006998ed9a/items/{{ wishlist[0] }} %}

Get {{item.title}} now, for just {{item.sale_price}}!
```
{% endraw %}

Which will display as the following:
> Get Tales now, for just 7.49 USD!

With templating, you can render a different catalog item for each user based on their individual custom attributes, event properties, or any other templatable field.

### Using filtered sets

You can use filtered sets to define a set of criteria, and Braze will return matching items from your catalog in a special array of objects named `items`. You can then iterate through those items to pull them out and reference their different properties. Filtered sets are great for look-alike or "light recommendation engine" type use cases.

For example, here is a clothing catalog with fields for availability, category, brand, price, name, and color:

![The table shows 15 example clothing items with columns for id, availability, category, brand, price, name, and color][6]

In your message composer, first [assign variables][10] to the criteria you want to filter, sort, and limit by in your catalog. This makes it easier for you to adjust your filters later on.

{% raw %}
```liquid
{% assign var_category = 'pants' %}
{% assign var_availability = 'in_stock' %}
{% assign var_sort = 'price' %}
{% assign var_limit = 2 %}
```
{% endraw %}

Then reference your catalog using the following syntax:

{% raw %}
```liquid
{% catalogs /catalogs/<CATALOG_ID>/items?<QUERY_PARAMETERS> %}
```
{% endraw %}

Add `filter` parameters in the format `field=value`, where each parameter is separated with an ampersand `&`.

Add a `sort` parameter in the format `sort[field]=direction`.

Add a `limit` parameter in the format `limit=value`.

For example, the following filters for items in the pants category that are in stock. The results are sorted by price with a maximum of two items displayed:

{% tabs local %}
{% tab Variables %}

{% raw %}
```liquid
{% catalogs /catalogs/61a52350d266a7006d5a529c/items?category={{var_category}}&availability={{var_availability}}&sort[{{var_sort}}]=asc&limit={{var_limit}} %}
```
{% endraw %}

{% endtab %}
{% tab Values %}
{% raw %}
```liquid
{% catalogs /catalogs/61a52350d266a7006d5a529c/items?category=pants&availability=in_stock&sort[price]=asc&limit=3 %} 
```
{% endraw %}
{% endtab %}
{% endtabs %}

Finally, add your message copy and reference items from the array. To do so, use the format `items[0].id` where `[0]` is the position of the item in the array and `id` is the column name in your catalog. The following is a simple printout of the clothing item's name, color, and price:

{% raw %}
```liquid
title: {{ items[0].name }}, color: {{ items[0].color }}, price: {{items[0].price}}
title: {{ items[1].name }}, color: {{ items[1].color }}, price: {{items[1].price}}
```
{% endraw %}

Alternatively, you can iterate through all the `items` using:

{% raw %}
```liquid
{% for item in items %}
  title: {{ item.name }}, color: {{ item.color }}, price: {{item.price}}
{% endfor %}
```
{% endraw %}

Either of the above displays as follows:

![Example iOS push notification with filtered catalog items rendered][7]{: style="max-width:50%" }

{% alert tip %}
If no items meet the filter criteria, `items` will be an empty array.
{% endalert %}

#### Limitations

The following limitations apply to using filtered sets in catalogs:

- Filter is for string equals only
- Filter is for `AND` operations only
- Sort is ascending (`asc`) or descending (`desc`), defaults to `asc`
- Default limit (number of items to return) is 10
- Max limit is 100


[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/catalog_id.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[6]: {% image_buster /assets/img_archive/catalog_filtered_csv.png %}
[7]: {% image_buster /assets/img_archive/catalog_filtered_example.png %}

[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
