---
nav_title: Shopify Data in Braze
article_title: "Using Shopify Data in Braze"
description: "This article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner

---

# Shopify data in Braze


## Segmentation

You can filter Shopify's events with all of the [existing custom filters]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) in Segmentation. 

![Segment Details page for a Shopify_Test segment with the filter for the custom event "shopify_checkouts_abandon" highlighted.][22]{: style="max-width:80%;"}

In addition, you can also use Braze's breadth of purchase filter to create segments of users based on:
- First/last purchase
- First/last purchase for a specific app
- Products they have previously purchased within the last 30 days
- The number of purchases they made

![Segmentation filter for users that first made a purchase after October 17, 2020.][23]

![Searching for a specific product ID as a segmentation filter.][24]

{% alert note %}
If you are looking to segment by custom event properties, ensure that you work with your customer success manager or Braze [support]({{site.baseurl}}/braze_support/) to enable filtering for all relevant event properties that you'd like to use within segmentation and Liquid.
{% endalert %} 

## Campaign and Canvas triggering 

With Shopify custom events in Braze, you can trigger Canvases or campaigns like you normally would with any other [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). For example, you may create an Action-Based Canvas that triggers off of the Shopify `shopify_checkouts_abandon` event within the Canvas entry criteria. 

![Action-based Canvas that enters users who perform the custom event "shopify_checkouts_abandon".][22]

With Nested Object Support for Custom Event Properties, customers now can trigger campaigns and Canvases using a nested event property. The following is an example of triggering a campaign using a specific product from the `shopify_created_order` custom event.

![Action-based campaign that sends to users who perform the custom event "shopify_created_order" where the nested property "product_id" equals a specific number.][26]

[22]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
[13]: {% image_buster /assets/img/Shopify/abandoned_cart_delay.png %} 
