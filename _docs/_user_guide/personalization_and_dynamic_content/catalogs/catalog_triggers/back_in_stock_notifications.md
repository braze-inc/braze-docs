---
nav_title: Back-In-Stock Notifications
article_title: Back-In-Stock Notifications
page_order: 2
description: "This reference article describes how to create back-in-stock notifications in Braze catalogs."
---

# Back-in-stock notifications

> Using a combination of back-in-stock notifications through Braze catalogs and a Canvas, you can notify customers when an item is back-in-stock. Any time a customer performs a selected custom event, they can be automatically subscribed to be notified when the item is replenished.

{% alert important %}
Back-in-stock notifications for catalogs are currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

When a user triggers a custom event for an item, we'll automatically subscribe them to receive back-in-stock notifications for that item. When the item's inventory quantity meets your inventory rule (such as an inventory larger than 100), all subscribers will be eligible for notifications through a campaign or Canvas. However, only users who opted into notifications will receive notifications. 

## How back-in-stock notifications work

You'll set up a custom event to use as a subscription event, such as a `product_clicked` event. This event must contain a property of the item ID (catalog item IDs). We suggest you include a catalog name, but this isn't required. You'll also provide the name of an inventory quantity field, which must be a number-data type.

When an item has an inventory quantity that meets your inventory rule, we'll look up all your users who are subscribed to that item (users who did the subscription event) and send a Braze custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends!

## Setting up back-in-stock notifications

Follow these steps to set up back-in-stock notifications in a specific catalog.

1. Go to your catalog and select the **Settings** tab.
2. Select the **Back in stock** toggle.
3. If the global back-in-stock settings have not been configured, you will be prompted to set up the custom events and properties that will be used to trigger back-in-stock notifications:
    <br> ![Catalog settings drawer.][2]{: style="max-width:70%;"}
    - **Fallback Catalog** This is the catalog that will be used for the back-in-stock subscription, if there is no `catalog_name` property present on the custom event.
    - **Custom event for subscriptions** is the Braze custom event that will be used to subscribe a user for back-in-stock notifications. When this event occurs, the user that performed the event will be subscribed.
    - **Custom event for unsubscribing** is the Braze custom event that will be used to unsubscribe a user from back-in-stock notifications.
    - **Item ID event property** is the property on the above custom event that will be used to determine the item for a back-in-stock subscription or unsubscription. This property on the custom event should contain an Item ID, that is present in a catalog. The custom event should also contain a `catalog_name` property, to specify which catalog this item is in.
    
    - A sample custom event would look like
    ```json
    {
        "events": [
            {
                "external_id": "<external_id>",
                "name": "subscription",
                "time": "2024-04-15T19:22:28Z",
                "properties": {
                    "id": "shirt-xl",
                    "catalog_name": "on_sale_products",
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
Back-in-stock and price-drop triggers use the same event to subscribe the user to the notification. Create a price drop notification by setting `type` to `back-in-stock`. You cannot set both a price drop and back in stock notification.
{% endalert %}

{: start="4"}
4. Select **Save** and continue to the catalog's **Settings** page.
5. Set your notification rule. There are two options:
    - **Notify all subscribed users** notifies all customers who are waiting when the item is back in stock. 
    - **Set notification limits** notifies a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify or until the item goes out of stock. Your notification rate cannot exceed notifying 10,000 users per minute.
6. Set the **Inventory field in catalog**. This catalog field will be used to determine if the item is out of stock. The field must be number type.
7. Select **Save settings**.

![Catalog settings that show the back-in-stock feature turned on. The notification rules are to notify a thousand users every ten minutes.][1]

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using back-in-stock notifications in a Canvas

After setting up the back-in-stock feature in a catalog, follow these steps to use with Canvas.

1. Set up an action-based Canvas.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog with the back-in-stock notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers can be notified when an item is back in stock.

### Using Liquid

To template in details about the catalog item that's back in stock, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

Using {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} will return the ID of the item that came back in stock. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} will return the inventory value of the item prior to the update, and {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} will return the new inventory value after the update.

Use this Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} at the top of your message, then use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} to access data about that item throughout the message.

## Considerations

- Users are only subscribed for 90 days. If the item isn't back in stock in 90 days, the user is unsubscribed.
- When using the **Notify all subscribed users** notification rule, Braze will notify 100,000 over 10 minutes.
- Braze will process at most 10 item updates over one minute. If you update 11 items in one minute, only the first 10 can trigger a back-in-stock notification.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
