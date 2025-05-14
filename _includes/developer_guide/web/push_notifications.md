{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Push protocols

Web push notifications are implemented using the [W3C push standard](http://www.w3.org/TR/push-api/), which most major browsers support. For more information on specific push protocol standards and browser support, you can review resources from [Apple](https://developer.apple.com/notifications/safari-push-notifications/) [Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) and [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/).

## Setting up push notifications

### Step 1: Configure your service worker

In your project's `service-worker.js` file, add the following snippet and set the [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) initialization option to `true` when initializing the Web SDK.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Your web server must return a `Content-Type: application/javascript` when serving your service worker file. Additionally, if your service worker file is not `service-worker.js` named, you'll need to use the `serviceWorkerLocation` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).
{% endalert %}

### Step 2: Register the browser

To immediately request push permissions from a user so their browser can receive push notifications, call `braze.requestPushPermission()`. To test if push is supported in their browser first, call `braze.isPushSupported()`.

You can also [send a soft push prompt]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web) to the user before requesting push permission to show your own push-related UI.

{% alert important %}
On macOS, both **Google Chrome** and **Google Chrome Helper (Alerts)** must be enabled by the end-user in **System Settings > Notifications** before push notifications can be displayed&#8212;even if permissions are granted.
{% endalert %}

### Step 3: Disable `skipWaiting` (optional)

The Braze service worker file will automatically call `skipWaiting` upon install. If you'd like to disable this functionality, add the following code to your service worker file, after importing Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Unsubscribing a user

To unsubscribe a user, call `braze.unregisterPush()`.

{% alert important %}
Recent versions of Safari and Firefox require that you call this method from a short-lived event handler (such as from a button-click handler or soft push prompt). This is consistent with [Chrome's user experience best practices](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) for push registration.
{% endalert %}

## Alternate domains

To integrate web push, your domain must be [secure](https://w3c.github.io/webappsec-secure-contexts/), which generally means `https`, `localhost`, and other exceptions as defined in the [W3C push standard](https://www.w3.org/TR/service-workers/#security-considerations). You'll also need to be able to register a Service Worker at the root of your domain, or at least be able to control the HTTP headers for that file. This article covers how to integrate Braze Web Push on an alternate domain.

### Use cases

If you can't meet all of the criteria outlined in the [W3C push standard](https://www.w3.org/TR/service-workers/#security-considerations), you can use this method to add a push prompt dialog to your website instead. This can be helpful if you want to let your users opt-in from an `http` website or a browser extension popup that's preventing your push prompt from displaying.

### Considerations

Keep in mind, like many workarounds on the web, browsers continually evolve, and this method may not be viable in the future. Before continuing, ensure that:

- You own a separate secure domain (`https://`) and permissions to register a Service Worker on that domain.
- Users are logged in to your website which ensures push tokens are match to the correct profile.

{% alert important %}
You cannot use this method to implement push notifications for Shopify. Shopify will automatically remove the headers need to deliver push this way.
{% endalert %}

### Setting up an alternate push domain

To make the following example clear, we'll use use `http://insecure.com` and `https://secure.com` as our two domains with the goal of getting visitors to register for push on `http://insecure.com`. This example could also be applied to a `chrome-extension://` scheme for a browser extension's popup page.

#### Step 1: Initiate prompting flow

On `insecure.com`, open a new window to your secure domain using a URL parameter to pass the currently logged-in user's Braze external ID.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### Step 2: Register for push

At this point, `secure.com` will open a popup window in which you can initialize the Braze Web SDK for the same user ID and request the user's permission for Web push.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Step 3: Communicate between domains (optional)

Now that users can opt-in from this workflow originating on `insecure.com`, you may want to modify your site based on if the user is already opted-in or not. There's no point in asking the user to register for push if they already are.

You can use iFrames and the [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API to communicate between your two domains. 

**insecure.com**

On our `insecure.com` domain, we will ask the secure domain (where push is _actually_ registered) for information on the current user's push registration:

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

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
