---
nav_title: Back-In-Stock Notifications
article_title: Back-In-Stock Notifications
alias: "/back_in_stock/"
page_order: 1
description: "This reference article describes how to create back-in-stock notifications in Braze Shopify catalogs."
---

# Back-in-stock notifications

> Using a combination of back-in-stock notifications in Braze Shopify catalogs and a Canvas, you can create and notify customers when an item is back-in-stock. Any time a customer clicks on an item in the catalog, they can be automatically subscribed to be notified when the item is replenished.

{% alert important %}
Back-in-stock notifications for Braze Shopify catalogs are currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

When a customer clicks an item, we'll automatically subscribe them to receive back-in-stock notifications. Once the item's inventory quantity meets your inventory rule (such as an inventory larger than 100), all subscribers will be elgible for notifications through a campaign or Canvas. However, only users who opted into notifications will receive notifications. 

## How back-in-stock notifications work

As a Braze Shopify user with a Shopify catalog, you have a field called `inventory_quantity` that's synced from Shopify to Braze. Your Shopify users will send a `shopify_product_clicked` event when they click an item. This event and the Shopify catalog data will subscribe your users to back-in-stock notifications.

When an item has an `inventory_quantity` that meets your inventory rule, we'll look up all your users who are subscribed to that item (users who clicked the item) and send a Braze custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends!

## Prerequisities

- Use the Braze Shopify integration
- Use Braze Shopify catalogs
- Enable the back-in-stock feature flag

## Setting up back-in-stock notifications - Catalogs

Follow these steps to set up back-in-stock notifications in a specific catalog.

1. Go to your catalog and select the **Settings** tab.
2. Select the **Back in stock** toggle.
3. Set your iventory rule, such as greater than 0. This rule will be applied to all products.
4. Set your notification rule:
- **Notify all**: Notify all customers who are waiting for the item to be back in stock.
- **Trickle**: Notify X customers per 10 minutes per item. Braze will notify the specified number of customers in 10-minute increments until there are no more customers to notify or the item goes out of stock.
    - You currently cannot control the number of customers notified within a time period.

![Catalog settings that show the back in stock feature turned on. The notification rules are to notify a thousand users every ten minutes.][1]

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using back-in-stock notifications - Canvas and campaign

After setting up the back-in-stock feature in a catalog, follow these steps to use with a Canvas or campaign.

1. Set up an action-based Canvas or campaign.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog with the back-in-stock notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers can be notified when an item is back in stock.

### Using Liquid
{% raw %}
To template in details about the catalog item that's back in stock, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

Using ``{{canvas_entry_properties.${catalog_update}}}`` will return the ID of the item that came back in stock.
Use this Liquid tag  ``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}}} %}`` at the top of your message, then use ``items[0].<field_name>` to access data about that item throughout the message.
{% endraw %}

## Considerations

- Users are only subscribed for 90 days. If the item isn't back in stock in 90 days, the user is unsubscribed.
- When using the **Notify all** notification rule, Braze will notify 100,000 over 10 minutes.
- Braze will process at most 10 item updates over one minute. If you update 11 items in one minute, only the first 10 will be able to trigger a back-in-stock notification.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %} 