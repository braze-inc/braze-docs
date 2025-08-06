---
nav_title: Setting Up Shopify
article_title: "Setting up Shopify"
description: "This reference article outlines how to set up Shopify after integrating it into your Braze Web SDK."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Setting up Shopify in Braze

> This article outlines how to finish setting up the Shopify integration with Braze. Follow these instructions after you have [implemented the Braze Web SDK]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) onto your Shopify website.

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

## Shopify integration setup in Braze

### Step 1: Connect your Shopify store

In Braze, go to **Partner Integrations** > **Technology Partners** and then search for “Shopify”.

{% alert note %}
If you are using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

On the Shopify partner page, select **Go to Shopify App Store** to start the integration process.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

You’ll then be directed to the Shopify App Store to install the Braze app.

{% alert note %}
If your Shopify account is associated with more than one store, you can switch which store you’re logged into by selecting the store icon at the top-right of the page and selecting **Switch stores**. 
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

After selecting your store of choice, select **Install** on the Braze app page. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

After you install the Braze app, you will be redirected to Braze to confirm the workspace you want to connect to Shopify. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

After confirming that you're in the correct workspace, you can complete configuring your Shopify integration by selecting **Begin setup**.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
You can only connect one store per workspace at this time. If you have multiple Shopify stores that you’d like to connect to your workspace, reach out to your customer success manager for details on the Shopify multiple stores beta.
{% endalert %}

### Step 2: Select events and historical backfill

After connecting your Shopify store, proceed to Step 2 and select the events to include as part of your integration. You must select at least one event.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

Selecting **Product Viewed**, **Product Clicked**, or **Abandoned Cart** events will require the Braze Web SDK for tracking. If you implement the Braze Web SDK either through [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) or directly into your Shopify’s site [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features), Braze will automatically generate the tracking scripts and load onto your site. If you implement the Web SDK to your [headless Shopify site]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), you must manually turn on tracking for these events. 

#### Backfill historical data (optional)

You can optionally enable a backfill of purchases from the last 90 days prior to your installation. By automatically syncing past customer and purchase data, you can immediately start targeting and engaging with your customers. To learn more, check out Shopify historical backfill.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
For the backfill to import Order Created Events and Braze Purchase Events, you must have selected **Order Created** and **Braze Purchase Event** to include as part of your integration.
{% endalert %}

### Step 3: Collect subscribers (optional)

Using the Shopify integration, you can collect email and SMS subscribers from your Shopify store to Braze. For more information, see [Syncing Shopify subscribers]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Step 4: Set up Shopify product syncs (optional)

You can optionally sync your products in near real-time from your Shopify store into a Braze catalog, automating the process to bring in product data for deeper personalization of your messages. To learn more, check out [Shopify product syncs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Step 5: Enable in-browser messaging 

You can optionally use an additional channel on your Shopify store for in-browser messages by turning on this feature. This allows you to use our basic message types like slide-up, modal, full screen, simple surveys, and custom HTML.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

If you enable in-browser messages, the Braze Web SDK must be implemented for tracking. If you implement the Braze Web SDK either through [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) or directly into your Shopify’s site [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features), Braze will automatically generate the basic in-browser message implementation script onto your site. If you implement the Web SDK to your [headless Shopify site]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) or plan to add customizations to in-browser messages, you must manually add in-browser messages onto your site using our [developer guide]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web). 

### Step 6: Finish setup

After you configure your setup, select **Finish Setup**.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

That’s it! The “Connection Pending” status will update to “Connected” and will display the timestamp of when the connection was established. You’ll also see if each Shopify feature has successfully been enabled on the page. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Advanced Settings (optional) 

#### Update abandoned cart and abandoned checkout delays

By default, Braze automatically sets the delay to trigger the `shopify_abandoned_checkout` and `shopify_abandoned_cart` events to one hour of inactivity. You can set the **Abandoned Cart Delay** and **Abandoned Checkout Delay** for each event from 5 minutes up to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Set your preferred product identifier

If you included Braze purchase events in your Shopify integration setup, by default, Braze will set the Shopify Product ID as the `product_id` used within the Braze purchase event. This will be used when you filter for products purchased in Y days or personalize content in your message using Liquid.

You can also choose to set either the SKU or product title from Shopify instead of the Shopify Product ID.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Troubleshooting

{% details Why is my Shopify app install still pending? %}
Your installation may still be pending for one of the following reasons:
 - When Braze is setting up your Shopify webhooks
 - When Braze is communicating with Shopify


If your app installation is pending for 1 hour, Braze will fail the installation, and you will be prompted to Retry Setup.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Why did my Shopify app install fail? %}
Your install may have failed for one of the following reasons:
 - Braze could not reach Shopify
 - Braze failed to process the request
 - Your Shopify access token is invalid
 - The Braze Shopify app was deleted from your Shopify admin page


If this happens, you will be able to select **Retry Setup** and start the installation process again.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details How do I uninstall the Braze application from my Shopify store? %}

There are two ways to uninstall Braze from your Shopify store:

1. On the Shopify partner page, select **Disconnect**.<br><br> ![The "Disconnect Integration" section with a link to disconnect.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Go to your Shopify admin page located under **Apps**. You will then see an option to delete the Braze application.<br><br> ![A modal asking for confirmation you'd like to delete the Braze app.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details I am struggling to reconcile my users. What might be the reason? %}

The type of support you'll need for user reconciliation is determined by how you implemented the Web SDK. For more information, refer to [Getting started with Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/). 

- If you're on a Shopify headless site, check out [headless implementation]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) to make sure you've enabled checkout user reconciliation.
- If you're encountering duplicate user profiles with the same email or phone number, you can use the following Braze tools to merge the duplicates into one profile: 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) endpoint
    - [Bulk merging]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- If you use the ScriptTag integration, and your Shopify store offers a "Buy Now" option that skips the cart, Braze may struggle to reconcile users as Shopify does not allow script tags to retrieve a `device_id` to map the events to a user who skips the cart.

{% enddetails %}
