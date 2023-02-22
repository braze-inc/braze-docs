---
nav_title: Safari Mobile Web Push
article_title: Safari Mobile Web Push
platform: Web
channel: push
page_order: 5
page_type: reference
description: "Learn how to integrate web push on your iOS and iPad Safari browsers."
search_rank: 3
---

# Web Push on Safari Mobile (iOS and iPadOS)

[Safari v16.4][safari-release-notes] adds support for mobile web push, which means you can now re-engage mobile users with Push Notifications on iOS and iPadOS.

This article will guide you through the steps required to set up mobile push for safari.

## Integration

First, please read and follow our standard [web push integration guide][web-push-integration]. The following steps are only required to support web push on Safari for iOS and iPadOS support.

### Manifest File

A [Web Application Manifest][manifest-file] is a JSON file that controls how your website is presented when installed to a user's home screen.

For example, you can set the background theme color and icon that the [App Switcher][app-switcher] uses, whether it renders as full screen to resemble a native app, or whether the app should open in landscape or portrait mode.

Create a new `manifest.json` file in your website's root directory, with the following mandatory fields. The full list of supported fields can be found [here][https://developer.mozilla.org/en-US/docs/Web/Manifest].

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

Next, add the following `<link>` tag to your website's HTML pointing to where your manifest file is hosted.

```html
<link rel="manifest" href="/manifest.json" />
```

### Service Worker

Your website must have a Service Worker file that imports the Braze service-worker library, as described in our [web push integration guide][service-worker].

### Add To Homescreen

Unlike major browsers like Chrome and Firefox, you are not allowed to request push permission on Safari iOS/iPadOS unless your website has been added to the user's homescreen. 

The [Add to Homescreen][add-to-homescreen] feature lets users bookmark your website, adding your icon to their valuable homescreen real estate.

![An iphone showing options to bookmark a website and save to the homescreen][{{site.baseurl}}/assets/img/push_implementation_guide/add-to-homescreen.png]

## Next Steps

Next, follow out standard [web push integration guide][web-push-integration] and send yourself a [test message][test-message] to validate the integration.

[webkit-release-notes]: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
[safari-release-notes]: https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes
[manifest-file]: https://developer.mozilla.org/en-US/docs/Web/Manifest
[app-switcher]: https://support.apple.com/en-us/HT202070
[add-to-homescreen]: https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc
[web-push-integration]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[service-worker]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker
[test-message]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
