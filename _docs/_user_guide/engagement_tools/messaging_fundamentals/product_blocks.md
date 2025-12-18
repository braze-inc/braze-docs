---
nav_title: Product blocks
article_title: Drag-and-Drop Product Blocks
page_order: 7.5
description: "This reference article covers drag-and-drop product blocks, which allow users to quickly add and configure dynamic or static showcases of catalog items."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Drag-and-drop product blocks 

> The drag-and-drop editor empowers you to quickly add and configure product blocks to your messages for seamless product showcases, without the need to create custom Liquid code. 

{% alert important %}
The drag-and-drop product block feature is in early access and is currently only available for email. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Requirements 

| Requirement | Description |
| --- | --- |
| eCommerce recommended events | [eCommerce recommended events]({{site.baseurl}}/ecommerce_events/) provide standardized data schemas for key behavioral events that occur before and after an order is placed. These events will eventually replace the legacy Braze purchase event and will become the standard for tracking commerce-related behavior. <br><br> eCommerce recommended events are required for dynamic product blocks.<br><br> eCommerce recommended events are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. |
| eCommerce Canvas templates | The eCommerce recommended events support pre-built templates, including eCommerce Canvas templates designed for essential use cases such as abandoned browsing, abandoned carts, and order confirmations. <br><br>If you plan to implement any of these essential eCommerce use cases using the [eCommerce Canvas templates]({{site.baseurl}}/ecommerce_use_cases/), you must use or follow the provided Canvas template. |
| Braze catalog | You must create a Braze catalog that includes the following fields, which you use in your product block configuration:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Catalog selection | For static product blocks, you must create a [catalog selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to specify which products to include in your product block. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Types of drag-and-drop product blocks

| Product block | Purpose | Use cases | Availability |
| --- | --- | --- | --- |
| Dynamic | Personalize your messaging with a showcase of products based on customer interactions by using [eCommerce recommended events]({{site.baseurl}}/ecommerce_events/) and catalogs within our [eCommerce Canvas templates]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Abandoned browse</li><li>Abandoned cart</li><li>Abandoned checkout</li><li>Order confirmations</li></ul>{:/} | Available in Canvas only. |
| Static | Personalize products using data stored in a Braze catalog. You must use a [catalog selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to specify which products to include. | Perfect for showcasing new product launches or category-specific offerings.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Product block content configuration

Each block type has different content configurations. 

### Product fields

In the **Product Fields** section, select your product block type, then toggle on the fields you’d like to include for each product. Each field is pulled from different sources based on the type of product block you select.

#### Dynamic product block

| Product field | Source |
| --- | --- | 
| Variant image | Catalogs | 
| Product title | Catalogs | 
| Button for product URL | Catalogs |
| Price | eCommerce Recommended event property|
| Quantity | eCommerce Recommended event property| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Product fields for a dynamic product block, which are divided into catalog data and event data]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Static product block

| Product field | Source |
| --- | --- | --- |
| Variant image | Catalogs |
| Product title | Catalogs |
| Button for product URL | Catalogs |
| Price | Catalogs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![Product fields for a static product block, which are all categorized as catalog data.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Layout options

Use layout options to customize how your products display within your product block.

| Option | Description |
| --- | --- |
| Product orientation | Choose how the image and product fields within the block are oriented. |
| Alignment | Adjust the alignment of the text fields and button within the block. |
| Max products per row | Display up to three products per row, up to 12 products total for static product blocks, and up to 24 products total for dynamic product blocks. |
| Product spacing | Set the spacing between products. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Layout options for product orientation, alignment, max products per row, and product spacing.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Global email style settings 

[Global email style settings]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) allow you to apply consistent styling to your emails within Braze. This means you can define specific styles—such as fonts, colors, and button designs—that will automatically apply to all your emails.

#### How global email style settings work with product blocks

Existing styles for paragraphs and buttons automatically apply to the text and button elements within the product block. This means that your product block consistently uses any formatting you have set for paragraphs and buttons, maintaining a cohesive look throughout your email.

## Setting up product blocks

### Catalog setup 

{% alert important %}
If you’re using the Braze and Shopify integration for [product syncing]({{site.baseurl}}/shopify_catalogs/), you don’t need to take any additional steps to use drag-and-drop product blocks.<br><br> If you don’t have product variant information, you need to duplicate their top-level product information in both the product and the product variant fields within the event payloads and catalogs. This means you need to provide the same product details for both identifiers to maintain consistency for the product block to work properly.
{% endalert %}

To use drag-and-drop product blocks, you need to set up a Braze catalog that includes specific field values. You use these fields in your product block configuration. Make sure your catalog includes the following fields:

| Field | Description |
| --- | --- |
|`product_title` | The title of the product.|
|`product_url` | The URL where customers can view or purchase the product. |
|`variant_image_url` | The URL for the variant image. |

Get a jumpstart by working off this [sample Product Catalog]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), which includes the required fields. 

