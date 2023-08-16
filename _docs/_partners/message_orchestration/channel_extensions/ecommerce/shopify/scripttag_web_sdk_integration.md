---
nav_title: Web SDK Integration via Shopify ScriptTag
article_title: "Web SDK Integration via Shopify ScriptTag"
description: "This reference article outlines how to integrate the Web SDK via Shopify ScriptTag. "
page_type: partner
search_tag: Partner
alias: "/scripttag_web_sdk_integration/"
page_order: 1
---

# Web SDK integration via Shopify ScriptTag

> [Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) is a remote JavaScript code loaded into the pages of your store or the order status page of checkout. When a store page is loaded, Shopify will check to see if any script tags need to be loaded to the site page. Within the process, the Braze Web SDK scripts will be loaded onto your Shopify store site directly.

## Prerequisites

Confirm with your development team that the following is supported within your Shopify store setup. If any of the following is not supported in your Shopify store, the Braze Web SDK via Shopify ScriptTag cannot be supported.

| Requirement | Description |
| ----------- | ----------- |
| [Shopify Ajax API](https://shopify.dev/api/ajax) | Possible use of the Ajax API includes:<br>- Add products to the cart and update the cart item counter.<br>- Display related product recommendations.<br>- Suggest products and collections to visitors as they type in a search field.<br><br>Braze requires the Ajax API as we will fetch product information for your product events. |
| [Cart token management by Shopify](https://shopify.dev/api/examples/cart) | A cart contains merchandise that a customer intends to purchase and the estimated cost associated with the cart. You can use the [Storefront API](https://shopify.dev/api/storefront) to interact with a cart during a customer's session. <br><br>Braze requires cart token management through Shopify directly and not a 3rd party system to fetch the cart token ID for abandoned cart events. |
| URL management by Shopify | Your store will need to follow the structured Shopify URL pathing, where each of the paths for collections or products follows one of the following:<br>- /collections/collectionA<br>- /collections/collectionA/products/productA<br>- /products/productB |
| Fetch API calls | Stores should be using Shopify's recommended and newer method of calling the API (Fetch). Stores making calls using the older method (XHR) will result in abandoned cart events not registering at all and user reconciliation not properly working. |
{: .reset-td-br-1 .reset-td-br-2}

## What is the Braze Web SDK?

The [Braze Web SDK]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/) is a powerful tool used to track the behavior of your Shopify store customers. With the Web SDK, you can collect session data, identify users, and record user behavior data from a web or mobile browser. In addition, you can unlock native messaging channels like in-browser messages to ensure you're providing the right message, to the right user, on the right channel.

Review the following Web SDK details with your developers to prevent issues during the integration process.

### Braze Web SDK initialization

Initializing the Web SDK upon session start will be required. Braze will need to collect the `device_id` for tracking anonymous user data as other identifiers like the Shopify customer ID, email, or phone number may not be readily available for guest visitors of your Shopify store.

The `device_id` will also be used to reconcile user data to the anonymous user profile as a customer provides more identifiable information (i.e., email or phone number) during and after the checkout process.

### Braze Web SDK version

The current version of the Braze Web SDK via Shopify ScriptTag integration is v4.0.

If you have the Web SDK already installed onto your Shopify store, see the [following section](#existing) to see how you might be impacted.

### Monthly active users

The Web SDK tracks sessions of your Shopify customers and guests. As a result, this will accrue as monthly active users (MAU) within your Braze dashboard reporting and towards your MAU allotments. It is important to note that anonymous users will also count toward your MAU. For mobile devices, anonymous users are device-dependent. For web users, anonymous users are browser cache dependent. 

### User data
You have the option to include the following events that will require the Web SDK:
- Product viewed
- Product clicked
- Abandoned cart

At this time, you will not be able to customize the Shopify scripts to include more event and attribute tracking.

{% alert note %}
If you do want to add more customization to the Braze Web SDK implementation via Shopify ScriptTag, you will need to engage with your development team to directly integrate with the Shopify ScriptTag API.
{% endalert %}

## How does the Braze Web SDK get installed on my Shopify store?

#### No pre-existing Web SDK implementation

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) is a remote JavaScript code loaded into the pages of your store or the order status page of checkout. When a store page is loaded, Shopify will check to see if any script tags need to be loaded to the site page. Within the process, the Braze Web SDK scripts will be loaded onto your Shopify store site directly.

From the event selector within the Shopify setup wizard, the events denoted with an asterisk (&#42;) are supported by the Web SDK. If you select these events or include in-browser messaging, Braze will determine that the Web SDK implementation via Shopify ScriptTag will be added to your Shopify store as part of your setup.

After you install Braze's Shopify app, you'll be redirected back into Braze. After the app is successfully installed, you'll see the Shopify configuration page.

#### What if I already have the Web SDK or Google Tag Manager enabled on my Shopify store? {#existing}

If you already have the Web SDK installed on your Shopify store, you can still proceed with setting up the Shopify ScriptTag within the onboarding process. During the installation process, Braze will check if there are instances of the Web SDK already available on your Shopify store. 

We'll then add the necessary scripts to make sure you can track the selected events or enable in-browser messaging. 

It is important to review your existing Web SDK integration for the following items:
- Web SDK version should be v4.0+
- Web SDK initializes upon session start

If the above items are not met, then the Web SDK integration via Shopify ScriptTag will not be supportable.

#### What if I use a customer data platform like Segment or mParticle?

Confirm that you have disabled Shopify events you may have been sending through your customer data platform.

