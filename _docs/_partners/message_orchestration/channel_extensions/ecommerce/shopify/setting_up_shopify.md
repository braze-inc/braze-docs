---
nav_title: Setting Up Shopify
article_title: "Setting up Shopify"
description: "This reference article outlines how to set up Shopify after integrating it into your Braze Web SDK."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify/"
page_order: 2
---

# Setting up Shopify in Braze

> This article outlines how to finish setting up the Shopify integration with Braze. Follow these instructions after you have [implemented the Braze Web SDK]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) onto your Shopify website.

## Shopify integration setup in Braze

### Step 1: Locate Shopify within the dashboard

In Braze, go to **Partner Integrations** > **Technology Partners** and then search for “Shopify”.

{% alert note %}
If you are using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

On the Shopify partner page, select **Begin Setup** to start the integration process.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %})

### Step 2: Braze setup

In the Braze setup workflow, enter your Shopify store name. Make sure you enter your store name, not your Shopify domain. 

![]({% image_buster /assets/img/Shopify/shop_setup_2.png %})

You can only connect one store per workspace at this time. If you have multiple Shopify stores that you’d like to connect to your workspace, reach out to your customer success manager for details on the Shopify multiple stores beta.

### Step 3: Flexible event selection

Read the explanation of which events require us to implement the Braze Web SDK on your store and what to expect when this is added. Then, select and confirm the Shopify events you want Braze to track. Selecting any events with an asterisk (*) next to them will enable our Web SDK.

![]({% image_buster /assets/img/Shopify/shop_setup_3a.png %})

![]({% image_buster /assets/img/Shopify/shop_setup_3b.png %})

### Step 4: Backfill historical data (optional)

You can optionally enable a backfill of purchases from the last 90 days prior to your installation. By automatically syncing past customer and purchase data, you can immediately start targeting and engaging with your customers. To learn more, check out Shopify historical backfill.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %})

{% alert warning %}
To make sure the backfill imports Order Created Events and Braze Purchase Events, you must have selected “Order Created” and “Braze Purchase Event” during event selection in [Step 3](#step-3-flexible-event-selection).
{% endalert %}

### Step 5: Shopify Catalog Sync (optional)

You can optionally import your products in near real-time from your Shopify store into a Braze catalog, automating the process to bring in product data for deeper personalization of your messages. To learn more, check out [Shopify catalogs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shop_setup_5.png %})

### Step 6: Enable in-browser message channel (optional)

You can optionally use an additional channel on your Shopify store for in-browser messages. This allows you to use our basic message types like slide-up, modal, full screen, simple surveys, and custom HTML. 

![]({% image_buster /assets/img/Shopify/shop_setup_6.png %})

If you enable in-app messages, Braze will add the necessary in-app message scripts to your Shopify site, regardless of how you implement the Web SDK in your Shopify site. If you plan to customize in-app messages on your site, refer to the [in-app message developer guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/). 

### Step 7: Collect email or SMS subscribers (optional)

You can optionally select whether you want to collect email and SMS opt-ins from your Shopify store to sync to Braze. We recommend that you determine a source of truth for your subscriber statuses and modify your settings accordingly. To learn more, check out [Syncing Shopify subscribers](). 

![]({% image_buster /assets/img/Shopify/shop_setup_7.png %})

### Step 8: Install the Braze app 

You’ll then be redirected to your Shopify store to install the Braze app. Select **Install App** to be redirected to the Braze dashboard.

![]({% image_buster /assets/img/Shopify/shop_setup_8.png %})

Step 9: Verify integration 
The status of your integration appears in the **Data Import** section of the Shopify partner page. 

After the Braze app is installed, you will be notified via email, and Braze will start to ingest your selected Shopify data. You’ll also be notified via email when your historical backfill and initial catalog import are completed. Additionally, the **Connection Pending** status will be updated to **Connected** and will display the timestamp of when the connection was established. 

![]({% image_buster /assets/img/Shopify/shop_setup_9.png %})

### Advanced Settings (optional) 

#### Update abandoned cart and abandoned checkout delays

By default, Braze automatically sets the delay to trigger the `shopify_abandoned_checkout` and `shopify_abandoned_cart` events to one hour of inactivity. You can set the **Abandoned Cart Delay** and **Abandoned Checkout Delay** for each event from 5 minutes up to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %})

#### Set your preferred product identifier

If you included Braze purchase events in your Shopify integration setup, by default, Braze will set the Shopify Product ID as the `product_id` used within the Braze purchase event. This will be used when you filter for products purchased in Y days or personalize content in your message using Liquid.

You can also choose to set either the SKU or product title from Shopify instead of the Shopify Product ID.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %})