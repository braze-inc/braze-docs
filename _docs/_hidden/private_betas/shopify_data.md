---
nav_title: Shopify Data in Braze
article_title: "Shopify Data in Braze"
description: "This article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner
hidden: true

---

# Shopify data in Braze

## Shopify webhooks

Braze offers a turnkey solution to support abandoned checkout, purchase, and post-purchase lifecycle campaigns through [Shopify Webhooks](https://shopify.dev/api/admin-rest/2022-04/resources/webhook#top). Depending on which events you select during your onboarding process, Braze determines which Shopify event topics to subscribe to. As soon as you have successfully onboarded your Shopify store, Braze will instantly receive your Shopify customer activity.

For more information on which Shopify event data is supported, see the section below.

### Supported Shopify events

| Event name | Braze event type | Triggered when... |
| --- | --- | --- |
| `shopify_product_viewed` | Custom Event| Product views will trigger when products are fully visible on the Shopify store to the customer. |
| `shopify_product_clicked` | Custom Event | Product clicks will trigger as soon as the customer clicks on the product information page. |
| `shopify_abandoned_cart` | Custom Event | As soon as a customer adds items to their cart, Braze will store the cart token ID. <br><br>The default Abandoned Cart Delay is set at 1 hour. Meaning, that after 1 hour of cart abandonment where no updates have been made to the cart, Braze will then trigger the event. You can update your Abandoned Cart Delay within Advanced Settings. |
| `shopify_abandoned_checkout` | Custom Event | Checkout updates the webhook's trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process, including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned. The Abandoned Checkout Delay is set to 1 hour but is configurable within the Advanced Settings section on the Shopify partner page.
| `shopify_created_order` | Custom Event| Order create events trigger:<br><br>Automatically after a customer has completed a purchase from your Shopify store.<br>OR<br>Manually through the orders section of your Shopify account.|
| Purchase | Braze Purchase Event | Shopify's order create event immediately triggers a Braze purchase event. |
| `shopify_paid_order` | Custom Event | Order paid events will trigger when an order's payment status is changed to paid. An order is in paid status after a credit card payment has been captured or when an order using a manual payment method is marked as paid. |
| `shopify_partially_fulfilled_order` | Custom Event | Partially fulfilled order events will trigger when some of the line items in an order are fulfilled successfully. |
| `shopify_fulfilled_order` | Custom Event | Fulfilled order events will trigger when the fulfillment of all of the line items in a fulfillment order is successful. |
| `shopify_cancelled_order` | Custom Event | Canceled order events will trigger when a customer creates an order but then cancels the order before fulfillment. |
| `shopify_created_refund` | Custom Event | Created refunds events are triggered when a customer is provided a refund for their order, whether a partial refund or a complete refund.<br><br> A refund can also be triggered when a Shopify account admin manually processes the refund in Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Event payloads

### Supported Shopify custom attributes
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Attribute Name | Description |
| --- | --- |
| `shopify_accepts_marketing` | This custom attribute corresponds to the email marketing opt-in status that is captured on the checkout page. |
| `shopify_sms_consent` | This custom attribute corresponds to the SMS marketing opt-in status that is captured on the checkout page. |
| `shopify_tags`  | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify SMS Consent %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_sms_consent": {
        "state": "subscribed",
        "opt_in_level": "single_opt_in",
        "collected_from": "other"
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Accepts Marketing (Email) %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_accepts_marketing": true
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


#### Supported Shopify standard attributes

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and the customer will not be charged a data point.
{% endalert %}

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

With Nested Object Support for Custom Event Properties, customers can now trigger campaigns and Canvases using a nested event property. The following is an example of triggering a campaign using a specific product from the `shopify_created_order` custom event.

![Action-based campaign that sends to users who perform the custom event "shopify_created_order" where the nested property "product_id" equals a specific number.][26]

[22]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
[13]: {% image_buster /assets/img/Shopify/abandoned_cart_delay.png %} 
