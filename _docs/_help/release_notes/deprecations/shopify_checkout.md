---
nav_title: Shopify checkout46liquid
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

You will no longer be able to add custom SDK code snippets to the information, shipping, or payment pages in `checkout.liquid`. Instead, you'll need to add custom SDK code snippets to the thank you or order status pages. This allows you to reconcile users that completed checkout.
1. Load the Braze web SDK on the thank you and order status pages.
2. Retrieve the email from the user.
3. Call `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. On Braze, merge the user profiles on email.

If you encounter duplicate user profiles, you can use our [bulk merging tool]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) to help streamline your data. 
