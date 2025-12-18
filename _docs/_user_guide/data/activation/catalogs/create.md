---
nav_title: Creating a catalog
article_title: Creating a Catalog
alias: "/catalogs/"
page_order: 1
description: "This reference article covers how to create catalogs that reference non-user data in your Braze campaigns through Liquid."
---

# Creating a catalog

> Creating a catalog involves importing a CSV file of non-user data into Braze. This allows you to then access that information to enrich your messages. You can bring in any type of data into a catalog. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

## Use cases

Commons use cases for catalogs include:

- Products
- Services
- Food
- Upcoming events
- Music
- Packages

After this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

## Creating a catalog

To create a catalog, go to **Data Settings** > **Catalogs**, then select **Create New Catalog** and choose one of the following options:

{% tabs local %}
{% tab Upload CSV %}
### Step 1: Review your CSV file

Before you upload your CSV file, ensure that your CSV file meets the following requirements:

| CSV Requirement | Details |
|-----------------|---------|
| Headers | The first column in the CSV file must be named `id`, and each row must have a unique `id` value. |
| Columns | A CSV file can have a maximum of 1,000 fields (columns), and each column name can be up to 250 characters long. |
| File size | For Free plans, the total size of all CSV files across a company is limited to 100 MB. For Pro plans, the maximum file size for a single CSV file is 2 GB. |
| Field values | Each cell (field value) can contain up to 5,000 characters. |
| Valid characters | The `id` column and all header values can only contain letters, numbers, hyphens, and underscores. |
| Data types | Supported data types for uploading a CSV file include string, integer, float, boolean, or datetime. |
| Formatting | Format all text in lowercase to maintain consistency. |
| Encoding | Save and upload the CSV file using UTF-8 encoding. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Need more space to accommodate for your CSV files? Contact your Braze account manager for more information about upgrading your catalogs.
{% endalert %}

### Step 2: Upload CSV

Drag and drop your file to the upload zone, or select **Upload CSV** and choose your file.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Select a data type for each column.

{% alert note %}
This data type cannot be edited after you set up your catalog. In addition, a `NULL` value isn't supported in CSV upload and will be treated as a string.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Enter a name and optional description for your catalog. Keep the following requirements in mind when naming your catalog:

  - Must be unique
  - Maximum of 250 characters
  - Can only include numbers, letters, hyphens, and underscores

{% alert tip %}
You can also [use templates in a catalog name](#template-catalog-names), letting you dynamically generate catalog names based on variables like language or campaign.
{% endalert %}

![A catalog named "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Select **Process Catalog** to create the catalog.

{% alert important %}
Your CSV file can be rejected if you go above your [tier](#tiers). 
{% endalert %}

### Tutorial: Creating a catalog from a CSV file

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
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

We'll create the catalog by uploading a CSV file. The data types for `id`, `title`, `price`, and `image_link` are string, string, number, and string, respectively. 

{% alert note %}
This data type cannot be edited after you set up your catalog.
{% endalert %}

![Four catalog column names: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Next, we'll name this catalog "games_catalog" and select the **Process Catalog** button. Then, Braze will check the catalog for any errors before catalog creation.

![A catalog named "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Note that you won't be able to edit this name after the catalog is created. You can delete a catalog and re-upload an updated version using the same catalog name.

After creating the catalog, you can begin referencing the [catalog in a campaign]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Prerequisites

Before you can edit or create catalogs in the browser, you need the following [user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) for your workspace:

- View Catalogs
- Edit Catalogs
- Export Catalogs
- Delete Catalogs

{% multi_lang_include deprecations/user_permissions.md %}

### Step 1: Enter catalog details

Enter a name and optional description for your catalog. Keep the following requirements in mind when naming your catalog:

- Must be unique
- Maximum of 250 characters
- Can only include numbers, letters, hyphens, and underscores

{% alert tip %}
You can also [use templates in a catalog name](#template-catalog-names), letting you dynamically generate catalog names based on variables like language or campaign.
{% endalert %}

![A catalog named "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Step 2: Create your catalog

Select your catalog from the list, then select **Update Catalog** > **Add fields**. Enter the **Field name** and use the dropdown to select the data type. Repeat as needed.

![Two example fields "rating" and "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Select **Update Catalog** > **Add items** to add an item to your catalog by entering the information based on the fields you previously added. Then, select **Save Item** or **Save and Add Another** to continue adding your items.

![Add a catalog item.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze processes time values based on the dashboard timestamp. For example, if a column has a value of "03/13/2024" and your time zone is the Pacific Time Zone, this time would be imported to Braze as "Mar 12, 2024, 5:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Using templates in catalog names {#template-catalog-names}

When naming your catalog, you can also use templates in a catalog name. This lets you dynamically generate catalog names based on variables like language or campaign. For example, you can use the following:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Managing catalogs

### In the dashboard

To update your catalog after uploading a CSV or creating a catalog in the browser, select **Update Catalog > Upload CSV**, then select whether to update, add, or delete items in your catalog.

### Using the REST API

As you build more catalogs, you can also use the [List catalogs endpoint]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) to return a list of the catalogs in a workspace.

Supported data types for using API include: string, integer, float, boolean, or datetime. You can also upload arrays and objects when managing your catalogs with the API.

## Managing catalog items

In addition to managing your catalogs, you can also use asynchronous and synchronous endpoints to manage the catalog items. This includes the ability to edit and delete catalog items, and to list catalog item details. 

For example, if you want to edit an individual catalog item, you can use the [`/catalogs/catalog_name/items/item_id` endpoint]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Catalog storage {#tiers}

The free version of catalogs supports CSV file sizes of up to 100 MB for all CSV files combined across your company, whereas the Catalogs Pro version supports CSV file sizes of up to 2 GB for a single CSV file.

{% alert important %}
The package entitlement shown in the Braze dashboard is rounded to the nearest unit for visual purposes; however, you are still entitled to the full entitlement purchased. To request an upgrade for catalog storage, contact your Braze account manager.
{% endalert %}

#### Free version

The storage size for the free version of catalogs is up to 100&nbsp;MB. You can have unlimited items as long as they're under 100&nbsp;MB. 

#### Catalogs Pro

At a company level, the maximum storage for Catalogs Pro is based on the size of catalog data. The storage size options are: 5&nbsp;GB, 10&nbsp;GB, or 15&nbsp;GB. Note that the free version's storage (100&nbsp;MB) is included in each of these plans.
