---
nav_title: Price drop notifications
article_title: Price drop notifications
page_order: 2
description: "This reference article describes how to create price drop notifications in Braze catalogs."
---

# Price drop notifications

> Using a combination of price drop notifications through Braze catalogs and a Canvas, you can notify customers when an item's price has decreased. Any time a customer performs a selected custom event, they can be automatically subscribed to be notified when the item's price is reduced.

{% alert important %}
Price drop notifications for catalogs are currently in early access and is not supported for customers using Shopify. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

When the selected custom event is performed by a user, and has a `type` property that includes `price_drop`, it can be used to create a price drop subscription for a combination of that user and catalog item that it occurred for, Once the item's price drops by the specified amount, users can be notified through a Canvas.

Price drop notifications are determined by notification rules. If the user has not opted in to notifications, they will be filtered out and will not receive messaging.

Users are only subscribed for 90 days. If an item does not drop in price within 90 days, the user is removed from the subscription. Braze will process up to 10 item updates per minute. This means if you update 11 items in one minute, only the first 10 items will trigger the notifications.

## Setting up Price drop notifications

Follow these steps to set up price drop notifications in a specific catalog.

1. Go to your catalog and click the **Settings** tab.
2. Select the **Price Drop** toggle.
3. If the global catalog settings have not been configured, you will be prompted to set up the custom events and properties that will be used to trigger notifications:
    <br>
    - **Custom event for subscribing** is the Braze custom event that will be used to subscribe a user for catalog notifications. When this event occurs, the user that performed the event will be subscribed.
    - **Custom event for unsubscribing** is the Braze custom event that will be used to unsubscribe a user from notifications.
    - **Item ID event property** is the property on the above custom event that will be used to determine the item for a subscription or unsubscription. This property on the custom event should contain an Item ID, that is present in a catalog. The custom event should contain a `catalog_name` property, to specify which catalog this item is in.
    - **Fallback Catalog** This is the catalog that will be used for the subscription, if there is no `catalog_name` property present on the custom event. 

4. Click **Save** and continue to the catalog's Price Drop settings page.
5. Set your notification rule. There are two options: **Notify all subscribed users** and **Notify a certain number of users per a certain number of minutes**. <br>Selecting **Notify all subscribed users** notifies all customers who are waiting when the item's price drops. **Notify a certain number of users per a certain number of minutes** notifies a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify, or until the item's price goes back up. Your notification rate cannot exceed notifying 10,000 users per minute.
6. Set the **Price field in catalog** this is the catalog field that will be used to determine the item's price. It must be a Number type field.
7. Set the **Price drop rule** this is the logic that will be used to determine if a notification should be sent. Price drop can be configured as a percentage price change, or how much value the price field has changed by.
8. Click **Save settings**.

![Catalog settings that show the price drop feature turned on. The price drop rule is a change of three percent to the original price][1]

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using price drop notifications in Canvas

After setting up the price drop feature in a catalog, follow these steps to use with Canvas.

1. Set up an action-based Canvas.
2. Select **Perform Price Drop Event** as the trigger.
3. Select the name of the catalog with the price drop notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers will be notified when an item's price drops.

### Using Liquid
{% raw %}
To template in details about the catalog item that has dropped in price, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

Using ``{{canvas_entry_properties.${catalog_update}}}`` will return the ID of the item that dropped in price.
Use this Liquid tag  ``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}}} %}`` at the top of your message, then use ``items[0].<field_name>` to access data about that item throughout the message.
{% endraw %}

[1]: {% image_buster /assets/img/price_drop_notification.png %} 