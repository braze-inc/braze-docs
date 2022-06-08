---
nav_title: Shopify Use Case in Braze
article_title: "Shopify Use Cases in Braze"
description: "This article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner
permalink: "/use_case/"

---

# Shopify use cases

## Beginner

These are some simple yet effective use cases that you can create shortly after setting up Shopify. No additional work is required. 

### Campaigns

These are transactional use case that allow you to alert your users when there's an update to their Shopify order.

{% tabs local %}
{% tab Refund %}
**Shopify Refund Event** - `shopify_created_refund`

Users were provided a refund, either partial, or complete. This campaign lets the user know that their order was successfully refunded.

![Action-based campaign that enters users who perform the custom event "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Shopify Cancellation Event** - `shopify_cancelled_order`

Users were able to cancel their order before fulfillment. This campaign lets the user know that their purchase was successfully cancelled.

![Action-based campaign that enters users who perform the custom event "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Shopify Fulfilled Event** - `shopify_fulfilled_order`

All line items in a user’s order were fulfilled successfully. This campaign lets the user know that their entire order was fulfilled.

![Action-based campaign that enters users who perform the custom event "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Shopify Partially Fulfilled Event** - `shopify_partially_fulfilled_order`

Some line items in a user’s order were fulfilled successfully. This campaign lets the user know that part of their entire order was fulfilled.

![Action-based campaign that enters users who perform the custom event "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Shopify Paid Order Event** - `shopify_paid_order`

User pays for their order and the order status changes to paid. This campaign lets the user know that their credit card payment was captured or the order was marked as paid if there was a manual payment.

![Action-based campaign that enters users who perform the custom event "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**Abandoned Checkout Canvas**

Users are abandoning the checkout flow and failing to complete transactions before they depart. The Canvas allows you to send automated reminders to users who have not finished their transactions to bring them back into the checkout flow.

Action-based entry event: `shopify_abandoned_checkout`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**Post-Purchase Canvas**

Users made a successful purchase and now you want to know how they liked their purchase. This Canvas allows you to send follow up messages to your user to collect feedback. 

Action-based entry event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Advanced use cases

Once you've gotten more familiar with the platform, you can set up some of these more complex use cases.

### Campaigns
Requires Connected Content

{% tabs local %}
{% tab User recommendation %}
**User Recommendations**

User clicked / viewed an item but didn’t purchase it. This Campaign sends a follow up message to the user with the same or similar items (recommended by Connected Content) to prompt the user to purchase one of them.

Action-based entry event: `shopify_product_clicked` or `shopify_product_viewed`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:60%;"}

![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:80%;border:0;"}

![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Refund winback Canvas %}

**Refund Winback Canvas**

Users were provided a refund, either partial or complete. This Canvas sends follow up messages to get the user to make their purchase again.

Action-based entry event: `shopify_created_refund`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**Winback Cancellation Canvas**

Users were able to cancel their order before fulfillment. This Canvas sends follow up messages to get the user to make their purchase again.

Action-based entry event: `shopify_cancelled_order`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}




