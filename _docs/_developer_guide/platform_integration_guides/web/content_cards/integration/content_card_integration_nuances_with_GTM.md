---
nav_title: Integration Nuances with GTM
article_title: Content Card Nuances for Web with GTM
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "This article covers nuances on integrating Content Card for Web if you implemented the Braze Web SDK using Google Tab Manager."
---

# Content Card nuances for Web with GTM

If you implemented the Braze Web SDK using [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/) (GTM), there are some nuances you need to be aware of when integrating Content Cards.

Google Tag Manager works by injecting the [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (a version of our Web SDK) directly into your website code, which means that all SDK methods are available just as if you had integrated the SDK without GTM. The only difference is when implementing Content Cards.

## What you need to know

### Telling GTM where to display the feed

For both a standard and custom feed implementation, you need to specify where GTM should display Content Cards in your website. To do so, add a `<div>` element in which you tell Braze to show the Content Card feed. See [Content Card integration]({{site.baseurl}}s/developer_guide/platform_integration_guides/web/content_cards/integration#content-card-integration-1) for details.

### Standard feed UI

When implementing the [standard feed UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), Braze methods must have `window.` added to the start of the method. For example, `braze.showContentCards` should instead be `window.braze.showContentCards`. 

### Custom feed UI

For custom feed styling, the steps are the same as if you had integrated the SDK without GTM. Unlike the standard feed UI, with a custom UI you are overwriting the CSS file, so you don't need to prepend `window.` to Braze methods. For example, if you want to customize the width of the Content Card feed, you can paste the following into your CSS file:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

See [Custom styling](((site.baseurl))/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling) for details.

The exception is if you want to manually [refresh the feed]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui#refreshing-the-feed), in which case use `window.braze.requestContentCardsRefresh();`.