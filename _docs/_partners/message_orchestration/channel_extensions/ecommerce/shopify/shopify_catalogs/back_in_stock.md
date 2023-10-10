---
nav_title: Back-In-Stock Notifications
article_title: Back-In-Stock Notifications
page_order: 1
description: "This reference article covers."
---

# Back-in-stock notifications

> 

{% alert important %}
Back-in-stock notifications for Braze Shopify catalogs are currently in early access. Contacy your account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

Any time a customer clicks on an item, we’ll automatically subscribe them to be notified of that item’s replenishment.  No need to fill out a form.

When the item’s inventory quantity meets the inventory rule, all customers who clicked on that item will be eligible to be notified through a canvas/campaign.

Subscription statuses will be observed so if the user has not opted in to notifications, they will be filtered out and will not receive notifications.

Note that users are only subscribed for 90 days. If an item isn't back in stock within 90 days, the user is removed from the subscription. Braze will process up to 10 item updates per minute. This means if you update 11 items in one minute, only the first 10 items will trigger the back-in-stock notification.

## Setting up back-in-stock

Follow these steps to set up back-in-stock in a specific catalog.

1. Go to your catalog and click the **Settings** tab.
2. Select the **Back in stock** toggle.
3. Set your inventory rule. This applies to all products in your catalog.
4. Set your notification rule. There are two options: **Notify all** and **Trickle**. **Notify all** will notify all customers who are waiting when the item is back in stock. **Trickle** will notify a specified number of customers per 10 minutes per item. Braze will notify the specified numbers of customers in 10-minute increments until there are no more customers to notify, or until the item goes out of stock. 

## Using back-in-stock in Canvas

After setting up the back-in-stock feature in a catalog, follow these steps to use with Canvas.

1. Set up an action-based Canvas.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog you're using.
4. Continue the Canvas setup steps as you normally would.

### Using Liquid
{% raw %}
To template in details about the catalog item that's back in stock, you can use the `catalog_entry_properties` Liquid tag to access the `item_id`. 

Using ``{{catalog_entry_properties.${item_id}}}`` will return the ID of the item that came back in stock.
Use this Liquid tag  ``{% catalog_items <name_of_your_catalog> {{catalog_entry_properties.${item_id}}} %}`` at the top of your message, then use ``items[0].<field_name>` to access data about that item throughout the message.
{% endraw %}

