Content Cards and Banners are both in-product messages you can embed directly in your app or website. While similar, they serve different purposes and have different features:

| Feature | Content Cards | Banners |
| --- | --- | --- |
| **Best for** | Persistent notification centers and feeds where users can discover and revisit content at their own pace. | High-visibility, contextual messages for spotlights, promotions, and ongoing campaigns. |
| **Delivery methods** | Scheduled, action-based, and API-triggered. | Scheduled availability window only. |
| **Canvas support** | Yes. | No (coming in a future release). |
| **Content updates** | Content is **static**; it is set when sent and does not change. | Content **refreshes** at each session start, including any personalization updates. |
| **Creation** | Standard editor. | Drag-and-drop editor for easy content building. |
| **Persistence** | Up to 30 days before expiring. | Unlimited (based on the campaign window). |
| **Customization** | Sends a flexible data payload (JSON) to support complex, custom-built use cases. | Supports custom HTML/CSS/JavaScript within the editor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Which should I use?

Consider using **Content Cards** when you need to:
* Trigger messages from an API or based on user actions.
* Include messages as part of a Canvas journey.
* Power complex, custom-built features that require a flexible data payload (e.g., sending raw JSON, not just pre-formatted content).

Consider using **Banners** when you need to:
* Build and launch messages quickly with a drag-and-drop editor.
* Show persistent messages that last longer than 30 days.
* Ensure content and personalization update automatically every time a user starts a new session.
* Manage message placement and priority natively within your app.

Many customers use both. For example, you might use **Banners** for homepage promotions that need to update dynamically, while using **Content Cards** for a notification center where users can review past offers and updates.
