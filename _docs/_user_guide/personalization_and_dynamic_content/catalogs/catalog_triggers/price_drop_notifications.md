---
nav_title: Price Drop Notifications
article_title: Price Drop Notifications
page_order: 3
alias: "/price_drop_notifications/"
description: "This reference article describes how to create price drop notifications in Braze catalogs."
---

# Price drop notifications

> Using a combination of price drop notifications through Braze catalogs and a Canvas, you can notify customers when an item's price has decreased. Any time a customer performs a selected custom event, they can be automatically subscribed to be notified when the item's price is reduced.

{% alert important %}
Price drop notifications for catalogs are currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

When a user triggers a custom event for an item, we'll automatically subscribe them to receive price drop notifications for that item. When the item's price meets your inventory rule (such as a drop larger than 50%), all subscribers will be eligible for notifications through a campaign or Canvas. However, only users who opted into notifications will receive notifications. 

## How price drop notifications work

You'll set up a custom event to use as a subscription event, such as a `product_clicked` event. This event must contain a property of the item ID (catalog item IDs). We suggest you include a catalog name, but this isn't required. You'll also provide the name of a price field, which must be a number-data type. 

When a selected custom event is performed by a user and has a `type` property that includes `price_drop`, it can be used to create a price drop subscription for a user and a catalog item it occurred for. You can also use this `type` array to set both price-drop and back-in-stock notifications in the same event.

When an item has a price change that meets your price rule, we'll look up all your users who are subscribed to that item (users who did the subscription event) and send a Braze custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends!

## Setting up price drop notifications

Follow these steps to set up price drop notifications in a specific catalog.

1. Go to your catalog and select the **Settings** tab.<br>
2. Select the **Price Drop** toggle.<br>
3. If the global catalog settings have not been configured, you will be prompted to set up the custom events and properties that will be used to trigger notifications:
    <br> ![Catalog settings drawer.][2]{: style="max-width:70%;"}
    - **Fallback Catalog:** The catalog used for the subscription if there isn't a `catalog_name` property in the custom event.
    - **Custom event for subscribing:** The Braze custom event used to subscribe a user for catalog notifications. When this event occurs, the user who performed the event will be subscribed.
    - **Custom event for unsubscribing:** The Braze custom event used to unsubscribe a user from notifications.
    - **Item ID event property:** The property on the above custom event used to determine the item for a subscription or unsubscription. This property on the custom event should contain an item ID that exists in a catalog. The custom event must contain a `catalog_name` property to specify which catalog this item is in.
   
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
                    "type": ["price_drop", "back_in_stock"]
                }
            }
        ]
    }
    ```

{: start="4"}
4. Select **Save** and continue to the catalog's **Settings** page.
5. Set your notification rule. There are two options:
    - **Notify all subscribed users** notifies all customers who are waiting when the item's price drops.
    - **Set notification limits** notifies a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify, or until the item's price goes back up. Your notification rate cannot exceed notifying 10,000 users per minute.
6. Set the **Price field in catalog**. This is the catalog field that will be used to determine the item's price. It must be a number type.<br>
7. Set the **Price drop rule**. This is the logic used to determine if a notification should be sent. A price drop can be configured as a percentage price change or how much value the price field has changed by.<br>
8. Select **Save settings**.

![Catalog settings that show the price drop feature turned on. The price drop rule is a change of three percent to the original price.][1]{:style="max-width:60%;"}

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using price drop notifications in Canvas

After setting up the price drop notifications in a catalog, follow these steps to use these notifications in a Canvas.

1. Set up an action-based Canvas.
2. Select **Perform Price Drop Event** as the trigger.
3. Select the name of the catalog with the price drop notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers will be notified when an item's price drops.

### Using Liquid

To template in details about the catalog item that has dropped in price, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

Using {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} will return the ID of the item that dropped in price. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} will return the price value of the item prior to the update, and {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} will return the new price value after the update. 

Use this Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} at the top of your message, then use {%raw%}`{{items[0].<field_name>}}`{%endraw%} to access data about that item throughout the message.

## Considerations

- Users are subscribed for 90 days. If an item does not drop in price in 90 days, the user is removed from the subscription.
- When using the **Notify all subscribed users** notification rule, Braze will notify 100,000 users over 10 minutes.
- Braze will process up to 10 item updates per minute. This means if you update 11 items in one minute, only the first 10 items can trigger a price drop notification.

[1]: {% image_buster /assets/img/price_drop_notifications.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
