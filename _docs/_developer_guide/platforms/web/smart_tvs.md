---
nav_title: Smart TV support
article_title: Smart TV support for the Web Braze SDK
platform: Web
page_order: 30
description: "This article covers how to use the Braze Web SDK to integrate with Smart TVs (Samsung and LG)."

---

# Smart TV support

> The Braze Web SDK lets you collect analytics and display rich in-app messages and Content Card messages to Smart TV users, including [Samsung Tizen TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) and [LG TVs (webOS)](https://webostv.developer.lge.com/discover). This article covers how to use the Braze Web SDK to integrate with Smart TVs.

{% alert tip %}
For a complete technical reference, check out our [JavaScript Documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) or our [sample apps](https://github.com/Appboy/smart-tv-sample-apps) to see the Web SDK running on a TV.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Configuring the Web Braze SDK

There are two changes required when integrating with Smart TVs:

1. When downloading or importing the Web SDK, be sure to use the "core" bundle (available at `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, where `x.y` is the desired version). We recommend using the CDN version of our Web SDK, since the NPM version is written in native ES modules whereas the CDN version is transpiled down to ES5. If you prefer to use the [NPM version](https://www.npmjs.com/package/@braze/web-sdk), ensure you are using a bundler such as webpack that will remove unused code and that the code is transpiled down to ES5.
2. When initializing the Web SDK, you must set the `disablePushTokenMaintenance` and `manageServiceWorkerExternally` initialization options to `true`.

## Analytics

All of the same Web SDK methods for analytics can be used on Smart TVs. For a a full-walkthrough for tracking custom events, custom attributes, and more, see [Analytics]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

## In-app messages and Content Cards

The Braze Web SDK supports both [in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web) and [Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) on Smart TVs. Note that you must use the ["Core" Web SDK](https://www.npmjs.com/package/@braze/web-sdk) as rendering in-app messages and Content Cards is not supported using our standard UI display and should instead be customized by your app to fit into your TV App's experience.

For more information on how your Smart TV App can receive and display in-app messages, see [Triggering messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).
