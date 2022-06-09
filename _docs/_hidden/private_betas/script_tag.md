---
nav_title: Setting up Shopify
article_title: "Setting up Shopify"
description: "This article outlines how to set up Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze."
page_type: partner
search_tag: Partner
permalink: "/setting_up_shopify/"
hidden: true

---

# Setting up Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere. 

The Shopify and Braze integration allows brands to connect their Shopify store seamlessly to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging to nudge customers to complete their purchase or retarget users based on their previous purchases. 

## Prerequisites

All Braze customers looking to utilize the Shopify integration must sign Braze's Shopify order form. Reach out to your account executive for more details.

This integration will create alias user profiles if we are unable to match Shopify data using the email or phone number ([see here for more details on Shopify user reconciliation](#shopify-user-syncing)). Consult with your development teams around the downstream impacts and need to merge these user profiles as part of your user lifecycle before you enable the integration. 

| Requirement | Description |
| ----------- | ----------- |
| Shopify store | You must have an active [Shopify](https://www.shopify.com) store.<br><br>Note that at this time, you are only able to connect one Shopify store per app group. |
| Event property segmentation enabled | To ensure you can segment your Shopify events properties, you must work with your customer success manager or [Braze support]({{site.baseurl}}/braze_support/) to confirm that you have event property segmentation enabled for your dashboard. |
| Nested custom attribute support | This will be enabled with the Spotify integration.<br><br>You will be given access to this feature to receive Shopify marketing opt-in custom attributes. |
{: .reset-td-br-1 .reset-td-br-2}

## What's supported in the integration?

- Integrating the Braze Web SDK via Shopify ScriptTag
- Shopify user data syncing into Braze
- Ability to orchestrate the following multi-channel eCommerce user cases:
   - Path to purchase user journeys
   - Abandoned cart and checkout user journeys
   - Post-purchase retargeting
   - Transactional messaging

## Integration

The types of Shopify use cases you intend on supporting will determine the integration path you will set up within the onboarding process in the Braze dashboard.

<style>
    table {
        table-layout: fixed;
        width: 100%;
    }
    table td {
    word-break: break-word;
    }
</style>

| Use case | Integration method |
| -------- | ------------------ |
| Retarget customers as they start their path to purchase. You can retarget using the following top-of-funnel eCommerce events:<br>   • Product clicked<br>   • Product viewed<br>   • Abandoned cart | Braze Web SDK via Shopify ScriptTag |
| Support abandoned checkout, purchase, and post-purchase targeting:<br>   • Abandoned checkout<br>   • Order created<br>   • Braze purchase event | Shopify webhooks |
| Support transactional marketing messaging:<br>   • Order paid<br>   • Order fulfillment<br>   • Partial order fulfilment<br>   • Order cancellation<br>   • Order refund | Shopify webhooks |
|Anonymous user tracking | Braze Web SDK via Shopify ScriptTag |
| Channel support:<br>   • In-browser messaging | Braze Web SDK via Shopify ScriptTag |

### Step 1: Locate Shopify within the dashboard
In Braze, go to the **Technology Partners** section and then search **Shopify**. On the Shopify partner page, select **Begin Setup** to start the integration process.

![Data Import and Web SDK Installation section of the Shopify partner page in Braze.][2]{: style="max-width:80%;"}

### Step 2: Shopify set up
![][3]{: style="float:right;max-width:30%;margin-top:15px;"} 

As you go through the onboarding process, you will be expected to:
1. Connect your Shopify store name
2. Select Shopify events
3. Enable a Braze channel
4. Installation of the Braze app into your storefront
<br><br>

#### Connect Shopify store name

When you click **Begin Setup**, you'll be prompted to input your **Shopify Store Name**. Ensure that you input your store name, not the [Shopify domain](https://help.shopify.com/en/manual/domains).

![][6]{: style="max-width:65%;"} 

#### Web SDK

In the next step of the setup wizard, you'll be presented with information about the Braze Web SDK. The Braze Web SDK can be integrated via Shopify ScriptTag to unlock the following functionality:
- 1-click Braze Web SDK integration onto your Shopify store
- Anonymous user tracking
- Out-of-the-box tracking for top-of-funnel eCommerce events:
  - Product viewed
  - Product clicked
  - Abandoned cart
- Option to enable in-browser messaging

![][4]{: style="max-width:65%;"} 

Keep in mind that when you enable the Braze Web SDK, it will begin tracking monthly active users, and the user data collected will count towards your data consumption.

For a deeper understanding of the Braze Web SDK integration via Shopify ScriptTag, review []().

For more general information about Braze's Web SDK, visit our [Web SDK overview]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/).

#### Select Shopify events

Next, you'll be able to select which Shopify events you wish to integrate with Braze.

For the events denoted with an asterisk (&#42;), you will be required to integrate with the Braze Web SDK to track these events.

![][7]{: style="max-width:65%;"} 

#### In-browser messages (optional)

Once you have selected and confirmed which Shopify events to collect, you'll have the option to include in-browser messages as part of your integration. In-browser messages allow brands to deliver rich content within their Shopify store to promote deals, collect email and SMS opt-ins, and so much more. To learn more, go to our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/#potential-use-cases).

![][5]{: style="max-width:65%;"} 

#### Install Braze app in your storefront

After you select your Shopify events and channels, you can confirm your integration settings within the setup wizard. Once confirmed, select **Go to Shopify** to install Braze's Shopify app. Once you select **Install App**, you will be redirected back to Braze to complete the app installation and display your integration settings.

![][8]{: style="max-width:85%;"} 














# Braze Web SDK integration via Shopify ScriptTag

## Prerequisites


## What is the Web SDK?
The Web SDK is a powerful tool used to track the behavior of your Shopify store customers. With the Web SDK, you can collect session data, identify users, and record user behavior data via a web/mobile browser. In addition, you can unlock native messaging channels like in-browser messages to ensure you're providing the right message, to the right user, on the right channel.

For more information about the Web SDK, see [here]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/).

## What will the Web SDK on my Shopify store support?

The Braze Web SDK on your Shopify store will support tracking the following:
- [Anonymous user tracking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) to track guest activity in your store
- [Monthly active user]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/#monthly-active-users) tracking as the Web SDK is capable of tracking session data from your store visitors
- Option to collect Shopify [user data]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection) which will count toward your [data point]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points) consumption
   - To see what user data can be tracked, please refer to [user data section]
- Option to enable [in-browser messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) as a channel on your Shopify store.

## Integration

Please review the following Web SDK details with your developers to prevent any issues during the integration process.

### Braze Web SDK initialization

Initializing the Web SDK upon session start will be required. Braze will need to collect the `device_id` for tracking anonymous user data as other identifiers like the Shopify customer ID, email, or phone number may not be readily available for guest visitors of your Shopify store.

The `device_id` will also be used to reconcile user data to the anonymous user profile as a customer provides more identifiable information (i.e., email or phone number) during and after the checkout process.

### Braze Web SDK version

The current version of the Braze Web SDK via Shopify ScriptTag integration is v4.0.

If you have the Web SDK already installed onto your Shopify store, please see [this section]() to see how you might be impacted.

### Monthly active users

The Web SDK tracks sessions of your Shopify customers and guests. As a result, this will accrue as monthly active users (MAU) within your Braze dashboard reporting and towards your MAU allotments. It is important to note that anonymous users will also count toward your MAU. For mobile devices, anonymous users are device-dependent. For web users, anonymous users are browser cache dependent. 

### User data
You have the option to include the following events that will require the Web SDK:
- Product viewed
- Product clicked
- Abandoned cart

At this time, you will not be able to customize the Shopify scripts to include more event and attribute tracking.

## How does the Braze Web SDK get installed onto my Shopify store?

### No pre-existing Web SDK implementation
[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) is a remote JavaScript code loaded into the pages of your store or the order status page of checkout. When a store page is loaded, Shopify will check to see if any script tags need to be loaded to the site page. Within the process, the Braze Web SDK scripts will be loaded onto your Shopify store site directly.

From the event selector within the Shopify setup wizard, the events denoted with an asterisk (&#42;) are supported by the Web SDK. If you select these events and/or include in-browser messaging, Braze will determine that the Web SDK implementation via Shopify ScriptTag will be added to your Shopify store as part of your setup.

After you install Braze's Shopify app, you'll be redirected back into Braze. Once successfully installed, you'll then see the Shopify configuration page.

### What if I already have the Web SDK or Google Tag Manager enabled on my Shopify store?

If you already have the Web SDK installed on your Shopify store, you can still proceed with setting up the Shopify ScriptTag within the onboarding process. During the installation process, Braze will check if there are instances of the Web SDK already available on your Shopify store. 

We'll then add the necessary scripts to ensure you can track the selected events or enable in-browser messaging. 

It is important to review your existing Web SDK integration for the following items:
- Web SDK version should be v4.0+
- Web SDK initializes upon session start

If the above items are not met, then the Web SDK integration via Shopify ScriptTag will not be supportable.

### What if I use a Customer Data Platform like Segment or mParticle?












## Shopify advanced settings

### Update abandoned cart delay
By default, Braze will automatically set the delay to trigger the `shopify_abandoned_cart` event to one hour of inactivity. You can set the **Abandoned Cart Delay** from 5 minutes to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![Option in Advanced Settings to set a rule for how long after a user leaves their cart to trigger abandoned cart.][11]{: style="max-width:40%;"}

### Update abandoned checkout delay

By default, Braze will automatically set the delay to trigger the `shopify_abandoned_checkout` event to one hour of inactivity. You can set the **Abandoned Checkout Delay** from 5 minutes up to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![Option in Advanced Settings to set a rule for how long after a user leaves their cart to trigger abandoned checkout.][11]{: style="max-width:40%;"}

### Set your preferred product identifier

If you have included Braze purchase events within your Shopify integration setup, by default, Braze will set the Shopify Product ID as the Product ID used within Braze's purchase event. This will then be used when you filter for products purchased in Y days or when personalizing content in your message using Liquid.

You can also choose to set either the SKU or Product Title from Shopify instead of the Shopify Product ID through advanced settings.

![Option in Advanced Settings to specify a field to use as your product identifier within the Braze purchase event.][12]{: style="max-width:40%;"}










# User reconciliation

## The Web SDK and Shopify webhooks
### Anonymous users
With the Web SDK integration, you will begin tracking sessions for your Shopify customers. If your store visitors are guests (i.e., anonymous), Braze will capture the device_id for that particular customer's session.

As the customer progresses through to checkout and provides additional identifiable information like email or phone number, Braze will capture the relevant Shopify user data via Shopify webhooks.

In this process, Braze will effectively match the user by the same device_id for the same session and merge all of the user data captured from both the Web SDK and Shopify webhooks into a single user profile in Braze.

Braze will also assign the Shopify customer ID as the [user alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) on the user profile.

### Identified users

## Shopify webhooks only
Braze will map the supported Shopify data to user profiles using the customer's email address or phone number. 

### Identified user profiles

- If the email address or phone number is associated with an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) Braze syncs the Shopify data to that user.
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.

### Anonymous users

- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user.
  - For existing alias-only profiles, we'll add the Shopify alias object for that user. 
- If the email address or phone number is not associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object.
  - If these alias-only user eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [users identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 


[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/scripttag1.png %} 
[4]: {% image_buster /assets/img/Shopify/scripttag2.png %} 
[5]: {% image_buster /assets/img/Shopify/scripttag3.png %} 
[6]: {% image_buster /assets/img/Shopify/scripttag4.png %} 
[7]: {% image_buster /assets/img/Shopify/scripttag5.png %} 
[8]: {% image_buster /assets/img/Shopify/scripttag.gif %} 
