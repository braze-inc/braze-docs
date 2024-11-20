---
nav_title: Shopify Standard Integration Setup
article_title: "Shopify Standard Integration Setup"
description: "This reference article outlines how to set up the standard Shopify integration."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_integration/"
page_order: 1
hidden: true
---

# Shopify standard integration setup

> This page walks you through how to integrate Braze with Shopify using our standard integration for users with a Shopify online store.<br><br>This is part of the [Shopify beta collection]({{site.baseurl}}/shopify_beta/).

## Step 1: Connect your Shopify store

1. In Braze, go to **Partner Integrations** > **Technology Partners** and then search for “Shopify”.

{% alert note %}
If you’re using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

{: start="2"}
2. On the Shopify partner page, select **Begin setup** to start the integration process.<br><br>![Shopify integration page with button to begin setup.][1] 
3. In the Shopify app store, install the Braze application.<br><br>![The Braze app store page with a button for logging in to install the application.][5] 

{% alert note %}
If your Shopify account is associated with more than one store, you can change the store you’re logged into by selecting the store icon at the top-right of the page and selecting **Switch stores**.
{% endalert %}

{: start="4"}
4. After installing the Braze app, you’ll be redirected to Braze to confirm the workspace you want to connect to Shopify. A Shopify store can connect to only one workspace. If you need to switch, select the correct workspace.<br><br>![A window asking you to confirm that you’re in the right workspace.][2]

{: start="5"}
5. Configure your integration.<br><br>![Integration settings page with a button to configure your integration.][12]

## Step 2: Enable Braze Web SDKs

For Shopify online stores, you can select the standard setup to automatically implement the Braze Web SDK and JavaScript SDK.

![“Enable Web SDK” step with options to implement through a standard setup or custom setup.][3]

After you select the standard setup onboarding path, you’ll need to choose when Braze should initialize and load the SDKs from one of the following options: 
- Upon site visit, such as session start
    - Tracks both identified and anonymous users
- Upon account signup, such as account login
    - Track only identified users
    - Starts tracking data when site visitors sign up or log into their accounts

The Braze Web SDK and JavaScript SDK versions will automatically be set to v5.3.0.

## Step 3: Configure your Shopify data

### Standard data setup

Now you’ll select the Shopify data you want to track.

![“Enable Web SDK” step with a checkbox to track behavioral events and user attributes.][6]

The following events will be enabled by default in the standard integration.

| Braze recommended events | Shopify custom events | Shopify custom attributes |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Product viewed</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 }

For more information on the data tracked through the integration, see [Shopify Data]({{site.baseurl}}/shopify_features#shopify-data).

### Historical backfill setup

Through the standard setup, you have the option to perform an initial load of your Shopify customers and orders from the last 90 days prior to your Shopify integration connection. To do so, select the checkbox to include the initial data load as part of your integration. 

![Historical data backfill toggle.][4]

This table contains the data that will be initially loaded through the backfill.

| Braze recommended events | Shopify custom events | Braze standard attributes | Braze subscription statuses |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li></ul>{:/} | {::nomarkdown}<ul><li>Email marketing subscriptions associated with this Shopify store</li><li>SMS marketing subscriptions associated with this Shopify store</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

As your Shopify customer records are loaded into Braze, the Shopify customer ID will be used as the Braze external ID. 

{% alert note %}
If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify historical backfill]({{site.baseurl}}/shopify_features#historical-backfill) for more details. 
{% endalert %}

### (Advanced) Custom data tracking setup

With the Braze SDKs, you can track custom events or custom attributes that go beyond standard events for this integration. Custom events capture unique interactions in your store, such as:

| Custom events | Custom attributes |
| --- | --- |
| {::nomarkdown}<ul><li>Using a custom discount code</li><li>Interacting with a personalized product recommendation</li></ul>{:/} | {::nomarkdown}<ul><li>Favorite brands or products</li><li>Preferred shopping categories</li><li>Membership or loyalty status</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Tracking custom data helps you gain deeper insights into user behavior and personalize their experience even further. To implement custom events, you’ll need to edit your [storefront's theme code](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in the `theme.liquid` file. You may need help from your developers.

For example, the following JavaScript snippet tracks if the current user subscribes to a newsletter, and logs that as a custom event on their profile in Braze:

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

The SDK must be initialized (listening for activity) on a user's device to log events or custom attributes. To learn more about logging custom data, refer to [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) and [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Step 4: Configure how you manage users

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

![“Collect subscribers” section to select if you want to collect email or SMS subscribers or both.][10]

## Step 5: Sync products (optional)

You can optionally sync your products in near real-time from your Shopify store into a Braze catalog, automating the process to bring in product data for deeper personalization of your messages. To learn more, check out [Shopify product sync]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/).

![Step 4 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".][11]{: style="max-width:70%;"}

## Step 6: Activate Channels

{% alert note %}
At this time, we don’t support in-app messages in our standard integration.
{% endalert %}

## Step 6: Finish setup

1. After you configure your setup, select **Finish Setup**.
2. Enable the Braze app embed within your Shopify theme settings. Select **Open Shopify** to be redirected to your Shopify account to enable the app embed within your store’s theme settings. 

![Banner that says you need to active the Braze app embed in Shopify and contains a button to open Shopify.][7]

{: start="3"}
3. After you enable the app embed, your setup is complete!
Confirm you can view your integration settings, the status of initial data sync, and your active Shopify events. ![Shopify partner page displaying the integration settings.][8]

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/tracking_shopify_data1.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}