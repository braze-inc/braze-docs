---
nav_title: Shopify checkout&#46;liquid
page_order: 7
description: "This article explains the deprecation of Shopify checkout&#46;liquid, including the impact to your Shopify integration and guidance for developers."
page_type: update

---

# Shopify checkout&#46;liquid deprecation

Shopify has informed all merchants about the deprecation of `checkout.liquid`, and the migration to [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), a new foundation for building customized checkout experiences. 

Shopify will deprecate `checkout.liquid` in two phases:

1. **[August 13, 2024](#phase-one-august-13-2024):** Deadline to upgrade your information, shipping, and payment pages.
2. **[August 28, 2025](#phase-two-august-28-2025):** Deadline to upgrade your thank you and order status pages, including your apps using script tags and additional scripts.

For general information on upgrading to Checkout Extensibilty, see [Shopify's upgrade guide](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Impact to your integration

The Braze and Shopify integration uses [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) to load the Braze Web SDK for non-headless sites. We are planning to launch a new version of the integration before the 2025 deadline to support all customers before `checkout.liquid` is fully deprecated. 

For the upcoming changes on August 13, 2024, check the details below to see if you will be impacted by your development team.

### Phase one: August 13, 2024

The default Braze and Shopify integration doesn't use the information, shipping, and payment pages within the checkout experience. As a result, the default integration will not be impacted. 

#### Shopify Plus

For Shopify Plus customers, any custom SDK code snippets that modify `checkout.liquid` for the information, shipping, or payment pages will become inactive after this date. For example, custom code that logs events from these pages will no longer work. If you have custom SDK code, view our [developer guidance](#developer-guidance) for migration.

#### Non-Shopify Plus

For non-Shopify Plus customers, if you need to customize the information, payment, and shipping pages you [need to upgrade to Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) and then follow the [developer guidance](#developer-guidance).

### Phase two: August 28, 2025

Shopify will deprecate support for [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) on `checkout.liquid` pages, which are used in the integration. In response, we are actively building a new version of the Shopify integration which we plan to release well in advance of the August 2025 deadline. Stay tuned for more information from the Braze product team. 

## Developer guidance

This guidance applies to Shopify Plus customers who have added custom SDK code snippets to the information, shipping, or payment pages in `checkout.liquid`. If you haven't made these customizations, you can disregard this guidance.

### Guidance for Shopify 2.0 theme stores (such as Liquid)

When migrating to Checkout Extensibility, follow these steps to maintain usage of Braze during checkout.

1. Set up the Braze web SDK on the storefront pages.
  - Create a [theme app extension](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) to turn on in the storefront.
  - Create an [app embed block](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#app-embed-blocks).
  - Load and initailize the Braze SDK with [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=google%20tag%20manager) or [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=braze%20cdn).

2. Retrieve the `deviceID` from the Braze web SDK.

3. Publish custom events from the theme app extension with the Braze `deviceID` in the payload.

{% raw %}
```java
// After initializing the Braze WebSDK
let event_data = {
	device_id: braze.getDeviceId()
}
Shopify.analytics.publish("custom_event", event_data);
```
{% endraw %}

{: start="4"}
4. Create a [web pixel](https://shopify.dev/docs/apps/build/marketing-analytics/build-web-pixels) and load it in checkout.

5. Subscribe to `custom_event` and save the Braze `deviceID` as a cookie.

6. Send a request to the Braze SDK or REST API depending on your use case.
  - Send requests to a proxy URL that will call server-side code to call the Braze REST API.
  - Fetch the `shopify/email_user_reconcile` endpoint and supply the URL parameter with the `deviceId` and `email`.

{% raw %}
```java
register(({analytics, browser, settings, init}) => {

  // subscribe to the custom events
  analytics.subscribe("custom_event", (event) => {
    // save braze deviceId in cookie
    browser.cookie.set('device_id', event.device_id);
  });

  // reconcile user by email after user enters contact info
  analytics.subscribe('checkout_contact_info_submitted', (event) => {
    // retrieve email from checkout
    const checkout = event.data.checkout;
    const email = checkout.email;

    // retrieve deviceId from cookies
    const deviceId = browser.cookie.get('device_id')

    fetch(
      'https://'
        + SDK_URL
        + `/api/v3/shopify/email_user_reconcile`
        + `?email=${encodeURIComponent(email)}`
        + `&device_id=${deviceId}`
        + `&api_key=${API_KEY}`
        + `&shop=${SHOP_DOMAIN}`,
      {method: 'POST'}
    ).then(response => {
      console.log(`Successfully reconciled email ${email} with device ID ${deviceId}`);
    }).catch(error => {
      console.error('There was a problem with the operation:', error);
    });
  });
});
```
{% endraw %}

### Guidance for Shopify hydrogen (headless) 

When migrating to Checkout Extensibility, follow these steps to maintain usage of Braze during checkout.

1. Set the checkout page as a subdomain of the main storefront.
  - For example, if your hydrogen store is hosted at `myshop.com`, the checkout must be on `checkout.myshop.com` or similar.

2. Set up the Braze web SDK on the storefront pages.
  - Load and initialize the Braze SDK via [NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-1-install-the-braze-library).

3. Retrieve the `deviceID` from the Braze web SDK.

4. Create a first-party cookie and set the value as the Braze `deviceID`.

{% raw %}
```java
const SHOP_DOMAIN = "SHOP_DOMAIN"; // shopify shop domain

// Set first party cookie to hold Braze deviceId on shop domain
document.cookie = "device_id={{ braze.getDeviceId() }}; domain={{ SHOP_DOMAIN }}; path=/";
```
{% endraw %}

{: start="5"}
5. Create a [web pixel](https://shopify.dev/docs/apps/marketing/pixels/getting-started) and load it in checkout.

6. Subscribe to checkout events and retireve the Braze `deviceID` from the first-party cookie.

7. Send a request to the Braze SDK or REST API depending on your use case:
  - Send requests to a proxy URL that will call server-side code to call the Braze REST API.
  - Fetch the `shopify/email_user_reconcile` endpoint and supply the URL parameter with the `deviceId` and `email`.

{% raw %}
```java
register(({analytics, browser, settings, init}) => {

  // reconcile user by email after user enters contact info
  analytics.subscribe('checkout_contact_info_submitted', (event) => {
    // retrieve email from checkout
    const checkout = event.data.checkout;
    const email = checkout.email;

    // retrieve deviceId from cookies
    const deviceId = browser.cookie.get('device_id')

    fetch(
      'https://'
        + SDK_URL
        + `/api/v3/shopify/email_user_reconcile`
        + `?email=${encodeURIComponent(email)}`
        + `&device_id=${deviceId}`
        + `&api_key=${API_KEY}`
        + `&shop=${SHOP_DOMAIN}`,
      {method: 'POST'}
    ).then(response => {
      console.log(`Successfully reconciled email ${email} with device ID ${deviceId}`);
    }).catch(error => {
      console.error('There was a problem with the operation:', error);
    });
  });
});
```
{% endraw %}
