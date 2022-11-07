---
nav_title: Creating a Catalog
article_title: Creating a Catalog
alias: "/catalogs/"
page_order: 1
description: "This reference article covers how to create and use catalogs to reference non-user data in your Braze campaigns through Liquid."
---

# Creating a catalog

You can use catalogs to reference non-user data in your Braze campaigns through [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). 

To do so, first import your catalog (a CSV file of non-user data) into Braze, and then access that information to enrich your messages. You can bring in any type of data into a catalog. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

Once this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

{% alert note %}
You can create up to five catalogs across your company.
{% endalert %}

To create a catalog in Braze, upload a CSV file to the **Catalogs** page. Each CSV file you upload will be its own distinct catalog. You can also download and reference [this sample CSV file]({{site.baseurl}}/assets/download_file/sample_sunglasses_catalog.csv) to follow along the steps for creating a catalog.

## Step 1: Create your CSV

First, create your CSV file. The first column of the CSV file must be a header of `id`, and each item's `id` must be unique. All other column names must be unique. Additionally, the following limitations apply to catalog CSV files:

- Maximum of 5,000 items (rows)
- Maximum of 30 fields (columns)
- Maximum field (column) name of 250 characters
- Maximum CSV file size of 100MB
- Maximum field value (cell) of 5,000 characters
- Maximum field value (cell) size of 0.5KB
- Only letters, numbers, hyphens, and underscores for `id` and header values

Ensure that you are encoding your CSV file using the UTF-8 format in order to successfully upload your CSV file in the next step. We also recommend that you format all text in your CSV files as lowercase.

{% alert note %}
Need more space to accommodate for your CSV files? Contact your Braze account manager for more information about upgrading your catalogs.
{% endalert %}

### Example catalog

For this tutorial, we're using a catalog that lists two games, their cost, and an image link.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49 USD</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49 USD</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

## Step 2: Upload your CSV

After you've created your CSV, navigate to the **Catalogs** page and upload the file. Drag and drop your file to the upload zone, or click **Upload CSV** and choose your file.

{% alert important %}
Your CSV file can be rejected if you go above [company limitations](#limits). 
{% endalert %}

![][1]{: style="max-width:85%;"}

Give your catalog a name. Keep in mind the following limitations for your catalog name:
- Must be unique
- Maximum of 250 characters
- Can only include numbers, letters, hyphens, and underscores

Note that you cannot use templates in a catalog name. For example, you cannot have the following as the catalog name or else the call will fail.
{% raw %}
```liquid
{% catalog_items custom_attribute.${catalog} item1, item2 %}
```
{% endraw %}

## Step 3: Select your data type

Select one of the following data types for each column:
- Boolean
- Number
- String
- Time

{% alert note %}
This data type cannot be edited after you set up your catalog.
{% endalert %}

![][9]{: style="max-width:85%;"}

## Step 4: Enter a catalog name

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
{% catalog_items Games %}
```
{% endraw %}

### Step 2: Select catalog items

Next, it's time to add your catalog items! Using the dropdown, select the catalog items and the information to display. This information corresponds to the columns in your uploaded CSV file used to generate your catalog.

For example, to reference the title and price of our Tales game, we could select the `id` for Tales (1234) as the catalog item and request `title` and `price` for the displayed information.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49 USD!

## Catalogs via API

You can leverage the [Catalogs Endpoints]({{site.baseurl}}/api/endpoints/catalogs/) to manage the growing data and information.

### Managing catalogs

You can create a catalog using the [Create Catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) endpoint.

As you build more catalogs, you can also use the [List Catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) endpoint to return a list of the catalogs in an app group.

### Managing catalog items

In addition to managing your catalogs, you can also use asynchronous and synchronous endpoints to manage the catalog items. This includes the ability to edit and delete catalog items, and to list catalog item details. 

For example, if you want to edit an individual catalog item, you can use the [`/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/) endpoint.

## Additional use cases

### Multiple items

You aren't limited to just one item in a single message! Simply insert the additional catalog items and information to display using the **Add Personalization** modal. Note that you can add up to three catalog items only. 

Check out this example where we add the `id` of three games, Tales, Teslagrad, and Acaratus, for **Catalog Items** and select `title` for **Information to Display**.

![][6]{: style="max-width:70%" }

We can further personalize our message by adding some text around our Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

This returns as the following:

> Get the ultimate trio Tales, Teslagrad, and Acaratus today!

{% alert tip %}
Check out [filtered sets]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/filtered_sets/) to create groups of data for more personalized messaging!
{% endalert %}

### Using images {#using-images}

You can also reference images in the catalog to use in your messaging. To do so, use the `catalogs` tag and `item` object in the Liquid field for images.

For example, to add the `image_link` from our Games catalog to our promotional message for Tales, select the `id` for the **Catalog Items** field and `image_link` for the **Information to Display** field. This adds the following Liquid tags to our image field:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

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
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

Using Liquid templating, you can dynamically pull out the wishlist IDs and then use them in your message. To do so, [assign a variable][10] to your custom attribute, then use the **Add Personalization** modal to pull a specific item from the array.

{% alert tip %}
Remember, arrays start at `0`, not `1`.
{% endalert %}

For example, to let a user know that Tales (an item in our catalog that they've wished for) is on sale, we can add the following to our message composer:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Which will display as the following:
> Get Tales now, for just 7.49 USD!

With templating, you can render a different catalog item for each user based on their individual custom attributes, event properties, or any other templatable field.

### Uploading a CSV

You can upload a CSV of new catalog items to add, or catalog items to update. To delete a list of items, you can upload a CSV of item IDs to delete them.

### Using Liquid

You can also manually piece together catalogs Liquid logic. However, note that if you type in an ID that doesn't exist, Braze will still return an items array without objects. We recommend that you include error handling, such as checking the size of the array and using an `if` statement to account for an empty array case.

## Managing catalogs

As you create more catalogs, you can leverage the [Catalogs Endpoints]({{site.baseurl}}/api/endpoints/catalogs/) to manage the growing data and information. This includes the ability to create, edit, and delete catalog items, and to list catalog item details.

## Limitations {#limits}

Refer to the following table for limitations that apply at a company level:

| Limitation Area | Free version | Catalogs Pro |
|---|---|---|
| Number of catalogs | Up to 5 catalogs | Up to 10 catalogs |
| Number of all catalogs items | Up to 5,000 items | Up to 100,000 items |
| Catalog storage | Up to 100MB of catalog data | Up to 2GB of catalog data |
| Filtered sets | Up to 1 filtered set per catalog | Up to 10 filtered sets per catalog |
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

Interested in upgrading your experience to Catalog Pro? Contact your account manager to get started.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[6]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
