---
nav_title: Swym
article_title: Swym
description: "This reference article outlines the partnership between Braze and Swym, which empowers shoppers to save products and seamlessly continue their journey across websites, mobile apps, and retail stores."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) helps eCommerce brands capture shopping intent with Wishlists, Save for Later, Gift Registry, and Back-in-Stock alerts. Using rich, permission-based data, you can craft hyper-targeted campaigns and deliver personalized shopping experiences that drive engagement, boost conversions, and increase loyalty.

*This integration is maintained by Swym.*

## About the integration

The Swym and Braze integration lets you deliver personalized, event-driven marketing campaigns that convert shopper intent into sales. Use the integration so shoppers can pick up where they left off, collaborate with others throughout their shopping journey, and receive high-performance retargeting campaigns.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Swym Wishlist Plus, Back in Stock apps, or both must be installed on your eCommerce platform (Shopify or BigCommerce), and you must be on the Enterprise plan.       |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Use cases

By connecting Swym’s Wishlist Plus and Back in Stock Alerts apps with Braze, you can automatically send shopper activity events, such as wishlist adds, back-in-stock subscriptions, price drop alerts, and reminders, into Braze as custom events. These events can then be used to trigger automated messages in Braze, facilitating timely, relevant, and engaging communication that brings shoppers back to make a purchase.

## Integrating Swym

### Step 1: Connect your Swym app to Braze

Currently, the Braze integration with Swym is a managed integration and is not self-serve. To get started, contact the Swym support team at [support@getswym.com](mailto:support@getswym.com) and provide the following information so that Swym can set up the integration on your behalf:

1. Generate a [REST API key]({{site.baseurl}}/api/basics/#about-rest-api-keys) in your Braze dashboard with the `users.track` permission.

![Generating an API key in Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
To protect your API keys, Swym recommends that you share credentials securely using a one-time, self-destructive link tool (for example, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2. Braze manages multiple instances for its dashboard and REST endpoints. Provide the [REST endpoint]({{site.baseurl}}/api/basics/#endpoints) for the instance you are provisioned.

3. After the API key and instance URL are shared with the Swym support team, they will set up the integration for you and respond with a confirmation.

4. After setup is completed, the custom events from Swym will be automatically registered in Braze. You can view the list of registered Swym events in the Braze dashboard by going to **Data Settings** > **Custom Events**. 

5. View the properties of each Swym event by selecting **Manage Properties** for the corresponding custom event. These properties contain the event values that can be used to personalize your messages.

![Custom properties in Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Step 2: Subscribe to events you want to send to Braze

From your Wishlist Plus app, go to the **Marketing** tab and find the **Automations** section. Here, you can select the events you want to subscribe to. 

![Events to be subscribed.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Swym Wishlist Plus app events

| Event name | When this event is triggered |  
|------------|------------------------------|  
| Share Wishlist | When a shopper shares a wishlist with someone else |  
| Add to Wishlist | When a shopper adds an item to their wishlist |  
| Wishlist Reminder | Reminder about items in a shopper’s wishlist|   
| Saved for Later Reminder | Reminder about a shopper’s Saved for Later items |  
| Price Drop alert | Product on a wishlist goes on sale |  
| Low Stock alert | Product on a wishlist is running low on stock |  
| Back in Stock alert | Product on a wishlist is restocked |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Swym Back in Stock Alerts app events

| Event Name | When this event is triggered |  
|------------|------------------------------|  
| Back in Stock Acknowledgment | Shopper subscribes to be notified when a product is back in stock |  
| Restock Alert | Product a shopper requested a back-in-stock alert for is restocked |  
| Restock Reminder | Follow-up alert (usually approximately 24 hours after the first restock alert, configurable)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 3: Create a Braze campaign or Canvas

To automate the delivery of personalized messages for your shoppers, you must create a separate campaign or Canvas in Braze for each event you subscribed to. Each campaign or Canvas should be configured to trigger based on the specific event and use the corresponding event properties to populate dynamic content in your messages. For step-by-step guidance, you can refer to [Getting Started: Campaigns and Canvases]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![An action-based event.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

For additional details, refer to the [Swym help center](https://help.getswym.com/en/articles/12344153-braze-integration) or contact the Swym support team at [support@getswym.com](mailto:support@getswym.com). 