---
nav_title: Integration
article_title: Push Integration for Web
platform: Web
channel: push
page_order: 0
page_type: reference
description: "This article describes how to integrate Braze Web push via the Braze SDK."

---

# Push integration

A push notification is an alert that appears on the user's screen when an important update occurs. Push notifications can be received even when your web page is not currently open in the user's browser. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your site.

![][27]

Refer to our [push best practices][7] for more resources.

Web push notifications are implemented using the [W3C push standard][1], which browsers are in the process of supporting. Currently, the browsers thats support web push include most versions of Chrome, Firefox, and Opera. Web push is not supported on any iOS browsers to date. It's expected that as the standard becomes more widely adopted, more browsers will continue to implement support. Additionally, desktop Safari (on Mac OS X) has a custom web push solution based on Apple push notification services; Braze supports these Safari notifications.

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

While industry best practice is to make your whole site secure, customers who cannot secure their site domain can work around the requirement by using a secure modal. Read more in our guide to using [Alternate push domain][28] or view a [working demo][4].

## Integration

### Step 1: Configure your site's service worker

- If you don't already have a Service Worker, create a new file named `service-worker.js` with the snippet below, and place it in the root directory of your website.
- Otherwise, if your site already registers a service worker, add the snippet below to the service worker file, and set the [`manageServiceWorkerExternally`]((https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize)) initialization option to `true` when initializing the Web SDK.

```java
self.importScripts('https://js.appboycdn.com/web-sdk/3.5/service-worker.js');
```

{% alert important %}
Your web server must return a `Content-Type: application/javascript` when serving your service worker file. 
{% endalert %}

#### What if I can't register a service worker in the root directory?

By default, a service worker can only be used within the same directory it is registered in. For example, if your service worker file exists in `/assets/service-worker.js`, it would only be possible to register it within `example.com/assets/*` or a subdirectory of the `assets` folder, but not on your homepage (`example.com/`). For this reason, it is recommended to host and register the service worker in the root directory (i.e., `https://example.com/service-worker.js`).

If you cannot register a service worker in your root domain, an alternative approach is to use the [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP header when serving your service worker file. By configuring your server to return `Service-Worker-Allowed: /` in the response for the service worker, this will instruct the browser to broaden the scope and allow it to be used from within a different directory.

### Step 2: Browser registration

For a browser to receive push notifications, you must register it for push by calling `appboy.registerAppboyPushMessages()`. This will immediately request push permission from the user. 

If you wish to show your own push-related UI to the user before requesting push permission (known as a soft push prompt), you can test to see if push is supported in the user's browser with `appboy.isPushSupported()`. Refer to the [soft push prompt example]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) using in-app messages.

If you wish to unsubscribe a user, you can do so by calling `appboy.unregisterAppboyPushMessages()`.

{% alert important %}
Recent versions of Safari and Firefox require that you call this method from a short-lived event handler (e.g., from a button click handler or soft push prompt). This is consistent with [Chrome's user experience best practices](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) for push registration.
{% endalert %}

### Step 3: Configure Safari push

If you wish to support push notifications for Safari on Mac OS X, follow these additional instructions:

- Generate a safari push certificate following the [Registering with Apple][3] instructions.
- In the Braze dashboard, on the **Settings** page (where your API keys are located), select your Web app. Click **Configure Safari Push** and follow the instructions, uploading the push certificate you just generated.
- When you call `appboy.initialize`, supply the optional `safariWebsitePushId` configuration option with the website push ID you used when generating your Safari push certificate. For example `appboy.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Service worker advanced settings

Braze's service worker file will automatically call `skipWaiting` upon install. If you'd like to avoid this, add the following code to your service worker file, above importing Braze:

```javascript
self.addEventListener('install', (event) => {
  event.stopImmediatePropagation();
}); 
self.importScripts('https://js.appboycdn.com/web-sdk/3.4/service-worker.js');
```

## Troubleshooting

**I followed the integration instructions, but I'm still not receiving any push notifications.**
- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `appboy.isPushSupported()` returns `true` in the browser.
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[27]: {{site.baseurl}}/assets/img_archive/web_push2.png
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
