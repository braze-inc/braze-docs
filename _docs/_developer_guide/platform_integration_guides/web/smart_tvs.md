---
nav_title: Smart TV Integrations
article_title: Smart TV Integration for Web
platform: Web
page_order: 20
description: "This article covers how to use the Braze Web SDK to integrate with Smart TVs (Samsung and LG)."

---

# Smart TV integration

The Braze Web SDK lets you collect analytics and display rich in-app messages and Content Card messages to Smart TV users, including [Samsung Tizen TVs][1] and [LG TVs (webOS)][2].

For a complete technical reference, check out our [Javascript Documentation][3] or our [sample apps][9] to see the Web SDK running on a TV.

## Install the Braze SDK

To get started, follow our [Initial SDK setup][4] guide for the Web SDK.

There are two changes required when integrating with Smart TVs:

1. When downloading or importing the Web SDK, be sure to use the ["core" bundle][6].
2. When initializing the Web SDK, you must set the `disablePushTokenMaintenance` and `manageServiceWorkerExternally` initialization options to `true`.

## Analytics

All of the same Web SDK methods for analytics can be used on Smart TVs.

For a complete guide to tracking custom events, custom attributes, and more, read our [Analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/) documentation.

## In-app messages and Content Cards

Braze's Web SDK supports both [in-app messages][7] and [Content Cards][8] on Smart TVs. Note that you must use the ["Core" Web SDK][6] as rendering in-app messages and Content Cards is not supported using our standard UI display and should instead be customized by your app to fit into your TV App's experience.

Visit [Manual in-app message display][5] for more information on how your Smart TV App can receive and display in-app messages.


[1]: https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html
[2]: http://webostv.developer.lge.com/discover/discover-webos-tv/
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display
[6]: https://www.npmjs.com/package/@braze/web-sdk-core
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/
[9]: https://github.com/Appboy/smart-tv-sample-apps
