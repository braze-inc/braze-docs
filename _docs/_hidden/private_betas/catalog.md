---
nav_title: Catalogs
permalink: "/catalogs/"
hidden: true
---

# Catalogs

You can use catalogs to reference non-user data in your Braze campaigns through Liquid. 

To do so, first import your catalog (a CSV file of non-user data) into Braze, and then access that information to enrich your messages. You can bring in any type of data into a catalog. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

Once this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

{% alert important %}
Catalogs are currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

If you'd like to share your feedback on this feature or make a request, you can [book a session](https://calendly.com/d/yzvf-frpy/catalog-beta-working-session?month=2021-10) with the Braze Data Ingestion team on Calendly!

## Creating a catalog

To create a catalog in Braze, upload a CSV file to the **Catalogs** page. Each CSV file you upload will be its own distinct catalog.

{% alert note %}
You can create up to five catalogs across your company.
{% endalert %}

### Step 1: Create your CSV

First, create your CSV file. The CSV file must have one column with a header of `id`, and each item's `id` must be unique. Additionally, the following limitations apply to catalog CSV files:

- Maximum of 5,000 items (rows)
- Maximum of 30 fields (columns)
- Maximum CSV file size of 100MB
- Maximum field value (cell) size of 0.5KB
- Only letters, numbers, hyphens, and underscores for `id` and header values

We also recommend that you format all text in your CSV files as lowercase.

{% alert note %}
Need more space to accomodate for your CSV files? Please contact your Braze Account Manager for more information about upgrading your catalogs.
{% endalert %}

For this tutorial, we're using a catalog that lists two games, their cost, and an image link.

![The table shows two example games with columns for id, title, price, and image_link.][5]

### Step 2: Upload your CSV

After you've created your CSV, navigate to the **Catalogs** page and upload the file. Drag and drop your file to the upload zone, or click **Upload CSV** and choose your file.

![][1]{: style="max-width:85%;"}

### Step 3: Select your data type

Select one of the following data types for each column:
- Boolean
- Number
- String
- Time

{% alert note %}
This data type cannot be edited after you set up your catalog.
{% endalert %}

![][9]{: style="max-width:85%;"}

### Step 4: Enter a catalog name

Enter a unique name for your catalog. This name can only contain numbers, letters, hyphens, and underscores. Optionally, you can also add a description for your catalog.

![][11]{: style="max-width:85%;"}

Lastly, click the **Create Catalog** button to finish creating your catalog!

Note that you won't be able to edit this name once the catalog is created. You can delete a catalog and reupload an updated version using the same catalog name. 

## Using catalogs in a message

You can use catalogs in all of your messaging channels, including anywhere in the Drag & Drop Editor where Liquid is supported.

### Step 1: Add personalization type {#step-one-personalization}

In the message composer of your choice, click the <i class="fas fa-plus-circle"></i> plus icon to open the **Add Personalization** modal and select **Catalogs Items** for the **Personalization Type**. Then, select your **Catalog Name**. Using our previous example, we'll select the Games catalog.

![][2]

We can immediately see the following Liquid preview:

{% raw %}
```liquid
{% catalogs_items Games %}
```
{% endraw %}

### Step 2: Select catalog items

Next, it's time to add your catalog items! Using the dropdown, select the catalog items and the information to display. This information corresponds to the columns in your uploaded CSV file used to generate your catalog.

For example, to reference the title and price of the `tales_storefront` item, we could select the `tales_storefront` as the catalog item and `title` and `price` for the displayed information.

{% raw %}
```liquid
{% catalogs_items Games tales_storefront %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!

## Additional use cases

### Multiple items

You aren't limited to just one item in a single message! Simply insert the additional catalog items and information to display using the **Add Personalization** modal. Refer to the following as an example:

{% raw %}
```liquid
{% catalogs_items Games tales_storefront %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
 
{% catalogs_items Games reformation_storefront %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!<br>
> Get Reformation for just 22.49 USD!

### Using images {#using-images}

You can also reference images in the catalog to use in your messaging. To do so, use the `catalogs` tag and `item` object in the Liquid field for images.

For example, to add the `image_link` from our Games catalog to our promotional message for Tales, select the `tales_storefront` for the **Catalog Items** field and `image_link` for the **Information to Display** field. This adds the following Liquid tags to our image field:

{% raw %}
```liquid
{% catalogs_items Games tales_storefront %}

{{ items[0].image_link }}
```
{% endraw %}

![Content Card composer with catalog Liquid tag used in the image field.][3]

Here's what this looks like when the Liquid is rendered:

![Example Content Card with catalog Liquid tags rendered.][4]{: style="max-width:50%" }

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

Using Liquid templating, you can dynamically pull out the wishlist IDs and then use them in your message. To do so, [assign a variable][10] to your custom attribute, then use the **Add Personalization** modal to pull a specific item from the array.

{% alert tip %}
Remember, arrays start at `0`, not `1`.
{% endalert %}

For example, to let a user know that `tales_storefront` (an item in our catalog that they've wished for) is on sale, we can add the following to our message composer:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalogs_items Games tales_storefront {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Which will display as the following:
> Get Tales now, for just 7.49 USD!

With templating, you can render a different catalog item for each user based on their individual custom attributes, event properties, or any other templatable field.

## Limitations

Refer to the following table for limitations that apply at a company level:

| Limitation Area | Free version | Catalogs Pro |
|---|---|---|
| Number of catalogs | Up to 5 catalogs | Up to 10 catalogs |
| Number of all catalogs items | Up to 5,000 items | Up to 100,000 items |
| Catalog storage | Up to 100MB of catalog data | Up to 2GB of catalog data |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

The following table describes the limitations that apply at a catalog level:

| Limitation Area | Free version | Catalogs Pro |
|---|---|---|
| CSV file size | Up to 100MB for a single CSV file | Up to 2GB for a single CSV file |
| Number of items | Up to 5,000 items in a single catalog | Up to 100,000 items in a single catalog |
| Number of fields | Up to 30 fields (columns) | Up to 30 fields (columns) |
| Characters limit for item value | Up to 5,000 characters in one value. For example, if you had a field labeled `description`, the maximum number of characters within the field is 5,000. | Up to 5,000 characters in one value. For example, if you had a field labeled `description`, the maximum number of characters within the field is 5,000. |
| Characters limit for item column name | Up to 250 characters | Up to 250 characters |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Interested in upgrading your experience to Catalog Pro? Contact the <a href="mailto:catalogs-product@braze.com">Catalogs team</a> for more informaton.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
