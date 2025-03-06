---
page_order: 1
nav_title: Push Notifications
description: "Learn how to set up push notifications for the Braze Web SDK."
---

# Push notifications

> A push notification is an alert that appears on the user's screen when an important update occurs. Push notifications can be received even when your web page is not currently open in the user's browser. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your site. To fully leverage push notifications, see [Push best practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

{% multi_lang_include archive/web-v4-rename.md %}

## Push protocols

Web push notifications are implemented using the [W3C push standard](http://www.w3.org/TR/push-api/), which most major browsers support. For more information on specific push protocol standards and browser support, you can review resources from [Apple](https://developer.apple.com/notifications/safari-push-notifications/ "Safari Push Notifications") [Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla Push API browser compatibility") and [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft Push API").

## Setting up push notifications

### Prerequisites

Before you can set up push notifications, you'll need to [integrate the Braze Web SDK]({{site.baseurl}}/developer_guide/platforms/web/sdk_integration/) into your app.

### Step 1: Configure your service worker

- If you don't already have a service worker, create a new file named `service-worker.js` with the following snippet, and place it in the root directory of your website.
- Otherwise, if your site already registers a service worker, add the following snippet to the service worker file, and set the [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) initialization option to `true` when initializing the Web SDK.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

If your service worker filename is not `service-worker.js`, you must use the `serviceWorkerLocation` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

{% alert important %}
Your web server must return a `Content-Type: application/javascript` when serving your service worker file. 
{% endalert %}

### Step 2: Register your browser

For a browser to receive push notifications, you must register it for push by calling `braze.requestPushPermission()`. This will immediately request push permission from the user. 

If you wish to show your own push-related UI to the user before requesting push permission (known as a soft push prompt), you can test to see if push is supported in the user's browser with `braze.isPushSupported()`. Refer to the [soft push prompt example]({{site.baseurl}}/developer_guide/platforms/web/push_notifications/soft_push_prompts/) using in-app messages.

If you wish to unsubscribe a user, you can do so by calling `braze.unregisterPush()`.

{% alert important %}
Recent versions of Safari and Firefox require that you call this method from a short-lived event handler (for example, from a button click handler or soft push prompt). This is consistent with [Chrome's user experience best practices](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) for push registration.
{% endalert %}

### Step 3: Disable `skipWaiting` (optional)

The Braze service worker file will automatically call `skipWaiting` upon install. If you'd like to disable this functionality, add the following code to your service worker file, after importing Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Troubleshooting

If you're experiencing issues after setting up push notifications, consider the following:

- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `braze.isPushSupported()` returns `true` in the browser.
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.

## Frequently Asked Questions (FAQ)

### Service workers

#### What if I can't register a service worker in the root directory?

By default, a service worker can only be used within the same directory it is registered in. For example, if your service worker file exists in `/assets/service-worker.js`, it would only be possible to register it within `example.com/assets/*` or a subdirectory of the `assets` folder, but not on your homepage (`example.com/`). For this reason, it is recommended to host and register the service worker in the root directory (such as `https://example.com/service-worker.js`).

If you cannot register a service worker in your root domain, an alternative approach is to use the [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP header when serving your service worker file. By configuring your server to return `Service-Worker-Allowed: /` in the response for the service worker, this will instruct the browser to broaden the scope and allow it to be used from within a different directory.

#### Can I create a service worker using a Tag Manager?

No, service workers must be hosted on your website's server and can't be loaded via Tag Manager.

### Site security

#### Is HTTPS required?

Yes. Web standards require that the domain requesting push notification permission be secure.

#### When is a site considered "secure"?

A site is considered secure if it matches one of the following secure-origin patterns. Braze Web push notifications are built on this open standard, so man-in-the-middle attacks are prevented.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### What if a secure site is not available?

While industry best practice is to make your whole site secure, customers who cannot secure their site domain can work around the requirement by using a secure modal. Read more in our guide to using [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) or view a [working demo](http://appboyj.com/modal-test.html).
