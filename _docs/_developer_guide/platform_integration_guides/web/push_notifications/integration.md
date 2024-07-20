---
nav_title: Integration
article_title: Push Integration for Web
platform: Web
channel: push
page_order: 0
page_type: reference
description: "This article describes how to integrate Braze Web push via the Braze SDK."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# Push notification integration

> A push notification is an alert that appears on the user's screen when an important update occurs. Push notifications can be received even when your web page is not currently open in the user's browser. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your site. This reference article covers how to integrate Braze web push with the Braze SDK.

Refer to our [push best practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) for more resources.

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

Web push notifications are implemented using the [W3C push standard](http://www.w3.org/TR/push-api/), which most major browsers support.

For more information on the push protocol standards and browser support, you can review resources from [Apple](https://developer.apple.com/notifications/safari-push-notifications/ "Safari Push Notifications") [Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla Push API browser compatibility") and [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft Push API")

{% multi_lang_include archive/web-v4-rename.md %}

## Integration

### Step 1: Configure your site's service worker

- If you don't already have a service worker, create a new file named `service-worker.js` with the following snippet, and place it in the root directory of your website.
- Otherwise, if your site already registers a service worker, add the following snippet to the service worker file, and set the [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) initialization option to `true` when initializing the Web SDK.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

If your service worker filename is not `service-worker.js`, you must use the `serviceWorkerLocation` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

{% alert important %}
Your web server must return a `Content-Type: application/javascript` when serving your service worker file. 
{% endalert %}

#### What if I can't register a service worker in the root directory?

By default, a service worker can only be used within the same directory it is registered in. For example, if your service worker file exists in `/assets/service-worker.js`, it would only be possible to register it within `example.com/assets/*` or a subdirectory of the `assets` folder, but not on your homepage (`example.com/`). For this reason, it is recommended to host and register the service worker in the root directory (such as `https://example.com/service-worker.js`).

If you cannot register a service worker in your root domain, an alternative approach is to use the [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP header when serving your service worker file. By configuring your server to return `Service-Worker-Allowed: /` in the response for the service worker, this will instruct the browser to broaden the scope and allow it to be used from within a different directory.

#### Can I create a service worker using a Tag Manager?

No, service workers must be hosted on your website's server and can't be loaded via Tag Manager.

### Step 2: Browser registration

For a browser to receive push notifications, you must register it for push by calling `braze.requestPushPermission()`. This will immediately request push permission from the user. 

If you wish to show your own push-related UI to the user before requesting push permission (known as a soft push prompt), you can test to see if push is supported in the user's browser with `braze.isPushSupported()`. Refer to the [soft push prompt example]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) using in-app messages.

If you wish to unsubscribe a user, you can do so by calling `braze.unregisterPush()`.

{% alert important %}
Recent versions of Safari and Firefox require that you call this method from a short-lived event handler (for example, from a button click handler or soft push prompt). This is consistent with [Chrome's user experience best practices](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) for push registration.
{% endalert %}

### Step 3: Configure Safari push (optional) {#safari}

{% alert important %}
This step is no longer required as of Safari 16 on macOS 13. Only complete this step if you want to support older macOS Safari versions.
{% endalert %}

If you wish to support push notifications for Safari on Mac OS X, follow these additional instructions:

- Generate a safari push certificate following the [Registering with Apple](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33) instructions.
- In the Braze dashboard, on the **Settings** page (where your API keys are located), select your Web app. Click **Configure Safari Push** and follow the instructions, uploading the push certificate you just generated.
- When you call `braze.initialize`, supply the optional `safariWebsitePushId` configuration option with the website push ID you used when generating your Safari push certificate. For example `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Safari Mobile push {#safari-mobile}

Safari 16.4+ on iOS and iPadOS supports web push for apps that have been [added to the homescreen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) and have a [Web Application Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) file. After you have completed the steps to integrate web push notifications, you can provide support for mobile push for Safari as well. 

To support mobile Safari web push, follow our [guide here]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

## Soft push prompt

A soft push prompt (also known as a "push primer") helps optimize your opt-in rate when it comes to asking for permission.

Visit [Soft push prompt]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) to learn more about setting up a soft push prompt.

## HTTPS requirement

Web standards require that the domain requesting push notification permission be secure.

### What defines a secure site?

A site is deemed secure if it matches one of the following secure origin patterns:

- (https, , *)
- (wss, *, *)
- (, localhost, )
- (, .localhost, *)
- (, 127/8, )
- (, ::1/128, *)
- (file, *, —)
- (chrome-extension, *, —)

This security requirement in the open standards specification that Braze Web push is built on prevents man-in-the-middle attacks.

### What if a secure site is not available?

While industry best practice is to make your whole site secure, customers who cannot secure their site domain can work around the requirement by using a secure modal. Read more in our guide to using [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) or view a [working demo](http://appboyj.com/modal-test.html).

## Service worker advanced settings

Our service worker file will automatically call `skipWaiting` upon install. If you'd like to avoid this, add the following code to your service worker file, preceding importing Braze:

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Troubleshooting

**I followed the integration instructions, but I'm still not receiving any push notifications.**
- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `braze.isPushSupported()` returns `true` in the browser.
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.

