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

---

# Push integration

A push notification is an alert that appears on the user's screen when an important update occurs. Push notifications can be received even when your web page is not currently open in the user's browser. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your site.

![][27]

Refer to our [push best practices][7] for more resources.

Web push notifications are implemented using the [W3C push standard][1], which browsers are in the process of supporting. Currently, the browsers thats support web push include most versions of Chrome, Firefox, and Opera. Web push is not supported on any iOS browsers to date. It's expected that as the standard becomes more widely adopted, more browsers will continue to implement support. Additionally, desktop Safari (on Mac OS X) has a custom web push solution based on Apple push notification services; Braze supports these Safari notifications.

{% include archive/web-v4-rename.md %}

## Integration

### Step 1: Configure your site's service worker

- If you don't already have a Service Worker, create a new file named `service-worker.js` with the following snippet, and place it in the root directory of your website.
- Otherwise, if your site already registers a service worker, add the following snippet to the service worker file, and set the [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) initialization option to `true` when initializing the Web SDK.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

If your service worker filename is not `service-worker.js`, you must use the `serviceWorkerLocation` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

{% alert important %}
Your web server must return a `Content-Type: application/javascript` when serving your service worker file. 
{% endalert %}

#### What if I can't register a service worker in the root directory?

By default, a service worker can only be used within the same directory it is registered in. For example, if your service worker file exists in `/assets/service-worker.js`, it would only be possible to register it within `example.com/assets/*` or a subdirectory of the `assets` folder, but not on your homepage (`example.com/`). For this reason, it is recommended to host and register the service worker in the root directory (i.e., `https://example.com/service-worker.js`).

If you cannot register a service worker in your root domain, an alternative approach is to use the [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP header when serving your service worker file. By configuring your server to return `Service-Worker-Allowed: /` in the response for the service worker, this will instruct the browser to broaden the scope and allow it to be used from within a different directory.

### Step 2: Browser registration

For a browser to receive push notifications, you must register it for push by calling `braze.requestPushPermission()`. This will immediately request push permission from the user. 

If you wish to show your own push-related UI to the user before requesting push permission (known as a soft push prompt), you can test to see if push is supported in the user's browser with `braze.isPushSupported()`. Refer to the [soft push prompt example]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) using in-app messages.

If you wish to unsubscribe a user, you can do so by calling `braze.unregisterPush()`.

{% alert important %}
Recent versions of Safari and Firefox require that you call this method from a short-lived event handler (e.g., from a button click handler or soft push prompt). This is consistent with [Chrome's user experience best practices](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) for push registration.
{% endalert %}

### Step 3: Configure Safari push

If you wish to support push notifications for Safari on Mac OS X, follow these additional instructions:

- Generate a safari push certificate following the [Registering with Apple][3] instructions.
- In the Braze dashboard, on the **Settings** page (where your API keys are located), select your Web app. Click **Configure Safari Push** and follow the instructions, uploading the push certificate you just generated.
- When you call `braze.initialize`, supply the optional `safariWebsitePushId` configuration option with the website push ID you used when generating your Safari push certificate. For example `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Soft push prompt

It's often a good idea for sites to implement a "soft" push prompt where you "prime" the user and make your case for sending them push notifications before requesting push permission. This is useful because the browser throttles how often you may prompt the user directly, and if the user denies permission you can never ask them again. This can be done simply through Braze's [triggered in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) for a seamless user experience. Instead of calling `braze.requestPushPermission()` directly as described above, instead:

1. Create a "Prime for Push" in-app messaging campaign on the Braze dashboard.
  - Make it a **Modal** in-app message. Give it whatever text and styling you wish to present to the user ("Can we stay in touch?").
  - Give the in-app message a Button 1 Text value of "OK" (or whatever affirmative text you wish), and set the on-click behavior to "Close Message." You'll customize that behavior later.
  - Under the gear composer section, add a key-value pair. Give it a key of `msg-id` and a value of `push-primer`.
  - Give the message a trigger action of the custom event 'prime-for-push' (you can create that custom event manually from the dashboard if you need to).<br><br>
2. In your Braze SDK integration, find and remove any calls to `braze.automaticallyShowInAppMessages()` from within your loading snippet.<br><br>
3. Replace the removed call with the following snippet:

```javascript

// Be sure to remove calls to braze.automaticallyShowInAppMessages() 
// from your code as noted in the steps above

braze.subscribeToInAppMessage(function(inAppMessage) {
  var shouldDisplay = true;

  if (inAppMessage instanceof braze.InAppMessage) {
    // Read the key-value pair for msg-id
    var msgId = inAppMessage.extras["msg-id"];

    // If this is our push primer message
    if (msgId == "push-primer") {
      // We don't want to display the soft push prompt to users on browsers that don't support push, or if the user
      // has already granted/blocked permission
      if (!braze.isPushSupported() || braze.isPushPermissionGranted() || braze.isPushBlocked()) {
        shouldDisplay = false;
      }
      if (inAppMessage.buttons[0] != null) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission();
        });
      }
    }
  }

  // Display the message
  if (shouldDisplay) {
    braze.showInAppMessage(inAppMessage);
  }
});
```

When you wish to display the soft push prompt to the user, call `braze.logCustomEvent("prime-for-push")` - for instance, to prompt the user on every page load just after the Braze session begins, your code would look like:

```javascript
braze.openSession();
braze.logCustomEvent("prime-for-push");
```

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

## Service Worker advanced settings

Braze's service worker file will automatically call `skipWaiting` upon install. If you'd like to avoid this, add the following code to your service worker file, preceding importing Braze:

```javascript
self.addEventListener('install', (event) => {
  event.stopImmediatePropagation();
}); 
self.importScripts('https://js.appboycdn.com/web-sdk/4.0/service-worker.js');
```

## Troubleshooting

**I followed the integration instructions, but I'm still not receiving any push notifications.**
- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `braze.isPushSupported()` returns `true` in the browser.
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[27]: {{site.baseurl}}/assets/img_archive/web_push2.png
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
