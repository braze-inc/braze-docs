Both Content Cards and Banners are part of Braze's in-product messaging suite and can be embedded directly into your app or website. However, they serve different purposes and have distinct capabilities:

| Feature | Content Cards | Banners |
| --- | --- | --- |
| **Best for** | Persistent notification centers and feeds where users can discover and revisit content at their own pace | High-visibility, contextual messages for spotlights, promotions, and ongoing campaigns |
| **Delivery methods** | Scheduled, action-based, and API-triggered | Scheduled only |
| **Canvas support** | Yes | No (coming in future) |
| **Content updates** | Rendered at impression or send time; content doesn't change after rendering | Refreshes at each session start, including personalization updates |
| **Creation** | Standard editor with optional customization | Drag-and-drop editor for easy content building |
| **Persistence** | Up to 30 days before expiring | Unlimited (campaign window-based) |
| **Customization** | Highly flexible data payload system that can be adapted to virtually any use case | Custom HTML/CSS/JavaScript available in editor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Which should I use?

Consider using **Content Cards** when you need:
- API-triggered or action-based messaging
- Canvas journey support
- Maximum flexibility to adapt to diverse or non-standard use cases
- A versatile data delivery system that extends beyond traditional messaging

Consider using **Banners** when you need:
- Quick deployment with minimal development effort using the drag-and-drop editor
- Truly persistent messaging (beyond 30 days)
- Content that dynamically updates with each user session
- Native placement management and prioritization

Many customers use both Content Cards and Banners together to maximize their in-product messaging capabilities. For example, you might use Banners for homepage promotions that need to update dynamically, while using Content Cards for a notification center where users can review past offers and updates.
