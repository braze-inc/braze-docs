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

## How it works

Back-in-stock notifications are determined by notification rules. Subscription statuses will be observed, so if the user has not opted in to notifications, they will be filtered out and will not receive notifications.

Note that users are only subscribed for 90 days. If an item isn't back in stock within 90 days, the user is removed from the subscription. Braze will process up to 10 item updates per minute. This means if you update 11 items in one minute, only the first 10 items will trigger the back-in-stock notification.

## Setting up back-in-stock notifications

Follow these steps to set up back-in-stock notifications in a specific catalog.

1. Go to your catalog and click the **Settings** tab.
2. Select the **Back in stock** toggle.
3. Set your notification rule. There are two options: **Notify all subscribed users** and **Notify a certain number of users per a certain number of minutes**. <br>Selecting **Notify all subscribed users** notifies all customers who are waiting when the item is back in stock. **Notify a certain number of users per a certain number of minutes** notifies a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify, or until the item goes out of stock. Your notification rate cannot exceed notifying 10,000 users per minute.

![Catalog settings that show the back in stock feature turned on. The notification rules are to notify a thousand users every ten minutes.][1]

{% alert important %}
Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.
{% endalert %}

## Using back-in-stock notifications in Canvas

After setting up the back-in-stock feature in a catalog, follow these steps to use with Canvas.

1. Set up an action-based Canvas.
2. Select **Back in stock** as the trigger.
3. Select the name of the catalog with the back-in-stock notifications.
4. Continue [setting up]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) your Canvas as you would.

Now, your customers can be notified when an item is back in stock.

### Using Liquid
{% raw %}
To template in details about the catalog item that's back in stock, you can use the `canvas_entry_properties` Liquid tag to access the `item_id`. 

Using ``{{canvas_entry_properties.${catalog_update}.item_id}}`` will return the ID of the item that came back in stock.
Use this Liquid tag  ``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}}`` at the top of your message, then use ``items[0].<field_name>` to access data about that item throughout the message.
{% endraw %}

[1]: {% image_buster /assets/img/back_in_stock_settings.png %} 