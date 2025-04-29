---
nav_title: Use Cases
article_title: "Shopify Use Cases in Braze"
description: "This reference article outlines common beginner and advanced Shopify use cases."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# Use cases

> Interested in seeing how you can leverage your Shopify integration to create timely and effective messaging for your users? Refer to the following sections on common [beginner](#beginner) and [advanced](#advanced) use cases to learn more!

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Beginner

These are some simple yet effective use cases that you can create shortly after setting up Shopify. No additional work is required. 

### Campaigns

These transactional use cases allow you to alert your users when there's an update to their Shopify order.

{% tabs local %}
{% tab Refund %}
**Shopify refund event** - `shopify_created_refund`

Users were provided a refund, either partial or complete. This campaign lets the user know that their order was successfully refunded.

![Action-based campaign that enters users who perform the custom event "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Messaging example**

![Email with the text "Your order has been refunded, Sorry that you were disappointed with your order. We've successfully sent your refund. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Shopify cancellation event** - `shopify_cancelled_order`

Users were able to cancel their orders before fulfillment. This campaign lets the user know that their purchase was successfully canceled. 

![Action-based campaign that enters users who perform the custom event "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Messaging example**

![Email with the text "Your order has been canceled, Sorry to see you go! We've successfully canceled your order. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Shopify fulfilled event** - `shopify_fulfilled_order`

All line items in a user's order were fulfilled successfully. This campaign lets the user know that their entire order was fulfilled.

![Action-based campaign that enters users who perform the custom event "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Messaging example**

![Text message with the text "Your order's been fulfilled! All items in your cart have been delivered! Please go into your account and confirm receipt. Bonus points for leaving feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Shopify partially fulfilled event** - `shopify_partially_fulfilled_order`

Some line items in a user's order were fulfilled successfully. This campaign lets users know that part of their entire order was fulfilled.

![Action-based campaign that enters users who perform the custom event "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Messaging example**

![Text message with the text "Your order's been partially fulfilled! We've delivered some of the items in your order and the rest are on the way! We'll send you another alert when the delivery's been fully complete."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Shopify paid order event** - `shopify_paid_order`

User pays for their order, and the order status changes to paid. This campaign lets the user know that their credit card payment was captured or the order was marked as paid if there was a manual payment.

![Action-based campaign that enters users who perform the custom event "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Messaging example**

![Email with the text "We've received your Payment! Woohoo your order's been paid for! Please wait 1-2 business days for us to process the payment and prep your items. Then we'll ship it out!" and a "View Account" button.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**Abandoned checkout Canvas**

Users are abandoning the checkout flow and failing to complete transactions before departing. This Canvas allows you to send automated reminders to users who have not finished their transactions to bring them back into the checkout flow.

Action-based entry event: `shopify_abandoned_checkout`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**Post-purchase Canvas**

Users made a successful purchase, and now you want to know how they liked their purchase. This Canvas allows you to send follow-up messages to your user to collect feedback. 

Action-based entry event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Advanced

Once you've become more familiar with the platform, you can set up some more complex use cases.

### Campaigns

{% tabs local %}
{% tab User recommendations %}
**User recommendations**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

User clicked or viewed an item but didn't purchase it. This campaign sends a follow-up message to the user with the same or similar items (recommended by Connected Content) to prompt the user to purchase one of them.

Action-based entry event: `shopify_product_clicked` or `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Exception event: `shopify_created_order` or Purchase<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Refund winback Canvas %}

**Refund winback Canvas**

Users were provided a refund, either partial or complete. This Canvas sends follow-up messages to get the user to make their purchase again.

Action-based entry event: `shopify_created_refund`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**Winback cancellation Canvas**

Users were able to cancel their orders before fulfillment. This Canvas sends follow-up messages to get the user to make their purchase again.

Action-based entry event: `shopify_cancelled_order`<br>
Exception event: `shopify_created_order` or Purchase

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}