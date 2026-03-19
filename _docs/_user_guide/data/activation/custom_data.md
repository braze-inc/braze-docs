---
nav_title: Custom data
article_title: Custom data
page_order: 0
page_type: landing
description: "Custom data powers your engagement strategy in Braze. Learn about custom attributes, events, catalogs, data types, and how to manage your data integrity."
---

# Custom data

> Custom data is the fuel for your engagement strategy. While standard attributes like first name and country come built-in, custom data allows you to capture the unique details that define your relationship with your customers—from their favorite movie genre to the exact moment they completed a purchase.

By bringing this information into Braze, you can move beyond generic messaging to create experiences that feel personal, timely, and relevant. You can use this data to build precise segments, personalize message content with Liquid, and trigger automated journeys based on real-time behavior.

## Attributes and events

The most important decision you'll make when setting up your data is choosing between an attribute and an event.

### Custom attributes: Who your users are

Think of custom attributes as the persistent traits or properties of your users. These are best for storing information that represents a current state or changes infrequently.

- **Use case:** You might use a `loyalty_tier` attribute to distinguish between your "Silver" and "Gold" members.
- **Personalization:** Attributes are perfect for personalization. You can pull a user's `favorite_category` into an email subject line to catch their eye.
- **Storage:** This data stays on a user's profile indefinitely as long as the profile remains active.

For more information, refer to [Custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Custom events: What your users do

Custom events track specific actions your users take at a single point in time. These are high-value interactions that help you understand the "when" and "how often" of user behavior.

- **Use case:** When a user completes a signup, you can log a `completed_registration` event.
- **Triggering:** Events are the primary way to trigger action-based delivery. You can send a "Welcome" push notification the moment the `completed_registration` event is logged.
- **Metadata:** You can add extra details to an event using event properties, such as the name of the item added to a cart.
- **Analytics:** Events power segmentation, reporting, and analytics so you can measure engagement and optimize your messaging.

For more information, refer to [Custom events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

## Catalogs

While attributes and events focus on your users, catalogs allow you to bring in non-user data like product inventories, course details, or event listings.

By importing this metadata through CSV or API, you can enrich your messages with information that isn't stored on the user profile. For example, you can use a catalog to automatically notify customers when an item they previously viewed is back in stock or has dropped in price.

For more information, refer to [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Data types

Braze supports several data types for your custom data—including boolean, number, string, array, time, and object types—each with specific behaviors and segmentation options. The data type you choose affects how you can filter and personalize in campaigns and segments.

For a full reference of supported data types for custom attributes, event properties, and catalogs, refer to [Data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).

## Managing your data integrity

Braze provides several tools to help you manage your custom data as your strategy evolves.

### Data type detection and changes

Braze automatically recognizes the data type (like a number or a string) for the first value it receives for an attribute. To maintain accuracy, ensure your team sends consistent data types across your environments. If you must change a data type, keep in mind that existing data on user profiles won't be retroactively updated, which may affect your segments.

### Blocklist and delete

If you find that certain attributes or events are no longer useful or were added in error, you can remove them from your workspace.

- **Blocklist:** This stops Braze from collecting new data for that object. It prevents the data from appearing in filters or graphs but keeps the existing data on profiles.
- **Delete:** This permanently removes the data from all user profiles. You must blocklist a data object for 7 days before it becomes eligible for deletion.

For more information, refer to [Manage custom data]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) and [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).
