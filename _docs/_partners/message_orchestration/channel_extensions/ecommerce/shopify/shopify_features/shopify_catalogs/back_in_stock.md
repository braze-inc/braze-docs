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

When a customer clicks an item, we'll automatically subscribe them to receive back-in-stock notifications for that item. Once the item's inventory quantity is greater than zero, all subscribers will be eligible for notifications through a campaign or Canvas. However, only users who opted into notifications will receive notifications. 

## How back-in-stock notifications work

As a Braze Shopify user with a Shopify catalog, you have a field called `inventory_quantity` that's synced from Shopify to Braze. Your Shopify users will send a `shopify_product_clicked` event when they click an item. This event and the Shopify catalog data will subscribe your users to back-in-stock notifications.

When an item has an `inventory_quantity` that meets your inventory rule, we'll look up all your users who are subscribed to that item (users who clicked the item) and send a Braze custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends!

## Prerequisities

- Use the Braze Shopify integration
- Use Braze Shopify catalogs
- Enable the back-in-stock feature flag

## Setting up back-in-stock notifications

Follow these steps to set up back-in-stock notifications in a specific catalog.

1. Go to your catalog and select the **Settings** tab.
2. Set your notification rule. There are two options:
    - **Notify all subscribed users** notifies all customers who are waiting when the item is back in stock. 
    - **Notify a certain number of users per a certain number of minutes** notifies a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify, or until the item goes out of stock. Your notification rate cannot exceed notifying 10,000 users per minute.
3. Select the **Back in stock** toggle.
4. Select the **Inventory field in catalog** as `inventory_quantity`. This will check the Shopify `inventory_quantity` field within your product syncs. If the value is greater than zero, then customers that are subscribed will be eligible to receive the back in stock notification.
5. Save your settings.

![Catalog settings that show the back in stock feature turned on. The notification rules are to notify a thousand users every ten minutes.][1]{: style="max-width:70%;"}

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using back-in-stock notifications in a Canvas or campaign

After setting up the back-in-stock feature in a catalog, follow these steps to use with a Canvas or campaign.

1. Set up an action-based Canvas or campaign.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog with the back-in-stock notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers can be notified when an item is back in stock.

### Using Liquid
{% raw %}
To template in details about the catalog item that's back in stock, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

To return the ID of the item that is back in stock, use the Liquid tag ``{{canvas_entry_properties.${catalog_update}}}``. To access data about that item throughout your message, put the Liquid tag  ``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}}} %}`` at the top of your message, then use ``items[0].<field_name>` to place the data in your message.
{% endraw %}

Here is a sample Liquid template that will display the item's product title, image URL, and price:

{% raw %}
```liquid
{% catalog_items shop-1234_shopify_catalog {{canvas_entry_properties.${catalog_update}.item_id}} %}
{{ items[0].shopify_product_title }}
{{ items[0].product_image_url }}
{{ items[0].price }}
```
{% endraw %}

## Considerations

- Users are only subscribed for 90 days. If the item isn't back in stock in 90 days, the user is unsubscribed.
- When using the **Notify all subscribed users** notification rule, Braze will notify 100,000 over 10 minutes.
- Braze will process at most 10 item updates over one minute. If you update 11 items in one minute, only the first 10 can trigger a back-in-stock notification.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %} 