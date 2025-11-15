Content Cards and Banners are both in-product messages you can embed directly in your app or website. While similar, they serve different purposes and have different features:

| Feature | Content Cards | Banners |
| --- | --- | --- |
| **Best for** | Feeds, like inboxes and notification centers, where users can discover and revisit content at their own pace. | Embedded, high-visibility banners for spotlights, promotions, and ongoing campaigns. |
| **Delivery methods** | Scheduled, action-based, and API-triggered. | Scheduled availability window only. |
| **Canvas support** | Yes. | No (coming in a future release). |
| **Content updates** | Dynamic liquid becomes **static**; it is set when sent and does not change. | Dynamic content **refreshes** every time a banner is requested. |
| **Creation** | Standard editor. | Drag-and-drop editor for easy content building; can add custom HTML/CSS. |
| **Persistence** | Up to 30 days before expiring. | Unlimited (based on the campaign window). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Which should I use?

Consider using **Content Cards** when you need to:
* Show messages in a feed, like a notification center or inbox.
* Trigger messages from an API or based on user actions.
* Include messages as part of a Canvas journey.

Consider using **Banners** when you need to:
* Build custom messages quickly with a drag-and-drop editor or HTML code.
* Show persistent messages that last longer than 30 days.
* Ensure content and personalization update automatically every time a banner is requested.
* Manage message placement and priority within your app.

Many customers use both. For example, you might use **Banners** for homepage promotions that need to update dynamically, while using **Content Cards** for a notification center where users can review past offers and updates.
