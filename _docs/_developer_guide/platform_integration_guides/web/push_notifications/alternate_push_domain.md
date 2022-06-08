---
nav_title: Alternate Web Push Domain
article_title: Alternate Web Push Domain
platform: Web
page_order: 20
page_type: reference
description: "This article covers how to integrate Braze Web Push on an alternate domain."
channel: push

---

# Alternate web push domain

To integrate web push, your domain must be [secure][2], which generally means `https`, `localhost`, and other exceptions as defined in the [W3C push standard][1]. You'll also need to be able to register a Service Worker at the root of your domain, or at least be able to control the HTTP headers for that file.

_If you aren't able to meet all of those criteria_, use this guide to set up a workaround that lets you add a push prompt dialog to your website. For example, this article would be helpful if you want the user to opt-in from an `http` (insecure) website or from a browser extension popup that prevents the push prompt from displaying.

## Caveats
Keep in mind that like many workarounds on the web, browsers continually evolve, and in the future, this may not work as intended.

- This requires that:
  - You own a separate secure domain (`https://`) and have access to register a Service Worker on that domain.
  - Users to be logged in to your website to ensure that push tokens are tied to the same profiles.

{% alert note %}
Push for Shopify is unable to be implemented in this way. Shopify takes steps to remove headers that are required to deliver push.
{% endalert %}

## Integration

To make the following example clear, we'll use use `http://insecure.com` and `https://secure.com` as our two domains with the goal of getting visitors to register for push on `http://insecure.com`. This example could also be applied to a `chrome-extension://` scheme for a browser extension's popup page.

### Step 1: Initiate prompting flow

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

### Step 2: Register for push

At this point, `secure.com` will open a popup window in which you can initialize the Braze Web SDK for the same user ID and request the user's permission for Web push.

**https://secure.com/push-registration.html**
```html
<html>
    <head>
        <title>Opt-In for Push</title>
        <script src="https://js.appboycdn.com/web-sdk/4.0/braze.min.js"></script>
    </head>
    <body>
    <button id="opt-in">Opt In For Push</button>
    <script>
        // initialize Braze
        braze.initialize("YOUR-API-KEY", {
            baseUrl: "YOUR-SDK-BASE-URL",
            enableLogging: true
        });
        // parse the `external_id` from the URL parameters
        const external_id = (location.search.substring(1).split('&').find(param => param.startsWith('external_id=')) || '').split('=')[1] || '';
        if (external_id) {
            braze.changeUser(external_id);
        }
        braze.automaticallyShowInAppMessages();
        braze.openSession();

        // when the user click's our Opt In button, prompt for permission
        document.getElementById("opt-in").onclick = function(){
            braze.requestPushPermission(() => {
                window.alert(`You are registered for push!`);
                window.close();
            }, () => {
                window.alert(`Something went wrong.`);
            });
        };
    </script>
    </body>
</html>
```

### Step 3: Communicate between domains (optional)

Now that users can opt-in from this workflow originating on `insecure.com`, you may want to modify your site based on if the user is already opted-in or not. There's no point in asking the user to register for push if they already are.

You can use iFrames and the [`postMessage`][3] API to communicate between your two domains. 

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

```html
<script src="https://js.appboycdn.com/web-sdk/4.0/braze.min.js"></script>
<script>
// initialize Braze
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-SDK-BASE-URL",
    enableLogging: true
});

// listen for a request from our insecure page
window.addEventListener("message", (event) => {
    if (event.origin === "http://insecure.com") {
        // when they ask for push status, retrieve from Braze SDK
        if (event.data.type === 'get_push_status') {
            // send the parent window (insecure.com) the results
            window.top.postMessage({
                type: 'set_push_status',
                isPushPermissionGranted: braze.isPushPermissionGranted()
            }, event.origin);
        }
    }
});
</script>
```

[1]: https://www.w3.org/TR/service-workers/#security-considerations
[2]: https://w3c.github.io/webappsec-secure-contexts/
[3]: https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
