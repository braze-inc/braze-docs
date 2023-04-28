---
nav_title: Shopify Data in Braze
article_title: "Using Shopify Data in Braze"
description: "This reference article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner
alias: "/shopify_data/"
page_order: 4
---

# Shopify data in Braze

## Personalization

Using nested object support for custom events, Braze Shopify customers can use Liquid template variables of the nested event properties. The following tables list the Liquid templating variables for each event.

{% tabs %}
{% tab Product Viewed %}
**Event**: `shopify_product_viewed`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |

{% endraw %}
{% endtab %}

{% tab Product Clicked %}
**Event**: `shopify_product_clicked`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Cart %}
**Event**: `shopify_abandoned_cart`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Checkout %}
**Event**: `shopify_abandoned_checkout`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Checkout ID | `{{event_properties.${checkout_id}}}` |
| Abandoned Card URL | `{{event_properties.${abandoned_checkout_url}}}` |
| Discount Code | `{{event_properties.${discount_code}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Discount Amount | `{{event_properties.${applied_discount}[0].amount}}` |
| Discount Title | `{{event_properties.${applied_discount}[0].title}}` |
| Discount Description | `{{event_properties.${applied_discount}[0].description}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Created Order %}

**Event**: `shopify_created_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Purchase %}

**Event**: Purchase<br>
**Type**: [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title  | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% tab Order Paid %}
**Event**: `shopify_paid_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Partially Fulfilled Order %}
**Event**: `shopify_partially_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Fulfilled Order %}
**Event**: `shopify_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Cancelled Order %}
**Event**: `shopify_cancelled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}


{% tab Created Refund %}
**Event**: `shopify_created_refund`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}
{% endtabs %}

## Segmentation

You can filter Shopify's events with all of the [existing custom filters]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) in Segmentation. 

![Segment Details page for a Shopify_Test segment with the filter for the custom event "shopify_checkouts_abandon" highlighted.][12]{: style="max-width:80%;"}

In addition, you can also use Braze's breadth of purchase filter to create segments of users based on:
- First/last purchase
- First/last purchase for a specific app
- Products they have previously purchased within the last 30 days
- The number of purchases they made

![Segmentation filter for users that first made a purchase after October 17, 2020.][13]

![Searching for a specific product ID as a segmentation filter.][14]

{% alert note %}
If you are looking to segment by custom event properties, ensure that you work with your customer success manager or Braze [support]({{site.baseurl}}/braze_support/) to enable filtering for all relevant event properties that you'd like to use within segmentation and Liquid.
{% endalert %} 

## Campaign and Canvas triggering 

With Shopify custom events in Braze, you can trigger Canvases or campaigns like you normally would with any other [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). For example, you may create an Action-Based Canvas that triggers off of the Shopify `shopify_checkouts_abandon` event within the Canvas entry criteria. 

![Action-based Canvas that enters users who perform the custom event "shopify_checkouts_abandon".][5]

With Nested Object Support for Custom Event Properties, customers can now trigger campaigns and Canvases using a nested event property. The following is an example of triggering a campaign using a specific product from the `shopify_created_order` custom event. Make sure to use `list_items[].product_id` to index your item list and access the product ID.

![Action-based campaign that sends to users who perform the custom event "shopify_created_order" where the nested property "product_id" equals a specific number.][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