![A sample CSV file with the required fields in addition to others.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mapping to catalog fields

In the **Settings** tab of your catalog, you can select the **Product blocks** toggle to map to specific fields and information in your catalog. This allows you to select which fields to use as the product title, product URL, and image URL. Note that Shopify catalog fields are mapped by default and can't be changed.

{% alert note %}
If you aren't using Shopify, you can contact your account manager to turn on field mapping, which allows you to connect any catalog to product blocks and map its fields to the `product_title`, `product_url`, and `variant_image_url`.
{% endalert %}

## Creating product blocks

This guide will walk you through the steps to create, test, and ensure the functionality of a dynamic or static product block using our email drag-and-drop editor.

### Step 1: Create an email campaign or email Canvas step

#### Dynamic product block

{% alert note %}
Dynamic product blocks require [eCommerce recommended events]({{site.baseurl}}/ecommerce_events/) and can only be used within [Canvases]({{site.baseurl}}/ecommerce_use_cases). For Braze Shopify users, these events are automatically included as part of the integration. For non-Shopify users, you need to work with your developers to pass these events into Braze and ensure that the primary product identifier within the events is added as the catalog item ID. 
{% endalert %}

Create a new Canvas that uses one of the available Braze templates for your specific use case:
- Abandoned Browse
- Abandoned Cart
- Abandoned Checkout
- Order Confirmations

For detailed instructions on creating your eCommerce Canvases, refer to [eCommerce use cases]({{site.baseurl}}/ecommerce_use_cases/).

#### Static product block

Create a drag-and-drop email campaign, action-based Canvas, or template that has a drag-and-drop email Message step.

### Step 2: Add a product block

{% tabs %}
{% tab Dynamic product block %}

Within the message step, create an email or modify the existing template using the drag-and-drop email composer.
Drag a product block into your email message.
Confirm the dynamic block type is selected.
Select the product catalog you want to use for personalization. Make sure it aligns with the products from the inbound events you are targeting.

{% endtab %}
{% tab Static product block %}

Drag a product block into your email message and select the static block type. 
Select the catalog you want to use for your product block. You must select a catalog selection to specify which products display in your product block.

{% endtab %}
{% endtabs %}

![The "Content" tab containing editor blocks, such as product blocks.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Step 3: Configure product fields

Select which [product fields](#product-fields) should be shown in the product block. Select **Apply Settings** after each change to see updates in the editor. 

You can also customize the text before your Liquid tags. For example, you can prepend a dollar sign ($) for an item's price or update the term for quantity to "amount" or another preferred label.

![Product block with a dollar side prepended to the item's price.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Step 4: Configure layout settings

Change the [layout options](#layout-options) to update how products display within your product block, and make sure to select **Apply settings** after each change.

### Step 5: Preview and test your message

{% tabs %}
{% tab Dynamic product block %}

1. In the **Preview & Test** section, preview the message as a custom user.
2. Specify how many items you want to render in the preview.
3. Confirm that the correct number of items appears and that your layout options are applied correctly. Note that the items that appear are randomly selected.

!["Preview as a User" tab with a dropdown section "Dynamic product block" that specifies to show 4 items.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

A preview will generate within the drag-and-drop composer when you apply changes to your product block. 

![Email drag-and-drop composer showing a generate product block with different item tiles.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

After you're done creating your message and confirming it looks like expected, you're ready to send!