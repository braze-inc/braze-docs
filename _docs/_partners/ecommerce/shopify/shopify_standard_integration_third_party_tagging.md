---
nav_title: Shopify Standard Integration with Third-Party Tagging
article_title: "Shopify Standard Integration with Third-Party Tagging"
description: "This reference article outlines how to set up the standard Shopify integration withn a third-party tagging tool."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Shopify standard integration with third-party tagging tool

> This page guides you through using third-party tools, like Google Tag Manager, with the [Shopify standard integration]({{site.baseurl}}/shopify_standard_integration/) to initialize and load the Braze Web SDK.

For Shopify online stores, we recommend using Braze's standard integration method to support the Braze SDKs on your site. However, we understand that you may prefer to use a third-party tool, like Google Tag Manager. If you choose to use a third-party tool with Braze's Shopify connector, keep in mind that the Braze integration and app embed will manage the SDK during the checkout process.

## Requirements

- **Consistent API key between your third-party tool and the Shopify connector:** The API key must be consistent across both Braze and your third-party tool. This prevents the creation of duplicate users and maintains compatibility across SDKs. 
  - **API key location:** After onboarding the standard integration path, the integration will automatically create a Braze web app named “Shopify”. Retrieve the API key within the integration that is used with your third-party tool configuration. 
- **Consistent SDK versions between your third-party tool and the Shopify connector:** The SDK version must be `5.4` within your third-party tool. Using an incorrect version number can cause incompatibility issues, as some SDK methods may not exist in older versions.
- **Consistent SDK initialization timing:** Within your Shopify standard integration settings, you can select the SDKs to initialize upon either session start or when an account login occurs. This setting should be consistent between your third-party tool and Braze. Inconsistencies could lead to downstream issues for the user and data syncing. 

{% alert note %}
We recommend using the standard integration method exclusively rather than using it in tandem with third-party tag managers, which may cause conflicts between the Braze SDK and third-party tools. If you do use a third-party tool, test to confirm that everything works as expected. 
{% endalert %}

## Setting up the integration with a third-party tool

Straying from the provided steps may lead to unexpected issues, so be sure to follow them closely.

1. Follow the provided steps in [Shopify standard integration setup]({{site.baseurl}}/shopify_standard_integration/). While [enabling Braze Web SDKs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks), check the box indicating that you're using a third-party tool to add the Braze Web SDK to your Shopify site.

!["Braze SDK settings" section with a checkbox to indicate that you'll use a third-party tool to add the Braze Web SDK.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2. Go to **Settings** > **App Settings**, select the **Shopify** web app, and then copy the **API key for Shopify on Web**.
3. Paste the API key into your third-party tool's web SDK configuration and set the SDK version to `5.4`.

## Capturing Shopify data and syncing users

As long as the Web SDK is accessible on the front-end of your Shopify site through a third-party tool, the standard integration will capture Shopify data and sync users as expected.

## Considerations and disclaimers

- **Initialization settings:** If you modify your initialization settings through your third-party tool, user and data syncing may be impacted. For example, if you choose to initialize your SDK when a cookie consent form is accepted, Braze won't receive tracking for anonymous users or data until the user consents. 
- **Setting attributes directly through `dataLayer` isn't supported:** Use `window.braze` instead of `dataLayer` to set attributes.
- **Potential duplicate users:** If the API key doesn't match across Braze and your third-party tool, duplicate users may be created.
- **SDK incompatibility:** Using an incorrect version number can cause issues with SDK methods.