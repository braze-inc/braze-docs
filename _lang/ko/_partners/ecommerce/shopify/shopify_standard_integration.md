---
nav_title: Shopify Standard Integration Setup
article_title: "Shopify Standard Integration Setup"
description: "This reference article outlines how to set up the standard Shopify integration."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify standard integration setup

> This page walks you through how to integrate Braze with Shopify using our standard integration for users with a Shopify online store. If you use a Shopify headless site or are looking to implement more tailored solutions, refer to [Shopify custom integration setup]({{site.baseurl}}/shopify_custom_integration/).

## Step 1: Connect your Shopify store

1. In Braze, go to **Partner Integrations** > **Technology Partners** and then search for “Shopify”.

{% alert note %}
If you’re using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

{: start="2"}
2\. On the Shopify partner page, select **Begin setup** to start the integration process.<br><br>![Shopify integration page with button to begin setup.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. In the Shopify app store, install the Braze application.<br><br>![The Braze app store page with a button to install the application.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
If your Shopify account is associated with more than one store, you can change the store you’re logged into by selecting the store icon at the top-right of the page and selecting **Switch stores**.
{% endalert %}

{: start="4"}
4\. After installing the Braze app, you’ll be redirected to Braze to confirm the workspace you want to connect to Shopify. A Shopify store can connect to only one workspace. If you need to switch, select the correct workspace.<br><br>![A window asking you to confirm that you’re in the right workspace.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Select **Begin setup**.<br><br>!["Integration settings" with field to enter domain and a button to begin setup.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Step 2: Enable Braze Web SDKs

For Shopify online stores, you can select the standard setup to automatically implement the Braze Web SDK and JavaScript SDK.

![“Enable Web SDK” step with options to implement through a standard setup or custom setup.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

After you select the standard setup onboarding path, you’ll need to choose when Braze should initialize and load the SDKs from one of the following options: 
- Upon site visit, such as session start
    - Tracks both identified and anonymous users
- Upon account signup, such as account login
    - Track only identified users
    - Starts tracking data when site visitors sign up or log into their accounts

## Step 3: Configure your Shopify data

### Standard data setup

Now you’ll select the Shopify data you want to track.

![“Tracking Shopify data” section with a checkbox to track behavioral events and user attributes.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

The following events will be enabled by default in the standard integration.

| Braze recommended events | Shopify custom events | Shopify custom attributes |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Product viewed</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

For more information on the data tracked through the integration, refer to [Shopify Data Features]({{site.baseurl}}/shopify_data_features/).

### Historical backfill setup

Through the standard setup, you have the option to perform an initial load of your Shopify customers and orders from the last 90 days prior to your Shopify integration connection. To do so, select the checkbox to include the initial data load as part of your integration. 

![Historical data backfill toggle.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

This table contains the data that will be initially loaded through the backfill.

| Braze recommended events | Shopify custom events | Braze standard attributes | Braze subscription statuses |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li></ul>{:/} | {::nomarkdown}<ul><li>Email marketing subscriptions associated with this Shopify store</li><li>SMS marketing subscriptions associated with this Shopify store</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

As your Shopify customer records are loaded into Braze, the Shopify customer ID will be used as the Braze external ID. 

{% alert note %}
If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify data features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) for more details.
{% endalert %}

### (Advanced) Custom data tracking setup

With the Braze SDKs, you can track custom events or custom attributes that go beyond standard events for this integration. Custom events capture unique interactions in your store, such as:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Custom events</th>
      <th style="width: 50%;">Custom attributes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Using a custom discount code</li>
          <li>Interacting with a personalized product recommendation</li>
          <li>Adding a gift message to their order</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Favorite brands or products</li>
          <li>Preferred shopping categories</li>
          <li>Membership or loyalty status</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Tracking custom data helps you gain deeper insights into user behavior and personalize their experience even further. To implement custom events, you need to edit your [storefront's theme code](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in the `theme.liquid` file. You may need help from your developers.

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

Select your `external_id` type from the dropdown. 

![“Collect subscribers” section.]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Using an email address or a hashed email address as your Braze external ID can help simplify identity management across your data sources. However, it's important to consider the potential risks to user privacy and data security.<br><br>

- **Guessable Information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of Exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.
{% endalert %}

If you selected a custom external ID type, proceed to steps 4.1 and 4.2. Otherwise, continue to step 4.3.

### Step 4.1: Create a custom `external_id`

First, go to Shopify and create the `braze.external_id` metafield. We recommend following the steps in [Creating custom metafield descriptions](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions). For **Namespace and key**, enter `braze.external_id`. For **Type**, we recommend you choose an ID type.

After creating the metafield, listen to [`customer/create` webhooks](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) so that you can write the metafield when a new customer is created. Then, use the [Admin API](https://shopify.dev/docs/api/admin-graphql) or [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) to backfill all of your previously created customers with this metafield.

### Step 4.2: Create an endpoint

You need a public GET endpoint to retrieve your external ID. If Shopify can't provide the metafield, Braze will call that endpoint to retrieve the external ID.

An example endpoint is: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

#### Response

Braze expects a `200` status code. Any other code is considered an endpoint failure. The response should be:

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Validate the `shopify_customer_id` and email address by using the Admin API or Customer API to confirm that the parameter values match the customer values in Shopify. After validating, you could also use the APIs to retrieve the `braze.external_id` metafield and return the external ID value.

### Step 4.3: Collect your email or SMS opt-ins from Shopify (optional)

You have the option to collect your email or SMS marketing opt-ins from Shopify. 

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

![“Collect subscribers” section with option to collect email or SMS marketing opt-ins.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
As mentioned in [Shopify overview]({{site.baseurl}}/shopify_overview/), if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your `theme.liquid` file:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Sets the email address on the user profile
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Updates the global email subscription status
{% endalert %}

## Step 5: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. Automatic updates occur in near real-time so your catalog always reflects the latest product details. To learn more, check out [Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Step 4 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Step 6: Activate Channels (optional)

You can enable in-app messages without using a developer by configuring them in your setup.

![Setup step to activate channels, with the available option being in-browser messaging.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. This information is then sent to Shopify. This data helps merchants recognize visitors to their store and create a more personalized shopping experience. For more details, refer to [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Supporting additional SDK channels

The Braze SDKs enable various messaging channels, including Content Cards.

#### Content Cards and Feature Flags

To add content cards or feature flags, you will need to collaborate with your developers to insert the necessary SDK code directly into your `theme.liquid` file. For detailed instructions, refer to [Integrating the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Web push notifications

Web push currently isn't supported for the Shopify integration. If you want to see this supported in the future, submit a product request through the [Braze product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

If you wish to see this supported in the future, submit a product request through the Braze [product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Step 7: Finish setup

1. After you configure your setup, select **Finish Setup**.
2. Enable the Braze app embed within your Shopify theme settings. Select **Open Shopify** to be redirected to your Shopify account to enable the app embed within your store’s theme settings. 

![Banner that says you need to active the Braze app embed in Shopify and contains a button to open Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. After you enable the app embed, your setup is complete!
Confirm you can view your integration settings, the status of initial data sync, and your active Shopify events. <br><br>![Shopify partner page displaying the integration settings.]({% image_buster /assets/img/Shopify/install_complete.png %})