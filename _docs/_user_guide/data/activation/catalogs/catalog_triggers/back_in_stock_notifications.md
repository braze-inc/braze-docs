---
nav_title: Back-in-stock notifications
article_title: Set up back-in-stock notifications
page_order: 2
description: "Learn how to set up back-in-stock notifications using your catalog and custom events, so you can automatically subscribe customers to receive notifications when an item is back in stock."
---

# Back-in-stock notifications

> Learn how to set up back-in-stock notifications using your catalog and custom events, so you can automatically subscribe customers to receive notifications when an item is back in stock. Keep in mind, this only applies to users who've already opted in to notifications.

## How it works

You can set up a custom event to use as a subscription event, such as a `product_clicked` event. This event must contain a property of the item ID (catalog item IDs). We suggest you include a catalog name, but this isn't required. You'll also provide the name of an inventory quantity field, which must be a number data type. 

Note that a catalog item's stock must be at zero for a user to subscribe to it successfully. When an item has an inventory quantity greater than zero, Braze will look up all users subscribed to that item and send a custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends.

## Setting up back-in-stock notifications

Follow these steps to set up back-in-stock notifications in a specific catalog.

1. Go to your catalog and select the **Settings** tab.
2. Select the **Back in stock** toggle.
3. If the global back-in-stock settings have not been configured, you will be prompted to set up the custom events and properties that will be used to trigger back-in-stock notifications:
    <br> ![Catalog settings drawer.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback Catalog** This is the catalog that will be used for the back-in-stock subscription, if there is no `catalog_name` property present on the custom event.
    - **Custom event for subscriptions** is the Braze custom event that will be used to subscribe a user to back-in-stock notifications. When this event occurs, the user who performed the event will be subscribed.
    - **Custom event for unsubscribing** is the Braze custom event that will be used to unsubscribe a user from back-in-stock notifications. This event is optional. If the user doesn't perform this event, they'll be unsubscribed after 90 days or when the back-in-stock event triggers, whichever occurs first.
    - **Item ID event property** is the property on the above custom event that will be used to determine the item for a back-in-stock subscription or unsubscription. This property on the custom event should contain an item ID (`id`) that is present in a catalog. The item ID must be sent as a string so that it matches the `id` data type stored in the target catalog. The custom event should also contain a `catalog_name` property to specify which catalog this item is in.
    
    - A sample custom event would look like:
    
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
Back-in-stock and price-drop triggers use the same event to subscribe the user to the notification, so you can use the `type` property to set both price-drop and back-in-stock notifications in the same event. Note that the `type` property must be an array.
{% endalert %}

{: start="4"}
4. Select **Save** and continue to the catalog's **Settings** page.
5. Set your notification rule. There are two options:
    - **Notify all subscribed users** notifies all customers who are waiting when the item is back in stock. 
    - **Set notification limits** notifies a specified number of customers per your configured notification period. Braze will notify the specified number of customers in increments until there are no more customers to notify or until the item goes out of stock. Your notification rate cannot exceed notifying 10,000 users per minute.
6. Set the **Inventory field in catalog**. This catalog field will be used to determine if the item is out of stock. The field must be a number type.
7. Select **Save settings**.

![Catalog settings that show the back-in-stock feature turned on. The notification rules are to notify a thousand users every ten minutes.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using back-in-stock notifications in a Canvas

After setting up the back-in-stock feature in a catalog, follow these steps to use it with Canvas.

1. Set up an action-based Canvas.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog with the back-in-stock notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers can be notified when an item is back in stock.

### Using Liquid

To template in details about the catalog item that's back in stock, you can use the `context` Liquid tag to access the `item_id`. 

Using {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} will return the ID of the item that came back in stock. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} will return the inventory value of the item prior to the update, and {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} will return the new inventory value after the update.

Use this Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} at the top of your message, then use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} to access data about that item throughout the message.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

## Considerations

- Users are only subscribed for 90 days. If the item isn't back in stock in 90 days, the user is unsubscribed.
- When using the **Notify all subscribed users** notification rule, Braze will notify 100,000 users over 10 minutes.
- Braze will process 10 requests to update catalog items per minute. Update endpoints allow for 50 item updates per request, supporting up to 500 item updates per minute that can trigger back-in-stock notifications

